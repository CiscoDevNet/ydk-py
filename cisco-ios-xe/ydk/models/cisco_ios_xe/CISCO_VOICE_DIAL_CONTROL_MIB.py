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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CvAmrNbRtpEncap(Enum):
    """
    CvAmrNbRtpEncap (Enum Class)

    Represents GSM AMR\-NB codec RTP encapsulation type.

    .. data:: rfc3267 = 1

    """

    rfc3267 = Enum.YLeaf(1, "rfc3267")


class CvCallConnectionType(Enum):
    """
    CvCallConnectionType (Enum Class)

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


class CvCallVolumeStatsIntvlType(Enum):
    """
    CvCallVolumeStatsIntvlType (Enum Class)

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


class CvCallVolumeWMIntvlType(Enum):
    """
    CvCallVolumeWMIntvlType (Enum Class)

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


class CvIlbcFrameMode(Enum):
    """
    CvIlbcFrameMode (Enum Class)

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


class CvSessionProtocol(Enum):
    """
    CvSessionProtocol (Enum Class)

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



class CISCOVOICEDIALCONTROLMIB(Entity):
    """
    
    
    .. attribute:: cvgeneralconfiguration
    
    	
    	**type**\:  :py:class:`Cvgeneralconfiguration <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvgeneralconfiguration>`
    
    .. attribute:: cvgatewaycallactive
    
    	
    	**type**\:  :py:class:`Cvgatewaycallactive <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvgatewaycallactive>`
    
    .. attribute:: cvcallvolume
    
    	
    	**type**\:  :py:class:`Cvcallvolume <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvolume>`
    
    .. attribute:: cvcallratemonitor
    
    	
    	**type**\:  :py:class:`Cvcallratemonitor <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallratemonitor>`
    
    .. attribute:: cvcallvolumestatshistory
    
    	
    	**type**\:  :py:class:`Cvcallvolumestatshistory <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvolumestatshistory>`
    
    .. attribute:: cvpeercfgtable
    
    	The table contains the Voice Generic Peer information that is used to create an ifIndexed row with an appropriate ifType that is associated with the cvPeerCfgType and cvPeerCfgPeerType objects
    	**type**\:  :py:class:`Cvpeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable>`
    
    .. attribute:: cvvoicepeercfgtable
    
    	The table contains the Voice over Telephony peer specific information that is required to accept voice calls or to which it will place them or perform various loopback tests via interface
    	**type**\:  :py:class:`Cvvoicepeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable>`
    
    .. attribute:: cvvoippeercfgtable
    
    	The table contains the Voice over IP (VoIP) peer specific information that is required to accept voice calls or to which it will place them via IP backbone with the specified session protocol in cvVoIPPeerCfgSessionProtocol
    	**type**\:  :py:class:`Cvvoippeercfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable>`
    
    .. attribute:: cvpeercommoncfgtable
    
    	The table contains the Voice specific peer common configuration information that is required to accept voice calls or to which it will place them or process the incoming calls
    	**type**\:  :py:class:`Cvpeercommoncfgtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable>`
    
    .. attribute:: cvcallactivetable
    
    	This table is the voice extension to the call active table of IETF Dial Control MIB. It contains voice encapsulation call leg information that is derived from the statistics of lower layer telephony interface
    	**type**\:  :py:class:`Cvcallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallactivetable>`
    
    .. attribute:: cvvoipcallactivetable
    
    	This table is the VoIP extension to the call active table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\:  :py:class:`Cvvoipcallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable>`
    
    .. attribute:: cvcallvolconntable
    
    	This table represents the number of active call connections for each call connection type in the voice gateway
    	**type**\:  :py:class:`Cvcallvolconntable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable>`
    
    .. attribute:: cvcallvoliftable
    
    	This table represents the information about the usage of an IP interface in a voice gateway for voice media calls. This table has a sparse\-dependent relationship with   ifTable. There exists an entry in this table,  for each of the  entries in ifTable where ifType  is one of 'ethernetCsmacd' and 'softwareLoopback'
    	**type**\:  :py:class:`Cvcallvoliftable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable>`
    
    .. attribute:: cvcallhistorytable
    
    	This table is the voice extension to the call history table of IETF Dial Control MIB. It contains voice encapsulation call leg information such as voice packet statistics, coder usage and end to end bandwidth of the call leg
    	**type**\:  :py:class:`Cvcallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable>`
    
    .. attribute:: cvvoipcallhistorytable
    
    	This table is the VoIP extension to the call history table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\:  :py:class:`Cvvoipcallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable>`
    
    .. attribute:: cvcallratestatstable
    
    	This table represents voice call rate measurement in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:  :py:class:`Cvcallratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable>`
    
    .. attribute:: cvcalllegratestatstable
    
    	cvCallLegRateStatsTable table represents voice call leg rate measurement in various interval lengths defined by  the CvCallVolumeStatsIntvlType object. Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:  :py:class:`Cvcalllegratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable>`
    
    .. attribute:: cvactivecallstatstable
    
    	This table represents the active voice calls in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:  :py:class:`Cvactivecallstatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable>`
    
    .. attribute:: cvcalldurationstatstable
    
    	This table represents the number of calls below a specific duration in various interval length defined by  the CvCallVolumeStatsIntvlType object.    The specific duration is configurable value of   cvCallDurationStatsThreshold object.  Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:  :py:class:`Cvcalldurationstatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable>`
    
    .. attribute:: cvsipmsgratestatstable
    
    	This table represents the SIP message rate measurement in various interval length defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:  :py:class:`Cvsipmsgratestatstable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable>`
    
    .. attribute:: cvcallratewmtable
    
    	This table represents high watermarks achieved by call rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:  :py:class:`Cvcallratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable>`
    
    .. attribute:: cvcalllegratewmtable
    
    	cvCallLegRateWMTable table represents high watermarks achieved by call\-leg rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\:  :py:class:`Cvcalllegratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable>`
    
    .. attribute:: cvactivecallwmtable
    
    	This table represents high watermarks achieved by active calls in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow  for detailed measurement to be collected
    	**type**\:  :py:class:`Cvactivecallwmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable>`
    
    .. attribute:: cvsipmsgratewmtable
    
    	This table represents of high watermarks achieved by SIP message rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\:  :py:class:`Cvsipmsgratewmtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable>`
    
    

    """

    _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
    _revision = '2012-05-15'

    def __init__(self):
        super(CISCOVOICEDIALCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cvGeneralConfiguration", ("cvgeneralconfiguration", CISCOVOICEDIALCONTROLMIB.Cvgeneralconfiguration)), ("cvGatewayCallActive", ("cvgatewaycallactive", CISCOVOICEDIALCONTROLMIB.Cvgatewaycallactive)), ("cvCallVolume", ("cvcallvolume", CISCOVOICEDIALCONTROLMIB.Cvcallvolume)), ("cvCallRateMonitor", ("cvcallratemonitor", CISCOVOICEDIALCONTROLMIB.Cvcallratemonitor)), ("cvCallVolumeStatsHistory", ("cvcallvolumestatshistory", CISCOVOICEDIALCONTROLMIB.Cvcallvolumestatshistory)), ("cvPeerCfgTable", ("cvpeercfgtable", CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable)), ("cvVoicePeerCfgTable", ("cvvoicepeercfgtable", CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable)), ("cvVoIPPeerCfgTable", ("cvvoippeercfgtable", CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable)), ("cvPeerCommonCfgTable", ("cvpeercommoncfgtable", CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable)), ("cvCallActiveTable", ("cvcallactivetable", CISCOVOICEDIALCONTROLMIB.Cvcallactivetable)), ("cvVoIPCallActiveTable", ("cvvoipcallactivetable", CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable)), ("cvCallVolConnTable", ("cvcallvolconntable", CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable)), ("cvCallVolIfTable", ("cvcallvoliftable", CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable)), ("cvCallHistoryTable", ("cvcallhistorytable", CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable)), ("cvVoIPCallHistoryTable", ("cvvoipcallhistorytable", CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable)), ("cvCallRateStatsTable", ("cvcallratestatstable", CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable)), ("cvCallLegRateStatsTable", ("cvcalllegratestatstable", CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable)), ("cvActiveCallStatsTable", ("cvactivecallstatstable", CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable)), ("cvCallDurationStatsTable", ("cvcalldurationstatstable", CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable)), ("cvSipMsgRateStatsTable", ("cvsipmsgratestatstable", CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable)), ("cvCallRateWMTable", ("cvcallratewmtable", CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable)), ("cvCallLegRateWMTable", ("cvcalllegratewmtable", CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable)), ("cvActiveCallWMTable", ("cvactivecallwmtable", CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable)), ("cvSipMsgRateWMTable", ("cvsipmsgratewmtable", CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cvgeneralconfiguration = CISCOVOICEDIALCONTROLMIB.Cvgeneralconfiguration()
        self.cvgeneralconfiguration.parent = self
        self._children_name_map["cvgeneralconfiguration"] = "cvGeneralConfiguration"
        self._children_yang_names.add("cvGeneralConfiguration")

        self.cvgatewaycallactive = CISCOVOICEDIALCONTROLMIB.Cvgatewaycallactive()
        self.cvgatewaycallactive.parent = self
        self._children_name_map["cvgatewaycallactive"] = "cvGatewayCallActive"
        self._children_yang_names.add("cvGatewayCallActive")

        self.cvcallvolume = CISCOVOICEDIALCONTROLMIB.Cvcallvolume()
        self.cvcallvolume.parent = self
        self._children_name_map["cvcallvolume"] = "cvCallVolume"
        self._children_yang_names.add("cvCallVolume")

        self.cvcallratemonitor = CISCOVOICEDIALCONTROLMIB.Cvcallratemonitor()
        self.cvcallratemonitor.parent = self
        self._children_name_map["cvcallratemonitor"] = "cvCallRateMonitor"
        self._children_yang_names.add("cvCallRateMonitor")

        self.cvcallvolumestatshistory = CISCOVOICEDIALCONTROLMIB.Cvcallvolumestatshistory()
        self.cvcallvolumestatshistory.parent = self
        self._children_name_map["cvcallvolumestatshistory"] = "cvCallVolumeStatsHistory"
        self._children_yang_names.add("cvCallVolumeStatsHistory")

        self.cvpeercfgtable = CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable()
        self.cvpeercfgtable.parent = self
        self._children_name_map["cvpeercfgtable"] = "cvPeerCfgTable"
        self._children_yang_names.add("cvPeerCfgTable")

        self.cvvoicepeercfgtable = CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable()
        self.cvvoicepeercfgtable.parent = self
        self._children_name_map["cvvoicepeercfgtable"] = "cvVoicePeerCfgTable"
        self._children_yang_names.add("cvVoicePeerCfgTable")

        self.cvvoippeercfgtable = CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable()
        self.cvvoippeercfgtable.parent = self
        self._children_name_map["cvvoippeercfgtable"] = "cvVoIPPeerCfgTable"
        self._children_yang_names.add("cvVoIPPeerCfgTable")

        self.cvpeercommoncfgtable = CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable()
        self.cvpeercommoncfgtable.parent = self
        self._children_name_map["cvpeercommoncfgtable"] = "cvPeerCommonCfgTable"
        self._children_yang_names.add("cvPeerCommonCfgTable")

        self.cvcallactivetable = CISCOVOICEDIALCONTROLMIB.Cvcallactivetable()
        self.cvcallactivetable.parent = self
        self._children_name_map["cvcallactivetable"] = "cvCallActiveTable"
        self._children_yang_names.add("cvCallActiveTable")

        self.cvvoipcallactivetable = CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable()
        self.cvvoipcallactivetable.parent = self
        self._children_name_map["cvvoipcallactivetable"] = "cvVoIPCallActiveTable"
        self._children_yang_names.add("cvVoIPCallActiveTable")

        self.cvcallvolconntable = CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable()
        self.cvcallvolconntable.parent = self
        self._children_name_map["cvcallvolconntable"] = "cvCallVolConnTable"
        self._children_yang_names.add("cvCallVolConnTable")

        self.cvcallvoliftable = CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable()
        self.cvcallvoliftable.parent = self
        self._children_name_map["cvcallvoliftable"] = "cvCallVolIfTable"
        self._children_yang_names.add("cvCallVolIfTable")

        self.cvcallhistorytable = CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable()
        self.cvcallhistorytable.parent = self
        self._children_name_map["cvcallhistorytable"] = "cvCallHistoryTable"
        self._children_yang_names.add("cvCallHistoryTable")

        self.cvvoipcallhistorytable = CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable()
        self.cvvoipcallhistorytable.parent = self
        self._children_name_map["cvvoipcallhistorytable"] = "cvVoIPCallHistoryTable"
        self._children_yang_names.add("cvVoIPCallHistoryTable")

        self.cvcallratestatstable = CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable()
        self.cvcallratestatstable.parent = self
        self._children_name_map["cvcallratestatstable"] = "cvCallRateStatsTable"
        self._children_yang_names.add("cvCallRateStatsTable")

        self.cvcalllegratestatstable = CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable()
        self.cvcalllegratestatstable.parent = self
        self._children_name_map["cvcalllegratestatstable"] = "cvCallLegRateStatsTable"
        self._children_yang_names.add("cvCallLegRateStatsTable")

        self.cvactivecallstatstable = CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable()
        self.cvactivecallstatstable.parent = self
        self._children_name_map["cvactivecallstatstable"] = "cvActiveCallStatsTable"
        self._children_yang_names.add("cvActiveCallStatsTable")

        self.cvcalldurationstatstable = CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable()
        self.cvcalldurationstatstable.parent = self
        self._children_name_map["cvcalldurationstatstable"] = "cvCallDurationStatsTable"
        self._children_yang_names.add("cvCallDurationStatsTable")

        self.cvsipmsgratestatstable = CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable()
        self.cvsipmsgratestatstable.parent = self
        self._children_name_map["cvsipmsgratestatstable"] = "cvSipMsgRateStatsTable"
        self._children_yang_names.add("cvSipMsgRateStatsTable")

        self.cvcallratewmtable = CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable()
        self.cvcallratewmtable.parent = self
        self._children_name_map["cvcallratewmtable"] = "cvCallRateWMTable"
        self._children_yang_names.add("cvCallRateWMTable")

        self.cvcalllegratewmtable = CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable()
        self.cvcalllegratewmtable.parent = self
        self._children_name_map["cvcalllegratewmtable"] = "cvCallLegRateWMTable"
        self._children_yang_names.add("cvCallLegRateWMTable")

        self.cvactivecallwmtable = CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable()
        self.cvactivecallwmtable.parent = self
        self._children_name_map["cvactivecallwmtable"] = "cvActiveCallWMTable"
        self._children_yang_names.add("cvActiveCallWMTable")

        self.cvsipmsgratewmtable = CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable()
        self.cvsipmsgratewmtable.parent = self
        self._children_name_map["cvsipmsgratewmtable"] = "cvSipMsgRateWMTable"
        self._children_yang_names.add("cvSipMsgRateWMTable")
        self._segment_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB"


    class Cvgeneralconfiguration(Entity):
        """
        
        
        .. attribute:: cvgeneralpoorqovnotificationenable
        
        	This object indicates whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for a poor quality of voice calls.  If the value of this object is 'true', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated for all voice over IP peers when a poor quality of voice call condition is detected after the voice gateway call disconnection.  If the value of this object is 'false', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated only for calls for which the cvVoIPPeerCfgPoorQoVNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        .. attribute:: cvgeneralfallbacknotificationenable
        
        	This object indicates whether cvdcFallbackNotification traps should be generated for fallback. If the value of this object is 'true', cvdcFallbackNotification traps will be generated for all voice over IP peers
        	**type**\: bool
        
        .. attribute:: cvgeneraldscppolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for a RPH to DSCP mapping violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when a RPH to DSCP violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgDSCPPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        .. attribute:: cvgeneralmediapolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for Media violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when media violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgMediaPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvgeneralconfiguration, self).__init__()

            self.yang_name = "cvGeneralConfiguration"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvgeneralpoorqovnotificationenable', YLeaf(YType.boolean, 'cvGeneralPoorQoVNotificationEnable')),
                ('cvgeneralfallbacknotificationenable', YLeaf(YType.boolean, 'cvGeneralFallbackNotificationEnable')),
                ('cvgeneraldscppolicynotificationenable', YLeaf(YType.boolean, 'cvGeneralDSCPPolicyNotificationEnable')),
                ('cvgeneralmediapolicynotificationenable', YLeaf(YType.boolean, 'cvGeneralMediaPolicyNotificationEnable')),
            ])
            self.cvgeneralpoorqovnotificationenable = None
            self.cvgeneralfallbacknotificationenable = None
            self.cvgeneraldscppolicynotificationenable = None
            self.cvgeneralmediapolicynotificationenable = None
            self._segment_path = lambda: "cvGeneralConfiguration"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvgeneralconfiguration, ['cvgeneralpoorqovnotificationenable', 'cvgeneralfallbacknotificationenable', 'cvgeneraldscppolicynotificationenable', 'cvgeneralmediapolicynotificationenable'], name, value)


    class Cvgatewaycallactive(Entity):
        """
        
        
        .. attribute:: cvcallactiveds0s
        
        	The current number of DS0 interfaces used for the active calls
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: interfaces
        
        .. attribute:: cvcallactiveds0shighthreshold
        
        	A high threshold used to determine when to generate the cvdcActiveDS0sHighNotification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\: int
        
        	**range:** 0..100
        
        	**units**\: percent
        
        .. attribute:: cvcallactiveds0slowthreshold
        
        	A low threshold used to determine when to generate the cvdcActiveDS0sLowNotification notification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\: int
        
        	**range:** 0..100
        
        	**units**\: percent
        
        .. attribute:: cvcallactiveds0shighnotifyenable
        
        	Specifies whether or not cvdcActiveDS0sHighNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sHighNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sHighNotification          generation is disabled
        	**type**\: bool
        
        .. attribute:: cvcallactiveds0slownotifyenable
        
        	Specifies whether or not cvdcActiveDS0sLowNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sLowNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sLowNotification          generation is disabled
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvgatewaycallactive, self).__init__()

            self.yang_name = "cvGatewayCallActive"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvcallactiveds0s', YLeaf(YType.uint32, 'cvCallActiveDS0s')),
                ('cvcallactiveds0shighthreshold', YLeaf(YType.uint32, 'cvCallActiveDS0sHighThreshold')),
                ('cvcallactiveds0slowthreshold', YLeaf(YType.uint32, 'cvCallActiveDS0sLowThreshold')),
                ('cvcallactiveds0shighnotifyenable', YLeaf(YType.boolean, 'cvCallActiveDS0sHighNotifyEnable')),
                ('cvcallactiveds0slownotifyenable', YLeaf(YType.boolean, 'cvCallActiveDS0sLowNotifyEnable')),
            ])
            self.cvcallactiveds0s = None
            self.cvcallactiveds0shighthreshold = None
            self.cvcallactiveds0slowthreshold = None
            self.cvcallactiveds0shighnotifyenable = None
            self.cvcallactiveds0slownotifyenable = None
            self._segment_path = lambda: "cvGatewayCallActive"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvgatewaycallactive, ['cvcallactiveds0s', 'cvcallactiveds0shighthreshold', 'cvcallactiveds0slowthreshold', 'cvcallactiveds0shighnotifyenable', 'cvcallactiveds0slownotifyenable'], name, value)


    class Cvcallvolume(Entity):
        """
        
        
        .. attribute:: cvcallvolconntotalactiveconnections
        
        	This object represents the total number of active call legs in the voice gateway
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallvolconnmaxcallconnectionlicenese
        
        	This object represents the licensed call capacity for a voice gateway.  If the value is 0, no  licensing is done and the gateway can be  accomodate as many calls depending on its capability
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallvolume, self).__init__()

            self.yang_name = "cvCallVolume"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvcallvolconntotalactiveconnections', YLeaf(YType.uint32, 'cvCallVolConnTotalActiveConnections')),
                ('cvcallvolconnmaxcallconnectionlicenese', YLeaf(YType.uint32, 'cvCallVolConnMaxCallConnectionLicenese')),
            ])
            self.cvcallvolconntotalactiveconnections = None
            self.cvcallvolconnmaxcallconnectionlicenese = None
            self._segment_path = lambda: "cvCallVolume"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvolume, ['cvcallvolconntotalactiveconnections', 'cvcallvolconnmaxcallconnectionlicenese'], name, value)


    class Cvcallratemonitor(Entity):
        """
        
        
        .. attribute:: cvcallratemonitorenable
        
        	This object represents the state of call\-monitoring. A value of 'true' indicates that call\-monitoring  is enabled.  A value of 'false' indicates that  call\-monitoring is disabled
        	**type**\: bool
        
        .. attribute:: cvcallratemonitortime
        
        	This object represents the interval for which the gateway monitors the call\-rate
        	**type**\: int
        
        	**range:** 1..12
        
        	**units**\: five seconds
        
        .. attribute:: cvcallrate
        
        	This object represents the total number of calls handled by the gateway during the  monitored time
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallratehiwatermark
        
        	This object represents the high water mark for the number of calls handled by the  gateway in an unit interval of  cvCallRateMonitorTime, from the time  the call\-monitoring is enabled
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallratemonitor, self).__init__()

            self.yang_name = "cvCallRateMonitor"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvcallratemonitorenable', YLeaf(YType.boolean, 'cvCallRateMonitorEnable')),
                ('cvcallratemonitortime', YLeaf(YType.uint32, 'cvCallRateMonitorTime')),
                ('cvcallrate', YLeaf(YType.uint32, 'cvCallRate')),
                ('cvcallratehiwatermark', YLeaf(YType.uint32, 'cvCallRateHiWaterMark')),
            ])
            self.cvcallratemonitorenable = None
            self.cvcallratemonitortime = None
            self.cvcallrate = None
            self.cvcallratehiwatermark = None
            self._segment_path = lambda: "cvCallRateMonitor"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallratemonitor, ['cvcallratemonitorenable', 'cvcallratemonitortime', 'cvcallrate', 'cvcallratehiwatermark'], name, value)


    class Cvcallvolumestatshistory(Entity):
        """
        
        
        .. attribute:: cvcalldurationstatsthreshold
        
        	This Object specifies the thresold duration in seconds. cvCallDurationStatsTable will monitor all the calls below this  threshold.  Decresing the value of the threshold will reset this table
        	**type**\: int
        
        	**range:** 1..3600
        
        	**units**\: seconds
        
        .. attribute:: cvcallvolumewmtablesize
        
        	This Object specifies the number of entries the watermark table will maintain.  This value will decide the number of elements in cvCallRateWMTable, cvCallLegRateWMTable, cvActiveCallWMTable and cvSipMsgRateWMTable
        	**type**\: int
        
        	**range:** 3..10
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallvolumestatshistory, self).__init__()

            self.yang_name = "cvCallVolumeStatsHistory"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvcalldurationstatsthreshold', YLeaf(YType.uint32, 'cvCallDurationStatsThreshold')),
                ('cvcallvolumewmtablesize', YLeaf(YType.uint32, 'cvCallVolumeWMTableSize')),
            ])
            self.cvcalldurationstatsthreshold = None
            self.cvcallvolumewmtablesize = None
            self._segment_path = lambda: "cvCallVolumeStatsHistory"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvolumestatshistory, ['cvcalldurationstatsthreshold', 'cvcallvolumewmtablesize'], name, value)


    class Cvpeercfgtable(Entity):
        """
        The table contains the Voice Generic Peer information that
        is used to create an ifIndexed row with an appropriate
        ifType that is associated with the cvPeerCfgType and
        cvPeerCfgPeerType objects.
        
        .. attribute:: cvpeercfgentry
        
        	A single voice generic Peer. The creation of this entry will create an associated ifEntry with an ifType that is associated with cvPeerCfgType, i.e., for 'voiceEncap' encapsulation, an ifEntry will contain an ifType voiceEncap(103); for 'voiceOverIp' encapsulation, an ifEntry will contain an ifType voiceOverIp(104). The ifAdminStatus of the newly created ifEntry is set to 'up' and ifOperStatus is set to 'down'. In addition, an associated voiceEncap/voiceOverIp Peer configuration entry is created after the successful ifEntry creation. Then ifIndex of the newly created ifEntry must be used by the network manager to create a peer configuration entry of IETF Dial Control MIB (Refer to RFC 2128 section 2.2.3.1 and the description of dialCtlPeerCfgEntry for the detailed information). In summary, the voice dial peer creation steps are as follows\: [1] create this entry (voice/data generic peer entry). [2] read the cvPeerCfgIfIndex of this entry for the     ifIndex of newly created voice/data generic peer. [3] create the dialCtlPeerCfgEntry of RFC 2128 with the     indices of dialCtlPeerCfgId and the ifIndex of newly     created voice generic peer.  For each VoIP peer, it uses IP address and UDP port with RTP protocol to transfer voice packet. Therefore, it does not have its lower layer interface. The dialCtlPeerCfgIfType object of IETF Dial Control MIB must set to 'other' and the dialCtlPeerCfgLowerIf must set to '0'.  After the successful creation of peer configuration entry of IETF Dial Control MIB, the dial plan software in managed device will set the ifOperStatus of the newly created voiceEncap/voiceOverIp ifEntry to 'up' for enabling the peer function if the peer configuration is completed. When this entry is deleted, its associated ifEntry, voiceEncap/voiceOverIp specific peer entry and the peer entry of IETF Dial Control MIB are deleted
        	**type**\: list of  		 :py:class:`Cvpeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable, self).__init__()

            self.yang_name = "cvPeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvPeerCfgEntry", ("cvpeercfgentry", CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry))])
            self._leafs = OrderedDict()

            self.cvpeercfgentry = YList(self)
            self._segment_path = lambda: "cvPeerCfgTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable, [], name, value)


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
            
            .. attribute:: cvpeercfgindex  (key)
            
            	An arbitrary index that uniquely identifies a generic voice peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvpeercfgifindex
            
            	The ifIndex of the peer associated ifEntry. The ifIndex appears after the associated ifEntry is created successfully. This ifIndex will be used to access the objects in the Voice over Telephony or Voice over IP peer specific table. In addition, the ifIndex is also used to access the associated peer configuration entry of the IETF Dial Control MIB. If the peer associated ifEntry had not been created, then this object has a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpeercfgtype
            
            	Specifies the type of voice related encapsulation. voice \- voice encapsulation (voiceEncap ifType) on the         telephony network. voip  \- VoIP encapsulation (voiceOverIp ifType) on the IP         network. mmail \- Media Mail over IP encapsulation (mediaMailOverIp         ifType) on the IP network. voatm \- VoATM encapsulation (voiceOverATM ifType) on the         ATM network. vofr  \- VoFR encapsulation (voiceOverFR ifType) on the         Frame Relay network
            	**type**\:  :py:class:`Cvpeercfgtype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry.Cvpeercfgtype>`
            
            .. attribute:: cvpeercfgrowstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cvpeercfgpeertype
            
            	Specifies the type of a peer. voice \- peer in voice type to be defined in a voice         gateway for voice calls.  data  \- peer in data type to be defined in gateway         that supports universal ports for modem/data         calls and integrated ports for data calls
            	**type**\:  :py:class:`Cvpeercfgpeertype <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry.Cvpeercfgpeertype>`
            
            .. attribute:: cvcallvolpeerincomingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an incoming dialpeer
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolpeeroutgoingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an outgoing dialpeer
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry, self).__init__()

                self.yang_name = "cvPeerCfgEntry"
                self.yang_parent_name = "cvPeerCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpeercfgindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpeercfgindex', YLeaf(YType.int32, 'cvPeerCfgIndex')),
                    ('cvpeercfgifindex', YLeaf(YType.int32, 'cvPeerCfgIfIndex')),
                    ('cvpeercfgtype', YLeaf(YType.enumeration, 'cvPeerCfgType')),
                    ('cvpeercfgrowstatus', YLeaf(YType.enumeration, 'cvPeerCfgRowStatus')),
                    ('cvpeercfgpeertype', YLeaf(YType.enumeration, 'cvPeerCfgPeerType')),
                    ('cvcallvolpeerincomingcalls', YLeaf(YType.uint32, 'cvCallVolPeerIncomingCalls')),
                    ('cvcallvolpeeroutgoingcalls', YLeaf(YType.uint32, 'cvCallVolPeerOutgoingCalls')),
                ])
                self.cvpeercfgindex = None
                self.cvpeercfgifindex = None
                self.cvpeercfgtype = None
                self.cvpeercfgrowstatus = None
                self.cvpeercfgpeertype = None
                self.cvcallvolpeerincomingcalls = None
                self.cvcallvolpeeroutgoingcalls = None
                self._segment_path = lambda: "cvPeerCfgEntry" + "[cvPeerCfgIndex='" + str(self.cvpeercfgindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvPeerCfgTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvpeercfgtable.Cvpeercfgentry, ['cvpeercfgindex', 'cvpeercfgifindex', 'cvpeercfgtype', 'cvpeercfgrowstatus', 'cvpeercfgpeertype', 'cvcallvolpeerincomingcalls', 'cvcallvolpeeroutgoingcalls'], name, value)

            class Cvpeercfgpeertype(Enum):
                """
                Cvpeercfgpeertype (Enum Class)

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
                Cvpeercfgtype (Enum Class)

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



    class Cvvoicepeercfgtable(Entity):
        """
        The table contains the Voice over Telephony peer specific
        information that is required to accept voice calls or to
        which it will place them or perform various loopback tests
        via interface.
        
        .. attribute:: cvvoicepeercfgentry
        
        	A single Voice specific Peer. One entry per voice encapsulation. The entry is created when its associated 'voiceEncap(103)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of  		 :py:class:`Cvvoicepeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable.Cvvoicepeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable, self).__init__()

            self.yang_name = "cvVoicePeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvVoicePeerCfgEntry", ("cvvoicepeercfgentry", CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable.Cvvoicepeercfgentry))])
            self._leafs = OrderedDict()

            self.cvvoicepeercfgentry = YList(self)
            self._segment_path = lambda: "cvVoicePeerCfgTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable, [], name, value)


        class Cvvoicepeercfgentry(Entity):
            """
            A single Voice specific Peer. One entry per voice
            encapsulation.
            The entry is created when its associated 'voiceEncap(103)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cvvoicepeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target.  The valid Mapping type definitions for the peer are as follows\: loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    compressed \- loopback is performed on compressed voice                 as close to the CODEC which processes the                 data as possible.    uncompressed \- loopback is performed on the PCM or                 analog voice as close to the telephony                 endpoint as possible.  Local loopback case\: uncompressed \- the PCM voice coming into the DSP is simply     turned around and sent back out, allowing testing of     the transmit\-\-> receive paths in the telephony     endpoint. compressed \- the compressed voice coming out of the CODEC is     turned around on the DSP module and fed back into the     decompressor through the jitter buffer. In addition to     the telephony endpoint, this tests both the encode and     decode paths without involving data paths or packet     handling on the host router.  Remote loopback case\: compressed \- RTP packets received from the network are     decapsulated and passed to the DSP board. Instead of     feeding these into the CODEC for decompression, they     are immediately sent back to the session application     as if they had originated locally and been compressed. uncompressed \- In addition to the above, the voice samples     are sent all the way through the CODEC and then turned     around instead of being sent to the telephony     endpoint
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cvvoicepeercfgdialdigitsprefix
            
            	The object specifies the prefix of the dial digits for the peer. The dial digits prefix is sent to telephony interface before the real phone number when the system places the outgoing call to the voice encapsulation peer over telephony interface
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cvvoicepeercfgdidcallenable
            
            	The object enables/disables the DID call treatment for incoming DNIS digits. true  \- treat the incoming DNIS digits as if the digits         are received from DID trunk. false \- Disable DID call treatment for incoming DNIS         digits
            	**type**\: bool
            
            .. attribute:: cvvoicepeercfgcasgroup
            
            	The object specifies the CAS group number of a CAS capable T1/E1  that is in the dialCtlPeerCfgLowerIf object of RFC2128. This object can be set to a valid CAS group number only if the dialCtlPeerCfgLowerIf contains a valid ifIndex for a CAS capable T1/E1. The object must set to \-1 before the value of the  dialCtlPeerCfgLowerIf object of RFC2128 can be changed
            	**type**\: int
            
            	**range:** \-1..30
            
            .. attribute:: cvvoicepeercfgregistere164
            
            	This object specifies that the E.164 number specified in the dialCtlPeerCfgOriginateAddress field of the associated dialCtlPeerCfgTable entry be registered as an extension  phone number of this gateway for H323 gatekeeper and/or  SIP registrar
            	**type**\: bool
            
            .. attribute:: cvvoicepeercfgforwarddigits
            
            	This object specifies the number of dialed digits to forward to the remote destination in the setup message. The object can take the value\:     0\-32 number of right justified digits to forward     \-1 default     \-2 forward extra digits i.e those over and above        those needed to match to the destination pattern     \-3 forward all digits
            	**type**\: int
            
            	**range:** \-3..32
            
            .. attribute:: cvvoicepeercfgechocancellertest
            
            	This object specifies which, if any, test to run in the echo canceller when a call from the network is connected. echoCancellerTestNone    \- do not run a test. echoCancellerG168Test2A  \- run ITU\-T G.168 Test 2A. echoCancellerG168Test2B  \- run ITU\-T G.168 Test 2B. echoCancellerG168Test2Ca \- run ITU\-T G.168 Test 2C(a). echoCancellerG168Test2Cb \- run ITU\-T G.168 Test 2C(b). echoCancellerG168Test3A  \- run ITU\-T G.168 Test 3A. echoCancellerG168Test3B  \- run ITU\-T G.168 Test 3B. echoCancellerG168Test3C  \- run ITU\-T G.168 Test 3C. echoCancellerG168Test4   \- run ITU\-T G.168 Test 4. echoCancellerG168Test5   \- run ITU\-T G.168 Test 5. echoCancellerG168Test6   \- run ITU\-T G.168 Test 6. echoCancellerG168Test7   \- run ITU\-T G.168 Test 7. echoCancellerG168Test9   \- run ITU\-T G.168 Test 9
            	**type**\:  :py:class:`Cvvoicepeercfgechocancellertest <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable.Cvvoicepeercfgentry.Cvvoicepeercfgechocancellertest>`
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable.Cvvoicepeercfgentry, self).__init__()

                self.yang_name = "cvVoicePeerCfgEntry"
                self.yang_parent_name = "cvVoicePeerCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cvvoicepeercfgsessiontarget', YLeaf(YType.str, 'cvVoicePeerCfgSessionTarget')),
                    ('cvvoicepeercfgdialdigitsprefix', YLeaf(YType.str, 'cvVoicePeerCfgDialDigitsPrefix')),
                    ('cvvoicepeercfgdidcallenable', YLeaf(YType.boolean, 'cvVoicePeerCfgDIDCallEnable')),
                    ('cvvoicepeercfgcasgroup', YLeaf(YType.int32, 'cvVoicePeerCfgCasGroup')),
                    ('cvvoicepeercfgregistere164', YLeaf(YType.boolean, 'cvVoicePeerCfgRegisterE164')),
                    ('cvvoicepeercfgforwarddigits', YLeaf(YType.int32, 'cvVoicePeerCfgForwardDigits')),
                    ('cvvoicepeercfgechocancellertest', YLeaf(YType.enumeration, 'cvVoicePeerCfgEchoCancellerTest')),
                ])
                self.ifindex = None
                self.cvvoicepeercfgsessiontarget = None
                self.cvvoicepeercfgdialdigitsprefix = None
                self.cvvoicepeercfgdidcallenable = None
                self.cvvoicepeercfgcasgroup = None
                self.cvvoicepeercfgregistere164 = None
                self.cvvoicepeercfgforwarddigits = None
                self.cvvoicepeercfgechocancellertest = None
                self._segment_path = lambda: "cvVoicePeerCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoicePeerCfgTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoicepeercfgtable.Cvvoicepeercfgentry, ['ifindex', 'cvvoicepeercfgsessiontarget', 'cvvoicepeercfgdialdigitsprefix', 'cvvoicepeercfgdidcallenable', 'cvvoicepeercfgcasgroup', 'cvvoicepeercfgregistere164', 'cvvoicepeercfgforwarddigits', 'cvvoicepeercfgechocancellertest'], name, value)

            class Cvvoicepeercfgechocancellertest(Enum):
                """
                Cvvoicepeercfgechocancellertest (Enum Class)

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



    class Cvvoippeercfgtable(Entity):
        """
        The table contains the Voice over IP (VoIP) peer specific
        information that is required to accept voice calls or to
        which it will place them via IP backbone with the
        specified session protocol in cvVoIPPeerCfgSessionProtocol.
        
        .. attribute:: cvvoippeercfgentry
        
        	A single VoIP specific Peer. One entry per VoIP encapsulation. The entry is created when its associated 'voiceOverIp(104)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of  		 :py:class:`Cvvoippeercfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable, self).__init__()

            self.yang_name = "cvVoIPPeerCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvVoIPPeerCfgEntry", ("cvvoippeercfgentry", CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry))])
            self._leafs = OrderedDict()

            self.cvvoippeercfgentry = YList(self)
            self._segment_path = lambda: "cvVoIPPeerCfgTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable, [], name, value)


        class Cvvoippeercfgentry(Entity):
            """
            A single VoIP specific Peer. One entry per VoIP
            encapsulation.
            The entry is created when its associated 'voiceOverIp(104)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cvvoippeercfgsessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:  :py:class:`CvSessionProtocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol>`
            
            .. attribute:: cvvoippeercfgdesiredqos
            
            	The object specifies the user requested Quality of Service for the call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoippeercfgminacceptableqos
            
            	The object specifies the minimally acceptable Quality of Service for the call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoippeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target. The type\-specific\-syntax is exactly that, something that the particular mapping scheme can understand. For example, Session target           Meaning ipv4\:171.68.13.55\:1006   The session target is the IP                          version 4 address of 171.68.13.55                          and port 1006. dns\:pots.cisco.com\:1661  The session target is the IP host                          with dns name pots.cisco.com, and                          port 1661. ras                      The session target is the                          gatekeeper with RAS (Registration                          , Admission,  Status protocol). settlement               The session target is the                          settlement server. enum\:1                   The session target is the enum                           profile match table 1.  The valid Mapping type definitions for the peer are as follows\: ipv4       \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z dns        \- Syntax\: dns\:host.domain\:port or                      dns\:host.domain ras        \- Syntax\: ras settlement \- Syntax\: settlement enum       \- Syntax\: enum\:  loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    rtp \- loopback is performed at the transport protocol          level.  Local loopback case\: rtp \- the session application sets up an RTP stream to     itself (i.e. actually allocates a port pair and opens     the appropriate UDP sockets). It then does the full     RTP encapsulation, sends the packets to the loopback     IP address, receives the RTP packets, and hands the     compressed voice back to the CODEC. This tests the     entire local processing path, both transmit and     receive, in the router, as well as all of the above     paths.  Remote loopback case\: rtp\: RTP packets received from the network are decapsulated and      immediately re\-encapsulated in the outbound RTP      stream, using the same media clock (i.e. timestamp)      as the received packet. They are then sent back to      the remote source router as if the voice had      originated on a telephony port on the local router
            	**type**\: str
            
            .. attribute:: cvvoippeercfgcoderrate
            
            	This object specifies the most desirable codec of speech for the VoIP peer
            	**type**\:  :py:class:`CvcSpeechCoderRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcSpeechCoderRate>`
            
            .. attribute:: cvvoippeercfgfaxrate
            
            	This object specifies the default transmit rate of FAX the VoIP peer. If the value of this object is 'none', then the Fax relay feature is disabled; otherwise the Fax relay feature is enabled
            	**type**\:  :py:class:`CvcFaxTransmitRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcFaxTransmitRate>`
            
            .. attribute:: cvvoippeercfgvadenable
            
            	This object specifies whether or not the VAD (Voice Activity Detection) voice data is continuously transmitted to IP backbone
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgexpectfactor
            
            	This object specifies the user requested Expectation Factor of voice quality for the call via this peer
            	**type**\: int
            
            	**range:** 0..20
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoippeercfgicpif
            
            	This object specifies the user requested Calculated Planning Impairment Factor (Icpif) for the call via this peer
            	**type**\: int
            
            	**range:** 0..55
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoippeercfgpoorqovnotificationenable
            
            	This object specifies whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for the call that is associated with this peer
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgudpchecksumenable
            
            	This object specifies whether the outgoing voice related UDP packet contains a valid checksum value. true  \- enable the checksum of outgoing voice UDP packets false \- disable the checksum of outgoing voice UDP packets
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgipprecedence
            
            	This object specifies the value to be stored in the IP Precedence field of voice packets, with values ranging from 0 (normal precedence) through 7 (network control), allowing the managed system to set the importance of each voice packet for delivering them to the destination peer
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cvvoippeercfgtechprefix
            
            	This object specifies the technology prefix of the peer, The technology prefix and the called party address are passed in Admission Request (ARQ) to gatekeeper for the called party address resolution during call setup
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cvvoippeercfgdigitrelay
            
            	This object specifies the methods to transmit dial digits (DTMF or MF digits) via IP network. rtpCisco       \- Enable capability to transmit dial digits                  with Cisco proprietary RTP payload type. h245Signal     \- Enable capability to transmit dtmf digits                  across the H.245 channel, via the signal                  field of the UserInputIndication message h245Alphanumeric \- Enable capability to transmit dtmf                  digit across the H.245 channel, via the                  string or alphanumeric fields of the                  UserInputIndication message rtpNte         \- Enable capability to transmit dial digits                  using Named Telephony Event per RFC 2833                  section 3. sipNotify      \- Enable capability to transmit dtmf                  digits using unsolicited SIP NOTIFY                  messages. This mechanism is only available                  for SIP dialpeers. sipKpml        \- Enable capability to transmit dtmf                  digits using KPML over SIP SUBSCRIBE                  and NOTIFY messages. This mechanism is                  only available for SIP dialpeers.   Modifying the value of cvVoIPPeerCfgSessionProtocol can reset the digit\-relay method associated bits value in this object if the modified session protocol does not support  these digit\-relay methods
            	**type**\:  :py:class:`Cvvoippeercfgdigitrelay <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgdigitrelay>`
            
            .. attribute:: cvvoippeercfgcoderbytes
            
            	This object specifies the size of the voice payload sample to be produced by the coder specified in cvVoIPPeerCfgCoderRate. Each coder sample produces 10 bytes of voice payload. The specified value will be rounded down to the nearest valid size.  A value of 0, specifies that the coder defined by cvVoIPPeerCfgCoderRate should produce its default payload size
            	**type**\: int
            
            	**range:** 0..None \| 10..240
            
            	**units**\: bytes
            
            .. attribute:: cvvoippeercfgfaxbytes
            
            	This object specifies the payload size to be produced by the coder when it is generating fax data. A value of 0, specifies that the coder specified in cvVoIPCfgPeerCoderRate should produce its default fax payload size
            	**type**\: int
            
            	**range:** 0..None \| 10..255
            
            	**units**\: bytes
            
            .. attribute:: cvvoippeercfginbandsignaling
            
            	This object specifies the type of in\-band signaling that will be used between the end points of the call. It is used by the router to determine how to interpret ABCD signaling bits sent as part of voice payload data
            	**type**\:  :py:class:`CvcInBandSignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling>`
            
            .. attribute:: cvvoippeercfgmediasetting
            
            	This object specifies how the media is to be setup on an IP\-IP Gateway. Two choices are valid\: flow\-through and flow\-around. When in flow\-through mode, which is the default setting, the IP\-IP Gateway will terminate and  then re\-originate the media stream. When flow\-around is configured the Gateway will not be involved with the media, since it will flow\-around the Gateway and will be established directly between the endpoints
            	**type**\:  :py:class:`Cvvoippeercfgmediasetting <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgmediasetting>`
            
            .. attribute:: cvvoippeercfgdesiredqosvideo
            
            	The object specifies the user requested Quality of Service for the video portion of the call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoippeercfgminacceptableqosvideo
            
            	The object specifies the minimally acceptable Quality of Service for the video portion of the call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoippeercfgredirectip2ip
            
            	This object specifies the Inbound VoIP calls that match an outbound VoIP dialpeer will be responded with a SIP  redirect(for inbound SIP) or H.450.3 call\-forward(for  inbound H.323)
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgbitrates
            
            	This object indicates modes of Bit rates. One or more upto four modes can be configured at the same time as bit rates can be changed dynamically for AMR\-NB codec. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\:  :py:class:`CvAmrNbBitRateMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode>`
            
            .. attribute:: cvvoippeercfgcrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgcodermode
            
            	This object indicates the iLBC codec mode to be used. The value of this object is valid only if  cvVoIPPeerCfgCoderRate is equal to 'iLBC'
            	**type**\:  :py:class:`CvIlbcFrameMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode>`
            
            .. attribute:: cvvoippeercfgcodingmode
            
            	This object specifies the coding mode to be used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following coding modes are supported\: adaptive    (1) \- adaptive mode where iSAC performs bandwidth                     estimation and adapts to the available channel                    bandwidth. independent (2) \- independent mode in which no bandwidth estimation                    is performed
            	**type**\:  :py:class:`Cvvoippeercfgcodingmode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgcodingmode>`
            
            .. attribute:: cvvoippeercfgbitrate
            
            	This object specifies the target bit rate. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'
            	**type**\: int
            
            	**range:** 10000..32000
            
            .. attribute:: cvvoippeercfgframesize
            
            	This object specifies the frame size used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. The frame size can be 30 ms or 60 ms, and it can be fixed for all packets or vary depending on the configuration and bandwidth estimation. Thus it can have the following values\: frameSize30      \- initial frame size of 30 ms frameSize60      \- initial frame size of 60 ms frameSize30fixed \- fixed frame size 30 ms frameSize60fixed \- fixed frame size 60 ms
            	**type**\:  :py:class:`Cvvoippeercfgframesize <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgframesize>`
            
            .. attribute:: cvvoippeercfgdscppolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for RPH to DSCP mapping and policing feature
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgmediapolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for Media policing feature.
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry, self).__init__()

                self.yang_name = "cvVoIPPeerCfgEntry"
                self.yang_parent_name = "cvVoIPPeerCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cvvoippeercfgsessionprotocol', YLeaf(YType.enumeration, 'cvVoIPPeerCfgSessionProtocol')),
                    ('cvvoippeercfgdesiredqos', YLeaf(YType.enumeration, 'cvVoIPPeerCfgDesiredQoS')),
                    ('cvvoippeercfgminacceptableqos', YLeaf(YType.enumeration, 'cvVoIPPeerCfgMinAcceptableQoS')),
                    ('cvvoippeercfgsessiontarget', YLeaf(YType.str, 'cvVoIPPeerCfgSessionTarget')),
                    ('cvvoippeercfgcoderrate', YLeaf(YType.enumeration, 'cvVoIPPeerCfgCoderRate')),
                    ('cvvoippeercfgfaxrate', YLeaf(YType.enumeration, 'cvVoIPPeerCfgFaxRate')),
                    ('cvvoippeercfgvadenable', YLeaf(YType.boolean, 'cvVoIPPeerCfgVADEnable')),
                    ('cvvoippeercfgexpectfactor', YLeaf(YType.int32, 'cvVoIPPeerCfgExpectFactor')),
                    ('cvvoippeercfgicpif', YLeaf(YType.int32, 'cvVoIPPeerCfgIcpif')),
                    ('cvvoippeercfgpoorqovnotificationenable', YLeaf(YType.boolean, 'cvVoIPPeerCfgPoorQoVNotificationEnable')),
                    ('cvvoippeercfgudpchecksumenable', YLeaf(YType.boolean, 'cvVoIPPeerCfgUDPChecksumEnable')),
                    ('cvvoippeercfgipprecedence', YLeaf(YType.int32, 'cvVoIPPeerCfgIPPrecedence')),
                    ('cvvoippeercfgtechprefix', YLeaf(YType.str, 'cvVoIPPeerCfgTechPrefix')),
                    ('cvvoippeercfgdigitrelay', YLeaf(YType.bits, 'cvVoIPPeerCfgDigitRelay')),
                    ('cvvoippeercfgcoderbytes', YLeaf(YType.int32, 'cvVoIPPeerCfgCoderBytes')),
                    ('cvvoippeercfgfaxbytes', YLeaf(YType.int32, 'cvVoIPPeerCfgFaxBytes')),
                    ('cvvoippeercfginbandsignaling', YLeaf(YType.enumeration, 'cvVoIPPeerCfgInBandSignaling')),
                    ('cvvoippeercfgmediasetting', YLeaf(YType.enumeration, 'cvVoIPPeerCfgMediaSetting')),
                    ('cvvoippeercfgdesiredqosvideo', YLeaf(YType.enumeration, 'cvVoIPPeerCfgDesiredQoSVideo')),
                    ('cvvoippeercfgminacceptableqosvideo', YLeaf(YType.enumeration, 'cvVoIPPeerCfgMinAcceptableQoSVideo')),
                    ('cvvoippeercfgredirectip2ip', YLeaf(YType.boolean, 'cvVoIPPeerCfgRedirectip2ip')),
                    ('cvvoippeercfgoctetaligned', YLeaf(YType.boolean, 'cvVoIPPeerCfgOctetAligned')),
                    ('cvvoippeercfgbitrates', YLeaf(YType.bits, 'cvVoIPPeerCfgBitRates')),
                    ('cvvoippeercfgcrc', YLeaf(YType.boolean, 'cvVoIPPeerCfgCRC')),
                    ('cvvoippeercfgcodermode', YLeaf(YType.enumeration, 'cvVoIPPeerCfgCoderMode')),
                    ('cvvoippeercfgcodingmode', YLeaf(YType.enumeration, 'cvVoIPPeerCfgCodingMode')),
                    ('cvvoippeercfgbitrate', YLeaf(YType.uint32, 'cvVoIPPeerCfgBitRate')),
                    ('cvvoippeercfgframesize', YLeaf(YType.enumeration, 'cvVoIPPeerCfgFrameSize')),
                    ('cvvoippeercfgdscppolicynotificationenable', YLeaf(YType.boolean, 'cvVoIPPeerCfgDSCPPolicyNotificationEnable')),
                    ('cvvoippeercfgmediapolicynotificationenable', YLeaf(YType.boolean, 'cvVoIPPeerCfgMediaPolicyNotificationEnable')),
                ])
                self.ifindex = None
                self.cvvoippeercfgsessionprotocol = None
                self.cvvoippeercfgdesiredqos = None
                self.cvvoippeercfgminacceptableqos = None
                self.cvvoippeercfgsessiontarget = None
                self.cvvoippeercfgcoderrate = None
                self.cvvoippeercfgfaxrate = None
                self.cvvoippeercfgvadenable = None
                self.cvvoippeercfgexpectfactor = None
                self.cvvoippeercfgicpif = None
                self.cvvoippeercfgpoorqovnotificationenable = None
                self.cvvoippeercfgudpchecksumenable = None
                self.cvvoippeercfgipprecedence = None
                self.cvvoippeercfgtechprefix = None
                self.cvvoippeercfgdigitrelay = Bits()
                self.cvvoippeercfgcoderbytes = None
                self.cvvoippeercfgfaxbytes = None
                self.cvvoippeercfginbandsignaling = None
                self.cvvoippeercfgmediasetting = None
                self.cvvoippeercfgdesiredqosvideo = None
                self.cvvoippeercfgminacceptableqosvideo = None
                self.cvvoippeercfgredirectip2ip = None
                self.cvvoippeercfgoctetaligned = None
                self.cvvoippeercfgbitrates = Bits()
                self.cvvoippeercfgcrc = None
                self.cvvoippeercfgcodermode = None
                self.cvvoippeercfgcodingmode = None
                self.cvvoippeercfgbitrate = None
                self.cvvoippeercfgframesize = None
                self.cvvoippeercfgdscppolicynotificationenable = None
                self.cvvoippeercfgmediapolicynotificationenable = None
                self._segment_path = lambda: "cvVoIPPeerCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPPeerCfgTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoippeercfgtable.Cvvoippeercfgentry, ['ifindex', 'cvvoippeercfgsessionprotocol', 'cvvoippeercfgdesiredqos', 'cvvoippeercfgminacceptableqos', 'cvvoippeercfgsessiontarget', 'cvvoippeercfgcoderrate', 'cvvoippeercfgfaxrate', 'cvvoippeercfgvadenable', 'cvvoippeercfgexpectfactor', 'cvvoippeercfgicpif', 'cvvoippeercfgpoorqovnotificationenable', 'cvvoippeercfgudpchecksumenable', 'cvvoippeercfgipprecedence', 'cvvoippeercfgtechprefix', 'cvvoippeercfgdigitrelay', 'cvvoippeercfgcoderbytes', 'cvvoippeercfgfaxbytes', 'cvvoippeercfginbandsignaling', 'cvvoippeercfgmediasetting', 'cvvoippeercfgdesiredqosvideo', 'cvvoippeercfgminacceptableqosvideo', 'cvvoippeercfgredirectip2ip', 'cvvoippeercfgoctetaligned', 'cvvoippeercfgbitrates', 'cvvoippeercfgcrc', 'cvvoippeercfgcodermode', 'cvvoippeercfgcodingmode', 'cvvoippeercfgbitrate', 'cvvoippeercfgframesize', 'cvvoippeercfgdscppolicynotificationenable', 'cvvoippeercfgmediapolicynotificationenable'], name, value)

            class Cvvoippeercfgcodingmode(Enum):
                """
                Cvvoippeercfgcodingmode (Enum Class)

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
                Cvvoippeercfgframesize (Enum Class)

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
                Cvvoippeercfgmediasetting (Enum Class)

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



    class Cvpeercommoncfgtable(Entity):
        """
        The table contains the Voice specific peer common
        configuration information that is required to accept voice
        calls or to which it will place them or process the
        incoming calls.
        
        .. attribute:: cvpeercommoncfgentry
        
        	A single Voice specific Peer. One entry per voice related encapsulation. The entry is created when a voice related encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of  		 :py:class:`Cvpeercommoncfgentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable.Cvpeercommoncfgentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable, self).__init__()

            self.yang_name = "cvPeerCommonCfgTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvPeerCommonCfgEntry", ("cvpeercommoncfgentry", CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable.Cvpeercommoncfgentry))])
            self._leafs = OrderedDict()

            self.cvpeercommoncfgentry = YList(self)
            self._segment_path = lambda: "cvPeerCommonCfgTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable, [], name, value)


        class Cvpeercommoncfgentry(Entity):
            """
            A single Voice specific Peer. One entry per voice related
            encapsulation.
            The entry is created when a voice related encapsulation
            ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cvpeercommoncfgincomingdnisdigits
            
            	The object specifies the prefix of the incoming Dialed Number Identification Service (DNIS) digits for the peer. The DNIS digits prefix is used to match with the incoming DNIS number for incoming call discrimination. If the digits in this object are matched with incoming DNIS number, the  associated dialCtlPeerCfgInfoType in RFC 2128 will be used as a call discriminator for differentiating speech, data, fax, video or modem calls
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cvpeercommoncfgmaxconnections
            
            	The object specifies the maximum allowed connection to/from the peer. A value of \-1 disables the limit of maximum connections
            	**type**\: int
            
            	**range:** \-1..None \| 1..2147483647
            
            	**units**\: connections
            
            .. attribute:: cvpeercommoncfgapplicationname
            
            	The object specifies the application to handle the incoming call after the peer is selected. If no application name is specified, then the default session application will take care of the incoming call
            	**type**\: str
            
            .. attribute:: cvpeercommoncfgpreference
            
            	This object specifies the selection preference of a peer when multiple peers are matched to the selection criteria. The value of 0 has the lowest preference for peer selection
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: cvpeercommoncfghuntstop
            
            	This object specifies whether dialpeer hunting should stop when this peer is reached
            	**type**\: bool
            
            .. attribute:: cvpeercommoncfgdnismappingname
            
            	The object specifies a Dialer Number Identification Service (DNIS) map name for the Voice specific peer entry specified in this row. A DNIS is a called party number and they can be grouped and identified by DNIS map
            	**type**\: str
            
            .. attribute:: cvpeercommoncfgsourcecarrierid
            
            	The object specifies the Source Carrier Id for the peer. The Source Carrier Id is used to match with the Source Carrier Id of a call. If the Source Carrier Id in this object is matched with the Source Carrier Id of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            .. attribute:: cvpeercommoncfgtargetcarrierid
            
            	The object specifies the Target Carrier Id for the peer. The Target Carrier Id is used to match with the Target Carrier Id of a call. If the Target Carrier Id in this object is matched with the Target Carrier Id of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            .. attribute:: cvpeercommoncfgsourcetrunkgrplabel
            
            	The object specifies the Source Trunk Group Label for the peer. The Source Trunk Group Label is used to match with the Source Trunk Group Label of a call. If the Source Trunk Group Label in this object is matched with the Source Trunk Group Label of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            .. attribute:: cvpeercommoncfgtargettrunkgrplabel
            
            	The object specifies the Target Trunk Group Label for the peer. The Target Trunk Group Label is used to match with the Target Trunk Group Label of a call. If the Target Trunk Group Label in this object is matched with the Target Trunk Group Label of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable.Cvpeercommoncfgentry, self).__init__()

                self.yang_name = "cvPeerCommonCfgEntry"
                self.yang_parent_name = "cvPeerCommonCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cvpeercommoncfgincomingdnisdigits', YLeaf(YType.str, 'cvPeerCommonCfgIncomingDnisDigits')),
                    ('cvpeercommoncfgmaxconnections', YLeaf(YType.int32, 'cvPeerCommonCfgMaxConnections')),
                    ('cvpeercommoncfgapplicationname', YLeaf(YType.str, 'cvPeerCommonCfgApplicationName')),
                    ('cvpeercommoncfgpreference', YLeaf(YType.int32, 'cvPeerCommonCfgPreference')),
                    ('cvpeercommoncfghuntstop', YLeaf(YType.boolean, 'cvPeerCommonCfgHuntStop')),
                    ('cvpeercommoncfgdnismappingname', YLeaf(YType.str, 'cvPeerCommonCfgDnisMappingName')),
                    ('cvpeercommoncfgsourcecarrierid', YLeaf(YType.str, 'cvPeerCommonCfgSourceCarrierId')),
                    ('cvpeercommoncfgtargetcarrierid', YLeaf(YType.str, 'cvPeerCommonCfgTargetCarrierId')),
                    ('cvpeercommoncfgsourcetrunkgrplabel', YLeaf(YType.str, 'cvPeerCommonCfgSourceTrunkGrpLabel')),
                    ('cvpeercommoncfgtargettrunkgrplabel', YLeaf(YType.str, 'cvPeerCommonCfgTargetTrunkGrpLabel')),
                ])
                self.ifindex = None
                self.cvpeercommoncfgincomingdnisdigits = None
                self.cvpeercommoncfgmaxconnections = None
                self.cvpeercommoncfgapplicationname = None
                self.cvpeercommoncfgpreference = None
                self.cvpeercommoncfghuntstop = None
                self.cvpeercommoncfgdnismappingname = None
                self.cvpeercommoncfgsourcecarrierid = None
                self.cvpeercommoncfgtargetcarrierid = None
                self.cvpeercommoncfgsourcetrunkgrplabel = None
                self.cvpeercommoncfgtargettrunkgrplabel = None
                self._segment_path = lambda: "cvPeerCommonCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvPeerCommonCfgTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvpeercommoncfgtable.Cvpeercommoncfgentry, ['ifindex', 'cvpeercommoncfgincomingdnisdigits', 'cvpeercommoncfgmaxconnections', 'cvpeercommoncfgapplicationname', 'cvpeercommoncfgpreference', 'cvpeercommoncfghuntstop', 'cvpeercommoncfgdnismappingname', 'cvpeercommoncfgsourcecarrierid', 'cvpeercommoncfgtargetcarrierid', 'cvpeercommoncfgsourcetrunkgrplabel', 'cvpeercommoncfgtargettrunkgrplabel'], name, value)


    class Cvcallactivetable(Entity):
        """
        This table is the voice extension to the call active table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information that is derived from the statistics
        of lower layer telephony interface.
        
        .. attribute:: cvcallactiveentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and call active entry contains the call establishment to a voice over telephony network peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvcallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallactivetable.Cvcallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallactivetable, self).__init__()

            self.yang_name = "cvCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallActiveEntry", ("cvcallactiveentry", CISCOVOICEDIALCONTROLMIB.Cvcallactivetable.Cvcallactiveentry))])
            self._leafs = OrderedDict()

            self.cvcallactiveentry = YList(self)
            self._segment_path = lambda: "cvCallActiveTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallactivetable, [], name, value)


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
            
            .. attribute:: callactivesetuptime  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: cvcallactiveconnectionid
            
            	The global connection identifier for the active telephony leg of the call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvcallactivetxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallactivevoicetxduration
            
            	Duration of voice transmitted from this peer to voice gateway for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallactivefaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            .. attribute:: cvcallactivenoiselevel
            
            	The object contains the active noise level for the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactiveacomlevel
            
            	The object contains the sum of Echo Return Loss (ERL), cancellation loss (Echo Return Loss Enhancement) and nonlinear processing loss for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..127
            
            	**units**\: dB
            
            .. attribute:: cvcallactiveoutsignallevel
            
            	The object contains the active output signal level to telephony interface that is used by the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactiveinsignallevel
            
            	The object contains the active input signal level from telephony interface that is used by the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallactiveerllevel
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..45
            
            	**units**\: dB
            
            	**status**\: deprecated
            
            .. attribute:: cvcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg. This object is set with the information in the call associated cvVoicePeerCfgSessionTarget object when the call is connected
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cvcallactiveimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: pages
            
            .. attribute:: cvcallactivecallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            .. attribute:: cvcallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\: bool
            
            .. attribute:: cvcallactiveecanreflectorlocation
            
            	The location in milliseconds of the largest amplitude reflector detected by the echo canceller for this call.  The value 0 indicates there is no reflector or the  information is not available
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: cvcallactiveaccountcode
            
            	The object indicates the account code input to the call. It could be used for call screen or by down stream server for billing purpose. The value of empty string indicates no account code input
            	**type**\: str
            
            	**length:** 0..50
            
            .. attribute:: cvcallactiveerllevelrev1
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..200
            
            	**units**\: dB
            
            .. attribute:: cvcallactivecallid
            
            	This object represents the call identifier for the active telephony leg of the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallactivetable.Cvcallactiveentry, self).__init__()

                self.yang_name = "cvCallActiveEntry"
                self.yang_parent_name = "cvCallActiveTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['callactivesetuptime','callactiveindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('callactivesetuptime', YLeaf(YType.str, 'callActiveSetupTime')),
                    ('callactiveindex', YLeaf(YType.str, 'callActiveIndex')),
                    ('cvcallactiveconnectionid', YLeaf(YType.str, 'cvCallActiveConnectionId')),
                    ('cvcallactivetxduration', YLeaf(YType.uint32, 'cvCallActiveTxDuration')),
                    ('cvcallactivevoicetxduration', YLeaf(YType.uint32, 'cvCallActiveVoiceTxDuration')),
                    ('cvcallactivefaxtxduration', YLeaf(YType.uint32, 'cvCallActiveFaxTxDuration')),
                    ('cvcallactivecodertyperate', YLeaf(YType.enumeration, 'cvCallActiveCoderTypeRate')),
                    ('cvcallactivenoiselevel', YLeaf(YType.int32, 'cvCallActiveNoiseLevel')),
                    ('cvcallactiveacomlevel', YLeaf(YType.int32, 'cvCallActiveACOMLevel')),
                    ('cvcallactiveoutsignallevel', YLeaf(YType.int32, 'cvCallActiveOutSignalLevel')),
                    ('cvcallactiveinsignallevel', YLeaf(YType.int32, 'cvCallActiveInSignalLevel')),
                    ('cvcallactiveerllevel', YLeaf(YType.int32, 'cvCallActiveERLLevel')),
                    ('cvcallactivesessiontarget', YLeaf(YType.str, 'cvCallActiveSessionTarget')),
                    ('cvcallactiveimgpagecount', YLeaf(YType.uint32, 'cvCallActiveImgPageCount')),
                    ('cvcallactivecallingname', YLeaf(YType.str, 'cvCallActiveCallingName')),
                    ('cvcallactivecalleridblock', YLeaf(YType.boolean, 'cvCallActiveCallerIDBlock')),
                    ('cvcallactiveecanreflectorlocation', YLeaf(YType.int32, 'cvCallActiveEcanReflectorLocation')),
                    ('cvcallactiveaccountcode', YLeaf(YType.str, 'cvCallActiveAccountCode')),
                    ('cvcallactiveerllevelrev1', YLeaf(YType.int32, 'cvCallActiveERLLevelRev1')),
                    ('cvcallactivecallid', YLeaf(YType.uint32, 'cvCallActiveCallId')),
                ])
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.cvcallactiveconnectionid = None
                self.cvcallactivetxduration = None
                self.cvcallactivevoicetxduration = None
                self.cvcallactivefaxtxduration = None
                self.cvcallactivecodertyperate = None
                self.cvcallactivenoiselevel = None
                self.cvcallactiveacomlevel = None
                self.cvcallactiveoutsignallevel = None
                self.cvcallactiveinsignallevel = None
                self.cvcallactiveerllevel = None
                self.cvcallactivesessiontarget = None
                self.cvcallactiveimgpagecount = None
                self.cvcallactivecallingname = None
                self.cvcallactivecalleridblock = None
                self.cvcallactiveecanreflectorlocation = None
                self.cvcallactiveaccountcode = None
                self.cvcallactiveerllevelrev1 = None
                self.cvcallactivecallid = None
                self._segment_path = lambda: "cvCallActiveEntry" + "[callActiveSetupTime='" + str(self.callactivesetuptime) + "']" + "[callActiveIndex='" + str(self.callactiveindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallActiveTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallactivetable.Cvcallactiveentry, ['callactivesetuptime', 'callactiveindex', 'cvcallactiveconnectionid', 'cvcallactivetxduration', 'cvcallactivevoicetxduration', 'cvcallactivefaxtxduration', 'cvcallactivecodertyperate', 'cvcallactivenoiselevel', 'cvcallactiveacomlevel', 'cvcallactiveoutsignallevel', 'cvcallactiveinsignallevel', 'cvcallactiveerllevel', 'cvcallactivesessiontarget', 'cvcallactiveimgpagecount', 'cvcallactivecallingname', 'cvcallactivecalleridblock', 'cvcallactiveecanreflectorlocation', 'cvcallactiveaccountcode', 'cvcallactiveerllevelrev1', 'cvcallactivecallid'], name, value)


    class Cvvoipcallactivetable(Entity):
        """
        This table is the VoIP extension to the call active table of
        IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallactiveentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the call establishment to the peer on the IP backbone via a voice over  IP peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvvoipcallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable.Cvvoipcallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable, self).__init__()

            self.yang_name = "cvVoIPCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvVoIPCallActiveEntry", ("cvvoipcallactiveentry", CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable.Cvvoipcallactiveentry))])
            self._leafs = OrderedDict()

            self.cvvoipcallactiveentry = YList(self)
            self._segment_path = lambda: "cvVoIPCallActiveTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable, [], name, value)


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
            
            .. attribute:: callactivesetuptime  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: cvvoipcallactiveconnectionid
            
            	The global connection identifier for the active VoIP leg of the call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallactiveremoteipaddress
            
            	Remote system IP address for the VoIP call
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactiveremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactiveroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactiveselectedqos
            
            	The selected RSVP QoS for the voice call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoipcallactivesessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:  :py:class:`CvSessionProtocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol>`
            
            .. attribute:: cvvoipcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call. This object is set with the information in the call associated cvVoIPPeerCfgSessionTarget object when the voice over IP call is connected
            	**type**\: str
            
            .. attribute:: cvvoipcallactiveontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivegapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivehiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivelowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivereceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallactivelostpackets
            
            	The number of lost voice packets during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactiveearlypackets
            
            	The number of received voice packets that arrived too early to store in jitter buffer during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactivelatepackets
            
            	The number of received voice packets that arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallactiveusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallactiveprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemSigIPAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvvoipcallactiveremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactiveremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemMediaIPAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvvoipcallactiveremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallactiveremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactivesrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactivebitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  :py:class:`CvAmrNbBitRateMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode>`
            
            .. attribute:: cvvoipcallactivemodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallactivemodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallActiveBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallActiveBitRates object. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactivemaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivecrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiverobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  :py:class:`CvAmrNbRtpEncap <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbRtpEncap>`
            
            .. attribute:: cvvoipcallactiveinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..50
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallactiveptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivechannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..6
            
            	**units**\: channels
            
            .. attribute:: cvvoipcallactivecodermode
            
            	The object indicates the iLBC codec mode. The value of this object is valid only if  cvVoIPCallActiveCoderTypeRate is equal to  'iLBC'
            	**type**\:  :py:class:`CvIlbcFrameMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode>`
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallactivecallid
            
            	This object represents the call identifier for the active VoIP leg of the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallactivecallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.    For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccvoipcallactivepolicyname
            
            	This object holds the policy name. It could be media policy, DSCP policy etc
            	**type**\: str
            
            .. attribute:: cvvoipcallactivereverseddirectionpeeraddress
            
            	This object store the reversed direction peer address  If the address is not available, then it will have a length of zero.  If the call is ingress then it contains called number and if the call is egress then it contains calling number
            	**type**\: str
            
            .. attribute:: cvvoipcallactivesessionid
            
            	This object indicates the active session ID assigned by the call manager to identify call legs that belong to the same call session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable.Cvvoipcallactiveentry, self).__init__()

                self.yang_name = "cvVoIPCallActiveEntry"
                self.yang_parent_name = "cvVoIPCallActiveTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['callactivesetuptime','callactiveindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('callactivesetuptime', YLeaf(YType.str, 'callActiveSetupTime')),
                    ('callactiveindex', YLeaf(YType.str, 'callActiveIndex')),
                    ('cvvoipcallactiveconnectionid', YLeaf(YType.str, 'cvVoIPCallActiveConnectionId')),
                    ('cvvoipcallactiveremoteipaddress', YLeaf(YType.str, 'cvVoIPCallActiveRemoteIPAddress')),
                    ('cvvoipcallactiveremoteudpport', YLeaf(YType.int32, 'cvVoIPCallActiveRemoteUDPPort')),
                    ('cvvoipcallactiveroundtripdelay', YLeaf(YType.uint32, 'cvVoIPCallActiveRoundTripDelay')),
                    ('cvvoipcallactiveselectedqos', YLeaf(YType.enumeration, 'cvVoIPCallActiveSelectedQoS')),
                    ('cvvoipcallactivesessionprotocol', YLeaf(YType.enumeration, 'cvVoIPCallActiveSessionProtocol')),
                    ('cvvoipcallactivesessiontarget', YLeaf(YType.str, 'cvVoIPCallActiveSessionTarget')),
                    ('cvvoipcallactiveontimervplayout', YLeaf(YType.uint32, 'cvVoIPCallActiveOnTimeRvPlayout')),
                    ('cvvoipcallactivegapfillwithsilence', YLeaf(YType.uint32, 'cvVoIPCallActiveGapFillWithSilence')),
                    ('cvvoipcallactivegapfillwithprediction', YLeaf(YType.uint32, 'cvVoIPCallActiveGapFillWithPrediction')),
                    ('cvvoipcallactivegapfillwithinterpolation', YLeaf(YType.uint32, 'cvVoIPCallActiveGapFillWithInterpolation')),
                    ('cvvoipcallactivegapfillwithredundancy', YLeaf(YType.uint32, 'cvVoIPCallActiveGapFillWithRedundancy')),
                    ('cvvoipcallactivehiwaterplayoutdelay', YLeaf(YType.uint32, 'cvVoIPCallActiveHiWaterPlayoutDelay')),
                    ('cvvoipcallactivelowaterplayoutdelay', YLeaf(YType.uint32, 'cvVoIPCallActiveLoWaterPlayoutDelay')),
                    ('cvvoipcallactivereceivedelay', YLeaf(YType.uint32, 'cvVoIPCallActiveReceiveDelay')),
                    ('cvvoipcallactivevadenable', YLeaf(YType.boolean, 'cvVoIPCallActiveVADEnable')),
                    ('cvvoipcallactivecodertyperate', YLeaf(YType.enumeration, 'cvVoIPCallActiveCoderTypeRate')),
                    ('cvvoipcallactivelostpackets', YLeaf(YType.uint32, 'cvVoIPCallActiveLostPackets')),
                    ('cvvoipcallactiveearlypackets', YLeaf(YType.uint32, 'cvVoIPCallActiveEarlyPackets')),
                    ('cvvoipcallactivelatepackets', YLeaf(YType.uint32, 'cvVoIPCallActiveLatePackets')),
                    ('cvvoipcallactiveusername', YLeaf(YType.str, 'cvVoIPCallActiveUsername')),
                    ('cvvoipcallactiveprotocolcallid', YLeaf(YType.str, 'cvVoIPCallActiveProtocolCallId')),
                    ('cvvoipcallactiveremsigipaddrt', YLeaf(YType.enumeration, 'cvVoIPCallActiveRemSigIPAddrT')),
                    ('cvvoipcallactiveremsigipaddr', YLeaf(YType.str, 'cvVoIPCallActiveRemSigIPAddr')),
                    ('cvvoipcallactiveremsigport', YLeaf(YType.int32, 'cvVoIPCallActiveRemSigPort')),
                    ('cvvoipcallactiveremmediaipaddrt', YLeaf(YType.enumeration, 'cvVoIPCallActiveRemMediaIPAddrT')),
                    ('cvvoipcallactiveremmediaipaddr', YLeaf(YType.str, 'cvVoIPCallActiveRemMediaIPAddr')),
                    ('cvvoipcallactiveremmediaport', YLeaf(YType.int32, 'cvVoIPCallActiveRemMediaPort')),
                    ('cvvoipcallactivesrtpenable', YLeaf(YType.boolean, 'cvVoIPCallActiveSRTPEnable')),
                    ('cvvoipcallactiveoctetaligned', YLeaf(YType.boolean, 'cvVoIPCallActiveOctetAligned')),
                    ('cvvoipcallactivebitrates', YLeaf(YType.bits, 'cvVoIPCallActiveBitRates')),
                    ('cvvoipcallactivemodechgperiod', YLeaf(YType.int32, 'cvVoIPCallActiveModeChgPeriod')),
                    ('cvvoipcallactivemodechgneighbor', YLeaf(YType.boolean, 'cvVoIPCallActiveModeChgNeighbor')),
                    ('cvvoipcallactivemaxptime', YLeaf(YType.int32, 'cvVoIPCallActiveMaxPtime')),
                    ('cvvoipcallactivecrc', YLeaf(YType.boolean, 'cvVoIPCallActiveCRC')),
                    ('cvvoipcallactiverobustsorting', YLeaf(YType.boolean, 'cvVoIPCallActiveRobustSorting')),
                    ('cvvoipcallactiveencap', YLeaf(YType.enumeration, 'cvVoIPCallActiveEncap')),
                    ('cvvoipcallactiveinterleaving', YLeaf(YType.int32, 'cvVoIPCallActiveInterleaving')),
                    ('cvvoipcallactiveptime', YLeaf(YType.int32, 'cvVoIPCallActivePtime')),
                    ('cvvoipcallactivechannels', YLeaf(YType.int32, 'cvVoIPCallActiveChannels')),
                    ('cvvoipcallactivecodermode', YLeaf(YType.enumeration, 'cvVoIPCallActiveCoderMode')),
                    ('cvvoipcallactivecallid', YLeaf(YType.uint32, 'cvVoIPCallActiveCallId')),
                    ('cvvoipcallactivecallreferenceid', YLeaf(YType.uint32, 'cvVoIPCallActiveCallReferenceId')),
                    ('ccvoipcallactivepolicyname', YLeaf(YType.str, 'ccVoIPCallActivePolicyName')),
                    ('cvvoipcallactivereverseddirectionpeeraddress', YLeaf(YType.str, 'cvVoIPCallActiveReversedDirectionPeerAddress')),
                    ('cvvoipcallactivesessionid', YLeaf(YType.uint32, 'cvVoIPCallActiveSessionId')),
                ])
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.cvvoipcallactiveconnectionid = None
                self.cvvoipcallactiveremoteipaddress = None
                self.cvvoipcallactiveremoteudpport = None
                self.cvvoipcallactiveroundtripdelay = None
                self.cvvoipcallactiveselectedqos = None
                self.cvvoipcallactivesessionprotocol = None
                self.cvvoipcallactivesessiontarget = None
                self.cvvoipcallactiveontimervplayout = None
                self.cvvoipcallactivegapfillwithsilence = None
                self.cvvoipcallactivegapfillwithprediction = None
                self.cvvoipcallactivegapfillwithinterpolation = None
                self.cvvoipcallactivegapfillwithredundancy = None
                self.cvvoipcallactivehiwaterplayoutdelay = None
                self.cvvoipcallactivelowaterplayoutdelay = None
                self.cvvoipcallactivereceivedelay = None
                self.cvvoipcallactivevadenable = None
                self.cvvoipcallactivecodertyperate = None
                self.cvvoipcallactivelostpackets = None
                self.cvvoipcallactiveearlypackets = None
                self.cvvoipcallactivelatepackets = None
                self.cvvoipcallactiveusername = None
                self.cvvoipcallactiveprotocolcallid = None
                self.cvvoipcallactiveremsigipaddrt = None
                self.cvvoipcallactiveremsigipaddr = None
                self.cvvoipcallactiveremsigport = None
                self.cvvoipcallactiveremmediaipaddrt = None
                self.cvvoipcallactiveremmediaipaddr = None
                self.cvvoipcallactiveremmediaport = None
                self.cvvoipcallactivesrtpenable = None
                self.cvvoipcallactiveoctetaligned = None
                self.cvvoipcallactivebitrates = Bits()
                self.cvvoipcallactivemodechgperiod = None
                self.cvvoipcallactivemodechgneighbor = None
                self.cvvoipcallactivemaxptime = None
                self.cvvoipcallactivecrc = None
                self.cvvoipcallactiverobustsorting = None
                self.cvvoipcallactiveencap = None
                self.cvvoipcallactiveinterleaving = None
                self.cvvoipcallactiveptime = None
                self.cvvoipcallactivechannels = None
                self.cvvoipcallactivecodermode = None
                self.cvvoipcallactivecallid = None
                self.cvvoipcallactivecallreferenceid = None
                self.ccvoipcallactivepolicyname = None
                self.cvvoipcallactivereverseddirectionpeeraddress = None
                self.cvvoipcallactivesessionid = None
                self._segment_path = lambda: "cvVoIPCallActiveEntry" + "[callActiveSetupTime='" + str(self.callactivesetuptime) + "']" + "[callActiveIndex='" + str(self.callactiveindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPCallActiveTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoipcallactivetable.Cvvoipcallactiveentry, ['callactivesetuptime', 'callactiveindex', 'cvvoipcallactiveconnectionid', 'cvvoipcallactiveremoteipaddress', 'cvvoipcallactiveremoteudpport', 'cvvoipcallactiveroundtripdelay', 'cvvoipcallactiveselectedqos', 'cvvoipcallactivesessionprotocol', 'cvvoipcallactivesessiontarget', 'cvvoipcallactiveontimervplayout', 'cvvoipcallactivegapfillwithsilence', 'cvvoipcallactivegapfillwithprediction', 'cvvoipcallactivegapfillwithinterpolation', 'cvvoipcallactivegapfillwithredundancy', 'cvvoipcallactivehiwaterplayoutdelay', 'cvvoipcallactivelowaterplayoutdelay', 'cvvoipcallactivereceivedelay', 'cvvoipcallactivevadenable', 'cvvoipcallactivecodertyperate', 'cvvoipcallactivelostpackets', 'cvvoipcallactiveearlypackets', 'cvvoipcallactivelatepackets', 'cvvoipcallactiveusername', 'cvvoipcallactiveprotocolcallid', 'cvvoipcallactiveremsigipaddrt', 'cvvoipcallactiveremsigipaddr', 'cvvoipcallactiveremsigport', 'cvvoipcallactiveremmediaipaddrt', 'cvvoipcallactiveremmediaipaddr', 'cvvoipcallactiveremmediaport', 'cvvoipcallactivesrtpenable', 'cvvoipcallactiveoctetaligned', 'cvvoipcallactivebitrates', 'cvvoipcallactivemodechgperiod', 'cvvoipcallactivemodechgneighbor', 'cvvoipcallactivemaxptime', 'cvvoipcallactivecrc', 'cvvoipcallactiverobustsorting', 'cvvoipcallactiveencap', 'cvvoipcallactiveinterleaving', 'cvvoipcallactiveptime', 'cvvoipcallactivechannels', 'cvvoipcallactivecodermode', 'cvvoipcallactivecallid', 'cvvoipcallactivecallreferenceid', 'ccvoipcallactivepolicyname', 'cvvoipcallactivereverseddirectionpeeraddress', 'cvvoipcallactivesessionid'], name, value)


    class Cvcallvolconntable(Entity):
        """
        This table represents the number of active
        call connections for each call connection type
        in the voice gateway.
        
        .. attribute:: cvcallvolconnentry
        
        	An entry in the cvCallVolConnTable indicates number of active calls for a call connection type in the voice gateway
        	**type**\: list of  		 :py:class:`Cvcallvolconnentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable.Cvcallvolconnentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable, self).__init__()

            self.yang_name = "cvCallVolConnTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallVolConnEntry", ("cvcallvolconnentry", CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable.Cvcallvolconnentry))])
            self._leafs = OrderedDict()

            self.cvcallvolconnentry = YList(self)
            self._segment_path = lambda: "cvCallVolConnTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable, [], name, value)


        class Cvcallvolconnentry(Entity):
            """
            An entry in the cvCallVolConnTable indicates
            number of active calls for a call connection type
            in the voice gateway.
            
            .. attribute:: cvcallvolconnindex  (key)
            
            	This object represents index to the cvCallVolConnTable
            	**type**\:  :py:class:`CvCallConnectionType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallConnectionType>`
            
            .. attribute:: cvcallvolconnactiveconnection
            
            	This object represents the total number of active calls for a connection type  in the voice gateway
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable.Cvcallvolconnentry, self).__init__()

                self.yang_name = "cvCallVolConnEntry"
                self.yang_parent_name = "cvCallVolConnTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcallvolconnindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcallvolconnindex', YLeaf(YType.enumeration, 'cvCallVolConnIndex')),
                    ('cvcallvolconnactiveconnection', YLeaf(YType.uint32, 'cvCallVolConnActiveConnection')),
                ])
                self.cvcallvolconnindex = None
                self.cvcallvolconnactiveconnection = None
                self._segment_path = lambda: "cvCallVolConnEntry" + "[cvCallVolConnIndex='" + str(self.cvcallvolconnindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallVolConnTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvolconntable.Cvcallvolconnentry, ['cvcallvolconnindex', 'cvcallvolconnactiveconnection'], name, value)


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
        	**type**\: list of  		 :py:class:`Cvcallvolifentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable.Cvcallvolifentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable, self).__init__()

            self.yang_name = "cvCallVolIfTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallVolIfEntry", ("cvcallvolifentry", CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable.Cvcallvolifentry))])
            self._leafs = OrderedDict()

            self.cvcallvolifentry = YList(self)
            self._segment_path = lambda: "cvCallVolIfTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable, [], name, value)


        class Cvcallvolifentry(Entity):
            """
            Each entry represents a row in cvCallVolIfTable
            and corresponds to the information about an IP 
            interface in the voice gateway.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cvcallvolmediaincomingcalls
            
            	This object represents the total number of inbound active media calls through this IP  interface
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolmediaoutgoingcalls
            
            	This object represents the total number of outbound active media calls through the IP  interface
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable.Cvcallvolifentry, self).__init__()

                self.yang_name = "cvCallVolIfEntry"
                self.yang_parent_name = "cvCallVolIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cvcallvolmediaincomingcalls', YLeaf(YType.uint32, 'cvCallVolMediaIncomingCalls')),
                    ('cvcallvolmediaoutgoingcalls', YLeaf(YType.uint32, 'cvCallVolMediaOutgoingCalls')),
                ])
                self.ifindex = None
                self.cvcallvolmediaincomingcalls = None
                self.cvcallvolmediaoutgoingcalls = None
                self._segment_path = lambda: "cvCallVolIfEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallVolIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallvoliftable.Cvcallvolifentry, ['ifindex', 'cvcallvolmediaincomingcalls', 'cvcallvolmediaoutgoingcalls'], name, value)


    class Cvcallhistorytable(Entity):
        """
        This table is the voice extension to the call history table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information such as voice packet statistics,
        coder usage and end to end bandwidth of the call leg.
        
        .. attribute:: cvcallhistoryentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains the call establishment to a voice encapsulation peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvcallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable.Cvcallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable, self).__init__()

            self.yang_name = "cvCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallHistoryEntry", ("cvcallhistoryentry", CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable.Cvcallhistoryentry))])
            self._leafs = OrderedDict()

            self.cvcallhistoryentry = YList(self)
            self._segment_path = lambda: "cvCallHistoryTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable, [], name, value)


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
            
            .. attribute:: ccallhistoryindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvcallhistoryconnectionid
            
            	The global connection identifier for the telephony leg, which was assigned to the call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvcallhistorytxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallhistoryvoicetxduration
            
            	Duration for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallhistoryfaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            .. attribute:: cvcallhistorynoiselevel
            
            	The object contains the average noise level for the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            	**units**\: dBm
            
            .. attribute:: cvcallhistoryacomlevel
            
            	The object contains the average ACOM level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..127
            
            	**units**\: dB
            
            .. attribute:: cvcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg via telephony interface
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cvcallhistoryimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: pages
            
            .. attribute:: cvcallhistorycallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            .. attribute:: cvcallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\: bool
            
            .. attribute:: cvcallhistoryaccountcode
            
            	The object indicates the account code input to the call. It could be used by down stream billing server. The value of empty string indicates no account code input
            	**type**\: str
            
            	**length:** 0..50
            
            .. attribute:: cvcallhistorycallid
            
            	This object represents the call identifier for the telephony leg, which was assigned to the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable.Cvcallhistoryentry, self).__init__()

                self.yang_name = "cvCallHistoryEntry"
                self.yang_parent_name = "cvCallHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccallhistoryindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccallhistoryindex', YLeaf(YType.str, 'cCallHistoryIndex')),
                    ('cvcallhistoryconnectionid', YLeaf(YType.str, 'cvCallHistoryConnectionId')),
                    ('cvcallhistorytxduration', YLeaf(YType.uint32, 'cvCallHistoryTxDuration')),
                    ('cvcallhistoryvoicetxduration', YLeaf(YType.uint32, 'cvCallHistoryVoiceTxDuration')),
                    ('cvcallhistoryfaxtxduration', YLeaf(YType.uint32, 'cvCallHistoryFaxTxDuration')),
                    ('cvcallhistorycodertyperate', YLeaf(YType.enumeration, 'cvCallHistoryCoderTypeRate')),
                    ('cvcallhistorynoiselevel', YLeaf(YType.int32, 'cvCallHistoryNoiseLevel')),
                    ('cvcallhistoryacomlevel', YLeaf(YType.int32, 'cvCallHistoryACOMLevel')),
                    ('cvcallhistorysessiontarget', YLeaf(YType.str, 'cvCallHistorySessionTarget')),
                    ('cvcallhistoryimgpagecount', YLeaf(YType.uint32, 'cvCallHistoryImgPageCount')),
                    ('cvcallhistorycallingname', YLeaf(YType.str, 'cvCallHistoryCallingName')),
                    ('cvcallhistorycalleridblock', YLeaf(YType.boolean, 'cvCallHistoryCallerIDBlock')),
                    ('cvcallhistoryaccountcode', YLeaf(YType.str, 'cvCallHistoryAccountCode')),
                    ('cvcallhistorycallid', YLeaf(YType.uint32, 'cvCallHistoryCallId')),
                ])
                self.ccallhistoryindex = None
                self.cvcallhistoryconnectionid = None
                self.cvcallhistorytxduration = None
                self.cvcallhistoryvoicetxduration = None
                self.cvcallhistoryfaxtxduration = None
                self.cvcallhistorycodertyperate = None
                self.cvcallhistorynoiselevel = None
                self.cvcallhistoryacomlevel = None
                self.cvcallhistorysessiontarget = None
                self.cvcallhistoryimgpagecount = None
                self.cvcallhistorycallingname = None
                self.cvcallhistorycalleridblock = None
                self.cvcallhistoryaccountcode = None
                self.cvcallhistorycallid = None
                self._segment_path = lambda: "cvCallHistoryEntry" + "[cCallHistoryIndex='" + str(self.ccallhistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallhistorytable.Cvcallhistoryentry, ['ccallhistoryindex', 'cvcallhistoryconnectionid', 'cvcallhistorytxduration', 'cvcallhistoryvoicetxduration', 'cvcallhistoryfaxtxduration', 'cvcallhistorycodertyperate', 'cvcallhistorynoiselevel', 'cvcallhistoryacomlevel', 'cvcallhistorysessiontarget', 'cvcallhistoryimgpagecount', 'cvcallhistorycallingname', 'cvcallhistorycalleridblock', 'cvcallhistoryaccountcode', 'cvcallhistorycallid'], name, value)


    class Cvvoipcallhistorytable(Entity):
        """
        This table is the VoIP extension to the call history table
        of IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallhistoryentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains information for the call establishment to the peer on the IP backbone via a voice over IP peer. The entry is deleted when its associated call history entry in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvvoipcallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable.Cvvoipcallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable, self).__init__()

            self.yang_name = "cvVoIPCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvVoIPCallHistoryEntry", ("cvvoipcallhistoryentry", CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable.Cvvoipcallhistoryentry))])
            self._leafs = OrderedDict()

            self.cvvoipcallhistoryentry = YList(self)
            self._segment_path = lambda: "cvVoIPCallHistoryTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable, [], name, value)


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
            
            .. attribute:: ccallhistoryindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvvoipcallhistoryconnectionid
            
            	The global connection identifier for the VoIP leg, which was assigned to the call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallhistoryremoteipaddress
            
            	Remote system IP address for the call
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets for the call
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryselectedqos
            
            	The selected RSVP QoS for the call
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            .. attribute:: cvvoipcallhistorysessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\:  :py:class:`CvSessionProtocol <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol>`
            
            .. attribute:: cvvoipcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the Voice over IP call
            	**type**\: str
            
            .. attribute:: cvvoipcallhistoryontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or  frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorygapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryhiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorylowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistoryreceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            	**status**\: deprecated
            
            .. attribute:: cvvoipcallhistoryicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the call = Itotal (total impairment value) of the call \- A (Expectation Factor) in the cvVoIPPeerCfgExpectFactor of the call leg associated peer. A value of \-1 implies that Icpif was not calculated and is meaningless for this call
            	**type**\: int
            
            	**range:** \-1..55
            
            	**units**\: equipment impairment factor (eif)
            
            .. attribute:: cvvoipcallhistorylostpackets
            
            	The number of lost voice packets during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistoryearlypackets
            
            	The number of received voice packets that are arrived too early to store in jitter buffer during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistorylatepackets
            
            	The number of received voice packets that are arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvvoipcallhistoryusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvvoipcallhistoryprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemSigIPAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvvoipcallhistoryremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemMediaIPAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvvoipcallhistoryremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvvoipcallhistoryremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistorysrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryfallbackicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the fallback probe = Itotal (total impairment value)  \- configured fallback (Expectation Factor). A value of 0 implies that Icpif was not calculated and is meaningless for this attempt
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cvvoipcallhistoryfallbackloss
            
            	FallbackLoss is the percentage of loss packets based on the total packets sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryfallbackdelay
            
            	The FallbackDelay is calculated as follows \- Take the sum of the round trips for all the probes,  divide by the number of probes,  and divide by two to get the one\-way delay.   Then add in jitter\_in or jiter\_out, which ever is higher
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistorybitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  :py:class:`CvAmrNbBitRateMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode>`
            
            .. attribute:: cvvoipcallhistorymodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallhistorymodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallHistoryBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallHistoryBitRates object. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistorymaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorycrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryrobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\:  :py:class:`CvAmrNbRtpEncap <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbRtpEncap>`
            
            .. attribute:: cvvoipcallhistoryinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..50
            
            	**units**\: frame-blocks
            
            .. attribute:: cvvoipcallhistoryptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorychannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..6
            
            	**units**\: channels
            
            .. attribute:: cvvoipcallhistorycodermode
            
            	The object indicates the iLBC mode. The value of this object is valid only if  cvVoIPCallHistoryCoderTypeRate is equal to  'iLBC'
            	**type**\:  :py:class:`CvIlbcFrameMode <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode>`
            
            	**units**\: milliseconds
            
            .. attribute:: cvvoipcallhistorycallid
            
            	This object represents the call identifier for the VoIP leg, which was assigned to the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallhistorycallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.   For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorysessionid
            
            	This object indicates the session ID assigned by the call manager to identify call legs that belong to the same call session.  This session ID (history) represents a completed call session, whereas the active session ID (cvVoIPCallActiveSessionId) represents an ongoing session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable.Cvvoipcallhistoryentry, self).__init__()

                self.yang_name = "cvVoIPCallHistoryEntry"
                self.yang_parent_name = "cvVoIPCallHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccallhistoryindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccallhistoryindex', YLeaf(YType.str, 'cCallHistoryIndex')),
                    ('cvvoipcallhistoryconnectionid', YLeaf(YType.str, 'cvVoIPCallHistoryConnectionId')),
                    ('cvvoipcallhistoryremoteipaddress', YLeaf(YType.str, 'cvVoIPCallHistoryRemoteIPAddress')),
                    ('cvvoipcallhistoryremoteudpport', YLeaf(YType.int32, 'cvVoIPCallHistoryRemoteUDPPort')),
                    ('cvvoipcallhistoryroundtripdelay', YLeaf(YType.uint32, 'cvVoIPCallHistoryRoundTripDelay')),
                    ('cvvoipcallhistoryselectedqos', YLeaf(YType.enumeration, 'cvVoIPCallHistorySelectedQoS')),
                    ('cvvoipcallhistorysessionprotocol', YLeaf(YType.enumeration, 'cvVoIPCallHistorySessionProtocol')),
                    ('cvvoipcallhistorysessiontarget', YLeaf(YType.str, 'cvVoIPCallHistorySessionTarget')),
                    ('cvvoipcallhistoryontimervplayout', YLeaf(YType.uint32, 'cvVoIPCallHistoryOnTimeRvPlayout')),
                    ('cvvoipcallhistorygapfillwithsilence', YLeaf(YType.uint32, 'cvVoIPCallHistoryGapFillWithSilence')),
                    ('cvvoipcallhistorygapfillwithprediction', YLeaf(YType.uint32, 'cvVoIPCallHistoryGapFillWithPrediction')),
                    ('cvvoipcallhistorygapfillwithinterpolation', YLeaf(YType.uint32, 'cvVoIPCallHistoryGapFillWithInterpolation')),
                    ('cvvoipcallhistorygapfillwithredundancy', YLeaf(YType.uint32, 'cvVoIPCallHistoryGapFillWithRedundancy')),
                    ('cvvoipcallhistoryhiwaterplayoutdelay', YLeaf(YType.uint32, 'cvVoIPCallHistoryHiWaterPlayoutDelay')),
                    ('cvvoipcallhistorylowaterplayoutdelay', YLeaf(YType.uint32, 'cvVoIPCallHistoryLoWaterPlayoutDelay')),
                    ('cvvoipcallhistoryreceivedelay', YLeaf(YType.uint32, 'cvVoIPCallHistoryReceiveDelay')),
                    ('cvvoipcallhistoryvadenable', YLeaf(YType.boolean, 'cvVoIPCallHistoryVADEnable')),
                    ('cvvoipcallhistorycodertyperate', YLeaf(YType.enumeration, 'cvVoIPCallHistoryCoderTypeRate')),
                    ('cvvoipcallhistoryicpif', YLeaf(YType.int32, 'cvVoIPCallHistoryIcpif')),
                    ('cvvoipcallhistorylostpackets', YLeaf(YType.uint32, 'cvVoIPCallHistoryLostPackets')),
                    ('cvvoipcallhistoryearlypackets', YLeaf(YType.uint32, 'cvVoIPCallHistoryEarlyPackets')),
                    ('cvvoipcallhistorylatepackets', YLeaf(YType.uint32, 'cvVoIPCallHistoryLatePackets')),
                    ('cvvoipcallhistoryusername', YLeaf(YType.str, 'cvVoIPCallHistoryUsername')),
                    ('cvvoipcallhistoryprotocolcallid', YLeaf(YType.str, 'cvVoIPCallHistoryProtocolCallId')),
                    ('cvvoipcallhistoryremsigipaddrt', YLeaf(YType.enumeration, 'cvVoIPCallHistoryRemSigIPAddrT')),
                    ('cvvoipcallhistoryremsigipaddr', YLeaf(YType.str, 'cvVoIPCallHistoryRemSigIPAddr')),
                    ('cvvoipcallhistoryremsigport', YLeaf(YType.int32, 'cvVoIPCallHistoryRemSigPort')),
                    ('cvvoipcallhistoryremmediaipaddrt', YLeaf(YType.enumeration, 'cvVoIPCallHistoryRemMediaIPAddrT')),
                    ('cvvoipcallhistoryremmediaipaddr', YLeaf(YType.str, 'cvVoIPCallHistoryRemMediaIPAddr')),
                    ('cvvoipcallhistoryremmediaport', YLeaf(YType.int32, 'cvVoIPCallHistoryRemMediaPort')),
                    ('cvvoipcallhistorysrtpenable', YLeaf(YType.boolean, 'cvVoIPCallHistorySRTPEnable')),
                    ('cvvoipcallhistoryfallbackicpif', YLeaf(YType.int32, 'cvVoIPCallHistoryFallbackIcpif')),
                    ('cvvoipcallhistoryfallbackloss', YLeaf(YType.uint32, 'cvVoIPCallHistoryFallbackLoss')),
                    ('cvvoipcallhistoryfallbackdelay', YLeaf(YType.uint32, 'cvVoIPCallHistoryFallbackDelay')),
                    ('cvvoipcallhistoryoctetaligned', YLeaf(YType.boolean, 'cvVoIPCallHistoryOctetAligned')),
                    ('cvvoipcallhistorybitrates', YLeaf(YType.bits, 'cvVoIPCallHistoryBitRates')),
                    ('cvvoipcallhistorymodechgperiod', YLeaf(YType.int32, 'cvVoIPCallHistoryModeChgPeriod')),
                    ('cvvoipcallhistorymodechgneighbor', YLeaf(YType.boolean, 'cvVoIPCallHistoryModeChgNeighbor')),
                    ('cvvoipcallhistorymaxptime', YLeaf(YType.int32, 'cvVoIPCallHistoryMaxPtime')),
                    ('cvvoipcallhistorycrc', YLeaf(YType.boolean, 'cvVoIPCallHistoryCRC')),
                    ('cvvoipcallhistoryrobustsorting', YLeaf(YType.boolean, 'cvVoIPCallHistoryRobustSorting')),
                    ('cvvoipcallhistoryencap', YLeaf(YType.enumeration, 'cvVoIPCallHistoryEncap')),
                    ('cvvoipcallhistoryinterleaving', YLeaf(YType.int32, 'cvVoIPCallHistoryInterleaving')),
                    ('cvvoipcallhistoryptime', YLeaf(YType.int32, 'cvVoIPCallHistoryPtime')),
                    ('cvvoipcallhistorychannels', YLeaf(YType.int32, 'cvVoIPCallHistoryChannels')),
                    ('cvvoipcallhistorycodermode', YLeaf(YType.enumeration, 'cvVoIPCallHistoryCoderMode')),
                    ('cvvoipcallhistorycallid', YLeaf(YType.uint32, 'cvVoIPCallHistoryCallId')),
                    ('cvvoipcallhistorycallreferenceid', YLeaf(YType.uint32, 'cvVoIPCallHistoryCallReferenceId')),
                    ('cvvoipcallhistorysessionid', YLeaf(YType.uint32, 'cvVoIPCallHistorySessionId')),
                ])
                self.ccallhistoryindex = None
                self.cvvoipcallhistoryconnectionid = None
                self.cvvoipcallhistoryremoteipaddress = None
                self.cvvoipcallhistoryremoteudpport = None
                self.cvvoipcallhistoryroundtripdelay = None
                self.cvvoipcallhistoryselectedqos = None
                self.cvvoipcallhistorysessionprotocol = None
                self.cvvoipcallhistorysessiontarget = None
                self.cvvoipcallhistoryontimervplayout = None
                self.cvvoipcallhistorygapfillwithsilence = None
                self.cvvoipcallhistorygapfillwithprediction = None
                self.cvvoipcallhistorygapfillwithinterpolation = None
                self.cvvoipcallhistorygapfillwithredundancy = None
                self.cvvoipcallhistoryhiwaterplayoutdelay = None
                self.cvvoipcallhistorylowaterplayoutdelay = None
                self.cvvoipcallhistoryreceivedelay = None
                self.cvvoipcallhistoryvadenable = None
                self.cvvoipcallhistorycodertyperate = None
                self.cvvoipcallhistoryicpif = None
                self.cvvoipcallhistorylostpackets = None
                self.cvvoipcallhistoryearlypackets = None
                self.cvvoipcallhistorylatepackets = None
                self.cvvoipcallhistoryusername = None
                self.cvvoipcallhistoryprotocolcallid = None
                self.cvvoipcallhistoryremsigipaddrt = None
                self.cvvoipcallhistoryremsigipaddr = None
                self.cvvoipcallhistoryremsigport = None
                self.cvvoipcallhistoryremmediaipaddrt = None
                self.cvvoipcallhistoryremmediaipaddr = None
                self.cvvoipcallhistoryremmediaport = None
                self.cvvoipcallhistorysrtpenable = None
                self.cvvoipcallhistoryfallbackicpif = None
                self.cvvoipcallhistoryfallbackloss = None
                self.cvvoipcallhistoryfallbackdelay = None
                self.cvvoipcallhistoryoctetaligned = None
                self.cvvoipcallhistorybitrates = Bits()
                self.cvvoipcallhistorymodechgperiod = None
                self.cvvoipcallhistorymodechgneighbor = None
                self.cvvoipcallhistorymaxptime = None
                self.cvvoipcallhistorycrc = None
                self.cvvoipcallhistoryrobustsorting = None
                self.cvvoipcallhistoryencap = None
                self.cvvoipcallhistoryinterleaving = None
                self.cvvoipcallhistoryptime = None
                self.cvvoipcallhistorychannels = None
                self.cvvoipcallhistorycodermode = None
                self.cvvoipcallhistorycallid = None
                self.cvvoipcallhistorycallreferenceid = None
                self.cvvoipcallhistorysessionid = None
                self._segment_path = lambda: "cvVoIPCallHistoryEntry" + "[cCallHistoryIndex='" + str(self.ccallhistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvVoIPCallHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvvoipcallhistorytable.Cvvoipcallhistoryentry, ['ccallhistoryindex', 'cvvoipcallhistoryconnectionid', 'cvvoipcallhistoryremoteipaddress', 'cvvoipcallhistoryremoteudpport', 'cvvoipcallhistoryroundtripdelay', 'cvvoipcallhistoryselectedqos', 'cvvoipcallhistorysessionprotocol', 'cvvoipcallhistorysessiontarget', 'cvvoipcallhistoryontimervplayout', 'cvvoipcallhistorygapfillwithsilence', 'cvvoipcallhistorygapfillwithprediction', 'cvvoipcallhistorygapfillwithinterpolation', 'cvvoipcallhistorygapfillwithredundancy', 'cvvoipcallhistoryhiwaterplayoutdelay', 'cvvoipcallhistorylowaterplayoutdelay', 'cvvoipcallhistoryreceivedelay', 'cvvoipcallhistoryvadenable', 'cvvoipcallhistorycodertyperate', 'cvvoipcallhistoryicpif', 'cvvoipcallhistorylostpackets', 'cvvoipcallhistoryearlypackets', 'cvvoipcallhistorylatepackets', 'cvvoipcallhistoryusername', 'cvvoipcallhistoryprotocolcallid', 'cvvoipcallhistoryremsigipaddrt', 'cvvoipcallhistoryremsigipaddr', 'cvvoipcallhistoryremsigport', 'cvvoipcallhistoryremmediaipaddrt', 'cvvoipcallhistoryremmediaipaddr', 'cvvoipcallhistoryremmediaport', 'cvvoipcallhistorysrtpenable', 'cvvoipcallhistoryfallbackicpif', 'cvvoipcallhistoryfallbackloss', 'cvvoipcallhistoryfallbackdelay', 'cvvoipcallhistoryoctetaligned', 'cvvoipcallhistorybitrates', 'cvvoipcallhistorymodechgperiod', 'cvvoipcallhistorymodechgneighbor', 'cvvoipcallhistorymaxptime', 'cvvoipcallhistorycrc', 'cvvoipcallhistoryrobustsorting', 'cvvoipcallhistoryencap', 'cvvoipcallhistoryinterleaving', 'cvvoipcallhistoryptime', 'cvvoipcallhistorychannels', 'cvvoipcallhistorycodermode', 'cvvoipcallhistorycallid', 'cvvoipcallhistorycallreferenceid', 'cvvoipcallhistorysessionid'], name, value)


    class Cvcallratestatstable(Entity):
        """
        This table represents voice call rate measurement in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcallratestatsentry
        
        	This is a conceptual\-row in cvCallRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of  		 :py:class:`Cvcallratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable.Cvcallratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable, self).__init__()

            self.yang_name = "cvCallRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallRateStatsEntry", ("cvcallratestatsentry", CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable.Cvcallratestatsentry))])
            self._leafs = OrderedDict()

            self.cvcallratestatsentry = YList(self)
            self._segment_path = lambda: "cvCallRateStatsTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable, [], name, value)


        class Cvcallratestatsentry(Entity):
            """
            This is a conceptual\-row in cvCallRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcallratestatsintvldurunits  (key)
            
            	The Object indexes in Call Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:  :py:class:`CvCallVolumeStatsIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType>`
            
            .. attribute:: cvcallratestatsintvldur  (key)
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcallratestatsmaxval
            
            	This object indicates the maximum calls per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls-per-second
            
            .. attribute:: cvcallratestatsavgval
            
            	This object indicates the average calls per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls-per-second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable.Cvcallratestatsentry, self).__init__()

                self.yang_name = "cvCallRateStatsEntry"
                self.yang_parent_name = "cvCallRateStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcallratestatsintvldurunits','cvcallratestatsintvldur']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcallratestatsintvldurunits', YLeaf(YType.enumeration, 'cvCallRateStatsIntvlDurUnits')),
                    ('cvcallratestatsintvldur', YLeaf(YType.uint32, 'cvCallRateStatsIntvlDur')),
                    ('cvcallratestatsmaxval', YLeaf(YType.uint32, 'cvCallRateStatsMaxVal')),
                    ('cvcallratestatsavgval', YLeaf(YType.uint32, 'cvCallRateStatsAvgVal')),
                ])
                self.cvcallratestatsintvldurunits = None
                self.cvcallratestatsintvldur = None
                self.cvcallratestatsmaxval = None
                self.cvcallratestatsavgval = None
                self._segment_path = lambda: "cvCallRateStatsEntry" + "[cvCallRateStatsIntvlDurUnits='" + str(self.cvcallratestatsintvldurunits) + "']" + "[cvCallRateStatsIntvlDur='" + str(self.cvcallratestatsintvldur) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallRateStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallratestatstable.Cvcallratestatsentry, ['cvcallratestatsintvldurunits', 'cvcallratestatsintvldur', 'cvcallratestatsmaxval', 'cvcallratestatsavgval'], name, value)


    class Cvcalllegratestatstable(Entity):
        """
        cvCallLegRateStatsTable table represents voice call leg rate
        measurement in various interval lengths defined by 
        the CvCallVolumeStatsIntvlType object.
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcalllegratestatsentry
        
        	This is a conceptual\-row in cvCallLegRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of  		 :py:class:`Cvcalllegratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable.Cvcalllegratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable, self).__init__()

            self.yang_name = "cvCallLegRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallLegRateStatsEntry", ("cvcalllegratestatsentry", CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable.Cvcalllegratestatsentry))])
            self._leafs = OrderedDict()

            self.cvcalllegratestatsentry = YList(self)
            self._segment_path = lambda: "cvCallLegRateStatsTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable, [], name, value)


        class Cvcalllegratestatsentry(Entity):
            """
            This is a conceptual\-row in cvCallLegRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalllegratestatsintvldurunits  (key)
            
            	The Object indexes in Call Leg Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:  :py:class:`CvCallVolumeStatsIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType>`
            
            .. attribute:: cvcalllegratestatsintvldur  (key)
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcalllegratestatsmaxval
            
            	This object indicates the maximum call\-legs per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: call-legs per second
            
            .. attribute:: cvcalllegratestatsavgval
            
            	This object indicates the average call\-legs per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: call-legs per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable.Cvcalllegratestatsentry, self).__init__()

                self.yang_name = "cvCallLegRateStatsEntry"
                self.yang_parent_name = "cvCallLegRateStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcalllegratestatsintvldurunits','cvcalllegratestatsintvldur']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcalllegratestatsintvldurunits', YLeaf(YType.enumeration, 'cvCallLegRateStatsIntvlDurUnits')),
                    ('cvcalllegratestatsintvldur', YLeaf(YType.uint32, 'cvCallLegRateStatsIntvlDur')),
                    ('cvcalllegratestatsmaxval', YLeaf(YType.uint32, 'cvCallLegRateStatsMaxVal')),
                    ('cvcalllegratestatsavgval', YLeaf(YType.uint32, 'cvCallLegRateStatsAvgVal')),
                ])
                self.cvcalllegratestatsintvldurunits = None
                self.cvcalllegratestatsintvldur = None
                self.cvcalllegratestatsmaxval = None
                self.cvcalllegratestatsavgval = None
                self._segment_path = lambda: "cvCallLegRateStatsEntry" + "[cvCallLegRateStatsIntvlDurUnits='" + str(self.cvcalllegratestatsintvldurunits) + "']" + "[cvCallLegRateStatsIntvlDur='" + str(self.cvcalllegratestatsintvldur) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallLegRateStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalllegratestatstable.Cvcalllegratestatsentry, ['cvcalllegratestatsintvldurunits', 'cvcalllegratestatsintvldur', 'cvcalllegratestatsmaxval', 'cvcalllegratestatsavgval'], name, value)


    class Cvactivecallstatstable(Entity):
        """
        This table represents the active voice calls in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvactivecallstatsentry
        
        	This is a conceptual\-row in cvActiveCallStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of  		 :py:class:`Cvactivecallstatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable.Cvactivecallstatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable, self).__init__()

            self.yang_name = "cvActiveCallStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvActiveCallStatsEntry", ("cvactivecallstatsentry", CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable.Cvactivecallstatsentry))])
            self._leafs = OrderedDict()

            self.cvactivecallstatsentry = YList(self)
            self._segment_path = lambda: "cvActiveCallStatsTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable, [], name, value)


        class Cvactivecallstatsentry(Entity):
            """
            This is a conceptual\-row in cvActiveCallStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvactivecallstatsintvldurunits  (key)
            
            	The Object indexes in Active Call Rate Table (con\-current calls table) to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:  :py:class:`CvCallVolumeStatsIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType>`
            
            .. attribute:: cvactivecallstatsintvldur  (key)
            
            	This is an index that references to the different past periods in given in interval of active call table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvactivecallstatsmaxval
            
            	This object indicates the maximum number of active call that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvactivecallstatsavgval
            
            	This object indicates the average number of active calls that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable.Cvactivecallstatsentry, self).__init__()

                self.yang_name = "cvActiveCallStatsEntry"
                self.yang_parent_name = "cvActiveCallStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvactivecallstatsintvldurunits','cvactivecallstatsintvldur']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvactivecallstatsintvldurunits', YLeaf(YType.enumeration, 'cvActiveCallStatsIntvlDurUnits')),
                    ('cvactivecallstatsintvldur', YLeaf(YType.uint32, 'cvActiveCallStatsIntvlDur')),
                    ('cvactivecallstatsmaxval', YLeaf(YType.uint32, 'cvActiveCallStatsMaxVal')),
                    ('cvactivecallstatsavgval', YLeaf(YType.uint32, 'cvActiveCallStatsAvgVal')),
                ])
                self.cvactivecallstatsintvldurunits = None
                self.cvactivecallstatsintvldur = None
                self.cvactivecallstatsmaxval = None
                self.cvactivecallstatsavgval = None
                self._segment_path = lambda: "cvActiveCallStatsEntry" + "[cvActiveCallStatsIntvlDurUnits='" + str(self.cvactivecallstatsintvldurunits) + "']" + "[cvActiveCallStatsIntvlDur='" + str(self.cvactivecallstatsintvldur) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvActiveCallStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvactivecallstatstable.Cvactivecallstatsentry, ['cvactivecallstatsintvldurunits', 'cvactivecallstatsintvldur', 'cvactivecallstatsmaxval', 'cvactivecallstatsavgval'], name, value)


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
        	**type**\: list of  		 :py:class:`Cvcalldurationstatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable.Cvcalldurationstatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable, self).__init__()

            self.yang_name = "cvCallDurationStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallDurationStatsEntry", ("cvcalldurationstatsentry", CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable.Cvcalldurationstatsentry))])
            self._leafs = OrderedDict()

            self.cvcalldurationstatsentry = YList(self)
            self._segment_path = lambda: "cvCallDurationStatsTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable, [], name, value)


        class Cvcalldurationstatsentry(Entity):
            """
            This is a conceptual\-row in cvCallDurationStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalldurationstatsintvldurunits  (key)
            
            	The Object indexes in Call Duration Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:  :py:class:`CvCallVolumeStatsIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType>`
            
            .. attribute:: cvcalldurationstatsintvldur  (key)
            
            	This is an index that references to the different past periods in given in interval of call Duration table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcalldurationstatsmaxval
            
            	This object indicates the maximum number of calls having a duration which is below the threshold for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvcalldurationstatsavgval
            
            	This object indicates the average number of calls having a duration which is below the threshold for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable.Cvcalldurationstatsentry, self).__init__()

                self.yang_name = "cvCallDurationStatsEntry"
                self.yang_parent_name = "cvCallDurationStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcalldurationstatsintvldurunits','cvcalldurationstatsintvldur']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcalldurationstatsintvldurunits', YLeaf(YType.enumeration, 'cvCallDurationStatsIntvlDurUnits')),
                    ('cvcalldurationstatsintvldur', YLeaf(YType.uint32, 'cvCallDurationStatsIntvlDur')),
                    ('cvcalldurationstatsmaxval', YLeaf(YType.uint32, 'cvCallDurationStatsMaxVal')),
                    ('cvcalldurationstatsavgval', YLeaf(YType.uint32, 'cvCallDurationStatsAvgVal')),
                ])
                self.cvcalldurationstatsintvldurunits = None
                self.cvcalldurationstatsintvldur = None
                self.cvcalldurationstatsmaxval = None
                self.cvcalldurationstatsavgval = None
                self._segment_path = lambda: "cvCallDurationStatsEntry" + "[cvCallDurationStatsIntvlDurUnits='" + str(self.cvcalldurationstatsintvldurunits) + "']" + "[cvCallDurationStatsIntvlDur='" + str(self.cvcalldurationstatsintvldur) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallDurationStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalldurationstatstable.Cvcalldurationstatsentry, ['cvcalldurationstatsintvldurunits', 'cvcalldurationstatsintvldur', 'cvcalldurationstatsmaxval', 'cvcalldurationstatsavgval'], name, value)


    class Cvsipmsgratestatstable(Entity):
        """
        This table represents the SIP message rate measurement in
        various interval length defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratestatsentry
        
        	This is a conceptual\-row in cvSipMsgRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of  		 :py:class:`Cvsipmsgratestatsentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable.Cvsipmsgratestatsentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable, self).__init__()

            self.yang_name = "cvSipMsgRateStatsTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvSipMsgRateStatsEntry", ("cvsipmsgratestatsentry", CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable.Cvsipmsgratestatsentry))])
            self._leafs = OrderedDict()

            self.cvsipmsgratestatsentry = YList(self)
            self._segment_path = lambda: "cvSipMsgRateStatsTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable, [], name, value)


        class Cvsipmsgratestatsentry(Entity):
            """
            This is a conceptual\-row in cvSipMsgRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvsipmsgratestatsintvldurunits  (key)
            
            	The Object indexes in SIP Message Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\:  :py:class:`CvCallVolumeStatsIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType>`
            
            .. attribute:: cvsipmsgratestatsintvldur  (key)
            
            	This is an index that references to the different past periods in given in interval of SIP message rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvsipmsgratestatsmaxval
            
            	This object indicates the maximum SIP messages  per second that is received for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            .. attribute:: cvsipmsgratestatsavgval
            
            	This object indicates the average SIP messages per second that is received for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable.Cvsipmsgratestatsentry, self).__init__()

                self.yang_name = "cvSipMsgRateStatsEntry"
                self.yang_parent_name = "cvSipMsgRateStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvsipmsgratestatsintvldurunits','cvsipmsgratestatsintvldur']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvsipmsgratestatsintvldurunits', YLeaf(YType.enumeration, 'cvSipMsgRateStatsIntvlDurUnits')),
                    ('cvsipmsgratestatsintvldur', YLeaf(YType.uint32, 'cvSipMsgRateStatsIntvlDur')),
                    ('cvsipmsgratestatsmaxval', YLeaf(YType.uint32, 'cvSipMsgRateStatsMaxVal')),
                    ('cvsipmsgratestatsavgval', YLeaf(YType.uint32, 'cvSipMsgRateStatsAvgVal')),
                ])
                self.cvsipmsgratestatsintvldurunits = None
                self.cvsipmsgratestatsintvldur = None
                self.cvsipmsgratestatsmaxval = None
                self.cvsipmsgratestatsavgval = None
                self._segment_path = lambda: "cvSipMsgRateStatsEntry" + "[cvSipMsgRateStatsIntvlDurUnits='" + str(self.cvsipmsgratestatsintvldurunits) + "']" + "[cvSipMsgRateStatsIntvlDur='" + str(self.cvsipmsgratestatsintvldur) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvSipMsgRateStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratestatstable.Cvsipmsgratestatsentry, ['cvsipmsgratestatsintvldurunits', 'cvsipmsgratestatsintvldur', 'cvsipmsgratestatsmaxval', 'cvsipmsgratestatsavgval'], name, value)


    class Cvcallratewmtable(Entity):
        """
        This table represents high watermarks achieved
        by call rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcallratewmentry
        
        	This is a conceptual\-row in cvCallRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of  		 :py:class:`Cvcallratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable.Cvcallratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable, self).__init__()

            self.yang_name = "cvCallRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallRateWMEntry", ("cvcallratewmentry", CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable.Cvcallratewmentry))])
            self._leafs = OrderedDict()

            self.cvcallratewmentry = YList(self)
            self._segment_path = lambda: "cvCallRateWMTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable, [], name, value)


        class Cvcallratewmentry(Entity):
            """
            This is a conceptual\-row in cvCallRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcallratewmintvldurunits  (key)
            
            	The Object indexes in call rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:  :py:class:`CvCallVolumeWMIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType>`
            
            .. attribute:: cvcallratewmindex  (key)
            
            	This is an index that references to different peaks in past period in call rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvcallratewmvalue
            
            	This object indicates high watermark value achieved by the calls per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls per second
            
            .. attribute:: cvcallratewmts
            
            	This object indicates date and Time when the high watermark is achieved for calls per second for the given interval
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable.Cvcallratewmentry, self).__init__()

                self.yang_name = "cvCallRateWMEntry"
                self.yang_parent_name = "cvCallRateWMTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcallratewmintvldurunits','cvcallratewmindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcallratewmintvldurunits', YLeaf(YType.enumeration, 'cvCallRateWMIntvlDurUnits')),
                    ('cvcallratewmindex', YLeaf(YType.uint32, 'cvCallRateWMIndex')),
                    ('cvcallratewmvalue', YLeaf(YType.uint32, 'cvCallRateWMValue')),
                    ('cvcallratewmts', YLeaf(YType.str, 'cvCallRateWMts')),
                ])
                self.cvcallratewmintvldurunits = None
                self.cvcallratewmindex = None
                self.cvcallratewmvalue = None
                self.cvcallratewmts = None
                self._segment_path = lambda: "cvCallRateWMEntry" + "[cvCallRateWMIntvlDurUnits='" + str(self.cvcallratewmintvldurunits) + "']" + "[cvCallRateWMIndex='" + str(self.cvcallratewmindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallRateWMTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcallratewmtable.Cvcallratewmentry, ['cvcallratewmintvldurunits', 'cvcallratewmindex', 'cvcallratewmvalue', 'cvcallratewmts'], name, value)


    class Cvcalllegratewmtable(Entity):
        """
        cvCallLegRateWMTable table represents high watermarks achieved
        by call\-leg rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcalllegratewmentry
        
        	This is a conceptual\-row in cvCallLegRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of  		 :py:class:`Cvcalllegratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable.Cvcalllegratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable, self).__init__()

            self.yang_name = "cvCallLegRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCallLegRateWMEntry", ("cvcalllegratewmentry", CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable.Cvcalllegratewmentry))])
            self._leafs = OrderedDict()

            self.cvcalllegratewmentry = YList(self)
            self._segment_path = lambda: "cvCallLegRateWMTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable, [], name, value)


        class Cvcalllegratewmentry(Entity):
            """
            This is a conceptual\-row in cvCallLegRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcalllegratewmintvldurunits  (key)
            
            	The Object indexes in call leg rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:  :py:class:`CvCallVolumeWMIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType>`
            
            .. attribute:: cvcalllegratewmindex  (key)
            
            	This is an index that references to different peaks in past period in call leg rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvcalllegratewmvalue
            
            	This object indicates high watermark value achieved by the call legs per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: call legs per second
            
            .. attribute:: cvcalllegratewmts
            
            	This object indicates date and time when the high watermark is achieved for call\-legs per second for the given interval
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable.Cvcalllegratewmentry, self).__init__()

                self.yang_name = "cvCallLegRateWMEntry"
                self.yang_parent_name = "cvCallLegRateWMTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvcalllegratewmintvldurunits','cvcalllegratewmindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvcalllegratewmintvldurunits', YLeaf(YType.enumeration, 'cvCallLegRateWMIntvlDurUnits')),
                    ('cvcalllegratewmindex', YLeaf(YType.uint32, 'cvCallLegRateWMIndex')),
                    ('cvcalllegratewmvalue', YLeaf(YType.uint32, 'cvCallLegRateWMValue')),
                    ('cvcalllegratewmts', YLeaf(YType.str, 'cvCallLegRateWMts')),
                ])
                self.cvcalllegratewmintvldurunits = None
                self.cvcalllegratewmindex = None
                self.cvcalllegratewmvalue = None
                self.cvcalllegratewmts = None
                self._segment_path = lambda: "cvCallLegRateWMEntry" + "[cvCallLegRateWMIntvlDurUnits='" + str(self.cvcalllegratewmintvldurunits) + "']" + "[cvCallLegRateWMIndex='" + str(self.cvcalllegratewmindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvCallLegRateWMTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvcalllegratewmtable.Cvcalllegratewmentry, ['cvcalllegratewmintvldurunits', 'cvcalllegratewmindex', 'cvcalllegratewmvalue', 'cvcalllegratewmts'], name, value)


    class Cvactivecallwmtable(Entity):
        """
        This table represents high watermarks achieved
        by active calls in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow 
        for detailed measurement to be collected.
        
        .. attribute:: cvactivecallwmentry
        
        	This is a conceptual\-row in cvActiveCallWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of  		 :py:class:`Cvactivecallwmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable.Cvactivecallwmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable, self).__init__()

            self.yang_name = "cvActiveCallWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvActiveCallWMEntry", ("cvactivecallwmentry", CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable.Cvactivecallwmentry))])
            self._leafs = OrderedDict()

            self.cvactivecallwmentry = YList(self)
            self._segment_path = lambda: "cvActiveCallWMTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable, [], name, value)


        class Cvactivecallwmentry(Entity):
            """
            This is a conceptual\-row in cvActiveCallWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvactivecallwmintvldurunits  (key)
            
            	The Object indexes in active call Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:  :py:class:`CvCallVolumeWMIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType>`
            
            .. attribute:: cvactivecallwmindex  (key)
            
            	This is an index that references to different peaks in past period in acive call watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvactivecallwmvalue
            
            	This object indicates high watermark value achieved by the active calls for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvactivecallwmts
            
            	This object indicates date and time when the high watermark is achieved for active calls for the given interval
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable.Cvactivecallwmentry, self).__init__()

                self.yang_name = "cvActiveCallWMEntry"
                self.yang_parent_name = "cvActiveCallWMTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvactivecallwmintvldurunits','cvactivecallwmindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvactivecallwmintvldurunits', YLeaf(YType.enumeration, 'cvActiveCallWMIntvlDurUnits')),
                    ('cvactivecallwmindex', YLeaf(YType.uint32, 'cvActiveCallWMIndex')),
                    ('cvactivecallwmvalue', YLeaf(YType.uint32, 'cvActiveCallWMValue')),
                    ('cvactivecallwmts', YLeaf(YType.str, 'cvActiveCallWMts')),
                ])
                self.cvactivecallwmintvldurunits = None
                self.cvactivecallwmindex = None
                self.cvactivecallwmvalue = None
                self.cvactivecallwmts = None
                self._segment_path = lambda: "cvActiveCallWMEntry" + "[cvActiveCallWMIntvlDurUnits='" + str(self.cvactivecallwmintvldurunits) + "']" + "[cvActiveCallWMIndex='" + str(self.cvactivecallwmindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvActiveCallWMTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvactivecallwmtable.Cvactivecallwmentry, ['cvactivecallwmintvldurunits', 'cvactivecallwmindex', 'cvactivecallwmvalue', 'cvactivecallwmts'], name, value)


    class Cvsipmsgratewmtable(Entity):
        """
        This table represents of high watermarks achieved
        by SIP message rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratewmentry
        
        	This is a conceptual\-row in cvSipMsgRateWMTable. This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted if cvCallVolumeWMTableSize is changed
        	**type**\: list of  		 :py:class:`Cvsipmsgratewmentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable.Cvsipmsgratewmentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
        _revision = '2012-05-15'

        def __init__(self):
            super(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable, self).__init__()

            self.yang_name = "cvSipMsgRateWMTable"
            self.yang_parent_name = "CISCO-VOICE-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvSipMsgRateWMEntry", ("cvsipmsgratewmentry", CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable.Cvsipmsgratewmentry))])
            self._leafs = OrderedDict()

            self.cvsipmsgratewmentry = YList(self)
            self._segment_path = lambda: "cvSipMsgRateWMTable"
            self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable, [], name, value)


        class Cvsipmsgratewmentry(Entity):
            """
            This is a conceptual\-row in cvSipMsgRateWMTable.
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvsipmsgratewmintvldurunits  (key)
            
            	The Object indexes in SIP Message rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\:  :py:class:`CvCallVolumeWMIntvlType <ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType>`
            
            .. attribute:: cvsipmsgratewmindex  (key)
            
            	This is an index that references to different peaks in past period in sip message rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvsipmsgratewmvalue
            
            	This object indicates high watermark value achieved by the SIP messages per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SIP messages per second
            
            .. attribute:: cvsipmsgratewmts
            
            	This object indicates date and time when the high watermark is achieved for SIP messages per second for the given interval
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VOICE-DIAL-CONTROL-MIB'
            _revision = '2012-05-15'

            def __init__(self):
                super(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable.Cvsipmsgratewmentry, self).__init__()

                self.yang_name = "cvSipMsgRateWMEntry"
                self.yang_parent_name = "cvSipMsgRateWMTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvsipmsgratewmintvldurunits','cvsipmsgratewmindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvsipmsgratewmintvldurunits', YLeaf(YType.enumeration, 'cvSipMsgRateWMIntvlDurUnits')),
                    ('cvsipmsgratewmindex', YLeaf(YType.uint32, 'cvSipMsgRateWMIndex')),
                    ('cvsipmsgratewmvalue', YLeaf(YType.uint32, 'cvSipMsgRateWMValue')),
                    ('cvsipmsgratewmts', YLeaf(YType.str, 'cvSipMsgRateWMts')),
                ])
                self.cvsipmsgratewmintvldurunits = None
                self.cvsipmsgratewmindex = None
                self.cvsipmsgratewmvalue = None
                self.cvsipmsgratewmts = None
                self._segment_path = lambda: "cvSipMsgRateWMEntry" + "[cvSipMsgRateWMIntvlDurUnits='" + str(self.cvsipmsgratewmintvldurunits) + "']" + "[cvSipMsgRateWMIndex='" + str(self.cvsipmsgratewmindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/cvSipMsgRateWMTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDIALCONTROLMIB.Cvsipmsgratewmtable.Cvsipmsgratewmentry, ['cvsipmsgratewmintvldurunits', 'cvsipmsgratewmindex', 'cvsipmsgratewmvalue', 'cvsipmsgratewmts'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOVOICEDIALCONTROLMIB()
        return self._top_entity

