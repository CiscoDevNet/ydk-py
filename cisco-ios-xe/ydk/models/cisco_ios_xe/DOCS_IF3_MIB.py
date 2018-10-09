""" DOCS_IF3_MIB 

This MIB module contains the management objects for the
management of DOCSIS 3.0 features, primarily channel bonding,
interface topology and enhanced signal quality monitoring.
Copyright 1999\-2016 Cable Television Laboratories, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CmRegState(Enum):
    """
    CmRegState (Enum Class)

    This data type defines the CM connectivity state as reported

    by the CM.

    The enumerated values associated with the CmRegState are\:

    'other'

     indicates any state not described below.

    'notReady'

     indicates that the CM has not started the registration process

     yet.

    'notSynchronized'

     indicates that the CM has not initiated or completed the

     synchronization of the downstream physical layer

    'phySynchronized'

     indicates that the CM has completed the synchronization of

     the downstream physical layer

    'dsTopologyResolutionInProgress'

     indicates that the CM is attempting to determine its MD\-DS\-SG

    'usParametersAcquired'

     indicates that the CM has completed the upstream parameters

     acquisition or have completed the downstream and upstream

     service groups resolution, whether the CM is registering in

     a pre\-3.0 or a 3.0 CMTS.

    'rangingInProgress'

     indicates that the CM has initiated the ranging process. 

    'rangingComplete'

     indicates that the CM has completed initial ranging and

     received a Ranging Status of success from the CMTS in the

     RNG\-RSP message.

    'eaeInProgress'

     indicates that the CM has sent an Auth Info message for EAE.

    'dhcpv4InProgress'

     indicates that the CM has sent a DHCPv4 DISCOVER to gain 

     IP connectivity.

    'dhcpv6InProgress'

     indicates that the CM has sent an DHCPv6 Solicit message.

    'dhcpv4Complete'

     indicates that the CM has received a DHCPv4 ACK message from

     the CMTS.

    'dhcpv6Complete'

     indicates that the CM has received a DHCPv6 Reply message from

     the CMTS.

    'todEstablished'

     indicates that the CM has successfully acquired time of day.

     If the ToD is acquired after the CM is operational, this

     value should not be reported.

    'securityEstablished'

     indicates that the CM has successfully completed the BPI

     initialization process.

    'configFileDownloadComplete'

     indicates that the CM has completed the config file download

     process.

    'registrationInProgress'

     indicates that the CM has sent a Registration Request

     (REG\-REQ or REG\-REQ\-MP)

    'registrationComplete'

     indicates that the CM has successfully completed the

     Registration process with the CMTS.

    'accessDenied'

     indicates that the CM has received a registration aborted

     notification from the CMTS

    'operational'

     indicates that the CM has completed all necessary

     initialization steps and is operational.

    'bpiInit'

     indicates that the CM has started the BPI initialization

     process as indicated in the CM config file. If the CM already

     performed EAE, this state is skipped by the CM.

    'forwardingDisabled'

     indicates that the registration process was completed, but 

     the network access option in the received configuration file

     prohibits forwarding.

    'rfMuteAll'

     indicates that the CM is instructed to mute all channels 

     in the CM\-CTRL\-REQ message from CMTS.

    .. data:: other = 1

    .. data:: notReady = 2

    .. data:: notSynchronized = 3

    .. data:: phySynchronized = 4

    .. data:: usParametersAcquired = 5

    .. data:: rangingComplete = 6

    .. data:: dhcpv4Complete = 7

    .. data:: todEstablished = 8

    .. data:: securityEstablished = 9

    .. data:: configFileDownloadComplete = 10

    .. data:: registrationComplete = 11

    .. data:: operational = 12

    .. data:: accessDenied = 13

    .. data:: eaeInProgress = 14

    .. data:: dhcpv4InProgress = 15

    .. data:: dhcpv6InProgress = 16

    .. data:: dhcpv6Complete = 17

    .. data:: registrationInProgress = 18

    .. data:: bpiInit = 19

    .. data:: forwardingDisabled = 20

    .. data:: dsTopologyResolutionInProgress = 21

    .. data:: rangingInProgress = 22

    .. data:: rfMuteAll = 23

    """

    other = Enum.YLeaf(1, "other")

    notReady = Enum.YLeaf(2, "notReady")

    notSynchronized = Enum.YLeaf(3, "notSynchronized")

    phySynchronized = Enum.YLeaf(4, "phySynchronized")

    usParametersAcquired = Enum.YLeaf(5, "usParametersAcquired")

    rangingComplete = Enum.YLeaf(6, "rangingComplete")

    dhcpv4Complete = Enum.YLeaf(7, "dhcpv4Complete")

    todEstablished = Enum.YLeaf(8, "todEstablished")

    securityEstablished = Enum.YLeaf(9, "securityEstablished")

    configFileDownloadComplete = Enum.YLeaf(10, "configFileDownloadComplete")

    registrationComplete = Enum.YLeaf(11, "registrationComplete")

    operational = Enum.YLeaf(12, "operational")

    accessDenied = Enum.YLeaf(13, "accessDenied")

    eaeInProgress = Enum.YLeaf(14, "eaeInProgress")

    dhcpv4InProgress = Enum.YLeaf(15, "dhcpv4InProgress")

    dhcpv6InProgress = Enum.YLeaf(16, "dhcpv6InProgress")

    dhcpv6Complete = Enum.YLeaf(17, "dhcpv6Complete")

    registrationInProgress = Enum.YLeaf(18, "registrationInProgress")

    bpiInit = Enum.YLeaf(19, "bpiInit")

    forwardingDisabled = Enum.YLeaf(20, "forwardingDisabled")

    dsTopologyResolutionInProgress = Enum.YLeaf(21, "dsTopologyResolutionInProgress")

    rangingInProgress = Enum.YLeaf(22, "rangingInProgress")

    rfMuteAll = Enum.YLeaf(23, "rfMuteAll")


class CmtsCmRegState(Enum):
    """
    CmtsCmRegState (Enum Class)

    This data type defines the CM connectivity states as reported

    by the CMTS.

    The enumerated values associated with the CmtsCmRegState are\:

    'other'

     indicates any state not described below.

    'initialRanging'

     indicates that the CMTS has received an Initial Ranging

     Request message from the CM, and the ranging process is not yet

     complete.

    'rangingAutoAdjComplete'

     indicates that the CM has completed initial ranging and the

     CMTS sends  a Ranging Status of success in the RNG\-RSP.

    'startEae'

     indicates that the CMTS has received an Auth Info message for

     EAE from the CM.

    'startDhcpv4'

     indicates that the CMTS has received a DHCPv4 DISCOVER message

     from the CM.

    'startDhcpv6'

     indicates that the CMTS has received a DHCPv6 Solicit message

     from the CM.

    'dhcpv4Complete'

     indicates that the CMTS has sent a DHCPv4 ACK message to the

     CM.

    'dhcpv6Complete'

     indicates that the CMTS has sent a DHCPv6 Reply message to the

     CM.

    'startConfigFileDownload'

     indicates that the CM has started the config file download.

     If the TFTP Proxy feature is not enabled, the CMTS may not

     report this state.

    'configFileDownloadComplete'

     indicates that the CM has completed the config file download

     process.  If the TFTP Proxy feature is not enabled, the CMTS

     is not required to report this state.

    'startRegistration'

     indicates that the CMTS has received a Registration

     Request (REG\-REQ or REG\-REQ\-MP) from the CM.

    'registrationComplete'

     indicates that the CMTS has received a Registration Acknowledge

     (REG\-ACK) with a confirmation code of okay/success.

    'operational'

     indicates that the CM has completed all necessary

     initialization steps and is operational.

    'bpiInit'

     indicates that the CMTS has received an Auth Info or Auth

     Request message as part of BPI Initialization.

    'forwardingDisabled'

     indicates that the registration process was completed, but 

     the network access option in the received configuration 

     file prohibits forwarding.

    'rfMuteAll'

     indicates that the CM is instructed to mute all channels 

     in the CM\-CTRL\-REQ message from CMTS.

    .. data:: other = 1

    .. data:: initialRanging = 2

    .. data:: rangingAutoAdjComplete = 4

    .. data:: dhcpv4Complete = 5

    .. data:: registrationComplete = 6

    .. data:: operational = 8

    .. data:: bpiInit = 9

    .. data:: startEae = 10

    .. data:: startDhcpv4 = 11

    .. data:: startDhcpv6 = 12

    .. data:: dhcpv6Complete = 13

    .. data:: startConfigFileDownload = 14

    .. data:: configFileDownloadComplete = 15

    .. data:: startRegistration = 16

    .. data:: forwardingDisabled = 17

    .. data:: rfMuteAll = 18

    """

    other = Enum.YLeaf(1, "other")

    initialRanging = Enum.YLeaf(2, "initialRanging")

    rangingAutoAdjComplete = Enum.YLeaf(4, "rangingAutoAdjComplete")

    dhcpv4Complete = Enum.YLeaf(5, "dhcpv4Complete")

    registrationComplete = Enum.YLeaf(6, "registrationComplete")

    operational = Enum.YLeaf(8, "operational")

    bpiInit = Enum.YLeaf(9, "bpiInit")

    startEae = Enum.YLeaf(10, "startEae")

    startDhcpv4 = Enum.YLeaf(11, "startDhcpv4")

    startDhcpv6 = Enum.YLeaf(12, "startDhcpv6")

    dhcpv6Complete = Enum.YLeaf(13, "dhcpv6Complete")

    startConfigFileDownload = Enum.YLeaf(14, "startConfigFileDownload")

    configFileDownloadComplete = Enum.YLeaf(15, "configFileDownloadComplete")

    startRegistration = Enum.YLeaf(16, "startRegistration")

    forwardingDisabled = Enum.YLeaf(17, "forwardingDisabled")

    rfMuteAll = Enum.YLeaf(18, "rfMuteAll")


class IfDirection(Enum):
    """
    IfDirection (Enum Class)

    Indicates a direction on an RF MAC interface.

    The value downstream(1) is from Cable Modem

    Termination System to Cable Modem.

    The value upstream(2) is from Cable Modem to

    Cable Modem Termination System.

    .. data:: downstream = 1

    .. data:: upstream = 2

    """

    downstream = Enum.YLeaf(1, "downstream")

    upstream = Enum.YLeaf(2, "upstream")


class RangingState(Enum):
    """
    RangingState (Enum Class)

    This data type defines the CM ranging state as reported

    by the CMTS.

    The enumerated values associated with the RangingState are\:

    'other'

     indicates any state not described below.

    'aborted'

     indicates that the CMTS has sent a ranging abort.

    'retriesExceeded'

     indicates that the CM ranging retry limit has exceeded. 

    'success'

     indicates that the CMTS has sent a ranging success in the

     ranging response.

    'continue'

     indicates that the CMTS has sent a ranging continue in the

     ranging response.

    'timeoutT4'

     indicates that the T4 timer expired on the CM.

    .. data:: other = 1

    .. data:: aborted = 2

    .. data:: retriesExceeded = 3

    .. data:: success = 4

    .. data:: continue_ = 5

    .. data:: timeoutT4 = 6

    """

    other = Enum.YLeaf(1, "other")

    aborted = Enum.YLeaf(2, "aborted")

    retriesExceeded = Enum.YLeaf(3, "retriesExceeded")

    success = Enum.YLeaf(4, "success")

    continue_ = Enum.YLeaf(5, "continue")

    timeoutT4 = Enum.YLeaf(6, "timeoutT4")


class SpectrumAnalysisWindowFunction(Enum):
    """
    SpectrumAnalysisWindowFunction (Enum Class)

    This object controls the windowing function which will be used 

    when performing the discrete fourier transform for the analysis.  

    Note that all window functions may not be supported by all 

    devices.  If an attempt is made to set the object to an 

    unsupported window function, an error of inconsistentValue will

    be returned.

    .. data:: other = 0

    .. data:: hann = 1

    .. data:: blackmanHarris = 2

    .. data:: rectangular = 3

    .. data:: hamming = 4

    .. data:: flatTop = 5

    .. data:: gaussian = 6

    .. data:: chebyshev = 7

    """

    other = Enum.YLeaf(0, "other")

    hann = Enum.YLeaf(1, "hann")

    blackmanHarris = Enum.YLeaf(2, "blackmanHarris")

    rectangular = Enum.YLeaf(3, "rectangular")

    hamming = Enum.YLeaf(4, "hamming")

    flatTop = Enum.YLeaf(5, "flatTop")

    gaussian = Enum.YLeaf(6, "gaussian")

    chebyshev = Enum.YLeaf(7, "chebyshev")



class DOCSIF3MIB(Entity):
    """
    
    
    .. attribute:: docsif3cmcapabilities
    
    	
    	**type**\:  :py:class:`DocsIf3CmCapabilities <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmCapabilities>`
    
    .. attribute:: docsif3cmtscmctrl
    
    	
    	**type**\:  :py:class:`DocsIf3CmtsCmCtrl <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmCtrl>`
    
    .. attribute:: docsif3cmenergymgtcfg
    
    	
    	**type**\:  :py:class:`DocsIf3CmEnergyMgtCfg <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEnergyMgtCfg>`
    
    .. attribute:: docsif3cmspectrumanalysisctrlcmd
    
    	
    	**type**\:  :py:class:`DocsIf3CmSpectrumAnalysisCtrlCmd <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmSpectrumAnalysisCtrlCmd>`
    
    .. attribute:: docsif3cmstatustable
    
    	This object defines attributes of the CM connectivity status. This object provides CM connectivity status information of the CM previously available in the SNMP table docsIfCmStatusTable
    	**type**\:  :py:class:`DocsIf3CmStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmStatusTable>`
    
    .. attribute:: docsif3cmstatusustable
    
    	This object defines PHY and MAC information about the CM's upstream channels operating in Multiple Transmit Channel (MTC) mode or in a Pre\-3.0 DOSCIS transmit channel mode. This object provides per\-CM Upstream channel information previously available in the SNMP table docsIfCmStatusTable
    	**type**\:  :py:class:`DocsIf3CmStatusUsTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmStatusUsTable>`
    
    .. attribute:: docsif3cmtscmregstatustable
    
    	This object defines attributes that represent the CM's registration status as tracked by the CMTS. Refer to the individual attribute definitions for  applicability to 3.0 and 3.1 Cable Modems
    	**type**\:  :py:class:`DocsIf3CmtsCmRegStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable>`
    
    .. attribute:: docsif3cmtscmusstatustable
    
    	This object defines status information of the CM currently in use Upstream Logical Channels, as reported by the CMTS
    	**type**\:  :py:class:`DocsIf3CmtsCmUsStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable>`
    
    .. attribute:: docsif3mdchcfgtable
    
    	This object configures the association of downstream and upstream channels to a particular MAC Domain (MD) on a CMTS.  The creation of channels and MAC domain object interface instances is vendor\-specific. In particular, the assignment of the channel interface index is normally vendor\-specific. Therefore, this object is intended only for associating channels to a MAC Domain and assumes that those channels were previously configured. The CMTS may have restrictions on which channels can be configured in the same MAC Domain.  For example, it could require the upstream channels to be from the same line card. This object supports the creation and deletion of multiple instances. Creation of a new instance of this object requires the ChId attribute to be set
    	**type**\:  :py:class:`DocsIf3MdChCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdChCfgTable>`
    
    .. attribute:: docsif3rcccfgtable
    
    	This object identifies the scope of the Receive Channel Configuration (RCC) and provides a top level container for the Receive Module and Receive Channel objects.  The CMTS selects an instance of this object to assign to a CM when it registers. This object supports the creation and deletion of multiple instances
    	**type**\:  :py:class:`DocsIf3RccCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable>`
    
    	**status**\: obsolete
    
    .. attribute:: docsif3rccstatustable
    
    	The RCC Status object provides a read\-only view of the statically\-configured (from the RccCfg object) and dynamically\-created RCCs. The CMTS creates an RCC Status instance for each unique MAC Domain Cable Modem Service Group (MD\-CM\-SG) to which it signals an RCC to the CM
    	**type**\:  :py:class:`DocsIf3RccStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable>`
    
    .. attribute:: docsif3rxchcfgtable
    
    	The Receive Channel Configuration object permits an operator to configure how CMs registered with certain Receive Channel Profiles will configure the Receive Channels within their profile. When a CM registers with an RCP for which all Receive Channel Indices (RcIds) are configured in the Receive Module object and all Receive Channels are configured within this object, the CMTS should use the configuration within these objects to set the Receive Channel Configuration returned to the CM in a REG\-RSP message.  A CMTS may require configuration of all pertinent Receive Module and Receive Channel instances in order to register a CM that reports a Receive Channel Profile (RCP), including any standard Receive Channel Profiles. If the CM reports multiple RCPs, and Receive Module and Receive Channel objects have instances for more than one RCP, the particular RCP selected by the CMTS is not specified.  A CMTS is not restricted to assigning Receive Modules based only on the contents of this object. This object supports the creation and deletion of multiple instances. Creation of a new instance of this object requires the ChIfIndex attribute to be set and a valid reference of a RccCfg instance
    	**type**\:  :py:class:`DocsIf3RxChCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxChCfgTable>`
    
    	**status**\: obsolete
    
    .. attribute:: docsif3rxchstatustable
    
    	The Receive Channel Status object reports the status of the statically\-configured and dynamically\-created Receive Channels within an RCC
    	**type**\:  :py:class:`DocsIf3RxChStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxChStatusTable>`
    
    .. attribute:: docsif3rxmodulecfgtable
    
    	The Receive Module Configuration object permits an operator to configure how CMs with certain Receive Channel Profiles (RCPs) will configure the Receive Modules within their profile upon CM registration.  When a CM registers with an RCP for which all Receive Module Indices (RmIds) are configured in this object and all Receive Channels are configured within the Receive Channel (ReceiveChannel) object, the CMTS should use the configuration within these objects to set the Receive Channel Configuration assigned to the CM in a REG\-RSP message.  A CMTS may require configuration of all pertinent Receive Module and Receive Channel instances (i.e., MIB table entries) in order to register a CM that reports a Receive Channel Profile.  If the CM reports multiple RCPs, and Receive Module and Receive Channel objects have instances (i.e., MIB table entries) for more than one RCP reported by the CM, the particular RCP selected by the CMTS is not specified.  A CMTS is not restricted to assigning Receive Modules based only on the contents of this object.  This object supports the creation and deletion of multiple instances. Creation of a new instance of this object requires the reference of a valid RccCfg instance
    	**type**\:  :py:class:`DocsIf3RxModuleCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxModuleCfgTable>`
    
    	**status**\: obsolete
    
    .. attribute:: docsif3rxmodulestatustable
    
    	The Receive Module Status object provides a read\-only view of the statically configured and dynamically created Receive Modules within an RCC
    	**type**\:  :py:class:`DocsIf3RxModuleStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxModuleStatusTable>`
    
    .. attribute:: docsif3mdnodestatustable
    
    	This object reports the MD\-DS\-SG\-ID and MD\-US\-SG\-ID associated with a MD\-CM\-SG\-ID within a MAC Domain and the Fiber Nodes reached by the MD\-CM\-SG
    	**type**\:  :py:class:`DocsIf3MdNodeStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdNodeStatusTable>`
    
    .. attribute:: docsif3mddssgstatustable
    
    	This object returns the list of downstream channel associated with a MAC Domain MD\-DS\-SG\-ID
    	**type**\:  :py:class:`DocsIf3MdDsSgStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdDsSgStatusTable>`
    
    .. attribute:: docsif3mdussgstatustable
    
    	This object returns the list of upstream channels associated with a MAC Domain MD\-US\-SG\-ID
    	**type**\:  :py:class:`DocsIf3MdUsSgStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdUsSgStatusTable>`
    
    .. attribute:: docsif3mdustodschmappingtable
    
    	This object returns the set of downstream channels that carry UCDs and MAPs for a particular upstream channel in a MAC Domain
    	**type**\:  :py:class:`DocsIf3MdUsToDsChMappingTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable>`
    
    .. attribute:: docsif3mdcfgtable
    
    	This object contains MAC domain level control and configuration attributes
    	**type**\:  :py:class:`DocsIf3MdCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable>`
    
    .. attribute:: docsif3bondinggrpcfgtable
    
    	This object defines statically configured Downstream Bonding Groups and Upstream Bonding Groups on the CMTS. This object supports the creation and deletion of multiple instances. Creation of a new instance of this object requires the ChList attribute to be set
    	**type**\:  :py:class:`DocsIf3BondingGrpCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3BondingGrpCfgTable>`
    
    .. attribute:: docsif3dsbondinggrpstatustable
    
    	This object returns administratively\-configured and CMTS defined downstream bonding groups
    	**type**\:  :py:class:`DocsIf3DsBondingGrpStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable>`
    
    .. attribute:: docsif3usbondinggrpstatustable
    
    	This object returns administratively\-configured and CMTS\-defined upstream bonding groups
    	**type**\:  :py:class:`DocsIf3UsBondingGrpStatusTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable>`
    
    .. attribute:: docsif3uschexttable
    
    	This object defines management extensions for upstream channels, in particular SCDMA parameters
    	**type**\:  :py:class:`DocsIf3UsChExtTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsChExtTable>`
    
    .. attribute:: docsif3uschsettable
    
    	This object defines a set of upstream channels. These channel sets may be associated with channel bonding groups, MD\-US\-SGs, MD\-CM\-SGs, or any other channel set that the CMTS may derive from other CMTS processes
    	**type**\:  :py:class:`DocsIf3UsChSetTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsChSetTable>`
    
    .. attribute:: docsif3dschsettable
    
    	This object defines a set of downstream channels. These channel sets may be associated with channel bonding groups, MD\-DS\-SGs, MD\-CM\-SGs, or any other channel set that the CMTS may derive from other CMTS processes
    	**type**\:  :py:class:`DocsIf3DsChSetTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3DsChSetTable>`
    
    .. attribute:: docsif3signalqualityexttable
    
    	This object provides an in\-channel received modulation error ratio metric for CM and CMTS
    	**type**\:  :py:class:`DocsIf3SignalQualityExtTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3SignalQualityExtTable>`
    
    .. attribute:: docsif3cmtssignalqualityexttable
    
    	This object provides metrics and parameters associated with received carrier, noise and interference power levels in the upstream channels of the CMTS
    	**type**\:  :py:class:`DocsIf3CmtsSignalQualityExtTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable>`
    
    .. attribute:: docsif3cmtsspectrumanalysismeastable
    
    	This object is used to configure the logical upstream interfaces to perform the spectrum measurements. This object supports creation and deletion of instances
    	**type**\:  :py:class:`DocsIf3CmtsSpectrumAnalysisMeasTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable>`
    
    .. attribute:: docsif3cmdpvstatstable
    
    	This object represents the DOCSIS Path Verify Statistics collected in the cable modem device. The CMTS controls the logging of DPV statistics in the cable modem. Therefore the context and nature of the measurements are governed by the CMTS and not self\-descriptive when read from the CM
    	**type**\:  :py:class:`DocsIf3CmDpvStatsTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmDpvStatsTable>`
    
    .. attribute:: docsif3cmeventctrltable
    
    	This object represents the control mechanism to enable the dispatching of events based on the event Id. The following rules define the event control behavior\:  \- The CmEventCtrl object has no instances or contains an    instance with Event ID 0. All events matching the Local Log   settings of docsDevEvReporting are sent to local log ONLY.  \- The CmEventCtrl object contains configured instances   Only events matching the Event Ids configured in the object   are sent according to the settings of the docsDevEvReporting   object.       The CM does not persist instances of CmEventCtrl across    reinitializations
    	**type**\:  :py:class:`DocsIf3CmEventCtrlTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEventCtrlTable>`
    
    .. attribute:: docsif3cmtseventctrltable
    
    	This object represents the control mechanism to enable the dispatching of  events based on the event Id. The following rules define the event control behavior\:  \- The CmtsEventCtrl object has no instances or contains an    instance with Event ID 0. All events matching the Local Log    settings of docsDevEvReporting are sent to local log ONLY.  \- The CmtsEventCtrl object contains configured instances   Only events matching the Event Ids configured in the object   are sent according to the settings of the docsDevEvReporting   object.     \- The CMTS persists all instances of CmtsEventCtrl across    reinitializations
    	**type**\:  :py:class:`DocsIf3CmtsEventCtrlTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsEventCtrlTable>`
    
    .. attribute:: docsif3cmmdcfgtable
    
    	This object contains CM MAC domain level control and configuration attributes
    	**type**\:  :py:class:`DocsIf3CmMdCfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmMdCfgTable>`
    
    .. attribute:: docsif3cmenergymgt1x1cfgtable
    
    	This object provides configuration state information  on the CM for the Energy Management 1x1 Mode feature
    	**type**\:  :py:class:`DocsIf3CmEnergyMgt1x1CfgTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable>`
    
    .. attribute:: docsif3cmspectrumanalysismeastable
    
    	This table provides a list of spectral analysis measurements  as performed across a range of center frequencies. The table  is capable of representing a full scan of the spectrum
    	**type**\:  :py:class:`DocsIf3CmSpectrumAnalysisMeasTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable>`
    
    .. attribute:: docsif3cmtscmemstatstable
    
    	This table defines Energy Management mode statistics for the CM as reported by the CMTS.  For example, such metrics can provide insight into configuration of appropriate EM 1x1 Mode Activity Detection thresholds on the CM and/or to get feedback on how/if the current thresholds are working well or are  causing user experience issues
    	**type**\:  :py:class:`DocsIf3CmtsCmEmStatsTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable>`
    
    .. attribute:: docsif3cmem1x1statstable
    
    	This object defines Energy Management 1x1 mode statistics on the CM to provide insight into configuration of appropriate EM 1x1 Mode Activity Detection thresholds and/or to get feedback on how/if the current thresholds are working well or are  causing user experience issues. These statistics are only applicable/valid when the Energy  Management 1x1 mode is enabled in the CM
    	**type**\:  :py:class:`DocsIf3CmEm1x1StatsTable <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEm1x1StatsTable>`
    
    

    """

    _prefix = 'DOCS-IF3-MIB'
    _revision = '2016-05-05'

    def __init__(self):
        super(DOCSIF3MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-IF3-MIB"
        self.yang_parent_name = "DOCS-IF3-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsIf3CmCapabilities", ("docsif3cmcapabilities", DOCSIF3MIB.DocsIf3CmCapabilities)), ("docsIf3CmtsCmCtrl", ("docsif3cmtscmctrl", DOCSIF3MIB.DocsIf3CmtsCmCtrl)), ("docsIf3CmEnergyMgtCfg", ("docsif3cmenergymgtcfg", DOCSIF3MIB.DocsIf3CmEnergyMgtCfg)), ("docsIf3CmSpectrumAnalysisCtrlCmd", ("docsif3cmspectrumanalysisctrlcmd", DOCSIF3MIB.DocsIf3CmSpectrumAnalysisCtrlCmd)), ("docsIf3CmStatusTable", ("docsif3cmstatustable", DOCSIF3MIB.DocsIf3CmStatusTable)), ("docsIf3CmStatusUsTable", ("docsif3cmstatusustable", DOCSIF3MIB.DocsIf3CmStatusUsTable)), ("docsIf3CmtsCmRegStatusTable", ("docsif3cmtscmregstatustable", DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable)), ("docsIf3CmtsCmUsStatusTable", ("docsif3cmtscmusstatustable", DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable)), ("docsIf3MdChCfgTable", ("docsif3mdchcfgtable", DOCSIF3MIB.DocsIf3MdChCfgTable)), ("docsIf3RccCfgTable", ("docsif3rcccfgtable", DOCSIF3MIB.DocsIf3RccCfgTable)), ("docsIf3RccStatusTable", ("docsif3rccstatustable", DOCSIF3MIB.DocsIf3RccStatusTable)), ("docsIf3RxChCfgTable", ("docsif3rxchcfgtable", DOCSIF3MIB.DocsIf3RxChCfgTable)), ("docsIf3RxChStatusTable", ("docsif3rxchstatustable", DOCSIF3MIB.DocsIf3RxChStatusTable)), ("docsIf3RxModuleCfgTable", ("docsif3rxmodulecfgtable", DOCSIF3MIB.DocsIf3RxModuleCfgTable)), ("docsIf3RxModuleStatusTable", ("docsif3rxmodulestatustable", DOCSIF3MIB.DocsIf3RxModuleStatusTable)), ("docsIf3MdNodeStatusTable", ("docsif3mdnodestatustable", DOCSIF3MIB.DocsIf3MdNodeStatusTable)), ("docsIf3MdDsSgStatusTable", ("docsif3mddssgstatustable", DOCSIF3MIB.DocsIf3MdDsSgStatusTable)), ("docsIf3MdUsSgStatusTable", ("docsif3mdussgstatustable", DOCSIF3MIB.DocsIf3MdUsSgStatusTable)), ("docsIf3MdUsToDsChMappingTable", ("docsif3mdustodschmappingtable", DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable)), ("docsIf3MdCfgTable", ("docsif3mdcfgtable", DOCSIF3MIB.DocsIf3MdCfgTable)), ("docsIf3BondingGrpCfgTable", ("docsif3bondinggrpcfgtable", DOCSIF3MIB.DocsIf3BondingGrpCfgTable)), ("docsIf3DsBondingGrpStatusTable", ("docsif3dsbondinggrpstatustable", DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable)), ("docsIf3UsBondingGrpStatusTable", ("docsif3usbondinggrpstatustable", DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable)), ("docsIf3UsChExtTable", ("docsif3uschexttable", DOCSIF3MIB.DocsIf3UsChExtTable)), ("docsIf3UsChSetTable", ("docsif3uschsettable", DOCSIF3MIB.DocsIf3UsChSetTable)), ("docsIf3DsChSetTable", ("docsif3dschsettable", DOCSIF3MIB.DocsIf3DsChSetTable)), ("docsIf3SignalQualityExtTable", ("docsif3signalqualityexttable", DOCSIF3MIB.DocsIf3SignalQualityExtTable)), ("docsIf3CmtsSignalQualityExtTable", ("docsif3cmtssignalqualityexttable", DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable)), ("docsIf3CmtsSpectrumAnalysisMeasTable", ("docsif3cmtsspectrumanalysismeastable", DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable)), ("docsIf3CmDpvStatsTable", ("docsif3cmdpvstatstable", DOCSIF3MIB.DocsIf3CmDpvStatsTable)), ("docsIf3CmEventCtrlTable", ("docsif3cmeventctrltable", DOCSIF3MIB.DocsIf3CmEventCtrlTable)), ("docsIf3CmtsEventCtrlTable", ("docsif3cmtseventctrltable", DOCSIF3MIB.DocsIf3CmtsEventCtrlTable)), ("docsIf3CmMdCfgTable", ("docsif3cmmdcfgtable", DOCSIF3MIB.DocsIf3CmMdCfgTable)), ("docsIf3CmEnergyMgt1x1CfgTable", ("docsif3cmenergymgt1x1cfgtable", DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable)), ("docsIf3CmSpectrumAnalysisMeasTable", ("docsif3cmspectrumanalysismeastable", DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable)), ("docsIf3CmtsCmEmStatsTable", ("docsif3cmtscmemstatstable", DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable)), ("docsIf3CmEm1x1StatsTable", ("docsif3cmem1x1statstable", DOCSIF3MIB.DocsIf3CmEm1x1StatsTable))])
        self._leafs = OrderedDict()

        self.docsif3cmcapabilities = DOCSIF3MIB.DocsIf3CmCapabilities()
        self.docsif3cmcapabilities.parent = self
        self._children_name_map["docsif3cmcapabilities"] = "docsIf3CmCapabilities"

        self.docsif3cmtscmctrl = DOCSIF3MIB.DocsIf3CmtsCmCtrl()
        self.docsif3cmtscmctrl.parent = self
        self._children_name_map["docsif3cmtscmctrl"] = "docsIf3CmtsCmCtrl"

        self.docsif3cmenergymgtcfg = DOCSIF3MIB.DocsIf3CmEnergyMgtCfg()
        self.docsif3cmenergymgtcfg.parent = self
        self._children_name_map["docsif3cmenergymgtcfg"] = "docsIf3CmEnergyMgtCfg"

        self.docsif3cmspectrumanalysisctrlcmd = DOCSIF3MIB.DocsIf3CmSpectrumAnalysisCtrlCmd()
        self.docsif3cmspectrumanalysisctrlcmd.parent = self
        self._children_name_map["docsif3cmspectrumanalysisctrlcmd"] = "docsIf3CmSpectrumAnalysisCtrlCmd"

        self.docsif3cmstatustable = DOCSIF3MIB.DocsIf3CmStatusTable()
        self.docsif3cmstatustable.parent = self
        self._children_name_map["docsif3cmstatustable"] = "docsIf3CmStatusTable"

        self.docsif3cmstatusustable = DOCSIF3MIB.DocsIf3CmStatusUsTable()
        self.docsif3cmstatusustable.parent = self
        self._children_name_map["docsif3cmstatusustable"] = "docsIf3CmStatusUsTable"

        self.docsif3cmtscmregstatustable = DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable()
        self.docsif3cmtscmregstatustable.parent = self
        self._children_name_map["docsif3cmtscmregstatustable"] = "docsIf3CmtsCmRegStatusTable"

        self.docsif3cmtscmusstatustable = DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable()
        self.docsif3cmtscmusstatustable.parent = self
        self._children_name_map["docsif3cmtscmusstatustable"] = "docsIf3CmtsCmUsStatusTable"

        self.docsif3mdchcfgtable = DOCSIF3MIB.DocsIf3MdChCfgTable()
        self.docsif3mdchcfgtable.parent = self
        self._children_name_map["docsif3mdchcfgtable"] = "docsIf3MdChCfgTable"

        self.docsif3rcccfgtable = DOCSIF3MIB.DocsIf3RccCfgTable()
        self.docsif3rcccfgtable.parent = self
        self._children_name_map["docsif3rcccfgtable"] = "docsIf3RccCfgTable"

        self.docsif3rccstatustable = DOCSIF3MIB.DocsIf3RccStatusTable()
        self.docsif3rccstatustable.parent = self
        self._children_name_map["docsif3rccstatustable"] = "docsIf3RccStatusTable"

        self.docsif3rxchcfgtable = DOCSIF3MIB.DocsIf3RxChCfgTable()
        self.docsif3rxchcfgtable.parent = self
        self._children_name_map["docsif3rxchcfgtable"] = "docsIf3RxChCfgTable"

        self.docsif3rxchstatustable = DOCSIF3MIB.DocsIf3RxChStatusTable()
        self.docsif3rxchstatustable.parent = self
        self._children_name_map["docsif3rxchstatustable"] = "docsIf3RxChStatusTable"

        self.docsif3rxmodulecfgtable = DOCSIF3MIB.DocsIf3RxModuleCfgTable()
        self.docsif3rxmodulecfgtable.parent = self
        self._children_name_map["docsif3rxmodulecfgtable"] = "docsIf3RxModuleCfgTable"

        self.docsif3rxmodulestatustable = DOCSIF3MIB.DocsIf3RxModuleStatusTable()
        self.docsif3rxmodulestatustable.parent = self
        self._children_name_map["docsif3rxmodulestatustable"] = "docsIf3RxModuleStatusTable"

        self.docsif3mdnodestatustable = DOCSIF3MIB.DocsIf3MdNodeStatusTable()
        self.docsif3mdnodestatustable.parent = self
        self._children_name_map["docsif3mdnodestatustable"] = "docsIf3MdNodeStatusTable"

        self.docsif3mddssgstatustable = DOCSIF3MIB.DocsIf3MdDsSgStatusTable()
        self.docsif3mddssgstatustable.parent = self
        self._children_name_map["docsif3mddssgstatustable"] = "docsIf3MdDsSgStatusTable"

        self.docsif3mdussgstatustable = DOCSIF3MIB.DocsIf3MdUsSgStatusTable()
        self.docsif3mdussgstatustable.parent = self
        self._children_name_map["docsif3mdussgstatustable"] = "docsIf3MdUsSgStatusTable"

        self.docsif3mdustodschmappingtable = DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable()
        self.docsif3mdustodschmappingtable.parent = self
        self._children_name_map["docsif3mdustodschmappingtable"] = "docsIf3MdUsToDsChMappingTable"

        self.docsif3mdcfgtable = DOCSIF3MIB.DocsIf3MdCfgTable()
        self.docsif3mdcfgtable.parent = self
        self._children_name_map["docsif3mdcfgtable"] = "docsIf3MdCfgTable"

        self.docsif3bondinggrpcfgtable = DOCSIF3MIB.DocsIf3BondingGrpCfgTable()
        self.docsif3bondinggrpcfgtable.parent = self
        self._children_name_map["docsif3bondinggrpcfgtable"] = "docsIf3BondingGrpCfgTable"

        self.docsif3dsbondinggrpstatustable = DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable()
        self.docsif3dsbondinggrpstatustable.parent = self
        self._children_name_map["docsif3dsbondinggrpstatustable"] = "docsIf3DsBondingGrpStatusTable"

        self.docsif3usbondinggrpstatustable = DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable()
        self.docsif3usbondinggrpstatustable.parent = self
        self._children_name_map["docsif3usbondinggrpstatustable"] = "docsIf3UsBondingGrpStatusTable"

        self.docsif3uschexttable = DOCSIF3MIB.DocsIf3UsChExtTable()
        self.docsif3uschexttable.parent = self
        self._children_name_map["docsif3uschexttable"] = "docsIf3UsChExtTable"

        self.docsif3uschsettable = DOCSIF3MIB.DocsIf3UsChSetTable()
        self.docsif3uschsettable.parent = self
        self._children_name_map["docsif3uschsettable"] = "docsIf3UsChSetTable"

        self.docsif3dschsettable = DOCSIF3MIB.DocsIf3DsChSetTable()
        self.docsif3dschsettable.parent = self
        self._children_name_map["docsif3dschsettable"] = "docsIf3DsChSetTable"

        self.docsif3signalqualityexttable = DOCSIF3MIB.DocsIf3SignalQualityExtTable()
        self.docsif3signalqualityexttable.parent = self
        self._children_name_map["docsif3signalqualityexttable"] = "docsIf3SignalQualityExtTable"

        self.docsif3cmtssignalqualityexttable = DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable()
        self.docsif3cmtssignalqualityexttable.parent = self
        self._children_name_map["docsif3cmtssignalqualityexttable"] = "docsIf3CmtsSignalQualityExtTable"

        self.docsif3cmtsspectrumanalysismeastable = DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable()
        self.docsif3cmtsspectrumanalysismeastable.parent = self
        self._children_name_map["docsif3cmtsspectrumanalysismeastable"] = "docsIf3CmtsSpectrumAnalysisMeasTable"

        self.docsif3cmdpvstatstable = DOCSIF3MIB.DocsIf3CmDpvStatsTable()
        self.docsif3cmdpvstatstable.parent = self
        self._children_name_map["docsif3cmdpvstatstable"] = "docsIf3CmDpvStatsTable"

        self.docsif3cmeventctrltable = DOCSIF3MIB.DocsIf3CmEventCtrlTable()
        self.docsif3cmeventctrltable.parent = self
        self._children_name_map["docsif3cmeventctrltable"] = "docsIf3CmEventCtrlTable"

        self.docsif3cmtseventctrltable = DOCSIF3MIB.DocsIf3CmtsEventCtrlTable()
        self.docsif3cmtseventctrltable.parent = self
        self._children_name_map["docsif3cmtseventctrltable"] = "docsIf3CmtsEventCtrlTable"

        self.docsif3cmmdcfgtable = DOCSIF3MIB.DocsIf3CmMdCfgTable()
        self.docsif3cmmdcfgtable.parent = self
        self._children_name_map["docsif3cmmdcfgtable"] = "docsIf3CmMdCfgTable"

        self.docsif3cmenergymgt1x1cfgtable = DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable()
        self.docsif3cmenergymgt1x1cfgtable.parent = self
        self._children_name_map["docsif3cmenergymgt1x1cfgtable"] = "docsIf3CmEnergyMgt1x1CfgTable"

        self.docsif3cmspectrumanalysismeastable = DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable()
        self.docsif3cmspectrumanalysismeastable.parent = self
        self._children_name_map["docsif3cmspectrumanalysismeastable"] = "docsIf3CmSpectrumAnalysisMeasTable"

        self.docsif3cmtscmemstatstable = DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable()
        self.docsif3cmtscmemstatstable.parent = self
        self._children_name_map["docsif3cmtscmemstatstable"] = "docsIf3CmtsCmEmStatsTable"

        self.docsif3cmem1x1statstable = DOCSIF3MIB.DocsIf3CmEm1x1StatsTable()
        self.docsif3cmem1x1statstable.parent = self
        self._children_name_map["docsif3cmem1x1statstable"] = "docsIf3CmEm1x1StatsTable"
        self._segment_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSIF3MIB, [], name, value)


    class DocsIf3CmCapabilities(Entity):
        """
        
        
        .. attribute:: docsif3cmcapabilitiesreq
        
        	This attribute contains the TLV encoding for TLV\-5 sent in a REG\-REQ.  The first byte of this encoding is expected to be '05'H
        	**type**\: str
        
        	**length:** 0 \| 2..255
        
        .. attribute:: docsif3cmcapabilitiesrsp
        
        	This attribute contains the TLV encoding for TLV\-5 received in a REG\-RSP. The first byte of this encoding is expected to be '05'H
        	**type**\: str
        
        	**length:** 0 \| 2..255
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmCapabilities, self).__init__()

            self.yang_name = "docsIf3CmCapabilities"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsif3cmcapabilitiesreq', (YLeaf(YType.str, 'docsIf3CmCapabilitiesReq'), ['str'])),
                ('docsif3cmcapabilitiesrsp', (YLeaf(YType.str, 'docsIf3CmCapabilitiesRsp'), ['str'])),
            ])
            self.docsif3cmcapabilitiesreq = None
            self.docsif3cmcapabilitiesrsp = None
            self._segment_path = lambda: "docsIf3CmCapabilities"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmCapabilities, ['docsif3cmcapabilitiesreq', 'docsif3cmcapabilitiesrsp'], name, value)


    class DocsIf3CmtsCmCtrl(Entity):
        """
        
        
        .. attribute:: docsif3cmtscmctrlcmdmacaddr
        
        	This attribute represents the MAC Address of the CM which the  CMTS is instructed to send the CM\-CTRL\-REQ message
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: docsif3cmtscmctrlcmdmuteuschid
        
        	This attribute represents the Upstream Channel ID (UCID) to  mute or unmute.  A value of zero indicates all upstream  channels.  This attribute is only applicable when the  docsIf3CmtsCmCtrlCmdCommit attribute is set to  'mute'
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: docsif3cmtscmctrlcmdmuteinterval
        
        	This attribute represents the length of time that the mute  operation is in effect.  This attribute is only applicable  when the docsIf3CmtsCmCtrlCmdCommit attribute is set to  'mute'.  A value of 0 is an indication to unmute the channel referenced by the docsIf3CmtsCmCtrlCmdMuteUsChId attribute while a value of 0xFFFFFFFF is used to mute the channel referenced by the docsIf3CmtsCmCtrlCmdMuteUsChId attribute indefinitely
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: docsif3cmtscmctrlcmddisableforwarding
        
        	When set to 'true', this attribute disables data forwarding  to the CMCI when the docsIf3CmtsCmCtrlCmdCommit attribute is set to 'disableForwarding'.  When set to 'false', this attribute enables data forwarding to the CMCI when the docsIf3CmtsCmCtrlCmdCommit attribute is set to 'disableForwarding'.  This attribute is only applicable when the  docsIf3CmtsCmCtrlCmdCommit attribute is set to  'disableForwarding'
        	**type**\: bool
        
        .. attribute:: docsif3cmtscmctrlcmdcommit
        
        	This attribute indicates the type of command for the  CMTS to trigger in the CM\-CTRL\-REQ message. This attribute will return the value of the last operation  performed or the default value if no operation has been  performed
        	**type**\:  :py:class:`DocsIf3CmtsCmCtrlCmdCommit <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmCtrl.DocsIf3CmtsCmCtrlCmdCommit>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsCmCtrl, self).__init__()

            self.yang_name = "docsIf3CmtsCmCtrl"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsif3cmtscmctrlcmdmacaddr', (YLeaf(YType.str, 'docsIf3CmtsCmCtrlCmdMacAddr'), ['str'])),
                ('docsif3cmtscmctrlcmdmuteuschid', (YLeaf(YType.uint32, 'docsIf3CmtsCmCtrlCmdMuteUsChId'), ['int'])),
                ('docsif3cmtscmctrlcmdmuteinterval', (YLeaf(YType.uint32, 'docsIf3CmtsCmCtrlCmdMuteInterval'), ['int'])),
                ('docsif3cmtscmctrlcmddisableforwarding', (YLeaf(YType.boolean, 'docsIf3CmtsCmCtrlCmdDisableForwarding'), ['bool'])),
                ('docsif3cmtscmctrlcmdcommit', (YLeaf(YType.enumeration, 'docsIf3CmtsCmCtrlCmdCommit'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3CmtsCmCtrl.DocsIf3CmtsCmCtrlCmdCommit')])),
            ])
            self.docsif3cmtscmctrlcmdmacaddr = None
            self.docsif3cmtscmctrlcmdmuteuschid = None
            self.docsif3cmtscmctrlcmdmuteinterval = None
            self.docsif3cmtscmctrlcmddisableforwarding = None
            self.docsif3cmtscmctrlcmdcommit = None
            self._segment_path = lambda: "docsIf3CmtsCmCtrl"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmCtrl, ['docsif3cmtscmctrlcmdmacaddr', 'docsif3cmtscmctrlcmdmuteuschid', 'docsif3cmtscmctrlcmdmuteinterval', 'docsif3cmtscmctrlcmddisableforwarding', 'docsif3cmtscmctrlcmdcommit'], name, value)

        class DocsIf3CmtsCmCtrlCmdCommit(Enum):
            """
            DocsIf3CmtsCmCtrlCmdCommit (Enum Class)

            This attribute indicates the type of command for the 

            CMTS to trigger in the CM\-CTRL\-REQ message.

            This attribute will return the value of the last operation 

            performed or the default value if no operation has been 

            performed.

            .. data:: mute = 1

            .. data:: cmReinit = 2

            .. data:: disableForwarding = 3

            """

            mute = Enum.YLeaf(1, "mute")

            cmReinit = Enum.YLeaf(2, "cmReinit")

            disableForwarding = Enum.YLeaf(3, "disableForwarding")



    class DocsIf3CmEnergyMgtCfg(Entity):
        """
        
        
        .. attribute:: docsif3cmenergymgtcfgfeatureenabled
        
        	This attribute indicates which energy savings features have been enabled in the Cable Modem. The CM enables use of Energy Management Features only if both the Energy Management Feature Control TLV and Energy Management Modem Capability Response from the CMTS indicate that the feature is enabled.  If bit 0 is set,  the Energy Management 1x1 Mode feature is enabled
        	**type**\:  :py:class:`DocsIf3CmEnergyMgtCfgFeatureEnabled <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEnergyMgtCfg.DocsIf3CmEnergyMgtCfgFeatureEnabled>`
        
        .. attribute:: docsif3cmenergymgtcfgcycleperiod
        
        	This attribute specifies a minimum time period (in seconds)  that must elapse between EM\-REQ transactions in certain  situations\:  \- In the case of Energy Management 1x1 Mode, this attribute   sets the minimum cycle time that a CM will use for sending   requests to enter Energy Management 1x1 Mode.  \- In the case that the CM fails to receive an EM\-RSP message   after the maximum number of retries, this attribute sets    the minimum amount of time to elapse before the CM can    attempt another EM\-REQ transaction
        	**type**\: int
        
        	**range:** 0..65535
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmEnergyMgtCfg, self).__init__()

            self.yang_name = "docsIf3CmEnergyMgtCfg"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsif3cmenergymgtcfgfeatureenabled', (YLeaf(YType.bits, 'docsIf3CmEnergyMgtCfgFeatureEnabled'), ['Bits'])),
                ('docsif3cmenergymgtcfgcycleperiod', (YLeaf(YType.uint32, 'docsIf3CmEnergyMgtCfgCyclePeriod'), ['int'])),
            ])
            self.docsif3cmenergymgtcfgfeatureenabled = Bits()
            self.docsif3cmenergymgtcfgcycleperiod = None
            self._segment_path = lambda: "docsIf3CmEnergyMgtCfg"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmEnergyMgtCfg, ['docsif3cmenergymgtcfgfeatureenabled', 'docsif3cmenergymgtcfgcycleperiod'], name, value)


    class DocsIf3CmSpectrumAnalysisCtrlCmd(Entity):
        """
        
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdenable
        
        	This attribute is used to enable or disable the spectrum  analyzer feature. Setting this attribute to true triggers the CM to initiate measurements for the spectrum analyzer feature based on the other configuration attributes for the feature. By  default, the feature is disabled unless explicitly enabled.  Note that the feature may be disabled by the system under  certain circumstances if the spectrum analyzer would affect  critical services. In such a case, the attribute will return 'false' when read, and will reject sets to 'true' with an  error. Once the feature is enabled, any Set operation on  the docsIf3CmSpectrumAnalysisCtrlCmd MIB group might not  be effective until the feature is re\-enabled again
        	**type**\: bool
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdinactivitytimeout
        
        	This attribute controls the length of time after the last  spectrum analysis measurement before the feature is  automatically disabled. If set to a value of 0, the feature will remain enabled until it is explicitly disabled
        	**type**\: int
        
        	**range:** 0..86400
        
        	**units**\: seconds
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdfirstsegmentcenterfrequency
        
        	This attribute controls the center frequency of the first segment for the spectrum analysis measurement. The frequency bins for this segment lie symmetrically to the left and right of this center frequency.    If the number of bins in a segment is odd, the segment center frequency lies directly on the center bin.    If the number of bins in a segment is even, the segment center frequency lies halfway between two bins.  Changing the value of this attribute may result in  changes to the docsIf3CmSpectrumAnalysisMeasTable. Note that if this attribute is set to an invalid value,  the device may return an error, or may adjust the  value of the attribute to the closest valid value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Hz
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdlastsegmentcenterfrequency
        
        	This attribute controls the center frequency of the last segment of the spectrum analysis measurement.  The frequency bins for this segment lie symmetrically to the left and right of this center frequency.   If the number of bins in a segment is odd, the segment center frequency lies directly on the center bin.   If the number of bins in a segment is even, the segment center frequency lies halfway between two bins.  The value of the LastSegmentCenterFrequency attribute  should be equal to the FirstSegmentCenterFrequency  plus and integer number of segment spans as determined  by the SegmentFrequencySpan.  Changing the value of this attribute may result in changes to the docsIf3CmSpectrumAnalysisMeasTable.  Note that if this attribute is set to an invalid value,  the device may return an error, or may adjust the  value of the attribute to the closest valid value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Hz
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdsegmentfrequencyspan
        
        	This attribute controls the frequency span of each  segment (instance) in the docsIf3CmSpectrumAnalysisMeasTable.    If set to a value of 0, then a default span will be chosen based on the hardware capabilities of the  device. Segments are contiguous from the  FirstSegementCenterFrequency to the  LastSegmentCenterFrequency and the center frequency  for each successive segment is incremented by the  SegmentFequencySpan.  The number of segments is (LastSegmentCenterFrequency \- FirstSegmentCenterFrequency)/SegmentFrequencySpan + 1.  A segment is equivalent to an instance in the  docsIf3CmSpectrumAnalysisMeasTable. The chosen  SegmentFrequencySpan affects the number of entries in  the docsIf3CmSpectrumAnalysisMeasTable. A more granular  SegmentFrequencySpan may adversely affect the amount of  time needed to query the table entries in addition to  possibly increasing the acquisition time.  Changing the value of this attribute may result in  changes to the docsIf3CmSpectrumAnalysisMeasTable.  Note that if this attribute is set to an invalid value, the device may return an error, or may adjust the value  of the object to the closest valid value
        	**type**\: int
        
        	**range:** 1000000..900000000
        
        	**units**\: Hz
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdnumbinspersegment
        
        	This attribute controls the number of bins collected  by the measurement performed for each segment (instance)  in the docsIf3CmSpectrumAnalysisMeasTable.    Note that if this attribute is set to an invalid value,  the device may return an error, or may adjust the value of the attribute to the closest valid value
        	**type**\: int
        
        	**range:** 2..2048
        
        	**units**\: bins-per-segment
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdequivalentnoisebandwidth
        
        	This attribute allows the user to request an equivalent  noise bandwidth for the resolution bandwidth filter used  in the spectrum analysis.  This corresponds to the  spectral width of the window function used when performing a discrete Fourier transform for the analysis.    The window function which corresponds to a value written  to this object may be obtained by reading the value of the WindowFunction attribute.  If an unsupported value is requested, the device may  return an error, or choose the closest valid value to the  one which is requested.   If the closest value is chosen, then a subsequent read of  this attribute will return the actual value which is in use
        	**type**\: int
        
        	**range:** 50..500
        
        	**units**\: hundredthsbin
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdwindowfunction
        
        	This attribute controls or indicates the windowing function  which will be used when performing the discrete Fourier transform for the analysis.  The WindowFunction and the Equivalent Noise Bandwidth are related. If a particular WindowFunction is selected, then the EquivalentNoiseBandwidth  for the function which is in use, will be reported by the EquivalentNoiseBandwidth attribute. Alternatively if an EquivalentNoiseBandwidth value is chosen then if a WindowFunction function representing that  EquivalentNoiseBandwidth is defined in the CM, that value will be reported in the WindowFunction MIB object, or a value of  'other' will be reported. Use of 'modern' windowing functions not yet defined will likely be reported as 'other'.  Note that all window functions may not be supported by all  devices.  If an attempt is made to set the object to an  unsupported window function, or if writing of the  WindowFunction is not supported, an error will be returned
        	**type**\:  :py:class:`SpectrumAnalysisWindowFunction <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.SpectrumAnalysisWindowFunction>`
        
        .. attribute:: docsif3cmspectrumanalysisctrlcmdnumberofaverages
        
        	This attribute controls the number of averages  that will be performed on spectral bins.   The average will be computed using the 'leaky integrator' method, where\:   reported bin value = alpha\*accumulated bin values +                         (1\-alpha)\*current bin value.    Alpha is one minus the reciprocal of the number of averages. For example, if N=25, then alpha = 0.96.   A value of 1 indicates no averaging.   Re\-writing the number of averages will restart the averaging process.  If there are no accumulated values, the  accumulators are made equal to the first measured bin  amplitudes.  If an attempt is made to set the attribute to an unsupported  number of averages, an error will be returned
        	**type**\: int
        
        	**range:** 1..1000
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisCtrlCmd, self).__init__()

            self.yang_name = "docsIf3CmSpectrumAnalysisCtrlCmd"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsif3cmspectrumanalysisctrlcmdenable', (YLeaf(YType.boolean, 'docsIf3CmSpectrumAnalysisCtrlCmdEnable'), ['bool'])),
                ('docsif3cmspectrumanalysisctrlcmdinactivitytimeout', (YLeaf(YType.int32, 'docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdfirstsegmentcenterfrequency', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdlastsegmentcenterfrequency', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdsegmentfrequencyspan', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdnumbinspersegment', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdequivalentnoisebandwidth', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth'), ['int'])),
                ('docsif3cmspectrumanalysisctrlcmdwindowfunction', (YLeaf(YType.enumeration, 'docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'SpectrumAnalysisWindowFunction', '')])),
                ('docsif3cmspectrumanalysisctrlcmdnumberofaverages', (YLeaf(YType.uint32, 'docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages'), ['int'])),
            ])
            self.docsif3cmspectrumanalysisctrlcmdenable = None
            self.docsif3cmspectrumanalysisctrlcmdinactivitytimeout = None
            self.docsif3cmspectrumanalysisctrlcmdfirstsegmentcenterfrequency = None
            self.docsif3cmspectrumanalysisctrlcmdlastsegmentcenterfrequency = None
            self.docsif3cmspectrumanalysisctrlcmdsegmentfrequencyspan = None
            self.docsif3cmspectrumanalysisctrlcmdnumbinspersegment = None
            self.docsif3cmspectrumanalysisctrlcmdequivalentnoisebandwidth = None
            self.docsif3cmspectrumanalysisctrlcmdwindowfunction = None
            self.docsif3cmspectrumanalysisctrlcmdnumberofaverages = None
            self._segment_path = lambda: "docsIf3CmSpectrumAnalysisCtrlCmd"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisCtrlCmd, ['docsif3cmspectrumanalysisctrlcmdenable', 'docsif3cmspectrumanalysisctrlcmdinactivitytimeout', 'docsif3cmspectrumanalysisctrlcmdfirstsegmentcenterfrequency', 'docsif3cmspectrumanalysisctrlcmdlastsegmentcenterfrequency', 'docsif3cmspectrumanalysisctrlcmdsegmentfrequencyspan', 'docsif3cmspectrumanalysisctrlcmdnumbinspersegment', 'docsif3cmspectrumanalysisctrlcmdequivalentnoisebandwidth', 'docsif3cmspectrumanalysisctrlcmdwindowfunction', 'docsif3cmspectrumanalysisctrlcmdnumberofaverages'], name, value)


    class DocsIf3CmStatusTable(Entity):
        """
        This object defines attributes of the CM connectivity
        status. This object provides CM connectivity status
        information of the CM previously available in
        the SNMP table docsIfCmStatusTable.
        
        .. attribute:: docsif3cmstatusentry
        
        	The conceptual row of docsIf3CmStatusTable. An instance exist for the CM MAC Domain Interface
        	**type**\: list of  		 :py:class:`DocsIf3CmStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmStatusTable.DocsIf3CmStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmStatusTable, self).__init__()

            self.yang_name = "docsIf3CmStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmStatusEntry", ("docsif3cmstatusentry", DOCSIF3MIB.DocsIf3CmStatusTable.DocsIf3CmStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3CmStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmStatusTable, [], name, value)


        class DocsIf3CmStatusEntry(Entity):
            """
            The conceptual row of docsIf3CmStatusTable.
            An instance exist for the CM MAC Domain Interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmstatusvalue
            
            	This attribute denotes the current CM connectivity state. For the case of IP acquisition related states, this attribute reflects states for the current CM provisioning mode, not the other DHCP process associated with dual stack operation
            	**type**\:  :py:class:`CmRegState <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.CmRegState>`
            
            .. attribute:: docsif3cmstatuscode
            
            	This attribute denotes the status code for CM as defined in the OSSI Specification. The status code consists of a single character indicating error groups, followed by a two\- or three\-digit number indicating the status condition, followed by a decimal. An example of a returned value could be 'T101.0'. The zero\-length hex string indicates no status code yet registered
            	**type**\: str
            
            	**length:** 0 \| 5..7
            
            .. attribute:: docsif3cmstatusresets
            
            	This attribute denotes the number of times the CM reset or initialized this interface. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: resets
            
            .. attribute:: docsif3cmstatuslostsyncs
            
            	This attribute denotes the number of times the CM lost synchronization with the downstream channel. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: messages
            
            .. attribute:: docsif3cmstatusinvalidmaps
            
            	This attribute denotes the number of times the CM received invalid MAP messages. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: maps
            
            .. attribute:: docsif3cmstatusinvaliducds
            
            	This attribute denotes the number of times the CM received invalid UCD messages. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: messages
            
            .. attribute:: docsif3cmstatusinvalidrangingrsps
            
            	This attribute denotes the number of times the CM received invalid ranging response messages. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: messages
            
            .. attribute:: docsif3cmstatusinvalidregrsps
            
            	This attribute denotes the number of times the CM received invalid registration response messages. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: messages
            
            .. attribute:: docsif3cmstatust1timeouts
            
            	This attribute denotes the number of times counter T1 expired in the CM. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: timeouts
            
            .. attribute:: docsif3cmstatust2timeouts
            
            	This attribute denotes the number of times counter T2 expired in the CM. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: timeouts
            
            .. attribute:: docsif3cmstatusuccssuccesses
            
            	This attribute denotes the number of successful Upstream Channel Change transactions. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime  for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            	**status**\: obsolete
            
            .. attribute:: docsif3cmstatusuccfails
            
            	This attribute denotes the number of failed Upstream Channel Change transactions. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            	**status**\: obsolete
            
            .. attribute:: docsif3cmstatusenergymgt1x1operstatus
            
            	This attribute indicates whether the CM is currently operating in Energy Management 1x1 Mode. If this attribute returns 'true',  the CM is operating in Energy Management 1x1 Mode
            	**type**\: bool
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmStatusTable.DocsIf3CmStatusEntry, self).__init__()

                self.yang_name = "docsIf3CmStatusEntry"
                self.yang_parent_name = "docsIf3CmStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmstatusvalue', (YLeaf(YType.enumeration, 'docsIf3CmStatusValue'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'CmRegState', '')])),
                    ('docsif3cmstatuscode', (YLeaf(YType.str, 'docsIf3CmStatusCode'), ['str'])),
                    ('docsif3cmstatusresets', (YLeaf(YType.uint32, 'docsIf3CmStatusResets'), ['int'])),
                    ('docsif3cmstatuslostsyncs', (YLeaf(YType.uint32, 'docsIf3CmStatusLostSyncs'), ['int'])),
                    ('docsif3cmstatusinvalidmaps', (YLeaf(YType.uint32, 'docsIf3CmStatusInvalidMaps'), ['int'])),
                    ('docsif3cmstatusinvaliducds', (YLeaf(YType.uint32, 'docsIf3CmStatusInvalidUcds'), ['int'])),
                    ('docsif3cmstatusinvalidrangingrsps', (YLeaf(YType.uint32, 'docsIf3CmStatusInvalidRangingRsps'), ['int'])),
                    ('docsif3cmstatusinvalidregrsps', (YLeaf(YType.uint32, 'docsIf3CmStatusInvalidRegRsps'), ['int'])),
                    ('docsif3cmstatust1timeouts', (YLeaf(YType.uint32, 'docsIf3CmStatusT1Timeouts'), ['int'])),
                    ('docsif3cmstatust2timeouts', (YLeaf(YType.uint32, 'docsIf3CmStatusT2Timeouts'), ['int'])),
                    ('docsif3cmstatusuccssuccesses', (YLeaf(YType.uint32, 'docsIf3CmStatusUCCsSuccesses'), ['int'])),
                    ('docsif3cmstatusuccfails', (YLeaf(YType.uint32, 'docsIf3CmStatusUCCFails'), ['int'])),
                    ('docsif3cmstatusenergymgt1x1operstatus', (YLeaf(YType.boolean, 'docsIf3CmStatusEnergyMgt1x1OperStatus'), ['bool'])),
                ])
                self.ifindex = None
                self.docsif3cmstatusvalue = None
                self.docsif3cmstatuscode = None
                self.docsif3cmstatusresets = None
                self.docsif3cmstatuslostsyncs = None
                self.docsif3cmstatusinvalidmaps = None
                self.docsif3cmstatusinvaliducds = None
                self.docsif3cmstatusinvalidrangingrsps = None
                self.docsif3cmstatusinvalidregrsps = None
                self.docsif3cmstatust1timeouts = None
                self.docsif3cmstatust2timeouts = None
                self.docsif3cmstatusuccssuccesses = None
                self.docsif3cmstatusuccfails = None
                self.docsif3cmstatusenergymgt1x1operstatus = None
                self._segment_path = lambda: "docsIf3CmStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmStatusTable.DocsIf3CmStatusEntry, ['ifindex', 'docsif3cmstatusvalue', 'docsif3cmstatuscode', 'docsif3cmstatusresets', 'docsif3cmstatuslostsyncs', 'docsif3cmstatusinvalidmaps', 'docsif3cmstatusinvaliducds', 'docsif3cmstatusinvalidrangingrsps', 'docsif3cmstatusinvalidregrsps', 'docsif3cmstatust1timeouts', 'docsif3cmstatust2timeouts', 'docsif3cmstatusuccssuccesses', 'docsif3cmstatusuccfails', 'docsif3cmstatusenergymgt1x1operstatus'], name, value)


    class DocsIf3CmStatusUsTable(Entity):
        """
        This object defines PHY and MAC information about
        the CM's upstream channels operating in Multiple Transmit
        Channel (MTC) mode or in a Pre\-3.0 DOSCIS transmit
        channel mode. This object provides per\-CM Upstream
        channel information previously available in the
        SNMP table docsIfCmStatusTable.
        
        .. attribute:: docsif3cmstatususentry
        
        	The conceptual row of docsIf3CmStatusUsTable. An instance exist for each of the CM's SC\-QAM upstream channels  which are configured for data transmission
        	**type**\: list of  		 :py:class:`DocsIf3CmStatusUsEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmStatusUsTable.DocsIf3CmStatusUsEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmStatusUsTable, self).__init__()

            self.yang_name = "docsIf3CmStatusUsTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmStatusUsEntry", ("docsif3cmstatususentry", DOCSIF3MIB.DocsIf3CmStatusUsTable.DocsIf3CmStatusUsEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmstatususentry = YList(self)
            self._segment_path = lambda: "docsIf3CmStatusUsTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmStatusUsTable, [], name, value)


        class DocsIf3CmStatusUsEntry(Entity):
            """
            The conceptual row of docsIf3CmStatusUsTable.
            An instance exist for each of the CM's SC\-QAM upstream channels 
            which are configured for data transmission.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmstatusustxpower
            
            	This attribute represents the operational CM transmit power for this SC\-QAM upstream channel. In order for this attribute to provide consistent information  under all circumstances, a 3.1 CM will report the average total  power for the SC\-QAM channel the same as was done for  DOCSIS 3.0, regardless of whether it is operating with a 3.1 or  a 3.0 CMTS. The value that is reported was referred to as Pr in  the DOCSIS 3.0 PHY Spec. This attribute is not applicable for  OFDMA channels
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: TenthdBmV
            
            .. attribute:: docsif3cmstatusust3timeouts
            
            	This attribute denotes the number of times counter T3 expired in the CM for this upstream channel. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: timeouts
            
            .. attribute:: docsif3cmstatusust4timeouts
            
            	This attribute denotes the number of times counter T4 expired in the CM for this upstream channel. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: timeouts
            
            .. attribute:: docsif3cmstatususrangingaborteds
            
            	This attribute denotes the number of times the ranging process was aborted by the CMTS. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime ([RFC2863]) for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: docsif3cmstatususmodulationtype
            
            	This attribute indicates modulation type status currently used by the CM for this upstream channel. Since this object specifically identifies PHY Layer mode, the shared upstream channel type 'tdmaAndAtdma' is not permitted
            	**type**\:  :py:class:`DocsisUpstreamType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamType>`
            
            .. attribute:: docsif3cmstatususeqdata
            
            	This attribute indicates the pre\-equalization data for the specified upstream Channel on this CM after convolution with data indicated in the RNG\-RSP. This data is valid when docsIfUpChannelPreEqEnable RFC 4546 is set to true
            	**type**\: str
            
            	**length:** 0 \| 36..260
            
            .. attribute:: docsif3cmstatusust3exceededs
            
            	This attribute denotes the number of times for excessive T3 timeouts. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: timeouts
            
            .. attribute:: docsif3cmstatususismuted
            
            	This attribute denotes whether the upstream channel is muted
            	**type**\: bool
            
            .. attribute:: docsif3cmstatususrangingstatus
            
            	This attribute denotes the ranging state of the CM
            	**type**\:  :py:class:`RangingState <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.RangingState>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmStatusUsTable.DocsIf3CmStatusUsEntry, self).__init__()

                self.yang_name = "docsIf3CmStatusUsEntry"
                self.yang_parent_name = "docsIf3CmStatusUsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmstatusustxpower', (YLeaf(YType.int32, 'docsIf3CmStatusUsTxPower'), ['int'])),
                    ('docsif3cmstatusust3timeouts', (YLeaf(YType.uint32, 'docsIf3CmStatusUsT3Timeouts'), ['int'])),
                    ('docsif3cmstatusust4timeouts', (YLeaf(YType.uint32, 'docsIf3CmStatusUsT4Timeouts'), ['int'])),
                    ('docsif3cmstatususrangingaborteds', (YLeaf(YType.uint32, 'docsIf3CmStatusUsRangingAborteds'), ['int'])),
                    ('docsif3cmstatususmodulationtype', (YLeaf(YType.enumeration, 'docsIf3CmStatusUsModulationType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamType', '')])),
                    ('docsif3cmstatususeqdata', (YLeaf(YType.str, 'docsIf3CmStatusUsEqData'), ['str'])),
                    ('docsif3cmstatusust3exceededs', (YLeaf(YType.uint32, 'docsIf3CmStatusUsT3Exceededs'), ['int'])),
                    ('docsif3cmstatususismuted', (YLeaf(YType.boolean, 'docsIf3CmStatusUsIsMuted'), ['bool'])),
                    ('docsif3cmstatususrangingstatus', (YLeaf(YType.enumeration, 'docsIf3CmStatusUsRangingStatus'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'RangingState', '')])),
                ])
                self.ifindex = None
                self.docsif3cmstatusustxpower = None
                self.docsif3cmstatusust3timeouts = None
                self.docsif3cmstatusust4timeouts = None
                self.docsif3cmstatususrangingaborteds = None
                self.docsif3cmstatususmodulationtype = None
                self.docsif3cmstatususeqdata = None
                self.docsif3cmstatusust3exceededs = None
                self.docsif3cmstatususismuted = None
                self.docsif3cmstatususrangingstatus = None
                self._segment_path = lambda: "docsIf3CmStatusUsEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmStatusUsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmStatusUsTable.DocsIf3CmStatusUsEntry, ['ifindex', 'docsif3cmstatusustxpower', 'docsif3cmstatusust3timeouts', 'docsif3cmstatusust4timeouts', 'docsif3cmstatususrangingaborteds', 'docsif3cmstatususmodulationtype', 'docsif3cmstatususeqdata', 'docsif3cmstatusust3exceededs', 'docsif3cmstatususismuted', 'docsif3cmstatususrangingstatus'], name, value)


    class DocsIf3CmtsCmRegStatusTable(Entity):
        """
        This object defines attributes that represent the CM's
        registration status as tracked by the CMTS.
        Refer to the individual attribute definitions for 
        applicability to 3.0 and 3.1 Cable Modems.
        
        .. attribute:: docsif3cmtscmregstatusentry
        
        	The conceptual row of docsIf3CmtsCmRegStatusTable
        	**type**\: list of  		 :py:class:`DocsIf3CmtsCmRegStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable, self).__init__()

            self.yang_name = "docsIf3CmtsCmRegStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsCmRegStatusEntry", ("docsif3cmtscmregstatusentry", DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtscmregstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsCmRegStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable, [], name, value)


        class DocsIf3CmtsCmRegStatusEntry(Entity):
            """
            The conceptual row of docsIf3CmtsCmRegStatusTable.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	This attribute uniquely identifies a CM.  The CMTS must assign a single id value for each CM MAC address seen by the CMTS.  The CMTS should ensure that the association between an Id and MAC Address remains constant during CMTS uptime
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsif3cmtscmregstatusmacaddr
            
            	This attribute represents the MAC address of the CM. If the CM has multiple MAC addresses, this is the MAC address associated with the MAC Domain interface
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsif3cmtscmregstatusipv6addr
            
            	This attribute represents the IPv6 address of the CM. If the CM has no Internet address assigned, or the Internet address is unknown, the value of this attribute is the all zeros address
            	**type**\: str
            
            .. attribute:: docsif3cmtscmregstatusipv6linklocal
            
            	This attribute represents the IPv6 local scope address of the CM. If the CM has no link local address assigned, or the Internet address is unknown, the value of this attribute is the all zeros address
            	**type**\: str
            
            .. attribute:: docsif3cmtscmregstatusipv4addr
            
            	This attribute represents the IPv4 address of this CM. If the CM has no IP address assigned, or the IP address is unknown, this object returns 0.0.0.0
            	**type**\: str
            
            .. attribute:: docsif3cmtscmregstatusvalue
            
            	This attribute represents the current CM connectivity state
            	**type**\:  :py:class:`CmtsCmRegState <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.CmtsCmRegState>`
            
            .. attribute:: docsif3cmtscmregstatusmdifindex
            
            	This attribute represents the interface Index of the CMTS MAC Domain where the CM is active. If the interface is unknown, the CMTS returns a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsif3cmtscmregstatusmdcmsgid
            
            	This attribute represents the ID of the MAC Domain CM Service Group Id (MD\-CM\-SG\-ID) in which the CM is registered. If the ID is unknown, the CMTS returns a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmregstatusrcpid
            
            	This attribute represents the RCP\-ID associated with the CM if the CM is in DOCSIS 3.0 mode. If the  RCP\-ID is unknown or the CM is in DOCSIS 3.1 mode, the CMTS returns a five octet long string of zeros
            	**type**\: str
            
            	**length:** 5
            
            .. attribute:: docsif3cmtscmregstatusrccstatusid
            
            	This attribute represents the RCC Id the CMTS used to configure the CM receive channel set during the registration process, if the CM is in DOCSIS 3.0 mode. If unknown or the CM is in DOCSIS 3.1 mode, the CMTS returns the value zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmregstatusrcsid
            
            	This attribute represents the Receive Channel Set (RCS) that the CM is currently using. If the RCS is unknown, the CMTS returns the value zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmregstatustcsid
            
            	This attribute represents Transmit Channel Set (TCS) the CM is currently using. If the TCS is unknown, the CMTS returns the value zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmregstatusqosversion
            
            	This attribute denotes the queuing services the CM  registered, either DOCSIS 1.1 QoS or DOCSIS 1.0 CoS mode
            	**type**\:  :py:class:`DocsisQosVersion <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisQosVersion>`
            
            .. attribute:: docsif3cmtscmregstatuslastregtime
            
            	This attribute represents the last time the CM registered
            	**type**\: str
            
            .. attribute:: docsif3cmtscmregstatusaddrresolutionreqs
            
            	This attribute counts the number of upstream packets received on the SIDs assigned to a CM that are any of the following\: Upstream IPv4 ARP Requests Upstream IPv6 Neighbor Solicitation Requests (For Routing CMTSs) Upstream IPv4 or IPv6 packets to unresolved destinations in locally connected downstream subnets in the HFC. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated MAC Domain interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmregstatusenergymgtenabled
            
            	This attribute indicates which, if any, of the Energy  Management Features are enabled for this CM. If this attribute returns the em1x1Mode(0) bit set, the CM is configured with the  Energy Management 1x1 Feature enabled. If this attribute returns the dlsMode(1) bit set, the CM is configured with the DLS Feature enabled. If this attribute returns all bits cleared, the CM will  not request to operate in any Energy Management mode of operation.    Note\: This attribute only indicates if an Energy Management Feature  is enabled/disabled via the CM config file and registration  request/response exchange and does not indicate whether the CM is  actively operating in an Energy Management Mode
            	**type**\:  :py:class:`DocsIf3CmtsCmRegStatusEnergyMgtEnabled <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry.DocsIf3CmtsCmRegStatusEnergyMgtEnabled>`
            
            .. attribute:: docsif3cmtscmregstatusenergymgtoperstatus
            
            	This attribute indicates whether the CM is currently operating in an Energy Management Mode. If this attribute returns the em1x1Mode(0) bit set, the CM is operating in Energy Management 1x1 Mode. If this attribute returns the dlsMode(1) bit set, the CM is operating in DLS Mode. If this attribute returns all bits  cleared, the CM is not operating in any Energy Management Mode.  This attribute always returns 0x00 (no bits set) in the case when  docsIf3CmtsCmRegStatusEnergyMgtEnabled is set to 0x00 (no Energy  Management Features enabled).  Note\: dlsMode(1) and em1x1Mode(0) are mutually exclusive, thus  a return value where both of these bits are 'true' is invalid
            	**type**\:  :py:class:`DocsIf3CmtsCmRegStatusEnergyMgtOperStatus <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry.DocsIf3CmtsCmRegStatusEnergyMgtOperStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry, self).__init__()

                self.yang_name = "docsIf3CmtsCmRegStatusEntry"
                self.yang_parent_name = "docsIf3CmtsCmRegStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docsif3cmtscmregstatusmacaddr', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusMacAddr'), ['str'])),
                    ('docsif3cmtscmregstatusipv6addr', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusIPv6Addr'), ['str'])),
                    ('docsif3cmtscmregstatusipv6linklocal', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusIPv6LinkLocal'), ['str'])),
                    ('docsif3cmtscmregstatusipv4addr', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusIPv4Addr'), ['str'])),
                    ('docsif3cmtscmregstatusvalue', (YLeaf(YType.enumeration, 'docsIf3CmtsCmRegStatusValue'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'CmtsCmRegState', '')])),
                    ('docsif3cmtscmregstatusmdifindex', (YLeaf(YType.int32, 'docsIf3CmtsCmRegStatusMdIfIndex'), ['int'])),
                    ('docsif3cmtscmregstatusmdcmsgid', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusMdCmSgId'), ['int'])),
                    ('docsif3cmtscmregstatusrcpid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusRcpId'), ['str'])),
                    ('docsif3cmtscmregstatusrccstatusid', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusRccStatusId'), ['int'])),
                    ('docsif3cmtscmregstatusrcsid', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusRcsId'), ['int'])),
                    ('docsif3cmtscmregstatustcsid', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusTcsId'), ['int'])),
                    ('docsif3cmtscmregstatusqosversion', (YLeaf(YType.enumeration, 'docsIf3CmtsCmRegStatusQosVersion'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisQosVersion', '')])),
                    ('docsif3cmtscmregstatuslastregtime', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusLastRegTime'), ['str'])),
                    ('docsif3cmtscmregstatusaddrresolutionreqs', (YLeaf(YType.uint32, 'docsIf3CmtsCmRegStatusAddrResolutionReqs'), ['int'])),
                    ('docsif3cmtscmregstatusenergymgtenabled', (YLeaf(YType.bits, 'docsIf3CmtsCmRegStatusEnergyMgtEnabled'), ['Bits'])),
                    ('docsif3cmtscmregstatusenergymgtoperstatus', (YLeaf(YType.bits, 'docsIf3CmtsCmRegStatusEnergyMgtOperStatus'), ['Bits'])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docsif3cmtscmregstatusmacaddr = None
                self.docsif3cmtscmregstatusipv6addr = None
                self.docsif3cmtscmregstatusipv6linklocal = None
                self.docsif3cmtscmregstatusipv4addr = None
                self.docsif3cmtscmregstatusvalue = None
                self.docsif3cmtscmregstatusmdifindex = None
                self.docsif3cmtscmregstatusmdcmsgid = None
                self.docsif3cmtscmregstatusrcpid = None
                self.docsif3cmtscmregstatusrccstatusid = None
                self.docsif3cmtscmregstatusrcsid = None
                self.docsif3cmtscmregstatustcsid = None
                self.docsif3cmtscmregstatusqosversion = None
                self.docsif3cmtscmregstatuslastregtime = None
                self.docsif3cmtscmregstatusaddrresolutionreqs = None
                self.docsif3cmtscmregstatusenergymgtenabled = Bits()
                self.docsif3cmtscmregstatusenergymgtoperstatus = Bits()
                self._segment_path = lambda: "docsIf3CmtsCmRegStatusEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsCmRegStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry, ['docsif3cmtscmregstatusid', 'docsif3cmtscmregstatusmacaddr', 'docsif3cmtscmregstatusipv6addr', 'docsif3cmtscmregstatusipv6linklocal', 'docsif3cmtscmregstatusipv4addr', 'docsif3cmtscmregstatusvalue', 'docsif3cmtscmregstatusmdifindex', 'docsif3cmtscmregstatusmdcmsgid', 'docsif3cmtscmregstatusrcpid', 'docsif3cmtscmregstatusrccstatusid', 'docsif3cmtscmregstatusrcsid', 'docsif3cmtscmregstatustcsid', 'docsif3cmtscmregstatusqosversion', 'docsif3cmtscmregstatuslastregtime', 'docsif3cmtscmregstatusaddrresolutionreqs', 'docsif3cmtscmregstatusenergymgtenabled', 'docsif3cmtscmregstatusenergymgtoperstatus'], name, value)


    class DocsIf3CmtsCmUsStatusTable(Entity):
        """
        This object defines status information of the CM
        currently in use Upstream Logical Channels, as reported
        by the CMTS.
        
        .. attribute:: docsif3cmtscmusstatusentry
        
        	The conceptual row of docsIf3CmtsCmUsStatusTable
        	**type**\: list of  		 :py:class:`DocsIf3CmtsCmUsStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable.DocsIf3CmtsCmUsStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable, self).__init__()

            self.yang_name = "docsIf3CmtsCmUsStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsCmUsStatusEntry", ("docsif3cmtscmusstatusentry", DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable.DocsIf3CmtsCmUsStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtscmusstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsCmUsStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable, [], name, value)


        class DocsIf3CmtsCmUsStatusEntry(Entity):
            """
            The conceptual row of docsIf3CmtsCmUsStatusTable.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3cmtscmregstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
            
            .. attribute:: docsif3cmtscmusstatuschifindex  (key)
            
            	This attribute is a key that represents the ifIndex of the upstream interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsif3cmtscmusstatusmodulationtype
            
            	This attribute represents the modulation type currently used by this upstream channel
            	**type**\:  :py:class:`DocsisUpstreamType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamType>`
            
            .. attribute:: docsif3cmtscmusstatusrxpower
            
            	This attribute represents the receive power of this upstream channel. The reported value represents the total average power for the  channel regardless of whether the CM is reporting Pr, total  average power, or P1.6r, the power spectral density in an  equivalent 1.6 MHz spectrum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: TenthdBmV
            
            .. attribute:: docsif3cmtscmusstatussignalnoise
            
            	This attribute represents Signal/Noise ratio as perceived for upstream data from the CM on this upstream channel
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: TenthdB
            
            .. attribute:: docsif3cmtscmusstatusmicroreflections
            
            	This attribute represents microreflections received on this upstream channel
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: -dBc
            
            .. attribute:: docsif3cmtscmusstatuseqdata
            
            	This attribute represents the equalization data for the CM on this upstream channel
            	**type**\: str
            
            	**length:** 0 \| 36..260
            
            .. attribute:: docsif3cmtscmusstatusunerroreds
            
            	This attribute represents the codewords received without error from the CM on this interface. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmusstatuscorrecteds
            
            	This attribute represents the codewords received with correctable errors from the CM on this upstream channel. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmusstatusuncorrectables
            
            	This attribute represents the codewords received with uncorrectable errors from the CM on this upstream channel. Discontinuities in the value of this counter can occur at re\-initialization of the managed system, and at other times as indicated by the value of ifCounterDiscontinuityTime for the associated upstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtscmusstatushighresolutiontimingoffset
            
            	This attribute represents the current measured round trip time on this CM's upstream channel in units of (6.25 microseconds/(64\*256)).  This attribute returns zero if the value is unknown
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: time tick/(64*256)
            
            .. attribute:: docsif3cmtscmusstatusismuted
            
            	This attribute has a value 'true' to indicate that  the CM's upstream channel has been muted via  CM\-CTRL\-REQ/CM\-CTRL\-RSP message exchange
            	**type**\: bool
            
            .. attribute:: docsif3cmtscmusstatusrangingstatus
            
            	This attribute denotes the ranging state of the CM
            	**type**\:  :py:class:`RangingState <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.RangingState>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable.DocsIf3CmtsCmUsStatusEntry, self).__init__()

                self.yang_name = "docsIf3CmtsCmUsStatusEntry"
                self.yang_parent_name = "docsIf3CmtsCmUsStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid','docsif3cmtscmusstatuschifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docsif3cmtscmusstatuschifindex', (YLeaf(YType.int32, 'docsIf3CmtsCmUsStatusChIfIndex'), ['int'])),
                    ('docsif3cmtscmusstatusmodulationtype', (YLeaf(YType.enumeration, 'docsIf3CmtsCmUsStatusModulationType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamType', '')])),
                    ('docsif3cmtscmusstatusrxpower', (YLeaf(YType.int32, 'docsIf3CmtsCmUsStatusRxPower'), ['int'])),
                    ('docsif3cmtscmusstatussignalnoise', (YLeaf(YType.int32, 'docsIf3CmtsCmUsStatusSignalNoise'), ['int'])),
                    ('docsif3cmtscmusstatusmicroreflections', (YLeaf(YType.uint32, 'docsIf3CmtsCmUsStatusMicroreflections'), ['int'])),
                    ('docsif3cmtscmusstatuseqdata', (YLeaf(YType.str, 'docsIf3CmtsCmUsStatusEqData'), ['str'])),
                    ('docsif3cmtscmusstatusunerroreds', (YLeaf(YType.uint32, 'docsIf3CmtsCmUsStatusUnerroreds'), ['int'])),
                    ('docsif3cmtscmusstatuscorrecteds', (YLeaf(YType.uint32, 'docsIf3CmtsCmUsStatusCorrecteds'), ['int'])),
                    ('docsif3cmtscmusstatusuncorrectables', (YLeaf(YType.uint32, 'docsIf3CmtsCmUsStatusUncorrectables'), ['int'])),
                    ('docsif3cmtscmusstatushighresolutiontimingoffset', (YLeaf(YType.int32, 'docsIf3CmtsCmUsStatusHighResolutionTimingOffset'), ['int'])),
                    ('docsif3cmtscmusstatusismuted', (YLeaf(YType.boolean, 'docsIf3CmtsCmUsStatusIsMuted'), ['bool'])),
                    ('docsif3cmtscmusstatusrangingstatus', (YLeaf(YType.enumeration, 'docsIf3CmtsCmUsStatusRangingStatus'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'RangingState', '')])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docsif3cmtscmusstatuschifindex = None
                self.docsif3cmtscmusstatusmodulationtype = None
                self.docsif3cmtscmusstatusrxpower = None
                self.docsif3cmtscmusstatussignalnoise = None
                self.docsif3cmtscmusstatusmicroreflections = None
                self.docsif3cmtscmusstatuseqdata = None
                self.docsif3cmtscmusstatusunerroreds = None
                self.docsif3cmtscmusstatuscorrecteds = None
                self.docsif3cmtscmusstatusuncorrectables = None
                self.docsif3cmtscmusstatushighresolutiontimingoffset = None
                self.docsif3cmtscmusstatusismuted = None
                self.docsif3cmtscmusstatusrangingstatus = None
                self._segment_path = lambda: "docsIf3CmtsCmUsStatusEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']" + "[docsIf3CmtsCmUsStatusChIfIndex='" + str(self.docsif3cmtscmusstatuschifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsCmUsStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmUsStatusTable.DocsIf3CmtsCmUsStatusEntry, ['docsif3cmtscmregstatusid', 'docsif3cmtscmusstatuschifindex', 'docsif3cmtscmusstatusmodulationtype', 'docsif3cmtscmusstatusrxpower', 'docsif3cmtscmusstatussignalnoise', 'docsif3cmtscmusstatusmicroreflections', 'docsif3cmtscmusstatuseqdata', 'docsif3cmtscmusstatusunerroreds', 'docsif3cmtscmusstatuscorrecteds', 'docsif3cmtscmusstatusuncorrectables', 'docsif3cmtscmusstatushighresolutiontimingoffset', 'docsif3cmtscmusstatusismuted', 'docsif3cmtscmusstatusrangingstatus'], name, value)


    class DocsIf3MdChCfgTable(Entity):
        """
        This object configures the association of downstream
        and upstream channels to a particular MAC Domain
        (MD) on a CMTS.  The creation of channels and MAC domain
        object interface instances is vendor\-specific.
        In particular, the assignment of the channel interface
        index is normally vendor\-specific. Therefore,
        this object is intended only for associating channels
        to a MAC Domain and assumes that those channels were
        previously configured.
        The CMTS may have restrictions on which channels can
        be configured in the same MAC Domain.  For example, it
        could require the upstream channels to be from the same
        line card.
        This object supports the creation and deletion of multiple
        instances.
        Creation of a new instance of this object requires the
        ChId attribute to be set.
        
        .. attribute:: docsif3mdchcfgentry
        
        	The conceptual row of docsIf3MdChCfgTable. The ifIndex key corresponds to the MAC Domain interface where the channel is configured. The CMTS persists all instances of MdChCfg across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3MdChCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdChCfgTable.DocsIf3MdChCfgEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdChCfgTable, self).__init__()

            self.yang_name = "docsIf3MdChCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdChCfgEntry", ("docsif3mdchcfgentry", DOCSIF3MIB.DocsIf3MdChCfgTable.DocsIf3MdChCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3mdchcfgentry = YList(self)
            self._segment_path = lambda: "docsIf3MdChCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdChCfgTable, [], name, value)


        class DocsIf3MdChCfgEntry(Entity):
            """
            The conceptual row of docsIf3MdChCfgTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the channel is configured.
            The CMTS persists all instances of MdChCfg across
            reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3mdchcfgchifindex  (key)
            
            	This key represents the interface index of an existing upstream or downstream channel that is configured to be part of the MAC Domain. For the case of upstream interfaces the CMTS could reject the assignment of upstream logical channels under the same physical upstream interface to different MAC Domains
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsif3mdchcfgispricapableds
            
            	If set to 'true', this attribute configures the downstream channel as Primary\-Capable.  The default value for a downstream channel is 'true'. This attribute is not relevant for upstream interfaces,  therefore it reports the value 'false' for such interfaces. A CMTS may restrict the permitted value of this attribute based upon physical channel capabilities
            	**type**\: bool
            
            .. attribute:: docsif3mdchcfgchid
            
            	This attribute contains the 8\-bit Downstream Channel ID (DCID) or Upstream Channel ID (UCID) configured for the channel in the MAC Domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsif3mdchcfgsfprovattrmask
            
            	This attribute contains Provisioned Attribute Mask of non\-bonded service flow assignment to this channel
            	**type**\:  :py:class:`AttributeMask <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.AttributeMask>`
            
            .. attribute:: docsif3mdchcfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdChCfgTable.DocsIf3MdChCfgEntry, self).__init__()

                self.yang_name = "docsIf3MdChCfgEntry"
                self.yang_parent_name = "docsIf3MdChCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3mdchcfgchifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3mdchcfgchifindex', (YLeaf(YType.int32, 'docsIf3MdChCfgChIfIndex'), ['int'])),
                    ('docsif3mdchcfgispricapableds', (YLeaf(YType.boolean, 'docsIf3MdChCfgIsPriCapableDs'), ['bool'])),
                    ('docsif3mdchcfgchid', (YLeaf(YType.uint32, 'docsIf3MdChCfgChId'), ['int'])),
                    ('docsif3mdchcfgsfprovattrmask', (YLeaf(YType.bits, 'docsIf3MdChCfgSfProvAttrMask'), ['Bits'])),
                    ('docsif3mdchcfgrowstatus', (YLeaf(YType.enumeration, 'docsIf3MdChCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3mdchcfgchifindex = None
                self.docsif3mdchcfgispricapableds = None
                self.docsif3mdchcfgchid = None
                self.docsif3mdchcfgsfprovattrmask = Bits()
                self.docsif3mdchcfgrowstatus = None
                self._segment_path = lambda: "docsIf3MdChCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3MdChCfgChIfIndex='" + str(self.docsif3mdchcfgchifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdChCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdChCfgTable.DocsIf3MdChCfgEntry, ['ifindex', 'docsif3mdchcfgchifindex', 'docsif3mdchcfgispricapableds', 'docsif3mdchcfgchid', 'docsif3mdchcfgsfprovattrmask', 'docsif3mdchcfgrowstatus'], name, value)


    class DocsIf3RccCfgTable(Entity):
        """
        This object identifies the scope of the Receive Channel
        Configuration (RCC) and provides a top level container
        for the Receive Module and Receive Channel
        objects.  The CMTS selects an instance of this object
        to assign to a CM when it registers.
        This object supports the creation and deletion of multiple
        instances.
        
        .. attribute:: docsif3rcccfgentry
        
        	The conceptual row of docsIf3RccCfgTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured.  The CMTS persists all instances of RccCfg across  reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3RccCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RccCfgTable, self).__init__()

            self.yang_name = "docsIf3RccCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RccCfgEntry", ("docsif3rcccfgentry", DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3rcccfgentry = YList(self)
            self._segment_path = lambda: "docsIf3RccCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RccCfgTable, [], name, value)


        class DocsIf3RccCfgEntry(Entity):
            """
            The conceptual row of docsIf3RccCfgTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured.
             The CMTS persists all instances of RccCfg across
             reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rcccfgrcpid  (key)
            
            	This key represents the 'Receive Channel Profile Identifier' (RCP\-ID) configured for the MAC Domain indicated by this instance
            	**type**\: str
            
            	**length:** 5
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgrcccfgid  (key)
            
            	This key denotes an RCC combination assignment for a particular RcpId and is unique per combination of MAC Domain and RcpId
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgvendorspecific
            
            	This attribute contains vendor\-specific information of the CM Receive Channel configuration
            	**type**\: str
            
            	**length:** 0..252
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgdescription
            
            	This attribute contains a human\-readable description of the CM RCP Configuration
            	**type**\: str
            
            	**length:** 0..15
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry, self).__init__()

                self.yang_name = "docsIf3RccCfgEntry"
                self.yang_parent_name = "docsIf3RccCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rcccfgrcpid','docsif3rcccfgrcccfgid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rcccfgrcpid', (YLeaf(YType.str, 'docsIf3RccCfgRcpId'), ['str'])),
                    ('docsif3rcccfgrcccfgid', (YLeaf(YType.uint32, 'docsIf3RccCfgRccCfgId'), ['int'])),
                    ('docsif3rcccfgvendorspecific', (YLeaf(YType.str, 'docsIf3RccCfgVendorSpecific'), ['str'])),
                    ('docsif3rcccfgdescription', (YLeaf(YType.str, 'docsIf3RccCfgDescription'), ['str'])),
                    ('docsif3rcccfgrowstatus', (YLeaf(YType.enumeration, 'docsIf3RccCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3rcccfgrcpid = None
                self.docsif3rcccfgrcccfgid = None
                self.docsif3rcccfgvendorspecific = None
                self.docsif3rcccfgdescription = None
                self.docsif3rcccfgrowstatus = None
                self._segment_path = lambda: "docsIf3RccCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccCfgRcpId='" + str(self.docsif3rcccfgrcpid) + "']" + "[docsIf3RccCfgRccCfgId='" + str(self.docsif3rcccfgrcccfgid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RccCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry, ['ifindex', 'docsif3rcccfgrcpid', 'docsif3rcccfgrcccfgid', 'docsif3rcccfgvendorspecific', 'docsif3rcccfgdescription', 'docsif3rcccfgrowstatus'], name, value)


    class DocsIf3RccStatusTable(Entity):
        """
        The RCC Status object provides a read\-only view of
        the statically\-configured (from the RccCfg object)
        and dynamically\-created RCCs.
        The CMTS creates an RCC Status instance for each unique
        MAC Domain Cable Modem Service Group (MD\-CM\-SG) to
        which it signals an RCC to the CM.
        
        .. attribute:: docsif3rccstatusentry
        
        	The conceptual row of docsIf3RccStatusTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured
        	**type**\: list of  		 :py:class:`DocsIf3RccStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RccStatusTable, self).__init__()

            self.yang_name = "docsIf3RccStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RccStatusEntry", ("docsif3rccstatusentry", DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3rccstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3RccStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RccStatusTable, [], name, value)


        class DocsIf3RccStatusEntry(Entity):
            """
            The conceptual row of docsIf3RccStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rccstatusrcpid  (key)
            
            	This key represents the RCP\-ID to which this instance applies
            	**type**\: str
            
            	**length:** 5
            
            .. attribute:: docsif3rccstatusrccstatusid  (key)
            
            	This key represents an RCC combination for a particular RcpId either from an RCC configuration object or a CMTS\-determined RCC and is unique per combination of MAC Domain IfIndex and RcpId
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsif3rccstatusrcccfgid
            
            	This attribute identifies an RCC\-Configured combination from which this instance was defined. If nonzero, it corresponds to the RccCfg instance from which the RCC was created. Zero means that the  RCC was dynamically created by the CMTS
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsif3rccstatusvaliditycode
            
            	This attribute indicates whether the RCC instance of this object is valid or not. An RCC Status instance from a configured or a dynamic RCC could become invalid, for example, due changes in the topology
            	**type**\:  :py:class:`DocsIf3RccStatusValidityCode <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry.DocsIf3RccStatusValidityCode>`
            
            .. attribute:: docsif3rccstatusvaliditycodetext
            
            	This attribute contains the CMTS vendor\-specific log information from the Receive Channel Configuration Status encoding
            	**type**\: str
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry, self).__init__()

                self.yang_name = "docsIf3RccStatusEntry"
                self.yang_parent_name = "docsIf3RccStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rccstatusrcpid','docsif3rccstatusrccstatusid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rccstatusrcpid', (YLeaf(YType.str, 'docsIf3RccStatusRcpId'), ['str'])),
                    ('docsif3rccstatusrccstatusid', (YLeaf(YType.uint32, 'docsIf3RccStatusRccStatusId'), ['int'])),
                    ('docsif3rccstatusrcccfgid', (YLeaf(YType.uint32, 'docsIf3RccStatusRccCfgId'), ['int'])),
                    ('docsif3rccstatusvaliditycode', (YLeaf(YType.enumeration, 'docsIf3RccStatusValidityCode'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3RccStatusTable.DocsIf3RccStatusEntry.DocsIf3RccStatusValidityCode')])),
                    ('docsif3rccstatusvaliditycodetext', (YLeaf(YType.str, 'docsIf3RccStatusValidityCodeText'), ['str'])),
                ])
                self.ifindex = None
                self.docsif3rccstatusrcpid = None
                self.docsif3rccstatusrccstatusid = None
                self.docsif3rccstatusrcccfgid = None
                self.docsif3rccstatusvaliditycode = None
                self.docsif3rccstatusvaliditycodetext = None
                self._segment_path = lambda: "docsIf3RccStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccStatusRcpId='" + str(self.docsif3rccstatusrcpid) + "']" + "[docsIf3RccStatusRccStatusId='" + str(self.docsif3rccstatusrccstatusid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RccStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry, ['ifindex', 'docsif3rccstatusrcpid', 'docsif3rccstatusrccstatusid', 'docsif3rccstatusrcccfgid', 'docsif3rccstatusvaliditycode', 'docsif3rccstatusvaliditycodetext'], name, value)

            class DocsIf3RccStatusValidityCode(Enum):
                """
                DocsIf3RccStatusValidityCode (Enum Class)

                This attribute indicates whether the RCC instance

                of this object is valid or not. An RCC Status instance

                from a configured or a dynamic RCC could become invalid,

                for example, due changes in the topology.

                .. data:: other = 1

                .. data:: valid = 2

                .. data:: invalid = 3

                .. data:: wrongPrimaryDs = 4

                .. data:: missingPrimaryDs = 5

                .. data:: multiplePrimaryDs = 6

                .. data:: duplicateDs = 7

                .. data:: wrongFrequencyRange = 8

                .. data:: wrongConnectivity = 9

                """

                other = Enum.YLeaf(1, "other")

                valid = Enum.YLeaf(2, "valid")

                invalid = Enum.YLeaf(3, "invalid")

                wrongPrimaryDs = Enum.YLeaf(4, "wrongPrimaryDs")

                missingPrimaryDs = Enum.YLeaf(5, "missingPrimaryDs")

                multiplePrimaryDs = Enum.YLeaf(6, "multiplePrimaryDs")

                duplicateDs = Enum.YLeaf(7, "duplicateDs")

                wrongFrequencyRange = Enum.YLeaf(8, "wrongFrequencyRange")

                wrongConnectivity = Enum.YLeaf(9, "wrongConnectivity")



    class DocsIf3RxChCfgTable(Entity):
        """
        The Receive Channel Configuration object permits
        an operator to configure how CMs registered with certain
        Receive Channel Profiles will configure the Receive
        Channels within their profile. When a CM registers
        with an RCP for which all Receive Channel Indices
        (RcIds) are configured in the Receive Module object
        and all Receive Channels are configured within this
        object, the CMTS should use the configuration within
        these objects to set the Receive Channel Configuration
        returned to the CM in a REG\-RSP message.  A CMTS
        may require configuration of all pertinent Receive
        Module and Receive Channel instances in order to register
        a CM that reports a Receive Channel Profile (RCP),
        including any standard Receive Channel Profiles.
        If the CM reports multiple RCPs, and Receive Module
        and Receive Channel objects have instances for more
        than one RCP, the particular RCP selected by the CMTS
        is not specified.  A CMTS is not restricted to assigning
        Receive Modules based only on the contents of this
        object.
        This object supports the creation and deletion of multiple
        instances.
        Creation of a new instance of this object requires the
        ChIfIndex attribute to be set and a valid reference of
        a RccCfg instance.
        
        .. attribute:: docsif3rxchcfgentry
        
        	The conceptual row of docsIf3RxChCfgTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured. The CMTS persists all instances of ReceiveChannelCfg across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3RxChCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxChCfgTable.DocsIf3RxChCfgEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RxChCfgTable, self).__init__()

            self.yang_name = "docsIf3RxChCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RxChCfgEntry", ("docsif3rxchcfgentry", DOCSIF3MIB.DocsIf3RxChCfgTable.DocsIf3RxChCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3rxchcfgentry = YList(self)
            self._segment_path = lambda: "docsIf3RxChCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RxChCfgTable, [], name, value)


        class DocsIf3RxChCfgEntry(Entity):
            """
            The conceptual row of docsIf3RxChCfgTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured.
            The CMTS persists all instances of ReceiveChannelCfg across
            reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rcccfgrcpid  (key)
            
            	
            	**type**\: str
            
            	**length:** 5
            
            	**refers to**\:  :py:class:`docsif3rcccfgrcpid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry>`
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgrcccfgid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3rcccfgrcccfgid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry>`
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxchcfgrcid  (key)
            
            	This key represents an identifier for the parameters of the Receive Channel instance within the Receive Channel Profile
            	**type**\: int
            
            	**range:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxchcfgchifindex
            
            	This attribute contains the interface index of a Downstream Channel that this Receive Channel Instance defines
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxchcfgprimarydsindicator
            
            	If set to 'true', this attribute indicates the Receive Channel is to be the primary\-capable downstream channel for the CM receiving this RCC. Otherwise, the downstream channel is to be a non\-primary\-capable channel
            	**type**\: bool
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxchcfgrcrmconnectivityid
            
            	This attribute indicates the Receive Module (via the RmId from the ReceiveModule object) to which this Receive Channel connects.  If this object contains a zero value (and thus no Receive Channel Connectivity), the Receive Channel Connectivity TLV is omitted from the RCC
            	**type**\: int
            
            	**range:** 0..255
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxchcfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RxChCfgTable.DocsIf3RxChCfgEntry, self).__init__()

                self.yang_name = "docsIf3RxChCfgEntry"
                self.yang_parent_name = "docsIf3RxChCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rcccfgrcpid','docsif3rcccfgrcccfgid','docsif3rxchcfgrcid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rcccfgrcpid', (YLeaf(YType.str, 'docsIf3RccCfgRcpId'), ['str'])),
                    ('docsif3rcccfgrcccfgid', (YLeaf(YType.str, 'docsIf3RccCfgRccCfgId'), ['int'])),
                    ('docsif3rxchcfgrcid', (YLeaf(YType.uint32, 'docsIf3RxChCfgRcId'), ['int'])),
                    ('docsif3rxchcfgchifindex', (YLeaf(YType.int32, 'docsIf3RxChCfgChIfIndex'), ['int'])),
                    ('docsif3rxchcfgprimarydsindicator', (YLeaf(YType.boolean, 'docsIf3RxChCfgPrimaryDsIndicator'), ['bool'])),
                    ('docsif3rxchcfgrcrmconnectivityid', (YLeaf(YType.uint32, 'docsIf3RxChCfgRcRmConnectivityId'), ['int'])),
                    ('docsif3rxchcfgrowstatus', (YLeaf(YType.enumeration, 'docsIf3RxChCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3rcccfgrcpid = None
                self.docsif3rcccfgrcccfgid = None
                self.docsif3rxchcfgrcid = None
                self.docsif3rxchcfgchifindex = None
                self.docsif3rxchcfgprimarydsindicator = None
                self.docsif3rxchcfgrcrmconnectivityid = None
                self.docsif3rxchcfgrowstatus = None
                self._segment_path = lambda: "docsIf3RxChCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccCfgRcpId='" + str(self.docsif3rcccfgrcpid) + "']" + "[docsIf3RccCfgRccCfgId='" + str(self.docsif3rcccfgrcccfgid) + "']" + "[docsIf3RxChCfgRcId='" + str(self.docsif3rxchcfgrcid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RxChCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RxChCfgTable.DocsIf3RxChCfgEntry, ['ifindex', 'docsif3rcccfgrcpid', 'docsif3rcccfgrcccfgid', 'docsif3rxchcfgrcid', 'docsif3rxchcfgchifindex', 'docsif3rxchcfgprimarydsindicator', 'docsif3rxchcfgrcrmconnectivityid', 'docsif3rxchcfgrowstatus'], name, value)


    class DocsIf3RxChStatusTable(Entity):
        """
        The Receive Channel Status object reports the status
        of the statically\-configured and dynamically\-created
        Receive Channels within an RCC.
        
        .. attribute:: docsif3rxchstatusentry
        
        	The conceptual row of docsIf3RxChStatusTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured. When this object is defined on the CM, the value of RccStatusId is always 1
        	**type**\: list of  		 :py:class:`DocsIf3RxChStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxChStatusTable.DocsIf3RxChStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RxChStatusTable, self).__init__()

            self.yang_name = "docsIf3RxChStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RxChStatusEntry", ("docsif3rxchstatusentry", DOCSIF3MIB.DocsIf3RxChStatusTable.DocsIf3RxChStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3rxchstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3RxChStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RxChStatusTable, [], name, value)


        class DocsIf3RxChStatusEntry(Entity):
            """
            The conceptual row of docsIf3RxChStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured. When this object is defined
            on the CM, the value of RccStatusId is always 1.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rccstatusrcpid  (key)
            
            	
            	**type**\: str
            
            	**length:** 5
            
            	**refers to**\:  :py:class:`docsif3rccstatusrcpid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry>`
            
            .. attribute:: docsif3rccstatusrccstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3rccstatusrccstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry>`
            
            .. attribute:: docsif3rxchstatusrcid  (key)
            
            	This key represents an identifier for the parameters of the Receive Channel instance within the Receive Channel Profile
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsif3rxchstatuschifindex
            
            	This attribute contains the interface index of the Downstream Channel that this Receive Channel Instance defines
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsif3rxchstatusprimarydsindicator
            
            	If set to 'true', this attribute indicates the Receive Channel is to be the primary\-capable downstream channel for the CM receiving this RCC. Otherwise, the downstream channel is to be a non\-primary\-capable channel
            	**type**\: bool
            
            .. attribute:: docsif3rxchstatusrcrmconnectivityid
            
            	This attribute identifies the Receive Module to which this Receive Channel connects.  A value a zero indicates that the Receive Channel Connectivity TLV is omitted from the RCC
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RxChStatusTable.DocsIf3RxChStatusEntry, self).__init__()

                self.yang_name = "docsIf3RxChStatusEntry"
                self.yang_parent_name = "docsIf3RxChStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rccstatusrcpid','docsif3rccstatusrccstatusid','docsif3rxchstatusrcid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rccstatusrcpid', (YLeaf(YType.str, 'docsIf3RccStatusRcpId'), ['str'])),
                    ('docsif3rccstatusrccstatusid', (YLeaf(YType.str, 'docsIf3RccStatusRccStatusId'), ['int'])),
                    ('docsif3rxchstatusrcid', (YLeaf(YType.uint32, 'docsIf3RxChStatusRcId'), ['int'])),
                    ('docsif3rxchstatuschifindex', (YLeaf(YType.int32, 'docsIf3RxChStatusChIfIndex'), ['int'])),
                    ('docsif3rxchstatusprimarydsindicator', (YLeaf(YType.boolean, 'docsIf3RxChStatusPrimaryDsIndicator'), ['bool'])),
                    ('docsif3rxchstatusrcrmconnectivityid', (YLeaf(YType.uint32, 'docsIf3RxChStatusRcRmConnectivityId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3rccstatusrcpid = None
                self.docsif3rccstatusrccstatusid = None
                self.docsif3rxchstatusrcid = None
                self.docsif3rxchstatuschifindex = None
                self.docsif3rxchstatusprimarydsindicator = None
                self.docsif3rxchstatusrcrmconnectivityid = None
                self._segment_path = lambda: "docsIf3RxChStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccStatusRcpId='" + str(self.docsif3rccstatusrcpid) + "']" + "[docsIf3RccStatusRccStatusId='" + str(self.docsif3rccstatusrccstatusid) + "']" + "[docsIf3RxChStatusRcId='" + str(self.docsif3rxchstatusrcid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RxChStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RxChStatusTable.DocsIf3RxChStatusEntry, ['ifindex', 'docsif3rccstatusrcpid', 'docsif3rccstatusrccstatusid', 'docsif3rxchstatusrcid', 'docsif3rxchstatuschifindex', 'docsif3rxchstatusprimarydsindicator', 'docsif3rxchstatusrcrmconnectivityid'], name, value)


    class DocsIf3RxModuleCfgTable(Entity):
        """
        The Receive Module Configuration object permits
        an operator to configure how CMs with certain Receive
        Channel Profiles (RCPs) will configure the Receive
        Modules within their profile upon CM registration.
         When a CM registers with an RCP for which all Receive
        Module Indices (RmIds) are configured in this object
        and all Receive Channels are configured within the
        Receive Channel (ReceiveChannel) object, the CMTS
        should use the configuration within these objects to
        set the Receive Channel Configuration assigned to
        the CM in a REG\-RSP message.  A CMTS may require configuration
        of all pertinent Receive Module and Receive
        Channel instances (i.e., MIB table entries) in order
        to register a CM that reports a Receive Channel Profile.
         If the CM reports multiple RCPs, and Receive Module
        and Receive Channel objects have instances (i.e.,
        MIB table entries) for more than one RCP reported by
        the CM, the particular RCP selected by the CMTS is not
        specified.  A CMTS is not restricted to assigning Receive
        Modules based only on the contents of this object.
        
        This object supports the creation and deletion of multiple
        instances.
        Creation of a new instance of this object requires the
        reference of a valid RccCfg instance.
        
        .. attribute:: docsif3rxmodulecfgentry
        
        	The conceptual row of docsIf3RxModuleCfgTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured
        	**type**\: list of  		 :py:class:`DocsIf3RxModuleCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxModuleCfgTable.DocsIf3RxModuleCfgEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RxModuleCfgTable, self).__init__()

            self.yang_name = "docsIf3RxModuleCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RxModuleCfgEntry", ("docsif3rxmodulecfgentry", DOCSIF3MIB.DocsIf3RxModuleCfgTable.DocsIf3RxModuleCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3rxmodulecfgentry = YList(self)
            self._segment_path = lambda: "docsIf3RxModuleCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RxModuleCfgTable, [], name, value)


        class DocsIf3RxModuleCfgEntry(Entity):
            """
            The conceptual row of docsIf3RxModuleCfgTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rcccfgrcpid  (key)
            
            	
            	**type**\: str
            
            	**length:** 5
            
            	**refers to**\:  :py:class:`docsif3rcccfgrcpid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry>`
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rcccfgrcccfgid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3rcccfgrcccfgid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccCfgTable.DocsIf3RccCfgEntry>`
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxmodulecfgrmid  (key)
            
            	This key represents an identifier of a Receive Module instance within the Receive Channel Profile
            	**type**\: int
            
            	**range:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxmodulecfgrmrmconnectivityid
            
            	This attribute represents the higher level (i.e., closer to RF) Receive Module to which this Receive Module connects.  If this object contains a zero value (and thus no Receive Module Connectivity), the Receive Module Connectivity TLV is omitted from the RCC. Within a single instance of the ReceiveModule object, the RmRmConnectivityId attribute cannot contain the same value as the RmId attribute.  The RmRmConnectivityId attribute points to a separate ReceiveModule object instance with the same value of RccCfgId
            	**type**\: int
            
            	**range:** 0..255
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxmodulecfgfirstcenterfrequency
            
            	This attribute represents the center frequency, in Hz, and a multiple of 62500, that indicates the lowest frequency channel of the Receive Module, or 0 if not applicable to the Receive Module
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Hz
            
            	**status**\: obsolete
            
            .. attribute:: docsif3rxmodulecfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RxModuleCfgTable.DocsIf3RxModuleCfgEntry, self).__init__()

                self.yang_name = "docsIf3RxModuleCfgEntry"
                self.yang_parent_name = "docsIf3RxModuleCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rcccfgrcpid','docsif3rcccfgrcccfgid','docsif3rxmodulecfgrmid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rcccfgrcpid', (YLeaf(YType.str, 'docsIf3RccCfgRcpId'), ['str'])),
                    ('docsif3rcccfgrcccfgid', (YLeaf(YType.str, 'docsIf3RccCfgRccCfgId'), ['int'])),
                    ('docsif3rxmodulecfgrmid', (YLeaf(YType.uint32, 'docsIf3RxModuleCfgRmId'), ['int'])),
                    ('docsif3rxmodulecfgrmrmconnectivityid', (YLeaf(YType.uint32, 'docsIf3RxModuleCfgRmRmConnectivityId'), ['int'])),
                    ('docsif3rxmodulecfgfirstcenterfrequency', (YLeaf(YType.uint32, 'docsIf3RxModuleCfgFirstCenterFrequency'), ['int'])),
                    ('docsif3rxmodulecfgrowstatus', (YLeaf(YType.enumeration, 'docsIf3RxModuleCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3rcccfgrcpid = None
                self.docsif3rcccfgrcccfgid = None
                self.docsif3rxmodulecfgrmid = None
                self.docsif3rxmodulecfgrmrmconnectivityid = None
                self.docsif3rxmodulecfgfirstcenterfrequency = None
                self.docsif3rxmodulecfgrowstatus = None
                self._segment_path = lambda: "docsIf3RxModuleCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccCfgRcpId='" + str(self.docsif3rcccfgrcpid) + "']" + "[docsIf3RccCfgRccCfgId='" + str(self.docsif3rcccfgrcccfgid) + "']" + "[docsIf3RxModuleCfgRmId='" + str(self.docsif3rxmodulecfgrmid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RxModuleCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RxModuleCfgTable.DocsIf3RxModuleCfgEntry, ['ifindex', 'docsif3rcccfgrcpid', 'docsif3rcccfgrcccfgid', 'docsif3rxmodulecfgrmid', 'docsif3rxmodulecfgrmrmconnectivityid', 'docsif3rxmodulecfgfirstcenterfrequency', 'docsif3rxmodulecfgrowstatus'], name, value)


    class DocsIf3RxModuleStatusTable(Entity):
        """
        The Receive Module Status object provides a read\-only
        view of the statically configured and dynamically
        created Receive Modules within an RCC.
        
        .. attribute:: docsif3rxmodulestatusentry
        
        	The conceptual row of docsIf3RxModuleStatusTable. The ifIndex key corresponds to the MAC Domain interface where the RCC is configured. When this object is defined on the CM, the value of RccStatusId is always 1
        	**type**\: list of  		 :py:class:`DocsIf3RxModuleStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RxModuleStatusTable.DocsIf3RxModuleStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3RxModuleStatusTable, self).__init__()

            self.yang_name = "docsIf3RxModuleStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3RxModuleStatusEntry", ("docsif3rxmodulestatusentry", DOCSIF3MIB.DocsIf3RxModuleStatusTable.DocsIf3RxModuleStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3rxmodulestatusentry = YList(self)
            self._segment_path = lambda: "docsIf3RxModuleStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3RxModuleStatusTable, [], name, value)


        class DocsIf3RxModuleStatusEntry(Entity):
            """
            The conceptual row of docsIf3RxModuleStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the RCC is configured. When this object is defined
            on the CM, the value of RccStatusId is always 1.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3rccstatusrcpid  (key)
            
            	
            	**type**\: str
            
            	**length:** 5
            
            	**refers to**\:  :py:class:`docsif3rccstatusrcpid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry>`
            
            .. attribute:: docsif3rccstatusrccstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3rccstatusrccstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3RccStatusTable.DocsIf3RccStatusEntry>`
            
            .. attribute:: docsif3rxmodulestatusrmid  (key)
            
            	This key represents an identifier of a Receive Module instance within the Receive Channel Profile
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsif3rxmodulestatusrmrmconnectivityid
            
            	This attribute represents the Receive Module to which this Receive Module connects. Requirements for module connectivity are detailed in the RmRmConnectivityId of the RccCfg object. A value of zero indicates that the Receive Module TLV is omitted from the RCC
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsif3rxmodulestatusfirstcenterfrequency
            
            	This attribute represents the low frequency channel of the Receive Module, or 0 if not applicable to the Receive Module
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Hz
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3RxModuleStatusTable.DocsIf3RxModuleStatusEntry, self).__init__()

                self.yang_name = "docsIf3RxModuleStatusEntry"
                self.yang_parent_name = "docsIf3RxModuleStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3rccstatusrcpid','docsif3rccstatusrccstatusid','docsif3rxmodulestatusrmid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3rccstatusrcpid', (YLeaf(YType.str, 'docsIf3RccStatusRcpId'), ['str'])),
                    ('docsif3rccstatusrccstatusid', (YLeaf(YType.str, 'docsIf3RccStatusRccStatusId'), ['int'])),
                    ('docsif3rxmodulestatusrmid', (YLeaf(YType.uint32, 'docsIf3RxModuleStatusRmId'), ['int'])),
                    ('docsif3rxmodulestatusrmrmconnectivityid', (YLeaf(YType.uint32, 'docsIf3RxModuleStatusRmRmConnectivityId'), ['int'])),
                    ('docsif3rxmodulestatusfirstcenterfrequency', (YLeaf(YType.uint32, 'docsIf3RxModuleStatusFirstCenterFrequency'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3rccstatusrcpid = None
                self.docsif3rccstatusrccstatusid = None
                self.docsif3rxmodulestatusrmid = None
                self.docsif3rxmodulestatusrmrmconnectivityid = None
                self.docsif3rxmodulestatusfirstcenterfrequency = None
                self._segment_path = lambda: "docsIf3RxModuleStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3RccStatusRcpId='" + str(self.docsif3rccstatusrcpid) + "']" + "[docsIf3RccStatusRccStatusId='" + str(self.docsif3rccstatusrccstatusid) + "']" + "[docsIf3RxModuleStatusRmId='" + str(self.docsif3rxmodulestatusrmid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3RxModuleStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3RxModuleStatusTable.DocsIf3RxModuleStatusEntry, ['ifindex', 'docsif3rccstatusrcpid', 'docsif3rccstatusrccstatusid', 'docsif3rxmodulestatusrmid', 'docsif3rxmodulestatusrmrmconnectivityid', 'docsif3rxmodulestatusfirstcenterfrequency'], name, value)


    class DocsIf3MdNodeStatusTable(Entity):
        """
        This object reports the MD\-DS\-SG\-ID and MD\-US\-SG\-ID
        associated with a MD\-CM\-SG\-ID within a MAC Domain
        and the Fiber Nodes reached by the MD\-CM\-SG.
        
        .. attribute:: docsif3mdnodestatusentry
        
        	The conceptual row of docsIf3MdNodeStatusTable. The ifIndex key corresponds to the MAC Domain interface where the MD\-CM\-SG\-ID is configured
        	**type**\: list of  		 :py:class:`DocsIf3MdNodeStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdNodeStatusTable.DocsIf3MdNodeStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdNodeStatusTable, self).__init__()

            self.yang_name = "docsIf3MdNodeStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdNodeStatusEntry", ("docsif3mdnodestatusentry", DOCSIF3MIB.DocsIf3MdNodeStatusTable.DocsIf3MdNodeStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3mdnodestatusentry = YList(self)
            self._segment_path = lambda: "docsIf3MdNodeStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdNodeStatusTable, [], name, value)


        class DocsIf3MdNodeStatusEntry(Entity):
            """
            The conceptual row of docsIf3MdNodeStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the MD\-CM\-SG\-ID is configured.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3mdnodestatusnodename  (key)
            
            	This key represents the name of a fiber node associated with a MD\-CM\-SG of a MAC Domain
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: docsif3mdnodestatusmdcmsgid  (key)
            
            	This attribute is a key and indicates the MD\-CM\-SG\-ID of this instance. A particular MdCmSgId in a MAC Domain is associated with one or more Fiber Nodes
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsif3mdnodestatusmddssgid
            
            	This attribute corresponds to the MD\-DS\-SG\-ID of the MD\-CM\-SG of this object instance. The MdDsSgId values are unique within a MAC Domain
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsif3mdnodestatusmdussgid
            
            	This attribute corresponds to the MD\-US\-SG\-ID of the MD\-CM\-SG of this object instance. The MdUsSgId values are unique within a MAC Domain
            	**type**\: int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdNodeStatusTable.DocsIf3MdNodeStatusEntry, self).__init__()

                self.yang_name = "docsIf3MdNodeStatusEntry"
                self.yang_parent_name = "docsIf3MdNodeStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3mdnodestatusnodename','docsif3mdnodestatusmdcmsgid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3mdnodestatusnodename', (YLeaf(YType.str, 'docsIf3MdNodeStatusNodeName'), ['str'])),
                    ('docsif3mdnodestatusmdcmsgid', (YLeaf(YType.uint32, 'docsIf3MdNodeStatusMdCmSgId'), ['int'])),
                    ('docsif3mdnodestatusmddssgid', (YLeaf(YType.uint32, 'docsIf3MdNodeStatusMdDsSgId'), ['int'])),
                    ('docsif3mdnodestatusmdussgid', (YLeaf(YType.uint32, 'docsIf3MdNodeStatusMdUsSgId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3mdnodestatusnodename = None
                self.docsif3mdnodestatusmdcmsgid = None
                self.docsif3mdnodestatusmddssgid = None
                self.docsif3mdnodestatusmdussgid = None
                self._segment_path = lambda: "docsIf3MdNodeStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3MdNodeStatusNodeName='" + str(self.docsif3mdnodestatusnodename) + "']" + "[docsIf3MdNodeStatusMdCmSgId='" + str(self.docsif3mdnodestatusmdcmsgid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdNodeStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdNodeStatusTable.DocsIf3MdNodeStatusEntry, ['ifindex', 'docsif3mdnodestatusnodename', 'docsif3mdnodestatusmdcmsgid', 'docsif3mdnodestatusmddssgid', 'docsif3mdnodestatusmdussgid'], name, value)


    class DocsIf3MdDsSgStatusTable(Entity):
        """
        This object returns the list of downstream channel
        associated with a MAC Domain MD\-DS\-SG\-ID.
        
        .. attribute:: docsif3mddssgstatusentry
        
        	The conceptual row of docsIf3MdDsSgStatusTable. The ifIndex key corresponds to the MAC Domain interface where the MD\-DS\-SG\-ID is configured. The CMTS is not required to persist instances of this object across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3MdDsSgStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdDsSgStatusTable.DocsIf3MdDsSgStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdDsSgStatusTable, self).__init__()

            self.yang_name = "docsIf3MdDsSgStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdDsSgStatusEntry", ("docsif3mddssgstatusentry", DOCSIF3MIB.DocsIf3MdDsSgStatusTable.DocsIf3MdDsSgStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3mddssgstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3MdDsSgStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdDsSgStatusTable, [], name, value)


        class DocsIf3MdDsSgStatusEntry(Entity):
            """
            The conceptual row of docsIf3MdDsSgStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the MD\-DS\-SG\-ID is configured.
            The CMTS is not required to persist instances of this
            object across reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3mddssgstatusmddssgid  (key)
            
            	This key represents a MD\-DS\-SG\-ID in a Mac Domain
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsif3mddssgstatuschsetid
            
            	This attribute represents a reference to the list of downstream channels of the MD\-DS\-SG\-ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdDsSgStatusTable.DocsIf3MdDsSgStatusEntry, self).__init__()

                self.yang_name = "docsIf3MdDsSgStatusEntry"
                self.yang_parent_name = "docsIf3MdDsSgStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3mddssgstatusmddssgid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3mddssgstatusmddssgid', (YLeaf(YType.uint32, 'docsIf3MdDsSgStatusMdDsSgId'), ['int'])),
                    ('docsif3mddssgstatuschsetid', (YLeaf(YType.uint32, 'docsIf3MdDsSgStatusChSetId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3mddssgstatusmddssgid = None
                self.docsif3mddssgstatuschsetid = None
                self._segment_path = lambda: "docsIf3MdDsSgStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3MdDsSgStatusMdDsSgId='" + str(self.docsif3mddssgstatusmddssgid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdDsSgStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdDsSgStatusTable.DocsIf3MdDsSgStatusEntry, ['ifindex', 'docsif3mddssgstatusmddssgid', 'docsif3mddssgstatuschsetid'], name, value)


    class DocsIf3MdUsSgStatusTable(Entity):
        """
        This object returns the list of upstream channels
        associated with a MAC Domain MD\-US\-SG\-ID.
        
        .. attribute:: docsif3mdussgstatusentry
        
        	The conceptual row of docsIf3MdUsSgStatusTable. The ifIndex key corresponds to the MAC Domain interface where the MD\-DS\-SG\-ID is configured. The CMTS is not required to persist instances of this object across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3MdUsSgStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdUsSgStatusTable.DocsIf3MdUsSgStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdUsSgStatusTable, self).__init__()

            self.yang_name = "docsIf3MdUsSgStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdUsSgStatusEntry", ("docsif3mdussgstatusentry", DOCSIF3MIB.DocsIf3MdUsSgStatusTable.DocsIf3MdUsSgStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3mdussgstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3MdUsSgStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdUsSgStatusTable, [], name, value)


        class DocsIf3MdUsSgStatusEntry(Entity):
            """
            The conceptual row of docsIf3MdUsSgStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the MD\-DS\-SG\-ID is configured.
            The CMTS is not required to persist instances of this
            object across reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3mdussgstatusmdussgid  (key)
            
            	This key represents a MD\-US\-SG\-ID in a Mac Domain
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsif3mdussgstatuschsetid
            
            	This attribute represents a reference to the list of upstream channels of the MD\-US\-SG\-ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdUsSgStatusTable.DocsIf3MdUsSgStatusEntry, self).__init__()

                self.yang_name = "docsIf3MdUsSgStatusEntry"
                self.yang_parent_name = "docsIf3MdUsSgStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3mdussgstatusmdussgid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3mdussgstatusmdussgid', (YLeaf(YType.uint32, 'docsIf3MdUsSgStatusMdUsSgId'), ['int'])),
                    ('docsif3mdussgstatuschsetid', (YLeaf(YType.uint32, 'docsIf3MdUsSgStatusChSetId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3mdussgstatusmdussgid = None
                self.docsif3mdussgstatuschsetid = None
                self._segment_path = lambda: "docsIf3MdUsSgStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3MdUsSgStatusMdUsSgId='" + str(self.docsif3mdussgstatusmdussgid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdUsSgStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdUsSgStatusTable.DocsIf3MdUsSgStatusEntry, ['ifindex', 'docsif3mdussgstatusmdussgid', 'docsif3mdussgstatuschsetid'], name, value)


    class DocsIf3MdUsToDsChMappingTable(Entity):
        """
        This object returns the set of downstream channels
        that carry UCDs and MAPs for a particular upstream channel
        in a MAC Domain.
        
        .. attribute:: docsif3mdustodschmappingentry
        
        	The conceptual row of docsIf3MdUsToDsChMappingTable
        	**type**\: list of  		 :py:class:`DocsIf3MdUsToDsChMappingEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable.DocsIf3MdUsToDsChMappingEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable, self).__init__()

            self.yang_name = "docsIf3MdUsToDsChMappingTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdUsToDsChMappingEntry", ("docsif3mdustodschmappingentry", DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable.DocsIf3MdUsToDsChMappingEntry))])
            self._leafs = OrderedDict()

            self.docsif3mdustodschmappingentry = YList(self)
            self._segment_path = lambda: "docsIf3MdUsToDsChMappingTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable, [], name, value)


        class DocsIf3MdUsToDsChMappingEntry(Entity):
            """
            The conceptual row of docsIf3MdUsToDsChMappingTable.
            
            .. attribute:: docsif3mdustodschmappingusifindex  (key)
            
            	This key represents the interface index of the upstream channel to which this instance applies
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsif3mdustodschmappingdsifindex  (key)
            
            	This key represents the interface index of a downstream channel carrying in UCDs and Maps associated with the upstream channel defined by this instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsif3mdustodschmappingmdifindex  (key)
            
            	This key represents the MAC domain of the upstream and downstream channels of this instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable.DocsIf3MdUsToDsChMappingEntry, self).__init__()

                self.yang_name = "docsIf3MdUsToDsChMappingEntry"
                self.yang_parent_name = "docsIf3MdUsToDsChMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3mdustodschmappingusifindex','docsif3mdustodschmappingdsifindex','docsif3mdustodschmappingmdifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3mdustodschmappingusifindex', (YLeaf(YType.int32, 'docsIf3MdUsToDsChMappingUsIfIndex'), ['int'])),
                    ('docsif3mdustodschmappingdsifindex', (YLeaf(YType.int32, 'docsIf3MdUsToDsChMappingDsIfIndex'), ['int'])),
                    ('docsif3mdustodschmappingmdifindex', (YLeaf(YType.int32, 'docsIf3MdUsToDsChMappingMdIfIndex'), ['int'])),
                ])
                self.docsif3mdustodschmappingusifindex = None
                self.docsif3mdustodschmappingdsifindex = None
                self.docsif3mdustodschmappingmdifindex = None
                self._segment_path = lambda: "docsIf3MdUsToDsChMappingEntry" + "[docsIf3MdUsToDsChMappingUsIfIndex='" + str(self.docsif3mdustodschmappingusifindex) + "']" + "[docsIf3MdUsToDsChMappingDsIfIndex='" + str(self.docsif3mdustodschmappingdsifindex) + "']" + "[docsIf3MdUsToDsChMappingMdIfIndex='" + str(self.docsif3mdustodschmappingmdifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdUsToDsChMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdUsToDsChMappingTable.DocsIf3MdUsToDsChMappingEntry, ['docsif3mdustodschmappingusifindex', 'docsif3mdustodschmappingdsifindex', 'docsif3mdustodschmappingmdifindex'], name, value)


    class DocsIf3MdCfgTable(Entity):
        """
        This object contains MAC domain level control and
        configuration attributes.
        
        .. attribute:: docsif3mdcfgentry
        
        	The conceptual row of docsIf3MdCfgTable. The CMTS persists all instances of MdCfg across reinitializations. The ifIndex key corresponds to the MAC Domain interface
        	**type**\: list of  		 :py:class:`DocsIf3MdCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3MdCfgTable, self).__init__()

            self.yang_name = "docsIf3MdCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3MdCfgEntry", ("docsif3mdcfgentry", DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3mdcfgentry = YList(self)
            self._segment_path = lambda: "docsIf3MdCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3MdCfgTable, [], name, value)


        class DocsIf3MdCfgEntry(Entity):
            """
            The conceptual row of docsIf3MdCfgTable.
            The CMTS persists all instances of MdCfg across
            reinitializations.
            The ifIndex key corresponds to the MAC Domain interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3mdcfgmddinterval
            
            	This attribute configures the interval for the insertion of MDD messages in each downstream channel of a MAC Domain
            	**type**\: int
            
            	**range:** 1..2000
            
            	**units**\: milliseconds
            
            .. attribute:: docsif3mdcfgipprovmode
            
            	This attribute configures the CMTS IP provisioning mode for a MAC Domain.  When this attribute is set to 'ipv4Only' the CM will acquire a single IPv4 address for the CM management stack. When this attribute is set to 'ipv6Only' the CM will acquire a single IPv6 address for the CM management stack. When this attribute is set to 'alternate' the CM will acquire a single IPv6 address for the CM management stack and, if failures occur, the CM will fall back to provision and operation with an IPv4 address. When this attribute is set to 'dualStack' the CM will acquire both an IPv6 and IPv4 address for provisioning and operation
            	**type**\:  :py:class:`DocsIf3MdCfgIpProvMode <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgIpProvMode>`
            
            .. attribute:: docsif3mdcfgcmstatusevctlenabled
            
            	If set to 'true', this attribute enables the signaling of the CM\-Status Event reporting mechanism
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgusfreqrange
            
            	This attribute indicates in MDD messages the upstream frequency upper band edge of an upstream Channel.  A value 'standard' means Standard Frequency Range and a value 'extended' means Extended Frequency Range
            	**type**\:  :py:class:`DocsIf3MdCfgUsFreqRange <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgUsFreqRange>`
            
            .. attribute:: docsif3mdcfgmcastdsidfwdenabled
            
            	If set to 'true', this attribute enables the CMTS to use IP Multicast DSID Forwarding (MDF) for the MAC domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgmultrxchmodeenabled
            
            	If set to 'true', this attribute enables Downstream Channel Bonding for the MAC Domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgmulttxchmodeenabled
            
            	If set to 'true', this attribute enables Multiple Transmit Channel (MTC) Mode for the MAC Domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgearlyauthencrctrl
            
            	This attribute enables or disables early authentication and encryption (EAE) signaling for the MAC Domain. It also defines the type of EAE enforcement in the case that EAE is enabled. If set to 'disableEAE', EAE is disabled for the MAC Domain.  If set to 'enableEaeRangingBasedEnforcement', 'enableEaeCapabilityBasedEnforcement' or 'enableEaeTotalEnforcement', EAE is enabled for the MAC Domain.  The following EAE enforcement methods are defined in the case where EAE signaling is enabled\: The option 'enableEaeRangingBasedEnforcement' indicates EAE is enforced on CMs that perform ranging with a B\-INIT\-RNG\-REQ message. The option 'enableEaeCapabilityBasedEnforcement' indicates EAE is enforced on CMs that perform ranging with a B\-INIT\-RNG\-REQ message in which the EAE capability flag is set. The option 'enableEaeTotalEnforcement' indicates EAE is enforced on all CMs regardless of their EAE capabilities
            	**type**\:  :py:class:`DocsIf3MdCfgEarlyAuthEncrCtrl <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgEarlyAuthEncrCtrl>`
            
            .. attribute:: docsif3mdcfgtftpproxyenabled
            
            	If set to 'true', this attribute enables TFTP Proxy functionality for the MAC Domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgsrcaddrverifenabled
            
            	If set to 'true', this attribute enables Source Address Verification (SAV) functionality for the MAC Domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgdownchannelannex
            
            	This attribute defines the ITU\-J\-83 Annex being used  for this MAC Domain.  The value of this attribute  indicates the conformance of the implementation to  important regional cable standards.   Valid enumerations for the attribute are\: unknown other annexA \: Annex A from ITU\-J83 is used. annexB \: Annex B from ITU\-J83 is used. annexC \: Annex C from ITU\-J83 is used.  Values 6\-255 are reserved
            	**type**\:  :py:class:`DocsIf3MdCfgDownChannelAnnex <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgDownChannelAnnex>`
            
            .. attribute:: docsif3mdcfgcmudcenabled
            
            	If set to 'true', this attribute instructs the CMTS MAC  Domain to enable Upstream Drop Classifiers (UDC) for the  CMs attempting registration in this MAC Domain
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgsendudcrulesenabled
            
            	If set to 'true' and when the CM signals to the CMTS 'Upstream Drop Classifier Group ID' encodings, this attribute instructs the CMTS MAC Domain to send the Subscriber  Management Filters rules associated with the 'Upstream Drop Classifier Group ID' encodings to the CM in the form of UDCs  when the following conditions occurs\: \- The attribute CmUdcEnabled value for this MAC Domain    is set to 'true', and  \- The CM has the UDC capability advertised as supported.  If there is no a single Subscriber Management Filter  configured in the CMTS for the CM's signaled UDC Group ID, the CMTS does not send UDC encodings to the CM.  It is vendor specific whether the CMTS maintains enforcement of the CM signaled or default Subscriber Management Filter  groups in the upstream direction
            	**type**\: bool
            
            .. attribute:: docsif3mdcfgservicetypeidlist
            
            	This attribute indicates the list of Service Type IDs  associated with the MAC Domain.  During the CM registration process the CMTS will attempt to redirect the CM to a MAC Domain where the CM' Service Type TLV is contained in this attribute
            	**type**\: str
            
            .. attribute:: docsif3mdcfgbpi2enforcectrl
            
            	This attribute indicates the level of BPI+ enforcement policies with the MAC Domain.  The following BPI+ enforcement policies are defined in the case where BPI+ is enabled\:  The option 'disable' indicates the CMTS does not enforce BPI+.  The option 'qosCfgFileWithBpi2AndCapabPrivSupportEnabled'  indicates the CMTS enforces BPI+ on CMs that register with a  DOCSIS 1.1 style configuration file with parameters indicating BPI+ is enabled (missing TLV 29 or containing TLV 29 set to  enable) and with a Modem Capabilities Privacy Support TLV (5.6)  set to BPI+ support.  The option 'qosCfgFileWithBpi2Enabled' indicates the CMTS  enforces BPI+ on CMs that register with a DOCSIS 1.1 style  configuration file with parameters indicating BPI+ is enabled  (missing TLV 29 or containing TLV 29 set to enable).  The option 'qosCfgFile' indicates the CMTS enforces BPI+ on CMs that register with a DOCSIS 1.1 style configuration file.  The option 'total' indicates the CMTS enforces BPI+ on all CMs
            	**type**\:  :py:class:`DocsIf3MdCfgBpi2EnforceCtrl <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgBpi2EnforceCtrl>`
            
            .. attribute:: docsif3mdcfgenergymgt1x1enabled
            
            	This attribute indicates whether the CMTS is configured for  1x1 Energy Management Mode of operation on a per MAC Domain  basis. If this attribute is set to 'true', the CMTS is  configured for 1x1 Energy Management Mode of operation on this MAC Domain. If this attribute is set to 'false', the Energy  Management 1x1 Mode of operation is disabled in the CMTS on  this MAC Domain
            	**type**\: int
            
            	**range:** 0..1
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry, self).__init__()

                self.yang_name = "docsIf3MdCfgEntry"
                self.yang_parent_name = "docsIf3MdCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3mdcfgmddinterval', (YLeaf(YType.uint32, 'docsIf3MdCfgMddInterval'), ['int'])),
                    ('docsif3mdcfgipprovmode', (YLeaf(YType.enumeration, 'docsIf3MdCfgIpProvMode'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgIpProvMode')])),
                    ('docsif3mdcfgcmstatusevctlenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgCmStatusEvCtlEnabled'), ['bool'])),
                    ('docsif3mdcfgusfreqrange', (YLeaf(YType.enumeration, 'docsIf3MdCfgUsFreqRange'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgUsFreqRange')])),
                    ('docsif3mdcfgmcastdsidfwdenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgMcastDsidFwdEnabled'), ['bool'])),
                    ('docsif3mdcfgmultrxchmodeenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgMultRxChModeEnabled'), ['bool'])),
                    ('docsif3mdcfgmulttxchmodeenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgMultTxChModeEnabled'), ['bool'])),
                    ('docsif3mdcfgearlyauthencrctrl', (YLeaf(YType.enumeration, 'docsIf3MdCfgEarlyAuthEncrCtrl'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgEarlyAuthEncrCtrl')])),
                    ('docsif3mdcfgtftpproxyenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgTftpProxyEnabled'), ['bool'])),
                    ('docsif3mdcfgsrcaddrverifenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgSrcAddrVerifEnabled'), ['bool'])),
                    ('docsif3mdcfgdownchannelannex', (YLeaf(YType.enumeration, 'docsIf3MdCfgDownChannelAnnex'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgDownChannelAnnex')])),
                    ('docsif3mdcfgcmudcenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgCmUdcEnabled'), ['bool'])),
                    ('docsif3mdcfgsendudcrulesenabled', (YLeaf(YType.boolean, 'docsIf3MdCfgSendUdcRulesEnabled'), ['bool'])),
                    ('docsif3mdcfgservicetypeidlist', (YLeaf(YType.str, 'docsIf3MdCfgServiceTypeIdList'), ['str'])),
                    ('docsif3mdcfgbpi2enforcectrl', (YLeaf(YType.enumeration, 'docsIf3MdCfgBpi2EnforceCtrl'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3MdCfgTable.DocsIf3MdCfgEntry.DocsIf3MdCfgBpi2EnforceCtrl')])),
                    ('docsif3mdcfgenergymgt1x1enabled', (YLeaf(YType.int32, 'docsIf3MdCfgEnergyMgt1x1Enabled'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3mdcfgmddinterval = None
                self.docsif3mdcfgipprovmode = None
                self.docsif3mdcfgcmstatusevctlenabled = None
                self.docsif3mdcfgusfreqrange = None
                self.docsif3mdcfgmcastdsidfwdenabled = None
                self.docsif3mdcfgmultrxchmodeenabled = None
                self.docsif3mdcfgmulttxchmodeenabled = None
                self.docsif3mdcfgearlyauthencrctrl = None
                self.docsif3mdcfgtftpproxyenabled = None
                self.docsif3mdcfgsrcaddrverifenabled = None
                self.docsif3mdcfgdownchannelannex = None
                self.docsif3mdcfgcmudcenabled = None
                self.docsif3mdcfgsendudcrulesenabled = None
                self.docsif3mdcfgservicetypeidlist = None
                self.docsif3mdcfgbpi2enforcectrl = None
                self.docsif3mdcfgenergymgt1x1enabled = None
                self._segment_path = lambda: "docsIf3MdCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3MdCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3MdCfgTable.DocsIf3MdCfgEntry, ['ifindex', 'docsif3mdcfgmddinterval', 'docsif3mdcfgipprovmode', 'docsif3mdcfgcmstatusevctlenabled', 'docsif3mdcfgusfreqrange', 'docsif3mdcfgmcastdsidfwdenabled', 'docsif3mdcfgmultrxchmodeenabled', 'docsif3mdcfgmulttxchmodeenabled', 'docsif3mdcfgearlyauthencrctrl', 'docsif3mdcfgtftpproxyenabled', 'docsif3mdcfgsrcaddrverifenabled', 'docsif3mdcfgdownchannelannex', 'docsif3mdcfgcmudcenabled', 'docsif3mdcfgsendudcrulesenabled', 'docsif3mdcfgservicetypeidlist', 'docsif3mdcfgbpi2enforcectrl', 'docsif3mdcfgenergymgt1x1enabled'], name, value)

            class DocsIf3MdCfgBpi2EnforceCtrl(Enum):
                """
                DocsIf3MdCfgBpi2EnforceCtrl (Enum Class)

                This attribute indicates the level of BPI+ enforcement

                policies with the MAC Domain.

                The following BPI+ enforcement policies are defined in

                the case where BPI+ is enabled\:

                The option 'disable' indicates the CMTS does not enforce BPI+.

                The option 'qosCfgFileWithBpi2AndCapabPrivSupportEnabled' 

                indicates the CMTS enforces BPI+ on CMs that register with a 

                DOCSIS 1.1 style configuration file with parameters indicating

                BPI+ is enabled (missing TLV 29 or containing TLV 29 set to 

                enable) and with a Modem Capabilities Privacy Support TLV (5.6) 

                set to BPI+ support.

                The option 'qosCfgFileWithBpi2Enabled' indicates the CMTS 

                enforces BPI+ on CMs that register with a DOCSIS 1.1 style 

                configuration file with parameters indicating BPI+ is enabled 

                (missing TLV 29 or containing TLV 29 set to enable).

                The option 'qosCfgFile' indicates the CMTS enforces BPI+ on CMs

                that register with a DOCSIS 1.1 style configuration file.

                The option 'total' indicates the CMTS enforces BPI+ on all CMs.

                .. data:: disable = 0

                .. data:: qosCfgFileWithBpi2AndCapabPrivSupportEnabled = 1

                .. data:: qosCfgFileWithBpi2Enabled = 2

                .. data:: qosCfgFile = 3

                .. data:: total = 4

                """

                disable = Enum.YLeaf(0, "disable")

                qosCfgFileWithBpi2AndCapabPrivSupportEnabled = Enum.YLeaf(1, "qosCfgFileWithBpi2AndCapabPrivSupportEnabled")

                qosCfgFileWithBpi2Enabled = Enum.YLeaf(2, "qosCfgFileWithBpi2Enabled")

                qosCfgFile = Enum.YLeaf(3, "qosCfgFile")

                total = Enum.YLeaf(4, "total")


            class DocsIf3MdCfgDownChannelAnnex(Enum):
                """
                DocsIf3MdCfgDownChannelAnnex (Enum Class)

                This attribute defines the ITU\-J\-83 Annex being used 

                for this MAC Domain.  The value of this attribute 

                indicates the conformance of the implementation to 

                important regional cable standards.  

                Valid enumerations for the attribute are\:

                unknown

                other

                annexA \: Annex A from ITU\-J83 is used.

                annexB \: Annex B from ITU\-J83 is used.

                annexC \: Annex C from ITU\-J83 is used. 

                Values 6\-255 are reserved.

                .. data:: unknown = 1

                .. data:: other = 2

                .. data:: annexA = 3

                .. data:: annexB = 4

                .. data:: annexC = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                other = Enum.YLeaf(2, "other")

                annexA = Enum.YLeaf(3, "annexA")

                annexB = Enum.YLeaf(4, "annexB")

                annexC = Enum.YLeaf(5, "annexC")


            class DocsIf3MdCfgEarlyAuthEncrCtrl(Enum):
                """
                DocsIf3MdCfgEarlyAuthEncrCtrl (Enum Class)

                This attribute enables or disables early authentication

                and encryption (EAE) signaling for the MAC Domain.

                It also defines the type of EAE enforcement in

                the case that EAE is enabled.

                If set to 'disableEAE', EAE is disabled for the MAC Domain.

                If set to 'enableEaeRangingBasedEnforcement',

                'enableEaeCapabilityBasedEnforcement'

                or 'enableEaeTotalEnforcement',

                EAE is enabled for the MAC Domain.

                The following EAE enforcement methods are defined in

                the case where EAE signaling is enabled\:

                The option 'enableEaeRangingBasedEnforcement' indicates

                EAE is enforced on CMs that perform ranging

                with a B\-INIT\-RNG\-REQ message.

                The option 'enableEaeCapabilityBasedEnforcement'

                indicates EAE is enforced on CMs that perform ranging

                with a B\-INIT\-RNG\-REQ message in which the EAE capability

                flag is set.

                The option 'enableEaeTotalEnforcement' indicates

                EAE is enforced on all CMs regardless of their EAE

                capabilities.

                .. data:: disableEae = 1

                .. data:: enableEaeRangingBasedEnforcement = 2

                .. data:: enableEaeCapabilityBasedEnforcement = 3

                .. data:: enableEaeTotalEnforcement = 4

                """

                disableEae = Enum.YLeaf(1, "disableEae")

                enableEaeRangingBasedEnforcement = Enum.YLeaf(2, "enableEaeRangingBasedEnforcement")

                enableEaeCapabilityBasedEnforcement = Enum.YLeaf(3, "enableEaeCapabilityBasedEnforcement")

                enableEaeTotalEnforcement = Enum.YLeaf(4, "enableEaeTotalEnforcement")


            class DocsIf3MdCfgIpProvMode(Enum):
                """
                DocsIf3MdCfgIpProvMode (Enum Class)

                This attribute configures the CMTS IP provisioning

                mode for a MAC Domain. 

                When this attribute is set to 'ipv4Only' the CM will acquire

                a single IPv4 address for the CM management stack.

                When this attribute is set to 'ipv6Only' the CM will acquire

                a single IPv6 address for the CM management stack.

                When this attribute is set to 'alternate' the CM will acquire a

                single IPv6 address for the CM management stack and, if failures

                occur, the CM will fall back to provision and operation with

                an IPv4 address.

                When this attribute is set to 'dualStack' the CM will acquire both

                an IPv6 and IPv4 address for provisioning and operation.

                .. data:: ipv4Only = 0

                .. data:: ipv6Only = 1

                .. data:: alternate = 2

                .. data:: dualStack = 3

                """

                ipv4Only = Enum.YLeaf(0, "ipv4Only")

                ipv6Only = Enum.YLeaf(1, "ipv6Only")

                alternate = Enum.YLeaf(2, "alternate")

                dualStack = Enum.YLeaf(3, "dualStack")


            class DocsIf3MdCfgUsFreqRange(Enum):
                """
                DocsIf3MdCfgUsFreqRange (Enum Class)

                This attribute indicates in MDD messages the upstream

                frequency upper band edge of an upstream Channel.

                A value 'standard' means Standard Frequency Range and

                a value 'extended' means Extended Frequency Range.

                .. data:: standard = 0

                .. data:: extended = 1

                """

                standard = Enum.YLeaf(0, "standard")

                extended = Enum.YLeaf(1, "extended")



    class DocsIf3BondingGrpCfgTable(Entity):
        """
        This object defines statically configured Downstream
        Bonding Groups and Upstream Bonding Groups on
        the CMTS.
        This object supports the creation and deletion of multiple
        instances.
        Creation of a new instance of this object requires the
        ChList attribute to be set.
        
        .. attribute:: docsif3bondinggrpcfgentry
        
        	The conceptual row of docsIf3BondingGrpCfgTable. The ifIndex key corresponds to the MAC Domain interface where the Bonding Group is configured. The CMTS persists all instances of BondingGrpCfg across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3BondingGrpCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3BondingGrpCfgTable.DocsIf3BondingGrpCfgEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3BondingGrpCfgTable, self).__init__()

            self.yang_name = "docsIf3BondingGrpCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3BondingGrpCfgEntry", ("docsif3bondinggrpcfgentry", DOCSIF3MIB.DocsIf3BondingGrpCfgTable.DocsIf3BondingGrpCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3bondinggrpcfgentry = YList(self)
            self._segment_path = lambda: "docsIf3BondingGrpCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3BondingGrpCfgTable, [], name, value)


        class DocsIf3BondingGrpCfgEntry(Entity):
            """
            The conceptual row of docsIf3BondingGrpCfgTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the Bonding Group is configured.
            The CMTS persists all instances of BondingGrpCfg
            across reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3bondinggrpcfgdir  (key)
            
            	This attribute defines the ordered list of channels that comprise the channel set
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.IfDirection>`
            
            .. attribute:: docsif3bondinggrpcfgcfgid  (key)
            
            	This key represents the configured bonding group identifier in the indicated direction for the MAC Domain. This attribute is used for the sole purpose of tracking bonding groups defined by management systems
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: docsif3bondinggrpcfgchlist
            
            	This attribute contains the list of channels of the bonding group
            	**type**\: str
            
            	**length:** 2..255
            
            .. attribute:: docsif3bondinggrpcfgsfprovattrmask
            
            	This attribute represents the Provisioned Attribute Mask encoding for the bonding group
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: docsif3bondinggrpcfgdsidreseqwaittime
            
            	For a Downstream Bonding Group, this attribute provides the DSID Resequencing Wait Time that is to be used for all DSIDs associated with this Downstream Bonding Group.  The value of 255 indicates that the DSID Resequencing Wait Time is determined by the CMTS. The value zero in not supported for downstream  bonding groups. For an Upstream Bonding Group, this attribute has no meaning and returns the value 0
            	**type**\: int
            
            	**range:** 0..180 \| 255..None
            
            	**units**\: hundredMicroseconds
            
            .. attribute:: docsif3bondinggrpcfgdsidreseqwarnthrshld
            
            	For a Downstream Bonding Group, this attribute provides the DSID Resequencing Warning Threshold that is to be used for all DSIDs associated with this Downstream Bonding Group. The value of 255 indicates that the DSID Resequencing Warning Threshold is determined by the CMTS.  The value of 0 indicates that the threshold warnings are disabled.  When  the value of DsidReseqWaitTime is not equal to 0 or 255, the CMTS must ensure that the value of this object is either  255 or less than the value of DsidReseqWaitTime
            	**type**\: int
            
            	**range:** 0..179 \| 255..None
            
            	**units**\: hundredMicroseconds
            
            .. attribute:: docsif3bondinggrpcfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3BondingGrpCfgTable.DocsIf3BondingGrpCfgEntry, self).__init__()

                self.yang_name = "docsIf3BondingGrpCfgEntry"
                self.yang_parent_name = "docsIf3BondingGrpCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3bondinggrpcfgdir','docsif3bondinggrpcfgcfgid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3bondinggrpcfgdir', (YLeaf(YType.enumeration, 'docsIf3BondingGrpCfgDir'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'IfDirection', '')])),
                    ('docsif3bondinggrpcfgcfgid', (YLeaf(YType.uint32, 'docsIf3BondingGrpCfgCfgId'), ['int'])),
                    ('docsif3bondinggrpcfgchlist', (YLeaf(YType.str, 'docsIf3BondingGrpCfgChList'), ['str'])),
                    ('docsif3bondinggrpcfgsfprovattrmask', (YLeaf(YType.str, 'docsIf3BondingGrpCfgSfProvAttrMask'), ['str'])),
                    ('docsif3bondinggrpcfgdsidreseqwaittime', (YLeaf(YType.uint32, 'docsIf3BondingGrpCfgDsidReseqWaitTime'), ['int'])),
                    ('docsif3bondinggrpcfgdsidreseqwarnthrshld', (YLeaf(YType.uint32, 'docsIf3BondingGrpCfgDsidReseqWarnThrshld'), ['int'])),
                    ('docsif3bondinggrpcfgrowstatus', (YLeaf(YType.enumeration, 'docsIf3BondingGrpCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3bondinggrpcfgdir = None
                self.docsif3bondinggrpcfgcfgid = None
                self.docsif3bondinggrpcfgchlist = None
                self.docsif3bondinggrpcfgsfprovattrmask = None
                self.docsif3bondinggrpcfgdsidreseqwaittime = None
                self.docsif3bondinggrpcfgdsidreseqwarnthrshld = None
                self.docsif3bondinggrpcfgrowstatus = None
                self._segment_path = lambda: "docsIf3BondingGrpCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3BondingGrpCfgDir='" + str(self.docsif3bondinggrpcfgdir) + "']" + "[docsIf3BondingGrpCfgCfgId='" + str(self.docsif3bondinggrpcfgcfgid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3BondingGrpCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3BondingGrpCfgTable.DocsIf3BondingGrpCfgEntry, ['ifindex', 'docsif3bondinggrpcfgdir', 'docsif3bondinggrpcfgcfgid', 'docsif3bondinggrpcfgchlist', 'docsif3bondinggrpcfgsfprovattrmask', 'docsif3bondinggrpcfgdsidreseqwaittime', 'docsif3bondinggrpcfgdsidreseqwarnthrshld', 'docsif3bondinggrpcfgrowstatus'], name, value)


    class DocsIf3DsBondingGrpStatusTable(Entity):
        """
        This object returns administratively\-configured
        and CMTS defined downstream bonding groups.
        
        .. attribute:: docsif3dsbondinggrpstatusentry
        
        	The conceptual row of docsIf3DsBondingGrpStatusTable. The ifIndex key corresponds to the MAC Domain interface where the Bonding Group is configured
        	**type**\: list of  		 :py:class:`DocsIf3DsBondingGrpStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable.DocsIf3DsBondingGrpStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable, self).__init__()

            self.yang_name = "docsIf3DsBondingGrpStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3DsBondingGrpStatusEntry", ("docsif3dsbondinggrpstatusentry", DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable.DocsIf3DsBondingGrpStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3dsbondinggrpstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3DsBondingGrpStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable, [], name, value)


        class DocsIf3DsBondingGrpStatusEntry(Entity):
            """
            The conceptual row of docsIf3DsBondingGrpStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the Bonding Group is configured.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3dsbondinggrpstatuschsetid  (key)
            
            	This key represents the identifier for the Downstream Bonding Group or the single\-downstream channel of this instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3dsbondinggrpstatusmddssgid
            
            	This attribute corresponds to the MD\-DS\-SG\-ID that includes all the downstream channels of the Downstream Bonding Group. The value zero indicates that the bonding group does not contain channels from a single MD\-DS\-SG and therefore the bonding group is not valid and usable
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsif3dsbondinggrpstatuscfgid
            
            	This attribute provides the BondingGrpCfgId for the downstream bonding group if it was configured. Otherwise, the zero value indicates that the CMTS will define the bonding group
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable.DocsIf3DsBondingGrpStatusEntry, self).__init__()

                self.yang_name = "docsIf3DsBondingGrpStatusEntry"
                self.yang_parent_name = "docsIf3DsBondingGrpStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3dsbondinggrpstatuschsetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3dsbondinggrpstatuschsetid', (YLeaf(YType.uint32, 'docsIf3DsBondingGrpStatusChSetId'), ['int'])),
                    ('docsif3dsbondinggrpstatusmddssgid', (YLeaf(YType.uint32, 'docsIf3DsBondingGrpStatusMdDsSgId'), ['int'])),
                    ('docsif3dsbondinggrpstatuscfgid', (YLeaf(YType.uint32, 'docsIf3DsBondingGrpStatusCfgId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3dsbondinggrpstatuschsetid = None
                self.docsif3dsbondinggrpstatusmddssgid = None
                self.docsif3dsbondinggrpstatuscfgid = None
                self._segment_path = lambda: "docsIf3DsBondingGrpStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3DsBondingGrpStatusChSetId='" + str(self.docsif3dsbondinggrpstatuschsetid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3DsBondingGrpStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3DsBondingGrpStatusTable.DocsIf3DsBondingGrpStatusEntry, ['ifindex', 'docsif3dsbondinggrpstatuschsetid', 'docsif3dsbondinggrpstatusmddssgid', 'docsif3dsbondinggrpstatuscfgid'], name, value)


    class DocsIf3UsBondingGrpStatusTable(Entity):
        """
        This object returns administratively\-configured
        and CMTS\-defined upstream bonding groups.
        
        .. attribute:: docsif3usbondinggrpstatusentry
        
        	The conceptual row of docsIf3UsBondingGrpStatusTable. The ifIndex key corresponds to the MAC Domain interface where the Bonding Group is configured
        	**type**\: list of  		 :py:class:`DocsIf3UsBondingGrpStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable.DocsIf3UsBondingGrpStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable, self).__init__()

            self.yang_name = "docsIf3UsBondingGrpStatusTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3UsBondingGrpStatusEntry", ("docsif3usbondinggrpstatusentry", DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable.DocsIf3UsBondingGrpStatusEntry))])
            self._leafs = OrderedDict()

            self.docsif3usbondinggrpstatusentry = YList(self)
            self._segment_path = lambda: "docsIf3UsBondingGrpStatusTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable, [], name, value)


        class DocsIf3UsBondingGrpStatusEntry(Entity):
            """
            The conceptual row of docsIf3UsBondingGrpStatusTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the Bonding Group is configured.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3usbondinggrpstatuschsetid  (key)
            
            	This key represents the identifier for the Upstream Bonding Group or the single\-upstream channel of this instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3usbondinggrpstatusmdussgid
            
            	This attribute corresponds to the MD\-US\-SG\-ID that includes all the upstream channels of the Upstream Bonding Group. The value zero indicates that the bonding group does not contain channels from a single MD\-US\-SG and therefore the bonding group is not valid and usable
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsif3usbondinggrpstatuscfgid
            
            	This attribute provides the BondingGrpCfgId for the upstream bonding group if it was configured. Otherwise, the zero value indicates that the CMTS defines the bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable.DocsIf3UsBondingGrpStatusEntry, self).__init__()

                self.yang_name = "docsIf3UsBondingGrpStatusEntry"
                self.yang_parent_name = "docsIf3UsBondingGrpStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3usbondinggrpstatuschsetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3usbondinggrpstatuschsetid', (YLeaf(YType.uint32, 'docsIf3UsBondingGrpStatusChSetId'), ['int'])),
                    ('docsif3usbondinggrpstatusmdussgid', (YLeaf(YType.uint32, 'docsIf3UsBondingGrpStatusMdUsSgId'), ['int'])),
                    ('docsif3usbondinggrpstatuscfgid', (YLeaf(YType.uint32, 'docsIf3UsBondingGrpStatusCfgId'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3usbondinggrpstatuschsetid = None
                self.docsif3usbondinggrpstatusmdussgid = None
                self.docsif3usbondinggrpstatuscfgid = None
                self._segment_path = lambda: "docsIf3UsBondingGrpStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3UsBondingGrpStatusChSetId='" + str(self.docsif3usbondinggrpstatuschsetid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3UsBondingGrpStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3UsBondingGrpStatusTable.DocsIf3UsBondingGrpStatusEntry, ['ifindex', 'docsif3usbondinggrpstatuschsetid', 'docsif3usbondinggrpstatusmdussgid', 'docsif3usbondinggrpstatuscfgid'], name, value)


    class DocsIf3UsChExtTable(Entity):
        """
        This object defines management extensions for upstream
        channels, in particular SCDMA parameters.
        
        .. attribute:: docsif3uschextentry
        
        	The conceptual row of docsIf3UsChExtTable. The ifIndex key corresponds to each of the upstream channels
        	**type**\: list of  		 :py:class:`DocsIf3UsChExtEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsChExtTable.DocsIf3UsChExtEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3UsChExtTable, self).__init__()

            self.yang_name = "docsIf3UsChExtTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3UsChExtEntry", ("docsif3uschextentry", DOCSIF3MIB.DocsIf3UsChExtTable.DocsIf3UsChExtEntry))])
            self._leafs = OrderedDict()

            self.docsif3uschextentry = YList(self)
            self._segment_path = lambda: "docsIf3UsChExtTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3UsChExtTable, [], name, value)


        class DocsIf3UsChExtEntry(Entity):
            """
            The conceptual row of docsIf3UsChExtTable.
            The ifIndex key corresponds to each of the upstream
            channels.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3uschextsaccodehoppingselectionmode
            
            	This attribute indicates the selection mode for active codes and code hopping. 'none'    Non\-SCDMA channel 'sac1NoCodeHopping'    Selectable active codes mode 1 and code hopping disabled  'sac1CodeHoppingMode1'    Selectable active codes mode 1 and code hopping mode 1 'sac2CodeHoppingMode2'   Selectable active codes mode 2 and code hopping mode 2 'sac2NoCodeHopping'   Selectable active codes mode 2 and code hopping disabled
            	**type**\:  :py:class:`DocsIf3UsChExtSacCodeHoppingSelectionMode <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsChExtTable.DocsIf3UsChExtEntry.DocsIf3UsChExtSacCodeHoppingSelectionMode>`
            
            .. attribute:: docsif3uschextscdmaselectionstringactivecodes
            
            	This attribute represents the active codes of the upstream channel and it is applicable only when SacCodeHoppingSelectionMode is 'sac2CodeHoppingMode2
            	**type**\: str
            
            	**length:** 0 \| 16
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3UsChExtTable.DocsIf3UsChExtEntry, self).__init__()

                self.yang_name = "docsIf3UsChExtEntry"
                self.yang_parent_name = "docsIf3UsChExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3uschextsaccodehoppingselectionmode', (YLeaf(YType.enumeration, 'docsIf3UsChExtSacCodeHoppingSelectionMode'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3UsChExtTable.DocsIf3UsChExtEntry.DocsIf3UsChExtSacCodeHoppingSelectionMode')])),
                    ('docsif3uschextscdmaselectionstringactivecodes', (YLeaf(YType.str, 'docsIf3UsChExtScdmaSelectionStringActiveCodes'), ['str'])),
                ])
                self.ifindex = None
                self.docsif3uschextsaccodehoppingselectionmode = None
                self.docsif3uschextscdmaselectionstringactivecodes = None
                self._segment_path = lambda: "docsIf3UsChExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3UsChExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3UsChExtTable.DocsIf3UsChExtEntry, ['ifindex', 'docsif3uschextsaccodehoppingselectionmode', 'docsif3uschextscdmaselectionstringactivecodes'], name, value)

            class DocsIf3UsChExtSacCodeHoppingSelectionMode(Enum):
                """
                DocsIf3UsChExtSacCodeHoppingSelectionMode (Enum Class)

                This attribute indicates the selection mode for active

                codes and code hopping.

                'none'

                   Non\-SCDMA channel

                'sac1NoCodeHopping'

                   Selectable active codes mode 1 and code hopping disabled

                'sac1CodeHoppingMode1'

                   Selectable active codes mode 1 and code hopping mode

                1

                'sac2CodeHoppingMode2'

                  Selectable active codes mode 2 and code hopping mode

                2

                'sac2NoCodeHopping'

                  Selectable active codes mode 2 and code hopping disabled.

                .. data:: none = 0

                .. data:: sac1NoCodeHopping = 1

                .. data:: sac1CodeHoppingMode1 = 2

                .. data:: sac2CodeHoppingMode2 = 3

                .. data:: sac2NoCodeHopping = 4

                """

                none = Enum.YLeaf(0, "none")

                sac1NoCodeHopping = Enum.YLeaf(1, "sac1NoCodeHopping")

                sac1CodeHoppingMode1 = Enum.YLeaf(2, "sac1CodeHoppingMode1")

                sac2CodeHoppingMode2 = Enum.YLeaf(3, "sac2CodeHoppingMode2")

                sac2NoCodeHopping = Enum.YLeaf(4, "sac2NoCodeHopping")



    class DocsIf3UsChSetTable(Entity):
        """
        This object defines a set of upstream channels. These
        channel sets may be associated with channel bonding
        groups, MD\-US\-SGs, MD\-CM\-SGs, or any other channel
        set that the CMTS may derive from other CMTS processes.
        
        .. attribute:: docsif3uschsetentry
        
        	The conceptual row of docsIf3UsChSetTable. The ifIndex key corresponds to the MAC Domain interface where the upstream channel set is defined
        	**type**\: list of  		 :py:class:`DocsIf3UsChSetEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3UsChSetTable.DocsIf3UsChSetEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3UsChSetTable, self).__init__()

            self.yang_name = "docsIf3UsChSetTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3UsChSetEntry", ("docsif3uschsetentry", DOCSIF3MIB.DocsIf3UsChSetTable.DocsIf3UsChSetEntry))])
            self._leafs = OrderedDict()

            self.docsif3uschsetentry = YList(self)
            self._segment_path = lambda: "docsIf3UsChSetTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3UsChSetTable, [], name, value)


        class DocsIf3UsChSetEntry(Entity):
            """
            The conceptual row of docsIf3UsChSetTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the upstream channel set is defined.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3uschsetid  (key)
            
            	This key defines a reference identifier for the upstream channel set within the MAC Domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3uschsetchlist
            
            	This attribute defines the ordered list of channels that comprise the upstream channel set
            	**type**\: str
            
            	**length:** 0 \| 2..255
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3UsChSetTable.DocsIf3UsChSetEntry, self).__init__()

                self.yang_name = "docsIf3UsChSetEntry"
                self.yang_parent_name = "docsIf3UsChSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3uschsetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3uschsetid', (YLeaf(YType.uint32, 'docsIf3UsChSetId'), ['int'])),
                    ('docsif3uschsetchlist', (YLeaf(YType.str, 'docsIf3UsChSetChList'), ['str'])),
                ])
                self.ifindex = None
                self.docsif3uschsetid = None
                self.docsif3uschsetchlist = None
                self._segment_path = lambda: "docsIf3UsChSetEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3UsChSetId='" + str(self.docsif3uschsetid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3UsChSetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3UsChSetTable.DocsIf3UsChSetEntry, ['ifindex', 'docsif3uschsetid', 'docsif3uschsetchlist'], name, value)


    class DocsIf3DsChSetTable(Entity):
        """
        This object defines a set of downstream channels.
        These channel sets may be associated with channel bonding
        groups, MD\-DS\-SGs, MD\-CM\-SGs, or any other channel
        set that the CMTS may derive from other CMTS processes.
        
        .. attribute:: docsif3dschsetentry
        
        	The conceptual row of docsIf3DsChSetTable. The ifIndex key corresponds to the MAC Domain interface where the downstream channel set is defined
        	**type**\: list of  		 :py:class:`DocsIf3DsChSetEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3DsChSetTable.DocsIf3DsChSetEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3DsChSetTable, self).__init__()

            self.yang_name = "docsIf3DsChSetTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3DsChSetEntry", ("docsif3dschsetentry", DOCSIF3MIB.DocsIf3DsChSetTable.DocsIf3DsChSetEntry))])
            self._leafs = OrderedDict()

            self.docsif3dschsetentry = YList(self)
            self._segment_path = lambda: "docsIf3DsChSetTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3DsChSetTable, [], name, value)


        class DocsIf3DsChSetEntry(Entity):
            """
            The conceptual row of docsIf3DsChSetTable.
            The ifIndex key corresponds to the MAC Domain interface
            where the downstream channel set is defined.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3dschsetid  (key)
            
            	This key defines a reference identifier for the downstream channel set within the MAC Domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3dschsetchlist
            
            	This attribute defines the ordered list of channels that comprise the downstream channel set
            	**type**\: str
            
            	**length:** 0 \| 2..255
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3DsChSetTable.DocsIf3DsChSetEntry, self).__init__()

                self.yang_name = "docsIf3DsChSetEntry"
                self.yang_parent_name = "docsIf3DsChSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3dschsetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3dschsetid', (YLeaf(YType.uint32, 'docsIf3DsChSetId'), ['int'])),
                    ('docsif3dschsetchlist', (YLeaf(YType.str, 'docsIf3DsChSetChList'), ['str'])),
                ])
                self.ifindex = None
                self.docsif3dschsetid = None
                self.docsif3dschsetchlist = None
                self._segment_path = lambda: "docsIf3DsChSetEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3DsChSetId='" + str(self.docsif3dschsetid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3DsChSetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3DsChSetTable.DocsIf3DsChSetEntry, ['ifindex', 'docsif3dschsetid', 'docsif3dschsetchlist'], name, value)


    class DocsIf3SignalQualityExtTable(Entity):
        """
        This object provides an in\-channel received modulation
        error ratio metric for CM and CMTS.
        
        .. attribute:: docsif3signalqualityextentry
        
        	The conceptual row of docsIf3SignalQualityExtTable. At the CM, this object describes the received modulation  error ratio of each downstream channel. At the CMTS,  it describes the received modulation error ratio of each logical upstream channel.  An entry in this table exists for each ifEntry with an ifType of docsCableDownstream(128) for Cable Modems. For Cable Modem Termination Systems, an entry exists for  each ifEntry with an ifType of docsCableUpstreamChannel(205)
        	**type**\: list of  		 :py:class:`DocsIf3SignalQualityExtEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3SignalQualityExtTable.DocsIf3SignalQualityExtEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3SignalQualityExtTable, self).__init__()

            self.yang_name = "docsIf3SignalQualityExtTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3SignalQualityExtEntry", ("docsif3signalqualityextentry", DOCSIF3MIB.DocsIf3SignalQualityExtTable.DocsIf3SignalQualityExtEntry))])
            self._leafs = OrderedDict()

            self.docsif3signalqualityextentry = YList(self)
            self._segment_path = lambda: "docsIf3SignalQualityExtTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3SignalQualityExtTable, [], name, value)


        class DocsIf3SignalQualityExtEntry(Entity):
            """
            The conceptual row of docsIf3SignalQualityExtTable.
            At the CM, this object describes the received modulation 
            error ratio of each downstream channel. At the CMTS, 
            it describes the received modulation error ratio of each
            logical upstream channel. 
            An entry in this table exists for each ifEntry with an
            ifType of docsCableDownstream(128) for Cable Modems.
            For Cable Modem Termination Systems, an entry exists for 
            each ifEntry with an ifType of docsCableUpstreamChannel(205).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3signalqualityextrxmer
            
            	RxMER provides an in\-channel received Modulation Error Ratio (MER). RxMER is defined as an estimate, provided by the demodulator, of the ratio\: (average constellation energy with equally likely symbols) / (average squared magnitude of error vector)  RxMER is measured just prior to FEC (trellis/Reed\-Solomon) decoding. RxMER includes the effects of the HFC channel as well as implementation effects of the modulator and demodulator. Error vector estimation may vary among demodulator implementations.  The CMTS RxMER is averaged over a given number of bursts at the burst receiver, which may correspond to transmissions from multiple users. In the case of S\-CDMA mode, RxMER is measured on the de\-spread signal
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: TenthdB
            
            .. attribute:: docsif3signalqualityextrxmersamples
            
            	RxMerSamples is a statistically significant number of symbols for the CM, or bursts for the CMTS, processed to arrive at the RxMER value. For the CMTS, the MER measurement includes only valid bursts that are not in contention regions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3SignalQualityExtTable.DocsIf3SignalQualityExtEntry, self).__init__()

                self.yang_name = "docsIf3SignalQualityExtEntry"
                self.yang_parent_name = "docsIf3SignalQualityExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3signalqualityextrxmer', (YLeaf(YType.int32, 'docsIf3SignalQualityExtRxMER'), ['int'])),
                    ('docsif3signalqualityextrxmersamples', (YLeaf(YType.uint32, 'docsIf3SignalQualityExtRxMerSamples'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3signalqualityextrxmer = None
                self.docsif3signalqualityextrxmersamples = None
                self._segment_path = lambda: "docsIf3SignalQualityExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3SignalQualityExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3SignalQualityExtTable.DocsIf3SignalQualityExtEntry, ['ifindex', 'docsif3signalqualityextrxmer', 'docsif3signalqualityextrxmersamples'], name, value)


    class DocsIf3CmtsSignalQualityExtTable(Entity):
        """
        This object provides metrics and parameters associated
        with received carrier, noise and interference
        power levels in the upstream channels of the CMTS.
        
        .. attribute:: docsif3cmtssignalqualityextentry
        
        	The conceptual row of docsIf3CmtsSignalQualityExtTable. The ifIndex key corresponds to each of the upstream channels. The CMTS is not required to persist the values of all  instances of CmtsSignalQualityExt across reinitialization
        	**type**\: list of  		 :py:class:`DocsIf3CmtsSignalQualityExtEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable.DocsIf3CmtsSignalQualityExtEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable, self).__init__()

            self.yang_name = "docsIf3CmtsSignalQualityExtTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsSignalQualityExtEntry", ("docsif3cmtssignalqualityextentry", DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable.DocsIf3CmtsSignalQualityExtEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtssignalqualityextentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsSignalQualityExtTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable, [], name, value)


        class DocsIf3CmtsSignalQualityExtEntry(Entity):
            """
            The conceptual row of docsIf3CmtsSignalQualityExtTable.
            The ifIndex key corresponds to each of the upstream
            channels.
            The CMTS is not required to persist the values of all 
            instances of CmtsSignalQualityExt across reinitialization.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmtssignalqualityextcnir
            
            	This attribute provides an upstream in\-channel Carrier\-to\-Noise plus Interference Ratio (CNIR). CNIR is defined as the ratio of the expected commanded received signal power at the CMTS input, assuming QPSK0 modulation, to the noise plus interference in the channel. This measurement occurs prior to the point at which  the desired CM signal, when present, is demodulated. The measurement includes the effect of the receive matched filter but does not include the effect of any ingress filtering. Both the signal power and noise/interference power are referenced to the same point, e.g., CMTS input
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: docsif3cmtssignalqualityextexpectedrxsignalpower
            
            	ExpectedReceivedSignalPower is the power of the expected commanded received signal in the channel, referenced to the CMTS input
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable.DocsIf3CmtsSignalQualityExtEntry, self).__init__()

                self.yang_name = "docsIf3CmtsSignalQualityExtEntry"
                self.yang_parent_name = "docsIf3CmtsSignalQualityExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmtssignalqualityextcnir', (YLeaf(YType.int32, 'docsIf3CmtsSignalQualityExtCNIR'), ['int'])),
                    ('docsif3cmtssignalqualityextexpectedrxsignalpower', (YLeaf(YType.int32, 'docsIf3CmtsSignalQualityExtExpectedRxSignalPower'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3cmtssignalqualityextcnir = None
                self.docsif3cmtssignalqualityextexpectedrxsignalpower = None
                self._segment_path = lambda: "docsIf3CmtsSignalQualityExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsSignalQualityExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsSignalQualityExtTable.DocsIf3CmtsSignalQualityExtEntry, ['ifindex', 'docsif3cmtssignalqualityextcnir', 'docsif3cmtssignalqualityextexpectedrxsignalpower'], name, value)


    class DocsIf3CmtsSpectrumAnalysisMeasTable(Entity):
        """
        This object is used to configure the logical upstream
        interfaces to perform the spectrum measurements.
        This object supports creation and deletion of instances.
        
        .. attribute:: docsif3cmtsspectrumanalysismeasentry
        
        	The conceptual row of docsIf3CmtsSpectrumAnalysisMeasTable. The ifIndex key corresponds to each of the upstream channels. The CMTS is not required to persist instances of this object across reinitializations
        	**type**\: list of  		 :py:class:`DocsIf3CmtsSpectrumAnalysisMeasEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable.DocsIf3CmtsSpectrumAnalysisMeasEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable, self).__init__()

            self.yang_name = "docsIf3CmtsSpectrumAnalysisMeasTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsSpectrumAnalysisMeasEntry", ("docsif3cmtsspectrumanalysismeasentry", DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable.DocsIf3CmtsSpectrumAnalysisMeasEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtsspectrumanalysismeasentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsSpectrumAnalysisMeasTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable, [], name, value)


        class DocsIf3CmtsSpectrumAnalysisMeasEntry(Entity):
            """
            The conceptual row of docsIf3CmtsSpectrumAnalysisMeasTable.
            The ifIndex key corresponds to each of the upstream
            channels.
            The CMTS is not required to persist instances of this
            object across reinitializations.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmtsspectrumanalysismeasamplitudedata
            
            	This attribute provides a list of the spectral amplitudes corresponding to the frequency bins ordered from lowest to highest frequencies covering the frequency span. Information about the center frequency, frequency span, number of bins and resolution bandwidth are included to provide context to the measurement point The CMTS must support the number of bins as an odd number in order to provide a spectrum representation that is symmetric about the middle data point or bin. The CMTS must support a number of bins greater than or equal to 257 for frequency spans greater than or equal to 6.4 MHz.  The CMTS must not exceed 25 kHz bin spacing for measurement of frequency spans less than or equal to 6.4 MHz.  The bins measurements are updated periodically at time intervals given by the TimeInterval attribute
            	**type**\: str
            
            	**length:** 0 \| 2..4116
            
            .. attribute:: docsif3cmtsspectrumanalysismeastimeinterval
            
            	TimeInterval is the CMTS estimated average repetition period of measurements. This attribute defines the average rate at which new spectra can be retrieved
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: docsif3cmtsspectrumanalysismeasrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable.DocsIf3CmtsSpectrumAnalysisMeasEntry, self).__init__()

                self.yang_name = "docsIf3CmtsSpectrumAnalysisMeasEntry"
                self.yang_parent_name = "docsIf3CmtsSpectrumAnalysisMeasTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmtsspectrumanalysismeasamplitudedata', (YLeaf(YType.str, 'docsIf3CmtsSpectrumAnalysisMeasAmplitudeData'), ['str'])),
                    ('docsif3cmtsspectrumanalysismeastimeinterval', (YLeaf(YType.uint32, 'docsIf3CmtsSpectrumAnalysisMeasTimeInterval'), ['int'])),
                    ('docsif3cmtsspectrumanalysismeasrowstatus', (YLeaf(YType.enumeration, 'docsIf3CmtsSpectrumAnalysisMeasRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsif3cmtsspectrumanalysismeasamplitudedata = None
                self.docsif3cmtsspectrumanalysismeastimeinterval = None
                self.docsif3cmtsspectrumanalysismeasrowstatus = None
                self._segment_path = lambda: "docsIf3CmtsSpectrumAnalysisMeasEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsSpectrumAnalysisMeasTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsSpectrumAnalysisMeasTable.DocsIf3CmtsSpectrumAnalysisMeasEntry, ['ifindex', 'docsif3cmtsspectrumanalysismeasamplitudedata', 'docsif3cmtsspectrumanalysismeastimeinterval', 'docsif3cmtsspectrumanalysismeasrowstatus'], name, value)


    class DocsIf3CmDpvStatsTable(Entity):
        """
        This object represents the DOCSIS Path Verify Statistics
        collected in the cable modem device.
        The CMTS controls the logging of DPV statistics in the
        cable modem. Therefore the context and nature of the
        measurements are governed by the CMTS and not self\-descriptive
        when read from the CM.
        
        .. attribute:: docsif3cmdpvstatsentry
        
        	The conceptual row of docsIf3CmDpvStatsTable
        	**type**\: list of  		 :py:class:`DocsIf3CmDpvStatsEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmDpvStatsTable.DocsIf3CmDpvStatsEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmDpvStatsTable, self).__init__()

            self.yang_name = "docsIf3CmDpvStatsTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmDpvStatsEntry", ("docsif3cmdpvstatsentry", DOCSIF3MIB.DocsIf3CmDpvStatsTable.DocsIf3CmDpvStatsEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmdpvstatsentry = YList(self)
            self._segment_path = lambda: "docsIf3CmDpvStatsTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmDpvStatsTable, [], name, value)


        class DocsIf3CmDpvStatsEntry(Entity):
            """
            The conceptual row of docsIf3CmDpvStatsTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmdpvstatsgrpid  (key)
            
            	This key represents the DPV Group ID. The CM reports two instance of DPV statistics per downstream normally referred as Statistical Group 1 and Statistical Group 2
            	**type**\: int
            
            	**range:** 1..2
            
            .. attribute:: docsif3cmdpvstatslastmeaslatency
            
            	This attribute represents the last latency measurement for this statistical group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: nanoseconds
            
            .. attribute:: docsif3cmdpvstatslastmeastime
            
            	This attribute represents the last measurement time of the last latency measurement for this statistical group. This attribute reports the EPOC time value when no measurements are being reported or after the statistics were cleared
            	**type**\: str
            
            .. attribute:: docsif3cmdpvstatsminlatency
            
            	This attribute represents the minimum latency measurement for this statistical group since the last time statistics were cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: nanoseconds
            
            .. attribute:: docsif3cmdpvstatsmaxlatency
            
            	This attribute represents the maximum latency measurement for this statistical group since the last time statistics were cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: nanoseconds
            
            .. attribute:: docsif3cmdpvstatsavglatency
            
            	This attribute represents the average latency measurement for this statistical group since the last time statistics were cleared. The averaging mechanism is controlled by the CMTS, and can be a simple average (mean) or an exponential moving average
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: nanoseconds
            
            .. attribute:: docsif3cmdpvstatsnummeas
            
            	This attribute represents the number of latency measurements made for this statistical group since the last time statistics were cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: measurements
            
            .. attribute:: docsif3cmdpvstatslastcleartime
            
            	This attribute represents the last time statistics were cleared for this statistical group
            	**type**\: str
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmDpvStatsTable.DocsIf3CmDpvStatsEntry, self).__init__()

                self.yang_name = "docsIf3CmDpvStatsEntry"
                self.yang_parent_name = "docsIf3CmDpvStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsif3cmdpvstatsgrpid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmdpvstatsgrpid', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsGrpId'), ['int'])),
                    ('docsif3cmdpvstatslastmeaslatency', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsLastMeasLatency'), ['int'])),
                    ('docsif3cmdpvstatslastmeastime', (YLeaf(YType.str, 'docsIf3CmDpvStatsLastMeasTime'), ['str'])),
                    ('docsif3cmdpvstatsminlatency', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsMinLatency'), ['int'])),
                    ('docsif3cmdpvstatsmaxlatency', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsMaxLatency'), ['int'])),
                    ('docsif3cmdpvstatsavglatency', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsAvgLatency'), ['int'])),
                    ('docsif3cmdpvstatsnummeas', (YLeaf(YType.uint32, 'docsIf3CmDpvStatsNumMeas'), ['int'])),
                    ('docsif3cmdpvstatslastcleartime', (YLeaf(YType.str, 'docsIf3CmDpvStatsLastClearTime'), ['str'])),
                ])
                self.ifindex = None
                self.docsif3cmdpvstatsgrpid = None
                self.docsif3cmdpvstatslastmeaslatency = None
                self.docsif3cmdpvstatslastmeastime = None
                self.docsif3cmdpvstatsminlatency = None
                self.docsif3cmdpvstatsmaxlatency = None
                self.docsif3cmdpvstatsavglatency = None
                self.docsif3cmdpvstatsnummeas = None
                self.docsif3cmdpvstatslastcleartime = None
                self._segment_path = lambda: "docsIf3CmDpvStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIf3CmDpvStatsGrpId='" + str(self.docsif3cmdpvstatsgrpid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmDpvStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmDpvStatsTable.DocsIf3CmDpvStatsEntry, ['ifindex', 'docsif3cmdpvstatsgrpid', 'docsif3cmdpvstatslastmeaslatency', 'docsif3cmdpvstatslastmeastime', 'docsif3cmdpvstatsminlatency', 'docsif3cmdpvstatsmaxlatency', 'docsif3cmdpvstatsavglatency', 'docsif3cmdpvstatsnummeas', 'docsif3cmdpvstatslastcleartime'], name, value)


    class DocsIf3CmEventCtrlTable(Entity):
        """
        This object represents the control mechanism to enable the
        dispatching of events based on the event Id. The following
        rules define the event control behavior\:
        
        \- The CmEventCtrl object has no instances or contains an 
          instance with Event ID 0. All events matching the Local Log
          settings of docsDevEvReporting are sent to local log ONLY.
        
        \- The CmEventCtrl object contains configured instances
          Only events matching the Event Ids configured in the object
          are sent according to the settings of the docsDevEvReporting
          object. 
          
          The CM does not persist instances of CmEventCtrl across 
          reinitializations.
        
        .. attribute:: docsif3cmeventctrlentry
        
        	The conceptual row of docsIf3CmEventCtrlTable
        	**type**\: list of  		 :py:class:`DocsIf3CmEventCtrlEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEventCtrlTable.DocsIf3CmEventCtrlEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmEventCtrlTable, self).__init__()

            self.yang_name = "docsIf3CmEventCtrlTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmEventCtrlEntry", ("docsif3cmeventctrlentry", DOCSIF3MIB.DocsIf3CmEventCtrlTable.DocsIf3CmEventCtrlEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmeventctrlentry = YList(self)
            self._segment_path = lambda: "docsIf3CmEventCtrlTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmEventCtrlTable, [], name, value)


        class DocsIf3CmEventCtrlEntry(Entity):
            """
            The conceptual row of docsIf3CmEventCtrlTable.
            
            .. attribute:: docsif3cmeventctrleventid  (key)
            
            	This key represents the Event ID of the event being  enabled for delivery to a dispatch mechanism (e.g., syslog)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmeventctrlstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmEventCtrlTable.DocsIf3CmEventCtrlEntry, self).__init__()

                self.yang_name = "docsIf3CmEventCtrlEntry"
                self.yang_parent_name = "docsIf3CmEventCtrlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmeventctrleventid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmeventctrleventid', (YLeaf(YType.uint32, 'docsIf3CmEventCtrlEventId'), ['int'])),
                    ('docsif3cmeventctrlstatus', (YLeaf(YType.enumeration, 'docsIf3CmEventCtrlStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docsif3cmeventctrleventid = None
                self.docsif3cmeventctrlstatus = None
                self._segment_path = lambda: "docsIf3CmEventCtrlEntry" + "[docsIf3CmEventCtrlEventId='" + str(self.docsif3cmeventctrleventid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmEventCtrlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmEventCtrlTable.DocsIf3CmEventCtrlEntry, ['docsif3cmeventctrleventid', 'docsif3cmeventctrlstatus'], name, value)


    class DocsIf3CmtsEventCtrlTable(Entity):
        """
        This object represents the control mechanism to enable the
        dispatching of  events based on the event Id. The following
        rules define the event control behavior\:
        
        \- The CmtsEventCtrl object has no instances or contains an 
          instance with Event ID 0. All events matching the Local Log 
          settings of docsDevEvReporting are sent to local log ONLY.
        
        \- The CmtsEventCtrl object contains configured instances
          Only events matching the Event Ids configured in the object
          are sent according to the settings of the docsDevEvReporting
          object. 
          
        \- The CMTS persists all instances of CmtsEventCtrl across 
          reinitializations.
        
        .. attribute:: docsif3cmtseventctrlentry
        
        	The conceptual row of docsIf3CmtsEventCtrlTable
        	**type**\: list of  		 :py:class:`DocsIf3CmtsEventCtrlEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsEventCtrlTable.DocsIf3CmtsEventCtrlEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsEventCtrlTable, self).__init__()

            self.yang_name = "docsIf3CmtsEventCtrlTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsEventCtrlEntry", ("docsif3cmtseventctrlentry", DOCSIF3MIB.DocsIf3CmtsEventCtrlTable.DocsIf3CmtsEventCtrlEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtseventctrlentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsEventCtrlTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsEventCtrlTable, [], name, value)


        class DocsIf3CmtsEventCtrlEntry(Entity):
            """
            The conceptual row of docsIf3CmtsEventCtrlTable.
            
            .. attribute:: docsif3cmtseventctrleventid  (key)
            
            	This key represents the Event ID of the event being  enabled for delivery to a dispatch mechanism (e.g., syslog)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmtseventctrlstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsEventCtrlTable.DocsIf3CmtsEventCtrlEntry, self).__init__()

                self.yang_name = "docsIf3CmtsEventCtrlEntry"
                self.yang_parent_name = "docsIf3CmtsEventCtrlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtseventctrleventid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtseventctrleventid', (YLeaf(YType.uint32, 'docsIf3CmtsEventCtrlEventId'), ['int'])),
                    ('docsif3cmtseventctrlstatus', (YLeaf(YType.enumeration, 'docsIf3CmtsEventCtrlStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docsif3cmtseventctrleventid = None
                self.docsif3cmtseventctrlstatus = None
                self._segment_path = lambda: "docsIf3CmtsEventCtrlEntry" + "[docsIf3CmtsEventCtrlEventId='" + str(self.docsif3cmtseventctrleventid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsEventCtrlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsEventCtrlTable.DocsIf3CmtsEventCtrlEntry, ['docsif3cmtseventctrleventid', 'docsif3cmtseventctrlstatus'], name, value)


    class DocsIf3CmMdCfgTable(Entity):
        """
        This object contains CM MAC domain level control and
        configuration attributes.
        
        .. attribute:: docsif3cmmdcfgentry
        
        	The conceptual row of docsIf3CmMdCfgTable. The ifIndex key corresponds to the MAC Domain interface
        	**type**\: list of  		 :py:class:`DocsIf3CmMdCfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmMdCfgTable, self).__init__()

            self.yang_name = "docsIf3CmMdCfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmMdCfgEntry", ("docsif3cmmdcfgentry", DOCSIF3MIB.DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmmdcfgentry = YList(self)
            self._segment_path = lambda: "docsIf3CmMdCfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmMdCfgTable, [], name, value)


        class DocsIf3CmMdCfgEntry(Entity):
            """
            The conceptual row of docsIf3CmMdCfgTable.
            The ifIndex key corresponds to the MAC Domain interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmmdcfgipprovmode
            
            	This attribute specifies whether the CM honors or ignores the  CMTS MDD TLV 5.1 setting in order to configure its IP provisioning  mode. The CM relies upon the CMTS to facilitate the successful  IP address acquisition independently of the MDD. When this attribute is set to 'ipv4Only' the CM will initiate the acquisition of a single  IPv4 address for the CM management stack. When this attribute is set to 'ipv6Only' the CM will initiate the  acquisition of a single IPv6 address for the CM management stack. When this attribute is set to 'honorMdd' the CM will initiate the  acquisition of an IPv6 or IPv4 address as directed by the MDD  message for provisioning and operation
            	**type**\:  :py:class:`DocsIf3CmMdCfgIpProvMode <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry.DocsIf3CmMdCfgIpProvMode>`
            
            .. attribute:: docsif3cmmdcfgipprovmoderesetonchange
            
            	This attribute determines if the CM is to automatically reset upon change of the IpProvMode attribute. The attribute has a default value of 'false' (2) which means that the CM does not reset upon change to IpProvMode attribute.  When this attribute is set to 'true' (1), the CM resets upon a change to the IpProvMode attribute
            	**type**\: bool
            
            .. attribute:: docsif3cmmdcfgipprovmoderesetonchangeholdofftimer
            
            	This attribute determines how long a CM with  IpProvModeResetOnChange set to 'true' waits to reset. When the  IpProvModeResetOnChange attribute is set to 'true' (1), the CM will decrement from the configured timer value before resetting. The default value of the IpProvModeResetOnChangeHoldOffTimer is 0  seconds which is equivalent to an immediate reset
            	**type**\: int
            
            	**range:** 0..300
            
            	**units**\: seconds
            
            .. attribute:: docsif3cmmdcfgipprovmodestoragetype
            
            	This attribute determines if the CM persists the value of  IpProvMode across a single reset or across all resets.   The  default value of this attribute is 'nonVolatile' (3) which means that the CM persists the value of IpProvMode across all resets.  The CM persists the value of IpProveMode across only a single  reset when IpProvModeStorageType is set to volatile(2). Other  StorageType values are not applicable for this object; an attempt to set this object to a value of other(1), permanent(4), or readOnly(5) will be rejected with an error code of inconsistentValue
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry, self).__init__()

                self.yang_name = "docsIf3CmMdCfgEntry"
                self.yang_parent_name = "docsIf3CmMdCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmmdcfgipprovmode', (YLeaf(YType.enumeration, 'docsIf3CmMdCfgIpProvMode'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'DOCSIF3MIB', 'DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry.DocsIf3CmMdCfgIpProvMode')])),
                    ('docsif3cmmdcfgipprovmoderesetonchange', (YLeaf(YType.boolean, 'docsIf3CmMdCfgIpProvModeResetOnChange'), ['bool'])),
                    ('docsif3cmmdcfgipprovmoderesetonchangeholdofftimer', (YLeaf(YType.uint32, 'docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer'), ['int'])),
                    ('docsif3cmmdcfgipprovmodestoragetype', (YLeaf(YType.enumeration, 'docsIf3CmMdCfgIpProvModeStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.ifindex = None
                self.docsif3cmmdcfgipprovmode = None
                self.docsif3cmmdcfgipprovmoderesetonchange = None
                self.docsif3cmmdcfgipprovmoderesetonchangeholdofftimer = None
                self.docsif3cmmdcfgipprovmodestoragetype = None
                self._segment_path = lambda: "docsIf3CmMdCfgEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmMdCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmMdCfgTable.DocsIf3CmMdCfgEntry, ['ifindex', 'docsif3cmmdcfgipprovmode', 'docsif3cmmdcfgipprovmoderesetonchange', 'docsif3cmmdcfgipprovmoderesetonchangeholdofftimer', 'docsif3cmmdcfgipprovmodestoragetype'], name, value)

            class DocsIf3CmMdCfgIpProvMode(Enum):
                """
                DocsIf3CmMdCfgIpProvMode (Enum Class)

                This attribute specifies whether the CM honors or ignores the 

                CMTS MDD TLV 5.1 setting in order to configure its IP provisioning 

                mode. The CM relies upon the CMTS to facilitate the successful 

                IP address acquisition independently of the MDD. When this attribute

                is set to 'ipv4Only' the CM will initiate the acquisition of a single 

                IPv4 address for the CM management stack.

                When this attribute is set to 'ipv6Only' the CM will initiate the 

                acquisition of a single IPv6 address for the CM management stack.

                When this attribute is set to 'honorMdd' the CM will initiate the 

                acquisition of an IPv6 or IPv4 address as directed by the MDD 

                message for provisioning and operation.

                .. data:: ipv4Only = 0

                .. data:: ipv6Only = 1

                .. data:: honorMdd = 4

                """

                ipv4Only = Enum.YLeaf(0, "ipv4Only")

                ipv6Only = Enum.YLeaf(1, "ipv6Only")

                honorMdd = Enum.YLeaf(4, "honorMdd")



    class DocsIf3CmEnergyMgt1x1CfgTable(Entity):
        """
        This object provides configuration state information 
        on the CM for the Energy Management 1x1 Mode feature.
        
        .. attribute:: docsif3cmenergymgt1x1cfgentry
        
        	The conceptual row of docsIf3CmEnergyMgt1x1CfgTable
        	**type**\: list of  		 :py:class:`DocsIf3CmEnergyMgt1x1CfgEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable.DocsIf3CmEnergyMgt1x1CfgEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable, self).__init__()

            self.yang_name = "docsIf3CmEnergyMgt1x1CfgTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmEnergyMgt1x1CfgEntry", ("docsif3cmenergymgt1x1cfgentry", DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable.DocsIf3CmEnergyMgt1x1CfgEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmenergymgt1x1cfgentry = YList(self)
            self._segment_path = lambda: "docsIf3CmEnergyMgt1x1CfgTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable, [], name, value)


        class DocsIf3CmEnergyMgt1x1CfgEntry(Entity):
            """
            The conceptual row of docsIf3CmEnergyMgt1x1CfgTable.
            
            .. attribute:: docsif3cmenergymgt1x1cfgdirection  (key)
            
            	This index indicates whether the threshold applies to the  upstream or downstream
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.IfDirection>`
            
            .. attribute:: docsif3cmenergymgt1x1cfgentrybitratethrshld
            
            	This attribute specifies the upstream or downstream bitrate threshold (in bps) below which the CM will request to enter  Energy Management 1x1 Mode operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bps
            
            .. attribute:: docsif3cmenergymgt1x1cfgentrytimethrshld
            
            	This attribute specifies the number of consecutive seconds  that the upstream or downstream data rate needs to remain below the Upstream or Downstream Entry Bitrate Threshold in order to  determine that a transition to Energy Management 1x1 Mode is  required
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: docsif3cmenergymgt1x1cfgexitbitratethrshld
            
            	This attribute specifies the upstream or downstream bitrate  threshold (in bps) above which the CM will request to leave  Energy Management 1x1 Mode operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bps
            
            .. attribute:: docsif3cmenergymgt1x1cfgexittimethrshld
            
            	This attribute specifies the number of consecutive seconds  that the upstream or downstream data rate needs to remain above the Upstream or Downstream Exit Bitrate Threshold in order to  determine that a transition out of Energy Management 1x1 Mode  is required
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable.DocsIf3CmEnergyMgt1x1CfgEntry, self).__init__()

                self.yang_name = "docsIf3CmEnergyMgt1x1CfgEntry"
                self.yang_parent_name = "docsIf3CmEnergyMgt1x1CfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmenergymgt1x1cfgdirection']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmenergymgt1x1cfgdirection', (YLeaf(YType.enumeration, 'docsIf3CmEnergyMgt1x1CfgDirection'), [('ydk.models.cisco_ios_xe.DOCS_IF3_MIB', 'IfDirection', '')])),
                    ('docsif3cmenergymgt1x1cfgentrybitratethrshld', (YLeaf(YType.uint32, 'docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld'), ['int'])),
                    ('docsif3cmenergymgt1x1cfgentrytimethrshld', (YLeaf(YType.uint32, 'docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld'), ['int'])),
                    ('docsif3cmenergymgt1x1cfgexitbitratethrshld', (YLeaf(YType.uint32, 'docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld'), ['int'])),
                    ('docsif3cmenergymgt1x1cfgexittimethrshld', (YLeaf(YType.uint32, 'docsIf3CmEnergyMgt1x1CfgExitTimeThrshld'), ['int'])),
                ])
                self.docsif3cmenergymgt1x1cfgdirection = None
                self.docsif3cmenergymgt1x1cfgentrybitratethrshld = None
                self.docsif3cmenergymgt1x1cfgentrytimethrshld = None
                self.docsif3cmenergymgt1x1cfgexitbitratethrshld = None
                self.docsif3cmenergymgt1x1cfgexittimethrshld = None
                self._segment_path = lambda: "docsIf3CmEnergyMgt1x1CfgEntry" + "[docsIf3CmEnergyMgt1x1CfgDirection='" + str(self.docsif3cmenergymgt1x1cfgdirection) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmEnergyMgt1x1CfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmEnergyMgt1x1CfgTable.DocsIf3CmEnergyMgt1x1CfgEntry, ['docsif3cmenergymgt1x1cfgdirection', 'docsif3cmenergymgt1x1cfgentrybitratethrshld', 'docsif3cmenergymgt1x1cfgentrytimethrshld', 'docsif3cmenergymgt1x1cfgexitbitratethrshld', 'docsif3cmenergymgt1x1cfgexittimethrshld'], name, value)


    class DocsIf3CmSpectrumAnalysisMeasTable(Entity):
        """
        This table provides a list of spectral analysis measurements 
        as performed across a range of center frequencies. The table 
        is capable of representing a full scan of the spectrum.
        
        .. attribute:: docsif3cmspectrumanalysismeasentry
        
        	Each row in the docsIf3CmSpectrumAnalysisMeasTable  represents the spectral analysis around a single center  frequency point in the spectrum
        	**type**\: list of  		 :py:class:`DocsIf3CmSpectrumAnalysisMeasEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable.DocsIf3CmSpectrumAnalysisMeasEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable, self).__init__()

            self.yang_name = "docsIf3CmSpectrumAnalysisMeasTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmSpectrumAnalysisMeasEntry", ("docsif3cmspectrumanalysismeasentry", DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable.DocsIf3CmSpectrumAnalysisMeasEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmspectrumanalysismeasentry = YList(self)
            self._segment_path = lambda: "docsIf3CmSpectrumAnalysisMeasTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable, [], name, value)


        class DocsIf3CmSpectrumAnalysisMeasEntry(Entity):
            """
            Each row in the docsIf3CmSpectrumAnalysisMeasTable 
            represents the spectral analysis around a single center 
            frequency point in the spectrum.
            
            .. attribute:: docsif3cmspectrumanalysismeasfrequency  (key)
            
            	This index indicates the center frequency of the spectral analysis span which is represented by this instance
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: docsif3cmspectrumanalysismeasamplitudedata
            
            	This attribute provides a list of the spectral amplitudes as  measured at the center frequency specified by the Frequency index.  The frequency bins are ordered from lowest to highest  frequencies covering the frequency span. Information about the center frequency, frequency span, number of bins and resolution bandwidth are included to provide context to the measurement  point
            	**type**\: str
            
            	**length:** 0 \| 2..4116
            
            .. attribute:: docsif3cmspectrumanalysismeastotalsegmentpower
            
            	This attribute provides the total RF power present in the  segment with the center frequency equal to the Frequency index and the span equal to the SegmentFrequencySpan. The value  represents the sum of the spectrum power in all of the  associated bins. The value is computed by summing power (not  dB) values and converting the final sum to TenthdB
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable.DocsIf3CmSpectrumAnalysisMeasEntry, self).__init__()

                self.yang_name = "docsIf3CmSpectrumAnalysisMeasEntry"
                self.yang_parent_name = "docsIf3CmSpectrumAnalysisMeasTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmspectrumanalysismeasfrequency']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmspectrumanalysismeasfrequency', (YLeaf(YType.int32, 'docsIf3CmSpectrumAnalysisMeasFrequency'), ['int'])),
                    ('docsif3cmspectrumanalysismeasamplitudedata', (YLeaf(YType.str, 'docsIf3CmSpectrumAnalysisMeasAmplitudeData'), ['str'])),
                    ('docsif3cmspectrumanalysismeastotalsegmentpower', (YLeaf(YType.int32, 'docsIf3CmSpectrumAnalysisMeasTotalSegmentPower'), ['int'])),
                ])
                self.docsif3cmspectrumanalysismeasfrequency = None
                self.docsif3cmspectrumanalysismeasamplitudedata = None
                self.docsif3cmspectrumanalysismeastotalsegmentpower = None
                self._segment_path = lambda: "docsIf3CmSpectrumAnalysisMeasEntry" + "[docsIf3CmSpectrumAnalysisMeasFrequency='" + str(self.docsif3cmspectrumanalysismeasfrequency) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmSpectrumAnalysisMeasTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmSpectrumAnalysisMeasTable.DocsIf3CmSpectrumAnalysisMeasEntry, ['docsif3cmspectrumanalysismeasfrequency', 'docsif3cmspectrumanalysismeasamplitudedata', 'docsif3cmspectrumanalysismeastotalsegmentpower'], name, value)


    class DocsIf3CmtsCmEmStatsTable(Entity):
        """
        This table defines Energy Management mode statistics for the
        CM as reported by the CMTS.  For example, such metrics can
        provide insight into configuration of appropriate EM 1x1 Mode
        Activity Detection thresholds on the CM and/or to get feedback
        on how/if the current thresholds are working well or are 
        causing user experience issues.
        
        .. attribute:: docsif3cmtscmemstatsentry
        
        	The conceptual row of docsIf3CmtsCmEmStatsTable
        	**type**\: list of  		 :py:class:`DocsIf3CmtsCmEmStatsEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable.DocsIf3CmtsCmEmStatsEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable, self).__init__()

            self.yang_name = "docsIf3CmtsCmEmStatsTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmtsCmEmStatsEntry", ("docsif3cmtscmemstatsentry", DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable.DocsIf3CmtsCmEmStatsEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmtscmemstatsentry = YList(self)
            self._segment_path = lambda: "docsIf3CmtsCmEmStatsTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable, [], name, value)


        class DocsIf3CmtsCmEmStatsEntry(Entity):
            """
            The conceptual row of docsIf3CmtsCmEmStatsTable.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3cmtscmregstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
            
            .. attribute:: docsif3cmtscmemstatsem1x1modetotalduration
            
            	This attribute indicates the total time duration, in seconds since registration, the CM identified by  docsIf3CmtsCmRegStatusId has been in Energy Management 1x1  mode, as controlled by the DBC\-REQ Energy Management 1x1  Mode Indicator TLV
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable.DocsIf3CmtsCmEmStatsEntry, self).__init__()

                self.yang_name = "docsIf3CmtsCmEmStatsEntry"
                self.yang_parent_name = "docsIf3CmtsCmEmStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docsif3cmtscmemstatsem1x1modetotalduration', (YLeaf(YType.uint32, 'docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration'), ['int'])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docsif3cmtscmemstatsem1x1modetotalduration = None
                self._segment_path = lambda: "docsIf3CmtsCmEmStatsEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmtsCmEmStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmtsCmEmStatsTable.DocsIf3CmtsCmEmStatsEntry, ['docsif3cmtscmregstatusid', 'docsif3cmtscmemstatsem1x1modetotalduration'], name, value)


    class DocsIf3CmEm1x1StatsTable(Entity):
        """
        This object defines Energy Management 1x1 mode statistics on
        the CM to provide insight into configuration of appropriate EM
        1x1 Mode Activity Detection thresholds and/or to get feedback
        on how/if the current thresholds are working well or are 
        causing user experience issues.
        These statistics are only applicable/valid when the Energy 
        Management 1x1 mode is enabled in the CM.
        
        .. attribute:: docsif3cmem1x1statsentry
        
        	The conceptual row of docsIf3CmEm1x1StatsTable. An instance exist for the CM MAC Domain Interface
        	**type**\: list of  		 :py:class:`DocsIf3CmEm1x1StatsEntry <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmEm1x1StatsTable.DocsIf3CmEm1x1StatsEntry>`
        
        

        """

        _prefix = 'DOCS-IF3-MIB'
        _revision = '2016-05-05'

        def __init__(self):
            super(DOCSIF3MIB.DocsIf3CmEm1x1StatsTable, self).__init__()

            self.yang_name = "docsIf3CmEm1x1StatsTable"
            self.yang_parent_name = "DOCS-IF3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIf3CmEm1x1StatsEntry", ("docsif3cmem1x1statsentry", DOCSIF3MIB.DocsIf3CmEm1x1StatsTable.DocsIf3CmEm1x1StatsEntry))])
            self._leafs = OrderedDict()

            self.docsif3cmem1x1statsentry = YList(self)
            self._segment_path = lambda: "docsIf3CmEm1x1StatsTable"
            self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIF3MIB.DocsIf3CmEm1x1StatsTable, [], name, value)


        class DocsIf3CmEm1x1StatsEntry(Entity):
            """
            The conceptual row of docsIf3CmEm1x1StatsTable.
            An instance exist for the CM MAC Domain Interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsif3cmem1x1statsnumbertimescrossedbelowusentrythrshlds
            
            	This attribute indicates the number of times since  registration the CM crossed below the upstream entry bitrate threshold for a number of consecutive seconds equal to or  exceeding the upstream entry time threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmem1x1statsnumbertimescrossedbelowdsentrythrshlds
            
            	This attribute indicates the number of times since  registration the CM crossed below the downstream entry  bitrate threshold for a number of consecutive seconds equal to or exceeding the downstream entry time threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsif3cmem1x1statstotalduration
            
            	This attribute indicates the total time duration, in seconds since registration, the CM has been in Energy Management 1x1 mode, as controlled by the DBC\-REQ Energy Management 1x1 Mode Indicator TLV. This attribute differs from  docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds because it is dependent on effects of the Energy Management Cycle  Period, and processing of EM\-REQ/EM\-RSP messages and DBC  messages that specifically indicate entry into or exit from Energy Management 1x1 mode
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: docsif3cmem1x1statstotaldurationbelowusthrshlds
            
            	This attribute indicates the total time duration, in seconds since registration, the CM satisfied upstream conditions for  entry into or remaining in Energy Management 1x1 mode
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: docsif3cmem1x1statstotaldurationbelowdsthrshlds
            
            	This attribute indicates the total time duration, in seconds since registration, the CM satisfied downstream conditions for  entry into or remaining in Energy Management 1x1 mode
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: docsif3cmem1x1statstotaldurationbelowusdsthrshlds
            
            	This attribute indicates the total time duration, in seconds  since registration, the CM, with respect to both upstream and  downstream entry and exit thresholds, satisfied conditions for  entry into and remaining in Energy Management 1x1 mode.  This  attribute differs from docsIf3CmEm1x1StatsTotalDuration  because it is not dependent on effects of the Energy  Management Cycle Period or processing of EM\-REQ/EM\-RSP  messages and DBC messages that specifically indicate entry into or exit from Energy Management 1x1 mode
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'DOCS-IF3-MIB'
            _revision = '2016-05-05'

            def __init__(self):
                super(DOCSIF3MIB.DocsIf3CmEm1x1StatsTable.DocsIf3CmEm1x1StatsEntry, self).__init__()

                self.yang_name = "docsIf3CmEm1x1StatsEntry"
                self.yang_parent_name = "docsIf3CmEm1x1StatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsif3cmem1x1statsnumbertimescrossedbelowusentrythrshlds', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds'), ['int'])),
                    ('docsif3cmem1x1statsnumbertimescrossedbelowdsentrythrshlds', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds'), ['int'])),
                    ('docsif3cmem1x1statstotalduration', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsTotalDuration'), ['int'])),
                    ('docsif3cmem1x1statstotaldurationbelowusthrshlds', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds'), ['int'])),
                    ('docsif3cmem1x1statstotaldurationbelowdsthrshlds', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds'), ['int'])),
                    ('docsif3cmem1x1statstotaldurationbelowusdsthrshlds', (YLeaf(YType.uint32, 'docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds'), ['int'])),
                ])
                self.ifindex = None
                self.docsif3cmem1x1statsnumbertimescrossedbelowusentrythrshlds = None
                self.docsif3cmem1x1statsnumbertimescrossedbelowdsentrythrshlds = None
                self.docsif3cmem1x1statstotalduration = None
                self.docsif3cmem1x1statstotaldurationbelowusthrshlds = None
                self.docsif3cmem1x1statstotaldurationbelowdsthrshlds = None
                self.docsif3cmem1x1statstotaldurationbelowusdsthrshlds = None
                self._segment_path = lambda: "docsIf3CmEm1x1StatsEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF3-MIB:DOCS-IF3-MIB/docsIf3CmEm1x1StatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIF3MIB.DocsIf3CmEm1x1StatsTable.DocsIf3CmEm1x1StatsEntry, ['ifindex', 'docsif3cmem1x1statsnumbertimescrossedbelowusentrythrshlds', 'docsif3cmem1x1statsnumbertimescrossedbelowdsentrythrshlds', 'docsif3cmem1x1statstotalduration', 'docsif3cmem1x1statstotaldurationbelowusthrshlds', 'docsif3cmem1x1statstotaldurationbelowdsthrshlds', 'docsif3cmem1x1statstotaldurationbelowusdsthrshlds'], name, value)

    def clone_ptr(self):
        self._top_entity = DOCSIF3MIB()
        return self._top_entity

