""" CISCO_DOCS_EXT_MIB 

This is the MIB module for the Cisco specific extension 
objects of Data Over Cable Service, Radio Frequency 
interface.  There is a standard MIB for Data\-Over\-Cable 
Service Interface Specifications (DOCSIS) and in Cisco,
it is called DOCS\-IF\-MIB. Besides the objects in 
DOCS\-IF\-MIB, this MIB module contains the extension 
objects to manage the Cable Modem Termination Systems 
(CMTS).

This MIB module includes objects for the scheduler 
that supports Quality of Service (QoS) of MCNS/DOCSIS 
compliant Radio Frequency (RF) interfaces in Cable Modem 
Termination Systems (CMTS). And the purpose is to let 
users configure attributes of the schedulers in 
order to ensure the Quality of Service and fairness for 
modem requests according to users' business needs. 
Also this MIB shows various states of the schedulers 
for users to monitor of the schedulers' current status. 

This MIB module also includes connection status objects
for cable modems and Customer Premise Equipment (CPE) 
and the purpose is to let users easily get the connection 
status and manage access group information about cable 
modems and CPE.

This MIB module also includes objects for upstream 
configuration for automated spectrum management in 
order to mitigate upstream impairment.

This MIB module also includes objects to keep count of
the total # of modems, # of registered and # of active
modems on the mac interface as well as each 
upstream. 

Glossary\:
BE       Best Effort

CPE      Customer Premise Equipment

CM       Cable Modem

CMTS     Cable Modem Termination Systems

DMIC     Dynamic Message Integrity Check

DOCSIS   Data Over Cable Service Interface Specifications

IE       Information Element

NIC      Network Interface Card

QoS      Quality of Service

RF       Radio Frequency

RTPS     Real\-Time Polling Service

SFID     Service Flow ID

SID      Service Id

TOD      Time of the Day

UGS      Unsolicited Grant Service

UGS\-AD   Unsolicited Grant Service with Activity Detection

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCODOCSEXTMIB(Entity):
    """
    
    
    .. attribute:: cdxcmtscmcpeobjects
    
    	
    	**type**\:  :py:class:`CdxCmtsCmCpeObjects <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmCpeObjects>`
    
    	**config**\: False
    
    .. attribute:: cdxwbresilobjects
    
    	
    	**type**\:  :py:class:`CdxWBResilObjects <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxWBResilObjects>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtsdocsislbobjects
    
    	
    	**type**\:  :py:class:`CdxCmtsDocsisLBObjects <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects>`
    
    	**config**\: False
    
    .. attribute:: cdxqosctrluptable
    
    	For each upstream interface, this table maintains a number  of objects related to Quality of Service scheduler which uses these attributes to control cable modem registration. 
    	**type**\:  :py:class:`CdxQosCtrlUpTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosCtrlUpTable>`
    
    	**config**\: False
    
    .. attribute:: cdxqosifratelimittable
    
    	This table describes the attributes of rate limiting for  schedulers in cable upstream and downstream interfaces that  support Quality of Service.  The rate limiting process is  to ensure the Quality of Service and fairness. 
    	**type**\:  :py:class:`CdxQosIfRateLimitTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosIfRateLimitTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtsserviceexttable
    
    	The list contains the additional attributes of a single Service ID that provided by docsIfCmtsServiceEntry. 
    	**type**\:  :py:class:`CdxCmtsServiceExtTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsServiceExtTable>`
    
    	**config**\: False
    
    .. attribute:: cdxupinfoelemstatstable
    
    	The table contains the attributes of a particular  Information Element type for each instance of the MAC  scheduler. It is indexed by upstream ifIndex. An Entry exists for each ifEntry with ifType of docsCableUpstream(129) Since each upstream has an instance of a MAC Scheduler so  this table has the per MAC scheduler slot information on a per Information Element basis. 
    	**type**\:  :py:class:`CdxUpInfoElemStatsTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxUpInfoElemStatsTable>`
    
    	**config**\: False
    
    .. attribute:: cdxbwqueuetable
    
    	This table describes the attributes of queues   in cable interfaces schedulers that support  Quality of Service
    	**type**\:  :py:class:`CdxBWQueueTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBWQueueTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmcpetable
    
    	This table contains information about cable modems (CM) or  Customer Premises Equipments (CPE). 
    	**type**\:  :py:class:`CdxCmCpeTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmCpeTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtscmstatusexttable
    
    	The list contains the additional CM status information. 
    	**type**\:  :py:class:`CdxCmtsCmStatusExtTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtsmacexttable
    
    	This table contains the additions attributes of a CMTS MAC interface that provided by docsIfCmtsMacTable. 
    	**type**\:  :py:class:`CdxCmtsMacExtTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsMacExtTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtscmchovertable
    
    	A table of CMTS operation entries to instruct cable modems to move to a new downstream and/or upstream channel.   An entry in this table is an operation that has been  initiated from CMTS to generates downstream frequency and/or  upstream channel override fields in the RNG\-RSP message sent  to a cable modem.  A RNG\-RSP message is sent to a cable  modem during initial maintenance opportunity.   This operation causes the uBR to place an entry for the cable  modem specified into the override request queue.  The link is  then broken by deleting the modem from its polling list.  When  the modem attempts initial ranging, the override request  causes downstream frequency and upstream channel override  fields to be inserted into the RNG\-RSP message.  
    	**type**\:  :py:class:`CdxCmtsCmChOverTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmChOverTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtscmtable
    
    	This table contains attributes or configurable parameters  for cable modems from a CMTS. 
    	**type**\:  :py:class:`CdxCmtsCmTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtscmstatusdmictable
    
    	This table contains the list of modems which failed the CMTS Dynamic Message Integrity Check (DMIC). The modems are  either Marked\: The modems failed the DMIC check but were still          allowed to come online. Locked\: The modems failed the DMIC check and hence were          allowed to come online with a restrictive QoS          profile as defined in  cdxCmtsCmDMICLockQos. Rejected\: The modems failed the DMIC check and hence           were not allowed to come online. Another objective of the objects in this table is to clear the lock on the modems
    	**type**\:  :py:class:`CdxCmtsCmStatusDMICTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtocpetable
    
    	This table contains information about CPE connects behind cable modem. It will return IP address and IP address type of each CPE connect to a CM.  It is not intended to walk the whole table. An application would need to query this table based on the specific indices. Otherwise, it will impact the CMTS performance due to the  huge size of this table.  The agent creates/destroys/modifies an entry whenever there is a CPE connect to a cable modem or disconnect from a cable modem
    	**type**\:  :py:class:`CdxCmToCpeTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmToCpeTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcpetocmtable
    
    	This table contains information about cable modems with CPE connects to.  It is not intended to walk the whole table. An application would need to query this table base on the specific index. Otherwise, it will impact the CMTS performance due to the huge size of this table.  The agent creates/destroys/modifies an entry whenever there is update for the cable modem that CPE connects to
    	**type**\:  :py:class:`CdxCpeToCmTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCpeToCmTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcpeipprefixtable
    
    	The table contains a list CPE's IP Prefix management information
    	**type**\:  :py:class:`CdxCpeIpPrefixTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCpeIpPrefixTable>`
    
    	**config**\: False
    
    .. attribute:: cdxifupstreamchannelexttable
    
    	This table contains upstream channel attributes for   automated Spectrum management, in addition to the ones provided by docsIfUpstreamChannelEntry. It also contains upstream channel attributes to count  the number of active,registered and total number of cable  modems on this upstream. 
    	**type**\:  :py:class:`CdxIfUpstreamChannelExtTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable>`
    
    	**config**\: False
    
    .. attribute:: cdxwbresilcmtable
    
    	This table contains information about partial service cable modems (CM), including both downstream and upstream partial service modems
    	**type**\:  :py:class:`CdxWBResilCmTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxWBResilCmTable>`
    
    	**config**\: False
    
    .. attribute:: cdxrftoprimarychannelmappingtable
    
    	This table contains information of the mapping of the physical RF channels to the primary RF channels
    	**type**\:  :py:class:`CdxRFtoPrimaryChannelMappingTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cdxprimarychanneltorfmappingtable
    
    	This table contains information of the mapping of the primary RF channels to the physical RF channels
    	**type**\:  :py:class:`CdxPrimaryChanneltoRFMappingTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtsmtccmtable
    
    	This table contains CM management information of Transmit Channel Set(TCS) in the system
    	**type**\:  :py:class:`CdxCmtsMtcCmTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsMtcCmTable>`
    
    	**config**\: False
    
    .. attribute:: cdxcmtsuscbsflowtable
    
    	This table contains the Upstream Channel Bonding Service Flow management information
    	**type**\:  :py:class:`CdxCmtsUscbSflowTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsUscbSflowTable>`
    
    	**config**\: False
    
    .. attribute:: cdxrpdgs7ktable
    
    	The cdxRPDGS7KTable contains the attributes of GS7K.  An Entry exists for each instance.  It is indexed by GS7K's MacAddress
    	**type**\:  :py:class:`CdxRPDGS7KTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRPDGS7KTable>`
    
    	**config**\: False
    
    .. attribute:: cdxbundleiphelpertable
    
    	A list of cable helper entries on Bundle/Sub\-Bundle interface
    	**type**\:  :py:class:`CdxBundleIpHelperTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIpHelperTable>`
    
    	**config**\: False
    
    .. attribute:: cdxbundleipv6dhcprelaytable
    
    	Ipv6 dhcp relay configurations on Bundle/Sub\-Bundle interface
    	**type**\:  :py:class:`CdxBundleIPv6DHCPRelayTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable>`
    
    	**config**\: False
    
    .. attribute:: cdxbundleipv6dhcprelaydesttable
    
    	 A list of IPv6 DHCP relay destination entries on Cable Bundle/Sub\-Bundle interfaces
    	**type**\:  :py:class:`CdxBundleIPv6DHCPRelayDestTable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-DOCS-EXT-MIB'
    _revision = '2017-11-10'

    def __init__(self):
        super(CISCODOCSEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DOCS-EXT-MIB"
        self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cdxCmtsCmCpeObjects", ("cdxcmtscmcpeobjects", CISCODOCSEXTMIB.CdxCmtsCmCpeObjects)), ("cdxWBResilObjects", ("cdxwbresilobjects", CISCODOCSEXTMIB.CdxWBResilObjects)), ("cdxCmtsDocsisLBObjects", ("cdxcmtsdocsislbobjects", CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects)), ("cdxQosCtrlUpTable", ("cdxqosctrluptable", CISCODOCSEXTMIB.CdxQosCtrlUpTable)), ("cdxQosIfRateLimitTable", ("cdxqosifratelimittable", CISCODOCSEXTMIB.CdxQosIfRateLimitTable)), ("cdxCmtsServiceExtTable", ("cdxcmtsserviceexttable", CISCODOCSEXTMIB.CdxCmtsServiceExtTable)), ("cdxUpInfoElemStatsTable", ("cdxupinfoelemstatstable", CISCODOCSEXTMIB.CdxUpInfoElemStatsTable)), ("cdxBWQueueTable", ("cdxbwqueuetable", CISCODOCSEXTMIB.CdxBWQueueTable)), ("cdxCmCpeTable", ("cdxcmcpetable", CISCODOCSEXTMIB.CdxCmCpeTable)), ("cdxCmtsCmStatusExtTable", ("cdxcmtscmstatusexttable", CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable)), ("cdxCmtsMacExtTable", ("cdxcmtsmacexttable", CISCODOCSEXTMIB.CdxCmtsMacExtTable)), ("cdxCmtsCmChOverTable", ("cdxcmtscmchovertable", CISCODOCSEXTMIB.CdxCmtsCmChOverTable)), ("cdxCmtsCmTable", ("cdxcmtscmtable", CISCODOCSEXTMIB.CdxCmtsCmTable)), ("cdxCmtsCmStatusDMICTable", ("cdxcmtscmstatusdmictable", CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable)), ("cdxCmToCpeTable", ("cdxcmtocpetable", CISCODOCSEXTMIB.CdxCmToCpeTable)), ("cdxCpeToCmTable", ("cdxcpetocmtable", CISCODOCSEXTMIB.CdxCpeToCmTable)), ("cdxCpeIpPrefixTable", ("cdxcpeipprefixtable", CISCODOCSEXTMIB.CdxCpeIpPrefixTable)), ("cdxIfUpstreamChannelExtTable", ("cdxifupstreamchannelexttable", CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable)), ("cdxWBResilCmTable", ("cdxwbresilcmtable", CISCODOCSEXTMIB.CdxWBResilCmTable)), ("cdxRFtoPrimaryChannelMappingTable", ("cdxrftoprimarychannelmappingtable", CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable)), ("cdxPrimaryChanneltoRFMappingTable", ("cdxprimarychanneltorfmappingtable", CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable)), ("cdxCmtsMtcCmTable", ("cdxcmtsmtccmtable", CISCODOCSEXTMIB.CdxCmtsMtcCmTable)), ("cdxCmtsUscbSflowTable", ("cdxcmtsuscbsflowtable", CISCODOCSEXTMIB.CdxCmtsUscbSflowTable)), ("cdxRPDGS7KTable", ("cdxrpdgs7ktable", CISCODOCSEXTMIB.CdxRPDGS7KTable)), ("cdxBundleIpHelperTable", ("cdxbundleiphelpertable", CISCODOCSEXTMIB.CdxBundleIpHelperTable)), ("cdxBundleIPv6DHCPRelayTable", ("cdxbundleipv6dhcprelaytable", CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable)), ("cdxBundleIPv6DHCPRelayDestTable", ("cdxbundleipv6dhcprelaydesttable", CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable))])
        self._leafs = OrderedDict()

        self.cdxcmtscmcpeobjects = CISCODOCSEXTMIB.CdxCmtsCmCpeObjects()
        self.cdxcmtscmcpeobjects.parent = self
        self._children_name_map["cdxcmtscmcpeobjects"] = "cdxCmtsCmCpeObjects"

        self.cdxwbresilobjects = CISCODOCSEXTMIB.CdxWBResilObjects()
        self.cdxwbresilobjects.parent = self
        self._children_name_map["cdxwbresilobjects"] = "cdxWBResilObjects"

        self.cdxcmtsdocsislbobjects = CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects()
        self.cdxcmtsdocsislbobjects.parent = self
        self._children_name_map["cdxcmtsdocsislbobjects"] = "cdxCmtsDocsisLBObjects"

        self.cdxqosctrluptable = CISCODOCSEXTMIB.CdxQosCtrlUpTable()
        self.cdxqosctrluptable.parent = self
        self._children_name_map["cdxqosctrluptable"] = "cdxQosCtrlUpTable"

        self.cdxqosifratelimittable = CISCODOCSEXTMIB.CdxQosIfRateLimitTable()
        self.cdxqosifratelimittable.parent = self
        self._children_name_map["cdxqosifratelimittable"] = "cdxQosIfRateLimitTable"

        self.cdxcmtsserviceexttable = CISCODOCSEXTMIB.CdxCmtsServiceExtTable()
        self.cdxcmtsserviceexttable.parent = self
        self._children_name_map["cdxcmtsserviceexttable"] = "cdxCmtsServiceExtTable"

        self.cdxupinfoelemstatstable = CISCODOCSEXTMIB.CdxUpInfoElemStatsTable()
        self.cdxupinfoelemstatstable.parent = self
        self._children_name_map["cdxupinfoelemstatstable"] = "cdxUpInfoElemStatsTable"

        self.cdxbwqueuetable = CISCODOCSEXTMIB.CdxBWQueueTable()
        self.cdxbwqueuetable.parent = self
        self._children_name_map["cdxbwqueuetable"] = "cdxBWQueueTable"

        self.cdxcmcpetable = CISCODOCSEXTMIB.CdxCmCpeTable()
        self.cdxcmcpetable.parent = self
        self._children_name_map["cdxcmcpetable"] = "cdxCmCpeTable"

        self.cdxcmtscmstatusexttable = CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable()
        self.cdxcmtscmstatusexttable.parent = self
        self._children_name_map["cdxcmtscmstatusexttable"] = "cdxCmtsCmStatusExtTable"

        self.cdxcmtsmacexttable = CISCODOCSEXTMIB.CdxCmtsMacExtTable()
        self.cdxcmtsmacexttable.parent = self
        self._children_name_map["cdxcmtsmacexttable"] = "cdxCmtsMacExtTable"

        self.cdxcmtscmchovertable = CISCODOCSEXTMIB.CdxCmtsCmChOverTable()
        self.cdxcmtscmchovertable.parent = self
        self._children_name_map["cdxcmtscmchovertable"] = "cdxCmtsCmChOverTable"

        self.cdxcmtscmtable = CISCODOCSEXTMIB.CdxCmtsCmTable()
        self.cdxcmtscmtable.parent = self
        self._children_name_map["cdxcmtscmtable"] = "cdxCmtsCmTable"

        self.cdxcmtscmstatusdmictable = CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable()
        self.cdxcmtscmstatusdmictable.parent = self
        self._children_name_map["cdxcmtscmstatusdmictable"] = "cdxCmtsCmStatusDMICTable"

        self.cdxcmtocpetable = CISCODOCSEXTMIB.CdxCmToCpeTable()
        self.cdxcmtocpetable.parent = self
        self._children_name_map["cdxcmtocpetable"] = "cdxCmToCpeTable"

        self.cdxcpetocmtable = CISCODOCSEXTMIB.CdxCpeToCmTable()
        self.cdxcpetocmtable.parent = self
        self._children_name_map["cdxcpetocmtable"] = "cdxCpeToCmTable"

        self.cdxcpeipprefixtable = CISCODOCSEXTMIB.CdxCpeIpPrefixTable()
        self.cdxcpeipprefixtable.parent = self
        self._children_name_map["cdxcpeipprefixtable"] = "cdxCpeIpPrefixTable"

        self.cdxifupstreamchannelexttable = CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable()
        self.cdxifupstreamchannelexttable.parent = self
        self._children_name_map["cdxifupstreamchannelexttable"] = "cdxIfUpstreamChannelExtTable"

        self.cdxwbresilcmtable = CISCODOCSEXTMIB.CdxWBResilCmTable()
        self.cdxwbresilcmtable.parent = self
        self._children_name_map["cdxwbresilcmtable"] = "cdxWBResilCmTable"

        self.cdxrftoprimarychannelmappingtable = CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable()
        self.cdxrftoprimarychannelmappingtable.parent = self
        self._children_name_map["cdxrftoprimarychannelmappingtable"] = "cdxRFtoPrimaryChannelMappingTable"

        self.cdxprimarychanneltorfmappingtable = CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable()
        self.cdxprimarychanneltorfmappingtable.parent = self
        self._children_name_map["cdxprimarychanneltorfmappingtable"] = "cdxPrimaryChanneltoRFMappingTable"

        self.cdxcmtsmtccmtable = CISCODOCSEXTMIB.CdxCmtsMtcCmTable()
        self.cdxcmtsmtccmtable.parent = self
        self._children_name_map["cdxcmtsmtccmtable"] = "cdxCmtsMtcCmTable"

        self.cdxcmtsuscbsflowtable = CISCODOCSEXTMIB.CdxCmtsUscbSflowTable()
        self.cdxcmtsuscbsflowtable.parent = self
        self._children_name_map["cdxcmtsuscbsflowtable"] = "cdxCmtsUscbSflowTable"

        self.cdxrpdgs7ktable = CISCODOCSEXTMIB.CdxRPDGS7KTable()
        self.cdxrpdgs7ktable.parent = self
        self._children_name_map["cdxrpdgs7ktable"] = "cdxRPDGS7KTable"

        self.cdxbundleiphelpertable = CISCODOCSEXTMIB.CdxBundleIpHelperTable()
        self.cdxbundleiphelpertable.parent = self
        self._children_name_map["cdxbundleiphelpertable"] = "cdxBundleIpHelperTable"

        self.cdxbundleipv6dhcprelaytable = CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable()
        self.cdxbundleipv6dhcprelaytable.parent = self
        self._children_name_map["cdxbundleipv6dhcprelaytable"] = "cdxBundleIPv6DHCPRelayTable"

        self.cdxbundleipv6dhcprelaydesttable = CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable()
        self.cdxbundleipv6dhcprelaydesttable.parent = self
        self._children_name_map["cdxbundleipv6dhcprelaydesttable"] = "cdxBundleIPv6DHCPRelayDestTable"
        self._segment_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCODOCSEXTMIB, [], name, value)


    class CdxCmtsCmCpeObjects(Entity):
        """
        
        
        .. attribute:: cdxcmtscmchovertimeexpiration
        
        	The time period to expire a CMTS channel override operation.  Within the time period, if the CMTS cannot send out a  RNG\-RSP message with channel override fields to a cable  modem specified in the operation, the CMTS will abort  the operation. The possible reason is that the cable  modem does not repeat the initial ranging.   The change to this object will not affect the already active  operations in this cdxCmtsCmChOverTable.      Once the operation completes, the management station should retrieve the values of the cdxCmtsCmChOverState  object of interest, and should then delete the entry from cdxCmtsCmChOverTable.  In order to prevent old  entries from clogging the table, entries will be aged out,  but an entry will never be deleted within 15 minutes of  completing. 
        	**type**\: int
        
        	**range:** 1..86400
        
        	**config**\: False
        
        	**units**\: minutes
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsCmCpeObjects, self).__init__()

            self.yang_name = "cdxCmtsCmCpeObjects"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cdxcmtscmchovertimeexpiration', (YLeaf(YType.int32, 'cdxCmtsCmChOverTimeExpiration'), ['int'])),
            ])
            self.cdxcmtscmchovertimeexpiration = None
            self._segment_path = lambda: "cdxCmtsCmCpeObjects"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmCpeObjects, ['cdxcmtscmchovertimeexpiration'], name, value)



    class CdxWBResilObjects(Entity):
        """
        
        
        .. attribute:: cdxwbresilrfchangedampentime
        
        	This object specifies the amount of time an RF channel must remain in its new state, either UP or DOWN, before the transition is considered valid.  This value applies to all non\-primary RF channels in the CMTS
        	**type**\: int
        
        	**range:** 1..65535
        
        	**config**\: False
        
        	**units**\: Second
        
        .. attribute:: cdxwbresilrfchangetriggerpercentage
        
        	This object specifies the percentage of cable modems (CMs) that must report that a particular Non Primary RF channel is DOWN, before that channel is removed from any/all bonding groups with that Non Primary RF channel configured. The value of 0 will prevent from any bonding group modifications. In order to dampen state's changes for an RF channel, the trigger for  a channel being restored is one half of this object's value. 
        	**type**\: int
        
        	**range:** 0..100
        
        	**config**\: False
        
        	**units**\: Percentage
        
        .. attribute:: cdxwbresilrfchangetriggercount
        
        	This object specifies the count of cable modems (CMs) that must report that a particular Non Primary RF channel is DOWN, before that channel is removed from any/all bonding groups with that Non Primary RF channel configured. The value of 0 will prevent from any bonding group modifications. In order to dampen state's changes for an RF channel, the trigger for  a channel being restored is one half of this object's value
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: cdxwbresilrfchangetriggermovesecondary
        
        	This object specifies whether the secondary service flows are allowed to be moved and created on the narrowband interface
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cdxwbresilnotificationenable
        
        	An indication of whether the cdxWBResilRFDown, cdxWBResilRFUp,  cdxWBResilCMPartialServiceNotif, cdxWBResilCMFullServiceNotif,  cdxWBResilEvent, cdxWBResilUsFullServiceNotif and cdxWBResilUsPartialServiceNotif are enabled
        	**type**\:  :py:class:`CdxWBResilNotificationEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxWBResilObjects.CdxWBResilNotificationEnable>`
        
        	**config**\: False
        
        .. attribute:: cdxwbresilnotificationsinterval
        
        	This object specifies the interval that cdxWBResilEvent traps  could be sent per cable modem. It is to avoid too many cdxWBResilEvent traps sent for a cable modem during a short period of time. The default value is 1 (second). If the value is 0, the trap  cdxWBResilEvent will be sent for every wideband resiliency event. If the value is set to any value greater than 0, for the wideband  resiliency events which occurred in the same specific period of time,  the CMTS will send only one trap
        	**type**\: int
        
        	**range:** 0..86400
        
        	**config**\: False
        
        	**units**\: Second
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxWBResilObjects, self).__init__()

            self.yang_name = "cdxWBResilObjects"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cdxwbresilrfchangedampentime', (YLeaf(YType.int32, 'cdxWBResilRFChangeDampenTime'), ['int'])),
                ('cdxwbresilrfchangetriggerpercentage', (YLeaf(YType.int32, 'cdxWBResilRFChangeTriggerPercentage'), ['int'])),
                ('cdxwbresilrfchangetriggercount', (YLeaf(YType.int32, 'cdxWBResilRFChangeTriggerCount'), ['int'])),
                ('cdxwbresilrfchangetriggermovesecondary', (YLeaf(YType.boolean, 'cdxWBResilRFChangeTriggerMoveSecondary'), ['bool'])),
                ('cdxwbresilnotificationenable', (YLeaf(YType.bits, 'cdxWBResilNotificationEnable'), ['Bits'])),
                ('cdxwbresilnotificationsinterval', (YLeaf(YType.int32, 'cdxWBResilNotificationsInterval'), ['int'])),
            ])
            self.cdxwbresilrfchangedampentime = None
            self.cdxwbresilrfchangetriggerpercentage = None
            self.cdxwbresilrfchangetriggercount = None
            self.cdxwbresilrfchangetriggermovesecondary = None
            self.cdxwbresilnotificationenable = Bits()
            self.cdxwbresilnotificationsinterval = None
            self._segment_path = lambda: "cdxWBResilObjects"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxWBResilObjects, ['cdxwbresilrfchangedampentime', 'cdxwbresilrfchangetriggerpercentage', 'cdxwbresilrfchangetriggercount', 'cdxwbresilrfchangetriggermovesecondary', 'cdxwbresilnotificationenable', 'cdxwbresilnotificationsinterval'], name, value)



    class CdxCmtsDocsisLBObjects(Entity):
        """
        
        
        .. attribute:: cdxcmtsdocsislbenable
        
        	This is a cisco private object. Setting this object to true(1) enables d2.0 loadbalancing on CMTS and allows user to further config other options for d3.0 loadbalancing(cdxCmtsD30LBEnable, cdxCmtsD30LBUpstreamEnable cdxCmtsD30LBStaticEnable  		and cdxCmtsD30LBDynEnable).  Setting it to false(2) disables all oad balancing operations
        	**type**\:  :py:class:`CdxCmtsDocsisLBEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects.CdxCmtsDocsisLBEnable>`
        
        	**config**\: False
        
        .. attribute:: cdxcmtsd30lbenable
        
        	Setting this object to true(1) enables d3.0 static loadbalancing on CMTS and allows user to further config other objects for d3.0 loadbalancing(cdxCmtsD30LBUpstreamEnable and cdxCmtsD30LBStaticEnable and cdxCmtsD30LBDynEnable) . Setting it to false(2) disables d3.0 loadbalancing
        	**type**\:  :py:class:`CdxCmtsD30LBEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects.CdxCmtsD30LBEnable>`
        
        	**config**\: False
        
        .. attribute:: cdxcmtsd30lbupstreamenable
        
        	Setting this object to true(1) enables upstream loadbalancing in docsis 3.0 static loadbalancing. Default is false(2).Only if docsis\-enable and docsis30\-enable set to true can this object take effect
        	**type**\:  :py:class:`CdxCmtsD30LBUpstreamEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects.CdxCmtsD30LBUpstreamEnable>`
        
        	**config**\: False
        
        .. attribute:: cdxcmtsd30lbstaticenable
        
        	Setting this to true(1) enables autonomous D30 LB to move wideband modems if LB group is not in a balancing state.Default is false(2). Only if docsis\-enable and docsis30\-enable is set to true can this object set to true(1)
        	**type**\:  :py:class:`CdxCmtsD30LBStaticEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects.CdxCmtsD30LBStaticEnable>`
        
        	**config**\: False
        
        .. attribute:: cdxcmtsd30lbdynenable
        
        	Setting this to true(1) enables autonomous D30 LB to move wideband modems if LB group is not in a balancing state.Default is false(2). Only if docsis\-enable and docsis30\-enable is set to true can this object set to true(1)
        	**type**\:  :py:class:`CdxCmtsD30LBDynEnable <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects.CdxCmtsD30LBDynEnable>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects, self).__init__()

            self.yang_name = "cdxCmtsDocsisLBObjects"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cdxcmtsdocsislbenable', (YLeaf(YType.enumeration, 'cdxCmtsDocsisLBEnable'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsDocsisLBObjects.CdxCmtsDocsisLBEnable')])),
                ('cdxcmtsd30lbenable', (YLeaf(YType.enumeration, 'cdxCmtsD30LBEnable'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsDocsisLBObjects.CdxCmtsD30LBEnable')])),
                ('cdxcmtsd30lbupstreamenable', (YLeaf(YType.enumeration, 'cdxCmtsD30LBUpstreamEnable'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsDocsisLBObjects.CdxCmtsD30LBUpstreamEnable')])),
                ('cdxcmtsd30lbstaticenable', (YLeaf(YType.enumeration, 'cdxCmtsD30LBStaticEnable'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsDocsisLBObjects.CdxCmtsD30LBStaticEnable')])),
                ('cdxcmtsd30lbdynenable', (YLeaf(YType.enumeration, 'cdxCmtsD30LBDynEnable'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsDocsisLBObjects.CdxCmtsD30LBDynEnable')])),
            ])
            self.cdxcmtsdocsislbenable = None
            self.cdxcmtsd30lbenable = None
            self.cdxcmtsd30lbupstreamenable = None
            self.cdxcmtsd30lbstaticenable = None
            self.cdxcmtsd30lbdynenable = None
            self._segment_path = lambda: "cdxCmtsDocsisLBObjects"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsDocsisLBObjects, ['cdxcmtsdocsislbenable', 'cdxcmtsd30lbenable', 'cdxcmtsd30lbupstreamenable', 'cdxcmtsd30lbstaticenable', 'cdxcmtsd30lbdynenable'], name, value)

        class CdxCmtsD30LBDynEnable(Enum):
            """
            CdxCmtsD30LBDynEnable (Enum Class)

            Setting this to true(1) enables autonomous D30 LB to move

            wideband modems if LB group is not in a balancing state.Default

            is false(2).

            Only if docsis\-enable and docsis30\-enable is set to true can

            this object set to true(1)

            .. data:: true = 1

            .. data:: false = 2

            """

            true = Enum.YLeaf(1, "true")

            false = Enum.YLeaf(2, "false")


        class CdxCmtsD30LBEnable(Enum):
            """
            CdxCmtsD30LBEnable (Enum Class)

            Setting this object to true(1) enables d3.0 static

            loadbalancing on CMTS and allows user to further config other

            objects for d3.0 loadbalancing(cdxCmtsD30LBUpstreamEnable and

            cdxCmtsD30LBStaticEnable and cdxCmtsD30LBDynEnable) .

            Setting it to false(2) disables d3.0 loadbalancing.

            .. data:: true = 1

            .. data:: false = 2

            """

            true = Enum.YLeaf(1, "true")

            false = Enum.YLeaf(2, "false")


        class CdxCmtsD30LBStaticEnable(Enum):
            """
            CdxCmtsD30LBStaticEnable (Enum Class)

            Setting this to true(1) enables autonomous D30 LB to move

            wideband modems if LB group is not in a balancing state.Default

            is false(2).

            Only if docsis\-enable and docsis30\-enable is set to true can

            this object set to true(1)

            .. data:: true = 1

            .. data:: false = 2

            """

            true = Enum.YLeaf(1, "true")

            false = Enum.YLeaf(2, "false")


        class CdxCmtsD30LBUpstreamEnable(Enum):
            """
            CdxCmtsD30LBUpstreamEnable (Enum Class)

            Setting this object to true(1) enables upstream loadbalancing

            in docsis 3.0 static loadbalancing. Default is false(2).Only

            if docsis\-enable and docsis30\-enable set to true can this object

            take effect.

            .. data:: true = 1

            .. data:: false = 2

            """

            true = Enum.YLeaf(1, "true")

            false = Enum.YLeaf(2, "false")


        class CdxCmtsDocsisLBEnable(Enum):
            """
            CdxCmtsDocsisLBEnable (Enum Class)

            This is a cisco private object. Setting this object to true(1)

            enables d2.0 loadbalancing on CMTS and allows user to further

            config other options for d3.0 loadbalancing(cdxCmtsD30LBEnable,

            cdxCmtsD30LBUpstreamEnable cdxCmtsD30LBStaticEnable 

            		and cdxCmtsD30LBDynEnable). 

            Setting it to false(2) disables all oad balancing operations.

            .. data:: true = 1

            .. data:: false = 2

            """

            true = Enum.YLeaf(1, "true")

            false = Enum.YLeaf(2, "false")




    class CdxQosCtrlUpTable(Entity):
        """
        For each upstream interface, this table maintains a number 
        of objects related to Quality of Service scheduler which uses
        these attributes to control cable modem registration. 
        
        .. attribute:: cdxqosctrlupentry
        
        	A list of attributes for each upstream MAC scheduler  that supports Quality of Service.  Entries in this table exist for each ifEntry with ifType of docsCableUpstream(129). 
        	**type**\: list of  		 :py:class:`CdxQosCtrlUpEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosCtrlUpTable.CdxQosCtrlUpEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxQosCtrlUpTable, self).__init__()

            self.yang_name = "cdxQosCtrlUpTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxQosCtrlUpEntry", ("cdxqosctrlupentry", CISCODOCSEXTMIB.CdxQosCtrlUpTable.CdxQosCtrlUpEntry))])
            self._leafs = OrderedDict()

            self.cdxqosctrlupentry = YList(self)
            self._segment_path = lambda: "cdxQosCtrlUpTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxQosCtrlUpTable, [], name, value)


        class CdxQosCtrlUpEntry(Entity):
            """
            A list of attributes for each upstream MAC scheduler 
            that supports Quality of Service.  Entries in this table
            exist for each ifEntry with ifType of docsCableUpstream(129). 
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxqosctrlupadmissionctrl
            
            	The admission control status for minimum guaranteed upstream  bandwidth scheduling service requests for this upstream.  When this object is set to 'true', if there is a new modem  with minimum guaranteed upstream bandwidth scheduling service in its QoS class requesting to be supported in this upstream, the upstream scheduler will check the virtual reserved  bandwidth remaining capacity before giving admission to this  new modem. If there is not enough reserved upstream bandwidth to serve the modem's minimum guaranteed bandwidth, the  registration request will be rejected.    This object is set to 'false' to disable admission control. That is, there will be no checking for bandwidth capacity and the upstream interface scheduler just admits modem registration requests.   This object is not meant for Unsolicited Grant Service(UGS)  scheduling service as admission control is a requirement in  this case. 
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxqosctrlupmaxrsvdbwpercent
            
            	The percentage of upstream maximum reserved bandwidth to the  raw bandwidth if the admission control is enabled on this  upstream.   For example, if the upstream interface has raw bandwidth  1,600,000 bits/second and cdxQosCtrlUpMaxRsvdBWPercent is 200  percent, then this upstream scheduler will set the maximum of  virtual reserved bandwidth capacity to 3,200,000 bits/second  (1,600,000 \* 2) to serve cable modems with minimum guaranteed  upstream bandwidth.    The default value is 100 percent (that is, maximum reserved  bandwidth is the raw bandwidth.) Whenever the admission control  is changed (on to off, off to on), this value will be reset to  the default value 100.    If the admission control is disabled, the value will be reset  to 100 (the default value). 
            	**type**\: int
            
            	**range:** 10..1000
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cdxqosctrlupadmissionrejects
            
            	The count of cable modem registration requests rejected on  this upstream interface due to insufficient reserved  bandwidth for serving the cable modems with Unsolicited  Grant Service (UGS) scheduling service when UGS is  supported and for serving the cable modems with minimum  guaranteed bandwidth in its Quality of Service class when admission control is enabled on this upstream interface 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxqosctrlupreservedbw
            
            	The current total reserved bandwidth in bits per second of  this upstream interface.  It is the sum of all cable modems' minimum guaranteed bandwidth in bits per second currently  supported on this upstream. 
            	**type**\: int
            
            	**range:** 0..102400000
            
            	**config**\: False
            
            	**units**\: bits/second
            
            .. attribute:: cdxqosctrlupmaxvirtualbw
            
            	The maximum virtual bandwidth capacity of this upstream interface if the admission control is enabled. It is the raw bandwidth  in bits per second times the percentage. If the admission  control is disabled, then this object will contain the value  zero. 
            	**type**\: int
            
            	**range:** 0..102400000
            
            	**config**\: False
            
            	**units**\: bits/second
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxQosCtrlUpTable.CdxQosCtrlUpEntry, self).__init__()

                self.yang_name = "cdxQosCtrlUpEntry"
                self.yang_parent_name = "cdxQosCtrlUpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxqosctrlupadmissionctrl', (YLeaf(YType.boolean, 'cdxQosCtrlUpAdmissionCtrl'), ['bool'])),
                    ('cdxqosctrlupmaxrsvdbwpercent', (YLeaf(YType.int32, 'cdxQosCtrlUpMaxRsvdBWPercent'), ['int'])),
                    ('cdxqosctrlupadmissionrejects', (YLeaf(YType.uint32, 'cdxQosCtrlUpAdmissionRejects'), ['int'])),
                    ('cdxqosctrlupreservedbw', (YLeaf(YType.int32, 'cdxQosCtrlUpReservedBW'), ['int'])),
                    ('cdxqosctrlupmaxvirtualbw', (YLeaf(YType.int32, 'cdxQosCtrlUpMaxVirtualBW'), ['int'])),
                ])
                self.ifindex = None
                self.cdxqosctrlupadmissionctrl = None
                self.cdxqosctrlupmaxrsvdbwpercent = None
                self.cdxqosctrlupadmissionrejects = None
                self.cdxqosctrlupreservedbw = None
                self.cdxqosctrlupmaxvirtualbw = None
                self._segment_path = lambda: "cdxQosCtrlUpEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxQosCtrlUpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxQosCtrlUpTable.CdxQosCtrlUpEntry, ['ifindex', 'cdxqosctrlupadmissionctrl', 'cdxqosctrlupmaxrsvdbwpercent', 'cdxqosctrlupadmissionrejects', 'cdxqosctrlupreservedbw', 'cdxqosctrlupmaxvirtualbw'], name, value)




    class CdxQosIfRateLimitTable(Entity):
        """
        This table describes the attributes of rate limiting for 
        schedulers in cable upstream and downstream interfaces that 
        support Quality of Service.  The rate limiting process is 
        to ensure the Quality of Service and fairness. 
        
        .. attribute:: cdxqosifratelimitentry
        
        	List of the rate limiting attributes for cable upstream and  downstream interfaces schedulers that support Quality of  Service. Entries in this table exist for each ifEntry with  ifType of docsCableUpstream(129) and docsCableDownstream(128)
        	**type**\: list of  		 :py:class:`CdxQosIfRateLimitEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxQosIfRateLimitTable, self).__init__()

            self.yang_name = "cdxQosIfRateLimitTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxQosIfRateLimitEntry", ("cdxqosifratelimitentry", CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry))])
            self._leafs = OrderedDict()

            self.cdxqosifratelimitentry = YList(self)
            self._segment_path = lambda: "cdxQosIfRateLimitTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxQosIfRateLimitTable, [], name, value)


        class CdxQosIfRateLimitEntry(Entity):
            """
            List of the rate limiting attributes for cable upstream and 
            downstream interfaces schedulers that support Quality of 
            Service. Entries in this table exist for each ifEntry with 
            ifType of docsCableUpstream(129) and docsCableDownstream(128).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxqosifratelimitalgm
            
            	To ensure fairness, the CMTS will throttle the rate for bandwidth  request (upstream)/packet sent (downstream) at which CMTS issues  grants(upstream) or allow packet to be send(downstream) such that  the flow never gets more than its provisioned peak rate in bps.   There are two directions for every Service Id (Sid) traffic\:  downstream and upstream. Each direction is called a service flow  here and assigned one token bucket with chosen algorithm.   The enumerations for the rate limiting algorithm are\:  noRateLimit(1)\: The rate limiting is disabled. No rate limiting.  oneSecBurst(2)\: Bursty 1 second token bucket algorithm.  carLike(3)    \: Average token usage (CAR\-like) algorithm   wtExPacketDiscard(4) \: Weighted excess packet discard algorithm.  shaping(5)\: token bucket algorithm with shaping  Upstream supports the following\:    No rate limiting (1),    Bursty 1 second token bucket algorithm(2),    Average token usage (CAR\-like) algorithm(3),   Token bucket algorithm with shaping(5).  Downstream supports the following\:   No rate limiting (1),    Bursty 1 second token bucket algorithm(2),   Average token usage (CAR\-like) algorithm(3),   Weighted excess packet discard algorithm(4), and   Token bucket algorithm with shaping(5).  Token bucket algorithm with shaping is the default algorithm for upstream if CMTS is in DOCSIS 1.0 mode or DOCSIS 1.1 mode.   Bursty 1 second token bucket algorithm is the  default algorithm for downstream if the CMTS is in DOCSIS 1.0 mode. If it is in DOCSIS 1.1 mode the default algorithm for downstream is  Token bucket algorithm with shaping .  Each algorithm is described as below\:   No rate limiting\:      The rate limiting process is disabled and no checking      against the maximum bandwidth allowed.     Bursty 1 second token bucket rate limiting algorithm\:      In this algorithm, at the start of every 1 second interval,      a service flow's token usage is reset to 0, and every time      the modem for that service flow sends a request (upstream) /      packet (downstream) the upstream/downstream bandwidth      token usage is incremented by the size of the      request/packet sent. As long as the service flow's bandwidth      token usage is less than the maximum bandwidth in bits      per second (peak rate limit) its QoS service class      allows, the request/packets will not be restricted.      Once the service flow has sent more than its peak rate in the      one second interval, it is prevented from sending more      data by rejecting request (upstream) or dropping      packets (downstream). This is expected to slow down     the higher layer sources. The token usage counter gets      reset to 0 after the 1 second interval has elapsed. The      modem for that service flow is free to send more data up to the      peak rate limit in the new 1 second interval that follows.      Average token usage (Cisco CAR like) algorithm\:      This algorithm maintains a continuous average of the      burst token usage of a service flow. There is no sudden      refilling of tokens every 1 second interval. Every time a      request/packet is to be handled, the scheduler tries to see      how much time has elapsed since last transmission, and      computes the number of tokens accumulated by this service flow      at its QoS class peak rate. If burst usage of the service flow      is less than tokens accumulated, the burst usage is reset to 0      and request/packet is forwarded. If the service flow has      accumulated fewer tokens than its burst usage, the burst usage      shows an outstanding balance usage after decrementing by the      tokens accumulated. In such cases, the request/packet is still      forwarded, provided the service flow's outstanding usage does      not exceed peak rate limit of its QoS class. If outstanding      burst usage exceeds the peak rate of the class, the service      flow is given some token credit up to a certain maximum credit      limit and the request/packet is forwarded. The request/packet      is dropped when outstanding usage exceeds peak rate and maximum      credit has been used up by this service flow. This algorithm      tracks long term average bandwidth usage of the service flow      and controls this average usage at the peak rate limit.    Weighted excess packet discard algorithm\:     This rate limiting algorithm is only available as an option      for downstream rate limiting. The algorithm is to maintain an      weighted exponential moving average of the loss rate of a      service flow over time. The loss rate, expressed in packets,      represents the number of packets that can be sent from this      service flow in a one second interval before a packet will      be dropped. At every one second interval, the loss rate gets      updated using the ratio between the flow peak rate (in bps)      in its QoS profile and the service flow actual usage (in bps).      If the service flow begins to send more than its peak rate      continuously, the number of packets it can send in an one      second interval before experiencing a drop will slowly keep      reducing until cable modem for that service flow slows down      as indicated by actual usage less or equal to the peak rate.     Token bucket algorithm with shaping\:      If there is no QoS class peak rate limit, forward the       request/packet without delay. If there is a QoS peak rate       limit, every time a request/packet is to be handled, the       scheduler determines the number of bandwidth tokens that this       service flow has accumulated over the elapsed time at its       QoS class peak rate and increments the tokens counter of the       service flow accordingly.  The scheduler limits the token       count to the maximum transmit burst (token bucket depth).        If token count is greater than the number of tokens required       to handle current request/packet, decrement token count by       size of request/packet and forwards the request/packet       without delay.  If token count is less than the size of       request/packet, compute the shaping delay time after       which the deficit number of tokens would be available. If       shaping delay time is less than the maximum shaping delay,       decrement tokens count by size of request/packet and       forward this request/packet with the shaping delay in the       shaping delay queue. When the delay time expires, the       request/packet is forwarded. If shaping delay time is       greater than the maximum shaping delay that the subsequent       shaper can handle, the request/packet is dropped. Users can      use cdxQosIfRateLimitShpMaxDelay to configure the the maximum       shaping delay and cdxQosIfRateLimitShpGranularity to       configure the shaping granularity.  
            	**type**\:  :py:class:`CdxQosIfRateLimitAlgm <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitAlgm>`
            
            	**config**\: False
            
            .. attribute:: cdxqosifratelimitexpwt
            
            	Weight for exponential moving average of loss rate for  weighted excess packet discard algorithm to maintain. The higher value of the weight makes the algorithm more sensitive to the recent bandwidth usage by the Sid.   The default value is 1 and whenever the rate limiting algorithm is changed to weighted excess packet discard  algorithm, this value will be reset to the default 1.  If the rate limiting algorithm is not weighted excess  packet discard algorithm, the value will be always the  default value 1. 
            	**type**\: int
            
            	**range:** 1..4
            
            	**config**\: False
            
            .. attribute:: cdxqosifratelimitshpmaxdelay
            
            	The maximum shaping delay in milliseconds. That is, the maximum  amount time of buffering the CMTS will allow for any rate exceeded  flow.  If the max buffering delay is large, the grants/packets of  the flow will be buffered for a longer period of time even though  the flow is rate exceeded. This means fewer chances of drops for such rate exceeded flow. However, too large a max shaping delay  can result is quick drainage of packet buffers at the CMTS, since  several packets will be in the shaping (delay) queue waiting for  their proper transmission time. Another important point to be noted  is that delaying a flows packets (especially TCP flows) for  extended periods of time is useless, since the higher protocol  layers may assume a packet loss after a certain amount of time.  The maximum shaping delay is only applied to rate limit algorithm\:  Token bucket algorithm with shaping.  If the rate limit  algorithm is not Token bucket algorithm with shaping, the  value is always na(1) which is not applicable.  If the token count is less than the size of request/packet, CMTS  computes the shaping delay time after which the deficit number of  tokens would be available. If the shaping delay time is greater  than the maximum shaping delay, the request/packet will be dropped.    The enumerations for maximum shaping delay are\:   na(1)\: maximum shaping delay is not applied to the current           rate limit algorithm  msec128(2)\: maximum shaping delay is 128 milliseconds    msec256(3)\: maximum shaping delay is 256 milliseconds   msec512(4)\: maximum shaping delay is 512 milliseconds  msec1024(5)\: maximum shaping delay is 1024 milliseconds   The downstream maximum shaping delay is configurable and the default value is msec128(2). Whenever the downstream rate  limit algorithm is changed to Token bucket algorithm with  shaping from other rate limit algorithm, the value will  be reset to the default value.   The upstream maximum shaping delay is not configurable and it  is read\-only value.  
            	**type**\:  :py:class:`CdxQosIfRateLimitShpMaxDelay <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitShpMaxDelay>`
            
            	**config**\: False
            
            .. attribute:: cdxqosifratelimitshpgranularity
            
            	The width in milliseconds of each element in shaping  delay queue, that is, the shaping granularity.  The shaping granularity is only applied to rate limit algorithm\: Token bucket algorithm with shaping. It  controls how accurately the algorithm quantizes the shaping  delay for a rate exceeded flow. If granularity is large, several  shaping delay values will all be quantized to the same element  in the queue resulting in less accurate rate shaping for the flows  in bits/sec. On the other hand, choosing too small granularity  causes more memory to be used for the shaper block, and also  can cost a bit more in runtime overhead.  If the rate limit algorithm is not Token bucket algorithm with  shaping, the value is always na(1) which is not applicable.  The enumerations for shaping granularity are\:   na(1)\: shaping granularity is not applied to the current           rate limit algorithm    msec1(2)\: shaping granularity in 1 milliseconds     msec2(3)\: shaping granularity in 2 milliseconds     msec4(4)\: shaping granularity in 4 milliseconds     msec8(5)\: shaping granularity in 8 milliseconds    msec16(6)\: shaping granularity in 16 milliseconds    The downstream shaping granularity is configurable and the default value is msec4(4). Whenever the downstream rate limit  algorithm is changed to Token bucket algorithm with shaping  from other rate limit algorithm, the value will be reset to the  default value.   The upstream shaping granularity is not configurable and  it is read\-only value.  
            	**type**\:  :py:class:`CdxQosIfRateLimitShpGranularity <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitShpGranularity>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry, self).__init__()

                self.yang_name = "cdxQosIfRateLimitEntry"
                self.yang_parent_name = "cdxQosIfRateLimitTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxqosifratelimitalgm', (YLeaf(YType.enumeration, 'cdxQosIfRateLimitAlgm'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitAlgm')])),
                    ('cdxqosifratelimitexpwt', (YLeaf(YType.int32, 'cdxQosIfRateLimitExpWt'), ['int'])),
                    ('cdxqosifratelimitshpmaxdelay', (YLeaf(YType.enumeration, 'cdxQosIfRateLimitShpMaxDelay'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitShpMaxDelay')])),
                    ('cdxqosifratelimitshpgranularity', (YLeaf(YType.enumeration, 'cdxQosIfRateLimitShpGranularity'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry.CdxQosIfRateLimitShpGranularity')])),
                ])
                self.ifindex = None
                self.cdxqosifratelimitalgm = None
                self.cdxqosifratelimitexpwt = None
                self.cdxqosifratelimitshpmaxdelay = None
                self.cdxqosifratelimitshpgranularity = None
                self._segment_path = lambda: "cdxQosIfRateLimitEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxQosIfRateLimitTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxQosIfRateLimitTable.CdxQosIfRateLimitEntry, ['ifindex', 'cdxqosifratelimitalgm', 'cdxqosifratelimitexpwt', 'cdxqosifratelimitshpmaxdelay', 'cdxqosifratelimitshpgranularity'], name, value)

            class CdxQosIfRateLimitAlgm(Enum):
                """
                CdxQosIfRateLimitAlgm (Enum Class)

                To ensure fairness, the CMTS will throttle the rate for bandwidth 

                request (upstream)/packet sent (downstream) at which CMTS issues 

                grants(upstream) or allow packet to be send(downstream) such that 

                the flow never gets more than its provisioned peak rate in bps. 

                There are two directions for every Service Id (Sid) traffic\: 

                downstream and upstream. Each direction is called a service flow 

                here and assigned one token bucket with chosen algorithm. 

                The enumerations for the rate limiting algorithm are\:

                 noRateLimit(1)\: The rate limiting is disabled. No rate limiting.

                 oneSecBurst(2)\: Bursty 1 second token bucket algorithm.

                 carLike(3)    \: Average token usage (CAR\-like) algorithm 

                 wtExPacketDiscard(4) \: Weighted excess packet discard algorithm.

                 shaping(5)\: token bucket algorithm with shaping

                Upstream supports the following\: 

                  No rate limiting (1), 

                  Bursty 1 second token bucket algorithm(2), 

                  Average token usage (CAR\-like) algorithm(3),

                  Token bucket algorithm with shaping(5).

                Downstream supports the following\:

                  No rate limiting (1), 

                  Bursty 1 second token bucket algorithm(2),

                  Average token usage (CAR\-like) algorithm(3),

                  Weighted excess packet discard algorithm(4), and

                  Token bucket algorithm with shaping(5).

                Token bucket algorithm with shaping is the

                default algorithm for upstream if CMTS is in DOCSIS 1.0 mode

                or DOCSIS 1.1 mode.

                Bursty 1 second token bucket algorithm is the 

                default algorithm for downstream if the CMTS is in

                DOCSIS 1.0 mode. If it is in DOCSIS 1.1 mode the default

                algorithm for downstream is  Token bucket algorithm with

                shaping .

                Each algorithm is described as below\:

                  No rate limiting\: 

                    The rate limiting process is disabled and no checking 

                    against the maximum bandwidth allowed. 

                  Bursty 1 second token bucket rate limiting algorithm\: 

                    In this algorithm, at the start of every 1 second interval, 

                    a service flow's token usage is reset to 0, and every time 

                    the modem for that service flow sends a request (upstream) / 

                    packet (downstream) the upstream/downstream bandwidth 

                    token usage is incremented by the size of the 

                    request/packet sent. As long as the service flow's bandwidth 

                    token usage is less than the maximum bandwidth in bits 

                    per second (peak rate limit) its QoS service class 

                    allows, the request/packets will not be restricted. 

                    Once the service flow has sent more than its peak rate in the 

                    one second interval, it is prevented from sending more 

                    data by rejecting request (upstream) or dropping 

                    packets (downstream). This is expected to slow down

                    the higher layer sources. The token usage counter gets 

                    reset to 0 after the 1 second interval has elapsed. The 

                    modem for that service flow is free to send more data up to the 

                    peak rate limit in the new 1 second interval that follows.  

                  Average token usage (Cisco CAR like) algorithm\: 

                    This algorithm maintains a continuous average of the 

                    burst token usage of a service flow. There is no sudden 

                    refilling of tokens every 1 second interval. Every time a 

                    request/packet is to be handled, the scheduler tries to see 

                    how much time has elapsed since last transmission, and 

                    computes the number of tokens accumulated by this service flow 

                    at its QoS class peak rate. If burst usage of the service flow 

                    is less than tokens accumulated, the burst usage is reset to 0 

                    and request/packet is forwarded. If the service flow has 

                    accumulated fewer tokens than its burst usage, the burst usage 

                    shows an outstanding balance usage after decrementing by the 

                    tokens accumulated. In such cases, the request/packet is still 

                    forwarded, provided the service flow's outstanding usage does 

                    not exceed peak rate limit of its QoS class. If outstanding 

                    burst usage exceeds the peak rate of the class, the service 

                    flow is given some token credit up to a certain maximum credit 

                    limit and the request/packet is forwarded. The request/packet 

                    is dropped when outstanding usage exceeds peak rate and maximum 

                    credit has been used up by this service flow. This algorithm 

                    tracks long term average bandwidth usage of the service flow 

                    and controls this average usage at the peak rate limit.

                  Weighted excess packet discard algorithm\:

                    This rate limiting algorithm is only available as an option 

                    for downstream rate limiting. The algorithm is to maintain an 

                    weighted exponential moving average of the loss rate of a 

                    service flow over time. The loss rate, expressed in packets, 

                    represents the number of packets that can be sent from this 

                    service flow in a one second interval before a packet will 

                    be dropped. At every one second interval, the loss rate gets 

                    updated using the ratio between the flow peak rate (in bps) 

                    in its QoS profile and the service flow actual usage (in bps). 

                    If the service flow begins to send more than its peak rate 

                    continuously, the number of packets it can send in an one 

                    second interval before experiencing a drop will slowly keep 

                    reducing until cable modem for that service flow slows down 

                    as indicated by actual usage less or equal to the peak rate. 

                  Token bucket algorithm with shaping\:

                     If there is no QoS class peak rate limit, forward the 

                     request/packet without delay. If there is a QoS peak rate 

                     limit, every time a request/packet is to be handled, the 

                     scheduler determines the number of bandwidth tokens that this 

                     service flow has accumulated over the elapsed time at its 

                     QoS class peak rate and increments the tokens counter of the 

                     service flow accordingly.  The scheduler limits the token 

                     count to the maximum transmit burst (token bucket depth).  

                     If token count is greater than the number of tokens required 

                     to handle current request/packet, decrement token count by 

                     size of request/packet and forwards the request/packet 

                     without delay.  If token count is less than the size of 

                     request/packet, compute the shaping delay time after 

                     which the deficit number of tokens would be available. If 

                     shaping delay time is less than the maximum shaping delay, 

                     decrement tokens count by size of request/packet and 

                     forward this request/packet with the shaping delay in the 

                     shaping delay queue. When the delay time expires, the 

                     request/packet is forwarded. If shaping delay time is 

                     greater than the maximum shaping delay that the subsequent 

                     shaper can handle, the request/packet is dropped. Users can

                     use cdxQosIfRateLimitShpMaxDelay to configure the the maximum 

                     shaping delay and cdxQosIfRateLimitShpGranularity to 

                     configure the shaping granularity.  

                .. data:: noRateLimit = 1

                .. data:: oneSecBurst = 2

                .. data:: carLike = 3

                .. data:: wtExPacketDiscard = 4

                .. data:: shaping = 5

                """

                noRateLimit = Enum.YLeaf(1, "noRateLimit")

                oneSecBurst = Enum.YLeaf(2, "oneSecBurst")

                carLike = Enum.YLeaf(3, "carLike")

                wtExPacketDiscard = Enum.YLeaf(4, "wtExPacketDiscard")

                shaping = Enum.YLeaf(5, "shaping")


            class CdxQosIfRateLimitShpGranularity(Enum):
                """
                CdxQosIfRateLimitShpGranularity (Enum Class)

                The width in milliseconds of each element in shaping 

                delay queue, that is, the shaping granularity.

                The shaping granularity is only applied to rate limit

                algorithm\: Token bucket algorithm with shaping. It 

                controls how accurately the algorithm quantizes the shaping 

                delay for a rate exceeded flow. If granularity is large, several 

                shaping delay values will all be quantized to the same element 

                in the queue resulting in less accurate rate shaping for the flows 

                in bits/sec. On the other hand, choosing too small granularity 

                causes more memory to be used for the shaper block, and also 

                can cost a bit more in runtime overhead.

                If the rate limit algorithm is not Token bucket algorithm with 

                shaping, the value is always na(1) which is not applicable.

                The enumerations for shaping granularity are\:

                  na(1)\: shaping granularity is not applied to the current 

                         rate limit algorithm

                   msec1(2)\: shaping granularity in 1 milliseconds 

                   msec2(3)\: shaping granularity in 2 milliseconds 

                   msec4(4)\: shaping granularity in 4 milliseconds 

                   msec8(5)\: shaping granularity in 8 milliseconds 

                  msec16(6)\: shaping granularity in 16 milliseconds  

                The downstream shaping granularity is configurable and the

                default value is msec4(4). Whenever the downstream rate limit 

                algorithm is changed to Token bucket algorithm with shaping 

                from other rate limit algorithm, the value will be reset to the 

                default value. 

                The upstream shaping granularity is not configurable and 

                it is read\-only value.  

                .. data:: na = 1

                .. data:: msec1 = 2

                .. data:: msec2 = 3

                .. data:: msec4 = 4

                .. data:: msec8 = 5

                .. data:: msec16 = 6

                """

                na = Enum.YLeaf(1, "na")

                msec1 = Enum.YLeaf(2, "msec1")

                msec2 = Enum.YLeaf(3, "msec2")

                msec4 = Enum.YLeaf(4, "msec4")

                msec8 = Enum.YLeaf(5, "msec8")

                msec16 = Enum.YLeaf(6, "msec16")


            class CdxQosIfRateLimitShpMaxDelay(Enum):
                """
                CdxQosIfRateLimitShpMaxDelay (Enum Class)

                The maximum shaping delay in milliseconds. That is, the maximum 

                amount time of buffering the CMTS will allow for any rate exceeded 

                flow.  If the max buffering delay is large, the grants/packets of 

                the flow will be buffered for a longer period of time even though 

                the flow is rate exceeded. This means fewer chances of drops for

                such rate exceeded flow. However, too large a max shaping delay 

                can result is quick drainage of packet buffers at the CMTS, since 

                several packets will be in the shaping (delay) queue waiting for 

                their proper transmission time. Another important point to be noted 

                is that delaying a flows packets (especially TCP flows) for 

                extended periods of time is useless, since the higher protocol 

                layers may assume a packet loss after a certain amount of time.

                The maximum shaping delay is only applied to rate limit algorithm\: 

                Token bucket algorithm with shaping.  If the rate limit 

                algorithm is not Token bucket algorithm with shaping, the 

                value is always na(1) which is not applicable.

                If the token count is less than the size of request/packet, CMTS 

                computes the shaping delay time after which the deficit number of 

                tokens would be available. If the shaping delay time is greater 

                than the maximum shaping delay, the request/packet will be dropped.  

                The enumerations for maximum shaping delay are\:

                  na(1)\: maximum shaping delay is not applied to the current 

                         rate limit algorithm

                 msec128(2)\: maximum shaping delay is 128 milliseconds  

                 msec256(3)\: maximum shaping delay is 256 milliseconds 

                 msec512(4)\: maximum shaping delay is 512 milliseconds 

                msec1024(5)\: maximum shaping delay is 1024 milliseconds 

                The downstream maximum shaping delay is configurable and the

                default value is msec128(2). Whenever the downstream rate 

                limit algorithm is changed to Token bucket algorithm with 

                shaping from other rate limit algorithm, the value will 

                be reset to the default value. 

                The upstream maximum shaping delay is not configurable and it 

                is read\-only value.  

                .. data:: na = 1

                .. data:: msec128 = 2

                .. data:: msec256 = 3

                .. data:: msec512 = 4

                .. data:: msec1024 = 5

                """

                na = Enum.YLeaf(1, "na")

                msec128 = Enum.YLeaf(2, "msec128")

                msec256 = Enum.YLeaf(3, "msec256")

                msec512 = Enum.YLeaf(4, "msec512")

                msec1024 = Enum.YLeaf(5, "msec1024")





    class CdxCmtsServiceExtTable(Entity):
        """
        The list contains the additional attributes of a single Service
        ID that provided by docsIfCmtsServiceEntry. 
        
        .. attribute:: cdxcmtsserviceextentry
        
        	Additional objects for docsIfCmtsServiceTable entry including  downstream traffic statistics and excess counts against the  Quality of Service limits for each Service ID. From DOCSIS 1.1 onwards statistics are maintained for each  Service Flow(instead of the Service ID) in the DOCS\-QOS\-MIB  in docsQosServiceFlowStatsTable objects. For Cable modems not running in DOCSIS 1.0 mode, the objects   cdxIfCmtsServiceOutOctets and cdxIfCmtsServiceOutPackets will only support primary service flow. 
        	**type**\: list of  		 :py:class:`CdxCmtsServiceExtEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsServiceExtTable.CdxCmtsServiceExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsServiceExtTable, self).__init__()

            self.yang_name = "cdxCmtsServiceExtTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsServiceExtEntry", ("cdxcmtsserviceextentry", CISCODOCSEXTMIB.CdxCmtsServiceExtTable.CdxCmtsServiceExtEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtsserviceextentry = YList(self)
            self._segment_path = lambda: "cdxCmtsServiceExtTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsServiceExtTable, [], name, value)


        class CdxCmtsServiceExtEntry(Entity):
            """
            Additional objects for docsIfCmtsServiceTable entry including 
            downstream traffic statistics and excess counts against the 
            Quality of Service limits for each Service ID.
            From DOCSIS 1.1 onwards statistics are maintained for each 
            Service Flow(instead of the Service ID) in the DOCS\-QOS\-MIB 
            in docsQosServiceFlowStatsTable objects. For Cable modems
            not running in DOCSIS 1.0 mode, the objects  
            cdxIfCmtsServiceOutOctets and cdxIfCmtsServiceOutPackets
            will only support primary service flow. 
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: docsifcmtsserviceid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..16383
            
            	**refers to**\:  :py:class:`docsifcmtsserviceid <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsserviceoutoctets
            
            	The cumulative number of Packet Data octets sent for this  Service ID. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsserviceoutpackets
            
            	The cumulative number of Packet data packets sent for this  Service ID. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxqosmaxupbwexcessrequests
            
            	The number of upstream bandwidth requests which exceeds the maximum upstream bandwidth allowed for a service defined  in the Quality of Service profile associated with this Sid.  The request which exceeds the maximum upstream bandwidth  allowed will be rejected by the upstream's rate limiting  process using one of the rate limiting algorithm.   Note that the value of this counter cannot be directly used  to know the number of upstream packets that got dropped at  the cable modem.  A single upstream packet drop of a modem  can result in up to 16 increments in this counter, since the  modem keeps retrying and keeps getting bandwidth request  drops at CMTS if it has consumed its peak rate.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxqosmaxdownbwexcesspackets
            
            	The number of downstream bandwidth packets which exceeds the maximum downstream bandwidth allowed for a service defined in the Quality of Service profile associated with this Sid.  The packet which exceeds the maximum downstream bandwidth  allowed will be dropped by the downstream's rate limiting  process using one of the rate limiting algorithm. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsservicehcinoctets
            
            	The cumulative number of Packet Data octets received on this Service ID. The count does not include the size of the Cable MAC header. This object is a 64\-bit version of docsIfCmtsServiceInOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsservicehcinpackets
            
            	The cumulative number of Packet Data packets received on this Service ID. This object is a 64\-bit version of docsIfCmtsServiceInPackets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsservicehcoutoctets
            
            	The cumulative number of Packet Data octets sent for this Service ID. This object is a 64\-bit version of cdxIfCmtsServiceOutOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cdxifcmtsservicehcoutpackets
            
            	The cumulative number of Packet Data packets sent for this Service ID. This object is a 64\-bit version of cdxIfCmtsServiceOutPackets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsServiceExtTable.CdxCmtsServiceExtEntry, self).__init__()

                self.yang_name = "cdxCmtsServiceExtEntry"
                self.yang_parent_name = "cdxCmtsServiceExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsifcmtsserviceid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtsserviceid', (YLeaf(YType.str, 'docsIfCmtsServiceId'), ['int'])),
                    ('cdxifcmtsserviceoutoctets', (YLeaf(YType.uint32, 'cdxIfCmtsServiceOutOctets'), ['int'])),
                    ('cdxifcmtsserviceoutpackets', (YLeaf(YType.uint32, 'cdxIfCmtsServiceOutPackets'), ['int'])),
                    ('cdxqosmaxupbwexcessrequests', (YLeaf(YType.uint32, 'cdxQosMaxUpBWExcessRequests'), ['int'])),
                    ('cdxqosmaxdownbwexcesspackets', (YLeaf(YType.uint32, 'cdxQosMaxDownBWExcessPackets'), ['int'])),
                    ('cdxifcmtsservicehcinoctets', (YLeaf(YType.uint64, 'cdxIfCmtsServiceHCInOctets'), ['int'])),
                    ('cdxifcmtsservicehcinpackets', (YLeaf(YType.uint64, 'cdxIfCmtsServiceHCInPackets'), ['int'])),
                    ('cdxifcmtsservicehcoutoctets', (YLeaf(YType.uint64, 'cdxIfCmtsServiceHCOutOctets'), ['int'])),
                    ('cdxifcmtsservicehcoutpackets', (YLeaf(YType.uint64, 'cdxIfCmtsServiceHCOutPackets'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtsserviceid = None
                self.cdxifcmtsserviceoutoctets = None
                self.cdxifcmtsserviceoutpackets = None
                self.cdxqosmaxupbwexcessrequests = None
                self.cdxqosmaxdownbwexcesspackets = None
                self.cdxifcmtsservicehcinoctets = None
                self.cdxifcmtsservicehcinpackets = None
                self.cdxifcmtsservicehcoutoctets = None
                self.cdxifcmtsservicehcoutpackets = None
                self._segment_path = lambda: "cdxCmtsServiceExtEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIfCmtsServiceId='" + str(self.docsifcmtsserviceid) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsServiceExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsServiceExtTable.CdxCmtsServiceExtEntry, ['ifindex', 'docsifcmtsserviceid', 'cdxifcmtsserviceoutoctets', 'cdxifcmtsserviceoutpackets', 'cdxqosmaxupbwexcessrequests', 'cdxqosmaxdownbwexcesspackets', 'cdxifcmtsservicehcinoctets', 'cdxifcmtsservicehcinpackets', 'cdxifcmtsservicehcoutoctets', 'cdxifcmtsservicehcoutpackets'], name, value)




    class CdxUpInfoElemStatsTable(Entity):
        """
        The table contains the attributes of a particular 
        Information Element type for each instance of the MAC 
        scheduler. It is indexed by upstream ifIndex. An Entry
        exists for each ifEntry with ifType of docsCableUpstream(129)
        Since each upstream has an instance of a MAC Scheduler so 
        this table has the per MAC scheduler slot information on a
        per Information Element basis. 
        
        .. attribute:: cdxupinfoelemstatsentry
        
        	The list of statistics for a type of Information Element(IE) which defines the allowed usage for a range of upstream mini slots. One entry exists for each Information Element (IE) in a upstream which ifType is docsCableUpstream (12)
        	**type**\: list of  		 :py:class:`CdxUpInfoElemStatsEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxUpInfoElemStatsTable, self).__init__()

            self.yang_name = "cdxUpInfoElemStatsTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxUpInfoElemStatsEntry", ("cdxupinfoelemstatsentry", CISCODOCSEXTMIB.CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry))])
            self._leafs = OrderedDict()

            self.cdxupinfoelemstatsentry = YList(self)
            self._segment_path = lambda: "cdxUpInfoElemStatsTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxUpInfoElemStatsTable, [], name, value)


        class CdxUpInfoElemStatsEntry(Entity):
            """
            The list of statistics for a type of Information Element(IE)
            which defines the allowed usage for a range of upstream mini
            slots. One entry exists for each Information Element (IE) in
            a upstream which ifType is docsCableUpstream (12).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxupinfoelemstatsnamecode  (key)
            
            	This entry describes the Information Element (IE) type. Enumerations are \: reqIE(1)          \: Request Information Element,                     The request Information Element provides                     an upstream interval in which a CM can                     request the CMTS for bandwidth on the                      upstream channel. reqOrDataIE(2)    \: Request/Data Information Element,                     The Request/data Information Element                      provides an upstream interval in which                      request may be made by the CM to the                      CMTS for bandwidth or short data                      packets may be transmitted on the                     upstream channel. initMtnIE(3)      \: Initial Maintenance Information Element,                     The Initial Maintenance Information                      Element provides an interval in which                      new stations may join the network. stnMtnIE(4)       \: Station Maintenance Information Element,                     The Station Maintenance Information                      Element provides an interval in which                      stations are expected to perform some                      aspect of routine network maintenance ,                      such as ranging or power adjustment. shortGrantIE(5)   \: Short Data Grant Information Element,                     Short data grant Information Element                     provides the CM an opportunity to                      transmit one or more upstream PDU's.                     Short data grants are used with                      intervals equal to or less than the                      maximum burst size for the usage                      specified in the Upstream Channel                      Descriptor. longGrantIE(6)    \: Long Data Grant Information Element,                     The long data grant Information Element                     also provides the CM an opportunity to                     transmit one or more upstream PDU's.                     All long data grant Information Elements                     must have a larger number of mini\-slots                     than that defined for a short data grant                     Information Element profile defined in                     the Upstream Channel Descriptor. 
            	**type**\:  :py:class:`CdxUpInfoElemStatsNameCode <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry.CdxUpInfoElemStatsNameCode>`
            
            	**config**\: False
            
            .. attribute:: cdxupinfoelemstatsietype
            
            	The current number of mini\-slots used for the Information  Element type. The value is only a snapshot since the  current number of mini\-slots of this IE type could be changing rapidly. 
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry, self).__init__()

                self.yang_name = "cdxUpInfoElemStatsEntry"
                self.yang_parent_name = "cdxUpInfoElemStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxupinfoelemstatsnamecode']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxupinfoelemstatsnamecode', (YLeaf(YType.enumeration, 'cdxUpInfoElemStatsNameCode'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry.CdxUpInfoElemStatsNameCode')])),
                    ('cdxupinfoelemstatsietype', (YLeaf(YType.int32, 'cdxUpInfoElemStatsIEType'), ['int'])),
                ])
                self.ifindex = None
                self.cdxupinfoelemstatsnamecode = None
                self.cdxupinfoelemstatsietype = None
                self._segment_path = lambda: "cdxUpInfoElemStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxUpInfoElemStatsNameCode='" + str(self.cdxupinfoelemstatsnamecode) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxUpInfoElemStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxUpInfoElemStatsTable.CdxUpInfoElemStatsEntry, ['ifindex', 'cdxupinfoelemstatsnamecode', 'cdxupinfoelemstatsietype'], name, value)

            class CdxUpInfoElemStatsNameCode(Enum):
                """
                CdxUpInfoElemStatsNameCode (Enum Class)

                This entry describes the Information Element (IE) type.

                Enumerations are \:

                reqIE(1)          \: Request Information Element,

                                    The request Information Element provides

                                    an upstream interval in which a CM can

                                    request the CMTS for bandwidth on the 

                                    upstream channel.

                reqOrDataIE(2)    \: Request/Data Information Element,

                                    The Request/data Information Element 

                                    provides an upstream interval in which 

                                    request may be made by the CM to the 

                                    CMTS for bandwidth or short data 

                                    packets may be transmitted on the

                                    upstream channel.

                initMtnIE(3)      \: Initial Maintenance Information Element,

                                    The Initial Maintenance Information 

                                    Element provides an interval in which 

                                    new stations may join the network.

                stnMtnIE(4)       \: Station Maintenance Information Element,

                                    The Station Maintenance Information 

                                    Element provides an interval in which 

                                    stations are expected to perform some 

                                    aspect of routine network maintenance , 

                                    such as ranging or power adjustment.

                shortGrantIE(5)   \: Short Data Grant Information Element,

                                    Short data grant Information Element

                                    provides the CM an opportunity to 

                                    transmit one or more upstream PDU's.

                                    Short data grants are used with 

                                    intervals equal to or less than the 

                                    maximum burst size for the usage 

                                    specified in the Upstream Channel 

                                    Descriptor.

                longGrantIE(6)    \: Long Data Grant Information Element,

                                    The long data grant Information Element

                                    also provides the CM an opportunity to

                                    transmit one or more upstream PDU's.

                                    All long data grant Information Elements

                                    must have a larger number of mini\-slots

                                    than that defined for a short data grant

                                    Information Element profile defined in

                                    the Upstream Channel Descriptor. 

                .. data:: reqIE = 1

                .. data:: reqOrDataIE = 2

                .. data:: initMtnIE = 3

                .. data:: stnMtnIE = 4

                .. data:: shortGrantIE = 5

                .. data:: longGrantIE = 6

                """

                reqIE = Enum.YLeaf(1, "reqIE")

                reqOrDataIE = Enum.YLeaf(2, "reqOrDataIE")

                initMtnIE = Enum.YLeaf(3, "initMtnIE")

                stnMtnIE = Enum.YLeaf(4, "stnMtnIE")

                shortGrantIE = Enum.YLeaf(5, "shortGrantIE")

                longGrantIE = Enum.YLeaf(6, "longGrantIE")





    class CdxBWQueueTable(Entity):
        """
        This table describes the attributes of queues  
        in cable interfaces schedulers that support 
        Quality of Service.
        
        .. attribute:: cdxbwqueueentry
        
        	The list of queue attributes in cable upstream and downstream interfaces schedulers that supports Quality of Service.  Entries in this table exist for each ifEntry with ifType of  docsCableUpstream(129) and docsCableDownstream(128). 
        	**type**\: list of  		 :py:class:`CdxBWQueueEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxBWQueueTable, self).__init__()

            self.yang_name = "cdxBWQueueTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxBWQueueEntry", ("cdxbwqueueentry", CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry))])
            self._leafs = OrderedDict()

            self.cdxbwqueueentry = YList(self)
            self._segment_path = lambda: "cdxBWQueueTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxBWQueueTable, [], name, value)


        class CdxBWQueueEntry(Entity):
            """
            The list of queue attributes in cable upstream and downstream
            interfaces schedulers that supports Quality of Service. 
            Entries in this table exist for each ifEntry with ifType of 
            docsCableUpstream(129) and docsCableDownstream(128). 
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuenamecode  (key)
            
            	The name code for the queue.  cirQ \:CIR queue. The queue is for Committed Information Rate        (CIR) type of service which serves Service IDs which       have minimum guaranteed rate in its QoS profile.       It is applicable if CMTS is running is either of        DOCSIS 1.0 or 1.1 modes.For DOCSIS 1.1 it has        priority 8.                   tbeQ \:TBE Queue.The queue is for TIERED BEST EFFORT type        service which serves Service IDs which does not have        minimum guaranteed rate in its QoS profile. It is        only applicable if CMTS is running in DOCSIS 1.0       mode.  p0BEGrantQ\-p7BEGrantQ \: BEST EFFORT Queue       The queues p0BEGrantQ to P7BEGrantQ are for TIERED        BEST EFFORT type service which serves Service IDs        which do not have minimum guaranteed rate specified       in the QoS parameters. P0 has lowest priority and P7       has highest.Best Effort type is purely handled with        prioritization in FIFO's and hence demands more        number of queues. These queues are applicable only if       CMTS is running under mode DOCSIS 1.1.                               rngPollQ \: RngPoll queue.       The queue is for the ranging SID's.It has the highest       priority. This queue information is only provided if       CMTS is running under mode DOCSIS 1.1. 
            	**type**\:  :py:class:`CdxBWQueueNameCode <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry.CdxBWQueueNameCode>`
            
            	**config**\: False
            
            .. attribute:: cdxbwqueueorder
            
            	The relative order of this queue to the other queues within the  cable interface. The smaller number has higher order. That is, 0 is the highest order and 10 is the lowest order.  The  scheduler will serve the requests in higher order queue up to  the number of requests defined in cdxBWQueueNumServedBeforeYield before serving requests in the next higher order queue.    If there are n queues on this interface, the queue order will  be 0 to n\-1 and maximum number of requests defined as  cdxBWQueueNumServedBeforeYield in order 0 queue will be served  before the requests in order 1 queue to be served. 
            	**type**\: int
            
            	**range:** 0..10
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuenumservedbeforeyield
            
            	The maximum number of requests/packets the scheduler can  serve before yielding to another queue. The value 0 means all  requests must be served before yielding to another queue. The  range is 0\-50 for DOCSIS 1.0 and for DOCSIS 1.1 it is 0\-64. 
            	**type**\: int
            
            	**range:** 0..64
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuetype
            
            	The queuing type which decides the position of a request/packet within the queue.   unknown \: queue type unknown.    other   \: not fifo, and not priority.   fifo    \: first in first out.   priority\: each bandwidth request has a priority and the              position of the request within the queue depends              on its priority.   For DOCSIS1.1 all the priority queues are fifo queues. 
            	**type**\:  :py:class:`CdxBWQueueType <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry.CdxBWQueueType>`
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuemaxdepth
            
            	The maximum number of requests/packets which the queue can  support.The range is 0\-50 for DOCSIS1.0 and for DOCSIS1.1 it is 0\-64. 
            	**type**\: int
            
            	**range:** 0..64
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuedepth
            
            	The current number of requests/packets in the queue. The range is 0\-50 for DOCSIS1.0 and for DOCSIS1.1 it is 0\-64. 
            	**type**\: int
            
            	**range:** 0..64
            
            	**config**\: False
            
            .. attribute:: cdxbwqueuediscards
            
            	The number of requests/packets discarded because of queue overflow (queue depth > queue maximum depth). 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry, self).__init__()

                self.yang_name = "cdxBWQueueEntry"
                self.yang_parent_name = "cdxBWQueueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxbwqueuenamecode']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxbwqueuenamecode', (YLeaf(YType.enumeration, 'cdxBWQueueNameCode'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxBWQueueTable.CdxBWQueueEntry.CdxBWQueueNameCode')])),
                    ('cdxbwqueueorder', (YLeaf(YType.int32, 'cdxBWQueueOrder'), ['int'])),
                    ('cdxbwqueuenumservedbeforeyield', (YLeaf(YType.int32, 'cdxBWQueueNumServedBeforeYield'), ['int'])),
                    ('cdxbwqueuetype', (YLeaf(YType.enumeration, 'cdxBWQueueType'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxBWQueueTable.CdxBWQueueEntry.CdxBWQueueType')])),
                    ('cdxbwqueuemaxdepth', (YLeaf(YType.int32, 'cdxBWQueueMaxDepth'), ['int'])),
                    ('cdxbwqueuedepth', (YLeaf(YType.int32, 'cdxBWQueueDepth'), ['int'])),
                    ('cdxbwqueuediscards', (YLeaf(YType.uint32, 'cdxBWQueueDiscards'), ['int'])),
                ])
                self.ifindex = None
                self.cdxbwqueuenamecode = None
                self.cdxbwqueueorder = None
                self.cdxbwqueuenumservedbeforeyield = None
                self.cdxbwqueuetype = None
                self.cdxbwqueuemaxdepth = None
                self.cdxbwqueuedepth = None
                self.cdxbwqueuediscards = None
                self._segment_path = lambda: "cdxBWQueueEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxBWQueueNameCode='" + str(self.cdxbwqueuenamecode) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxBWQueueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxBWQueueTable.CdxBWQueueEntry, ['ifindex', 'cdxbwqueuenamecode', 'cdxbwqueueorder', 'cdxbwqueuenumservedbeforeyield', 'cdxbwqueuetype', 'cdxbwqueuemaxdepth', 'cdxbwqueuedepth', 'cdxbwqueuediscards'], name, value)

            class CdxBWQueueNameCode(Enum):
                """
                CdxBWQueueNameCode (Enum Class)

                The name code for the queue.

                cirQ \:CIR queue. The queue is for Committed Information Rate 

                      (CIR) type of service which serves Service IDs which

                      have minimum guaranteed rate in its QoS profile.

                      It is applicable if CMTS is running is either of 

                      DOCSIS 1.0 or 1.1 modes.For DOCSIS 1.1 it has 

                      priority 8.

                tbeQ \:TBE Queue.The queue is for TIERED BEST EFFORT type 

                      service which serves Service IDs which does not have 

                      minimum guaranteed rate in its QoS profile. It is 

                      only applicable if CMTS is running in DOCSIS 1.0

                      mode.

                p0BEGrantQ\-p7BEGrantQ \: BEST EFFORT Queue

                      The queues p0BEGrantQ to P7BEGrantQ are for TIERED 

                      BEST EFFORT type service which serves Service IDs 

                      which do not have minimum guaranteed rate specified

                      in the QoS parameters. P0 has lowest priority and P7

                      has highest.Best Effort type is purely handled with 

                      prioritization in FIFO's and hence demands more 

                      number of queues. These queues are applicable only if

                      CMTS is running under mode DOCSIS 1.1.

                rngPollQ \: RngPoll queue.

                      The queue is for the ranging SID's.It has the highest

                      priority. This queue information is only provided if

                      CMTS is running under mode DOCSIS 1.1. 

                .. data:: cirQ = 1

                .. data:: tbeQ = 2

                .. data:: p0BEGrantQ = 3

                .. data:: p1BEGrantQ = 4

                .. data:: p2BEGrantQ = 5

                .. data:: p3BEGrantQ = 6

                .. data:: p4BEGrantQ = 7

                .. data:: p5BEGrantQ = 8

                .. data:: p6BEGrantQ = 9

                .. data:: p7BEGrantQ = 10

                .. data:: rngPollQ = 11

                """

                cirQ = Enum.YLeaf(1, "cirQ")

                tbeQ = Enum.YLeaf(2, "tbeQ")

                p0BEGrantQ = Enum.YLeaf(3, "p0BEGrantQ")

                p1BEGrantQ = Enum.YLeaf(4, "p1BEGrantQ")

                p2BEGrantQ = Enum.YLeaf(5, "p2BEGrantQ")

                p3BEGrantQ = Enum.YLeaf(6, "p3BEGrantQ")

                p4BEGrantQ = Enum.YLeaf(7, "p4BEGrantQ")

                p5BEGrantQ = Enum.YLeaf(8, "p5BEGrantQ")

                p6BEGrantQ = Enum.YLeaf(9, "p6BEGrantQ")

                p7BEGrantQ = Enum.YLeaf(10, "p7BEGrantQ")

                rngPollQ = Enum.YLeaf(11, "rngPollQ")


            class CdxBWQueueType(Enum):
                """
                CdxBWQueueType (Enum Class)

                The queuing type which decides the position of a request/packet

                within the queue.

                  unknown \: queue type unknown. 

                  other   \: not fifo, and not priority.

                  fifo    \: first in first out.

                  priority\: each bandwidth request has a priority and the 

                            position of the request within the queue depends 

                            on its priority.

                  For DOCSIS1.1 all the priority queues are fifo queues. 

                .. data:: unknown = 1

                .. data:: other = 2

                .. data:: fifo = 3

                .. data:: priority = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                other = Enum.YLeaf(2, "other")

                fifo = Enum.YLeaf(3, "fifo")

                priority = Enum.YLeaf(4, "priority")





    class CdxCmCpeTable(Entity):
        """
        This table contains information about cable modems (CM) or 
        Customer Premises Equipments (CPE). 
        
        .. attribute:: cdxcmcpeentry
        
        	The list contains information for a cable modem (CM) or a Customer Premises Equipment (CPE). An entry exist for  each cable modem supported by CMTS and each Customer Premises  Equipment connected to a cable modem supported by CMTS. 
        	**type**\: list of  		 :py:class:`CdxCmCpeEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmCpeTable.CdxCmCpeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmCpeTable, self).__init__()

            self.yang_name = "cdxCmCpeTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmCpeEntry", ("cdxcmcpeentry", CISCODOCSEXTMIB.CdxCmCpeTable.CdxCmCpeEntry))])
            self._leafs = OrderedDict()

            self.cdxcmcpeentry = YList(self)
            self._segment_path = lambda: "cdxCmCpeTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmCpeTable, [], name, value)


        class CdxCmCpeEntry(Entity):
            """
            The list contains information for a cable modem (CM) or a
            Customer Premises Equipment (CPE). An entry exist for 
            each cable modem supported by CMTS and each Customer Premises 
            Equipment connected to a cable modem supported by CMTS. 
            
            .. attribute:: cdxcmcpemacaddress  (key)
            
            	The Mac address to identify a cable modem or a Customer  Premises Equipment. 
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcmcpetype
            
            	Indicate this entry is for cable modem or Customer Premises  Equipment.  The enumerations are\:   cm(1)\: cable modem  cpe(2)\: Customer Premises Equipment 
            	**type**\:  :py:class:`CdxCmCpeType <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmCpeTable.CdxCmCpeEntry.CdxCmCpeType>`
            
            	**config**\: False
            
            .. attribute:: cdxcmcpeipaddress
            
            	Ip address of the cable modem or Customer Premises Equipment. 
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: cdxcmcpeifindex
            
            	The CMTS cable MAC interface index (ifType of  docsCableMaclayer(127)) that cable modem or Customer Premises  Equipment connects to.    Use cdxCmCpeIfIndex and cdxCmCpeCmtsServiceId to identify an  entry in docsIfCmtsServiceTable.  
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmcpecmtsserviceid
            
            	The cable modem's primary Service ID if the type is cm.  The primary Service ID for the CM which the CPE connects if the  type is cpe.  Use cdxCmCpeIfIndex and cdxCmCpeCmtsServiceId to identify an  entry in docsIfCmtsServiceTable.  
            	**type**\: int
            
            	**range:** 1..16383
            
            	**config**\: False
            
            .. attribute:: cdxcmcpecmstatusindex
            
            	Pointer to an entry in docsIfCmtsCmStatusTable identifying  status of the CM (which the CPE connects to.) 
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmcpeaccessgroup
            
            	ASCII text to identify the Access Group for a CM or CPE.  Access Group is to filter the upstream traffic for that CM or CPE.  
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdxcmcperesetnow
            
            	Setting this object to true(1) causes the device to  reset.  Reading this object always returns false(2).  For cdxCmCpeType value cm(1),  CMTS removes the  CM from the Station Maintenance List and would cause  the CM to reset its interface.  For cdxCmCpeType value cpe(2), CMTS removes the  CPE's MAC address from the internal address table.   It then rediscovers and associates the CPE with the  correct CM during the next DHCP lease cycle.  By resetting  the CPE, the user can replace an existing CPE or change  its network interface card (NIC)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxcmcpedeletenow
            
            	Setting this object to true(1) causes the CM/CPE to be deleted.  Reading this object always returns false(2).  For cdxCmCpeType value cm(1),  CMTS delete CM from  its interface.  For cdxCmCpeType value cpe(2), CMTS delete CPE from  its associated CM
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmCpeTable.CdxCmCpeEntry, self).__init__()

                self.yang_name = "cdxCmCpeEntry"
                self.yang_parent_name = "cdxCmCpeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxcmcpemacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxcmcpemacaddress', (YLeaf(YType.str, 'cdxCmCpeMacAddress'), ['str'])),
                    ('cdxcmcpetype', (YLeaf(YType.enumeration, 'cdxCmCpeType'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmCpeTable.CdxCmCpeEntry.CdxCmCpeType')])),
                    ('cdxcmcpeipaddress', (YLeaf(YType.str, 'cdxCmCpeIpAddress'), ['str'])),
                    ('cdxcmcpeifindex', (YLeaf(YType.int32, 'cdxCmCpeIfIndex'), ['int'])),
                    ('cdxcmcpecmtsserviceid', (YLeaf(YType.int32, 'cdxCmCpeCmtsServiceId'), ['int'])),
                    ('cdxcmcpecmstatusindex', (YLeaf(YType.int32, 'cdxCmCpeCmStatusIndex'), ['int'])),
                    ('cdxcmcpeaccessgroup', (YLeaf(YType.str, 'cdxCmCpeAccessGroup'), ['str'])),
                    ('cdxcmcperesetnow', (YLeaf(YType.boolean, 'cdxCmCpeResetNow'), ['bool'])),
                    ('cdxcmcpedeletenow', (YLeaf(YType.boolean, 'cdxCmCpeDeleteNow'), ['bool'])),
                ])
                self.cdxcmcpemacaddress = None
                self.cdxcmcpetype = None
                self.cdxcmcpeipaddress = None
                self.cdxcmcpeifindex = None
                self.cdxcmcpecmtsserviceid = None
                self.cdxcmcpecmstatusindex = None
                self.cdxcmcpeaccessgroup = None
                self.cdxcmcperesetnow = None
                self.cdxcmcpedeletenow = None
                self._segment_path = lambda: "cdxCmCpeEntry" + "[cdxCmCpeMacAddress='" + str(self.cdxcmcpemacaddress) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmCpeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmCpeTable.CdxCmCpeEntry, ['cdxcmcpemacaddress', 'cdxcmcpetype', 'cdxcmcpeipaddress', 'cdxcmcpeifindex', 'cdxcmcpecmtsserviceid', 'cdxcmcpecmstatusindex', 'cdxcmcpeaccessgroup', 'cdxcmcperesetnow', 'cdxcmcpedeletenow'], name, value)

            class CdxCmCpeType(Enum):
                """
                CdxCmCpeType (Enum Class)

                Indicate this entry is for cable modem or Customer Premises 

                Equipment.  The enumerations are\: 

                 cm(1)\: cable modem

                 cpe(2)\: Customer Premises Equipment 

                .. data:: cm = 1

                .. data:: cpe = 2

                """

                cm = Enum.YLeaf(1, "cm")

                cpe = Enum.YLeaf(2, "cpe")





    class CdxCmtsCmStatusExtTable(Entity):
        """
        The list contains the additional CM status information. 
        
        .. attribute:: cdxcmtscmstatusextentry
        
        	Additional objects for docsIfCmtsCmStatusTable entry. 
        	**type**\: list of  		 :py:class:`CdxCmtsCmStatusExtEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable, self).__init__()

            self.yang_name = "cdxCmtsCmStatusExtTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsCmStatusExtEntry", ("cdxcmtscmstatusextentry", CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtscmstatusextentry = YList(self)
            self._segment_path = lambda: "cdxCmtsCmStatusExtTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable, [], name, value)


        class CdxCmtsCmStatusExtEntry(Entity):
            """
            Additional objects for docsIfCmtsCmStatusTable entry. 
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmstatusvalue
            
            	Current Cable Modem connectivity state. The object extends  states in docsIfCmtsCmStatusValue in more details.   The enumerations are\: offline(1)                \: modem considered offline. others(2)                 \: states is in                              docsIfCmtsCmStatusValue. initRangingRcvd(3)        \: modem sent initial ranging. initDhcpReqRcvd(4)        \: dhcp request received. onlineNetAccessDisabled(5)\: modem registered, but network                                 access for the CM is disabled. onlineKekAssigned(6)      \: modem registered, BPI enabled                             and KEK assigned. onlineTekAssigned(7)      \: modem registered, BPI enabled                             and TEK assigned. rejectBadMic(8)           \: modem did attempt to register but                             registration was refused due to                             bad mic. rejectBadCos(9)           \: modem did attempt to register but                             registration was refused due to                             bad COS. kekRejected(10)           \: KEK modem key assignment rejected. tekRejected(11)           \: TEK modem key assignment rejected. online(12)                \: modem registered, enabled for data. initTftpPacketRcvd(13)    \: tftp packet received and option                             file transfer started.  initTodRquestRcvd(14)     \: Time of the Day (TOD) request                              received. reset(15)                 \: modem is resetting. rangingInProgress(16)     \: initial ranging is in progress. \-\-            rangingCompleted(17)      \: initial ranging is completed. (deprecated) dhcpGotIpAddr(18)         \: modem has got an IP address                              from the DHCP server. rejStaleConfig(19)        \: modem did attempt to register                             but registration was refused                             due to stale Config. rejIpSpoof(20)            \: modem did attempt to register but                             registration was refused due to IP                             Spoof. rejClassFail(21)          \: modem did attempt to register but                             registration was refused due to                              Class failure. rejRegNack(22)            \: modem did attempt to register but                             no acknowledgement was                              received. bpiKekExpired(23)         \: KEK modem key assignment expired. bpiTekExpired(24)         \: TEK modem key assignment expired. shutdown(25)              \: modem is in shutdown state. channelChgInitRangingRcvd(26)  \: modem sent initial ranging                                   during channel change. channelChgRangingInProgress(27) \: initial ranging is in                                   progress during channel                                   change.  This cdxCmtsCmStatusValue could return initRangingRcvd(3) or rangingInProgress(16) when the docsIfCmtsCmStatusValue is ranging(2).  This cdxCmtsCmStatusValue will return others(2) when the docsIfCmtsCmStatusValue states is either rangingAborted(3), rangingComplete(4), and ipComplete(5).  This cdxCmtsCmStatusValue could return online(12), or onlineNetAccessDisabled(5) for CM with BPI disabled, or onlineNetAccessDisabled(5) or onlineTekAssigned(7) for CM with BPI enabled, when the docsIfCmtsCmStatusValue is registrationComplete(6).  This cdxCmtsCmStatusValue could return either rejectBadMic(8), rejectBadCos(9) rejStaleConfig(19) or rejRegNack(22) when the docsIfCmtsCmStatusValue is accessDenied(7) for possible reasons of cable modem registration abort.  This cdxCmtsCmStatusValue could return either onlineKekAssigned(6), kekRejected(10), tekRejected(11), or online(12) for the CM with BPI enabled when the docsIfCmtsCmStatusValue is registeredBPIInitializing(9).    FOR DOCSIS 1.0 \-\-\-\-\-\-\-\-\-\-\-\-\-\- The ranging, rangingAborted, rangingComplete, and ipComplete  states in docsIfCmtsCmStatusValue is others in this object since this object is extension of docsIfCmtsCmStatusValue.   The registrationComplete state in docsIfCmtsCmStatusValue  could be online, onlineNetAccessDisabled, onlineKekAssigned, or  onlineTekAssigned in this object.    The accessDenied state in docsIfCmtsCmStatusValue could be  rejectBadMic, rejectBadCos in this object for the possible reasons of cable modem registration abort.  The states 15 to 25 are not applicable.  FOR DOCSIS 1.1 \-\-\-\-\-\-\-\-\-\-\-\-\-\-               The registrationComplete state in docsIfCmtsCmStatusValue  could be online, onlineNetAccessDisabled,  onlineBpiKekAssigned,or onlineBpiTekAssigned in this  object.    The accessDenied state in docsIfCmtsCmStatusValue could be  rejMicFail, rejStaleConfig, rejIpSpoof, rejClassFail,  rejRegNack in this object for the possible reasons of cable modem registration abort.  The CMTS only reports states it is able to detect. States Online(2) and  rejectBadCos(9) are not applicable for  DOCSIS1.1 modems. 
            	**type**\:  :py:class:`CdxCmtsCmStatusValue <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry.CdxCmtsCmStatusValue>`
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusonlinetimes
            
            	The number of times that the modem changes the connectivity  state from 'offline' to 'online' over the time period from  the modem's first ranging message received by CMTS until  now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as 'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatuspercentonline
            
            	The percentage of time that the modem stays 'online' over  the time period from the modem's first ranging message  received by CMTS until now.   The value for this object is 100 times bigger than the real  percentage value. For example, 32.15% will be value 3215.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..10000
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusminonlinetime
            
            	The minimum period of time the modem stayed 'online' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusavgonlinetime
            
            	The average period of time the modem stayed 'online' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusmaxonlinetime
            
            	The maximum period of time the modem stayed 'online' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusminofflinetime
            
            	The minimum period of time modem stayed 'offline' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusavgofflinetime
            
            	The average period of time the modem stayed 'offline' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusmaxofflinetime
            
            	The maximum period of time the modem stayed 'offline' over the time period from the modem's first ranging message  received by CMTS until now.  The modem is considered as 'online' when the value for  cdxCmtsCmStatusValue is any of the values\: online(5),  onlineNetAccessDisabled(6), onlineKekAssigned(7), and  onlineTekAssigned(8), and the modem is considered as  'offline' for other values for cdxCmtsCmStatusValue.  
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusdynsidcount
            
            	The number of active dynamic SIDs on this modem. Prior to getting the assigned the Service Flow IDs(SFID) the CM must must complete a number of protocol  transactions. The CMTS assigns a temporary Service ID (SID) to complete these steps
            	**type**\: int
            
            	**range:** 0..16383
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusaddlinfo
            
            	This object indicates additional attributes regarding the CM. 1. noisyPlant indicates that the CM connection is noisy. 2. modemPowerMaxOut indicates that the modem has reached its maximum power level.  A bit of of this object is set to 1 if the condition indicated by the bit is satisfied.  Note that BITS are encoded most significant bit first. 
            	**type**\:  :py:class:`CdxIfCmtsCmStatusAddlInfo <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry.CdxIfCmtsCmStatusAddlInfo>`
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatusonlinetimesnum
            
            	The number of times that the modem changes the connectivity state from 'offline' to 'online' over the time period from the modem's first ranging message received by CMTS until now.  The modem is considered as 'online' when the value for cdxCmtsCmStatusValue is any of the values\: online(5), onlineNetAccessDisabled(6), onlineKekAssigned(7), and onlineTekAssigned(8), and the modem is considered as 'offline' for other values for cdxCmtsCmStatusValue.  The value of this object is reset to 0 if the value in cdxIfCmtsCmStatusLastResetTime is changed. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifcmtscmstatuslastresettime
            
            	The last cable modem connectivity statistics reset time. If the value of  this object is '0', then the cable modem connectivity statistics had not been reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry, self).__init__()

                self.yang_name = "cdxCmtsCmStatusExtEntry"
                self.yang_parent_name = "cdxCmtsCmStatusExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('cdxcmtscmstatusvalue', (YLeaf(YType.enumeration, 'cdxCmtsCmStatusValue'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry.CdxCmtsCmStatusValue')])),
                    ('cdxifcmtscmstatusonlinetimes', (YLeaf(YType.uint32, 'cdxIfCmtsCmStatusOnlineTimes'), ['int'])),
                    ('cdxifcmtscmstatuspercentonline', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusPercentOnline'), ['int'])),
                    ('cdxifcmtscmstatusminonlinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusMinOnlineTime'), ['int'])),
                    ('cdxifcmtscmstatusavgonlinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusAvgOnlineTime'), ['int'])),
                    ('cdxifcmtscmstatusmaxonlinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusMaxOnlineTime'), ['int'])),
                    ('cdxifcmtscmstatusminofflinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusMinOfflineTime'), ['int'])),
                    ('cdxifcmtscmstatusavgofflinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusAvgOfflineTime'), ['int'])),
                    ('cdxifcmtscmstatusmaxofflinetime', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusMaxOfflineTime'), ['int'])),
                    ('cdxifcmtscmstatusdynsidcount', (YLeaf(YType.int32, 'cdxIfCmtsCmStatusDynSidCount'), ['int'])),
                    ('cdxifcmtscmstatusaddlinfo', (YLeaf(YType.bits, 'cdxIfCmtsCmStatusAddlInfo'), ['Bits'])),
                    ('cdxifcmtscmstatusonlinetimesnum', (YLeaf(YType.uint32, 'cdxIfCmtsCmStatusOnlineTimesNum'), ['int'])),
                    ('cdxifcmtscmstatuslastresettime', (YLeaf(YType.uint32, 'cdxIfCmtsCmStatusLastResetTime'), ['int'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.cdxcmtscmstatusvalue = None
                self.cdxifcmtscmstatusonlinetimes = None
                self.cdxifcmtscmstatuspercentonline = None
                self.cdxifcmtscmstatusminonlinetime = None
                self.cdxifcmtscmstatusavgonlinetime = None
                self.cdxifcmtscmstatusmaxonlinetime = None
                self.cdxifcmtscmstatusminofflinetime = None
                self.cdxifcmtscmstatusavgofflinetime = None
                self.cdxifcmtscmstatusmaxofflinetime = None
                self.cdxifcmtscmstatusdynsidcount = None
                self.cdxifcmtscmstatusaddlinfo = Bits()
                self.cdxifcmtscmstatusonlinetimesnum = None
                self.cdxifcmtscmstatuslastresettime = None
                self._segment_path = lambda: "cdxCmtsCmStatusExtEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsCmStatusExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmStatusExtTable.CdxCmtsCmStatusExtEntry, ['docsifcmtscmstatusindex', 'cdxcmtscmstatusvalue', 'cdxifcmtscmstatusonlinetimes', 'cdxifcmtscmstatuspercentonline', 'cdxifcmtscmstatusminonlinetime', 'cdxifcmtscmstatusavgonlinetime', 'cdxifcmtscmstatusmaxonlinetime', 'cdxifcmtscmstatusminofflinetime', 'cdxifcmtscmstatusavgofflinetime', 'cdxifcmtscmstatusmaxofflinetime', 'cdxifcmtscmstatusdynsidcount', 'cdxifcmtscmstatusaddlinfo', 'cdxifcmtscmstatusonlinetimesnum', 'cdxifcmtscmstatuslastresettime'], name, value)

            class CdxCmtsCmStatusValue(Enum):
                """
                CdxCmtsCmStatusValue (Enum Class)

                Current Cable Modem connectivity state. The object extends 

                states in docsIfCmtsCmStatusValue in more details. 

                The enumerations are\:

                offline(1)                \: modem considered offline.

                others(2)                 \: states is in 

                                            docsIfCmtsCmStatusValue.

                initRangingRcvd(3)        \: modem sent initial ranging.

                initDhcpReqRcvd(4)        \: dhcp request received.

                onlineNetAccessDisabled(5)\: modem registered, but network    

                                            access for the CM is disabled.

                onlineKekAssigned(6)      \: modem registered, BPI enabled

                                            and KEK assigned.

                onlineTekAssigned(7)      \: modem registered, BPI enabled

                                            and TEK assigned.

                rejectBadMic(8)           \: modem did attempt to register but

                                            registration was refused due to

                                            bad mic.

                rejectBadCos(9)           \: modem did attempt to register but

                                            registration was refused due to

                                            bad COS.

                kekRejected(10)           \: KEK modem key assignment rejected.

                tekRejected(11)           \: TEK modem key assignment rejected.

                online(12)                \: modem registered, enabled for data.

                initTftpPacketRcvd(13)    \: tftp packet received and option

                                            file transfer started. 

                initTodRquestRcvd(14)     \: Time of the Day (TOD) request 

                                            received.

                reset(15)                 \: modem is resetting.

                rangingInProgress(16)     \: initial ranging is in progress.

                \-\-            rangingCompleted(17)      \: initial ranging is completed. (deprecated)

                dhcpGotIpAddr(18)         \: modem has got an IP address 

                                            from the DHCP server.

                rejStaleConfig(19)        \: modem did attempt to register

                                            but registration was refused

                                            due to stale Config.

                rejIpSpoof(20)            \: modem did attempt to register but

                                            registration was refused due to IP

                                            Spoof.

                rejClassFail(21)          \: modem did attempt to register but

                                            registration was refused due to 

                                            Class failure.

                rejRegNack(22)            \: modem did attempt to register but

                                            no acknowledgement was 

                                            received.

                bpiKekExpired(23)         \: KEK modem key assignment expired.

                bpiTekExpired(24)         \: TEK modem key assignment expired.

                shutdown(25)              \: modem is in shutdown state.

                channelChgInitRangingRcvd(26)  \: modem sent initial ranging

                                                  during channel change.

                channelChgRangingInProgress(27) \: initial ranging is in

                                                  progress during channel

                                                  change.

                This cdxCmtsCmStatusValue could return initRangingRcvd(3)

                or rangingInProgress(16) when the docsIfCmtsCmStatusValue

                is ranging(2).

                This cdxCmtsCmStatusValue will return others(2) when the

                docsIfCmtsCmStatusValue states is either

                rangingAborted(3), rangingComplete(4), and

                ipComplete(5).

                This cdxCmtsCmStatusValue could return online(12), or

                onlineNetAccessDisabled(5) for CM with BPI disabled, or

                onlineNetAccessDisabled(5) or onlineTekAssigned(7) for

                CM with BPI enabled, when the docsIfCmtsCmStatusValue

                is registrationComplete(6).

                This cdxCmtsCmStatusValue could return either

                rejectBadMic(8), rejectBadCos(9) rejStaleConfig(19) or

                rejRegNack(22) when the docsIfCmtsCmStatusValue

                is accessDenied(7) for possible reasons of cable modem

                registration abort.

                This cdxCmtsCmStatusValue could return either

                onlineKekAssigned(6), kekRejected(10), tekRejected(11),

                or online(12) for the CM with BPI enabled when the

                docsIfCmtsCmStatusValue is registeredBPIInitializing(9).

                FOR DOCSIS 1.0

                \-\-\-\-\-\-\-\-\-\-\-\-\-\-

                The ranging, rangingAborted, rangingComplete, and ipComplete 

                states in docsIfCmtsCmStatusValue is others in this object

                since this object is extension of docsIfCmtsCmStatusValue. 

                The registrationComplete state in docsIfCmtsCmStatusValue 

                could be online, onlineNetAccessDisabled, onlineKekAssigned, or 

                onlineTekAssigned in this object.  

                The accessDenied state in docsIfCmtsCmStatusValue could be 

                rejectBadMic, rejectBadCos in this object for the possible

                reasons of cable modem registration abort.

                The states 15 to 25 are not applicable.

                FOR DOCSIS 1.1

                \-\-\-\-\-\-\-\-\-\-\-\-\-\- 

                The registrationComplete state in docsIfCmtsCmStatusValue 

                could be online, onlineNetAccessDisabled, 

                onlineBpiKekAssigned,or onlineBpiTekAssigned in this 

                object.  

                The accessDenied state in docsIfCmtsCmStatusValue could be 

                rejMicFail, rejStaleConfig, rejIpSpoof, rejClassFail, 

                rejRegNack in this object for the possible reasons of cable

                modem registration abort.

                The CMTS only reports states it is able to detect. States

                Online(2) and  rejectBadCos(9) are not applicable for 

                DOCSIS1.1 modems. 

                .. data:: offline = 1

                .. data:: others = 2

                .. data:: initRangingRcvd = 3

                .. data:: initDhcpReqRcvd = 4

                .. data:: onlineNetAccessDisabled = 5

                .. data:: onlineKekAssigned = 6

                .. data:: onlineTekAssigned = 7

                .. data:: rejectBadMic = 8

                .. data:: rejectBadCos = 9

                .. data:: kekRejected = 10

                .. data:: tekRejected = 11

                .. data:: online = 12

                .. data:: initTftpPacketRcvd = 13

                .. data:: initTodRequestRcvd = 14

                .. data:: reset = 15

                .. data:: rangingInProgress = 16

                .. data:: rangingCompleted = 17

                .. data:: dhcpGotIpAddr = 18

                .. data:: rejStaleConfig = 19

                .. data:: rejIpSpoof = 20

                .. data:: rejClassFail = 21

                .. data:: rejRegNack = 22

                .. data:: bpiKekExpired = 23

                .. data:: bpiTekExpired = 24

                .. data:: shutdown = 25

                .. data:: channelChgInitRangingRcvd = 26

                .. data:: channelChgRangingInProgress = 27

                """

                offline = Enum.YLeaf(1, "offline")

                others = Enum.YLeaf(2, "others")

                initRangingRcvd = Enum.YLeaf(3, "initRangingRcvd")

                initDhcpReqRcvd = Enum.YLeaf(4, "initDhcpReqRcvd")

                onlineNetAccessDisabled = Enum.YLeaf(5, "onlineNetAccessDisabled")

                onlineKekAssigned = Enum.YLeaf(6, "onlineKekAssigned")

                onlineTekAssigned = Enum.YLeaf(7, "onlineTekAssigned")

                rejectBadMic = Enum.YLeaf(8, "rejectBadMic")

                rejectBadCos = Enum.YLeaf(9, "rejectBadCos")

                kekRejected = Enum.YLeaf(10, "kekRejected")

                tekRejected = Enum.YLeaf(11, "tekRejected")

                online = Enum.YLeaf(12, "online")

                initTftpPacketRcvd = Enum.YLeaf(13, "initTftpPacketRcvd")

                initTodRequestRcvd = Enum.YLeaf(14, "initTodRequestRcvd")

                reset = Enum.YLeaf(15, "reset")

                rangingInProgress = Enum.YLeaf(16, "rangingInProgress")

                rangingCompleted = Enum.YLeaf(17, "rangingCompleted")

                dhcpGotIpAddr = Enum.YLeaf(18, "dhcpGotIpAddr")

                rejStaleConfig = Enum.YLeaf(19, "rejStaleConfig")

                rejIpSpoof = Enum.YLeaf(20, "rejIpSpoof")

                rejClassFail = Enum.YLeaf(21, "rejClassFail")

                rejRegNack = Enum.YLeaf(22, "rejRegNack")

                bpiKekExpired = Enum.YLeaf(23, "bpiKekExpired")

                bpiTekExpired = Enum.YLeaf(24, "bpiTekExpired")

                shutdown = Enum.YLeaf(25, "shutdown")

                channelChgInitRangingRcvd = Enum.YLeaf(26, "channelChgInitRangingRcvd")

                channelChgRangingInProgress = Enum.YLeaf(27, "channelChgRangingInProgress")





    class CdxCmtsMacExtTable(Entity):
        """
        This table contains the additions attributes of a CMTS MAC
        interface that provided by docsIfCmtsMacTable. 
        
        .. attribute:: cdxcmtsmacextentry
        
        	Additional objects for docsIfCmtsMacTable entry including the cable modem notification enable/disable and the interval  of cable modem notification sent by the CMTS for a cable modem that the Mac interface supports. An entry in this table exists  for each ifEntry with an ifType of docsCableMaclayer(127). Additional objects added to determine the number of  active/registered/total cable modems on this cable mac  interface since boot. Also, it contains the object to set the Dynamic Message Integrity Check (DMIC) which users  can configure how cable modems are handled if CMs fail  the DMIC
        	**type**\: list of  		 :py:class:`CdxCmtsMacExtEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsMacExtTable.CdxCmtsMacExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsMacExtTable, self).__init__()

            self.yang_name = "cdxCmtsMacExtTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsMacExtEntry", ("cdxcmtsmacextentry", CISCODOCSEXTMIB.CdxCmtsMacExtTable.CdxCmtsMacExtEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtsmacextentry = YList(self)
            self._segment_path = lambda: "cdxCmtsMacExtTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsMacExtTable, [], name, value)


        class CdxCmtsMacExtEntry(Entity):
            """
            Additional objects for docsIfCmtsMacTable entry including
            the cable modem notification enable/disable and the interval 
            of cable modem notification sent by the CMTS for a cable modem
            that the Mac interface supports. An entry in this table exists 
            for each ifEntry with an ifType of docsCableMaclayer(127).
            Additional objects added to determine the number of 
            active/registered/total cable modems on this cable mac 
            interface since boot. Also, it contains the object to set
            the Dynamic Message Integrity Check (DMIC) which users 
            can configure how cable modems are handled if CMs fail 
            the DMIC.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmonofftrapenable
            
            	An indication of whether the cdxCmtsCmOnOffNotification  is enabled. The default value is false(2). 
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmonofftrapinterval
            
            	The interval for cdxCmtsCmOnOffNotification sent by CMTS for one online/offline state change if cdxCmtsCmOnOffTrapEnable  is true.   If there are more than one state changes to online/offline  for a cable modem during this interval, only one  cdxCmtsCmOnOffNotification is sent by CMTS for the first  state change to online and one cdxCmtsCmOnOffNotification  for the first state changing to offline if  cdxCmtsCmOnOffTrapEnable is true.  This is to avoid too many notifications sent for a cable  modem online/offline state changes during a short period of time.   If the value is 0, then cdxCmtsCmOnOffNotification will be  sent for every state changes to online/offline for a cable  modem if cdxCmtsCmOnOffTrapEnable is true.    If cdxCmtsCmOnOffTrapEnable value changes from true to false  or from false to true, this value will remain no change as  before.   The default value is 600 seconds. 
            	**type**\: int
            
            	**range:** 0..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdxcmtscmdefaultmaxcpes
            
            	The default maximum number of permitted CPEs per modem  in this cable interface. A modem can override this  value by setting the object cdxCmtsCmMaxCpeNumber in the cdxCmtsCmTable.    The value \-1 means the default value of maximum hosts  per modem in this cable interface is not specified.  The value 0 means no maximum limit.  Setting the value will not affect the already connected CPEs to the modems in this cable interface. 
            	**type**\: int
            
            	**range:** \-1..255
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmtotal
            
            	The total count of cable modems on this cable mac interface since boot
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmactive
            
            	The count of cable modems that are active. Active cable  modems are recognized by the cdxCmtsCmStatusValue  other than offline(1). 
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmregistered
            
            	The count of cable modems that are registered and online  on this cable mac interface. Registered cable modems are  those with one of the following values.  registrationComplete(6) of docsIfCmtsCmStatusValue OR  either of online(12), kekRejected(10),  onlineKekAssigned(6),tekRejected(11), onlineTekAssigned(7) of cdxCmtsCmStatusValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmdmicmode
            
            	The Dynamic Shared Secret feature can operate in three  different modes, depending on what action should be taken  for cable modems that fail the CMTS MIC verification check\: notConfigured(1)\: It indicates that the DMIC is not                    configured for this cable interface. mark(2)\: By default, the Dynamic Shared Secret feature           is enabled on all cable interfaces using the           mark option. In this mode, the CMTS allows           cable modems to come online even if they fail           the CMTS MIC validity check. However, for          this modem cdxCmtsCmStatusDMICMode will          be labeled as marked. lock(3)\: When the lock option is used, the CMTS assigns           a restrictive QoS configuration to CMs that           fail the MIC validity check twice in a row. A           particular QoS profile to be used for locked           cable modems can be specified by setting           cdxCmtsCmDMICLockQos.          If a customer resets their CM, the CM will           reregister but still uses the restricted QoS           profile. A locked CM continues with the           restricted QoS profile until it goes offline           and remains offline for at least 24 hours, at           which point it is allowed to reregister with a           valid DOCSIS configuration file. A system           operator can manually clear the lock on a CM by           setting cdxCmtsCmStatusDMICUnLock object. reject(4)\:  In the reject mode, the CMTS refuses to allow              CMs to come online if they fail the CMTS MIC              validity check
            	**type**\:  :py:class:`CdxCmtsCmDMICMode <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsMacExtTable.CdxCmtsMacExtEntry.CdxCmtsCmDMICMode>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmdmiclockqos
            
            	If cdxCmtsCmDMICMode is set to lockingMode(3), this object would contain the restrictive QoS profile number as  indicated by docsIfQosProfIndex if set and it will  have 0 if not applicable or not defined. In case, cdxCmtsCmDMICMode is set to lockingMode(3) and this object is not defined then the CMTS defaults to special QoS profile that limits the downstream and upstream  service flows to a maximum rate of 10 kbps. However, for this to happen the modems should have the  permission to create QoS profile
            	**type**\: int
            
            	**range:** 0..16383
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsMacExtTable.CdxCmtsMacExtEntry, self).__init__()

                self.yang_name = "cdxCmtsMacExtEntry"
                self.yang_parent_name = "cdxCmtsMacExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxcmtscmonofftrapenable', (YLeaf(YType.boolean, 'cdxCmtsCmOnOffTrapEnable'), ['bool'])),
                    ('cdxcmtscmonofftrapinterval', (YLeaf(YType.int32, 'cdxCmtsCmOnOffTrapInterval'), ['int'])),
                    ('cdxcmtscmdefaultmaxcpes', (YLeaf(YType.int32, 'cdxCmtsCmDefaultMaxCpes'), ['int'])),
                    ('cdxcmtscmtotal', (YLeaf(YType.int32, 'cdxCmtsCmTotal'), ['int'])),
                    ('cdxcmtscmactive', (YLeaf(YType.int32, 'cdxCmtsCmActive'), ['int'])),
                    ('cdxcmtscmregistered', (YLeaf(YType.int32, 'cdxCmtsCmRegistered'), ['int'])),
                    ('cdxcmtscmdmicmode', (YLeaf(YType.enumeration, 'cdxCmtsCmDMICMode'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsMacExtTable.CdxCmtsMacExtEntry.CdxCmtsCmDMICMode')])),
                    ('cdxcmtscmdmiclockqos', (YLeaf(YType.int32, 'cdxCmtsCmDMICLockQos'), ['int'])),
                ])
                self.ifindex = None
                self.cdxcmtscmonofftrapenable = None
                self.cdxcmtscmonofftrapinterval = None
                self.cdxcmtscmdefaultmaxcpes = None
                self.cdxcmtscmtotal = None
                self.cdxcmtscmactive = None
                self.cdxcmtscmregistered = None
                self.cdxcmtscmdmicmode = None
                self.cdxcmtscmdmiclockqos = None
                self._segment_path = lambda: "cdxCmtsMacExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsMacExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsMacExtTable.CdxCmtsMacExtEntry, ['ifindex', 'cdxcmtscmonofftrapenable', 'cdxcmtscmonofftrapinterval', 'cdxcmtscmdefaultmaxcpes', 'cdxcmtscmtotal', 'cdxcmtscmactive', 'cdxcmtscmregistered', 'cdxcmtscmdmicmode', 'cdxcmtscmdmiclockqos'], name, value)

            class CdxCmtsCmDMICMode(Enum):
                """
                CdxCmtsCmDMICMode (Enum Class)

                The Dynamic Shared Secret feature can operate in three 

                different modes, depending on what action should be taken 

                for cable modems that fail the CMTS MIC verification check\:

                notConfigured(1)\: It indicates that the DMIC is not 

                                  configured for this cable interface.

                mark(2)\: By default, the Dynamic Shared Secret feature 

                         is enabled on all cable interfaces using the 

                         mark option. In this mode, the CMTS allows 

                         cable modems to come online even if they fail 

                         the CMTS MIC validity check. However, for

                         this modem cdxCmtsCmStatusDMICMode will

                         be labeled as marked.

                lock(3)\: When the lock option is used, the CMTS assigns 

                         a restrictive QoS configuration to CMs that 

                         fail the MIC validity check twice in a row. A 

                         particular QoS profile to be used for locked 

                         cable modems can be specified by setting 

                         cdxCmtsCmDMICLockQos.

                         If a customer resets their CM, the CM will 

                         reregister but still uses the restricted QoS 

                         profile. A locked CM continues with the 

                         restricted QoS profile until it goes offline 

                         and remains offline for at least 24 hours, at 

                         which point it is allowed to reregister with a 

                         valid DOCSIS configuration file. A system 

                         operator can manually clear the lock on a CM by 

                         setting cdxCmtsCmStatusDMICUnLock object.

                reject(4)\:  In the reject mode, the CMTS refuses to allow 

                            CMs to come online if they fail the CMTS MIC 

                            validity check.

                .. data:: notConfigured = 1

                .. data:: mark = 2

                .. data:: lock = 3

                .. data:: reject = 4

                """

                notConfigured = Enum.YLeaf(1, "notConfigured")

                mark = Enum.YLeaf(2, "mark")

                lock = Enum.YLeaf(3, "lock")

                reject = Enum.YLeaf(4, "reject")





    class CdxCmtsCmChOverTable(Entity):
        """
        A table of CMTS operation entries to instruct cable modems
        to move to a new downstream and/or upstream channel. 
        
        An entry in this table is an operation that has been 
        initiated from CMTS to generates downstream frequency and/or 
        upstream channel override fields in the RNG\-RSP message sent 
        to a cable modem.  A RNG\-RSP message is sent to a cable 
        modem during initial maintenance opportunity. 
        
        This operation causes the uBR to place an entry for the cable 
        modem specified into the override request queue.  The link is 
        then broken by deleting the modem from its polling list.  When 
        the modem attempts initial ranging, the override request 
        causes downstream frequency and upstream channel override 
        fields to be inserted into the RNG\-RSP message.  
        
        .. attribute:: cdxcmtscmchoverentry
        
        	A CMTS operation entry to instruct a cable modem to move to a new downstream and/or upstream channel.  A CMTS operator can use this to initiate an operation in CMTS to instruct a cable modem to move to a new downstream, or upstream channel or both.   Each entry consists of the mac address of the cable modem to be moved, a new downstream frequency, a new upstream channel  id etc..  More than one entries could have for a cable modem, so there is a time stamp for each entry to show the time when this operation is initiated.   A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status  of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped. That is, it will run until either the CMTS has generated  downstream frequency and/or upstream channel override fields  in the RNG\-RSP message sent to a cable modem or time out.  In either case, the operation is completed.  Once the operation is completed, the real result of the  operation to the cable modem cannot be known from this table. The result of the cable modem's downstream frequency and the  upstream channel id can be checked from other MIB tables.   For example, docsIfCmtsServiceTable from DOCS\-IF\-MIB can be  used to check whether the cable modem's downstream frequency and upstream channel id are changed.  Please note that even the CMTS has generated downstream frequency and/or upstream  channel override fields in the RNG\-RSP message sent to a  cable modems, if the cable modem cannot lock the instructed  downstream frequency or no upstream channel id could be used,  it may reconnect back to the original downstream frequency and upstream channel id.   Once the operation completes, the management station should retrieve the values of the cdxCmtsCmChOverState  objects of interest, and should then delete the entry.   In order to prevent old entries from clogging the table,  entries will be aged out, but an entry will never be deleted  within 15 minutes of completing. 
        	**type**\: list of  		 :py:class:`CdxCmtsCmChOverEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsCmChOverTable, self).__init__()

            self.yang_name = "cdxCmtsCmChOverTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsCmChOverEntry", ("cdxcmtscmchoverentry", CISCODOCSEXTMIB.CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtscmchoverentry = YList(self)
            self._segment_path = lambda: "cdxCmtsCmChOverTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmChOverTable, [], name, value)


        class CdxCmtsCmChOverEntry(Entity):
            """
            A CMTS operation entry to instruct a cable modem to move to
            a new downstream and/or upstream channel.
            
            A CMTS operator can use this to initiate an operation
            in CMTS to instruct a cable modem to move to a new
            downstream, or upstream channel or both. 
            
            Each entry consists of the mac address of the cable modem
            to be moved, a new downstream frequency, a new upstream channel 
            id etc..  More than one entries could have for a cable modem,
            so there is a time stamp for each entry to show the time
            when this operation is initiated. 
            
            A management station wishing to create an entry should
            first generate a pseudo\-random serial number to be used
            as the index to this sparse table.  The station should
            then create the associated instance of the row status
            object. It must also, either in the same or in successive
            PDUs, create the associated instance of the command and
            parameter objects. It should also modify the default values
            for any of the parameter objects if the defaults are not
            appropriate.
            
            Once the appropriate instances of all the command
            objects have been created, either by an explicit SNMP
            set request or by default, the row status should be set
            to active to initiate the operation. Note that this entire
            procedure may be initiated via a single set request which
            specifies a row status  of createAndGo as well as specifies
            valid values for the non\-defaulted parameter objects.
            
            Once an operation has been activated, it cannot be stopped.
            That is, it will run until either the CMTS has generated 
            downstream frequency and/or upstream channel override fields 
            in the RNG\-RSP message sent to a cable modem or time out. 
            In either case, the operation is completed.
            
            Once the operation is completed, the real result of the 
            operation to the cable modem cannot be known from this table.
            The result of the cable modem's downstream frequency and the 
            upstream channel id can be checked from other MIB tables.  
            For example, docsIfCmtsServiceTable from DOCS\-IF\-MIB can be 
            used to check whether the cable modem's downstream frequency
            and upstream channel id are changed.  Please note that even
            the CMTS has generated downstream frequency and/or upstream 
            channel override fields in the RNG\-RSP message sent to a 
            cable modems, if the cable modem cannot lock the instructed 
            downstream frequency or no upstream channel id could be used, 
            it may reconnect back to the original downstream frequency
            and upstream channel id. 
            
            Once the operation completes, the management station should
            retrieve the values of the cdxCmtsCmChOverState 
            objects of interest, and should then delete the entry.  
            In order to prevent old entries from clogging the table, 
            entries will be aged out, but an entry will never be deleted 
            within 15 minutes of completing. 
            
            .. attribute:: cdxcmtscmchoverserialnumber  (key)
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a channel override operation should use a pseudo\-random  value for this object when creating or modifying an  instance of a cdxCmtsCmChOverEntry.  
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchovermacaddress
            
            	The mac address of the cable modem that the CMTS instructs to move to a new downstream and/or upstream channel.    This column must be set to a valid Mac address currently in the CMTS in order for this entry's row status to be set to active successfully
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchoverdownfrequency
            
            	The new downstream frequency which the cable modem is  instructed to move to.  The value 0 is to ask the CMTS not to override the downstream frequency. 
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**config**\: False
            
            	**units**\: hertz
            
            .. attribute:: cdxcmtscmchoverupchannelid
            
            	The new channel Id which the cable modem is instructed to  move to.  The value \-1 is to ask the CMTS not to override the upstream channel Id. 
            	**type**\: int
            
            	**range:** \-1..255
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchovertraponcompletion
            
            	Specifies whether or not a cdxCmtsCmChOverNotification  should be issued on completion of the operation.  If such a  notification is desired, it is the responsibility of the  management entity to ensure that the SNMP administrative model  is configured in such a way as to allow the notification to be  delivered. 
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchoveropinitiatedtime
            
            	The value of sysUpTime at which the operation was initiated.   Since it is possible to have more than one entry in this  table for a cable modem, this object can help to distinguish  the entries for the same cable modem. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchoverstate
            
            	The status of the specified channel override operation. The enumerations are\:   messageSent(1)\: the CMTS has sent a RNG\-RSP message                with channel override to the cable modem.    commandNotActive(2)\: the command is not in active mode                        due to this entry's row status is not                        in active yet.   noOpNeed(3)\: The downstream frequency and the upstream                 channel Id in this entry are the same as                 original ones when this entry's row status                is set to active, so CMTS does not need to                 do any operation.     modemNotFound(4)\: The modem is not found in the CMTS                     at the time when the command becomes                     active.   waitToSendMessage(5)\: specified the operation is active                         and CMTS is waiting to send                         a RNG\-RSP message with channel                          override to the cable modem.   timeOut(6)\: specified the operation is timed out.               That is, the CMTS cannot send a RNG\-RSP message                with channel override to the cable modem within                the time specified in the object of                cdxCmtsCmChOverTimeExpiration.                The possible reason is that the cable modem               does not repeat the initial ranging.      The possible state change diagram is as below\:     [commandNotActive \->] waitToSendMessage \->         messageSent or timeOut.     [commandNotActive \->] noOpNeeded or modemNotFound. 
            	**type**\:  :py:class:`CdxCmtsCmChOverState <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry.CdxCmtsCmChOverState>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmchoverrowstatus
            
            	The status of this table entry.    This value for cdxCmtsCmChOverMacAddress must be valid Mac  address currently in the CMTS in order for the row  status to be set to active successfully.      Once the row status becomes active and state becomes  waitToSendMessage, the entry cannot not be changed except  to delete the entry by setting the row status to destroy(6)  and since the operation cannot be stopped, the destroy(6)  will just cause the SNMP agent to hide the entry from  application and the SNMP agent will delete the entry  right after the operation is completed. 
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry, self).__init__()

                self.yang_name = "cdxCmtsCmChOverEntry"
                self.yang_parent_name = "cdxCmtsCmChOverTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxcmtscmchoverserialnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxcmtscmchoverserialnumber', (YLeaf(YType.int32, 'cdxCmtsCmChOverSerialNumber'), ['int'])),
                    ('cdxcmtscmchovermacaddress', (YLeaf(YType.str, 'cdxCmtsCmChOverMacAddress'), ['str'])),
                    ('cdxcmtscmchoverdownfrequency', (YLeaf(YType.int32, 'cdxCmtsCmChOverDownFrequency'), ['int'])),
                    ('cdxcmtscmchoverupchannelid', (YLeaf(YType.int32, 'cdxCmtsCmChOverUpChannelId'), ['int'])),
                    ('cdxcmtscmchovertraponcompletion', (YLeaf(YType.boolean, 'cdxCmtsCmChOverTrapOnCompletion'), ['bool'])),
                    ('cdxcmtscmchoveropinitiatedtime', (YLeaf(YType.uint32, 'cdxCmtsCmChOverOpInitiatedTime'), ['int'])),
                    ('cdxcmtscmchoverstate', (YLeaf(YType.enumeration, 'cdxCmtsCmChOverState'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry.CdxCmtsCmChOverState')])),
                    ('cdxcmtscmchoverrowstatus', (YLeaf(YType.enumeration, 'cdxCmtsCmChOverRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cdxcmtscmchoverserialnumber = None
                self.cdxcmtscmchovermacaddress = None
                self.cdxcmtscmchoverdownfrequency = None
                self.cdxcmtscmchoverupchannelid = None
                self.cdxcmtscmchovertraponcompletion = None
                self.cdxcmtscmchoveropinitiatedtime = None
                self.cdxcmtscmchoverstate = None
                self.cdxcmtscmchoverrowstatus = None
                self._segment_path = lambda: "cdxCmtsCmChOverEntry" + "[cdxCmtsCmChOverSerialNumber='" + str(self.cdxcmtscmchoverserialnumber) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsCmChOverTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmChOverTable.CdxCmtsCmChOverEntry, ['cdxcmtscmchoverserialnumber', 'cdxcmtscmchovermacaddress', 'cdxcmtscmchoverdownfrequency', 'cdxcmtscmchoverupchannelid', 'cdxcmtscmchovertraponcompletion', 'cdxcmtscmchoveropinitiatedtime', 'cdxcmtscmchoverstate', 'cdxcmtscmchoverrowstatus'], name, value)

            class CdxCmtsCmChOverState(Enum):
                """
                CdxCmtsCmChOverState (Enum Class)

                The status of the specified channel override operation.

                The enumerations are\:

                  messageSent(1)\: the CMTS has sent a RNG\-RSP message 

                              with channel override to the cable modem. 

                  commandNotActive(2)\: the command is not in active mode

                                       due to this entry's row status is not

                                       in active yet.

                  noOpNeed(3)\: The downstream frequency and the upstream 

                               channel Id in this entry are the same as 

                               original ones when this entry's row status

                               is set to active, so CMTS does not need to 

                               do any operation.  

                  modemNotFound(4)\: The modem is not found in the CMTS

                                    at the time when the command becomes

                                    active.

                  waitToSendMessage(5)\: specified the operation is active

                                        and CMTS is waiting to send

                                        a RNG\-RSP message with channel 

                                        override to the cable modem.

                  timeOut(6)\: specified the operation is timed out.

                              That is, the CMTS cannot send a RNG\-RSP message 

                              with channel override to the cable modem within 

                              the time specified in the object of 

                              cdxCmtsCmChOverTimeExpiration. 

                              The possible reason is that the cable modem

                              does not repeat the initial ranging. 

                   The possible state change diagram is as below\: 

                   [commandNotActive \->] waitToSendMessage \-> 

                       messageSent or timeOut. 

                   [commandNotActive \->] noOpNeeded or modemNotFound. 

                .. data:: messageSent = 1

                .. data:: commandNotActive = 2

                .. data:: noOpNeeded = 3

                .. data:: modemNotFound = 4

                .. data:: waitToSendMessage = 5

                .. data:: timeOut = 6

                """

                messageSent = Enum.YLeaf(1, "messageSent")

                commandNotActive = Enum.YLeaf(2, "commandNotActive")

                noOpNeeded = Enum.YLeaf(3, "noOpNeeded")

                modemNotFound = Enum.YLeaf(4, "modemNotFound")

                waitToSendMessage = Enum.YLeaf(5, "waitToSendMessage")

                timeOut = Enum.YLeaf(6, "timeOut")





    class CdxCmtsCmTable(Entity):
        """
        This table contains attributes or configurable parameters 
        for cable modems from a CMTS. 
        
        .. attribute:: cdxcmtscmentry
        
        	The list contains a cable modem's attributes or  configurable parameters from a CMTS. 
        	**type**\: list of  		 :py:class:`CdxCmtsCmEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmTable.CdxCmtsCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsCmTable, self).__init__()

            self.yang_name = "cdxCmtsCmTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsCmEntry", ("cdxcmtscmentry", CISCODOCSEXTMIB.CdxCmtsCmTable.CdxCmtsCmEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtscmentry = YList(self)
            self._segment_path = lambda: "cdxCmtsCmTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmTable, [], name, value)


        class CdxCmtsCmEntry(Entity):
            """
            The list contains a cable modem's attributes or 
            configurable parameters from a CMTS. 
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmmaxcpenumber
            
            	The maximum number of permitted CPEs connecting to the modem.   The value \-1 means to use the default value of maximum  hosts per modem in the CMTS cable interface which the modem  connects to and the value is defined in  cdxCmtsCmDefaultMaxCpes in the cdxCmtsMacExtTable.   The value 0 means no maximum limit.  Setting the value will not affect the already connected CPEs to the modem. 
            	**type**\: int
            
            	**range:** \-1..255
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmcurrcpenumber
            
            	The current number of CPEs connecting to the modem.  The value 0 means no hosts connecting to the modem
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmqosprofile
            
            	The index in docsIfQosProfileTable describing the quality of service attributes associated with this particular modem's primary SID.   When trying to change the value, if the new value is not  a valid index in the docsIfQosProfileTable, the modem will  retain the old docsIfQosProfileTable entry. If no associated  docsIfQosProfileTable entry exists for this modem,  this object returns a value of zero on read.  This object has meaning only for DOCSIS1.0 cable modems. For cable modems in DOCSIS1.1 or above mode, this object will  report 0 and cannot be changed to any other values since  there is no QoS profile associated with cable modems in  DOCSIS1.1 or above mode
            	**type**\: int
            
            	**range:** 0..16383
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsCmTable.CdxCmtsCmEntry, self).__init__()

                self.yang_name = "cdxCmtsCmEntry"
                self.yang_parent_name = "cdxCmtsCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('cdxcmtscmmaxcpenumber', (YLeaf(YType.int32, 'cdxCmtsCmMaxCpeNumber'), ['int'])),
                    ('cdxcmtscmcurrcpenumber', (YLeaf(YType.int32, 'cdxCmtsCmCurrCpeNumber'), ['int'])),
                    ('cdxcmtscmqosprofile', (YLeaf(YType.int32, 'cdxCmtsCmQosProfile'), ['int'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.cdxcmtscmmaxcpenumber = None
                self.cdxcmtscmcurrcpenumber = None
                self.cdxcmtscmqosprofile = None
                self._segment_path = lambda: "cdxCmtsCmEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmTable.CdxCmtsCmEntry, ['docsifcmtscmstatusindex', 'cdxcmtscmmaxcpenumber', 'cdxcmtscmcurrcpenumber', 'cdxcmtscmqosprofile'], name, value)




    class CdxCmtsCmStatusDMICTable(Entity):
        """
        This table contains the list of modems which failed the CMTS
        Dynamic Message Integrity Check (DMIC). The modems are 
        either
        Marked\: The modems failed the DMIC check but were still 
                allowed to come online.
        Locked\: The modems failed the DMIC check and hence were 
                allowed to come online with a restrictive QoS 
                profile as defined in  cdxCmtsCmDMICLockQos.
        Rejected\: The modems failed the DMIC check and hence
                  were not allowed to come online.
        Another objective of the objects in this table is to clear
        the lock on the modems.
        
        .. attribute:: cdxcmtscmstatusdmicentry
        
        	Additional DMIC objects for docsIfCmtsCmStatusTable  entry. 
        	**type**\: list of  		 :py:class:`CdxCmtsCmStatusDMICEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable, self).__init__()

            self.yang_name = "cdxCmtsCmStatusDMICTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsCmStatusDMICEntry", ("cdxcmtscmstatusdmicentry", CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtscmstatusdmicentry = YList(self)
            self._segment_path = lambda: "cdxCmtsCmStatusDMICTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable, [], name, value)


        class CdxCmtsCmStatusDMICEntry(Entity):
            """
            Additional DMIC objects for docsIfCmtsCmStatusTable 
            entry. 
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmstatusdmicmode
            
            	This shows all the cable modems that are online or offline and that had failed the Dynamic CMTS MIC verification check. The state is mentioned as follows\: mark(1)\: The modem was allowed to come online. lock(2)\: The modem was allowed to come online but with            a restrictive QoS profile as defined by             cdxCmtsCmDMICLockQos. reject(3)\: The modem was not allowed to come online
            	**type**\:  :py:class:`CdxCmtsCmStatusDMICMode <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry.CdxCmtsCmStatusDMICMode>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtscmstatusdmicunlock
            
            	When set to TRUE, it forces the cable modems to  reinitialize, and the cable modems must re\-register with a valid DOCSIS configuration file before being allowed online. Otherwise, the cable modem is locked  in its current restricted QoS profile and cannot  reregister with a different profile until it has  been offline for at least 24 hours. If cdxCmtsCmStatusDMICUnLock is set to TRUE, and re\-init succeeds, that modem row is removed from the cdxCmtsCmStatusDMICTable. And if re\-init again fails, the row remains in that table, possibly with a new value for cdxCmtsCmStatusDMICMode When polled, it will always return FALSE
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry, self).__init__()

                self.yang_name = "cdxCmtsCmStatusDMICEntry"
                self.yang_parent_name = "cdxCmtsCmStatusDMICTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('cdxcmtscmstatusdmicmode', (YLeaf(YType.enumeration, 'cdxCmtsCmStatusDMICMode'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry.CdxCmtsCmStatusDMICMode')])),
                    ('cdxcmtscmstatusdmicunlock', (YLeaf(YType.boolean, 'cdxCmtsCmStatusDMICUnLock'), ['bool'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.cdxcmtscmstatusdmicmode = None
                self.cdxcmtscmstatusdmicunlock = None
                self._segment_path = lambda: "cdxCmtsCmStatusDMICEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsCmStatusDMICTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsCmStatusDMICTable.CdxCmtsCmStatusDMICEntry, ['docsifcmtscmstatusindex', 'cdxcmtscmstatusdmicmode', 'cdxcmtscmstatusdmicunlock'], name, value)

            class CdxCmtsCmStatusDMICMode(Enum):
                """
                CdxCmtsCmStatusDMICMode (Enum Class)

                This shows all the cable modems that are online or offline

                and that had failed the Dynamic CMTS MIC verification

                check. The state is mentioned as follows\:

                mark(1)\: The modem was allowed to come online.

                lock(2)\: The modem was allowed to come online but with

                           a restrictive QoS profile as defined by 

                           cdxCmtsCmDMICLockQos.

                reject(3)\: The modem was not allowed to come online.

                .. data:: mark = 1

                .. data:: lock = 2

                .. data:: reject = 3

                """

                mark = Enum.YLeaf(1, "mark")

                lock = Enum.YLeaf(2, "lock")

                reject = Enum.YLeaf(3, "reject")





    class CdxCmToCpeTable(Entity):
        """
        This table contains information about CPE connects behind
        cable modem. It will return IP address and IP address type
        of each CPE connect to a CM.
        
        It is not intended to walk the whole table. An application
        would need to query this table based on the specific indices.
        Otherwise, it will impact the CMTS performance due to the 
        huge size of this table.
        
        The agent creates/destroys/modifies an entry whenever there
        is a CPE connect to a cable modem or disconnect from a cable
        modem.
        
        .. attribute:: cdxcmtocpeentry
        
        	Represents an entry in the table. Each entry is created if there is CPE connects to a cable modem.  The indices uniquely identify a CPE. It is never the intent for an application to perform a SNMP Get operation against a table of this nature, rather it is the intent to merely enumberate mappings.   An application would determine the CPEs behind all cable modems by performing a SNMP GetNext starting with the variable bindings\: \- cdxCmToCpeInetAddressType.0 \- cdxCmToCpeInetAddress.0  It will return the IP address type and value tuple corresponding to the CPE with lowest IP address behind the cable modem with the lowest MAC address. An application can perform a SNMP GetNext operation with the following variable bindings\: \- cdxCmToCpeInetAddressType.x.y.z \- cdxCmToCpeInetAddress.x.y.z where x is MAC address of cable modem, and y.z is IP address type and value tuple of the reported CPE. An application can repeat this process until it has traversed the entire table.  If the application only wants to know the CPEs behind a given cable modem, it can perform a SNMP GetNext opertaion with the following\: \- cdxCmToCpeInetAddressType.x \- cdxCmToCpeInetAddress.x where x is MAC address of cable modem
        	**type**\: list of  		 :py:class:`CdxCmToCpeEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmToCpeTable.CdxCmToCpeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmToCpeTable, self).__init__()

            self.yang_name = "cdxCmToCpeTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmToCpeEntry", ("cdxcmtocpeentry", CISCODOCSEXTMIB.CdxCmToCpeTable.CdxCmToCpeEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtocpeentry = YList(self)
            self._segment_path = lambda: "cdxCmToCpeTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmToCpeTable, [], name, value)


        class CdxCmToCpeEntry(Entity):
            """
            Represents an entry in the table. Each entry is created if
            there is CPE connects to a cable modem.
            
            The indices uniquely identify a CPE. It is never the intent
            for an application to perform a SNMP Get operation against
            a table of this nature, rather it is the intent to merely
            enumberate mappings. 
            
            An application would determine the CPEs behind all cable
            modems by performing a SNMP GetNext starting with the
            variable bindings\:
            \- cdxCmToCpeInetAddressType.0
            \- cdxCmToCpeInetAddress.0
            
            It will return the IP address type and value tuple
            corresponding to the CPE with lowest IP address behind the
            cable modem with the lowest MAC address. An application can
            perform a SNMP GetNext operation with the following variable
            bindings\:
            \- cdxCmToCpeInetAddressType.x.y.z
            \- cdxCmToCpeInetAddress.x.y.z
            where x is MAC address of cable modem, and y.z is IP address
            type and value tuple of the reported CPE.
            An application can repeat this process until it has
            traversed the entire table.
            
            If the application only wants to know the CPEs behind a
            given cable modem, it can perform a SNMP GetNext opertaion
            with the following\:
            \- cdxCmToCpeInetAddressType.x
            \- cdxCmToCpeInetAddress.x
            where x is MAC address of cable modem.
            
            .. attribute:: cdxcmtocpecmmacaddress  (key)
            
            	The MAC address that uniquely identifies a cable modem that CPEs connects to
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcmtocpeinetaddresstype  (key)
            
            	The type of Internet address of the cdxCmToCpeInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtocpeinetaddress  (key)
            
            	This object identifies the address assigned to this CPE
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmToCpeTable.CdxCmToCpeEntry, self).__init__()

                self.yang_name = "cdxCmToCpeEntry"
                self.yang_parent_name = "cdxCmToCpeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxcmtocpecmmacaddress','cdxcmtocpeinetaddresstype','cdxcmtocpeinetaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxcmtocpecmmacaddress', (YLeaf(YType.str, 'cdxCmToCpeCmMacAddress'), ['str'])),
                    ('cdxcmtocpeinetaddresstype', (YLeaf(YType.enumeration, 'cdxCmToCpeInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cdxcmtocpeinetaddress', (YLeaf(YType.str, 'cdxCmToCpeInetAddress'), ['str'])),
                ])
                self.cdxcmtocpecmmacaddress = None
                self.cdxcmtocpeinetaddresstype = None
                self.cdxcmtocpeinetaddress = None
                self._segment_path = lambda: "cdxCmToCpeEntry" + "[cdxCmToCpeCmMacAddress='" + str(self.cdxcmtocpecmmacaddress) + "']" + "[cdxCmToCpeInetAddressType='" + str(self.cdxcmtocpeinetaddresstype) + "']" + "[cdxCmToCpeInetAddress='" + str(self.cdxcmtocpeinetaddress) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmToCpeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmToCpeTable.CdxCmToCpeEntry, ['cdxcmtocpecmmacaddress', 'cdxcmtocpeinetaddresstype', 'cdxcmtocpeinetaddress'], name, value)




    class CdxCpeToCmTable(Entity):
        """
        This table contains information about cable modems with CPE
        connects to.
        
        It is not intended to walk the whole table. An application
        would need to query this table base on the specific index.
        Otherwise, it will impact the CMTS performance due to the
        huge size of this table.
        
        The agent creates/destroys/modifies an entry whenever there
        is update for the cable modem that CPE connects to.
        
        .. attribute:: cdxcpetocmentry
        
        	An entry in cdxCpeToCmTable. Each entry contains information on the MAC address, IP Address, and status index for the  cable modem with a specific CPE connects to. Each entry is created if there is any cable modem with CPE connects to. Entries are ordered by cdxCpeToCmCpeMacAddress
        	**type**\: list of  		 :py:class:`CdxCpeToCmEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCpeToCmTable.CdxCpeToCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCpeToCmTable, self).__init__()

            self.yang_name = "cdxCpeToCmTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCpeToCmEntry", ("cdxcpetocmentry", CISCODOCSEXTMIB.CdxCpeToCmTable.CdxCpeToCmEntry))])
            self._leafs = OrderedDict()

            self.cdxcpetocmentry = YList(self)
            self._segment_path = lambda: "cdxCpeToCmTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCpeToCmTable, [], name, value)


        class CdxCpeToCmEntry(Entity):
            """
            An entry in cdxCpeToCmTable. Each entry contains information
            on the MAC address, IP Address, and status index for the 
            cable modem with a specific CPE connects to. Each entry is
            created if there is any cable modem with CPE connects to.
            Entries are ordered by cdxCpeToCmCpeMacAddress.
            
            .. attribute:: cdxcpetocmcpemacaddress  (key)
            
            	This object identifies the MAC address of the CPE
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcpetocmmacaddress
            
            	This object identifies the MAC address of the cable modem
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcpetocminetaddresstype
            
            	The type of Internet address of the cdxCpeToCmInetAddress object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cdxcpetocminetaddress
            
            	This object identifies the address assigned to this cable modem
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdxcpetocmstatusindex
            
            	An entry in docsIfCmtsCmStatusTable identifying status index of the cable modem which the CPE connects to
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCpeToCmTable.CdxCpeToCmEntry, self).__init__()

                self.yang_name = "cdxCpeToCmEntry"
                self.yang_parent_name = "cdxCpeToCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxcpetocmcpemacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxcpetocmcpemacaddress', (YLeaf(YType.str, 'cdxCpeToCmCpeMacAddress'), ['str'])),
                    ('cdxcpetocmmacaddress', (YLeaf(YType.str, 'cdxCpeToCmMacAddress'), ['str'])),
                    ('cdxcpetocminetaddresstype', (YLeaf(YType.enumeration, 'cdxCpeToCmInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cdxcpetocminetaddress', (YLeaf(YType.str, 'cdxCpeToCmInetAddress'), ['str'])),
                    ('cdxcpetocmstatusindex', (YLeaf(YType.int32, 'cdxCpeToCmStatusIndex'), ['int'])),
                ])
                self.cdxcpetocmcpemacaddress = None
                self.cdxcpetocmmacaddress = None
                self.cdxcpetocminetaddresstype = None
                self.cdxcpetocminetaddress = None
                self.cdxcpetocmstatusindex = None
                self._segment_path = lambda: "cdxCpeToCmEntry" + "[cdxCpeToCmCpeMacAddress='" + str(self.cdxcpetocmcpemacaddress) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCpeToCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCpeToCmTable.CdxCpeToCmEntry, ['cdxcpetocmcpemacaddress', 'cdxcpetocmmacaddress', 'cdxcpetocminetaddresstype', 'cdxcpetocminetaddress', 'cdxcpetocmstatusindex'], name, value)




    class CdxCpeIpPrefixTable(Entity):
        """
        The table contains a list CPE's IP Prefix management
        information.
        
        .. attribute:: cdxcpeipprefixentry
        
        	An entry contains information of CM's MAC, CPE's IP prefix type, CPE's IP prefix address, CPE's IP prefix length and CPE's MAC address. An entry is created if CPE is associated with a prefix
        	**type**\: list of  		 :py:class:`CdxCpeIpPrefixEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCpeIpPrefixTable.CdxCpeIpPrefixEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCpeIpPrefixTable, self).__init__()

            self.yang_name = "cdxCpeIpPrefixTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCpeIpPrefixEntry", ("cdxcpeipprefixentry", CISCODOCSEXTMIB.CdxCpeIpPrefixTable.CdxCpeIpPrefixEntry))])
            self._leafs = OrderedDict()

            self.cdxcpeipprefixentry = YList(self)
            self._segment_path = lambda: "cdxCpeIpPrefixTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCpeIpPrefixTable, [], name, value)


        class CdxCpeIpPrefixEntry(Entity):
            """
            An entry contains information of CM's MAC,
            CPE's IP prefix type, CPE's IP prefix address,
            CPE's IP prefix length and CPE's MAC address.
            An entry is created if CPE is associated with a prefix.
            
            .. attribute:: cdxcpeipprefixcmmacaddress  (key)
            
            	This object indicates the MAC address of the cable modem
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcpeipprefixtype  (key)
            
            	This object indicates the IP prefix type of the CPE. This is the type of cdxCpeIpPrefixAddress object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cdxcpeipprefixaddress  (key)
            
            	This object indicates the IP prefix address. The type of this address is determined by the value of  cdxCpeIpPrefixType object
            	**type**\: str
            
            	**length:** 1..96
            
            	**config**\: False
            
            .. attribute:: cdxcpeipprefixlen  (key)
            
            	This object indicates the IP prefix length of the CPE. This is the length of cdxCpeIpPrefixAddress object
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cdxcpeipprefixcpemacaddress
            
            	This object indicates the MAC address of CPE
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxcpeipprefixcpetype
            
            	This object indicates the type of CPE. Device Type\: B \- CM Bridge, R \- CM Router IP Assignment Method\: D \- DHCP the format looks like 'R/D'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCpeIpPrefixTable.CdxCpeIpPrefixEntry, self).__init__()

                self.yang_name = "cdxCpeIpPrefixEntry"
                self.yang_parent_name = "cdxCpeIpPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxcpeipprefixcmmacaddress','cdxcpeipprefixtype','cdxcpeipprefixaddress','cdxcpeipprefixlen']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxcpeipprefixcmmacaddress', (YLeaf(YType.str, 'cdxCpeIpPrefixCmMacAddress'), ['str'])),
                    ('cdxcpeipprefixtype', (YLeaf(YType.enumeration, 'cdxCpeIpPrefixType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cdxcpeipprefixaddress', (YLeaf(YType.str, 'cdxCpeIpPrefixAddress'), ['str'])),
                    ('cdxcpeipprefixlen', (YLeaf(YType.uint32, 'cdxCpeIpPrefixLen'), ['int'])),
                    ('cdxcpeipprefixcpemacaddress', (YLeaf(YType.str, 'cdxCpeIpPrefixCpeMacAddress'), ['str'])),
                    ('cdxcpeipprefixcpetype', (YLeaf(YType.str, 'cdxCpeIpPrefixCpeType'), ['str'])),
                ])
                self.cdxcpeipprefixcmmacaddress = None
                self.cdxcpeipprefixtype = None
                self.cdxcpeipprefixaddress = None
                self.cdxcpeipprefixlen = None
                self.cdxcpeipprefixcpemacaddress = None
                self.cdxcpeipprefixcpetype = None
                self._segment_path = lambda: "cdxCpeIpPrefixEntry" + "[cdxCpeIpPrefixCmMacAddress='" + str(self.cdxcpeipprefixcmmacaddress) + "']" + "[cdxCpeIpPrefixType='" + str(self.cdxcpeipprefixtype) + "']" + "[cdxCpeIpPrefixAddress='" + str(self.cdxcpeipprefixaddress) + "']" + "[cdxCpeIpPrefixLen='" + str(self.cdxcpeipprefixlen) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCpeIpPrefixTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCpeIpPrefixTable.CdxCpeIpPrefixEntry, ['cdxcpeipprefixcmmacaddress', 'cdxcpeipprefixtype', 'cdxcpeipprefixaddress', 'cdxcpeipprefixlen', 'cdxcpeipprefixcpemacaddress', 'cdxcpeipprefixcpetype'], name, value)




    class CdxIfUpstreamChannelExtTable(Entity):
        """
        This table contains upstream channel attributes for  
        automated Spectrum management, in addition to the ones
        provided by docsIfUpstreamChannelEntry.
        It also contains upstream channel attributes to count 
        the number of active,registered and total number of cable 
        modems on this upstream. 
        
        .. attribute:: cdxifupstreamchannelextentry
        
        	Additional objects for docsIfUpstreamChannelEntry,including  the secondary upstream channel modulation profile,the  lower bound for the channel width and the number of active, registered and total number of cable modems on this  upstream channel. 
        	**type**\: list of  		 :py:class:`CdxIfUpstreamChannelExtEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable.CdxIfUpstreamChannelExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable, self).__init__()

            self.yang_name = "cdxIfUpstreamChannelExtTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxIfUpstreamChannelExtEntry", ("cdxifupstreamchannelextentry", CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable.CdxIfUpstreamChannelExtEntry))])
            self._leafs = OrderedDict()

            self.cdxifupstreamchannelextentry = YList(self)
            self._segment_path = lambda: "cdxIfUpstreamChannelExtTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable, [], name, value)


        class CdxIfUpstreamChannelExtEntry(Entity):
            """
            Additional objects for docsIfUpstreamChannelEntry,including 
            the secondary upstream channel modulation profile,the 
            lower bound for the channel width and the number of active,
            registered and total number of cable modems on this 
            upstream channel. 
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelwidth
            
            	The lower bound for the bandwidth of this upstream channel.  The bandwidth specified by docsIfUpChannelWidth is used as the upper bound of the upstream channel. The two objects, docsIfUpChannelWidth and cdxIfUpChannelWidth, in  conjunction, define the upstream channel width range to be used for the automated spectrum management.  This object returns 0 if the channel width is undefined  or unknown.  For those upstreams in the linecards which do not have the automated spectrum management feature, this channel width is undefined and always has value 0. 
            	**type**\: int
            
            	**range:** 0..16000000
            
            	**config**\: False
            
            	**units**\: hertz
            
            .. attribute:: cdxifupchannelmodulationprofile
            
            	The secondary modulation profile for the upstream channel. This should be a QPSK modulation profile if the primary profile  is QAM\-16. The CMTS will switch from primary profile (QAM16) to  secondary profile (QPSK) depending on the noise level of a  particular spectrum band.  This is an entry identical to the docsIfModIndex in the  docsIfCmtsModulationTable that describes this channel. This channel is further instantiated there by a grouping of interval usage codes which together fully describe the channel modulation. This object returns 0 if the docsIfCmtsModulationTable does not exist or is empty. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelcmtotal
            
            	The total count of cable modems on this upstream channel since boot
            	**type**\: int
            
            	**range:** 0..8191
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelcmactive
            
            	The count of cable modems that are active.Active cable  modems are recognized by the cdxCmtsCmStatusValue other   than offline(1). 
            	**type**\: int
            
            	**range:** 0..8191
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelcmregistered
            
            	The count of cable modems that are registered and online on this upstream. Registered cable modems are those with one of the following values\: registrationComplete(6) of docsIfCmtsCmStatusValue OR online(12), kekRejected(10), onlineKekAssigned(6), tekRejected(11),onlineTekAssigned(7) of  cdxCmtsCmStatusValue
            	**type**\: int
            
            	**range:** 0..8191
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelinputpowerlevel
            
            	The Upstream Input power level at the CMTS interface. This is the expected power level and is different from the actual power received. If not configured the default value is 0 dBmV and is also the optimum setting power level for the upstream. For FPGA line cards, the valid range is <\-10 to 10> dBmV and for ASIC Line cards, it is  <\-10  to 25> dBmV. 
            	**type**\: int
            
            	**range:** \-100..250
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelavgutil
            
            	The average percentage of upstream channel utilization.  This item indicates the running average of percent channel utilization in CMTS upstream Mac scheduler. 
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cdxifupchannelavgcontslots
            
            	The average percentage of contention mini\-slots. This item indicates the running average of percent contention mini\-slots in CMTS upstream Mac scheduler. 
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cdxifupchannelrangeslots
            
            	The average percentage of initial ranging mini\-slots.  This item indicates the running average of percent initial ranging mini\-slots in CMTS upstream Mac scheduler. 
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cdxifupchannelnumactiveugs
            
            	This object indicates the number of active  Unsolicited Grant Service (UGS) on a given upstream. This would be used for the user to evaluate traffic  load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to  support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelmaxugslastonehour
            
            	This object indicates the maximum number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelminugslastonehour
            
            	This object indicates the minimum number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelavgugslastonehour
            
            	This object indicates the average number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelmaxugslastfivemins
            
            	This object indicates the maximum number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would  be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelminugslastfivemins
            
            	This object indicates the minimum number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would  be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxifupchannelavgugslastfivemins
            
            	This object indicates the average number of  Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would  be used for the user to evaluate traffic load at any given time of the day.  The Unsolicited Grant Service (UGS) is designed to support real\-time service flows that generate fixed size data packets on a periodic basis. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable.CdxIfUpstreamChannelExtEntry, self).__init__()

                self.yang_name = "cdxIfUpstreamChannelExtEntry"
                self.yang_parent_name = "cdxIfUpstreamChannelExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxifupchannelwidth', (YLeaf(YType.int32, 'cdxIfUpChannelWidth'), ['int'])),
                    ('cdxifupchannelmodulationprofile', (YLeaf(YType.uint32, 'cdxIfUpChannelModulationProfile'), ['int'])),
                    ('cdxifupchannelcmtotal', (YLeaf(YType.int32, 'cdxIfUpChannelCmTotal'), ['int'])),
                    ('cdxifupchannelcmactive', (YLeaf(YType.int32, 'cdxIfUpChannelCmActive'), ['int'])),
                    ('cdxifupchannelcmregistered', (YLeaf(YType.int32, 'cdxIfUpChannelCmRegistered'), ['int'])),
                    ('cdxifupchannelinputpowerlevel', (YLeaf(YType.int32, 'cdxIfUpChannelInputPowerLevel'), ['int'])),
                    ('cdxifupchannelavgutil', (YLeaf(YType.int32, 'cdxIfUpChannelAvgUtil'), ['int'])),
                    ('cdxifupchannelavgcontslots', (YLeaf(YType.int32, 'cdxIfUpChannelAvgContSlots'), ['int'])),
                    ('cdxifupchannelrangeslots', (YLeaf(YType.int32, 'cdxIfUpChannelRangeSlots'), ['int'])),
                    ('cdxifupchannelnumactiveugs', (YLeaf(YType.uint32, 'cdxIfUpChannelNumActiveUGS'), ['int'])),
                    ('cdxifupchannelmaxugslastonehour', (YLeaf(YType.uint32, 'cdxIfUpChannelMaxUGSLastOneHour'), ['int'])),
                    ('cdxifupchannelminugslastonehour', (YLeaf(YType.uint32, 'cdxIfUpChannelMinUGSLastOneHour'), ['int'])),
                    ('cdxifupchannelavgugslastonehour', (YLeaf(YType.uint32, 'cdxIfUpChannelAvgUGSLastOneHour'), ['int'])),
                    ('cdxifupchannelmaxugslastfivemins', (YLeaf(YType.uint32, 'cdxIfUpChannelMaxUGSLastFiveMins'), ['int'])),
                    ('cdxifupchannelminugslastfivemins', (YLeaf(YType.uint32, 'cdxIfUpChannelMinUGSLastFiveMins'), ['int'])),
                    ('cdxifupchannelavgugslastfivemins', (YLeaf(YType.uint32, 'cdxIfUpChannelAvgUGSLastFiveMins'), ['int'])),
                ])
                self.ifindex = None
                self.cdxifupchannelwidth = None
                self.cdxifupchannelmodulationprofile = None
                self.cdxifupchannelcmtotal = None
                self.cdxifupchannelcmactive = None
                self.cdxifupchannelcmregistered = None
                self.cdxifupchannelinputpowerlevel = None
                self.cdxifupchannelavgutil = None
                self.cdxifupchannelavgcontslots = None
                self.cdxifupchannelrangeslots = None
                self.cdxifupchannelnumactiveugs = None
                self.cdxifupchannelmaxugslastonehour = None
                self.cdxifupchannelminugslastonehour = None
                self.cdxifupchannelavgugslastonehour = None
                self.cdxifupchannelmaxugslastfivemins = None
                self.cdxifupchannelminugslastfivemins = None
                self.cdxifupchannelavgugslastfivemins = None
                self._segment_path = lambda: "cdxIfUpstreamChannelExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxIfUpstreamChannelExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxIfUpstreamChannelExtTable.CdxIfUpstreamChannelExtEntry, ['ifindex', 'cdxifupchannelwidth', 'cdxifupchannelmodulationprofile', 'cdxifupchannelcmtotal', 'cdxifupchannelcmactive', 'cdxifupchannelcmregistered', 'cdxifupchannelinputpowerlevel', 'cdxifupchannelavgutil', 'cdxifupchannelavgcontslots', 'cdxifupchannelrangeslots', 'cdxifupchannelnumactiveugs', 'cdxifupchannelmaxugslastonehour', 'cdxifupchannelminugslastonehour', 'cdxifupchannelavgugslastonehour', 'cdxifupchannelmaxugslastfivemins', 'cdxifupchannelminugslastfivemins', 'cdxifupchannelavgugslastfivemins'], name, value)




    class CdxWBResilCmTable(Entity):
        """
        This table contains information about partial service cable
        modems (CM), including both downstream and upstream partial
        service modems.
        
        .. attribute:: cdxwbresilcmentry
        
        	The list contains information for a partial service cable modem (CM).  Provided the following information for a partial service cable modem\: How many downstream channels in total; How many upstream channels in total; How many active downstream channels; How many active upstream channels; Which downstream channels are in partial service mode; Which upstream channels are in partial service mode;
        	**type**\: list of  		 :py:class:`CdxWBResilCmEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxWBResilCmTable.CdxWBResilCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxWBResilCmTable, self).__init__()

            self.yang_name = "cdxWBResilCmTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxWBResilCmEntry", ("cdxwbresilcmentry", CISCODOCSEXTMIB.CdxWBResilCmTable.CdxWBResilCmEntry))])
            self._leafs = OrderedDict()

            self.cdxwbresilcmentry = YList(self)
            self._segment_path = lambda: "cdxWBResilCmTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxWBResilCmTable, [], name, value)


        class CdxWBResilCmEntry(Entity):
            """
            The list contains information for a partial service cable modem
            (CM).
            
            Provided the following information for a partial service cable
            modem\:
            How many downstream channels in total;
            How many upstream channels in total;
            How many active downstream channels;
            How many active upstream channels;
            Which downstream channels are in partial service mode;
            Which upstream channels are in partial service mode;
            
            .. attribute:: cdxwbresilcmindex  (key)
            
            	This attribute uniquely identifies a CM.  The CMTS must assign a single id value for each CM MAC address seen by the CMTS.  The CMTS should ensure that the association between an Id and MAC Address remains constant during CMTS uptime
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmmacaddr
            
            	This attribute represents the MAC address of the CM. If the CM has multiple MAC addresses, this is the MAC address associated with the MAC Domain interface
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmtotaldsnum
            
            	Total downstream channel number of the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmtotalusnum
            
            	Total upstream channel number of the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmcurrentdsnum
            
            	Current active downstream channel number, it's the total downstream channel minus downstream partial service channel number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmcurrentusnum
            
            	Current active upstream channel number, it's the total upstream channel minus upstream partial service channel number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmimpaireddschindex
            
            	Impaired downstream channel index list. The index in list is rf channel ifIndex. If there's no downstream channel impaired, return empty. The output looks like\: '137000 137001 137002'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdxwbresilcmimpaireduschindex
            
            	Impaired upstream channel index list. The index in list is upstream channel ifIndex. If there's no upstream channel impaired, return empty. The output looks like\: '196408 196409 196410'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxWBResilCmTable.CdxWBResilCmEntry, self).__init__()

                self.yang_name = "cdxWBResilCmEntry"
                self.yang_parent_name = "cdxWBResilCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxwbresilcmindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxwbresilcmindex', (YLeaf(YType.uint32, 'cdxWBResilCmIndex'), ['int'])),
                    ('cdxwbresilcmmacaddr', (YLeaf(YType.str, 'cdxWBResilCmMacAddr'), ['str'])),
                    ('cdxwbresilcmtotaldsnum', (YLeaf(YType.uint32, 'cdxWBResilCmTotalDsNum'), ['int'])),
                    ('cdxwbresilcmtotalusnum', (YLeaf(YType.uint32, 'cdxWBResilCmTotalUsNum'), ['int'])),
                    ('cdxwbresilcmcurrentdsnum', (YLeaf(YType.uint32, 'cdxWBResilCmCurrentDsNum'), ['int'])),
                    ('cdxwbresilcmcurrentusnum', (YLeaf(YType.uint32, 'cdxWBResilCmCurrentUsNum'), ['int'])),
                    ('cdxwbresilcmimpaireddschindex', (YLeaf(YType.str, 'cdxWBResilCmImpairedDsChIndex'), ['str'])),
                    ('cdxwbresilcmimpaireduschindex', (YLeaf(YType.str, 'cdxWBResilCmImpairedUsChIndex'), ['str'])),
                ])
                self.cdxwbresilcmindex = None
                self.cdxwbresilcmmacaddr = None
                self.cdxwbresilcmtotaldsnum = None
                self.cdxwbresilcmtotalusnum = None
                self.cdxwbresilcmcurrentdsnum = None
                self.cdxwbresilcmcurrentusnum = None
                self.cdxwbresilcmimpaireddschindex = None
                self.cdxwbresilcmimpaireduschindex = None
                self._segment_path = lambda: "cdxWBResilCmEntry" + "[cdxWBResilCmIndex='" + str(self.cdxwbresilcmindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxWBResilCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxWBResilCmTable.CdxWBResilCmEntry, ['cdxwbresilcmindex', 'cdxwbresilcmmacaddr', 'cdxwbresilcmtotaldsnum', 'cdxwbresilcmtotalusnum', 'cdxwbresilcmcurrentdsnum', 'cdxwbresilcmcurrentusnum', 'cdxwbresilcmimpaireddschindex', 'cdxwbresilcmimpaireduschindex'], name, value)




    class CdxRFtoPrimaryChannelMappingTable(Entity):
        """
        This table contains information of the mapping of
        the physical RF channels to the primary RF channels.
        
        .. attribute:: cdxrftoprimarychannelmappingentry
        
        	An Entry provides the association between the physical RF channels and the primary RF Channels
        	**type**\: list of  		 :py:class:`CdxRFtoPrimaryChannelMappingEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable.CdxRFtoPrimaryChannelMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable, self).__init__()

            self.yang_name = "cdxRFtoPrimaryChannelMappingTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxRFtoPrimaryChannelMappingEntry", ("cdxrftoprimarychannelmappingentry", CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable.CdxRFtoPrimaryChannelMappingEntry))])
            self._leafs = OrderedDict()

            self.cdxrftoprimarychannelmappingentry = YList(self)
            self._segment_path = lambda: "cdxRFtoPrimaryChannelMappingTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable, [], name, value)


        class CdxRFtoPrimaryChannelMappingEntry(Entity):
            """
            An Entry provides the association between the physical
            RF channels and the primary RF Channels.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxprimarychannelifindex
            
            	The ifIndex of the primary channel interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable.CdxRFtoPrimaryChannelMappingEntry, self).__init__()

                self.yang_name = "cdxRFtoPrimaryChannelMappingEntry"
                self.yang_parent_name = "cdxRFtoPrimaryChannelMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxprimarychannelifindex', (YLeaf(YType.int32, 'cdxPrimaryChannelIfIndex'), ['int'])),
                ])
                self.ifindex = None
                self.cdxprimarychannelifindex = None
                self._segment_path = lambda: "cdxRFtoPrimaryChannelMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxRFtoPrimaryChannelMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxRFtoPrimaryChannelMappingTable.CdxRFtoPrimaryChannelMappingEntry, ['ifindex', 'cdxprimarychannelifindex'], name, value)




    class CdxPrimaryChanneltoRFMappingTable(Entity):
        """
        This table contains information of the mapping of
        the primary RF channels to the physical RF channels.
        
        .. attribute:: cdxprimarychanneltorfmappingentry
        
        	An Entry provides the association between the primary RF channels and the physical RF Channels
        	**type**\: list of  		 :py:class:`CdxPrimaryChanneltoRFMappingEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable.CdxPrimaryChanneltoRFMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable, self).__init__()

            self.yang_name = "cdxPrimaryChanneltoRFMappingTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxPrimaryChanneltoRFMappingEntry", ("cdxprimarychanneltorfmappingentry", CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable.CdxPrimaryChanneltoRFMappingEntry))])
            self._leafs = OrderedDict()

            self.cdxprimarychanneltorfmappingentry = YList(self)
            self._segment_path = lambda: "cdxPrimaryChanneltoRFMappingTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable, [], name, value)


        class CdxPrimaryChanneltoRFMappingEntry(Entity):
            """
            An Entry provides the association between the primary
            RF channels and the physical RF Channels.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxphysicalrfifindex
            
            	The ifIndex of the physical RF channel interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable.CdxPrimaryChanneltoRFMappingEntry, self).__init__()

                self.yang_name = "cdxPrimaryChanneltoRFMappingEntry"
                self.yang_parent_name = "cdxPrimaryChanneltoRFMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxphysicalrfifindex', (YLeaf(YType.int32, 'cdxPhysicalRFIfIndex'), ['int'])),
                ])
                self.ifindex = None
                self.cdxphysicalrfifindex = None
                self._segment_path = lambda: "cdxPrimaryChanneltoRFMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxPrimaryChanneltoRFMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxPrimaryChanneltoRFMappingTable.CdxPrimaryChanneltoRFMappingEntry, ['ifindex', 'cdxphysicalrfifindex'], name, value)




    class CdxCmtsMtcCmTable(Entity):
        """
        This table contains CM management information of Transmit
        Channel Set(TCS) in the system.
        
        .. attribute:: cdxcmtsmtccmentry
        
        	An entry provides the CM statistics and management information of a specific TCS. The interface populated in this table is of ifType = docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`CdxCmtsMtcCmEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsMtcCmTable.CdxCmtsMtcCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsMtcCmTable, self).__init__()

            self.yang_name = "cdxCmtsMtcCmTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsMtcCmEntry", ("cdxcmtsmtccmentry", CISCODOCSEXTMIB.CdxCmtsMtcCmTable.CdxCmtsMtcCmEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtsmtccmentry = YList(self)
            self._segment_path = lambda: "cdxCmtsMtcCmTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsMtcCmTable, [], name, value)


        class CdxCmtsMtcCmEntry(Entity):
            """
            An entry provides the CM statistics and management
            information of a specific TCS. The interface populated in this
            table is of ifType = docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtctcsid  (key)
            
            	This object indicates the Id of the Transmit Channel Set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmtotal
            
            	This object indicates the total number of cable modems which use this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmoperational
            
            	This object indicates the number of operational cable modems which uses this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmregistered
            
            	This object indicates the number of registered cable modems which use this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmunregistered
            
            	This object indicates the number of unregistered cable modem which use this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmoffline
            
            	This object indicates the number of offline cable modems which uses this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtccmwideband
            
            	This object indicates the number of operational cable modems which are in wideband state and use this TCS in the MAC domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsmtcupstreambondgrp
            
            	This object specifies the upstream channel bonding group
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsMtcCmTable.CdxCmtsMtcCmEntry, self).__init__()

                self.yang_name = "cdxCmtsMtcCmEntry"
                self.yang_parent_name = "cdxCmtsMtcCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxcmtsmtctcsid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxcmtsmtctcsid', (YLeaf(YType.uint32, 'cdxCmtsMtcTcsId'), ['int'])),
                    ('cdxcmtsmtccmtotal', (YLeaf(YType.uint32, 'cdxCmtsMtcCmTotal'), ['int'])),
                    ('cdxcmtsmtccmoperational', (YLeaf(YType.uint32, 'cdxCMtsMtcCmOperational'), ['int'])),
                    ('cdxcmtsmtccmregistered', (YLeaf(YType.uint32, 'cdxCmtsMtcCmRegistered'), ['int'])),
                    ('cdxcmtsmtccmunregistered', (YLeaf(YType.uint32, 'cdxCmtsMtcCmUnregistered'), ['int'])),
                    ('cdxcmtsmtccmoffline', (YLeaf(YType.uint32, 'cdxCmtsMtcCmOffline'), ['int'])),
                    ('cdxcmtsmtccmwideband', (YLeaf(YType.uint32, 'cdxCmtsMtcCmWideband'), ['int'])),
                    ('cdxcmtsmtcupstreambondgrp', (YLeaf(YType.str, 'cdxCmtsMtcUpstreamBondGrp'), ['str'])),
                ])
                self.ifindex = None
                self.cdxcmtsmtctcsid = None
                self.cdxcmtsmtccmtotal = None
                self.cdxcmtsmtccmoperational = None
                self.cdxcmtsmtccmregistered = None
                self.cdxcmtsmtccmunregistered = None
                self.cdxcmtsmtccmoffline = None
                self.cdxcmtsmtccmwideband = None
                self.cdxcmtsmtcupstreambondgrp = None
                self._segment_path = lambda: "cdxCmtsMtcCmEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxCmtsMtcTcsId='" + str(self.cdxcmtsmtctcsid) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsMtcCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsMtcCmTable.CdxCmtsMtcCmEntry, ['ifindex', 'cdxcmtsmtctcsid', 'cdxcmtsmtccmtotal', 'cdxcmtsmtccmoperational', 'cdxcmtsmtccmregistered', 'cdxcmtsmtccmunregistered', 'cdxcmtsmtccmoffline', 'cdxcmtsmtccmwideband', 'cdxcmtsmtcupstreambondgrp'], name, value)




    class CdxCmtsUscbSflowTable(Entity):
        """
        This table contains the Upstream Channel Bonding
        Service Flow management information.
        
        .. attribute:: cdxcmtsuscbsflowentry
        
        	A entry contains the Service Flow statistics for a specific Upstream Channel Bonding group. The interface populated in this table is of ifType = docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`CdxCmtsUscbSflowEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxCmtsUscbSflowTable.CdxCmtsUscbSflowEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxCmtsUscbSflowTable, self).__init__()

            self.yang_name = "cdxCmtsUscbSflowTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxCmtsUscbSflowEntry", ("cdxcmtsuscbsflowentry", CISCODOCSEXTMIB.CdxCmtsUscbSflowTable.CdxCmtsUscbSflowEntry))])
            self._leafs = OrderedDict()

            self.cdxcmtsuscbsflowentry = YList(self)
            self._segment_path = lambda: "cdxCmtsUscbSflowTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsUscbSflowTable, [], name, value)


        class CdxCmtsUscbSflowEntry(Entity):
            """
            A entry contains the Service Flow statistics for a specific
            Upstream Channel Bonding group. The interface populated in this
            table is of ifType = docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxcmtsusbondinggrpid  (key)
            
            	This object indicates upstream bonding group identifier within the MAC Domain
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbsftotal
            
            	This object indicates the total number of service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbsfpri
            
            	This object indicates the total number of  primary service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbstaticsfbe
            
            	This object indicates the number of static BE service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbstaticsfugs
            
            	This object indicates the number of static UGS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbstaticsfugsad
            
            	This object indicates the number of static UGS\-AD service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbstaticsfrtps
            
            	This object indicates the number of static RTPS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbstaticsfnrtps
            
            	This object indicates the number of static NRTPS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdynsfbe
            
            	This object indicates the number of dynamic BE service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdynsfugs
            
            	This object indicates the number of dynamic UGS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdynsfugsad
            
            	This object indicates the number of dynamic UGS\-Ad service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdynsfrtps
            
            	This object indicates the number of dynamic RTPS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdynsfnrtps
            
            	This object indicates the number of dynamic NRTPS service flows which use this upstream channel bonding group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdxcmtsuscbdescr
            
            	This object indicates the description of upstream channel bonding group
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxCmtsUscbSflowTable.CdxCmtsUscbSflowEntry, self).__init__()

                self.yang_name = "cdxCmtsUscbSflowEntry"
                self.yang_parent_name = "cdxCmtsUscbSflowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxcmtsusbondinggrpid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxcmtsusbondinggrpid', (YLeaf(YType.uint32, 'cdxCmtsUsBondingGrpId'), ['int'])),
                    ('cdxcmtsuscbsftotal', (YLeaf(YType.uint32, 'cdxCmtsUscbSfTotal'), ['int'])),
                    ('cdxcmtsuscbsfpri', (YLeaf(YType.uint32, 'cdxCmtsUscbSfPri'), ['int'])),
                    ('cdxcmtsuscbstaticsfbe', (YLeaf(YType.uint32, 'cdxCmtsUscbStaticSfBe'), ['int'])),
                    ('cdxcmtsuscbstaticsfugs', (YLeaf(YType.uint32, 'cdxCmtsUscbStaticSfUgs'), ['int'])),
                    ('cdxcmtsuscbstaticsfugsad', (YLeaf(YType.uint32, 'cdxCmtsUscbStaticSfUgsad'), ['int'])),
                    ('cdxcmtsuscbstaticsfrtps', (YLeaf(YType.uint32, 'cdxCmtsUscbStaticSfRtps'), ['int'])),
                    ('cdxcmtsuscbstaticsfnrtps', (YLeaf(YType.uint32, 'cdxCmtsUscbStaticSfNrtps'), ['int'])),
                    ('cdxcmtsuscbdynsfbe', (YLeaf(YType.uint32, 'cdxCmtsUscbDynSfBe'), ['int'])),
                    ('cdxcmtsuscbdynsfugs', (YLeaf(YType.uint32, 'cdxCmtsUscbDynSfUgs'), ['int'])),
                    ('cdxcmtsuscbdynsfugsad', (YLeaf(YType.uint32, 'cdxCmtsUscbDynSfUgsad'), ['int'])),
                    ('cdxcmtsuscbdynsfrtps', (YLeaf(YType.uint32, 'cdxCmtsUscbDynSfRtps'), ['int'])),
                    ('cdxcmtsuscbdynsfnrtps', (YLeaf(YType.uint32, 'cdxCmtsUscbDynSfNrtps'), ['int'])),
                    ('cdxcmtsuscbdescr', (YLeaf(YType.str, 'cdxCmtsUscbDescr'), ['str'])),
                ])
                self.ifindex = None
                self.cdxcmtsusbondinggrpid = None
                self.cdxcmtsuscbsftotal = None
                self.cdxcmtsuscbsfpri = None
                self.cdxcmtsuscbstaticsfbe = None
                self.cdxcmtsuscbstaticsfugs = None
                self.cdxcmtsuscbstaticsfugsad = None
                self.cdxcmtsuscbstaticsfrtps = None
                self.cdxcmtsuscbstaticsfnrtps = None
                self.cdxcmtsuscbdynsfbe = None
                self.cdxcmtsuscbdynsfugs = None
                self.cdxcmtsuscbdynsfugsad = None
                self.cdxcmtsuscbdynsfrtps = None
                self.cdxcmtsuscbdynsfnrtps = None
                self.cdxcmtsuscbdescr = None
                self._segment_path = lambda: "cdxCmtsUscbSflowEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxCmtsUsBondingGrpId='" + str(self.cdxcmtsusbondinggrpid) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxCmtsUscbSflowTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxCmtsUscbSflowTable.CdxCmtsUscbSflowEntry, ['ifindex', 'cdxcmtsusbondinggrpid', 'cdxcmtsuscbsftotal', 'cdxcmtsuscbsfpri', 'cdxcmtsuscbstaticsfbe', 'cdxcmtsuscbstaticsfugs', 'cdxcmtsuscbstaticsfugsad', 'cdxcmtsuscbstaticsfrtps', 'cdxcmtsuscbstaticsfnrtps', 'cdxcmtsuscbdynsfbe', 'cdxcmtsuscbdynsfugs', 'cdxcmtsuscbdynsfugsad', 'cdxcmtsuscbdynsfrtps', 'cdxcmtsuscbdynsfnrtps', 'cdxcmtsuscbdescr'], name, value)




    class CdxRPDGS7KTable(Entity):
        """
        The cdxRPDGS7KTable contains the attributes of GS7K. 
        An Entry exists for each instance. 
        It is indexed by GS7K's MacAddress.
        
        .. attribute:: cdxrpdgs7kentry
        
        	The list of statistics for all the sensor,  such as volatage, the state of TriSwitch
        	**type**\: list of  		 :py:class:`CdxRPDGS7KEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxRPDGS7KTable, self).__init__()

            self.yang_name = "cdxRPDGS7KTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxRPDGS7KEntry", ("cdxrpdgs7kentry", CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry))])
            self._leafs = OrderedDict()

            self.cdxrpdgs7kentry = YList(self)
            self._segment_path = lambda: "cdxRPDGS7KTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxRPDGS7KTable, [], name, value)


        class CdxRPDGS7KEntry(Entity):
            """
            The list of statistics for all the sensor, 
            such as volatage, the state of TriSwitch.
            
            .. attribute:: cdxrpdgs7kmacaddress  (key)
            
            	This is MacAddress of RPDGS7K which is used for index
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: cdxrpdgs7kps1p24v
            
            	This is the Object of RPDGS7KPS1p24v
            	**type**\: int
            
            	**range:** 0..3000
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps1p8v
            
            	This is the Object of RPDGS7KPS1p8v
            	**type**\: int
            
            	**range:** 0..1000
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps1p5v
            
            	This is the Object of RPDGS7KPS1p5v
            	**type**\: int
            
            	**range:** 0..625
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps1n6v
            
            	This is the Object of RPDGS7KPS1n6v
            	**type**\: int
            
            	**range:** 0..800
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps1ac
            
            	This is the Object of RPDGS7KPS1AC
            	**type**\: int
            
            	**range:** 300..2000
            
            	**config**\: False
            
            	**units**\: 0.1VAC
            
            .. attribute:: cdxrpdgs7kps2p24v
            
            	RPDGS7KPS2p24v
            	**type**\: int
            
            	**range:** 0..3000
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps2p8v
            
            	This is the Object of RPDGS7KPS2p8v
            	**type**\: int
            
            	**range:** 0..1000
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps2p5v
            
            	This is the Object of RPDGS7KPS2p5v
            	**type**\: int
            
            	**range:** 0..625
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps2n6v
            
            	This is the Object of RPDGS7KPS2n6v
            	**type**\: int
            
            	**range:** 0..800
            
            	**config**\: False
            
            	**units**\: 0.01VDC
            
            .. attribute:: cdxrpdgs7kps2ac
            
            	This is the Object of RPDGS7KPS2AC
            	**type**\: int
            
            	**range:** 300..2000
            
            	**config**\: False
            
            	**units**\: 0.1VAC
            
            .. attribute:: cdxrpdgs7ktx1optpower
            
            	This is the Object of RPDGS7K Tx4 Opt Power
            	**type**\: int
            
            	**range:** 0..300
            
            	**config**\: False
            
            	**units**\: 0.01mW
            
            .. attribute:: cdxrpdgs7krx1optpower
            
            	This is the Object of RPDGS7K Rx4 Opt Power
            	**type**\: int
            
            	**range:** 0..300
            
            	**config**\: False
            
            	**units**\: 0.01mW
            
            .. attribute:: cdxrpdgs7ktriswitch
            
            	This is the Object of RPDGS7K TriSwitch, The relationship which the number indicates is    low(1) for \-6dB high(2) for 0dB pad(3) for off
            	**type**\:  :py:class:`CdxRPDGS7KTriSwitch <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry.CdxRPDGS7KTriSwitch>`
            
            	**config**\: False
            
            .. attribute:: cdxrpdgs7ktamp
            
            	This is the Object of RPDGS7K Tamp
            	**type**\:  :py:class:`CdxRPDGS7KTamp <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry.CdxRPDGS7KTamp>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry, self).__init__()

                self.yang_name = "cdxRPDGS7KEntry"
                self.yang_parent_name = "cdxRPDGS7KTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdxrpdgs7kmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdxrpdgs7kmacaddress', (YLeaf(YType.str, 'cdxRPDGS7KMacAddress'), ['str'])),
                    ('cdxrpdgs7kps1p24v', (YLeaf(YType.int32, 'cdxRPDGS7KPS1p24v'), ['int'])),
                    ('cdxrpdgs7kps1p8v', (YLeaf(YType.int32, 'cdxRPDGS7KPS1p8v'), ['int'])),
                    ('cdxrpdgs7kps1p5v', (YLeaf(YType.int32, 'cdxRPDGS7KPS1p5v'), ['int'])),
                    ('cdxrpdgs7kps1n6v', (YLeaf(YType.int32, 'cdxRPDGS7KPS1n6v'), ['int'])),
                    ('cdxrpdgs7kps1ac', (YLeaf(YType.int32, 'cdxRPDGS7KPS1AC'), ['int'])),
                    ('cdxrpdgs7kps2p24v', (YLeaf(YType.int32, 'cdxRPDGS7KPS2p24v'), ['int'])),
                    ('cdxrpdgs7kps2p8v', (YLeaf(YType.int32, 'cdxRPDGS7KPS2p8v'), ['int'])),
                    ('cdxrpdgs7kps2p5v', (YLeaf(YType.int32, 'cdxRPDGS7KPS2p5v'), ['int'])),
                    ('cdxrpdgs7kps2n6v', (YLeaf(YType.int32, 'cdxRPDGS7KPS2n6v'), ['int'])),
                    ('cdxrpdgs7kps2ac', (YLeaf(YType.int32, 'cdxRPDGS7KPS2AC'), ['int'])),
                    ('cdxrpdgs7ktx1optpower', (YLeaf(YType.int32, 'cdxRPDGS7KTx1OptPower'), ['int'])),
                    ('cdxrpdgs7krx1optpower', (YLeaf(YType.int32, 'cdxRPDGS7KRx1OptPower'), ['int'])),
                    ('cdxrpdgs7ktriswitch', (YLeaf(YType.enumeration, 'cdxRPDGS7KTriSwitch'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxRPDGS7KTable.CdxRPDGS7KEntry.CdxRPDGS7KTriSwitch')])),
                    ('cdxrpdgs7ktamp', (YLeaf(YType.enumeration, 'cdxRPDGS7KTamp'), [('ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB', 'CISCODOCSEXTMIB', 'CdxRPDGS7KTable.CdxRPDGS7KEntry.CdxRPDGS7KTamp')])),
                ])
                self.cdxrpdgs7kmacaddress = None
                self.cdxrpdgs7kps1p24v = None
                self.cdxrpdgs7kps1p8v = None
                self.cdxrpdgs7kps1p5v = None
                self.cdxrpdgs7kps1n6v = None
                self.cdxrpdgs7kps1ac = None
                self.cdxrpdgs7kps2p24v = None
                self.cdxrpdgs7kps2p8v = None
                self.cdxrpdgs7kps2p5v = None
                self.cdxrpdgs7kps2n6v = None
                self.cdxrpdgs7kps2ac = None
                self.cdxrpdgs7ktx1optpower = None
                self.cdxrpdgs7krx1optpower = None
                self.cdxrpdgs7ktriswitch = None
                self.cdxrpdgs7ktamp = None
                self._segment_path = lambda: "cdxRPDGS7KEntry" + "[cdxRPDGS7KMacAddress='" + str(self.cdxrpdgs7kmacaddress) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxRPDGS7KTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxRPDGS7KTable.CdxRPDGS7KEntry, ['cdxrpdgs7kmacaddress', 'cdxrpdgs7kps1p24v', 'cdxrpdgs7kps1p8v', 'cdxrpdgs7kps1p5v', 'cdxrpdgs7kps1n6v', 'cdxrpdgs7kps1ac', 'cdxrpdgs7kps2p24v', 'cdxrpdgs7kps2p8v', 'cdxrpdgs7kps2p5v', 'cdxrpdgs7kps2n6v', 'cdxrpdgs7kps2ac', 'cdxrpdgs7ktx1optpower', 'cdxrpdgs7krx1optpower', 'cdxrpdgs7ktriswitch', 'cdxrpdgs7ktamp'], name, value)

            class CdxRPDGS7KTamp(Enum):
                """
                CdxRPDGS7KTamp (Enum Class)

                This is the Object of RPDGS7K Tamp

                .. data:: intact = 1

                .. data:: compromised = 2

                """

                intact = Enum.YLeaf(1, "intact")

                compromised = Enum.YLeaf(2, "compromised")


            class CdxRPDGS7KTriSwitch(Enum):
                """
                CdxRPDGS7KTriSwitch (Enum Class)

                This is the Object of RPDGS7K TriSwitch,

                The relationship which the number indicates is   

                low(1) for \-6dB

                high(2) for 0dB

                pad(3) for off

                .. data:: low = 1

                .. data:: high = 2

                .. data:: pad = 3

                """

                low = Enum.YLeaf(1, "low")

                high = Enum.YLeaf(2, "high")

                pad = Enum.YLeaf(3, "pad")





    class CdxBundleIpHelperTable(Entity):
        """
        A list of cable helper entries on Bundle/Sub\-Bundle interface.
        
        .. attribute:: cdxbundleiphelperentry
        
        	The conceptual row of cdxBundleIpHelperEntry. An instance exists for Cable Bundle/Sub\-Bundle Interface
        	**type**\: list of  		 :py:class:`CdxBundleIpHelperEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIpHelperTable.CdxBundleIpHelperEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxBundleIpHelperTable, self).__init__()

            self.yang_name = "cdxBundleIpHelperTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxBundleIpHelperEntry", ("cdxbundleiphelperentry", CISCODOCSEXTMIB.CdxBundleIpHelperTable.CdxBundleIpHelperEntry))])
            self._leafs = OrderedDict()

            self.cdxbundleiphelperentry = YList(self)
            self._segment_path = lambda: "cdxBundleIpHelperTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIpHelperTable, [], name, value)


        class CdxBundleIpHelperEntry(Entity):
            """
            The conceptual row of cdxBundleIpHelperEntry.
            An instance exists for Cable Bundle/Sub\-Bundle Interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxbundlehelperaddr  (key)
            
            	Cable helper IP address
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdxbundlehelpertype
            
            	This object describes which kind of device will be associated to a cable helper. The entity may support more than one device  class. For example, the entity supports both host and mta. Therefore, bit 1 and bit 3 are set to 1 for this object. If  all bits are cleared, the entity supports all device types. Note that BITS are encoded most significant bit first
            	**type**\:  :py:class:`CdxBundleHelperType <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIpHelperTable.CdxBundleIpHelperEntry.CdxBundleHelperType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxBundleIpHelperTable.CdxBundleIpHelperEntry, self).__init__()

                self.yang_name = "cdxBundleIpHelperEntry"
                self.yang_parent_name = "cdxBundleIpHelperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxbundlehelperaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxbundlehelperaddr', (YLeaf(YType.str, 'cdxBundleHelperAddr'), ['str'])),
                    ('cdxbundlehelpertype', (YLeaf(YType.bits, 'cdxBundleHelperType'), ['Bits'])),
                ])
                self.ifindex = None
                self.cdxbundlehelperaddr = None
                self.cdxbundlehelpertype = Bits()
                self._segment_path = lambda: "cdxBundleIpHelperEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxBundleHelperAddr='" + str(self.cdxbundlehelperaddr) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxBundleIpHelperTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIpHelperTable.CdxBundleIpHelperEntry, ['ifindex', 'cdxbundlehelperaddr', 'cdxbundlehelpertype'], name, value)




    class CdxBundleIPv6DHCPRelayTable(Entity):
        """
        Ipv6 dhcp relay configurations on Bundle/Sub\-Bundle interface.
        
        .. attribute:: cdxbundleipv6dhcprelayentry
        
        	The conceptual row of cdxBundleIPv6DHCPRelayTable. An instance exist for the Bundle/Sub\-Bundle interface
        	**type**\: list of  		 :py:class:`CdxBundleIPv6DHCPRelayEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable.CdxBundleIPv6DHCPRelayEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable, self).__init__()

            self.yang_name = "cdxBundleIPv6DHCPRelayTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxBundleIPv6DHCPRelayEntry", ("cdxbundleipv6dhcprelayentry", CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable.CdxBundleIPv6DHCPRelayEntry))])
            self._leafs = OrderedDict()

            self.cdxbundleipv6dhcprelayentry = YList(self)
            self._segment_path = lambda: "cdxBundleIPv6DHCPRelayTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable, [], name, value)


        class CdxBundleIPv6DHCPRelayEntry(Entity):
            """
            The conceptual row of cdxBundleIPv6DHCPRelayTable.
            An instance exist for the Bundle/Sub\-Bundle interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelayinsertvssoption
            
            	Insert VSS option in Relay\-Forward Messages
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaytrusttorelayreply
            
            	Interface is trusted to process relay\-replies
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhdprelaysourceifname
            
            	Source interface name for IPv6 DHCP relayed messages
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable.CdxBundleIPv6DHCPRelayEntry, self).__init__()

                self.yang_name = "cdxBundleIPv6DHCPRelayEntry"
                self.yang_parent_name = "cdxBundleIPv6DHCPRelayTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxbundleipv6dhcprelayinsertvssoption', (YLeaf(YType.boolean, 'cdxBundleIPv6DHCPRelayInsertVSSOption'), ['bool'])),
                    ('cdxbundleipv6dhcprelaytrusttorelayreply', (YLeaf(YType.boolean, 'cdxBundleIPv6DHCPRelayTrustToRelayReply'), ['bool'])),
                    ('cdxbundleipv6dhdprelaysourceifname', (YLeaf(YType.str, 'cdxBundleIPv6DHDPRelaySourceIfname'), ['str'])),
                ])
                self.ifindex = None
                self.cdxbundleipv6dhcprelayinsertvssoption = None
                self.cdxbundleipv6dhcprelaytrusttorelayreply = None
                self.cdxbundleipv6dhdprelaysourceifname = None
                self._segment_path = lambda: "cdxBundleIPv6DHCPRelayEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxBundleIPv6DHCPRelayTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayTable.CdxBundleIPv6DHCPRelayEntry, ['ifindex', 'cdxbundleipv6dhcprelayinsertvssoption', 'cdxbundleipv6dhcprelaytrusttorelayreply', 'cdxbundleipv6dhdprelaysourceifname'], name, value)




    class CdxBundleIPv6DHCPRelayDestTable(Entity):
        """
         A list of IPv6 DHCP relay destination entries
        on Cable Bundle/Sub\-Bundle interfaces.
        
        .. attribute:: cdxbundleipv6dhcprelaydestentry
        
        	The conceptual row of cdxBundleIPv6DHCPRelayDestTable. An instance exists for the Cable Bundle/Sub\-Bundle interface
        	**type**\: list of  		 :py:class:`CdxBundleIPv6DHCPRelayDestEntry <ydk.models.cisco_ios_xe.CISCO_DOCS_EXT_MIB.CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable.CdxBundleIPv6DHCPRelayDestEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DOCS-EXT-MIB'
        _revision = '2017-11-10'

        def __init__(self):
            super(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable, self).__init__()

            self.yang_name = "cdxBundleIPv6DHCPRelayDestTable"
            self.yang_parent_name = "CISCO-DOCS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdxBundleIPv6DHCPRelayDestEntry", ("cdxbundleipv6dhcprelaydestentry", CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable.CdxBundleIPv6DHCPRelayDestEntry))])
            self._leafs = OrderedDict()

            self.cdxbundleipv6dhcprelaydestentry = YList(self)
            self._segment_path = lambda: "cdxBundleIPv6DHCPRelayDestTable"
            self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable, [], name, value)


        class CdxBundleIPv6DHCPRelayDestEntry(Entity):
            """
            The conceptual row of cdxBundleIPv6DHCPRelayDestTable.
            An instance exists for the Cable Bundle/Sub\-Bundle interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaydestoutifvrfindex  (key)
            
            	The vrf identifier that the cdxBundleIPv6DHCPRelayDestOutIfIndex belongs to, it is assigned to each VRF and is used to uniquely identify it, if it is zero, means in global vrf
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaydestaddr  (key)
            
            	IPv6 DHCP relay destination address
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaydestoutifindex  (key)
            
            	The snmp ifIndex of the IPv6 DHCP relay destination output interface. If the ifIndex is 0, it means there is no output interface specified
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaydestsourceaddress
            
            	IPv6 DHCP relay destination source address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdxbundleipv6dhcprelaydestlinkaddress
            
            	IPv6 DHCP relay destination link address
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DOCS-EXT-MIB'
            _revision = '2017-11-10'

            def __init__(self):
                super(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable.CdxBundleIPv6DHCPRelayDestEntry, self).__init__()

                self.yang_name = "cdxBundleIPv6DHCPRelayDestEntry"
                self.yang_parent_name = "cdxBundleIPv6DHCPRelayDestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cdxbundleipv6dhcprelaydestoutifvrfindex','cdxbundleipv6dhcprelaydestaddr','cdxbundleipv6dhcprelaydestoutifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cdxbundleipv6dhcprelaydestoutifvrfindex', (YLeaf(YType.uint32, 'cdxBundleIPv6DHCPRelayDestOutIfVrfIndex'), ['int'])),
                    ('cdxbundleipv6dhcprelaydestaddr', (YLeaf(YType.str, 'cdxBundleIPv6DHCPRelayDestAddr'), ['str'])),
                    ('cdxbundleipv6dhcprelaydestoutifindex', (YLeaf(YType.int32, 'cdxBundleIPv6DHCPRelayDestOutIfIndex'), ['int'])),
                    ('cdxbundleipv6dhcprelaydestsourceaddress', (YLeaf(YType.str, 'cdxBundleIPv6DHCPRelayDestSourceAddress'), ['str'])),
                    ('cdxbundleipv6dhcprelaydestlinkaddress', (YLeaf(YType.str, 'cdxBundleIPv6DHCPRelayDestLinkAddress'), ['str'])),
                ])
                self.ifindex = None
                self.cdxbundleipv6dhcprelaydestoutifvrfindex = None
                self.cdxbundleipv6dhcprelaydestaddr = None
                self.cdxbundleipv6dhcprelaydestoutifindex = None
                self.cdxbundleipv6dhcprelaydestsourceaddress = None
                self.cdxbundleipv6dhcprelaydestlinkaddress = None
                self._segment_path = lambda: "cdxBundleIPv6DHCPRelayDestEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cdxBundleIPv6DHCPRelayDestOutIfVrfIndex='" + str(self.cdxbundleipv6dhcprelaydestoutifvrfindex) + "']" + "[cdxBundleIPv6DHCPRelayDestAddr='" + str(self.cdxbundleipv6dhcprelaydestaddr) + "']" + "[cdxBundleIPv6DHCPRelayDestOutIfIndex='" + str(self.cdxbundleipv6dhcprelaydestoutifindex) + "']"
                self._absolute_path = lambda: "CISCO-DOCS-EXT-MIB:CISCO-DOCS-EXT-MIB/cdxBundleIPv6DHCPRelayDestTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODOCSEXTMIB.CdxBundleIPv6DHCPRelayDestTable.CdxBundleIPv6DHCPRelayDestEntry, ['ifindex', 'cdxbundleipv6dhcprelaydestoutifvrfindex', 'cdxbundleipv6dhcprelaydestaddr', 'cdxbundleipv6dhcprelaydestoutifindex', 'cdxbundleipv6dhcprelaydestsourceaddress', 'cdxbundleipv6dhcprelaydestlinkaddress'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCODOCSEXTMIB()
        return self._top_entity



