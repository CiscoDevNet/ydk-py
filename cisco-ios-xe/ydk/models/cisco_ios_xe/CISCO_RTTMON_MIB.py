""" CISCO_RTTMON_MIB 

This module defines a MIB for Round Trip Time
(RTT) monitoring of a list of targets, using a 
variety of protocols.

The table structure overview is a follows (t\: 
 indicates a table, at\:  indicates an augmented 
 table, and it\:  indicates table with the same 
 indices/control as parent table)\:

RTTMON MIB
\|\-\-\- Application Group
\|    \|\-\-\- Application Identity
\|    \|\-\-\- Application Capabilities
\|    \|\-\-\- Application Reset
\|    \|t\-\- Supported RTT Types
\|         \|\-\-\- Truth Value
\|    \|t\-\- Supported Protocols
\|         \|\-\-\- Truth Value
\|    \|t\-\- Application Preconfigured
\|         \|\-\-\- Script Names
\|         \|\-\-\- File Paths
\|    \|\-\-\- Responder control
\|    \|t\-\- Control Protocol Authentication
\|
\|\-\-\- Overall Control Group
\|    \|t\-\- Master Definitions Table
\|    \|    \|\-\-\- Global Configuration Definitions
\|    \|         \|\-\-\- Config for a single RTT Life
\|    \|    \|it\- Echo Specific Configuration
\|    \|    \|it\- Echo Path Hop Address Configuration
\|    \|    \|it\- File I/O Specific Configuration
\|    \|    \|it\- Script Specific Configuration
\|    \|    \|at\- Schedule Configuration
\|    \|    \|at\- Reaction Specific Config
\|    \|    \|at\- Statistics Capture Configuration
\|    \|    \|at\- History Collection Configuration
\|    \|    \|at\- Monitoring Operational State
\|    \|    \|at\- Last RTT operation
\|    \|
\|    \|t\-\- Reaction Trigger Table
\|         \|at\- Reaction Trigger Operational State
\|
\|\-\-\- Statistics Collection Group
\|    \|t\-\- Statistics Capture Table
\|         \|\-\-\- Captured Statistics
\|              \|\-\-\- Path Information
\|              \|\-\-\- Distribution Capture 
\|              \|\-\-\- Mean and Deviation Capture
\|         \|it\- Statistics Collection Table
\|    \|it\- Statistics Totals Table
\|    \|t\-\- HTTP Stats Table
\|    \|t\-\- Jitter Stats Table
\|
\|\-\-\- History Collection Group
\|    \|t\-\- History Collection Table
\|         \|\-\- Path Information
\|         \|\-\- Completion Information per operation
\|
\|\-\-\- Latest Operation Group
\|    \|t\-\- Latest HTTP Oper Table
\|    \|t\-\- Latest Jitter Oper Table

DEFINITIONS\:
  conceptual RTT control row \- 
          This is a row in the 'Overall Control 
          Group'.  This row is indexed via the 
          rttMonCtrlAdminIndex object.  This row 
          is spread across multiple real tables 
          in the 'Overall Control Group'.
  probe \-
          This is the entity that executes via a 
          conceptual RTT control row and populates
          a conceptual statistics row and a 
          conceptual history row.
  Rtt operation \-
          This is a single operation performed by
          a probe.  This operation can be a single
          Rtt attempt/completion or a group of Rtt
          attempts/completions that produce one
          operation table entry.

ARR Protocol Definition\:

The format of the RTT Asymmetric Request/Responses 
 (ARR) protocol is as follows\:

  The ARR Header (total of 12 octets)\: 

  4 octet \-> eyecatcher\: 'WxYz'
  1 octet \-> version   \: 0x01 \- protocol version
  1 octet \-> command   \: 0x01 \- logoff request
                         0x02 \- echo request
                         0x03 \- echo response
                         0x04 \- software version request
                         0x05 \- software version response
  2 octet \-> sequence number (Network Byte Order)
  4 octet \-> response data size (Network Byte Order)

  The ARR Data\:

  n octets \-> request/response data
                        \: 'AB..ZAB..ZAB..' 

  For software version request/response the 
   protocol version octet will contain the version
   number of the responder.  Thus the sequence 
   number, etc will not be included.

  For snaLU0EchoAppl and snaLU2EchoAppl all character 
   fields will be in EBCDIC.

  The response data should be appended to the 
   origin request data.  This allows data  
   verification to check the data that flows in 
   both directions.  If the response data size is
   smaller than the request data size the original
   request data will be truncated.  

  An example would be\:
    Request\:        /       Response\:
    'WxYz'          /       'WxYz'
    0x01            /       0x01
    0x02            /       0x03
    0x0001          /       0x0001
    0x00000008      /       0x00000008
    'ABCDEF'        /       'ABCDEFGH'

  NOTE\: We requested 8 bytes in the response and 
        the response had 8 bytes.  The size of the
        request data has no correlation to the
        size of the response data.

NOTE\:  For native RTT request/response (i.e. 
       ipIcmpecho) operations both the 'Header' 
       and 'Data' will be included.  Only the 
       'sequence number' in the Header will be 
       valid.

NOTE\:  For non\-connection oriented protocol the 
       initial RTT request/response operation will
       be preceded with an RTT request/response 
       operation to the target address to force 
       path exploration and to prove 
       connectivity.  The History collection table
       will contain these responses, but the 
       Statistics capture table will omit them to
       prevent skewed results.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCORTTMONMIB(Entity):
    """
    
    
    .. attribute:: rttmonappl
    
    	
    	**type**\:  :py:class:`RttMonAppl <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonAppl>`
    
    	**config**\: False
    
    .. attribute:: rttmonapplsupportedrtttypestable
    
    	A table of which contains the supported Rtt Monitor Types.  See the RttMonRttType textual convention for the definition of each type
    	**type**\:  :py:class:`RttMonApplSupportedRttTypesTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplSupportedRttTypesTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonapplsupportedprotocolstable
    
    	A table of which contains the supported Rtt Monitor Protocols.  See the RttMonProtocol textual convention  for the definition of each protocol
    	**type**\:  :py:class:`RttMonApplSupportedProtocolsTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplSupportedProtocolsTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonapplpreconfigedtable
    
    	A table of which contains the previously configured Script Names and File IO targets.  These Script Names and File IO targets are installed via a different mechanism than this application, and are specific to each platform
    	**type**\:  :py:class:`RttMonApplPreConfigedTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplPreConfigedTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: rttmonapplauthtable
    
    	A table which contains the definitions for key\-strings that will be used in authenticating RTR Control Protocol
    	**type**\:  :py:class:`RttMonApplAuthTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplAuthTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonctrladmintable
    
    	A table of Round Trip Time (RTT) monitoring definitions.  The RTT administration control is in multiple tables.   This first table, is used to create a conceptual RTT  control row.  The following tables contain objects which  configure scheduling, information gathering, and  notification/trigger generation.  All of these tables  will create the same conceptual RTT control row as this  table using this tables' index as their own index.   This table is limited in size by the agent  implementation.  The object rttMonApplNumCtrlAdminEntry will reflect this tables maximum number of entries
    	**type**\:  :py:class:`RttMonCtrlAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonechoadmintable
    
    	A table that contains Round Trip Time (RTT) specific definitions.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`RttMonEchoAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonfileioadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'fileIO' specific definitions.  When the RttMonRttType is not 'fileIO' this table is not valid.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`RttMonFileIOAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonFileIOAdminTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: rttmonscriptadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'script' specific definitions.  When the RttMonRttType is not 'script' this table is not valid.  This table is controlled via the rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`RttMonScriptAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonScriptAdminTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: rttmonreacttriggeradmintable
    
    	A table of which contains the list of conceptual RTT control rows that will start to collect data when a  reaction condition is violated and when  rttMonReactAdminActionType is set to one of the  following\:   \-  triggerOnly   \-  trapAndTrigger   \-  nmvtAndTrigger   \-  trapNmvtAndTrigger or when a reaction condition is violated and when any of the row in rttMonReactTable has rttMonReactActionType as one of the following\:   \- triggerOnly   \- trapAndTrigger  The goal of this table is to define one or more  additional conceptual RTT control rows that will become active and start to collect additional history and statistics (depending on the rows configuration values), when a problem has been detected.  If the conceptual RTT control row is undefined, and a  trigger occurs, no action will take place.    If the conceptual RTT control row is scheduled to start  at a later time, triggering that row will have no effect.  If the conceptual RTT control row is currently active,  triggering that row will have no effect on that row, but  the rttMonReactTriggerOperState object will transition to  'active'.  An entry in this table can only be triggered when it is not currently in a triggered state.  The object rttMonReactTriggerOperState will  reflect the state of each entry in this table
    	**type**\:  :py:class:`RttMonReactTriggerAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTriggerAdminTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonechopathadmintable
    
    	A table to store the hop addresses in a Loose Source Routing path. Response times are computed along the specified path using ping.  This maximum table size is limited by the size of the  maximum number of hop addresses that can fit in an IP header, which is 8. The object rttMonEchoPathAdminEntry will reflect  this tables maximum number of entries.  This table is coupled with rttMonCtrlAdminStatus
    	**type**\:  :py:class:`RttMonEchoPathAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoPathAdminTable>`
    
    	**config**\: False
    
    .. attribute:: rttmongrpscheduleadmintable
    
    	A table of Round Trip Time (RTT) monitoring group scheduling specific definitions. This table is used to create a conceptual group scheduling control row. The entries in this control row contain objects used to define group schedule configuration parameters.  The objects of this table will be used to schedule a group of probes identified by the conceptual rows of the rttMonCtrlAdminTable
    	**type**\:  :py:class:`RttMonGrpScheduleAdminTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonGrpScheduleAdminTable>`
    
    	**config**\: False
    
    .. attribute:: rttmplsvpnmonctrltable
    
    	A table of Auto SAA L3 MPLS VPN definitions.  The Auto SAA L3 MPLS VPN administration control is in multiple tables.  This first table, is used to create a conceptual Auto SAA L3 MPLS VPN control row.  The following tables contain objects which used in type specific configurations, scheduling and reaction configurations. All of these tables will create the same conceptual control row as this table using this table's index as their own index.  In order to a row in this table to become active the following objects must be defined.   rttMplsVpnMonCtrlRttType,   rttMplsVpnMonCtrlVrfName and   rttMplsVpnMonSchedulePeriod
    	**type**\:  :py:class:`RttMplsVpnMonCtrlTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonreacttable
    
    	A table that contains the reaction configurations. Each conceptual row in rttMonReactTable corresponds to a reaction configured for the probe defined in rttMonCtrlAdminTable.  For each reaction configured for a probe there is an entry in the table.  Each Probe can have multiple reactions and hence there can be multiple rows for a particular probe.  This table is coupled with rttMonCtrlAdminTable
    	**type**\:  :py:class:`RttMonReactTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTable>`
    
    	**config**\: False
    
    .. attribute:: rttmongeneratedopertable
    
    	This table contains information about the generated operation id as part of a parent IP SLA operation. The parent operation id is pseudo\-random number, selected by the management  station based on an operation started by the management  station,when creating a row via the rttMonCtrlAdminStatus object in the rttMonCtrlAdminTable table
    	**type**\:  :py:class:`RttMonGeneratedOperTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonGeneratedOperTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonstatscapturetable
    
    	The statistics capture database.  The statistics capture table contains summarized  information of the results for a conceptual RTT control  row.  A rolling accumulated history of this information  is maintained in a series of hourly 'group(s)'.  Each  'group' contains a series of 'path(s)', each 'path'  contains a series of 'hop(s)', each 'hop' contains a  series of 'statistics distribution bucket(s)'.  Each conceptual statistics row has a current hourly  group, into which RTT results are accumulated.  At the  end of each hour a new hourly group is created which  then becomes current.  The counters and accumulators in  the new group are initialized to zero.  The previous  group(s) is kept in the table until the table contains  rttMonStatisticsAdminNumHourGroups groups for the  conceptual statistics row;  at this point, the oldest  group is discarded and is replaced by the newly created  one.  The hourly group is uniquely identified by the  rttMonStatsCaptureStartTimeIndex object.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'inactive', the corresponding current hourly group in  this table is 'frozen', and a new hourly group is  created when activity is resumed.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'pending' this whole table will be cleared and reset to  its initial state.  When the RttMonRttType is 'pathEcho', the path  exploration RTT requests' statistics will not be  accumulated in this table.  NOTE\: When the RttMonRttType is 'pathEcho', a source to        target rttMonStatsCapturePathIndex path will be        created for each rttMonStatsCaptureStartTimeIndex        to hold all errors that occur when a specific path       had not been found or connection has not be setup.  Using this rttMonStatsCaptureTable, a managing  application can retrieve summarized data from accurately  measured periods, which is synchronized across multiple  conceptual RTT control rows.  With the new hourly group creation being performed on a 60 minute period, the  managing station has plenty of time to collect the data,  and need not be concerned with the vagaries of network  delays and lost PDU's when trying to get matching data.   Also, the managing station can spread the data gathering  over a longer period, which removes the need for a flood  of get requests in a short period which otherwise would  occur
    	**type**\:  :py:class:`RttMonStatsCaptureTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonstatscollecttable
    
    	The statistics collection database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it does not keep statistical distribution information.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:  :py:class:`RttMonStatsCollectTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCollectTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonstatstotalstable
    
    	The statistics totals database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it only keeps 60 minute group values.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:  :py:class:`RttMonStatsTotalsTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsTotalsTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonhttpstatstable
    
    	The HTTP statistics collection database.  The HTTP statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table can only  store a maximum of 2 hours of data
    	**type**\:  :py:class:`RttMonHTTPStatsTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonHTTPStatsTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonjitterstatstable
    
    	The Jitter statistics collection database.  The Jitter statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table will store  2 hours of data
    	**type**\:  :py:class:`RttMonJitterStatsTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonJitterStatsTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonlpdgrpstatstable
    
    	The Auto SAA L3 MPLS VPN LPD Group Database.  The LPD Group statistics table contains summarized performance statistics for the LPD group.  LPD Group \- The set of 'single probes' which are subset of the 'lspGroup' probe traversing set of paths between two PE end points are grouped together and called as the LPD group. The LPD group will be uniquely referenced by the LPD Group ID.  A rolling accumulated history of this information is maintained in a series of hourly 'group(s)'.  Each conceptual statistics row has a current hourly group, into which RTT results are accumulated. At the end of each hour a new hourly group is created which then becomes current. The counters and accumulators in the new group are initialized to zero. The previous group(s) is kept in the table until the table contains rttMplsVpnMonTypeLpdStatHours groups for the conceptual statistics row;  at this point, the oldest group is discarded and is replaced by the newly created one. The hourly group is uniquely identified by the rttMonLpdGrpStatsStartTimeIndex object
    	**type**\:  :py:class:`RttMonLpdGrpStatsTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLpdGrpStatsTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonhistorycollectiontable
    
    	The history collection database.  The history table contains a point by point rolling  history of the most recent RTT operations for each  conceptual RTT control row.  The rolling history of this  information is maintained in a series of 'live(s)', each containing a series of 'bucket(s)', each 'bucket'  contains a series of 'sample(s)'.  Each conceptual history row can have lives.  A life is  defined by the rttMonCtrlOperRttLife object.  A new life  will be created when rttMonCtrlOperState transitions 'active'.  When the number of lives become greater  than rttMonHistoryAdminNumLives the oldest life will be  discarded and a new life will be created by incrementing the index.  The path exploration RTT operation will be kept as an entry in this table
    	**type**\:  :py:class:`RttMonHistoryCollectionTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonHistoryCollectionTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonlatesthttpopertable
    
    	A table which contains the status of latest HTTP RTT operation
    	**type**\:  :py:class:`RttMonLatestHTTPOperTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLatestHTTPOperTable>`
    
    	**config**\: False
    
    .. attribute:: rttmonlatestjitteropertable
    
    	A table which contains the status of latest Jitter operation
    	**type**\:  :py:class:`RttMonLatestJitterOperTable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLatestJitterOperTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-RTTMON-MIB'
    _revision = '2012-08-16'

    def __init__(self):
        super(CISCORTTMONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RTTMON-MIB"
        self.yang_parent_name = "CISCO-RTTMON-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rttMonAppl", ("rttmonappl", CISCORTTMONMIB.RttMonAppl)), ("rttMonApplSupportedRttTypesTable", ("rttmonapplsupportedrtttypestable", CISCORTTMONMIB.RttMonApplSupportedRttTypesTable)), ("rttMonApplSupportedProtocolsTable", ("rttmonapplsupportedprotocolstable", CISCORTTMONMIB.RttMonApplSupportedProtocolsTable)), ("rttMonApplPreConfigedTable", ("rttmonapplpreconfigedtable", CISCORTTMONMIB.RttMonApplPreConfigedTable)), ("rttMonApplAuthTable", ("rttmonapplauthtable", CISCORTTMONMIB.RttMonApplAuthTable)), ("rttMonCtrlAdminTable", ("rttmonctrladmintable", CISCORTTMONMIB.RttMonCtrlAdminTable)), ("rttMonEchoAdminTable", ("rttmonechoadmintable", CISCORTTMONMIB.RttMonEchoAdminTable)), ("rttMonFileIOAdminTable", ("rttmonfileioadmintable", CISCORTTMONMIB.RttMonFileIOAdminTable)), ("rttMonScriptAdminTable", ("rttmonscriptadmintable", CISCORTTMONMIB.RttMonScriptAdminTable)), ("rttMonReactTriggerAdminTable", ("rttmonreacttriggeradmintable", CISCORTTMONMIB.RttMonReactTriggerAdminTable)), ("rttMonEchoPathAdminTable", ("rttmonechopathadmintable", CISCORTTMONMIB.RttMonEchoPathAdminTable)), ("rttMonGrpScheduleAdminTable", ("rttmongrpscheduleadmintable", CISCORTTMONMIB.RttMonGrpScheduleAdminTable)), ("rttMplsVpnMonCtrlTable", ("rttmplsvpnmonctrltable", CISCORTTMONMIB.RttMplsVpnMonCtrlTable)), ("rttMonReactTable", ("rttmonreacttable", CISCORTTMONMIB.RttMonReactTable)), ("rttMonGeneratedOperTable", ("rttmongeneratedopertable", CISCORTTMONMIB.RttMonGeneratedOperTable)), ("rttMonStatsCaptureTable", ("rttmonstatscapturetable", CISCORTTMONMIB.RttMonStatsCaptureTable)), ("rttMonStatsCollectTable", ("rttmonstatscollecttable", CISCORTTMONMIB.RttMonStatsCollectTable)), ("rttMonStatsTotalsTable", ("rttmonstatstotalstable", CISCORTTMONMIB.RttMonStatsTotalsTable)), ("rttMonHTTPStatsTable", ("rttmonhttpstatstable", CISCORTTMONMIB.RttMonHTTPStatsTable)), ("rttMonJitterStatsTable", ("rttmonjitterstatstable", CISCORTTMONMIB.RttMonJitterStatsTable)), ("rttMonLpdGrpStatsTable", ("rttmonlpdgrpstatstable", CISCORTTMONMIB.RttMonLpdGrpStatsTable)), ("rttMonHistoryCollectionTable", ("rttmonhistorycollectiontable", CISCORTTMONMIB.RttMonHistoryCollectionTable)), ("rttMonLatestHTTPOperTable", ("rttmonlatesthttpopertable", CISCORTTMONMIB.RttMonLatestHTTPOperTable)), ("rttMonLatestJitterOperTable", ("rttmonlatestjitteropertable", CISCORTTMONMIB.RttMonLatestJitterOperTable))])
        self._leafs = OrderedDict()

        self.rttmonappl = CISCORTTMONMIB.RttMonAppl()
        self.rttmonappl.parent = self
        self._children_name_map["rttmonappl"] = "rttMonAppl"

        self.rttmonapplsupportedrtttypestable = CISCORTTMONMIB.RttMonApplSupportedRttTypesTable()
        self.rttmonapplsupportedrtttypestable.parent = self
        self._children_name_map["rttmonapplsupportedrtttypestable"] = "rttMonApplSupportedRttTypesTable"

        self.rttmonapplsupportedprotocolstable = CISCORTTMONMIB.RttMonApplSupportedProtocolsTable()
        self.rttmonapplsupportedprotocolstable.parent = self
        self._children_name_map["rttmonapplsupportedprotocolstable"] = "rttMonApplSupportedProtocolsTable"

        self.rttmonapplpreconfigedtable = CISCORTTMONMIB.RttMonApplPreConfigedTable()
        self.rttmonapplpreconfigedtable.parent = self
        self._children_name_map["rttmonapplpreconfigedtable"] = "rttMonApplPreConfigedTable"

        self.rttmonapplauthtable = CISCORTTMONMIB.RttMonApplAuthTable()
        self.rttmonapplauthtable.parent = self
        self._children_name_map["rttmonapplauthtable"] = "rttMonApplAuthTable"

        self.rttmonctrladmintable = CISCORTTMONMIB.RttMonCtrlAdminTable()
        self.rttmonctrladmintable.parent = self
        self._children_name_map["rttmonctrladmintable"] = "rttMonCtrlAdminTable"

        self.rttmonechoadmintable = CISCORTTMONMIB.RttMonEchoAdminTable()
        self.rttmonechoadmintable.parent = self
        self._children_name_map["rttmonechoadmintable"] = "rttMonEchoAdminTable"

        self.rttmonfileioadmintable = CISCORTTMONMIB.RttMonFileIOAdminTable()
        self.rttmonfileioadmintable.parent = self
        self._children_name_map["rttmonfileioadmintable"] = "rttMonFileIOAdminTable"

        self.rttmonscriptadmintable = CISCORTTMONMIB.RttMonScriptAdminTable()
        self.rttmonscriptadmintable.parent = self
        self._children_name_map["rttmonscriptadmintable"] = "rttMonScriptAdminTable"

        self.rttmonreacttriggeradmintable = CISCORTTMONMIB.RttMonReactTriggerAdminTable()
        self.rttmonreacttriggeradmintable.parent = self
        self._children_name_map["rttmonreacttriggeradmintable"] = "rttMonReactTriggerAdminTable"

        self.rttmonechopathadmintable = CISCORTTMONMIB.RttMonEchoPathAdminTable()
        self.rttmonechopathadmintable.parent = self
        self._children_name_map["rttmonechopathadmintable"] = "rttMonEchoPathAdminTable"

        self.rttmongrpscheduleadmintable = CISCORTTMONMIB.RttMonGrpScheduleAdminTable()
        self.rttmongrpscheduleadmintable.parent = self
        self._children_name_map["rttmongrpscheduleadmintable"] = "rttMonGrpScheduleAdminTable"

        self.rttmplsvpnmonctrltable = CISCORTTMONMIB.RttMplsVpnMonCtrlTable()
        self.rttmplsvpnmonctrltable.parent = self
        self._children_name_map["rttmplsvpnmonctrltable"] = "rttMplsVpnMonCtrlTable"

        self.rttmonreacttable = CISCORTTMONMIB.RttMonReactTable()
        self.rttmonreacttable.parent = self
        self._children_name_map["rttmonreacttable"] = "rttMonReactTable"

        self.rttmongeneratedopertable = CISCORTTMONMIB.RttMonGeneratedOperTable()
        self.rttmongeneratedopertable.parent = self
        self._children_name_map["rttmongeneratedopertable"] = "rttMonGeneratedOperTable"

        self.rttmonstatscapturetable = CISCORTTMONMIB.RttMonStatsCaptureTable()
        self.rttmonstatscapturetable.parent = self
        self._children_name_map["rttmonstatscapturetable"] = "rttMonStatsCaptureTable"

        self.rttmonstatscollecttable = CISCORTTMONMIB.RttMonStatsCollectTable()
        self.rttmonstatscollecttable.parent = self
        self._children_name_map["rttmonstatscollecttable"] = "rttMonStatsCollectTable"

        self.rttmonstatstotalstable = CISCORTTMONMIB.RttMonStatsTotalsTable()
        self.rttmonstatstotalstable.parent = self
        self._children_name_map["rttmonstatstotalstable"] = "rttMonStatsTotalsTable"

        self.rttmonhttpstatstable = CISCORTTMONMIB.RttMonHTTPStatsTable()
        self.rttmonhttpstatstable.parent = self
        self._children_name_map["rttmonhttpstatstable"] = "rttMonHTTPStatsTable"

        self.rttmonjitterstatstable = CISCORTTMONMIB.RttMonJitterStatsTable()
        self.rttmonjitterstatstable.parent = self
        self._children_name_map["rttmonjitterstatstable"] = "rttMonJitterStatsTable"

        self.rttmonlpdgrpstatstable = CISCORTTMONMIB.RttMonLpdGrpStatsTable()
        self.rttmonlpdgrpstatstable.parent = self
        self._children_name_map["rttmonlpdgrpstatstable"] = "rttMonLpdGrpStatsTable"

        self.rttmonhistorycollectiontable = CISCORTTMONMIB.RttMonHistoryCollectionTable()
        self.rttmonhistorycollectiontable.parent = self
        self._children_name_map["rttmonhistorycollectiontable"] = "rttMonHistoryCollectionTable"

        self.rttmonlatesthttpopertable = CISCORTTMONMIB.RttMonLatestHTTPOperTable()
        self.rttmonlatesthttpopertable.parent = self
        self._children_name_map["rttmonlatesthttpopertable"] = "rttMonLatestHTTPOperTable"

        self.rttmonlatestjitteropertable = CISCORTTMONMIB.RttMonLatestJitterOperTable()
        self.rttmonlatestjitteropertable.parent = self
        self._children_name_map["rttmonlatestjitteropertable"] = "rttMonLatestJitterOperTable"
        self._segment_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCORTTMONMIB, [], name, value)


    class RttMonAppl(Entity):
        """
        
        
        .. attribute:: rttmonapplversion
        
        	Round Trip Time monitoring application version string.  The format will be\:  'Version.Release.Patch\-Level\: Textual\-Description'  For example\:  '1.0.0\: Initial RTT Application'
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: rttmonapplmaxpacketdatasize
        
        	The maximum size of the data portion an echo packet supported by this RTT application.  This is the maximum value that can be specified by (rttMonEchoAdminPktDataRequestSize + ARR Header) or  (rttMonEchoAdminPktDataResponseSize + ARR Header) in the rttMonCtrlAdminTable.  This object is undefined for conceptual RTT  control rows when the RttMonRttType object is set to 'fileIO' or 'script'
        	**type**\: int
        
        	**range:** 0..16384
        
        	**config**\: False
        
        	**units**\: octets
        
        .. attribute:: rttmonappltimeoflastset
        
        	The last time at which a set operation occurred on any of the objects in this MIB.  The managing  application can inspect this value in order to  determine whether changes have been made without  retrieving the entire Administration portion of this MIB.  This object applies to all settable objects in this MIB, including the 'Reset' objects that could clear saved history/statistics
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: rttmonapplnumctrladminentry
        
        	This object defines the maximum number of entries that can be added to the rttMonCtrlAdminTable. It is calculated at the system init time. The value is impacted when rttMonApplFreeMemLowWaterMark is changed
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**config**\: False
        
        .. attribute:: rttmonapplreset
        
        	When set to 'reset' the entire RTT application goes through a reset sequence, making a best  effort to revert to its startup condition.  Any  and all rows in the Overall Control Group will be immediately deleted, together with any associated rows in the Statistics Collection Group, and  History Collection Group.  All open connections  will also be closed.  Finally the  rttMonApplPreConfigedTable will reset (see  rttMonApplPreConfigedReset)
        	**type**\:  :py:class:`RttReset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttReset>`
        
        	**config**\: False
        
        .. attribute:: rttmonapplpreconfigedreset
        
        	When set to 'reset' the RTT application will reset the Application Preconfigured MIB section.  This will force the RTT application to delete all entries in the rttMonApplPreConfigedTable and then to repopulate the table with the current configuration.  This provides a mechanism to load and unload user scripts and file paths
        	**type**\:  :py:class:`RttReset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttReset>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        .. attribute:: rttmonapplprobecapacity
        
        	This object defines the number of new probes that can be configured on a router. The number depends on the value  of rttMonApplFreeMemLowWaterMark, free bytes available on the router and the system configured rttMonCtrlAdminEntry number. Equation\: rttMonApplProbeCapacity =  MIN(((Free\_Bytes\_on\_the\_Router \- rttMonApplFreeMemLowWaterMark)/ Memory\_required\_by\_each\_probe), rttMonApplNumCtrlAdminEntry \-  Num\_of\_Probes\_already\_configured))
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**config**\: False
        
        .. attribute:: rttmonapplfreememlowwatermark
        
        	This object defines the amount of free memory a router must have in order to configure RTR. If RTR found out that the memory is falling below this mark, it will not allow new probes to be configured.  This value should not be set higher (or very close to) than  the free bytes available on the router
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: rttmonappllatestseterror
        
        	An error description for the last error message caused by set.  Currently, it includes set error caused due to setting rttMonApplFreeMemLowWaterMark greater than the available free memory on the router or not enough memory left to create new probes
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: rttmonapplresponder
        
        	Enable or disable RTR responder on the router
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: rttmonappllpdgrpstatsreset
        
        	This object is used to reset certain objects within the rttMonLpdGrpStatsTable.  When the object is set to value of an active LPD Group identifier the associated objects will be reset. The reset objects will be set to a value as specified in the object's description.  The following objects will not be reset. \- rttMonLpdGrpStatsTargetPE \- rttMonLpdGrpStatsGroupProbeIndex \- rttMonLpdGrpStatsGroupIndex \- rttMonLpdGrpStatsStartTimeIndex
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonAppl, self).__init__()

            self.yang_name = "rttMonAppl"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('rttmonapplversion', (YLeaf(YType.str, 'rttMonApplVersion'), ['str'])),
                ('rttmonapplmaxpacketdatasize', (YLeaf(YType.int32, 'rttMonApplMaxPacketDataSize'), ['int'])),
                ('rttmonappltimeoflastset', (YLeaf(YType.uint32, 'rttMonApplTimeOfLastSet'), ['int'])),
                ('rttmonapplnumctrladminentry', (YLeaf(YType.int32, 'rttMonApplNumCtrlAdminEntry'), ['int'])),
                ('rttmonapplreset', (YLeaf(YType.enumeration, 'rttMonApplReset'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttReset', '')])),
                ('rttmonapplpreconfigedreset', (YLeaf(YType.enumeration, 'rttMonApplPreConfigedReset'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttReset', '')])),
                ('rttmonapplprobecapacity', (YLeaf(YType.int32, 'rttMonApplProbeCapacity'), ['int'])),
                ('rttmonapplfreememlowwatermark', (YLeaf(YType.int32, 'rttMonApplFreeMemLowWaterMark'), ['int'])),
                ('rttmonappllatestseterror', (YLeaf(YType.str, 'rttMonApplLatestSetError'), ['str'])),
                ('rttmonapplresponder', (YLeaf(YType.boolean, 'rttMonApplResponder'), ['bool'])),
                ('rttmonappllpdgrpstatsreset', (YLeaf(YType.int32, 'rttMonApplLpdGrpStatsReset'), ['int'])),
            ])
            self.rttmonapplversion = None
            self.rttmonapplmaxpacketdatasize = None
            self.rttmonappltimeoflastset = None
            self.rttmonapplnumctrladminentry = None
            self.rttmonapplreset = None
            self.rttmonapplpreconfigedreset = None
            self.rttmonapplprobecapacity = None
            self.rttmonapplfreememlowwatermark = None
            self.rttmonappllatestseterror = None
            self.rttmonapplresponder = None
            self.rttmonappllpdgrpstatsreset = None
            self._segment_path = lambda: "rttMonAppl"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonAppl, ['rttmonapplversion', 'rttmonapplmaxpacketdatasize', 'rttmonappltimeoflastset', 'rttmonapplnumctrladminentry', 'rttmonapplreset', 'rttmonapplpreconfigedreset', 'rttmonapplprobecapacity', 'rttmonapplfreememlowwatermark', 'rttmonappllatestseterror', 'rttmonapplresponder', 'rttmonappllpdgrpstatsreset'], name, value)



    class RttMonApplSupportedRttTypesTable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Types.
        
        See the RttMonRttType textual convention for
        the definition of each type.
        
        .. attribute:: rttmonapplsupportedrtttypesentry
        
        	A list that presents the valid Rtt Monitor Types
        	**type**\: list of  		 :py:class:`RttMonApplSupportedRttTypesEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplSupportedRttTypesTable.RttMonApplSupportedRttTypesEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonApplSupportedRttTypesTable, self).__init__()

            self.yang_name = "rttMonApplSupportedRttTypesTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonApplSupportedRttTypesEntry", ("rttmonapplsupportedrtttypesentry", CISCORTTMONMIB.RttMonApplSupportedRttTypesTable.RttMonApplSupportedRttTypesEntry))])
            self._leafs = OrderedDict()

            self.rttmonapplsupportedrtttypesentry = YList(self)
            self._segment_path = lambda: "rttMonApplSupportedRttTypesTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonApplSupportedRttTypesTable, [], name, value)


        class RttMonApplSupportedRttTypesEntry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Types.
            
            .. attribute:: rttmonapplsupportedrtttypes  (key)
            
            	This object indexes the supported 'RttMonRttType' types
            	**type**\:  :py:class:`RttMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonRttType>`
            
            	**config**\: False
            
            .. attribute:: rttmonapplsupportedrtttypesvalid
            
            	This object defines the supported 'RttMonRttType' types
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonApplSupportedRttTypesTable.RttMonApplSupportedRttTypesEntry, self).__init__()

                self.yang_name = "rttMonApplSupportedRttTypesEntry"
                self.yang_parent_name = "rttMonApplSupportedRttTypesTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplsupportedrtttypes']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplsupportedrtttypes', (YLeaf(YType.enumeration, 'rttMonApplSupportedRttTypes'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonRttType', '')])),
                    ('rttmonapplsupportedrtttypesvalid', (YLeaf(YType.boolean, 'rttMonApplSupportedRttTypesValid'), ['bool'])),
                ])
                self.rttmonapplsupportedrtttypes = None
                self.rttmonapplsupportedrtttypesvalid = None
                self._segment_path = lambda: "rttMonApplSupportedRttTypesEntry" + "[rttMonApplSupportedRttTypes='" + str(self.rttmonapplsupportedrtttypes) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedRttTypesTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonApplSupportedRttTypesTable.RttMonApplSupportedRttTypesEntry, ['rttmonapplsupportedrtttypes', 'rttmonapplsupportedrtttypesvalid'], name, value)




    class RttMonApplSupportedProtocolsTable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Protocols.
        
        See the RttMonProtocol textual convention 
        for the definition of each protocol.
        
        .. attribute:: rttmonapplsupportedprotocolsentry
        
        	A list that presents the valid Rtt Monitor Protocols
        	**type**\: list of  		 :py:class:`RttMonApplSupportedProtocolsEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplSupportedProtocolsTable.RttMonApplSupportedProtocolsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonApplSupportedProtocolsTable, self).__init__()

            self.yang_name = "rttMonApplSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonApplSupportedProtocolsEntry", ("rttmonapplsupportedprotocolsentry", CISCORTTMONMIB.RttMonApplSupportedProtocolsTable.RttMonApplSupportedProtocolsEntry))])
            self._leafs = OrderedDict()

            self.rttmonapplsupportedprotocolsentry = YList(self)
            self._segment_path = lambda: "rttMonApplSupportedProtocolsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonApplSupportedProtocolsTable, [], name, value)


        class RttMonApplSupportedProtocolsEntry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Protocols.
            
            .. attribute:: rttmonapplsupportedprotocols  (key)
            
            	This object indexes the supported 'RttMonProtocol' protocols
            	**type**\:  :py:class:`RttMonProtocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonProtocol>`
            
            	**config**\: False
            
            .. attribute:: rttmonapplsupportedprotocolsvalid
            
            	This object defines the supported 'RttMonProtocol' protocols
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonApplSupportedProtocolsTable.RttMonApplSupportedProtocolsEntry, self).__init__()

                self.yang_name = "rttMonApplSupportedProtocolsEntry"
                self.yang_parent_name = "rttMonApplSupportedProtocolsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplsupportedprotocols']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplsupportedprotocols', (YLeaf(YType.enumeration, 'rttMonApplSupportedProtocols'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonProtocol', '')])),
                    ('rttmonapplsupportedprotocolsvalid', (YLeaf(YType.boolean, 'rttMonApplSupportedProtocolsValid'), ['bool'])),
                ])
                self.rttmonapplsupportedprotocols = None
                self.rttmonapplsupportedprotocolsvalid = None
                self._segment_path = lambda: "rttMonApplSupportedProtocolsEntry" + "[rttMonApplSupportedProtocols='" + str(self.rttmonapplsupportedprotocols) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedProtocolsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonApplSupportedProtocolsTable.RttMonApplSupportedProtocolsEntry, ['rttmonapplsupportedprotocols', 'rttmonapplsupportedprotocolsvalid'], name, value)




    class RttMonApplPreConfigedTable(Entity):
        """
        A table of which contains the previously
        configured Script Names and File IO targets.
        
        These Script Names and File IO targets are installed
        via a different mechanism than this application, and
        are specific to each platform.
        
        .. attribute:: rttmonapplpreconfigedentry
        
        	A list of objects that describe the previously configured Script Names and File IO targets
        	**type**\: list of  		 :py:class:`RttMonApplPreConfigedEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonApplPreConfigedTable, self).__init__()

            self.yang_name = "rttMonApplPreConfigedTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonApplPreConfigedEntry", ("rttmonapplpreconfigedentry", CISCORTTMONMIB.RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry))])
            self._leafs = OrderedDict()

            self.rttmonapplpreconfigedentry = YList(self)
            self._segment_path = lambda: "rttMonApplPreConfigedTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonApplPreConfigedTable, [], name, value)


        class RttMonApplPreConfigedEntry(Entity):
            """
            A list of objects that describe the previously
            configured Script Names and File IO targets.
            
            .. attribute:: rttmonapplpreconfigedtype  (key)
            
            	This is the type of value being stored in the rttMonApplPreConfigedName object
            	**type**\:  :py:class:`RttMonApplPreConfigedType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry.RttMonApplPreConfigedType>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedname  (key)
            
            	This is either one of the following depending on the value of the rttMonApplPreConfigedType object\:   \- The file path to a server.  One of these file paths     must be used when defining an entry in the     rttMonFileIOAdminTable table with 'fileIO' as the     value of the rttMonCtrlAdminRttType object.   \- The script name to be used when generating RTT     operations.  One of these script names must be used     when defining an entry in the rttMonScriptAdminTable     table with 'script' as the value of the     rttMonCtrlAdminRttType object.  NOTE\:  For script names, command line parameters         can follow these names in the         rttMonScriptAdminTable table
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedvalid
            
            	When this row exists, this value will be 'true'. This object exists only to create a valid row in this  table
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry, self).__init__()

                self.yang_name = "rttMonApplPreConfigedEntry"
                self.yang_parent_name = "rttMonApplPreConfigedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplpreconfigedtype','rttmonapplpreconfigedname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplpreconfigedtype', (YLeaf(YType.enumeration, 'rttMonApplPreConfigedType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry.RttMonApplPreConfigedType')])),
                    ('rttmonapplpreconfigedname', (YLeaf(YType.str, 'rttMonApplPreConfigedName'), ['str'])),
                    ('rttmonapplpreconfigedvalid', (YLeaf(YType.boolean, 'rttMonApplPreConfigedValid'), ['bool'])),
                ])
                self.rttmonapplpreconfigedtype = None
                self.rttmonapplpreconfigedname = None
                self.rttmonapplpreconfigedvalid = None
                self._segment_path = lambda: "rttMonApplPreConfigedEntry" + "[rttMonApplPreConfigedType='" + str(self.rttmonapplpreconfigedtype) + "']" + "[rttMonApplPreConfigedName='" + str(self.rttmonapplpreconfigedname) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplPreConfigedTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonApplPreConfigedTable.RttMonApplPreConfigedEntry, ['rttmonapplpreconfigedtype', 'rttmonapplpreconfigedname', 'rttmonapplpreconfigedvalid'], name, value)

            class RttMonApplPreConfigedType(Enum):
                """
                RttMonApplPreConfigedType (Enum Class)

                This is the type of value being stored in the

                rttMonApplPreConfigedName object.

                .. data:: filePath = 1

                .. data:: scriptName = 2

                """

                filePath = Enum.YLeaf(1, "filePath")

                scriptName = Enum.YLeaf(2, "scriptName")





    class RttMonApplAuthTable(Entity):
        """
        A table which contains the definitions for key\-strings
        that will be used in authenticating RTR Control Protocol.
        
        .. attribute:: rttmonapplauthentry
        
        	A list that presents the valid parameters for Authenticating RTR Control Protocol
        	**type**\: list of  		 :py:class:`RttMonApplAuthEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonApplAuthTable.RttMonApplAuthEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonApplAuthTable, self).__init__()

            self.yang_name = "rttMonApplAuthTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonApplAuthEntry", ("rttmonapplauthentry", CISCORTTMONMIB.RttMonApplAuthTable.RttMonApplAuthEntry))])
            self._leafs = OrderedDict()

            self.rttmonapplauthentry = YList(self)
            self._segment_path = lambda: "rttMonApplAuthTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonApplAuthTable, [], name, value)


        class RttMonApplAuthEntry(Entity):
            """
            A list that presents the valid parameters for Authenticating
            RTR Control Protocol.
            
            .. attribute:: rttmonapplauthindex  (key)
            
            	Uniquely identifies a row in the rttMonApplAuthTable. This is a pseudo\-random number selected by the management station when creating a row via the rttMonApplAuthStatus  object. If the pseudo\-random number is already in use, an  'inconsistentValue' is returned. Currently, only one row  can be created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeychain
            
            	A string which represents the key\-chain name. If multiple key\-strings are specified, then the authenticator will  alternate between the specified strings
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeystring1
            
            	A string which represents a key\-string name whose id is 1
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeystring2
            
            	A string which represents a key\-string name whose id is 2
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeystring3
            
            	A string which represents a key\-string name whose id is 3
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeystring4
            
            	A string which represents a key\-string name whose id is 4
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthkeystring5
            
            	A string which represents a key\-string name whose id is 5
            	**type**\: str
            
            	**length:** 1..48
            
            	**config**\: False
            
            .. attribute:: rttmonapplauthstatus
            
            	The status of the Authentication row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonApplAuthTable.RttMonApplAuthEntry, self).__init__()

                self.yang_name = "rttMonApplAuthEntry"
                self.yang_parent_name = "rttMonApplAuthTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplauthindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplauthindex', (YLeaf(YType.int32, 'rttMonApplAuthIndex'), ['int'])),
                    ('rttmonapplauthkeychain', (YLeaf(YType.str, 'rttMonApplAuthKeyChain'), ['str'])),
                    ('rttmonapplauthkeystring1', (YLeaf(YType.str, 'rttMonApplAuthKeyString1'), ['str'])),
                    ('rttmonapplauthkeystring2', (YLeaf(YType.str, 'rttMonApplAuthKeyString2'), ['str'])),
                    ('rttmonapplauthkeystring3', (YLeaf(YType.str, 'rttMonApplAuthKeyString3'), ['str'])),
                    ('rttmonapplauthkeystring4', (YLeaf(YType.str, 'rttMonApplAuthKeyString4'), ['str'])),
                    ('rttmonapplauthkeystring5', (YLeaf(YType.str, 'rttMonApplAuthKeyString5'), ['str'])),
                    ('rttmonapplauthstatus', (YLeaf(YType.enumeration, 'rttMonApplAuthStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.rttmonapplauthindex = None
                self.rttmonapplauthkeychain = None
                self.rttmonapplauthkeystring1 = None
                self.rttmonapplauthkeystring2 = None
                self.rttmonapplauthkeystring3 = None
                self.rttmonapplauthkeystring4 = None
                self.rttmonapplauthkeystring5 = None
                self.rttmonapplauthstatus = None
                self._segment_path = lambda: "rttMonApplAuthEntry" + "[rttMonApplAuthIndex='" + str(self.rttmonapplauthindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplAuthTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonApplAuthTable.RttMonApplAuthEntry, ['rttmonapplauthindex', 'rttmonapplauthkeychain', 'rttmonapplauthkeystring1', 'rttmonapplauthkeystring2', 'rttmonapplauthkeystring3', 'rttmonapplauthkeystring4', 'rttmonapplauthkeystring5', 'rttmonapplauthstatus'], name, value)




    class RttMonCtrlAdminTable(Entity):
        """
        A table of Round Trip Time (RTT) monitoring definitions.
        
        The RTT administration control is in multiple tables.  
        This first table, is used to create a conceptual RTT 
        control row.  The following tables contain objects which 
        configure scheduling, information gathering, and 
        notification/trigger generation.  All of these tables 
        will create the same conceptual RTT control row as this 
        table using this tables' index as their own index. 
        
        This table is limited in size by the agent 
        implementation.  The object rttMonApplNumCtrlAdminEntry
        will reflect this tables maximum number of entries.
        
        .. attribute:: rttmonctrladminentry
        
        	A base list of objects that define a conceptual RTT control row
        	**type**\: list of  		 :py:class:`RttMonCtrlAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonCtrlAdminTable, self).__init__()

            self.yang_name = "rttMonCtrlAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonCtrlAdminEntry", ("rttmonctrladminentry", CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonctrladminentry = YList(self)
            self._segment_path = lambda: "rttMonCtrlAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonCtrlAdminTable, [], name, value)


        class RttMonCtrlAdminEntry(Entity):
            """
            A base list of objects that define a conceptual RTT
            control row.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	Uniquely identifies a row in the rttMonCtrlAdminTable. This is a pseudo\-random number, selected by the management  station or auto\-generated based on  operation started by the  management station,when creating a row via  the rttMonCtrlAdminStatus object.  If the pseudo\-random   number is already in use an 'inconsistentValue' return code   will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonctrladminowner
            
            	Identifies the entity that created this table row
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmonctrladmintag
            
            	A string which is used by a managing application to identify the RTT target.  This string is inserted into trap notifications, but has no other significance to the  agent
            	**type**\: str
            
            	**length:** 0..16
            
            	**config**\: False
            
            .. attribute:: rttmonctrladminrtttype
            
            	The type of RTT operation to be performed.  This value must be set in the same PDU or before setting any type specific configuration.  Note\: The RTT operation 'lspGroup' cannot be created via this control row. It will be created automatically by Auto SAA L3 MPLS VPN when rttMplsVpnMonCtrlLpd is 'true'
            	**type**\:  :py:class:`RttMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonRttType>`
            
            	**config**\: False
            
            .. attribute:: rttmonctrladminthreshold
            
            	This object defines an administrative threshold limit. If the RTT operation time exceeds this limit and if the  conditions specified in rttMonReactAdminThresholdType or  rttMonHistoryAdminFilter are satisfied, a threshold is generated
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladminfrequency
            
            	Specifies the duration between initiating each RTT operation.   This object cannot be set to a value which would be a  shorter duration than rttMonCtrlAdminTimeout.  When the RttMonRttType specifies an operation that is synchronous in nature, it may happen that the next RTT  operation is blocked by a RTT operation which has not yet completed.  In this case, the value of a counter (rttMonStatsCollectBusies) in rttMonStatsCaptureTable is incremented in lieu of initiating a RTT operation, and  the next attempt will occur at the next rttMonCtrlAdminFrequency expiration.   NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'pathEcho', setting this value to a small        value for your network size may cause an operation        attempt (or multiple attempts) to be started         before the previous operation has finished.  In         this situation the rttMonStatsCollectBusies object        will be incremented in lieu of initiating a new         RTT operation, and the next attempt will occur at        the next rttMonCtrlAdminFrequency expiration.  When the rttMonCtrlAdminRttType object is defined to be 'pathEcho', the suggested value for this object  is greater than rttMonCtrlAdminTimeout times the  maximum number of expected hops to the target.  NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'dhcp', the minimum allowed value for this        object is 10 seconds.  This restriction is due to        protocol limitations described in RFC 2131
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrladmintimeout
            
            	Specifies the duration to wait for a RTT operation completion.  The value of this object cannot be set to  a value which would specify a duration exceeding  rttMonCtrlAdminFrequency.  For connection oriented protocols, this may cause the connection to be closed by the probe.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladminverifydata
            
            	When set to true, the resulting data in each RTT operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object.  Some RttMonRttTypes may not support this option.  When a type does not support this option, the agent will  transition this object to false.  It is the management applications responsibility to check for this  transition
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonctrladminstatus
            
            	The status of the conceptual RTT control row.  In order for this object to become active, the following  row objects must be defined\:    \- rttMonCtrlAdminRttType Additionally\:  \- for echo, pathEcho based on 'ipIcmpEcho' and dlsw probes     rttMonEchoAdminProtocol and      rttMonEchoAdminTargetAddress;  \- for echo, pathEcho based on 'mplsLspPingAppl'     rttMonEchoAdminProtocol, rttMonEchoAdminTargetAddress      and rttMonEchoAdminLSPFECType  \- for udpEcho, tcpConnect and jitter probes     rttMonEchoAdminTargetAddress and     rttMonEchoAdminTargetPort  \- for http and ftp probe     rttMonEchoAdminURL   \- for dns probe     rttMonEchoAdminTargetAddressString      rttMonEchoAdminNameServer   \- dhcp probe doesn't require any additional objects  All other objects can assume default values. The  conceptual Rtt control row will be placed into a  'pending' state (via the rttMonCtrlOperState object) if rttMonScheduleAdminRttStartTime is not specified.  Most conceptual Rtt control row objects cannot be  modified once this conceptual Rtt control row has been  created.  The objects that can change are the following\:   \- Objects in the rttMonReactAdminTable can be modified    as needed without setting this object to     'notInService'.  \- Objects in the rttMonScheduleAdminTable can be     modified only when this object has the value of    'notInService'.  \- The rttMonCtrlOperState can be modified to control    the state of the probe.  Once this object is in 'active' status, it cannot be  set to 'notInService' while the rttMonCtrlOperState is in 'active' state.  Thus the rttMonCtrlOperState  object must be transitioned first.   This object can be set to 'destroy' from any value at any time
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rttmonctrladminnvgen
            
            	When set to true, this entry will be shown in 'show running' command and can be saved into Non\-volatile memory
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonctrladmingroupname
            
            	If the operation is created through auto measure group creation, then this string will specify the group name to which this operation is associated
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: rttmonscheduleadminrttlife
            
            	This object value will be placed into the rttMonCtrlOperRttLife object when the rttMonCtrlOperState object transitions to 'active' or 'pending'.  The value 2147483647 has a special meaning.  When this object is set to 2147483647, the  rttMonCtrlOperRttLife object will not decrement.   And thus the life time will never end
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmonscheduleadminrttstarttime
            
            	This is the time when this conceptional row will activate.    This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will  cause the activation of a conceptual Rtt row.  When an agent has the capability to determine date and  time, the agent should store this object as DateAndTime. This allows the agent to completely reset (restart) and still be able to start conceptual Rtt rows at the  intended time.  If the agent cannot keep date and time and the agent resets, all entries should take on one of the special value defined below.  The first special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'active' state when the rttMonCtrlAdminStatus  object transitions to active. This special value is defined to be a value of this object that, when initially set, is 1.  The second special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'pending' state when  the rttMonCtrlAdminStatus object transitions to active.   Also, when the rttMonCtrlOperRttLife counts down to zero  (and not when set to zero), this special value causes  this conceptual Rtt control row to  retransition the  rttMonCtrlOperState object into 'pending' state.  This  special value is defined to be a value of this object  that, when initially set, is smaller than the current sysUpTime. (With the exception of one, as defined in the previous paragraph)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonscheduleadminconceptrowageout
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active'  state, this timer will be reset and suspended.  When  this conceptual RTT control row enters a state other  than 'active', the timer will be restarted.  NOTE\:  When a conceptual Rtt control row ages out, the         agent needs to remove the associated entries in         the rttMonReactTriggerAdminTable and         rttMonReactTriggerOperTable.  When this value is set to zero, this entry will never be aged out. rttMonScheduleAdminConceptRowAgeout object is superseded by rttMonScheduleAdminConceptRowAgeoutV2
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**config**\: False
            
            	**units**\: seconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonscheduleadminrttrecurring
            
            	When set to true, this entry will be scheduled to run automatically for the specified duration equal to the life configured, at the same time daily.  This value cannot be set to true  (a) if rttMonScheduleAdminRttLife object has value greater or    equal to 86400 seconds. (b) if sum of values of rttMonScheduleAdminRttLife and    rttMonScheduleAdminConceptRowAgeout is less or equal to    86400 seconds
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonscheduleadminconceptrowageoutv2
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active' state, this timer will be reset and suspended.  When this conceptual RTT control row enters a state other than 'active', the timer will be restarted.  NOTE\:  It is the same as rttMonScheduleAdminConceptRowAgeout        except DEFVAL is 0 to be consistent with CLI ageout        default.  When this value is set to zero, this entry will never be aged out
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmonreactadminconnectionenable
            
            	If true, a reaction is generated when a RTT operation to a rttMonEchoAdminTargetAddress (echo type) causes  rttMonCtrlOperConnectionLostOccurred to change its  value.  Thus connections to intermediate hops will  not cause this value to change. rttMonReactAdminConnectionEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadmintimeoutenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperTimeoutOccurred  to change its value.    When the RttMonRttType is 'pathEcho' timeouts to  intermediate hops will not cause  rttMonCtrlOperTimeoutOccurred to change its value. rttMonReactAdminTimeoutEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdtype
            
            	This object specifies the conditions under which rttMonCtrlOperOverThresholdOccurred is changed\:  NOTE\:  When the RttMonRttType is 'pathEcho' this         objects' value and all associated         object values are only valid when RTT         'echo' operations are to the        rttMonEchoAdminTargetAddress object address.  Thus        'pathEcho' operations to intermediate        hops will not cause this object to change.  never       \- rttMonCtrlOperOverThresholdOccurred is                 never set immediate   \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold;                 conversely                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                 falls below                 rttMonReactAdminThresholdFalling  consecutive \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold on                 rttMonReactAdminThresholdCount consecutive                 RTT operations; conversely,                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                falls under the                 rttMonReactAdminThresholdFalling                 for the same number of consecutive                 operations  xOfy        \- rttMonCtrlOperOverThresholdOccurred is set                 to true when x (as specified by                 rttMonReactAdminThresholdCount) out of the                 last y (as specified by                 rttMonReactAdminThresholdCount2)                 operation completion time exceeds                 rttMonCtrlAdminThreshold;                 conversely, it is set to false when x,                 out of the last y operation completion                time fall below                rttMonReactAdminThresholdFalling                NOTE\: When x > y, the probe will never                      generate a reaction. average     \- rttMonCtrlOperOverThresholdOccurred is set                 to true when the running average of the                 previous rttMonReactAdminThresholdCount                 operation completion times exceed                 rttMonCtrlAdminThreshold; conversely, it                 is set to false when the running average                 falls below the                 rttMonReactAdminThresholdFalling  If this value is changed by a management station,  rttMonCtrlOperOverThresholdOccurred is set to false, but  no reaction is generated if the prior value of  rttMonCtrlOperOverThresholdOccurred was true. rttMonReactAdminThresholdType object is superseded by rttMonReactThresholdType
            	**type**\:  :py:class:`RttMonReactAdminThresholdType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonReactAdminThresholdType>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdfalling
            
            	This object defines a threshold limit. If the RTT operation time falls below this limit and if the conditions specified in rttMonReactAdminThresholdType are satisfied, an  threshold is generated. rttMonReactAdminThresholdFalling object is superseded by rttMonReactThresholdFalling
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount
            
            	This object defines the 'x' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount object is superseded by rttMonReactThresholdCountX
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount2
            
            	This object defines the 'y' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount2 object is superseded by rttMonReactThresholdCountyY
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched  conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated nmvtOnly           \- an SNA NMVT is generated triggerOnly        \- all trigger actions defined for this                        entry are initiated trapAndNmvt        \- both a trap and an SNA NMVT are                        generated trapAndTrigger     \- both a trap and all trigger actions                        are initiated  nmvtAndTrigger     \- both a NMVT and all trigger actions                        are initiated trapNmvtAndTrigger \- a NMVT, trap, and all trigger actions                       are initiated  A trigger action is defined via the  rttMonReactTriggerAdminTable. rttMonReactAdminActionType object is superseded by rttMonReactActionType
            	**type**\:  :py:class:`RttMonReactAdminActionType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonReactAdminActionType>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminverifyerrorenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperVerifyErrorOccurred  to change its value. rttMonReactAdminVerifyErrorEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatisticsadminnumhourgroups
            
            	The maximum number of groups of paths to record. Specifically this is the number of hourly groups  to keep before rolling over.    The value of one is not advisable because the  group will close and immediately be deleted before the network management station will have the  opportunity to retrieve the statistics.   The value used in the rttMonStatsCaptureTable to  uniquely identify this group is the  rttMonStatsCaptureStartTimeIndex.  HTTP and Jitter probes store only two hours of data.  When this object is set to the value of zero all  rttMonStatsCaptureTable data capturing will be shut off
            	**type**\: int
            
            	**range:** 0..25
            
            	**config**\: False
            
            .. attribute:: rttmonstatisticsadminnumpaths
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics paths to record per hourly group.   This value directly represents the path to a target.   For all other RttMonRttTypes this value will be  forced to one by the agent.  NOTE\: For 'pathEcho' a source to target path will be        created to to hold all errors that occur when a        specific path or connection has not be found/setup.        Thus, it is advised to set this value greater       than one.  Since this index does not rollover, only the first rttMonStatisticsAdminNumPaths will be kept
            	**type**\: int
            
            	**range:** 1..128
            
            	**config**\: False
            
            .. attribute:: rttmonstatisticsadminnumhops
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics hops to record per path group.   This value directly represents the number of hops along  a path to a target, thus we can only support 30 hops.   For all other RttMonRttTypes this value will be  forced to one by the agent.  Since this index does not rollover, only the first rttMonStatisticsAdminNumHops will be kept. This object  is applicable to pathEcho probes only
            	**type**\: int
            
            	**range:** 1..30
            
            	**config**\: False
            
            .. attribute:: rttmonstatisticsadminnumdistbuckets
            
            	The maximum number of statistical distribution Buckets to accumulate.  Since this index does not rollover, only the first rttMonStatisticsAdminNumDistBuckets will be kept.  The last rttMonStatisticsAdminNumDistBucket will contain all entries from its distribution interval start point to infinity. This object is not applicable  to http and jitter probes
            	**type**\: int
            
            	**range:** 1..20
            
            	**config**\: False
            
            .. attribute:: rttmonstatisticsadmindistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  rttMonStatisticsAdminNumDistBuckets = 5 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  rttMonStatisticsAdminNumDistBuckets = 1 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of  rttMonStatisticsAdminDistInterval does not apply when rttMonStatisticsAdminNumDistBuckets is one. This object is not applicable to http and jitter probes
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhistoryadminnumlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the rttMonCtrlOperRttLife object.  A new life is created when the same conceptual RTT control row is restarted via the transition of the  rttMonCtrlOperRttLife object and its subsequent  countdown.  The value of zero will shut off all  rttMonHistoryAdminTable data collection
            	**type**\: int
            
            	**range:** 0..2
            
            	**config**\: False
            
            .. attribute:: rttmonhistoryadminnumbuckets
            
            	The maximum number of history buckets to record.  When the RttMonRttType is 'pathEcho'  this value directly  represents a path to a target.  For all other  RttMonRttTypes this value should be set to the number  of operations to keep per lifetime.  After rttMonHistoryAdminNumBuckets are filled, the  and the oldest entries are deleted and the most recent rttMonHistoryAdminNumBuckets buckets are retained
            	**type**\: int
            
            	**range:** 1..60
            
            	**config**\: False
            
            .. attribute:: rttmonhistoryadminnumsamples
            
            	The maximum number of history samples to record per bucket.  When the RttMonRttType is 'pathEcho' this  value directly represents the number of hops along a  path to a target, thus we can only support 30 hops. For all other RttMonRttTypes this value will be  forced to one by the agent
            	**type**\: int
            
            	**range:** 1..30
            
            	**config**\: False
            
            .. attribute:: rttmonhistoryadminfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none          \- no history is recorded all           \- the results of all completion times                   and failed completions are recorded overThreshold \- the results of completion times                  over rttMonCtrlAdminThreshold are                   recorded. failures      \- the results of failed operations (only)                   are recorded
            	**type**\:  :py:class:`RttMonHistoryAdminFilter <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonHistoryAdminFilter>`
            
            	**config**\: False
            
            .. attribute:: rttmonctrlopermodificationtime
            
            	This object is updated whenever an object in the conceptual RTT control row is changed or updated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperdiagtext
            
            	A string which can be used as an aid in tracing problems. The content of this field will depend on the type of  target (rttMonEchoAdminProtocol).   When rttMonEchoAdminProtocol is one of snaLU0EchoAppl, or  snaLU2EchoAppl this object contains the name of the  Logical Unit (LU) being used for this RTT session (from the HOST's point of view), once the session has been  established; this can then be used to correlate this  name to the connection information stored in the  Mainframe Host.  When rttMonEchoAdminProtocol is snaLU62EchoAppl, this  object contains the Logical Unit (LU) name being used for this RTT session, once the session has been established.   This name can be used by the management application to  correlate this objects value to the connection  information stored at this SNMP Agent via the APPC or  APPN mib.  When rttMonEchoAdminProtocol is not one of the  previously mentioned values, this value will be null.  It is primarily intended that this object contains  information which has significance to a human operator
            	**type**\: str
            
            	**length:** 0..51
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperresettime
            
            	This object is set when the rttMonCtrlOperState is set to reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperoctetsinuse
            
            	This object is the number of octets currently in use by this composite conceptual RTT row.  A composite conceptual row include the control, statistics, and  history conceptual rows combined.  (All octets that are addressed via the rttMonCtrlAdminIndex in this mib.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperconnectionlostoccurred
            
            	This object will only change its value when the RttMonRttType is 'echo' or 'pathEcho'.  This object is set to true when the RTT connection fails  to be established or is lost, and set to false when a  connection is reestablished.  When the RttMonRttType is 'pathEcho', connection loss applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  When this value changes and  rttMonReactAdminConnectionEnable is true, a reaction  will occur.   If a trap is sent it is a  rttMonConnectionChangeNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'connectionLoss(8)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'connectionLoss'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonctrlopertimeoutoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is set to true when an operation times out,  and set to false when an operation completes under  rttMonCtrlAdminTimeout.  When this value changes, a  reaction may occur, as defined by  rttMonReactAdminTimeoutEnable.   When the RttMonRttType is 'pathEcho', this timeout applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  If a trap is sent it is a rttMonTimeoutNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'timeout(7)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'timeout'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperoverthresholdoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is changed by operation completion times over threshold, as defined by rttMonReactAdminThresholdType.   When this value changes, a reaction may occur, as defined  by rttMonReactAdminThresholdType.   If a trap is sent it is a rttMonThresholdNotification.  This object is set to true if the operation completion time exceeds the rttMonCtrlAdminThreshold and set to false when an operation completes under rttMonCtrlAdminThreshold. When this value changes, a reaction may occur, as defined by rttMonReactThresholdType.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'rtt'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonctrlopernumrtts
            
            	This is the total number of probe operations that have been attempted.     This value is incremented for each start of an RTT  operation.  Thus when rttMonCtrlAdminRttType is set to  'pathEcho' this value will be incremented by one and  not for very every hop along the path.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object.  This value is not effected by the rollover of a statistics hourly group
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperrttlife
            
            	This object is decremented every second, until it reaches zero.  When the value of this object is zero RTT operations for this row are suspended.  This  object will either reach zero by a countdown or  it will transition to zero via setting the rttMonCtrlOperState.  When this object reaches zero the agent needs to  transition the rttMonCtrlOperState to 'inactive'.  REMEMBER\:  The value 2147483647 has a special             meaning.  When this object has the            value 2147483647, this object will            not decrement.  And thus the life             time will never.  When the rttMonCtrlOperState object is 'active' and  the rttMonReactTriggerOperState object transitions to  'active' this object will not be updated with the  current value of rttMonCrtlAdminRttLife object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrloperstate
            
            	The RttMonOperStatus object is used to manage the 'state' of the probe that is implementing  conceptual RTT control row.  This status object has six defined values\:  reset(1)          \- reset this entry, transition                     to 'pending' orderlyStop(2)    \- shutdown this entry at the end                      of the next RTT operation attempt,                       transition to 'inactive' immediateStop(3)  \- shutdown this entry immediately                      (if possible), transition to                       'inactive' pending(4)        \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control either                       via the rttMonScheduleAdminTable                       or the rttMonReactAdminTable/                      rttMonReactTriggerAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      reseting this object, and second                      by creating a conceptual Rtt control                      row with the                       rttMonScheduleAdminRttStartTime                      object with the its special value inactive(5)       \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control via                      the rttMonScheduleAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      setting this object to 'orderlyStop'                      or 'immediateStop', second by                       the rttMonCtrlOperRttLife object                      reaching zero active(6)         \- this value is not settable and                      this conceptual RTT control row is                      currently active restart(7)        \- this value is only settable when the                      state is active. It clears the data                      of this entry and remain on active state.  The probes action when this object is set to 'reset'\:   \-  all rows in rttMonStatsCaptureTable that relate to        this conceptual RTT control row are destroyed and        the indices are set to 1   \-  if rttMonStatisticsAdminNumHourGroups is not zero, a        single new rttMonStatsCaptureTable row is created   \-  all rows in rttMonHistoryCaptureTable that relate        to this RTT definition are destroyed and the indices       are set to 1   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperRttLife is set to        rttMonScheduleAdminRttLife   \-  rttMonCtrlOperNumRtts is set to zero   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur   \-  the next RTT operation is controlled by the objects       in the rttMonScheduleAdminTable or the        rttMonReactAdminTable/rttMonReactTriggerAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending'   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections must be maintained  This can be used to synchronize various RTT  definitions, so that the RTT requests occur  simultaneously, or as simultaneously as possible.  The probes action when this object transitions to    'inactive' (via setting this object to 'orderlyStop'    or 'immediateStop' or by rttMonCtrlOperRttLife    reaching zero)\:   \-  all statistics and history collection information       table entries will be closed and kept   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur.   \-  the next RTT request is controlled by the objects       in the rttMonScheduleAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending' (this denotes that       the Trigger will be ready the next time this       object goes active)   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections are to be closed and cleanup.               rttMonCtrlOperState                     STATE           +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+           \|      A       \|       B      \|      C      \| ACTION       \|  'pending'   \|  'inactive'  \|   'active'  \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|inconsistent\- \|   noError   \| \|  to 'reset'    \|              \| Value        \|             \| \|                \|    \-> A      \|              \|   \-> A      \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|    noError   \|   noError   \| \|to 'orderlyStop'\|    \-> B      \|    \-> B      \|   \-> B      \| \|     or to      \|              \|              \|             \| \|'immediateStop' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  Event causes  \|    \-> C      \|    \-> B      \|   \-> C      \| \| Trigger State  \|              \|              \|   see (3)   \| \| to transition  \|              \|              \|             \| \| to 'active'    \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> C      \|    \-> C      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of one.        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> A      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of less than   \|              \|              \|             \| \| current time,  \|              \|              \|             \| \| excluding one. \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> B      \|   see (2)   \| \| transitions to \|              \|              \|             \| \| 'notInService' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> B      \|    \-> B      \|   \-> B      \| \| transitions to \|              \|              \|             \| \| 'delete'       \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus is \|    \-> C      \|    \-> C      \|   \-> C      \| \| 'active' & the \|              \|              \|   see (3)   \| \| RttStartTime   \|              \|              \|             \| \| arrives        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|   RowAgeout    \|    \-> B      \|    \-> B      \|   \-> B      \| \|    expires     \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  OperRttLife   \|    N/A       \|    N/A       \|   \-> B      \| \| counts down to \|              \|              \|             \| \| zero           \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+  (1) \- rttMonCtrlOperState must have transitioned to 'inactive' or 'pending' before the rttMonCtrlAdminStatus can transition to 'active'.  See (2). (2) \- rttMonCtrlAdminStatus cannot transition to 'notInService' unless rttMonCtrlOperState has been previously forced to 'inactive' or 'pending'. (3) \- when this happens the rttMonCtrlOperRttLife will not be updated with the rttMonCtrlAdminRttLife.  NOTE\:  In order for all objects in a PDU to be set        at the same time, this object can not be        part of a multi\-bound PDU
            	**type**\:  :py:class:`RttMonCtrlOperState <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonCtrlOperState>`
            
            	**config**\: False
            
            .. attribute:: rttmonctrloperverifyerroroccurred
            
            	This object is true if rttMonCtrlAdminVerifyData is set to true and data corruption occurs
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonlatestrttopercompletiontime
            
            	The completion time of the latest RTT operation successfully completed.  The unit of this object will be microsecond when rttMonCtrlAdminRttType is set to 'jitter' and  rttMonEchoAdminPrecision is set to 'microsecond'. Otherwise, the unit of this object will be millisecond
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds/microseconds
            
            .. attribute:: rttmonlatestrttopersense
            
            	A sense code for the completion status of the latest RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatestrttoperapplspecificsense
            
            	An application specific sense code for the completion status of the latest RTT operation.  This  object will only be valid when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestrttopersensedescription
            
            	A sense description for the completion status of the latest RTT operation when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonlatestrttopertime
            
            	The value of the agent system time at the time of the latest RTT operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestrttoperaddress
            
            	When the RttMonRttType is 'echo', 'pathEcho', 'udpEcho', 'tcpConnect', 'dns' and 'dlsw' this is a string which specifies  the address of the target for this RTT operation.  When the  RttMonRttType is not one of these types this object will  be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry, self).__init__()

                self.yang_name = "rttMonCtrlAdminEntry"
                self.yang_parent_name = "rttMonCtrlAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.int32, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonctrladminowner', (YLeaf(YType.str, 'rttMonCtrlAdminOwner'), ['str'])),
                    ('rttmonctrladmintag', (YLeaf(YType.str, 'rttMonCtrlAdminTag'), ['str'])),
                    ('rttmonctrladminrtttype', (YLeaf(YType.enumeration, 'rttMonCtrlAdminRttType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonRttType', '')])),
                    ('rttmonctrladminthreshold', (YLeaf(YType.int32, 'rttMonCtrlAdminThreshold'), ['int'])),
                    ('rttmonctrladminfrequency', (YLeaf(YType.int32, 'rttMonCtrlAdminFrequency'), ['int'])),
                    ('rttmonctrladmintimeout', (YLeaf(YType.int32, 'rttMonCtrlAdminTimeout'), ['int'])),
                    ('rttmonctrladminverifydata', (YLeaf(YType.boolean, 'rttMonCtrlAdminVerifyData'), ['bool'])),
                    ('rttmonctrladminstatus', (YLeaf(YType.enumeration, 'rttMonCtrlAdminStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rttmonctrladminnvgen', (YLeaf(YType.boolean, 'rttMonCtrlAdminNvgen'), ['bool'])),
                    ('rttmonctrladmingroupname', (YLeaf(YType.str, 'rttMonCtrlAdminGroupName'), ['str'])),
                    ('rttmonscheduleadminrttlife', (YLeaf(YType.int32, 'rttMonScheduleAdminRttLife'), ['int'])),
                    ('rttmonscheduleadminrttstarttime', (YLeaf(YType.uint32, 'rttMonScheduleAdminRttStartTime'), ['int'])),
                    ('rttmonscheduleadminconceptrowageout', (YLeaf(YType.int32, 'rttMonScheduleAdminConceptRowAgeout'), ['int'])),
                    ('rttmonscheduleadminrttrecurring', (YLeaf(YType.boolean, 'rttMonScheduleAdminRttRecurring'), ['bool'])),
                    ('rttmonscheduleadminconceptrowageoutv2', (YLeaf(YType.int32, 'rttMonScheduleAdminConceptRowAgeoutV2'), ['int'])),
                    ('rttmonreactadminconnectionenable', (YLeaf(YType.boolean, 'rttMonReactAdminConnectionEnable'), ['bool'])),
                    ('rttmonreactadmintimeoutenable', (YLeaf(YType.boolean, 'rttMonReactAdminTimeoutEnable'), ['bool'])),
                    ('rttmonreactadminthresholdtype', (YLeaf(YType.enumeration, 'rttMonReactAdminThresholdType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonReactAdminThresholdType')])),
                    ('rttmonreactadminthresholdfalling', (YLeaf(YType.int32, 'rttMonReactAdminThresholdFalling'), ['int'])),
                    ('rttmonreactadminthresholdcount', (YLeaf(YType.int32, 'rttMonReactAdminThresholdCount'), ['int'])),
                    ('rttmonreactadminthresholdcount2', (YLeaf(YType.int32, 'rttMonReactAdminThresholdCount2'), ['int'])),
                    ('rttmonreactadminactiontype', (YLeaf(YType.enumeration, 'rttMonReactAdminActionType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonReactAdminActionType')])),
                    ('rttmonreactadminverifyerrorenable', (YLeaf(YType.boolean, 'rttMonReactAdminVerifyErrorEnable'), ['bool'])),
                    ('rttmonstatisticsadminnumhourgroups', (YLeaf(YType.int32, 'rttMonStatisticsAdminNumHourGroups'), ['int'])),
                    ('rttmonstatisticsadminnumpaths', (YLeaf(YType.int32, 'rttMonStatisticsAdminNumPaths'), ['int'])),
                    ('rttmonstatisticsadminnumhops', (YLeaf(YType.int32, 'rttMonStatisticsAdminNumHops'), ['int'])),
                    ('rttmonstatisticsadminnumdistbuckets', (YLeaf(YType.int32, 'rttMonStatisticsAdminNumDistBuckets'), ['int'])),
                    ('rttmonstatisticsadmindistinterval', (YLeaf(YType.int32, 'rttMonStatisticsAdminDistInterval'), ['int'])),
                    ('rttmonhistoryadminnumlives', (YLeaf(YType.int32, 'rttMonHistoryAdminNumLives'), ['int'])),
                    ('rttmonhistoryadminnumbuckets', (YLeaf(YType.int32, 'rttMonHistoryAdminNumBuckets'), ['int'])),
                    ('rttmonhistoryadminnumsamples', (YLeaf(YType.int32, 'rttMonHistoryAdminNumSamples'), ['int'])),
                    ('rttmonhistoryadminfilter', (YLeaf(YType.enumeration, 'rttMonHistoryAdminFilter'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonHistoryAdminFilter')])),
                    ('rttmonctrlopermodificationtime', (YLeaf(YType.uint32, 'rttMonCtrlOperModificationTime'), ['int'])),
                    ('rttmonctrloperdiagtext', (YLeaf(YType.str, 'rttMonCtrlOperDiagText'), ['str'])),
                    ('rttmonctrloperresettime', (YLeaf(YType.uint32, 'rttMonCtrlOperResetTime'), ['int'])),
                    ('rttmonctrloperoctetsinuse', (YLeaf(YType.uint32, 'rttMonCtrlOperOctetsInUse'), ['int'])),
                    ('rttmonctrloperconnectionlostoccurred', (YLeaf(YType.boolean, 'rttMonCtrlOperConnectionLostOccurred'), ['bool'])),
                    ('rttmonctrlopertimeoutoccurred', (YLeaf(YType.boolean, 'rttMonCtrlOperTimeoutOccurred'), ['bool'])),
                    ('rttmonctrloperoverthresholdoccurred', (YLeaf(YType.boolean, 'rttMonCtrlOperOverThresholdOccurred'), ['bool'])),
                    ('rttmonctrlopernumrtts', (YLeaf(YType.int32, 'rttMonCtrlOperNumRtts'), ['int'])),
                    ('rttmonctrloperrttlife', (YLeaf(YType.int32, 'rttMonCtrlOperRttLife'), ['int'])),
                    ('rttmonctrloperstate', (YLeaf(YType.enumeration, 'rttMonCtrlOperState'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonCtrlAdminTable.RttMonCtrlAdminEntry.RttMonCtrlOperState')])),
                    ('rttmonctrloperverifyerroroccurred', (YLeaf(YType.boolean, 'rttMonCtrlOperVerifyErrorOccurred'), ['bool'])),
                    ('rttmonlatestrttopercompletiontime', (YLeaf(YType.uint32, 'rttMonLatestRttOperCompletionTime'), ['int'])),
                    ('rttmonlatestrttopersense', (YLeaf(YType.enumeration, 'rttMonLatestRttOperSense'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttResponseSense', '')])),
                    ('rttmonlatestrttoperapplspecificsense', (YLeaf(YType.int32, 'rttMonLatestRttOperApplSpecificSense'), ['int'])),
                    ('rttmonlatestrttopersensedescription', (YLeaf(YType.str, 'rttMonLatestRttOperSenseDescription'), ['str'])),
                    ('rttmonlatestrttopertime', (YLeaf(YType.uint32, 'rttMonLatestRttOperTime'), ['int'])),
                    ('rttmonlatestrttoperaddress', (YLeaf(YType.str, 'rttMonLatestRttOperAddress'), ['str'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonctrladminowner = None
                self.rttmonctrladmintag = None
                self.rttmonctrladminrtttype = None
                self.rttmonctrladminthreshold = None
                self.rttmonctrladminfrequency = None
                self.rttmonctrladmintimeout = None
                self.rttmonctrladminverifydata = None
                self.rttmonctrladminstatus = None
                self.rttmonctrladminnvgen = None
                self.rttmonctrladmingroupname = None
                self.rttmonscheduleadminrttlife = None
                self.rttmonscheduleadminrttstarttime = None
                self.rttmonscheduleadminconceptrowageout = None
                self.rttmonscheduleadminrttrecurring = None
                self.rttmonscheduleadminconceptrowageoutv2 = None
                self.rttmonreactadminconnectionenable = None
                self.rttmonreactadmintimeoutenable = None
                self.rttmonreactadminthresholdtype = None
                self.rttmonreactadminthresholdfalling = None
                self.rttmonreactadminthresholdcount = None
                self.rttmonreactadminthresholdcount2 = None
                self.rttmonreactadminactiontype = None
                self.rttmonreactadminverifyerrorenable = None
                self.rttmonstatisticsadminnumhourgroups = None
                self.rttmonstatisticsadminnumpaths = None
                self.rttmonstatisticsadminnumhops = None
                self.rttmonstatisticsadminnumdistbuckets = None
                self.rttmonstatisticsadmindistinterval = None
                self.rttmonhistoryadminnumlives = None
                self.rttmonhistoryadminnumbuckets = None
                self.rttmonhistoryadminnumsamples = None
                self.rttmonhistoryadminfilter = None
                self.rttmonctrlopermodificationtime = None
                self.rttmonctrloperdiagtext = None
                self.rttmonctrloperresettime = None
                self.rttmonctrloperoctetsinuse = None
                self.rttmonctrloperconnectionlostoccurred = None
                self.rttmonctrlopertimeoutoccurred = None
                self.rttmonctrloperoverthresholdoccurred = None
                self.rttmonctrlopernumrtts = None
                self.rttmonctrloperrttlife = None
                self.rttmonctrloperstate = None
                self.rttmonctrloperverifyerroroccurred = None
                self.rttmonlatestrttopercompletiontime = None
                self.rttmonlatestrttopersense = None
                self.rttmonlatestrttoperapplspecificsense = None
                self.rttmonlatestrttopersensedescription = None
                self.rttmonlatestrttopertime = None
                self.rttmonlatestrttoperaddress = None
                self._segment_path = lambda: "rttMonCtrlAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonCtrlAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry, ['rttmonctrladminindex', 'rttmonctrladminowner', 'rttmonctrladmintag', 'rttmonctrladminrtttype', 'rttmonctrladminthreshold', 'rttmonctrladminfrequency', 'rttmonctrladmintimeout', 'rttmonctrladminverifydata', 'rttmonctrladminstatus', 'rttmonctrladminnvgen', 'rttmonctrladmingroupname', 'rttmonscheduleadminrttlife', 'rttmonscheduleadminrttstarttime', 'rttmonscheduleadminconceptrowageout', 'rttmonscheduleadminrttrecurring', 'rttmonscheduleadminconceptrowageoutv2', 'rttmonreactadminconnectionenable', 'rttmonreactadmintimeoutenable', 'rttmonreactadminthresholdtype', 'rttmonreactadminthresholdfalling', 'rttmonreactadminthresholdcount', 'rttmonreactadminthresholdcount2', 'rttmonreactadminactiontype', 'rttmonreactadminverifyerrorenable', 'rttmonstatisticsadminnumhourgroups', 'rttmonstatisticsadminnumpaths', 'rttmonstatisticsadminnumhops', 'rttmonstatisticsadminnumdistbuckets', 'rttmonstatisticsadmindistinterval', 'rttmonhistoryadminnumlives', 'rttmonhistoryadminnumbuckets', 'rttmonhistoryadminnumsamples', 'rttmonhistoryadminfilter', 'rttmonctrlopermodificationtime', 'rttmonctrloperdiagtext', 'rttmonctrloperresettime', 'rttmonctrloperoctetsinuse', 'rttmonctrloperconnectionlostoccurred', 'rttmonctrlopertimeoutoccurred', 'rttmonctrloperoverthresholdoccurred', 'rttmonctrlopernumrtts', 'rttmonctrloperrttlife', 'rttmonctrloperstate', 'rttmonctrloperverifyerroroccurred', 'rttmonlatestrttopercompletiontime', 'rttmonlatestrttopersense', 'rttmonlatestrttoperapplspecificsense', 'rttmonlatestrttopersensedescription', 'rttmonlatestrttopertime', 'rttmonlatestrttoperaddress'], name, value)

            class RttMonCtrlOperState(Enum):
                """
                RttMonCtrlOperState (Enum Class)

                The RttMonOperStatus object is used to

                manage the 'state' of the probe that is implementing 

                conceptual RTT control row.

                This status object has six defined values\:

                reset(1)          \- reset this entry, transition

                                    to 'pending'

                orderlyStop(2)    \- shutdown this entry at the end

                                     of the next RTT operation attempt, 

                                     transition to 'inactive'

                immediateStop(3)  \- shutdown this entry immediately

                                     (if possible), transition to 

                                     'inactive'

                pending(4)        \- this value is not settable and

                                     this conceptual RTT control row is 

                                     waiting for further control either 

                                     via the rttMonScheduleAdminTable 

                                     or the rttMonReactAdminTable/

                                     rttMonReactTriggerAdminTable;

                                     This object can transition to this

                                     value via two mechanisms, first by

                                     reseting this object, and second

                                     by creating a conceptual Rtt control

                                     row with the 

                                     rttMonScheduleAdminRttStartTime

                                     object with the its special value

                inactive(5)       \- this value is not settable and

                                     this conceptual RTT control row is 

                                     waiting for further control via

                                     the rttMonScheduleAdminTable;

                                     This object can transition to this

                                     value via two mechanisms, first by

                                     setting this object to 'orderlyStop'

                                     or 'immediateStop', second by 

                                     the rttMonCtrlOperRttLife object

                                     reaching zero

                active(6)         \- this value is not settable and

                                     this conceptual RTT control row is

                                     currently active

                restart(7)        \- this value is only settable when the

                                     state is active. It clears the data

                                     of this entry and remain on active state.

                The probes action when this object is set to 'reset'\:

                  \-  all rows in rttMonStatsCaptureTable that relate to 

                      this conceptual RTT control row are destroyed and 

                      the indices are set to 1

                  \-  if rttMonStatisticsAdminNumHourGroups is not zero, a 

                      single new rttMonStatsCaptureTable row is created

                  \-  all rows in rttMonHistoryCaptureTable that relate 

                      to this RTT definition are destroyed and the indices

                      are set to 1

                  \-  implied history used for timeout or threshold

                      notification (see rttMonReactAdminThresholdType or

                      rttMonReactThresholdType)

                      is purged

                  \-  rttMonCtrlOperRttLife is set to 

                      rttMonScheduleAdminRttLife

                  \-  rttMonCtrlOperNumRtts is set to zero

                  \-  rttMonCtrlOperTimeoutOccurred, 

                      rttMonCtrlOperOverThresholdOccurred, and 

                      rttMonCtrlOperConnectionLostOccurred are set to 

                      false; if this causes a change in the value of 

                      either of these objects, resolution notifications 

                      will not occur

                  \-  the next RTT operation is controlled by the objects

                      in the rttMonScheduleAdminTable or the 

                      rttMonReactAdminTable/rttMonReactTriggerAdminTable

                  \-  if the rttMonReactTriggerOperState is 'active', it 

                      will transition to 'pending'

                  \-  all rttMonReactTriggerAdminEntries pointing to

                      this conceptual entry with their 

                      rttMonReactTriggerOperState object 'active', 

                      will transition their OperState to 'pending'

                  \-  all open connections must be maintained

                This can be used to synchronize various RTT 

                definitions, so that the RTT requests occur 

                simultaneously, or as simultaneously as possible.

                The probes action when this object transitions to 

                  'inactive' (via setting this object to 'orderlyStop' 

                  or 'immediateStop' or by rttMonCtrlOperRttLife 

                  reaching zero)\:

                  \-  all statistics and history collection information

                      table entries will be closed and kept

                  \-  implied history used for timeout or threshold

                      notification (see rttMonReactAdminThresholdType or

                      rttMonReactThresholdType)

                      is purged

                  \-  rttMonCtrlOperTimeoutOccurred, 

                      rttMonCtrlOperOverThresholdOccurred, and 

                      rttMonCtrlOperConnectionLostOccurred are set to 

                      false; if this causes a change in the value of 

                      either of these objects, resolution notifications 

                      will not occur.

                  \-  the next RTT request is controlled by the objects

                      in the rttMonScheduleAdminTable

                  \-  if the rttMonReactTriggerOperState is 'active', it 

                      will transition to 'pending' (this denotes that

                      the Trigger will be ready the next time this

                      object goes active)

                  \-  all rttMonReactTriggerAdminEntries pointing to

                      this conceptual entry with their 

                      rttMonReactTriggerOperState object 'active', 

                      will transition their OperState to 'pending'

                  \-  all open connections are to be closed and cleanup.

                             rttMonCtrlOperState

                                    STATE

                          +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+

                          \|      A       \|       B      \|      C      \|

                ACTION       \|  'pending'   \|  'inactive'  \|   'active'  \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| OperState set  \|    noError   \|inconsistent\- \|   noError   \|

                \|  to 'reset'    \|              \| Value        \|             \|

                \|                \|    \-> A      \|              \|   \-> A      \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| OperState set  \|    noError   \|    noError   \|   noError   \|

                \|to 'orderlyStop'\|    \-> B      \|    \-> B      \|   \-> B      \|

                \|     or to      \|              \|              \|             \|

                \|'immediateStop' \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \|  Event causes  \|    \-> C      \|    \-> B      \|   \-> C      \|

                \| Trigger State  \|              \|              \|   see (3)   \|

                \| to transition  \|              \|              \|             \|

                \| to 'active'    \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| AdminStatus    \|    \-> C      \|    \-> C      \|   see (1)   \|

                \| transitions to \|              \|              \|             \|

                \| 'active' &     \|              \|              \|             \|

                \| RttStartTime is\|              \|              \|             \|

                \| special value  \|              \|              \|             \|

                \| of one.        \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| AdminStatus    \|    \-> A      \|    \-> A      \|   see (1)   \|

                \| transitions to \|              \|              \|             \|

                \| 'active' &     \|              \|              \|             \|

                \| RttStartTime is\|              \|              \|             \|

                \| special value  \|              \|              \|             \|

                \| of less than   \|              \|              \|             \|

                \| current time,  \|              \|              \|             \|

                \| excluding one. \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| AdminStatus    \|    \-> A      \|    \-> B      \|   see (2)   \|

                \| transitions to \|              \|              \|             \|

                \| 'notInService' \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| AdminStatus    \|    \-> B      \|    \-> B      \|   \-> B      \|

                \| transitions to \|              \|              \|             \|

                \| 'delete'       \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \| AdminStatus is \|    \-> C      \|    \-> C      \|   \-> C      \|

                \| 'active' & the \|              \|              \|   see (3)   \|

                \| RttStartTime   \|              \|              \|             \|

                \| arrives        \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \|   RowAgeout    \|    \-> B      \|    \-> B      \|   \-> B      \|

                \|    expires     \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                \|  OperRttLife   \|    N/A       \|    N/A       \|   \-> B      \|

                \| counts down to \|              \|              \|             \|

                \| zero           \|              \|              \|             \|

                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+

                (1) \- rttMonCtrlOperState must have transitioned to 'inactive'

                or 'pending' before the rttMonCtrlAdminStatus can

                transition to 'active'.  See (2).

                (2) \- rttMonCtrlAdminStatus cannot transition to 'notInService'

                unless rttMonCtrlOperState has been previously forced

                to 'inactive' or 'pending'.

                (3) \- when this happens the rttMonCtrlOperRttLife will not

                be updated with the rttMonCtrlAdminRttLife.

                NOTE\:  In order for all objects in a PDU to be set

                       at the same time, this object can not be

                       part of a multi\-bound PDU.

                .. data:: reset = 1

                .. data:: orderlyStop = 2

                .. data:: immediateStop = 3

                .. data:: pending = 4

                .. data:: inactive = 5

                .. data:: active = 6

                .. data:: restart = 7

                """

                reset = Enum.YLeaf(1, "reset")

                orderlyStop = Enum.YLeaf(2, "orderlyStop")

                immediateStop = Enum.YLeaf(3, "immediateStop")

                pending = Enum.YLeaf(4, "pending")

                inactive = Enum.YLeaf(5, "inactive")

                active = Enum.YLeaf(6, "active")

                restart = Enum.YLeaf(7, "restart")


            class RttMonHistoryAdminFilter(Enum):
                """
                RttMonHistoryAdminFilter (Enum Class)

                Defines a filter for adding RTT results to the history

                buffer\:

                none          \- no history is recorded

                all           \- the results of all completion times 

                                 and failed completions are recorded

                overThreshold \- the results of completion times

                                 over rttMonCtrlAdminThreshold are 

                                 recorded.

                failures      \- the results of failed operations (only) 

                                 are recorded.

                .. data:: none = 1

                .. data:: all = 2

                .. data:: overThreshold = 3

                .. data:: failures = 4

                """

                none = Enum.YLeaf(1, "none")

                all = Enum.YLeaf(2, "all")

                overThreshold = Enum.YLeaf(3, "overThreshold")

                failures = Enum.YLeaf(4, "failures")


            class RttMonReactAdminActionType(Enum):
                """
                RttMonReactAdminActionType (Enum Class)

                Specifies what type(s), if any, of reaction(s) to

                generate if an operation violates one of the watched 

                conditions\:

                none               \- no reaction is generated

                trapOnly           \- a trap is generated

                nmvtOnly           \- an SNA NMVT is generated

                triggerOnly        \- all trigger actions defined for this 

                                      entry are initiated

                trapAndNmvt        \- both a trap and an SNA NMVT are 

                                      generated

                trapAndTrigger     \- both a trap and all trigger actions 

                                      are initiated 

                nmvtAndTrigger     \- both a NMVT and all trigger actions 

                                      are initiated

                trapNmvtAndTrigger \- a NMVT, trap, and all trigger actions

                                      are initiated

                A trigger action is defined via the 

                rttMonReactTriggerAdminTable.

                rttMonReactAdminActionType object is superseded by

                rttMonReactActionType.

                .. data:: none = 1

                .. data:: trapOnly = 2

                .. data:: nmvtOnly = 3

                .. data:: triggerOnly = 4

                .. data:: trapAndNmvt = 5

                .. data:: trapAndTrigger = 6

                .. data:: nmvtAndTrigger = 7

                .. data:: trapNmvtAndTrigger = 8

                """

                none = Enum.YLeaf(1, "none")

                trapOnly = Enum.YLeaf(2, "trapOnly")

                nmvtOnly = Enum.YLeaf(3, "nmvtOnly")

                triggerOnly = Enum.YLeaf(4, "triggerOnly")

                trapAndNmvt = Enum.YLeaf(5, "trapAndNmvt")

                trapAndTrigger = Enum.YLeaf(6, "trapAndTrigger")

                nmvtAndTrigger = Enum.YLeaf(7, "nmvtAndTrigger")

                trapNmvtAndTrigger = Enum.YLeaf(8, "trapNmvtAndTrigger")


            class RttMonReactAdminThresholdType(Enum):
                """
                RttMonReactAdminThresholdType (Enum Class)

                This object specifies the conditions under which

                rttMonCtrlOperOverThresholdOccurred is changed\:

                NOTE\:  When the RttMonRttType is 'pathEcho' this 

                       objects' value and all associated 

                       object values are only valid when RTT 

                       'echo' operations are to the

                       rttMonEchoAdminTargetAddress object address.  Thus

                       'pathEcho' operations to intermediate

                       hops will not cause this object to change.

                never       \- rttMonCtrlOperOverThresholdOccurred is 

                               never set

                immediate   \- rttMonCtrlOperOverThresholdOccurred is set 

                               to true when an operation completion time 

                               exceeds rttMonCtrlAdminThreshold; 

                               conversely 

                               rttMonCtrlOperOverThresholdOccurred is set 

                               to false when an operation completion time 

                               falls below 

                               rttMonReactAdminThresholdFalling 

                consecutive \- rttMonCtrlOperOverThresholdOccurred is set 

                               to true when an operation completion time 

                               exceeds rttMonCtrlAdminThreshold on 

                               rttMonReactAdminThresholdCount consecutive 

                               RTT operations; conversely, 

                               rttMonCtrlOperOverThresholdOccurred is set 

                               to false when an operation completion time

                               falls under the 

                               rttMonReactAdminThresholdFalling 

                               for the same number of consecutive 

                               operations 

                xOfy        \- rttMonCtrlOperOverThresholdOccurred is set 

                               to true when x (as specified by 

                               rttMonReactAdminThresholdCount) out of the 

                               last y (as specified by 

                               rttMonReactAdminThresholdCount2) 

                               operation completion time exceeds 

                               rttMonCtrlAdminThreshold; 

                               conversely, it is set to false when x, 

                               out of the last y operation completion

                               time fall below

                               rttMonReactAdminThresholdFalling

                               NOTE\: When x > y, the probe will never

                                     generate a reaction.

                average     \- rttMonCtrlOperOverThresholdOccurred is set 

                               to true when the running average of the 

                               previous rttMonReactAdminThresholdCount 

                               operation completion times exceed 

                               rttMonCtrlAdminThreshold; conversely, it 

                               is set to false when the running average 

                               falls below the 

                               rttMonReactAdminThresholdFalling

                If this value is changed by a management station, 

                rttMonCtrlOperOverThresholdOccurred is set to false, but 

                no reaction is generated if the prior value of 

                rttMonCtrlOperOverThresholdOccurred was true.

                rttMonReactAdminThresholdType object is superseded by

                rttMonReactThresholdType.

                .. data:: never = 1

                .. data:: immediate = 2

                .. data:: consecutive = 3

                .. data:: xOfy = 4

                .. data:: average = 5

                """

                never = Enum.YLeaf(1, "never")

                immediate = Enum.YLeaf(2, "immediate")

                consecutive = Enum.YLeaf(3, "consecutive")

                xOfy = Enum.YLeaf(4, "xOfy")

                average = Enum.YLeaf(5, "average")





    class RttMonEchoAdminTable(Entity):
        """
        A table that contains Round Trip Time (RTT) specific
        definitions.
        
        This table is controlled via the 
        rttMonCtrlAdminTable.  Entries in this table are
        created via the rttMonCtrlAdminStatus object.
        
        .. attribute:: rttmonechoadminentry
        
        	A list of objects that define specific configuration for RttMonRttType conceptual Rtt control rows
        	**type**\: list of  		 :py:class:`RttMonEchoAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonEchoAdminTable, self).__init__()

            self.yang_name = "rttMonEchoAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonEchoAdminEntry", ("rttmonechoadminentry", CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonechoadminentry = YList(self)
            self._segment_path = lambda: "rttMonEchoAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonEchoAdminTable, [], name, value)


        class RttMonEchoAdminEntry(Entity):
            """
            A list of objects that define specific configuration for
            RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminprotocol
            
            	Specifies the protocol to be used to perform the RTT operation. The following list defines what protocol  should be used for each probe type\:  echo, pathEcho   \- ipIcmpEcho / mplsLspPingAppl udpEcho          \- ipUdpEchoAppl tcpConnect       \- ipTcpConn http             \- httpAppl jitter           \- jitterAppl dlsw             \- dlswAppl dhcp             \- dhcpAppl ftp              \- ftpAppl mplsLspPing      \- mplsLspPingAppl voip             \- voipAppl video            \- videoAppl  When this protocol does not support the type, a 'badValue' error will be returned
            	**type**\:  :py:class:`RttMonProtocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonProtocol>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetaddress
            
            	A string which specifies the address of the target
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminpktdatarequestsize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request  message, when using SNA protocols.  For non\-ARR protocols' RTT request/responses,  this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included             in this value.  For echo probes the total packet size = (IP header(20) +  ICMP header(8) + 8 (internal timestamps) + request size).  For echo and pathEcho default request size is 28. For udp probe, default request size is 16 and for jitter  probe it is 32. For dlsw probes default request size is 0.  The minimum request size for echo and pathEcho is 28 bytes, for udp it is 4 and for jitter it is 16. For udp and jitter probes the maximum request size is 1500.  For ethernetPing the default request size is 66. For ethernetJitter the default request size is 51
            	**type**\: int
            
            	**range:** 0..16384
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadminpktdataresponsesize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the response message. This value is passed to the RTT Echo Server via a field in the ARR Header.  For non\-ARR RTT request/response (i.e. ipIcmpecho) this value will be set by the agent to match the size of rttMonEchoAdminPktDataRequestSize, when native payloads are supported.  REMEMBER\:  The ARR Header overhead is not included             in this value.  This object is only supported by SNA protocols
            	**type**\: int
            
            	**range:** 0..16384
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetport
            
            	This object represents the target's port number. This object is applicable to udpEcho, tcpConnect and jitter probes
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminsourceaddress
            
            	A string which specifies the IP address of the source. This object is applicable to all probes except dns, dlsw  and sna
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminsourceport
            
            	This object represents the source's port number. If this object is not specified, the application will get a  port allocated by the system. This object is applicable  to all probes except dns, dlsw and sna
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincontrolenable
            
            	If this object is enabled, then the RTR application will send control messages to a responder, residing on the  target router to respond to the data request packets being  sent by the source router. This object is not applicable to  echo, pathEcho, dns and http probes
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintos
            
            	This object represents the type of service octet in an IP header. This object is not applicable to dhcp, dns,  ethernetPing and ethernetJitter
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlsrenable
            
            	If this object is enabled then it means that the application calculates response time for a specific path, defined in rttMonEchoPathAdminEntry. This object is applicable to echo  probe only
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetaddressstring
            
            	A string which specifies the address of the target. This string can be in IP address format or a hostname. This object is applicable to dns probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminnameserver
            
            	A string which specifies the ip address of the name\-server. This object is applicable to dns probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminoperation
            
            	A code that represents the specific type of RTT operation. This object is applicable to http and ftp probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminhttpversion
            
            	A string which specifies the version number of the HTTP Server.  The syntax for the version string is  <major number>.<minor number> An example would be 1.0,  1.1 etc.,.  This object is applicable to http probe only
            	**type**\: str
            
            	**length:** 3..10
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminurl
            
            	A string which represents the URL to which a HTTP probe should communicate with. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincache
            
            	If this object is false then it means that HTTP request should not download cached pages. This means that the request should  be forwarded to the origin server. This object is applicable to http probe only
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmininterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for  Jitter probe. This object is applicable to jitter probe only
            	**type**\: int
            
            	**range:** 0..60000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadminnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe.  This object is applicable to jitter probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminproxy
            
            	This string represents the proxy server information. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminstring1
            
            	This string stores the content of HTTP raw request. If the request cannot fit into String1 then it should  be split and put in Strings 1 through 5.  This string stores the content of the DHCP raw option data.  The raw DHCP option data must be in HEX. If an odd number of characters are specified, a 0 will be appended to the end of the string.  Only DHCP option 82 (decimal) is allowed. Here is an example of a valid string\: 5208010610005A6F1234 Only rttMonEchoAdminString1 is used for dhcp, Strings 1 through 5 are not used.  This object is applicable to http and dhcp probe  types only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminstring2
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminstring3
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminstring4
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminstring5
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminmode
            
            	A code that represents the specific type of RTT operation. This object is applicable to ftp probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminvrfname
            
            	This field is used to specify the VPN name in which the RTT operation will be used. For regular RTT operation this field should not be configured. The agent  will use this field to identify the VPN routing Table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincodectype
            
            	Specifies the codec type to be used with jitter probe. This is applicable only for the jitter probe.  If codec\-type is configured the following parameters cannot be  configured. rttMonEchoAdminPktDataRequestSize rttMonEchoAdminInterval rttMonEchoAdminNumPackets
            	**type**\:  :py:class:`RttMonCodecType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonCodecType>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincodecinterval
            
            	This field represents the inter\-packet delay between packets and is in milliseconds. This object is applicable only to jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..60000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadmincodecpayload
            
            	This object represents the number of octets that needs to be placed into the Data portion of the message. This value is used only for jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..16384
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadmincodecnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is used only for jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..60000
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminicpifadvfactor
            
            	The advantage factor is dependant on the type of access and how the service is to be used. Conventional Wire\-line     0 Mobility within Building    5 Mobility within geographic area  10 Access to hard\-to\-reach location   20  This will be used while calculating the ICPIF values This valid only for Jitter while calculating the ICPIF value
            	**type**\: int
            
            	**range:** 0..20
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspfectype
            
            	The type of the target FEC for the RTT 'echo' and 'pathEcho' operations based on 'mplsLspPingAppl' RttMonProtocol.  ldpIpv4Prefix   \- LDP IPv4 prefix
            	**type**\:  :py:class:`RttMonEchoAdminLSPFECType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminLSPFECType>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspselector
            
            	A string which specifies a valid 127/8 address. This address is of the form 127.x.y.z. This address is not used to route the MPLS echo packet to the destination but is used for load balancing in cases where the IP payload's destination address is used for load balancing
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests
            	**type**\:  :py:class:`RttMonLSPPingReplyMode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonLSPPingReplyMode>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspttl
            
            	This object represents the TTL setting for MPLS echo request packets. For ping operation this represents the TTL value to be set in the echo request packet. For trace operation it represent the maximum ttl value that can be set in the echo request packets starting with TTL=1.  For 'echo' based on mplsLspPingAppl the default TTL will be set to 255, and for 'pathEcho' based on mplsLspPingAppl the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values to be used for 'echo' and 'pathEcho' based on 'mplsLspPingAppl'
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspexp
            
            	This object represents the EXP value that needs to be put as precedence bit in the MPLS echo request IP header
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminprecision
            
            	This object specifies the accuracy of statistics that needs to be calculated milliseconds \- The accuracy of stats will be of milliseconds microseconds \- The accuracy of stats will be in microseconds. This value can be set only for jitter operation
            	**type**\:  :py:class:`RttMonEchoAdminPrecision <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminPrecision>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminprobepakpriority
            
            	This object specifies the priority that will be assigned to probe packet.  This value can be set only for jitter  operation
            	**type**\:  :py:class:`RttMonEchoAdminProbePakPriority <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminProbePakPriority>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminowntpsynctolabs
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of NTP offsets on source and responder. The value specified is  microseconds. This value can be set only for jitter operation  with precision of microsecond
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rttmonechoadminowntpsynctolpct
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of  NTP offsets on source and responder. The value is expressed  as the percentage of actual oneway latency that is measured.  This value can be set only for jitter operation with precision  of microsecond
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminowntpsynctoltype
            
            	This object specifies whether the value in specified for oneway NTP sync tolerance is absolute value or percent value
            	**type**\:  :py:class:`RttMonEchoAdminOWNTPSyncTolType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminOWNTPSyncTolType>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincallednumber
            
            	This string stores the called number of post dial delay. This object is applicable to voip post dial delay probe only. The number will be like the one actualy the user could dial. It has the number required by the local country dial plan, plus E.164 number. The maximum length is 24 digits. Only digit (0\-9) is allowed
            	**type**\: str
            
            	**length:** 0..24
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmindetectpoint
            
            	A code that represents the detect point of post dial delay. This object is applicable to SAA post dial delay probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmingkregistration
            
            	A boolean that represents VoIP GK registration delay. This object is applicable to SAA GK registration delay  probe only
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminsourcevoiceport
            
            	A string which specifies the voice\-port on the source gateway. This object is applicable to RTP probe only
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincallduration
            
            	Duration of RTP/Video Probe session. This object is applicable to RTP and Video probe
            	**type**\: int
            
            	**range:** 1..600
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\: int
            
            	**range:** 0..63 \| 255..None
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspnullshim
            
            	This object specifies if the explicit\-null label is to be added to LSP echo requests which are sent while performing RTT operation
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetmpid
            
            	This object specifies the destination maintenance point ID. It is only applicable to ethernetPing and ethernetJitter  operation. It will be set to 0 for other types of  operations
            	**type**\: int
            
            	**range:** 0..8191
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetdomainname
            
            	This object specifies the name of the domain in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetvlan
            
            	This object specifies the ID of the VLAN in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to 0 for other types of operations
            	**type**\: int
            
            	**range:** 1..4094
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminethernetcos
            
            	This object specifies the class of service in an Ethernet packet header. It is only applicable to ethernetPing and  ethernetJitter operation
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlspvccvid
            
            	This object specifies MPLS LSP pseudowire VCCV ID values between 1 to 2147483647.  Note\: This object cannot be set to value of 0. This default value specifies that VCCV is not set for this row
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetevc
            
            	This object specifies the Ethernet Virtual Connection in which the destination maintenance point lies. It is only  applicable to ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\: str
            
            	**length:** 0..100
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetmepport
            
            	This object specifies that Port Level CFM testing towards an Outward/Down MEP will be used. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminvideotrafficprofile
            
            	A string which represents the profile name to which a video probe should use. This object is applicable to video probe only
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmindscp
            
            	This object represents the Differentiated Service Code Point (DSCP) QoS marking in the generated synthetic packets.  Value \- DiffServ Class     0 \- BE (default)    10 \- AF11    12 \- AF12    14 \- AF13    18 \- AF21    20 \- AF22    22 \- AF23    26 \- AF31    28 \- AF32    30 \- AF33    34 \- AF41    36 \- AF42    38 \- AF43     8 \- CS1    16 \- CS2    24 \- CS3    32 \- CS4    40 \- CS5    48 \- CS6    56 \- CS7    46 \- EF
            	**type**\: int
            
            	**range:** 0..63
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminreservedsp
            
            	This object represents the video traffic generation source.  be \: best effort using DSP but without reservation gs \: guaranteed service using DSP with reservation na \: not applicable for not using DSP
            	**type**\:  :py:class:`RttMonEchoAdminReserveDsp <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminReserveDsp>`
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmininputinterface
            
            	This object represents the network input interface on the sender router where the synthetic packets are received from the emulated endpoint source. This is used for path congruence with correct feature processing at the sender router.  The user can get the InterfaceIndex number from ifIndex object by looking up in ifTable. In fact, it should be useful to first get the entry by the augmented table ifXTable which has ifName object which matches the interface name used on the router or switch equipment console
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminemulatesourceaddress
            
            	This object specifies the IP address of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source IP address will by default be the same as rttMonEchoAdminSourceAddress. This object is applicable to video probes
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminemulatesourceport
            
            	This object represents the port number of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source port number will by default be the same as rttMonEchoAdminSourcePort. This object is applicable to video probes
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminemulatetargetaddress
            
            	This object specifies the IP address of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target IP address will by default be the same as rttMonEchoAdminTargetAddress. This object is applicable to video probes
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminemulatetargetport
            
            	This object represents the port number of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target port number will by default be the same as rttMonEchoAdminTargetPort. This object is applicable to video probes
            	**type**\: int
            
            	**range:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintargetmacaddress
            
            	This object indicates the MAC address of the target device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminTargetMacAddress and rttMonEchoAdminTargetMPID may not be used in conjunction
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminsourcemacaddress
            
            	This object indicates the MAC address of the source device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminSourceMacAddress and rttMonEchoAdminSourceMPID may not be used in conjunction
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminsourcempid
            
            	This object indicates the source maintenance point ID.  It is only applicable to Y.1731 operation.  It will be set to zero for other types of opearations.  rttMonEchoAdminSourceMPID and rttMonEchoAdminSourceMacAddress may not be used in conjunction
            	**type**\: int
            
            	**range:** 0..8191
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminendpointlistname
            
            	This object specifies the name of endpoint list which a probe uses to generate operations
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminssm
            
            	This object specifies if Source Specific Multicast is to be added. This object is applicable to multicast probe only
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincontrolretry
            
            	This object specifies the maximum number of retries for control message
            	**type**\: int
            
            	**range:** 1..5
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmincontroltimeout
            
            	This object specifies the wait duration before control message timeout
            	**type**\: int
            
            	**range:** 1..10000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadminigmptreeinit
            
            	This object specifies number of packets to be sent for multicast tree setup. This object is applicable to multicast probe only
            	**type**\: int
            
            	**range:** 0..10
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminenableburst
            
            	This object indicates that packets will be sent in burst
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminaggburstcycles
            
            	This object indicates the number of burst cycles to be sent during the aggregate interval. This value is currently used for Y1731 SLM(Synthetic Loss Measurment) probe. This object is applicable to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminlossrationumframes
            
            	This object indicates the number of frames over which to calculate the frame loss ratio. This object is applicable  to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadminavailnumframes
            
            	This object indicates the number of frames over which to calculate the availability. This object is applicable to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonechoadmintstampoptimization
            
            	This object specifies whether timestamp optimization is enabled.  When the value is 'true' then timestamp optimization is enabled.  The probe will utilize lower layer (Hardware/Packet Processor) timestamping values to improve accuracy of statistics.  This value can be set only for udp jitter operation with precision of microsecond
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry, self).__init__()

                self.yang_name = "rttMonEchoAdminEntry"
                self.yang_parent_name = "rttMonEchoAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonechoadminprotocol', (YLeaf(YType.enumeration, 'rttMonEchoAdminProtocol'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonProtocol', '')])),
                    ('rttmonechoadmintargetaddress', (YLeaf(YType.str, 'rttMonEchoAdminTargetAddress'), ['str'])),
                    ('rttmonechoadminpktdatarequestsize', (YLeaf(YType.int32, 'rttMonEchoAdminPktDataRequestSize'), ['int'])),
                    ('rttmonechoadminpktdataresponsesize', (YLeaf(YType.int32, 'rttMonEchoAdminPktDataResponseSize'), ['int'])),
                    ('rttmonechoadmintargetport', (YLeaf(YType.int32, 'rttMonEchoAdminTargetPort'), ['int'])),
                    ('rttmonechoadminsourceaddress', (YLeaf(YType.str, 'rttMonEchoAdminSourceAddress'), ['str'])),
                    ('rttmonechoadminsourceport', (YLeaf(YType.int32, 'rttMonEchoAdminSourcePort'), ['int'])),
                    ('rttmonechoadmincontrolenable', (YLeaf(YType.boolean, 'rttMonEchoAdminControlEnable'), ['bool'])),
                    ('rttmonechoadmintos', (YLeaf(YType.int32, 'rttMonEchoAdminTOS'), ['int'])),
                    ('rttmonechoadminlsrenable', (YLeaf(YType.boolean, 'rttMonEchoAdminLSREnable'), ['bool'])),
                    ('rttmonechoadmintargetaddressstring', (YLeaf(YType.str, 'rttMonEchoAdminTargetAddressString'), ['str'])),
                    ('rttmonechoadminnameserver', (YLeaf(YType.str, 'rttMonEchoAdminNameServer'), ['str'])),
                    ('rttmonechoadminoperation', (YLeaf(YType.enumeration, 'rttMonEchoAdminOperation'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonOperation', '')])),
                    ('rttmonechoadminhttpversion', (YLeaf(YType.str, 'rttMonEchoAdminHTTPVersion'), ['str'])),
                    ('rttmonechoadminurl', (YLeaf(YType.str, 'rttMonEchoAdminURL'), ['str'])),
                    ('rttmonechoadmincache', (YLeaf(YType.boolean, 'rttMonEchoAdminCache'), ['bool'])),
                    ('rttmonechoadmininterval', (YLeaf(YType.int32, 'rttMonEchoAdminInterval'), ['int'])),
                    ('rttmonechoadminnumpackets', (YLeaf(YType.int32, 'rttMonEchoAdminNumPackets'), ['int'])),
                    ('rttmonechoadminproxy', (YLeaf(YType.str, 'rttMonEchoAdminProxy'), ['str'])),
                    ('rttmonechoadminstring1', (YLeaf(YType.str, 'rttMonEchoAdminString1'), ['str'])),
                    ('rttmonechoadminstring2', (YLeaf(YType.str, 'rttMonEchoAdminString2'), ['str'])),
                    ('rttmonechoadminstring3', (YLeaf(YType.str, 'rttMonEchoAdminString3'), ['str'])),
                    ('rttmonechoadminstring4', (YLeaf(YType.str, 'rttMonEchoAdminString4'), ['str'])),
                    ('rttmonechoadminstring5', (YLeaf(YType.str, 'rttMonEchoAdminString5'), ['str'])),
                    ('rttmonechoadminmode', (YLeaf(YType.enumeration, 'rttMonEchoAdminMode'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonOperation', '')])),
                    ('rttmonechoadminvrfname', (YLeaf(YType.str, 'rttMonEchoAdminVrfName'), ['str'])),
                    ('rttmonechoadmincodectype', (YLeaf(YType.enumeration, 'rttMonEchoAdminCodecType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonCodecType', '')])),
                    ('rttmonechoadmincodecinterval', (YLeaf(YType.int32, 'rttMonEchoAdminCodecInterval'), ['int'])),
                    ('rttmonechoadmincodecpayload', (YLeaf(YType.int32, 'rttMonEchoAdminCodecPayload'), ['int'])),
                    ('rttmonechoadmincodecnumpackets', (YLeaf(YType.int32, 'rttMonEchoAdminCodecNumPackets'), ['int'])),
                    ('rttmonechoadminicpifadvfactor', (YLeaf(YType.int32, 'rttMonEchoAdminICPIFAdvFactor'), ['int'])),
                    ('rttmonechoadminlspfectype', (YLeaf(YType.enumeration, 'rttMonEchoAdminLSPFECType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminLSPFECType')])),
                    ('rttmonechoadminlspselector', (YLeaf(YType.str, 'rttMonEchoAdminLSPSelector'), ['str'])),
                    ('rttmonechoadminlspreplymode', (YLeaf(YType.enumeration, 'rttMonEchoAdminLSPReplyMode'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonLSPPingReplyMode', '')])),
                    ('rttmonechoadminlspttl', (YLeaf(YType.int32, 'rttMonEchoAdminLSPTTL'), ['int'])),
                    ('rttmonechoadminlspexp', (YLeaf(YType.int32, 'rttMonEchoAdminLSPExp'), ['int'])),
                    ('rttmonechoadminprecision', (YLeaf(YType.enumeration, 'rttMonEchoAdminPrecision'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminPrecision')])),
                    ('rttmonechoadminprobepakpriority', (YLeaf(YType.enumeration, 'rttMonEchoAdminProbePakPriority'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminProbePakPriority')])),
                    ('rttmonechoadminowntpsynctolabs', (YLeaf(YType.int32, 'rttMonEchoAdminOWNTPSyncTolAbs'), ['int'])),
                    ('rttmonechoadminowntpsynctolpct', (YLeaf(YType.int32, 'rttMonEchoAdminOWNTPSyncTolPct'), ['int'])),
                    ('rttmonechoadminowntpsynctoltype', (YLeaf(YType.enumeration, 'rttMonEchoAdminOWNTPSyncTolType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminOWNTPSyncTolType')])),
                    ('rttmonechoadmincallednumber', (YLeaf(YType.str, 'rttMonEchoAdminCalledNumber'), ['str'])),
                    ('rttmonechoadmindetectpoint', (YLeaf(YType.enumeration, 'rttMonEchoAdminDetectPoint'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonOperation', '')])),
                    ('rttmonechoadmingkregistration', (YLeaf(YType.boolean, 'rttMonEchoAdminGKRegistration'), ['bool'])),
                    ('rttmonechoadminsourcevoiceport', (YLeaf(YType.str, 'rttMonEchoAdminSourceVoicePort'), ['str'])),
                    ('rttmonechoadmincallduration', (YLeaf(YType.int32, 'rttMonEchoAdminCallDuration'), ['int'])),
                    ('rttmonechoadminlspreplydscp', (YLeaf(YType.int32, 'rttMonEchoAdminLSPReplyDscp'), ['int'])),
                    ('rttmonechoadminlspnullshim', (YLeaf(YType.boolean, 'rttMonEchoAdminLSPNullShim'), ['bool'])),
                    ('rttmonechoadmintargetmpid', (YLeaf(YType.uint32, 'rttMonEchoAdminTargetMPID'), ['int'])),
                    ('rttmonechoadmintargetdomainname', (YLeaf(YType.str, 'rttMonEchoAdminTargetDomainName'), ['str'])),
                    ('rttmonechoadmintargetvlan', (YLeaf(YType.int32, 'rttMonEchoAdminTargetVLAN'), ['int'])),
                    ('rttmonechoadminethernetcos', (YLeaf(YType.int32, 'rttMonEchoAdminEthernetCOS'), ['int'])),
                    ('rttmonechoadminlspvccvid', (YLeaf(YType.int32, 'rttMonEchoAdminLSPVccvID'), ['int'])),
                    ('rttmonechoadmintargetevc', (YLeaf(YType.str, 'rttMonEchoAdminTargetEVC'), ['str'])),
                    ('rttmonechoadmintargetmepport', (YLeaf(YType.boolean, 'rttMonEchoAdminTargetMEPPort'), ['bool'])),
                    ('rttmonechoadminvideotrafficprofile', (YLeaf(YType.str, 'rttMonEchoAdminVideoTrafficProfile'), ['str'])),
                    ('rttmonechoadmindscp', (YLeaf(YType.uint8, 'rttMonEchoAdminDscp'), ['int'])),
                    ('rttmonechoadminreservedsp', (YLeaf(YType.enumeration, 'rttMonEchoAdminReserveDsp'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonEchoAdminTable.RttMonEchoAdminEntry.RttMonEchoAdminReserveDsp')])),
                    ('rttmonechoadmininputinterface', (YLeaf(YType.int32, 'rttMonEchoAdminInputInterface'), ['int'])),
                    ('rttmonechoadminemulatesourceaddress', (YLeaf(YType.str, 'rttMonEchoAdminEmulateSourceAddress'), ['str'])),
                    ('rttmonechoadminemulatesourceport', (YLeaf(YType.int32, 'rttMonEchoAdminEmulateSourcePort'), ['int'])),
                    ('rttmonechoadminemulatetargetaddress', (YLeaf(YType.str, 'rttMonEchoAdminEmulateTargetAddress'), ['str'])),
                    ('rttmonechoadminemulatetargetport', (YLeaf(YType.int32, 'rttMonEchoAdminEmulateTargetPort'), ['int'])),
                    ('rttmonechoadmintargetmacaddress', (YLeaf(YType.str, 'rttMonEchoAdminTargetMacAddress'), ['str'])),
                    ('rttmonechoadminsourcemacaddress', (YLeaf(YType.str, 'rttMonEchoAdminSourceMacAddress'), ['str'])),
                    ('rttmonechoadminsourcempid', (YLeaf(YType.uint32, 'rttMonEchoAdminSourceMPID'), ['int'])),
                    ('rttmonechoadminendpointlistname', (YLeaf(YType.str, 'rttMonEchoAdminEndPointListName'), ['str'])),
                    ('rttmonechoadminssm', (YLeaf(YType.boolean, 'rttMonEchoAdminSSM'), ['bool'])),
                    ('rttmonechoadmincontrolretry', (YLeaf(YType.uint32, 'rttMonEchoAdminControlRetry'), ['int'])),
                    ('rttmonechoadmincontroltimeout', (YLeaf(YType.uint32, 'rttMonEchoAdminControlTimeout'), ['int'])),
                    ('rttmonechoadminigmptreeinit', (YLeaf(YType.uint32, 'rttMonEchoAdminIgmpTreeInit'), ['int'])),
                    ('rttmonechoadminenableburst', (YLeaf(YType.boolean, 'rttMonEchoAdminEnableBurst'), ['bool'])),
                    ('rttmonechoadminaggburstcycles', (YLeaf(YType.int32, 'rttMonEchoAdminAggBurstCycles'), ['int'])),
                    ('rttmonechoadminlossrationumframes', (YLeaf(YType.int32, 'rttMonEchoAdminLossRatioNumFrames'), ['int'])),
                    ('rttmonechoadminavailnumframes', (YLeaf(YType.int32, 'rttMonEchoAdminAvailNumFrames'), ['int'])),
                    ('rttmonechoadmintstampoptimization', (YLeaf(YType.boolean, 'rttMonEchoAdminTstampOptimization'), ['bool'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonechoadminprotocol = None
                self.rttmonechoadmintargetaddress = None
                self.rttmonechoadminpktdatarequestsize = None
                self.rttmonechoadminpktdataresponsesize = None
                self.rttmonechoadmintargetport = None
                self.rttmonechoadminsourceaddress = None
                self.rttmonechoadminsourceport = None
                self.rttmonechoadmincontrolenable = None
                self.rttmonechoadmintos = None
                self.rttmonechoadminlsrenable = None
                self.rttmonechoadmintargetaddressstring = None
                self.rttmonechoadminnameserver = None
                self.rttmonechoadminoperation = None
                self.rttmonechoadminhttpversion = None
                self.rttmonechoadminurl = None
                self.rttmonechoadmincache = None
                self.rttmonechoadmininterval = None
                self.rttmonechoadminnumpackets = None
                self.rttmonechoadminproxy = None
                self.rttmonechoadminstring1 = None
                self.rttmonechoadminstring2 = None
                self.rttmonechoadminstring3 = None
                self.rttmonechoadminstring4 = None
                self.rttmonechoadminstring5 = None
                self.rttmonechoadminmode = None
                self.rttmonechoadminvrfname = None
                self.rttmonechoadmincodectype = None
                self.rttmonechoadmincodecinterval = None
                self.rttmonechoadmincodecpayload = None
                self.rttmonechoadmincodecnumpackets = None
                self.rttmonechoadminicpifadvfactor = None
                self.rttmonechoadminlspfectype = None
                self.rttmonechoadminlspselector = None
                self.rttmonechoadminlspreplymode = None
                self.rttmonechoadminlspttl = None
                self.rttmonechoadminlspexp = None
                self.rttmonechoadminprecision = None
                self.rttmonechoadminprobepakpriority = None
                self.rttmonechoadminowntpsynctolabs = None
                self.rttmonechoadminowntpsynctolpct = None
                self.rttmonechoadminowntpsynctoltype = None
                self.rttmonechoadmincallednumber = None
                self.rttmonechoadmindetectpoint = None
                self.rttmonechoadmingkregistration = None
                self.rttmonechoadminsourcevoiceport = None
                self.rttmonechoadmincallduration = None
                self.rttmonechoadminlspreplydscp = None
                self.rttmonechoadminlspnullshim = None
                self.rttmonechoadmintargetmpid = None
                self.rttmonechoadmintargetdomainname = None
                self.rttmonechoadmintargetvlan = None
                self.rttmonechoadminethernetcos = None
                self.rttmonechoadminlspvccvid = None
                self.rttmonechoadmintargetevc = None
                self.rttmonechoadmintargetmepport = None
                self.rttmonechoadminvideotrafficprofile = None
                self.rttmonechoadmindscp = None
                self.rttmonechoadminreservedsp = None
                self.rttmonechoadmininputinterface = None
                self.rttmonechoadminemulatesourceaddress = None
                self.rttmonechoadminemulatesourceport = None
                self.rttmonechoadminemulatetargetaddress = None
                self.rttmonechoadminemulatetargetport = None
                self.rttmonechoadmintargetmacaddress = None
                self.rttmonechoadminsourcemacaddress = None
                self.rttmonechoadminsourcempid = None
                self.rttmonechoadminendpointlistname = None
                self.rttmonechoadminssm = None
                self.rttmonechoadmincontrolretry = None
                self.rttmonechoadmincontroltimeout = None
                self.rttmonechoadminigmptreeinit = None
                self.rttmonechoadminenableburst = None
                self.rttmonechoadminaggburstcycles = None
                self.rttmonechoadminlossrationumframes = None
                self.rttmonechoadminavailnumframes = None
                self.rttmonechoadmintstampoptimization = None
                self._segment_path = lambda: "rttMonEchoAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonEchoAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonEchoAdminTable.RttMonEchoAdminEntry, ['rttmonctrladminindex', 'rttmonechoadminprotocol', 'rttmonechoadmintargetaddress', 'rttmonechoadminpktdatarequestsize', 'rttmonechoadminpktdataresponsesize', 'rttmonechoadmintargetport', 'rttmonechoadminsourceaddress', 'rttmonechoadminsourceport', 'rttmonechoadmincontrolenable', 'rttmonechoadmintos', 'rttmonechoadminlsrenable', 'rttmonechoadmintargetaddressstring', 'rttmonechoadminnameserver', 'rttmonechoadminoperation', 'rttmonechoadminhttpversion', 'rttmonechoadminurl', 'rttmonechoadmincache', 'rttmonechoadmininterval', 'rttmonechoadminnumpackets', 'rttmonechoadminproxy', 'rttmonechoadminstring1', 'rttmonechoadminstring2', 'rttmonechoadminstring3', 'rttmonechoadminstring4', 'rttmonechoadminstring5', 'rttmonechoadminmode', 'rttmonechoadminvrfname', 'rttmonechoadmincodectype', 'rttmonechoadmincodecinterval', 'rttmonechoadmincodecpayload', 'rttmonechoadmincodecnumpackets', 'rttmonechoadminicpifadvfactor', 'rttmonechoadminlspfectype', 'rttmonechoadminlspselector', 'rttmonechoadminlspreplymode', 'rttmonechoadminlspttl', 'rttmonechoadminlspexp', 'rttmonechoadminprecision', 'rttmonechoadminprobepakpriority', 'rttmonechoadminowntpsynctolabs', 'rttmonechoadminowntpsynctolpct', 'rttmonechoadminowntpsynctoltype', 'rttmonechoadmincallednumber', 'rttmonechoadmindetectpoint', 'rttmonechoadmingkregistration', 'rttmonechoadminsourcevoiceport', 'rttmonechoadmincallduration', 'rttmonechoadminlspreplydscp', 'rttmonechoadminlspnullshim', 'rttmonechoadmintargetmpid', 'rttmonechoadmintargetdomainname', 'rttmonechoadmintargetvlan', 'rttmonechoadminethernetcos', 'rttmonechoadminlspvccvid', 'rttmonechoadmintargetevc', 'rttmonechoadmintargetmepport', 'rttmonechoadminvideotrafficprofile', 'rttmonechoadmindscp', 'rttmonechoadminreservedsp', 'rttmonechoadmininputinterface', 'rttmonechoadminemulatesourceaddress', 'rttmonechoadminemulatesourceport', 'rttmonechoadminemulatetargetaddress', 'rttmonechoadminemulatetargetport', 'rttmonechoadmintargetmacaddress', 'rttmonechoadminsourcemacaddress', 'rttmonechoadminsourcempid', 'rttmonechoadminendpointlistname', 'rttmonechoadminssm', 'rttmonechoadmincontrolretry', 'rttmonechoadmincontroltimeout', 'rttmonechoadminigmptreeinit', 'rttmonechoadminenableburst', 'rttmonechoadminaggburstcycles', 'rttmonechoadminlossrationumframes', 'rttmonechoadminavailnumframes', 'rttmonechoadmintstampoptimization'], name, value)

            class RttMonEchoAdminLSPFECType(Enum):
                """
                RttMonEchoAdminLSPFECType (Enum Class)

                The type of the target FEC for the RTT 'echo' and 'pathEcho'

                operations based on 'mplsLspPingAppl' RttMonProtocol.

                ldpIpv4Prefix   \- LDP IPv4 prefix.

                .. data:: ldpIpv4Prefix = 1

                """

                ldpIpv4Prefix = Enum.YLeaf(1, "ldpIpv4Prefix")


            class RttMonEchoAdminOWNTPSyncTolType(Enum):
                """
                RttMonEchoAdminOWNTPSyncTolType (Enum Class)

                This object specifies whether the value in specified for oneway

                NTP sync tolerance is absolute value or percent value

                .. data:: percent = 1

                .. data:: absolute = 2

                """

                percent = Enum.YLeaf(1, "percent")

                absolute = Enum.YLeaf(2, "absolute")


            class RttMonEchoAdminPrecision(Enum):
                """
                RttMonEchoAdminPrecision (Enum Class)

                This object specifies the accuracy of statistics that

                needs to be calculated

                milliseconds \- The accuracy of stats will be of milliseconds

                microseconds \- The accuracy of stats will be in microseconds.

                This value can be set only for jitter operation

                .. data:: milliseconds = 1

                .. data:: microseconds = 2

                """

                milliseconds = Enum.YLeaf(1, "milliseconds")

                microseconds = Enum.YLeaf(2, "microseconds")


            class RttMonEchoAdminProbePakPriority(Enum):
                """
                RttMonEchoAdminProbePakPriority (Enum Class)

                This object specifies the priority that will be assigned

                to probe packet.  This value can be set only for jitter 

                operation

                .. data:: normal = 1

                .. data:: high = 2

                """

                normal = Enum.YLeaf(1, "normal")

                high = Enum.YLeaf(2, "high")


            class RttMonEchoAdminReserveDsp(Enum):
                """
                RttMonEchoAdminReserveDsp (Enum Class)

                This object represents the video traffic generation source.

                be \: best effort using DSP but without reservation

                gs \: guaranteed service using DSP with reservation

                na \: not applicable for not using DSP

                .. data:: be = 1

                .. data:: gs = 2

                .. data:: na = 3

                """

                be = Enum.YLeaf(1, "be")

                gs = Enum.YLeaf(2, "gs")

                na = Enum.YLeaf(3, "na")





    class RttMonFileIOAdminTable(Entity):
        """
        A table of Round Trip Time (RTT) monitoring 'fileIO'
        specific definitions.
        
        When the RttMonRttType is not 'fileIO' this table is
        not valid.
        
        This table is controlled via the 
        rttMonCtrlAdminTable.  Entries in this table are
        created via the rttMonCtrlAdminStatus object.
        
        .. attribute:: rttmonfileioadminentry
        
        	A list of objects that define specific configuration for 'fileIO' RttMonRttType conceptual Rtt control rows
        	**type**\: list of  		 :py:class:`RttMonFileIOAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonFileIOAdminTable, self).__init__()

            self.yang_name = "rttMonFileIOAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonFileIOAdminEntry", ("rttmonfileioadminentry", CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonfileioadminentry = YList(self)
            self._segment_path = lambda: "rttMonFileIOAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonFileIOAdminTable, [], name, value)


        class RttMonFileIOAdminEntry(Entity):
            """
            A list of objects that define specific configuration for
            'fileIO' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonfileioadminfilepath
            
            	The fully qualified file path that will be the target of the RTT operation.  This value must match one of the rttMonApplPreConfigedName entries
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminsize
            
            	The size of the file to write/read from the File Server
            	**type**\:  :py:class:`RttMonFileIOAdminSize <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry.RttMonFileIOAdminSize>`
            
            	**config**\: False
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminaction
            
            	The File I/O action to be performed
            	**type**\:  :py:class:`RttMonFileIOAdminAction <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry.RttMonFileIOAdminAction>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry, self).__init__()

                self.yang_name = "rttMonFileIOAdminEntry"
                self.yang_parent_name = "rttMonFileIOAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonfileioadminfilepath', (YLeaf(YType.str, 'rttMonFileIOAdminFilePath'), ['str'])),
                    ('rttmonfileioadminsize', (YLeaf(YType.enumeration, 'rttMonFileIOAdminSize'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonFileIOAdminTable.RttMonFileIOAdminEntry.RttMonFileIOAdminSize')])),
                    ('rttmonfileioadminaction', (YLeaf(YType.enumeration, 'rttMonFileIOAdminAction'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonFileIOAdminTable.RttMonFileIOAdminEntry.RttMonFileIOAdminAction')])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonfileioadminfilepath = None
                self.rttmonfileioadminsize = None
                self.rttmonfileioadminaction = None
                self._segment_path = lambda: "rttMonFileIOAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonFileIOAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonFileIOAdminTable.RttMonFileIOAdminEntry, ['rttmonctrladminindex', 'rttmonfileioadminfilepath', 'rttmonfileioadminsize', 'rttmonfileioadminaction'], name, value)

            class RttMonFileIOAdminAction(Enum):
                """
                RttMonFileIOAdminAction (Enum Class)

                The File I/O action to be performed.

                .. data:: write = 1

                .. data:: read = 2

                .. data:: writeRead = 3

                """

                write = Enum.YLeaf(1, "write")

                read = Enum.YLeaf(2, "read")

                writeRead = Enum.YLeaf(3, "writeRead")


            class RttMonFileIOAdminSize(Enum):
                """
                RttMonFileIOAdminSize (Enum Class)

                The size of the file to write/read from the File

                Server.

                .. data:: n256 = 1

                .. data:: n1k = 2

                .. data:: n64k = 3

                .. data:: n128k = 4

                .. data:: n256k = 5

                """

                n256 = Enum.YLeaf(1, "n256")

                n1k = Enum.YLeaf(2, "n1k")

                n64k = Enum.YLeaf(3, "n64k")

                n128k = Enum.YLeaf(4, "n128k")

                n256k = Enum.YLeaf(5, "n256k")





    class RttMonScriptAdminTable(Entity):
        """
        A table of Round Trip Time (RTT) monitoring 'script'
        specific definitions.
        
        When the RttMonRttType is not 'script' this table is
        not valid.
        
        This table is controlled via the
        rttMonCtrlAdminTable.  Entries in this table are
        created via the rttMonCtrlAdminStatus object.
        
        .. attribute:: rttmonscriptadminentry
        
        	A list of objects that define specific configuration for 'script' RttMonRttType conceptual Rtt control rows
        	**type**\: list of  		 :py:class:`RttMonScriptAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonScriptAdminTable.RttMonScriptAdminEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonScriptAdminTable, self).__init__()

            self.yang_name = "rttMonScriptAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonScriptAdminEntry", ("rttmonscriptadminentry", CISCORTTMONMIB.RttMonScriptAdminTable.RttMonScriptAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonscriptadminentry = YList(self)
            self._segment_path = lambda: "rttMonScriptAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonScriptAdminTable, [], name, value)


        class RttMonScriptAdminEntry(Entity):
            """
            A list of objects that define specific configuration for
            'script' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonscriptadminname
            
            	This will be the Name of the Script that will be used to generate RTT operations.    This object must match one of the  rttMonApplPreConfigedName entries
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: rttmonscriptadmincmdlineparams
            
            	This will be the actual command line parameters passed to the rttMonScriptAdminName when being executed
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonScriptAdminTable.RttMonScriptAdminEntry, self).__init__()

                self.yang_name = "rttMonScriptAdminEntry"
                self.yang_parent_name = "rttMonScriptAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonscriptadminname', (YLeaf(YType.str, 'rttMonScriptAdminName'), ['str'])),
                    ('rttmonscriptadmincmdlineparams', (YLeaf(YType.str, 'rttMonScriptAdminCmdLineParams'), ['str'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonscriptadminname = None
                self.rttmonscriptadmincmdlineparams = None
                self._segment_path = lambda: "rttMonScriptAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonScriptAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonScriptAdminTable.RttMonScriptAdminEntry, ['rttmonctrladminindex', 'rttmonscriptadminname', 'rttmonscriptadmincmdlineparams'], name, value)




    class RttMonReactTriggerAdminTable(Entity):
        """
        A table of which contains the list of conceptual RTT
        control rows that will start to collect data when a 
        reaction condition is violated and when 
        rttMonReactAdminActionType is set to one of the 
        following\:
          \-  triggerOnly
          \-  trapAndTrigger
          \-  nmvtAndTrigger
          \-  trapNmvtAndTrigger
        or when a reaction condition is violated and when any of the
        row in rttMonReactTable has rttMonReactActionType as one of
        the following\:
          \- triggerOnly
          \- trapAndTrigger
        
        The goal of this table is to define one or more 
        additional conceptual RTT control rows that will become
        active and start to collect additional history and
        statistics (depending on the rows configuration values),
        when a problem has been detected.
        
        If the conceptual RTT control row is undefined, and a 
        trigger occurs, no action will take place.  
        
        If the conceptual RTT control row is scheduled to start 
        at a later time, triggering that row will have no effect.
        
        If the conceptual RTT control row is currently active, 
        triggering that row will have no effect on that row, but 
        the rttMonReactTriggerOperState object will transition to 
        'active'.
        
        An entry in this table can only be triggered when
        it is not currently in a triggered state.  The
        object rttMonReactTriggerOperState will 
        reflect the state of each entry in this table.
        
        .. attribute:: rttmonreacttriggeradminentry
        
        	A list of objects that will be triggered when a reaction condition is violated
        	**type**\: list of  		 :py:class:`RttMonReactTriggerAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonReactTriggerAdminTable, self).__init__()

            self.yang_name = "rttMonReactTriggerAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonReactTriggerAdminEntry", ("rttmonreacttriggeradminentry", CISCORTTMONMIB.RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonreacttriggeradminentry = YList(self)
            self._segment_path = lambda: "rttMonReactTriggerAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonReactTriggerAdminTable, [], name, value)


        class RttMonReactTriggerAdminEntry(Entity):
            """
            A list of objects that will be triggered when
            a reaction condition is violated.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonreacttriggeradminrttmonctrladminindex  (key)
            
            	This object points to a single conceptual Rtt control row.  If this row does not exist and this value is  triggered no action will result.  The conceptual Rtt control row will be triggered for the  rttMonCtrlOperRttLife length.  If this conceptual Rtt control row is already active, rttMonCtrlOperRttLife will not be updated, and its life will continue as previously  defined
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonreacttriggeradminstatus
            
            	This object is used to create Trigger entries
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rttmonreacttriggeroperstate
            
            	This object takes on the value active when its associated entry in the  rttMonReactTriggerAdminTable has been triggered.  When the associated entry in the rttMonReactTriggerAdminTable is not under a trigger state, this object will be pending.  When this object is in the active state this entry can not be retriggered
            	**type**\:  :py:class:`RttMonReactTriggerOperState <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry.RttMonReactTriggerOperState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry, self).__init__()

                self.yang_name = "rttMonReactTriggerAdminEntry"
                self.yang_parent_name = "rttMonReactTriggerAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonreacttriggeradminrttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonreacttriggeradminrttmonctrladminindex', (YLeaf(YType.int32, 'rttMonReactTriggerAdminRttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonreacttriggeradminstatus', (YLeaf(YType.enumeration, 'rttMonReactTriggerAdminStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rttmonreacttriggeroperstate', (YLeaf(YType.enumeration, 'rttMonReactTriggerOperState'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry.RttMonReactTriggerOperState')])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonreacttriggeradminrttmonctrladminindex = None
                self.rttmonreacttriggeradminstatus = None
                self.rttmonreacttriggeroperstate = None
                self._segment_path = lambda: "rttMonReactTriggerAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonReactTriggerAdminRttMonCtrlAdminIndex='" + str(self.rttmonreacttriggeradminrttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonReactTriggerAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonReactTriggerAdminTable.RttMonReactTriggerAdminEntry, ['rttmonctrladminindex', 'rttmonreacttriggeradminrttmonctrladminindex', 'rttmonreacttriggeradminstatus', 'rttmonreacttriggeroperstate'], name, value)

            class RttMonReactTriggerOperState(Enum):
                """
                RttMonReactTriggerOperState (Enum Class)

                This object takes on the value active

                when its associated entry in the 

                rttMonReactTriggerAdminTable has been

                triggered.

                When the associated entry in the

                rttMonReactTriggerAdminTable is not under

                a trigger state, this object will be

                pending.

                When this object is in the active state

                this entry can not be retriggered.

                .. data:: active = 1

                .. data:: pending = 2

                """

                active = Enum.YLeaf(1, "active")

                pending = Enum.YLeaf(2, "pending")





    class RttMonEchoPathAdminTable(Entity):
        """
        A table to store the hop addresses in a Loose Source Routing
        path. Response times are computed along the specified path
        using ping.
        
        This maximum table size is limited by the size of the 
        maximum number of hop addresses that can fit in an IP header,
        which is 8. The object rttMonEchoPathAdminEntry will reflect 
        this tables maximum number of entries.
        
        This table is coupled with rttMonCtrlAdminStatus.
        
        .. attribute:: rttmonechopathadminentry
        
        	A list of objects that define intermediate hop's IP Address.  This entry can be added only if the rttMonCtrlAdminRttType is 'echo'. The entry gets deleted when the corresponding RTR entry, which has an index of rttMonCtrlAdminIndex, is deleted
        	**type**\: list of  		 :py:class:`RttMonEchoPathAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonEchoPathAdminTable.RttMonEchoPathAdminEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonEchoPathAdminTable, self).__init__()

            self.yang_name = "rttMonEchoPathAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonEchoPathAdminEntry", ("rttmonechopathadminentry", CISCORTTMONMIB.RttMonEchoPathAdminTable.RttMonEchoPathAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmonechopathadminentry = YList(self)
            self._segment_path = lambda: "rttMonEchoPathAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonEchoPathAdminTable, [], name, value)


        class RttMonEchoPathAdminEntry(Entity):
            """
            A list of objects that define intermediate hop's IP Address.
            
            This entry can be added only if the rttMonCtrlAdminRttType is
            'echo'. The entry gets deleted when the corresponding RTR entry,
            which has an index of rttMonCtrlAdminIndex, is deleted.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonechopathadminhopindex  (key)
            
            	Uniquely identifies a row in the rttMonEchoPathAdminTable. This number represents the hop address number in a specific  ping path. All the indicies should start from 1 and must be  contiguous ie., entries should be  (say rttMonCtrlAdminIndex = 1)  1.1, 1.2, 1.3, they cannot be 1.1, 1.2, 1.4
            	**type**\: int
            
            	**range:** 1..8
            
            	**config**\: False
            
            .. attribute:: rttmonechopathadminhopaddress
            
            	A string which specifies the address of an intermediate hop's IP Address for a RTT 'echo' operation
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonEchoPathAdminTable.RttMonEchoPathAdminEntry, self).__init__()

                self.yang_name = "rttMonEchoPathAdminEntry"
                self.yang_parent_name = "rttMonEchoPathAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonechopathadminhopindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonechopathadminhopindex', (YLeaf(YType.int32, 'rttMonEchoPathAdminHopIndex'), ['int'])),
                    ('rttmonechopathadminhopaddress', (YLeaf(YType.str, 'rttMonEchoPathAdminHopAddress'), ['str'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonechopathadminhopindex = None
                self.rttmonechopathadminhopaddress = None
                self._segment_path = lambda: "rttMonEchoPathAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonEchoPathAdminHopIndex='" + str(self.rttmonechopathadminhopindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonEchoPathAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonEchoPathAdminTable.RttMonEchoPathAdminEntry, ['rttmonctrladminindex', 'rttmonechopathadminhopindex', 'rttmonechopathadminhopaddress'], name, value)




    class RttMonGrpScheduleAdminTable(Entity):
        """
        A table of Round Trip Time (RTT) monitoring group scheduling
        specific definitions.
        This table is used to create a conceptual group scheduling
        control row. The entries in this control row contain objects
        used to define group schedule configuration parameters.
        
        The objects of this table will be used to schedule a group of
        probes identified by the conceptual rows of the
        rttMonCtrlAdminTable.
        
        .. attribute:: rttmongrpscheduleadminentry
        
        	A list of objects that define a conceptual group scheduling control row
        	**type**\: list of  		 :py:class:`RttMonGrpScheduleAdminEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonGrpScheduleAdminTable.RttMonGrpScheduleAdminEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonGrpScheduleAdminTable, self).__init__()

            self.yang_name = "rttMonGrpScheduleAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonGrpScheduleAdminEntry", ("rttmongrpscheduleadminentry", CISCORTTMONMIB.RttMonGrpScheduleAdminTable.RttMonGrpScheduleAdminEntry))])
            self._leafs = OrderedDict()

            self.rttmongrpscheduleadminentry = YList(self)
            self._segment_path = lambda: "rttMonGrpScheduleAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonGrpScheduleAdminTable, [], name, value)


        class RttMonGrpScheduleAdminEntry(Entity):
            """
            A list of objects that define a conceptual group scheduling
            control row.
            
            .. attribute:: rttmongrpscheduleadminindex  (key)
            
            	Uniquely identifies a row in the rttMonGrpScheduleAdminTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMonGrpScheduleAdminStatus object. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmongrpscheduleadminprobes
            
            	A string which holds the different probes which are to be group scheduled. The probes can be specified in the following forms. (a) Individual ID's with comma separated as 23,45,34. (b) Range form including hyphens with multiple ranges being     separated by a comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25.  Any whitespace in the string is considered an error. Duplicates and overlapping ranges as an example 1,2,3,2\-10 are considered fine. For a single range like 1\-20 the upper value (in this example 20) must be greater than lower value (1), otherwise it's treated as an error. The agent will not normalize the list e.g., it will not change 1,2,1\-10 or even 1,2,3,4,5,6.. to 1\-10
            	**type**\: str
            
            	**length:** 0..200
            
            	**config**\: False
            
            .. attribute:: rttmongrpscheduleadminperiod
            
            	Specifies the time duration over which all the probes have to be scheduled
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfrequency
            
            	Specifies the duration between initiating each RTT operation for all the probes specified in the group.  The value of this object is only effective when both rttMonGrpScheduleAdminFreqMax and rttMonGrpScheduleAdminFreqMin  have zero values
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminlife
            
            	This object specifies the life of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminRttLife object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the probes listed in rttMonGrpScheduleAdminProbes,  will not decrement. And thus the life time of the probes will never end
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminageout
            
            	This object specifies the ageout value of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminConceptRowAgeout object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  When this value is set to zero, the probes listed in rttMonGrpScheduleAdminProbes, will never ageout
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminstatus
            
            	The status of the conceptual RTT group schedule control row.  In order for this object to become active, the following row objects must be defined\:  \- rttMonGrpScheduleAdminProbes  \- rttMonGrpScheduleAdminPeriod All other objects can assume default values.  The conceptual RTT group schedule control row objects cannot be modified once this conceptual RTT group schedule control row has been created. Once this object is in 'active' status, it cannot be set to 'notInService'. When this object moves to 'active' state it will schedule the probes of the rttMonCtrlAdminTable which had been created using 'createAndWait'.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the probes of the rttMonCtrlAdminTable, which had been group scheduled by it earlier, before destroying the RTT group schedule control row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rttmongrpscheduleadminfreqmax
            
            	Specifies the max duration between initiating each RTT operation for all the probes specified in the group.  If this is 0 and rttMonGrpScheduleAdminFreqMin is also 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfreqmin
            
            	Specifies the min duration between initiating each RTT operation for all the probes specified in the group.  The value of this object cannot be greater than the value of rttMonGrpScheduleAdminFreqMax.  If this is 0 and rttMonGrpScheduleAdminFreqMax is 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminstarttime
            
            	This is the time in seconds after which the member probes of this group specified in rttMonGrpScheduleAdminProbes will transition to active state
            	**type**\: int
            
            	**range:** 0..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminadd
            
            	Addition of members to an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are added to the existing group
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmongrpscheduleadmindelete
            
            	Removal of members from an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are removed from the existing group
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmongrpscheduleadminreset
            
            	When this is set to true then all members of this group will be stopped and rescheduled using the previously set values of this group
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonGrpScheduleAdminTable.RttMonGrpScheduleAdminEntry, self).__init__()

                self.yang_name = "rttMonGrpScheduleAdminEntry"
                self.yang_parent_name = "rttMonGrpScheduleAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmongrpscheduleadminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmongrpscheduleadminindex', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminIndex'), ['int'])),
                    ('rttmongrpscheduleadminprobes', (YLeaf(YType.str, 'rttMonGrpScheduleAdminProbes'), ['str'])),
                    ('rttmongrpscheduleadminperiod', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminPeriod'), ['int'])),
                    ('rttmongrpscheduleadminfrequency', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminFrequency'), ['int'])),
                    ('rttmongrpscheduleadminlife', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminLife'), ['int'])),
                    ('rttmongrpscheduleadminageout', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminAgeout'), ['int'])),
                    ('rttmongrpscheduleadminstatus', (YLeaf(YType.enumeration, 'rttMonGrpScheduleAdminStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rttmongrpscheduleadminfreqmax', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminFreqMax'), ['int'])),
                    ('rttmongrpscheduleadminfreqmin', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminFreqMin'), ['int'])),
                    ('rttmongrpscheduleadminstarttime', (YLeaf(YType.int32, 'rttMonGrpScheduleAdminStartTime'), ['int'])),
                    ('rttmongrpscheduleadminadd', (YLeaf(YType.boolean, 'rttMonGrpScheduleAdminAdd'), ['bool'])),
                    ('rttmongrpscheduleadmindelete', (YLeaf(YType.boolean, 'rttMonGrpScheduleAdminDelete'), ['bool'])),
                    ('rttmongrpscheduleadminreset', (YLeaf(YType.boolean, 'rttMonGrpScheduleAdminReset'), ['bool'])),
                ])
                self.rttmongrpscheduleadminindex = None
                self.rttmongrpscheduleadminprobes = None
                self.rttmongrpscheduleadminperiod = None
                self.rttmongrpscheduleadminfrequency = None
                self.rttmongrpscheduleadminlife = None
                self.rttmongrpscheduleadminageout = None
                self.rttmongrpscheduleadminstatus = None
                self.rttmongrpscheduleadminfreqmax = None
                self.rttmongrpscheduleadminfreqmin = None
                self.rttmongrpscheduleadminstarttime = None
                self.rttmongrpscheduleadminadd = None
                self.rttmongrpscheduleadmindelete = None
                self.rttmongrpscheduleadminreset = None
                self._segment_path = lambda: "rttMonGrpScheduleAdminEntry" + "[rttMonGrpScheduleAdminIndex='" + str(self.rttmongrpscheduleadminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonGrpScheduleAdminTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonGrpScheduleAdminTable.RttMonGrpScheduleAdminEntry, ['rttmongrpscheduleadminindex', 'rttmongrpscheduleadminprobes', 'rttmongrpscheduleadminperiod', 'rttmongrpscheduleadminfrequency', 'rttmongrpscheduleadminlife', 'rttmongrpscheduleadminageout', 'rttmongrpscheduleadminstatus', 'rttmongrpscheduleadminfreqmax', 'rttmongrpscheduleadminfreqmin', 'rttmongrpscheduleadminstarttime', 'rttmongrpscheduleadminadd', 'rttmongrpscheduleadmindelete', 'rttmongrpscheduleadminreset'], name, value)




    class RttMplsVpnMonCtrlTable(Entity):
        """
        A table of Auto SAA L3 MPLS VPN definitions.
        
        The Auto SAA L3 MPLS VPN administration control is in multiple
        tables.
        
        This first table, is used to create a conceptual Auto SAA L3
        MPLS VPN control row.  The following tables contain objects
        which used in type specific configurations, scheduling and
        reaction configurations. All of these tables will create the
        same conceptual control row as this table using this table's
        index as their own index.
        
        In order to a row in this table to become active the following
        objects must be defined.
          rttMplsVpnMonCtrlRttType,
          rttMplsVpnMonCtrlVrfName and
          rttMplsVpnMonSchedulePeriod.
        
        .. attribute:: rttmplsvpnmonctrlentry
        
        	A base list of objects that define a conceptual Auto SAA L3 MPLS VPN control row
        	**type**\: list of  		 :py:class:`RttMplsVpnMonCtrlEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMplsVpnMonCtrlTable, self).__init__()

            self.yang_name = "rttMplsVpnMonCtrlTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMplsVpnMonCtrlEntry", ("rttmplsvpnmonctrlentry", CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry))])
            self._leafs = OrderedDict()

            self.rttmplsvpnmonctrlentry = YList(self)
            self._segment_path = lambda: "rttMplsVpnMonCtrlTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMplsVpnMonCtrlTable, [], name, value)


        class RttMplsVpnMonCtrlEntry(Entity):
            """
            A base list of objects that define a conceptual Auto SAA L3
            MPLS VPN control row.
            
            .. attribute:: rttmplsvpnmonctrlindex  (key)
            
            	Uniquely identifies a row in the rttMplsVpnMonCtrlTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMplsVpnMonCtrlStatus object.  If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlrtttype
            
            	The type of RTT operation to be performed for Auto SAA L3 MPLS VPN.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  This value must be set before setting any other parameter configuration of an Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`RttMplsVpnMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonRttType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlvrfname
            
            	This field is used to specify the VPN name for which the Auto SAA L3 MPLS VPN RTT operation will be used.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  The Auto SAA L3 MPLS VPN will find the PEs participating in this VPN and configure RTT operation corresponding to value specified in rttMplsVpnMonCtrlRttType.  If the VPN corresponds to the value configured for this object doesn't exist 'inconsistentValue' error will be returned.  The value 'saa\-vrf\-all' has a special meaning. When this object is set to 'saa\-vrf\-all', all the VPNs in the PE will be discovered and Auto SAA L3 MPLS VPN will configure RTT operations corresponding to all these PEs with the value specified in rttMplsVpnMonCtrlRttType as type for those operations.  So, the user should avoid using this string for a particular VPN name when using this feature in order to avoid ambiguity
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrltag
            
            	A string which is used by a managing application to identify the RTT target.  This string will be configured as rttMonCtrlAdminTag for all the operations configured by this Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminTag in RTT operation
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlthreshold
            
            	This object defines an administrative threshold limit.  This value will be configured as rttMonCtrlAdminThreshold for all the operations that will be configured by the current Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminThreshold
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrltimeout
            
            	Specifies the duration to wait for a RTT operation configured automatically by the Auto SAA L3 MPLS VPN to complete.   The value of this object cannot be set to a value which would specify a duration exceeding rttMplsVpnMonScheduleFrequency.  The usage of this value in Auto SAA L3 MPLS VPN is similar to rttMonCtrlAdminTimeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrlscaninterval
            
            	Specifies the frequency at which the automatic PE addition should take place if there is any for an Auto SAA L3 MPLS VPN.  New RTT operations corresponding to the new PEs discovered will be created and scheduled.  The default value for this object is 4 hours. The maximum value supported is 49 days
            	**type**\: int
            
            	**range:** 1..70560
            
            	**config**\: False
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmonctrldelscanfactor
            
            	Specifies the frequency at which the automatic PE deletion should take place.  This object specifies the number of times of rttMonMplslmCtrlScanInterval (rttMplsVpnMonCtrlDelScanFactor \* rttMplsVpnMonCtrlScanInterval) to wait before removing the PEs. This object doesn't directly specify the explicit value to wait before removing the PEs that were down.  If this object set 0 the entries will never removed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlexp
            
            	This object represents the EXP value that needs to be put as precedence bit of an IP header
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlrequestsize
            
            	This object represents the native payload size that needs to be put on the packet.  This value will be configured as rttMonEchoAdminPktDataRequestSize for all the RTT operations configured by the current Auto SAA L3 MPLS VPN.  The minimum request size for jitter probe is 16. The maximum for jitter probe is 1500. The default request size is 32 for jitter probe.  For echo and pathEcho default request size is 28. The minimum request size for echo and pathEcho is 28 bytes
            	**type**\: int
            
            	**range:** 0..16384
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: rttmplsvpnmonctrlverifydata
            
            	When set to true, the resulting data in each RTT operation created by the current Auto SAA L3 MPLS VPN is compared with the expected data. This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object of each RTT operation created by the current Auto SAA L3 MPLS VPN
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlstoragetype
            
            	The storage type of this conceptual row. When set to 'nonVolatile', this entry will be shown in 'show running' command and can be saved into Non\-volatile memory.  By Default the entry will not be saved into Non\-volatile memory.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlprobelist
            
            	This object holds the list of probes ID's that are created by the Auto SAA L3 MPLS VPN.  The probes will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrlstatus
            
            	The status of the conceptual Auto SAA L3 MPLS VPN control row.  In order for this object to become active rttMplsVpnMonCtrlRttType,  rttMplsVpnMonCtrlVrfName and  rttMplsVpnMonSchedulePeriod objects must be defined. All other objects can assume default values.  If the object is set to 'createAndGo' rttMplsVpnMonCtrlRttType, rttMplsVpnMonCtrlVrfName and rttMplsVpnMonSchedulePeriod needs to be set along with rttMplsVpnMonCtrlStatus.  If the object is set to 'createAndWait' rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName needs to be set along with rttMplsVpnMonCtrlStatus. rttMplsVpnMonSchedulePeriod needs to be specified before setting rttMplsVpnMonCtrlStatus to 'active'.  The following objects cannot be modified after creating the Auto SAA L3 MPLS VPN conceptual row.   \- rttMplsVpnMonCtrlRttType  \- rttMplsVpnMonCtrlVrfName  The following objects can be modified even after creating the Auto SAA L3 MPLS VPN conceptual row by setting this object to 'notInService'   \- All other writable objects in rttMplsVpnMonCtrlTable except    rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName.  \- Objects in the rttMplsVpnMonTypeTable.  \- Objects in the rttMplsVpnMonScheduleTable.  The following objects can be modified as needed without setting this object to 'notInService' even after creating the Auto SAA L3 MPLS VPN conceptual row.   \- Objects in rttMplsVpnMonReactTable.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop and destroy all the probes created by this Auto SAA L3 MPLS VPN before destroying Auto SAA L3 MPLS VPN control row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrllpd
            
            	When set to true, this implies that LPD (LSP Path Discovery) is enabled for this row.  The Auto SAA L3 MPLS VPN will find all the paths to each of the PE's and configure RTT operation with rttMonCtrlAdminRttType value as 'lspGroup'. The 'lspGroup' probe will walk through the list of set of information that uniquely identifies a path and send the LSP echo requests across them. All these LSP echo requests sent for 1st path, 2nd path etc. can be thought of as 'single probes' sent as a part of 'lspGroup'. These single probes will of type 'rttMplsVpnMonCtrlRttType'.  'lspGroup' probe is a superset of individual probes that will test multiple paths. For example Suppose there are 10 paths to the target. One 'lspGroup' probe will be created which will store all the information related to uniquely identify the 10 paths. When the 'lspGroup' probe will run it will sweep through the set of information for 1st path, 2nd path, 3rd path and so on till it has tested all the paths
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrllpdgrplist
            
            	This object holds the list of LPD Group IDs that are created for this Auto SAA L3 MPLS VPN row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  The LPD Groups will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonctrllpdcomptime
            
            	The completion time of the LSP Path Discovery for the entire set of PEs which are discovered for this Auto SAA.  This object will be applicable only when LSP Path Discovery is enabled for this row
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmontypeinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminInterval
            	**type**\: int
            
            	**range:** 1..60000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypenumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminNumPackets
            	**type**\: int
            
            	**range:** 1..60000
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypedestport
            
            	This object represents the target's port number to which the packets need to be sent.  This value will be configured as target port for all the operations that is going to be configured   The usage of this value is same as rttMonEchoAdminTargetPort in RTT operation. This object is applicable to jitter type.  If this object is not being set random port will be used as destination port
            	**type**\: int
            
            	**range:** 1..65536
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypesecfreqtype
            
            	This object specifies the reaction type for which the rttMplsVpnMonTypeSecFreqValue should be applied.  The Value 'timeout' will cause secondary frequency to be set for frequency on timeout condition.  The Value 'connectionLoss' will cause secondary frequency to be set for frequency on connectionloss condition.  The Value 'both' will cause secondary frequency to be set for frequency on either of timeout/connectionloss condition.  Notifications must be configured on corresponding reaction type in order to rttMplsVpnMonTypeSecFreqValue get effect.  When LSP Path Discovery is enabled for this row the following rttMplsVpnMonReactLpdNotifyType notifications must be configured in order to rttMplsVpnMonTypeSecFreqValue get effect.   \- 'lpdGroupStatus' or 'lpdAll'.  Since the Frequency of the operation changes the stats will be collected in new bucket.  If any of the reaction type (timeout/connectionLoss) occurred for an operation configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the frequency of the operation will be changed to rttMplsVpnMonTypeSecFreqValue.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss).   2) A notification is configured for the same reaction type   (timeout/connectionLoss).  When LSP Path Discovery is enabled for this row, if any of the reaction type (timeout/connectionLoss) occurred for 'single probes' configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the secondary frequency rttMplsVpnMonTypeSecFreqValue will be applied to the 'lspGroup' probe.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss/both).   2) rttMplsVpnMonReactLpdNotifyType object must be set to   value of 'lpdGroupStatus' or 'lpdAll'.  The frequency of the individual operations will be restored to original frequency once the trap is sent
            	**type**\:  :py:class:`RttMplsVpnMonTypeSecFreqType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonTypeSecFreqType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypesecfreqvalue
            
            	This object represents the value that needs to be applied to secondary frequency of individual RTT operations configured by Auto SAA L3 MPLS VPN.  Setting rttMplsVpnMonTypeSecFreqValue without setting rttMplsVpnMonTypeSecFreqType will not have any effect
            	**type**\: int
            
            	**range:** 1..604800
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelspselector
            
            	A string which specifies the address of the local host (127.X.X.X).  This object will be used as lsp\-selector in MPLS RTT operations configured by the Auto SAA L3 MPLS VPN.  When LSP Path Discovery is enabled for the row, this object will be used to indicate the base LSP selector value to be used in the LSP Path Discovery.  This value of this object is significant in MPLS load balancing scenario. This value will be used as one of the parameter in that load balancing
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho
            	**type**\:  :py:class:`RttMonLSPPingReplyMode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonLSPPingReplyMode>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelspttl
            
            	This object represents the TTL setting for MPLS echo request packets originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho.  For 'echo' the default TTL will be set to 255. For 'pathEcho' the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values will be used for 'echo' and 'pathEcho'
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\: int
            
            	**range:** 0..63 \| 255..None
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelpdmaxsessions
            
            	This object represents the number of concurrent path discovery requests that will be active at one time per MPLS VPN control row. This object is meant for reducing the time for discovery of all the paths to the target in a large customer network. However its value should be chosen such that it does not cause any performance impact.  Note\: If the customer network has low end routers in the Core it is recommended to keep this value low
            	**type**\: int
            
            	**range:** 1..15
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelpdsesstimeout
            
            	This object specifies the maximum allowed duration of a particular tree trace request.  If no response is received in configured time the request will be considered a failure
            	**type**\: int
            
            	**range:** 1..900
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmontypelpdechotimeout
            
            	This object specifies the timeout value for the LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechointerval
            
            	This object specifies the send interval between LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\: int
            
            	**range:** 0..3600000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechonullshim
            
            	This object specifies if the explicit\-null label is added to LSP echo requests which are sent while performing the LSP Path Discovery.  If set to TRUE all the probes configured as part of this control row will send the LSP echo requests with the explicit\-null label added
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmontypelpdscanperiod
            
            	This object specifies the scan time for the completion of LSP Path Discovery for all the PEs discovered for this control row. If the scan period is exceeded on completion of the LSP Path Discovery for all the PEs, the next discovery will start immediately else it will wait till expiry of scan period.  For example\: If the value is set to 30 minutes then on start of the LSP Path Discovery a timestamp will be taken say T1. At the end of the tree trace discovery one more timestamp will be taken again say T2. If (T2\-T1) is greater than 30, the next discovery will start immediately else next discovery  will wait for [30 \- (T2\-T1)].  Note\: If the object is set to a special value of '0', it will force immediate start of the next discovery on all neighbours without any delay
            	**type**\: int
            
            	**range:** 0..7200
            
            	**config**\: False
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmontypelpdstathours
            
            	The maximum number of hours of data to be kept per LPD group. The LPD group statistics will be kept in an hourly bucket. At the maximum there can be two buckets. The value of 'one' is not advisable because the group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value used in the rttMplsVpnLpdGroupStatsTable to uniquely identify this group is the rttMonStatsCaptureStartTimeIndex.  Note\: When this object is set to the value of '0' all rttMplsVpnLpdGroupStatsTable data capturing will be shut off
            	**type**\: int
            
            	**range:** 0..2
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonschedulerttstarttime
            
            	This is the time when this conceptual row will activate. rttMplsVpnMonSchedulePeriod object must be specified before setting this object.  This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will cause the activation of a conceptual Auto SAA L3 MPLS VPN row.  When an agent has the capability to determine date and time, the agent should store this object as DateAndTime. This allows the agent to be able to activate conceptual Auto SAA L3 MPLS VPN row at the intended time.  If this object has value as 1, this means start the operation now itself. Value of 0 puts the operation in pending state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonscheduleperiod
            
            	Specifies the time duration over which all the probes created by the current Auto SAA L3 MPLS VPN have to be scheduled.  This object must be set first before setting rttMplsVpnMonScheduleRttStartTime
            	**type**\: int
            
            	**range:** 1..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonschedulefrequency
            
            	Specifies the duration between initiating each RTT operation configured by the Auto SAA L3 MPLS VPN.  This object cannot be set to a value which would be a shorter duration than rttMplsVpnMonCtrlTimeout.  The usage of this value in RTT operation is same as rttMonCtrlAdminFrequency
            	**type**\: int
            
            	**range:** 1..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonreactconnectionenable
            
            	The value set for this will be applied as rttMonReactAdminConnectionEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'connectionLoss(8)'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreacttimeoutenable
            
            	The value set for this will be applied as rttMonReactAdminTimeoutEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'timeout(7)'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreactthresholdtype
            
            	The value corresponding to this object will be applied as rttMonReactAdminThresholdType for individual probes created by the Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactThresholdType for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`RttMplsVpnMonReactThresholdType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactThresholdType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreactthresholdcount
            
            	This object value will be applied as rttMonReactAdminThresholdCount for individual probes created by the Auto SAA L3 MPLS VPN.  This object value will be applied as rttMonReactThresholdCountX for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreactactiontype
            
            	The value corresponding to this object will be applied as rttMonReactAdminActionType of individual probes created by this Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactActionType of individual probes created by this Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`RttMplsVpnMonReactActionType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactActionType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreactlpdnotifytype
            
            	This object specifies the type of LPD notifications to be generated for the current Auto SAA L3 MPLS VPN control row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  There are two types of notifications supported for the LPD \- (a) rttMonLpdDiscoveryNotification \- This notification will     be sent on the failure of LSP Path Discovery to the     particular PE. Reversal of the failure will also result in     sending the notification. (b) rttMonLpdGrpStatusNotification \- Individual probes in an LPD     group will not generate notifications independently but will     be generating dependent on the state of the group. Any     individual probe can initiate the generation of a     notification, dependent on the state of the group.     Notifications are only generated if the failure/restoration     of an individual probe causes the state of the group to     change.  The Value 'none' will not cause any notifications to be sent.  The Value 'lpdPathDiscovery' will cause (a) to be sent.  The Value 'lpdGroupStatus' will cause (b) to be sent.  The Value 'lpdAll' will cause both (a) and (b) to sent depending on the failure conditions
            	**type**\:  :py:class:`RttMplsVpnMonReactLpdNotifyType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactLpdNotifyType>`
            
            	**config**\: False
            
            .. attribute:: rttmplsvpnmonreactlpdretrycount
            
            	This object value specifies the number of attempts to be performed before declaring the path as 'down'. Each 'single probe' which is part of 'lspGroup' probe will be retried these many times before marking it as 'down'.  This object will be applicable only when LSP Path Discovery is enabled for this row.    \- When rttMplsVpnMonTypeSecFreqType is not configured, the     failure count will be incremented at the next cycle of     'lspGroup' probe at interval's of     rttMplsVpnMonScheduleFrequency value.      For example\: Assume there are 10 paths discovered and on     the first run of the 'lspGroup' probe first two paths failed     and rest passed. On the second run all the probes will be      run again. The probes 1 and 2 will be retried till the     rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured.    \- When rttMplsVpnMonTypeSecFreqType value is anything other     than 'none', the retry will happen for the failed probes at     the rttMplsVpnMonTypeSecFreqValue and only the failed     probes will be retried.      For example\: Assume there are 10 paths discovered and on the     first run of the 'lspGroup' probe first two paths failed and     rest passed. The secondary frequency will be applied to the     failed probes. At secondary frequency interval the first two     probes will be run again. The probes 1 and 2 will be retried     till the rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            	**units**\: attempts
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry, self).__init__()

                self.yang_name = "rttMplsVpnMonCtrlEntry"
                self.yang_parent_name = "rttMplsVpnMonCtrlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmplsvpnmonctrlindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmplsvpnmonctrlindex', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlIndex'), ['int'])),
                    ('rttmplsvpnmonctrlrtttype', (YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlRttType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMplsVpnMonRttType', '')])),
                    ('rttmplsvpnmonctrlvrfname', (YLeaf(YType.str, 'rttMplsVpnMonCtrlVrfName'), ['str'])),
                    ('rttmplsvpnmonctrltag', (YLeaf(YType.str, 'rttMplsVpnMonCtrlTag'), ['str'])),
                    ('rttmplsvpnmonctrlthreshold', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlThreshold'), ['int'])),
                    ('rttmplsvpnmonctrltimeout', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlTimeout'), ['int'])),
                    ('rttmplsvpnmonctrlscaninterval', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlScanInterval'), ['int'])),
                    ('rttmplsvpnmonctrldelscanfactor', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlDelScanFactor'), ['int'])),
                    ('rttmplsvpnmonctrlexp', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlEXP'), ['int'])),
                    ('rttmplsvpnmonctrlrequestsize', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlRequestSize'), ['int'])),
                    ('rttmplsvpnmonctrlverifydata', (YLeaf(YType.boolean, 'rttMplsVpnMonCtrlVerifyData'), ['bool'])),
                    ('rttmplsvpnmonctrlstoragetype', (YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('rttmplsvpnmonctrlprobelist', (YLeaf(YType.str, 'rttMplsVpnMonCtrlProbeList'), ['str'])),
                    ('rttmplsvpnmonctrlstatus', (YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rttmplsvpnmonctrllpd', (YLeaf(YType.boolean, 'rttMplsVpnMonCtrlLpd'), ['bool'])),
                    ('rttmplsvpnmonctrllpdgrplist', (YLeaf(YType.str, 'rttMplsVpnMonCtrlLpdGrpList'), ['str'])),
                    ('rttmplsvpnmonctrllpdcomptime', (YLeaf(YType.int32, 'rttMplsVpnMonCtrlLpdCompTime'), ['int'])),
                    ('rttmplsvpnmontypeinterval', (YLeaf(YType.int32, 'rttMplsVpnMonTypeInterval'), ['int'])),
                    ('rttmplsvpnmontypenumpackets', (YLeaf(YType.int32, 'rttMplsVpnMonTypeNumPackets'), ['int'])),
                    ('rttmplsvpnmontypedestport', (YLeaf(YType.int32, 'rttMplsVpnMonTypeDestPort'), ['int'])),
                    ('rttmplsvpnmontypesecfreqtype', (YLeaf(YType.enumeration, 'rttMplsVpnMonTypeSecFreqType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonTypeSecFreqType')])),
                    ('rttmplsvpnmontypesecfreqvalue', (YLeaf(YType.int32, 'rttMplsVpnMonTypeSecFreqValue'), ['int'])),
                    ('rttmplsvpnmontypelspselector', (YLeaf(YType.str, 'rttMplsVpnMonTypeLspSelector'), ['str'])),
                    ('rttmplsvpnmontypelspreplymode', (YLeaf(YType.enumeration, 'rttMplsVpnMonTypeLSPReplyMode'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonLSPPingReplyMode', '')])),
                    ('rttmplsvpnmontypelspttl', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLSPTTL'), ['int'])),
                    ('rttmplsvpnmontypelspreplydscp', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLSPReplyDscp'), ['int'])),
                    ('rttmplsvpnmontypelpdmaxsessions', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdMaxSessions'), ['int'])),
                    ('rttmplsvpnmontypelpdsesstimeout', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdSessTimeout'), ['int'])),
                    ('rttmplsvpnmontypelpdechotimeout', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdEchoTimeout'), ['int'])),
                    ('rttmplsvpnmontypelpdechointerval', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdEchoInterval'), ['int'])),
                    ('rttmplsvpnmontypelpdechonullshim', (YLeaf(YType.boolean, 'rttMplsVpnMonTypeLpdEchoNullShim'), ['bool'])),
                    ('rttmplsvpnmontypelpdscanperiod', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdScanPeriod'), ['int'])),
                    ('rttmplsvpnmontypelpdstathours', (YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdStatHours'), ['int'])),
                    ('rttmplsvpnmonschedulerttstarttime', (YLeaf(YType.uint32, 'rttMplsVpnMonScheduleRttStartTime'), ['int'])),
                    ('rttmplsvpnmonscheduleperiod', (YLeaf(YType.int32, 'rttMplsVpnMonSchedulePeriod'), ['int'])),
                    ('rttmplsvpnmonschedulefrequency', (YLeaf(YType.int32, 'rttMplsVpnMonScheduleFrequency'), ['int'])),
                    ('rttmplsvpnmonreactconnectionenable', (YLeaf(YType.boolean, 'rttMplsVpnMonReactConnectionEnable'), ['bool'])),
                    ('rttmplsvpnmonreacttimeoutenable', (YLeaf(YType.boolean, 'rttMplsVpnMonReactTimeoutEnable'), ['bool'])),
                    ('rttmplsvpnmonreactthresholdtype', (YLeaf(YType.enumeration, 'rttMplsVpnMonReactThresholdType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactThresholdType')])),
                    ('rttmplsvpnmonreactthresholdcount', (YLeaf(YType.int32, 'rttMplsVpnMonReactThresholdCount'), ['int'])),
                    ('rttmplsvpnmonreactactiontype', (YLeaf(YType.enumeration, 'rttMplsVpnMonReactActionType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactActionType')])),
                    ('rttmplsvpnmonreactlpdnotifytype', (YLeaf(YType.enumeration, 'rttMplsVpnMonReactLpdNotifyType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry.RttMplsVpnMonReactLpdNotifyType')])),
                    ('rttmplsvpnmonreactlpdretrycount', (YLeaf(YType.int32, 'rttMplsVpnMonReactLpdRetryCount'), ['int'])),
                ])
                self.rttmplsvpnmonctrlindex = None
                self.rttmplsvpnmonctrlrtttype = None
                self.rttmplsvpnmonctrlvrfname = None
                self.rttmplsvpnmonctrltag = None
                self.rttmplsvpnmonctrlthreshold = None
                self.rttmplsvpnmonctrltimeout = None
                self.rttmplsvpnmonctrlscaninterval = None
                self.rttmplsvpnmonctrldelscanfactor = None
                self.rttmplsvpnmonctrlexp = None
                self.rttmplsvpnmonctrlrequestsize = None
                self.rttmplsvpnmonctrlverifydata = None
                self.rttmplsvpnmonctrlstoragetype = None
                self.rttmplsvpnmonctrlprobelist = None
                self.rttmplsvpnmonctrlstatus = None
                self.rttmplsvpnmonctrllpd = None
                self.rttmplsvpnmonctrllpdgrplist = None
                self.rttmplsvpnmonctrllpdcomptime = None
                self.rttmplsvpnmontypeinterval = None
                self.rttmplsvpnmontypenumpackets = None
                self.rttmplsvpnmontypedestport = None
                self.rttmplsvpnmontypesecfreqtype = None
                self.rttmplsvpnmontypesecfreqvalue = None
                self.rttmplsvpnmontypelspselector = None
                self.rttmplsvpnmontypelspreplymode = None
                self.rttmplsvpnmontypelspttl = None
                self.rttmplsvpnmontypelspreplydscp = None
                self.rttmplsvpnmontypelpdmaxsessions = None
                self.rttmplsvpnmontypelpdsesstimeout = None
                self.rttmplsvpnmontypelpdechotimeout = None
                self.rttmplsvpnmontypelpdechointerval = None
                self.rttmplsvpnmontypelpdechonullshim = None
                self.rttmplsvpnmontypelpdscanperiod = None
                self.rttmplsvpnmontypelpdstathours = None
                self.rttmplsvpnmonschedulerttstarttime = None
                self.rttmplsvpnmonscheduleperiod = None
                self.rttmplsvpnmonschedulefrequency = None
                self.rttmplsvpnmonreactconnectionenable = None
                self.rttmplsvpnmonreacttimeoutenable = None
                self.rttmplsvpnmonreactthresholdtype = None
                self.rttmplsvpnmonreactthresholdcount = None
                self.rttmplsvpnmonreactactiontype = None
                self.rttmplsvpnmonreactlpdnotifytype = None
                self.rttmplsvpnmonreactlpdretrycount = None
                self._segment_path = lambda: "rttMplsVpnMonCtrlEntry" + "[rttMplsVpnMonCtrlIndex='" + str(self.rttmplsvpnmonctrlindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMplsVpnMonCtrlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMplsVpnMonCtrlTable.RttMplsVpnMonCtrlEntry, ['rttmplsvpnmonctrlindex', 'rttmplsvpnmonctrlrtttype', 'rttmplsvpnmonctrlvrfname', 'rttmplsvpnmonctrltag', 'rttmplsvpnmonctrlthreshold', 'rttmplsvpnmonctrltimeout', 'rttmplsvpnmonctrlscaninterval', 'rttmplsvpnmonctrldelscanfactor', 'rttmplsvpnmonctrlexp', 'rttmplsvpnmonctrlrequestsize', 'rttmplsvpnmonctrlverifydata', 'rttmplsvpnmonctrlstoragetype', 'rttmplsvpnmonctrlprobelist', 'rttmplsvpnmonctrlstatus', 'rttmplsvpnmonctrllpd', 'rttmplsvpnmonctrllpdgrplist', 'rttmplsvpnmonctrllpdcomptime', 'rttmplsvpnmontypeinterval', 'rttmplsvpnmontypenumpackets', 'rttmplsvpnmontypedestport', 'rttmplsvpnmontypesecfreqtype', 'rttmplsvpnmontypesecfreqvalue', 'rttmplsvpnmontypelspselector', 'rttmplsvpnmontypelspreplymode', 'rttmplsvpnmontypelspttl', 'rttmplsvpnmontypelspreplydscp', 'rttmplsvpnmontypelpdmaxsessions', 'rttmplsvpnmontypelpdsesstimeout', 'rttmplsvpnmontypelpdechotimeout', 'rttmplsvpnmontypelpdechointerval', 'rttmplsvpnmontypelpdechonullshim', 'rttmplsvpnmontypelpdscanperiod', 'rttmplsvpnmontypelpdstathours', 'rttmplsvpnmonschedulerttstarttime', 'rttmplsvpnmonscheduleperiod', 'rttmplsvpnmonschedulefrequency', 'rttmplsvpnmonreactconnectionenable', 'rttmplsvpnmonreacttimeoutenable', 'rttmplsvpnmonreactthresholdtype', 'rttmplsvpnmonreactthresholdcount', 'rttmplsvpnmonreactactiontype', 'rttmplsvpnmonreactlpdnotifytype', 'rttmplsvpnmonreactlpdretrycount'], name, value)

            class RttMplsVpnMonReactActionType(Enum):
                """
                RttMplsVpnMonReactActionType (Enum Class)

                The value corresponding to this object will be applied as

                rttMonReactAdminActionType of individual probes created by

                this Auto SAA L3 MPLS VPN.

                The value corresponding to this object will be applied as

                rttMonReactActionType of individual probes created by

                this Auto SAA L3 MPLS VPN.

                .. data:: none = 1

                .. data:: trapOnly = 2

                """

                none = Enum.YLeaf(1, "none")

                trapOnly = Enum.YLeaf(2, "trapOnly")


            class RttMplsVpnMonReactLpdNotifyType(Enum):
                """
                RttMplsVpnMonReactLpdNotifyType (Enum Class)

                This object specifies the type of LPD notifications to be

                generated for the current Auto SAA L3 MPLS VPN control row.

                This object will be applicable only when LSP Path Discovery is

                enabled for this row.

                There are two types of notifications supported for the LPD \-

                (a) rttMonLpdDiscoveryNotification \- This notification will

                    be sent on the failure of LSP Path Discovery to the

                    particular PE. Reversal of the failure will also result in

                    sending the notification.

                (b) rttMonLpdGrpStatusNotification \- Individual probes in an LPD

                    group will not generate notifications independently but will

                    be generating dependent on the state of the group. Any

                    individual probe can initiate the generation of a

                    notification, dependent on the state of the group.

                    Notifications are only generated if the failure/restoration

                    of an individual probe causes the state of the group to

                    change.

                The Value 'none' will not cause any notifications to be sent.

                The Value 'lpdPathDiscovery' will cause (a) to be sent.

                The Value 'lpdGroupStatus' will cause (b) to be sent.

                The Value 'lpdAll' will cause both (a) and (b) to sent

                depending on the failure conditions.

                .. data:: none = 1

                .. data:: lpdPathDiscovery = 2

                .. data:: lpdGroupStatus = 3

                .. data:: lpdAll = 4

                """

                none = Enum.YLeaf(1, "none")

                lpdPathDiscovery = Enum.YLeaf(2, "lpdPathDiscovery")

                lpdGroupStatus = Enum.YLeaf(3, "lpdGroupStatus")

                lpdAll = Enum.YLeaf(4, "lpdAll")


            class RttMplsVpnMonReactThresholdType(Enum):
                """
                RttMplsVpnMonReactThresholdType (Enum Class)

                The value corresponding to this object will be applied as

                rttMonReactAdminThresholdType for individual probes created by

                the Auto SAA L3 MPLS VPN.

                The value corresponding to this object will be applied as

                rttMonReactThresholdType for individual probes created by

                the Auto SAA L3 MPLS VPN.

                .. data:: never = 1

                .. data:: immediate = 2

                .. data:: consecutive = 3

                """

                never = Enum.YLeaf(1, "never")

                immediate = Enum.YLeaf(2, "immediate")

                consecutive = Enum.YLeaf(3, "consecutive")


            class RttMplsVpnMonTypeSecFreqType(Enum):
                """
                RttMplsVpnMonTypeSecFreqType (Enum Class)

                This object specifies the reaction type for which the

                rttMplsVpnMonTypeSecFreqValue should be applied.

                The Value 'timeout' will cause secondary frequency to be set

                for frequency on timeout condition.

                The Value 'connectionLoss' will cause secondary frequency to

                be set for frequency on connectionloss condition.

                The Value 'both' will cause secondary frequency to be set for

                frequency on either of timeout/connectionloss condition.

                Notifications must be configured on corresponding reaction type

                in order to rttMplsVpnMonTypeSecFreqValue get effect.

                When LSP Path Discovery is enabled for this row the following

                rttMplsVpnMonReactLpdNotifyType notifications must be

                configured in order to rttMplsVpnMonTypeSecFreqValue get effect.

                  \- 'lpdGroupStatus' or 'lpdAll'.

                Since the Frequency of the operation changes the stats will be

                collected in new bucket.

                If any of the reaction type (timeout/connectionLoss) occurred

                for an operation configured by this Auto SAA L3 MPLS VPN and

                the following conditions are satisfied, the frequency of the

                operation will be changed to rttMplsVpnMonTypeSecFreqValue.

                  1) rttMplsVpnMonTypeSecFreqType is set for a reaction type

                  (timeout/connectionLoss).

                  2) A notification is configured for the same reaction type

                  (timeout/connectionLoss).

                When LSP Path Discovery is enabled for this row, if any of the

                reaction type (timeout/connectionLoss) occurred for 'single

                probes' configured by this Auto SAA L3 MPLS VPN and the

                following conditions are satisfied, the secondary frequency

                rttMplsVpnMonTypeSecFreqValue will be applied to the

                'lspGroup' probe.

                  1) rttMplsVpnMonTypeSecFreqType is set for a reaction type

                  (timeout/connectionLoss/both).

                  2) rttMplsVpnMonReactLpdNotifyType object must be set to

                  value of 'lpdGroupStatus' or 'lpdAll'.

                The frequency of the individual operations will be restored to

                original frequency once the trap is sent.

                .. data:: none = 1

                .. data:: timeout = 2

                .. data:: connectionLoss = 3

                .. data:: both = 4

                """

                none = Enum.YLeaf(1, "none")

                timeout = Enum.YLeaf(2, "timeout")

                connectionLoss = Enum.YLeaf(3, "connectionLoss")

                both = Enum.YLeaf(4, "both")





    class RttMonReactTable(Entity):
        """
        A table that contains the reaction configurations. Each
        conceptual row in rttMonReactTable corresponds to a reaction
        configured for the probe defined in rttMonCtrlAdminTable.
        
        For each reaction configured for a probe there is an entry in
        the table.
        
        Each Probe can have multiple reactions and hence there can be
        multiple rows for a particular probe.
        
        This table is coupled with rttMonCtrlAdminTable.
        
        .. attribute:: rttmonreactentry
        
        	A base list of objects that define a conceptual reaction configuration control row
        	**type**\: list of  		 :py:class:`RttMonReactEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonReactTable, self).__init__()

            self.yang_name = "rttMonReactTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonReactEntry", ("rttmonreactentry", CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry))])
            self._leafs = OrderedDict()

            self.rttmonreactentry = YList(self)
            self._segment_path = lambda: "rttMonReactTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonReactTable, [], name, value)


        class RttMonReactEntry(Entity):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonreactconfigindex  (key)
            
            	This object along with rttMonCtrlAdminIndex identifies a particular reaction\-configuration for a particular probe. This is a pseudo\-random number selected by the management station when creating a row via the rttMonReactStatus. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonreactvar
            
            	This object specifies the type of reaction configured for a probe.  The reaction types 'rtt', 'timeout', and 'connectionLoss'  can be configured for all probe types.  The reaction type 'verifyError' can be configured for all  probe types except RTP probe type.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' and 'maxOfNegativeDS' can be configured for UDP jitter  and ICMP jitter probe types only.  The reaction types 'mos' and 'icpif' can be configured  for UDP jitter and ICMP jitter probe types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter, and  RTP probe types only.  The reaction types 'iaJitterDS', 'frameLossDS', 'mosLQDS',  'mosCQDS', 'rFactorDS', 'iaJitterSD', 'rFactorSD', 'mosCQSD'  can be configured for RTP probe type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter probe  type only
            	**type**\:  :py:class:`RttMonReactVar <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonReactVar>`
            
            	**config**\: False
            
            .. attribute:: rttmonreactthresholdtype
            
            	This object specifies the conditions under which the notification ( trap ) is sent.  never       \- rttMonReactOccurred is never set  immediate   \- rttMonReactOccurred is set to 'true' when the               value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,               mos etc ) violates the threshold.               Conversely, rttMonReactOccurred is set to 'false'               when the parameter ( e.g rtt, jitterAvg,               packetLossSD, mos etc ) is below the threshold               limits.  consecutive \- rttMonReactOccurred is set to true when the value               of parameter for which reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold for configured consecutive               times.               Conversely, rttMonReactOccurred is set to false               when the value of parameter ( e.g rtt, jitterAvg               packetLossSD, mos etc ) is below the threshold               limits for the same number of consecutive               operations.  xOfy        \- rttMonReactOccurred is set to true when x               ( as specified by rttMonReactThresholdCountX )               out of the last y ( as specified by               rttMonReacthresholdCountY ) times the value of               parameter for which the reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold.               Conversely, it is set to false when x, out of the               last y times the value of parameter               ( e.g rtt, jitterAvg, packetLossSD, mos ) is               below the threshold limits.               NOTE\: When x > y, the probe will never                     generate a reaction.  average    \- rttMonReactOccurred is set to true when the              average ( rttMonReactThresholdCountX times )              value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,              mos etc ) violates the threshold condition.              Conversely, it is set to false when the              average value of parameter ( e.g rtt, jitterAvg,              packetLossSD, mos etc ) is below the threshold              limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:  :py:class:`RttMonReactThresholdType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry.RttMonReactThresholdType>`
            
            	**config**\: False
            
            .. attribute:: rttmonreactactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched ( reaction\-configuration ) conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated triggerOnly        \- all trigger actions defined for this                      entry are initiated trapAndTrigger     \- both a trap and all trigger actions                      are initiated A trigger action is defined via the rttMonReactTriggerAdminTable
            	**type**\:  :py:class:`RttMonReactActionType <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry.RttMonReactActionType>`
            
            	**config**\: False
            
            .. attribute:: rttmonreactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 400.    'mosCQDS' is 400.    'rFactorDS' is 80.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  rttMonReactThresholdRising will be 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonreactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the conditions specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 310.    'mosCQDS' is 310.    'rFactorDS' is 60.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.    'iaJitterSD' is 20.    'mosCQSD' is 310.    'rFactorSD' is 60.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of rttMonReactThresholdFalling will be 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonreactthresholdcountx
            
            	If rttMonReactThresholdType value is 'xOfy', this object defines the 'x' value.  If rttMonReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  rttMonReactOccurred as true.  If rttMonReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if rttMonReactThresholdType has value of 'never' and 'immediate'
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            .. attribute:: rttmonreactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if rttMonReactThresholdType is 'xOfy'.  For other values of rttMonReactThresholdType, this object is not applicable
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            .. attribute:: rttmonreactvalue
            
            	This object will be set when the configured threshold condition is violated as defined by rttMonReactThresholdType and holds the actual value that violated the configured threshold values.  This object is not valid for the following values of rttMonReactVar and It will be always 0\:   \- timeout   \- connectionLoss   \- verifyError
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonreactoccurred
            
            	This object is set to true when the configured threshold condition is violated as defined by rttMonReactThresholdType. It will be again set to 'false' if the condition reverses.  This object is set to true in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to true.  \- rttMonReactVar is set to connectionLoss and    rttMonCtrlOperConnectionLostOccurred set to true.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to true.  \- For all other values of rttMonReactVar, if the    corresponding value exceeds the configured    rttMonReactThresholdRising.   This object is set to false in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to false.  \- rttMonReactVar is set to connectionLoss and     rttMonCtrlOperConnectionLostOccurred set to false.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to false.  \- For all other values of rttMonReactVar, if the    corresponding value fall below the configured     rttMonReactThresholdFalling.  When the RttMonRttType is 'pathEcho' or 'pathJitter', this object is applied only to the  rttMonEchoAdminTargetAddress and not to intermediate hops to the Target
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonreactstatus
            
            	This objects indicates the status of the conceptual RTT Reaction Control Row.Only CreateAndGo and destroy  operations are permitted on the row.  When this object moves to active state, the conceptual row having the Reaction configuration for the probe is monitored and the notifications are generated when the threshold violation takes place.  In order for this object to become active rttMonReactVar must be defined. All other objects assume the default value.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration for the probes would exist. The reaction configuration for the probe is removed
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry, self).__init__()

                self.yang_name = "rttMonReactEntry"
                self.yang_parent_name = "rttMonReactTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonreactconfigindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonreactconfigindex', (YLeaf(YType.int32, 'rttMonReactConfigIndex'), ['int'])),
                    ('rttmonreactvar', (YLeaf(YType.enumeration, 'rttMonReactVar'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMonReactVar', '')])),
                    ('rttmonreactthresholdtype', (YLeaf(YType.enumeration, 'rttMonReactThresholdType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonReactTable.RttMonReactEntry.RttMonReactThresholdType')])),
                    ('rttmonreactactiontype', (YLeaf(YType.enumeration, 'rttMonReactActionType'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonReactTable.RttMonReactEntry.RttMonReactActionType')])),
                    ('rttmonreactthresholdrising', (YLeaf(YType.int32, 'rttMonReactThresholdRising'), ['int'])),
                    ('rttmonreactthresholdfalling', (YLeaf(YType.int32, 'rttMonReactThresholdFalling'), ['int'])),
                    ('rttmonreactthresholdcountx', (YLeaf(YType.int32, 'rttMonReactThresholdCountX'), ['int'])),
                    ('rttmonreactthresholdcounty', (YLeaf(YType.int32, 'rttMonReactThresholdCountY'), ['int'])),
                    ('rttmonreactvalue', (YLeaf(YType.int32, 'rttMonReactValue'), ['int'])),
                    ('rttmonreactoccurred', (YLeaf(YType.boolean, 'rttMonReactOccurred'), ['bool'])),
                    ('rttmonreactstatus', (YLeaf(YType.enumeration, 'rttMonReactStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonreactconfigindex = None
                self.rttmonreactvar = None
                self.rttmonreactthresholdtype = None
                self.rttmonreactactiontype = None
                self.rttmonreactthresholdrising = None
                self.rttmonreactthresholdfalling = None
                self.rttmonreactthresholdcountx = None
                self.rttmonreactthresholdcounty = None
                self.rttmonreactvalue = None
                self.rttmonreactoccurred = None
                self.rttmonreactstatus = None
                self._segment_path = lambda: "rttMonReactEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonReactConfigIndex='" + str(self.rttmonreactconfigindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonReactTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonReactTable.RttMonReactEntry, ['rttmonctrladminindex', 'rttmonreactconfigindex', 'rttmonreactvar', 'rttmonreactthresholdtype', 'rttmonreactactiontype', 'rttmonreactthresholdrising', 'rttmonreactthresholdfalling', 'rttmonreactthresholdcountx', 'rttmonreactthresholdcounty', 'rttmonreactvalue', 'rttmonreactoccurred', 'rttmonreactstatus'], name, value)

            class RttMonReactActionType(Enum):
                """
                RttMonReactActionType (Enum Class)

                Specifies what type(s), if any, of reaction(s) to

                generate if an operation violates one of the watched

                ( reaction\-configuration ) conditions\:

                none               \- no reaction is generated

                trapOnly           \- a trap is generated

                triggerOnly        \- all trigger actions defined for this

                                     entry are initiated

                trapAndTrigger     \- both a trap and all trigger actions

                                     are initiated

                A trigger action is defined via the

                rttMonReactTriggerAdminTable.

                .. data:: none = 1

                .. data:: trapOnly = 2

                .. data:: triggerOnly = 3

                .. data:: trapAndTrigger = 4

                """

                none = Enum.YLeaf(1, "none")

                trapOnly = Enum.YLeaf(2, "trapOnly")

                triggerOnly = Enum.YLeaf(3, "triggerOnly")

                trapAndTrigger = Enum.YLeaf(4, "trapAndTrigger")


            class RttMonReactThresholdType(Enum):
                """
                RttMonReactThresholdType (Enum Class)

                This object specifies the conditions under which

                the notification ( trap ) is sent.

                never       \- rttMonReactOccurred is never set

                immediate   \- rttMonReactOccurred is set to 'true' when the

                              value of parameter for which reaction is

                              configured ( e.g rtt, jitterAvg, packetLossSD,

                              mos etc ) violates the threshold.

                              Conversely, rttMonReactOccurred is set to 'false'

                              when the parameter ( e.g rtt, jitterAvg,

                              packetLossSD, mos etc ) is below the threshold

                              limits.

                consecutive \- rttMonReactOccurred is set to true when the value

                              of parameter for which reaction is configured

                              ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                              violates the threshold for configured consecutive

                              times.

                              Conversely, rttMonReactOccurred is set to false

                              when the value of parameter ( e.g rtt, jitterAvg

                              packetLossSD, mos etc ) is below the threshold

                              limits for the same number of consecutive

                              operations.

                xOfy        \- rttMonReactOccurred is set to true when x

                              ( as specified by rttMonReactThresholdCountX )

                              out of the last y ( as specified by

                              rttMonReacthresholdCountY ) times the value of

                              parameter for which the reaction is configured

                              ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                              violates the threshold.

                              Conversely, it is set to false when x, out of the

                              last y times the value of parameter

                              ( e.g rtt, jitterAvg, packetLossSD, mos ) is

                              below the threshold limits.

                              NOTE\: When x > y, the probe will never

                                    generate a reaction.

                average    \- rttMonReactOccurred is set to true when the

                             average ( rttMonReactThresholdCountX times )

                             value of parameter for which reaction is 

                             configured ( e.g rtt, jitterAvg, packetLossSD,

                             mos etc ) violates the threshold condition.

                             Conversely, it is set to false when the

                             average value of parameter ( e.g rtt, jitterAvg,

                             packetLossSD, mos etc ) is below the threshold

                             limits.

                If this value is changed by a management station,

                rttMonReactOccurred is set to false, but

                no reaction is generated if the prior value of

                rttMonReactOccurred was true.

                .. data:: never = 1

                .. data:: immediate = 2

                .. data:: consecutive = 3

                .. data:: xOfy = 4

                .. data:: average = 5

                """

                never = Enum.YLeaf(1, "never")

                immediate = Enum.YLeaf(2, "immediate")

                consecutive = Enum.YLeaf(3, "consecutive")

                xOfy = Enum.YLeaf(4, "xOfy")

                average = Enum.YLeaf(5, "average")





    class RttMonGeneratedOperTable(Entity):
        """
        This table contains information about the generated
        operation id as part of a parent IP SLA operation. The parent
        operation id is pseudo\-random number, selected by the management 
        station based on an operation started by the management 
        station,when creating a row via the rttMonCtrlAdminStatus
        object in the rttMonCtrlAdminTable table.
        
        .. attribute:: rttmongeneratedoperentry
        
        	An entry in the Generated Oper table corresponding to a child or generated operation as part of a parent IP SLA operation
        	**type**\: list of  		 :py:class:`RttMonGeneratedOperEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonGeneratedOperTable.RttMonGeneratedOperEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonGeneratedOperTable, self).__init__()

            self.yang_name = "rttMonGeneratedOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonGeneratedOperEntry", ("rttmongeneratedoperentry", CISCORTTMONMIB.RttMonGeneratedOperTable.RttMonGeneratedOperEntry))])
            self._leafs = OrderedDict()

            self.rttmongeneratedoperentry = YList(self)
            self._segment_path = lambda: "rttMonGeneratedOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonGeneratedOperTable, [], name, value)


        class RttMonGeneratedOperEntry(Entity):
            """
            An entry in the Generated Oper table corresponding to
            a child or generated operation as part of a parent
            IP SLA operation.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmongeneratedoperrespipaddrtype  (key)
            
            	The type of Internet address, IPv4 or IPv6, of a responder for an IP SLA operation
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: rttmongeneratedoperrespipaddr  (key)
            
            	The internet address of a responder for IP SLA operation. The type of this address is determined by the value of rttMonGeneratedOperRespIpAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: rttmongeneratedoperctrladminindex
            
            	This is a pseudo\-random number, auto\-generated based to identify a child operation based on a parent  operation started by the management station,when  creating a row via the rttMonCtrlAdminStatus object
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonGeneratedOperTable.RttMonGeneratedOperEntry, self).__init__()

                self.yang_name = "rttMonGeneratedOperEntry"
                self.yang_parent_name = "rttMonGeneratedOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmongeneratedoperrespipaddrtype','rttmongeneratedoperrespipaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmongeneratedoperrespipaddrtype', (YLeaf(YType.enumeration, 'rttMonGeneratedOperRespIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('rttmongeneratedoperrespipaddr', (YLeaf(YType.str, 'rttMonGeneratedOperRespIpAddr'), ['str'])),
                    ('rttmongeneratedoperctrladminindex', (YLeaf(YType.uint32, 'rttMonGeneratedOperCtrlAdminIndex'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmongeneratedoperrespipaddrtype = None
                self.rttmongeneratedoperrespipaddr = None
                self.rttmongeneratedoperctrladminindex = None
                self._segment_path = lambda: "rttMonGeneratedOperEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonGeneratedOperRespIpAddrType='" + str(self.rttmongeneratedoperrespipaddrtype) + "']" + "[rttMonGeneratedOperRespIpAddr='" + str(self.rttmongeneratedoperrespipaddr) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonGeneratedOperTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonGeneratedOperTable.RttMonGeneratedOperEntry, ['rttmonctrladminindex', 'rttmongeneratedoperrespipaddrtype', 'rttmongeneratedoperrespipaddr', 'rttmongeneratedoperctrladminindex'], name, value)




    class RttMonStatsCaptureTable(Entity):
        """
        The statistics capture database.
        
        The statistics capture table contains summarized 
        information of the results for a conceptual RTT control 
        row.  A rolling accumulated history of this information 
        is maintained in a series of hourly 'group(s)'.  Each 
        'group' contains a series of 'path(s)', each 'path' 
        contains a series of 'hop(s)', each 'hop' contains a 
        series of 'statistics distribution bucket(s)'.
        
        Each conceptual statistics row has a current hourly 
        group, into which RTT results are accumulated.  At the 
        end of each hour a new hourly group is created which 
        then becomes current.  The counters and accumulators in 
        the new group are initialized to zero.  The previous 
        group(s) is kept in the table until the table contains 
        rttMonStatisticsAdminNumHourGroups groups for the 
        conceptual statistics row;  at this point, the oldest 
        group is discarded and is replaced by the newly created 
        one.  The hourly group is uniquely identified by the 
        rttMonStatsCaptureStartTimeIndex object.
        
        If the activity for a conceptual RTT control row ceases 
        because the rttMonCtrlOperState object transitions to 
        'inactive', the corresponding current hourly group in 
        this table is 'frozen', and a new hourly group is 
        created when activity is resumed.
        
        If the activity for a conceptual RTT control row ceases 
        because the rttMonCtrlOperState object transitions to 
        'pending' this whole table will be cleared and reset to 
        its initial state.
        
        When the RttMonRttType is 'pathEcho', the path 
        exploration RTT requests' statistics will not be 
        accumulated in this table.
        
        NOTE\: When the RttMonRttType is 'pathEcho', a source to 
              target rttMonStatsCapturePathIndex path will be 
              created for each rttMonStatsCaptureStartTimeIndex 
              to hold all errors that occur when a specific path
              had not been found or connection has not be setup.
        
        Using this rttMonStatsCaptureTable, a managing 
        application can retrieve summarized data from accurately 
        measured periods, which is synchronized across multiple 
        conceptual RTT control rows.  With the new hourly group
        creation being performed on a 60 minute period, the 
        managing station has plenty of time to collect the data, 
        and need not be concerned with the vagaries of network 
        delays and lost PDU's when trying to get matching data.  
        Also, the managing station can spread the data gathering 
        over a longer period, which removes the need for a flood 
        of get requests in a short period which otherwise would 
        occur.
        
        .. attribute:: rttmonstatscaptureentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  The statistics capture table is a rollover table.  When rttMonStatsCaptureStartTimeIndex groups exceeds the  rttMonStatisticsAdminNumHourGroups value, the oldest  corresponding hourly group will be deleted and will be  replaced with the new rttMonStatsCaptureStartTimeIndex hourly group.    All other indices will fill to there maximum size.   The statistics capture table has five indices.  Each described as follows\:    \-  The first index correlates its entries to a       conceptual RTT control row via the        rttMonCtrlAdminIndex object.   \-  The second index is a rollover group and it        uniquely identifies a 60 minute group. (The        rttMonStatsCaptureStartTimeIndex object       is used to make this value unique.)   \-  When the RttMonRttType is 'pathEcho', the third        index uniquely identifies the paths in a        statistics period.  (The period is 60       minutes.)  A path will be created for each       unique path through the network.  Note\:  A       path that does not contain the target is       considered a different path than one which       uses the exact same path, but does contain the       target.  For all other values of RttMonRttType       this index will be one.   \-  When the RttMonRttType is 'pathEcho', the fourth        index uniquely identifies the hops in each path,        as grouped by the third index.  This index does        imply the order of the hops along the path to a        target.  For all other values of RttMonRttType       this index will be one.   \-  The fifth index uniquely creates a statistical       distribution bucket
        	**type**\: list of  		 :py:class:`RttMonStatsCaptureEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonStatsCaptureTable, self).__init__()

            self.yang_name = "rttMonStatsCaptureTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonStatsCaptureEntry", ("rttmonstatscaptureentry", CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry))])
            self._leafs = OrderedDict()

            self.rttmonstatscaptureentry = YList(self)
            self._segment_path = lambda: "rttMonStatsCaptureTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonStatsCaptureTable, [], name, value)


        class RttMonStatsCaptureEntry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            The statistics capture table is a rollover table.  When
            rttMonStatsCaptureStartTimeIndex groups exceeds the 
            rttMonStatisticsAdminNumHourGroups value, the oldest 
            corresponding hourly group will be deleted and will be 
            replaced with the new rttMonStatsCaptureStartTimeIndex
            hourly group.  
            
            All other indices will fill to there maximum size. 
            
            The statistics capture table has five indices.  Each
            described as follows\:
            
              \-  The first index correlates its entries to a
                  conceptual RTT control row via the 
                  rttMonCtrlAdminIndex object.
              \-  The second index is a rollover group and it 
                  uniquely identifies a 60 minute group. (The 
                  rttMonStatsCaptureStartTimeIndex object
                  is used to make this value unique.)
              \-  When the RttMonRttType is 'pathEcho', the third 
                  index uniquely identifies the paths in a 
                  statistics period.  (The period is 60
                  minutes.)  A path will be created for each
                  unique path through the network.  Note\:  A
                  path that does not contain the target is
                  considered a different path than one which
                  uses the exact same path, but does contain the
                  target.  For all other values of RttMonRttType
                  this index will be one.
              \-  When the RttMonRttType is 'pathEcho', the fourth 
                  index uniquely identifies the hops in each path, 
                  as grouped by the third index.  This index does 
                  imply the order of the hops along the path to a 
                  target.  For all other values of RttMonRttType
                  this index will be one.
              \-  The fifth index uniquely creates a statistical
                  distribution bucket.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	The time when this row was created.  This object is the second index of the  rttMonStatsCaptureTable Table.  The the number of rttMonStatsCaptureStartTimeIndex   groups exceeds the rttMonStatisticsAdminNumHourGroups value, the oldest rttMonStatsCaptureStartTimeIndex  group will be removed and replaced with the new entry.  When the RttMonRttType is 'pathEcho', this object also  uniquely defines a group of paths.  See the  rttMonStatsCaptureEntry object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturepathindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a path for a given value of  rttMonStatsCaptureStartTimeIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of  rttMonStatsCaptureStartTimeIndex, the agent assigns the first instance of a path a value of 1, then second  instance a value of 2, and so on.  The sequence keeps  incrementing until the number of paths equals  rttMonStatisticsAdminNumPaths value, then no new paths  are kept for the current rttMonStatsCaptureStartTimeIndex  group.  NOTE\: A source to target rttMonStatsCapturePathIndex       path will be created for each        rttMonStatsCaptureStartTimeIndex to hold all        errors that occur when a specific path or        connection has not be setup.  This value directly represents the path to a target. We can only support 128 paths
            	**type**\: int
            
            	**range:** 1..128
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturehopindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a hop for a given value of  rttMonStatsCapturePathIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of rttMonStatsCapturePathIndex, the agent assigns the first instance of a hop a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  hops equals rttMonStatisticsAdminNumHops value, then no new hops are kept for the current rttMonStatsCapturePathIndex.  This value directly represents a hop along the path to a target, thus we can only support 30 hops.  This value shows the order along the path to a target
            	**type**\: int
            
            	**range:** 1..30
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturedistindex  (key)
            
            	This object uniquely defines a statistical distribution bucket for a given value of rttMonStatsCaptureHopIndex.  For a particular value of rttMonStatsCaptureHopIndex, the agent assigns the first instance of a distribution a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  statistics distribution intervals equals  rttMonStatisticsAdminNumDistBuckets value, then all values that fall above the last interval will be placed into the last interval.  Each of these Statistics Distribution Buckets contain  the results of each completion as defined by  rttMonStatisticsAdminDistInterval object
            	**type**\: int
            
            	**range:** 1..20
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturecompletions
            
            	The number of RTT operations that have completed without an error and without timing out.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscaptureoverthresholds
            
            	The number of RTT operations successfully completed, but in excess of rttMonCtrlAdminThreshold.  This number is a subset of the accumulation of all  rttMonStatsCaptureCompletions.  The operation time  of these completed operations will be accumulated.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturesumcompletiontime
            
            	The accumulated completion time of RTT operations which complete successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturesumcompletiontime2low
            
            	The low order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  Low/High order is defined where the binary number will look as follows\: \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| High order 32 bits    \| Low order 32 bits     \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- For example the number 4294967296 would have all Low order bits as '0' and the rightmost High order bit will be 1 (zeros,1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturesumcompletiontime2high
            
            	The high order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  See the rttMonStatsCaptureSumCompletionTime2Low object for a definition of Low/High Order
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturecompletiontimemax
            
            	The maximum completion time of any RTT operation which completes successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturecompletiontimemin
            
            	The minimum completion time of any RTT operation which completes successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry, self).__init__()

                self.yang_name = "rttMonStatsCaptureEntry"
                self.yang_parent_name = "rttMonStatsCaptureTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex','rttmonstatscapturepathindex','rttmonstatscapturehopindex','rttmonstatscapturedistindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonstatscapturestarttimeindex', (YLeaf(YType.uint32, 'rttMonStatsCaptureStartTimeIndex'), ['int'])),
                    ('rttmonstatscapturepathindex', (YLeaf(YType.int32, 'rttMonStatsCapturePathIndex'), ['int'])),
                    ('rttmonstatscapturehopindex', (YLeaf(YType.int32, 'rttMonStatsCaptureHopIndex'), ['int'])),
                    ('rttmonstatscapturedistindex', (YLeaf(YType.int32, 'rttMonStatsCaptureDistIndex'), ['int'])),
                    ('rttmonstatscapturecompletions', (YLeaf(YType.int32, 'rttMonStatsCaptureCompletions'), ['int'])),
                    ('rttmonstatscaptureoverthresholds', (YLeaf(YType.int32, 'rttMonStatsCaptureOverThresholds'), ['int'])),
                    ('rttmonstatscapturesumcompletiontime', (YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime'), ['int'])),
                    ('rttmonstatscapturesumcompletiontime2low', (YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime2Low'), ['int'])),
                    ('rttmonstatscapturesumcompletiontime2high', (YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime2High'), ['int'])),
                    ('rttmonstatscapturecompletiontimemax', (YLeaf(YType.uint32, 'rttMonStatsCaptureCompletionTimeMax'), ['int'])),
                    ('rttmonstatscapturecompletiontimemin', (YLeaf(YType.uint32, 'rttMonStatsCaptureCompletionTimeMin'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonstatscapturestarttimeindex = None
                self.rttmonstatscapturepathindex = None
                self.rttmonstatscapturehopindex = None
                self.rttmonstatscapturedistindex = None
                self.rttmonstatscapturecompletions = None
                self.rttmonstatscaptureoverthresholds = None
                self.rttmonstatscapturesumcompletiontime = None
                self.rttmonstatscapturesumcompletiontime2low = None
                self.rttmonstatscapturesumcompletiontime2high = None
                self.rttmonstatscapturecompletiontimemax = None
                self.rttmonstatscapturecompletiontimemin = None
                self._segment_path = lambda: "rttMonStatsCaptureEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonStatsCaptureStartTimeIndex='" + str(self.rttmonstatscapturestarttimeindex) + "']" + "[rttMonStatsCapturePathIndex='" + str(self.rttmonstatscapturepathindex) + "']" + "[rttMonStatsCaptureHopIndex='" + str(self.rttmonstatscapturehopindex) + "']" + "[rttMonStatsCaptureDistIndex='" + str(self.rttmonstatscapturedistindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsCaptureTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatscapturepathindex', 'rttmonstatscapturehopindex', 'rttmonstatscapturedistindex', 'rttmonstatscapturecompletions', 'rttmonstatscaptureoverthresholds', 'rttmonstatscapturesumcompletiontime', 'rttmonstatscapturesumcompletiontime2low', 'rttmonstatscapturesumcompletiontime2high', 'rttmonstatscapturecompletiontimemax', 'rttmonstatscapturecompletiontimemin'], name, value)




    class RttMonStatsCollectTable(Entity):
        """
        The statistics collection database.
        
        This table has the exact same behavior as the
        rttMonStatsCaptureTable, except it does not keep
        statistical distribution information.
        
        For a complete table description see
        the rttMonStatsCaptureTable object.
        
        .. attribute:: rttmonstatscollectentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry has the exact same behavior as the  rttMonStatsCaptureEntry, except it does not keep statistical distribution information.  For a complete entry description see the rttMonStatsCaptureEntry object
        	**type**\: list of  		 :py:class:`RttMonStatsCollectEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCollectTable.RttMonStatsCollectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonStatsCollectTable, self).__init__()

            self.yang_name = "rttMonStatsCollectTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonStatsCollectEntry", ("rttmonstatscollectentry", CISCORTTMONMIB.RttMonStatsCollectTable.RttMonStatsCollectEntry))])
            self._leafs = OrderedDict()

            self.rttmonstatscollectentry = YList(self)
            self._segment_path = lambda: "rttMonStatsCollectTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonStatsCollectTable, [], name, value)


        class RttMonStatsCollectEntry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry has the exact same behavior as the 
            rttMonStatsCaptureEntry, except it does not keep
            statistical distribution information.
            
            For a complete entry description see
            the rttMonStatsCaptureEntry object.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturepathindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..128
            
            	**refers to**\:  :py:class:`rttmonstatscapturepathindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturehopindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..30
            
            	**refers to**\:  :py:class:`rttmonstatscapturehopindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectnumdisconnects
            
            	When the RttMonRttType is 'echo' or pathEcho', this object represents the number of times that the target or  hop along the path to a target became disconnected.  For all other values of RttMonRttType, this object will remain zero.  For connectionless protocols this has no meaning, and will consequently remain 0.  When rttMonEchoAdminProtocol is one of snaRUEcho, this is the number of times that an LU\-SSCP session was lost,  for snaLU0EchoAppl, snaLU2EchoAppl, snaLu62Echo, and for  snaLU62EchoAppl, this is the number of times that LU\-LU  session was lost.  Since this error does not indicate any information about the failure of an RTT operation, no response time  information for this instance will be recorded in the  appropriate objects.  If this error occurs and the rttMonStatsCapturePathIndex  cannot be determined, this error will be accumulated in  the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollecttimeouts
            
            	The number of occasions when a RTT operation was not completed before a timeout occurred, i.e. rttMonCtrlAdminTimeout was exceeded.  Since the RTT operation was never completed, the  completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions (in  any of the statistics distribution buckets).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectbusies
            
            	The number of occasions when a RTT operation could not be initiated because a previous RTT operation has not  been completed.  When the RttMonRttType is 'pathEcho' this can occur for both connection oriented protocols and connectionless protocols.  When the RttMonRttType is 'echo' this can only occur for connection oriented protocols such as SNA.   When the initiation of a new operation cannot be started, this object will be incremented and the operation will be omitted.  (The next operation will start at the next  Frequency).  Since, a RTT operation was never initiated,  the completion time of these operations is not  accumulated, nor do they increment  rttMonStatsCaptureCompletions.  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the source  to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectnoconnections
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is the number of occasions when a RTT operation could not be initiated because the connection to the target has not  been established.  For all other RttMonRttTypes this object will remain zero.  This cannot occur for connectionless protocols, but may occur for connection oriented protocols, such as SNA.  Since a RTT operation was never initiated, the completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions.   If this error occurs and the rttMonStatsCapturePathIndex cannot be determined, this error will be accumulated in the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectdrops
            
            	The number of occasions when a RTT operation could not be initiated because some necessary internal resource  (for example memory, or SNA subsystem) was not available, or the operation completion could not be recognized.  Since a RTT operation was never initiated or was not recognized, the completion time of these operations  are not accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected  Distribution Bucket).  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the  source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectsequenceerrors
            
            	When the RttMonRttType is 'echo' of 'pathEcho' this is the number of RTT operation completions received with  an unexpected sequence identifier.  For all other values of RttMonRttType this object will remain zero.  When this has occurred some of the possible reasons may be\:      \- a duplicate packet was received    \- a response was received after it had timed\-out    \- a corrupted packet was received and was not detected  The completion time of these operations are not  accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectverifyerrors
            
            	The number of RTT operation completions received with data that does not compare with the expected data.  The  completion time of these operations are not accumulated,  nor do they increment rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectaddress
            
            	This object only applies when the RttMonRttType is 'echo', 'pathEcho', 'dlsw', 'udpEcho', 'tcpConnect'.   For all other values of the RttMonRttType, this will be  null.   The object is a string which specifies the address of  the target for the this RTT operation.  This address will be the address of the hop along the  path to the rttMonEchoAdminTargetAddress address,  including rttMonEchoAdminTargetAddress address, or just  the rttMonEchoAdminTargetAddress address, when the  path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type  of RTT operation selected, as specified by the  rttMonEchoAdminProtocol object
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmoncontrolenableerrors
            
            	The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonControlEnableErrors object is superseded by rttMonStatsCollectCtrlEnErrors
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatsretrieveerrors
            
            	The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonStatsRetrieveErrors object is superseded by rttMonStatsCollectRetrieveErrors
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatscollectctrlenerrors
            
            	The object is same as rttMonControlEnableErrors, with corrected name for consistency.  The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatscollectretrieveerrors
            
            	The object is same as rttMonStatsRetrieveErrors, with corrected name for consistency.  The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonStatsCollectTable.RttMonStatsCollectEntry, self).__init__()

                self.yang_name = "rttMonStatsCollectEntry"
                self.yang_parent_name = "rttMonStatsCollectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex','rttmonstatscapturepathindex','rttmonstatscapturehopindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonstatscapturestarttimeindex', (YLeaf(YType.str, 'rttMonStatsCaptureStartTimeIndex'), ['int'])),
                    ('rttmonstatscapturepathindex', (YLeaf(YType.str, 'rttMonStatsCapturePathIndex'), ['int'])),
                    ('rttmonstatscapturehopindex', (YLeaf(YType.str, 'rttMonStatsCaptureHopIndex'), ['int'])),
                    ('rttmonstatscollectnumdisconnects', (YLeaf(YType.int32, 'rttMonStatsCollectNumDisconnects'), ['int'])),
                    ('rttmonstatscollecttimeouts', (YLeaf(YType.int32, 'rttMonStatsCollectTimeouts'), ['int'])),
                    ('rttmonstatscollectbusies', (YLeaf(YType.int32, 'rttMonStatsCollectBusies'), ['int'])),
                    ('rttmonstatscollectnoconnections', (YLeaf(YType.int32, 'rttMonStatsCollectNoConnections'), ['int'])),
                    ('rttmonstatscollectdrops', (YLeaf(YType.int32, 'rttMonStatsCollectDrops'), ['int'])),
                    ('rttmonstatscollectsequenceerrors', (YLeaf(YType.int32, 'rttMonStatsCollectSequenceErrors'), ['int'])),
                    ('rttmonstatscollectverifyerrors', (YLeaf(YType.int32, 'rttMonStatsCollectVerifyErrors'), ['int'])),
                    ('rttmonstatscollectaddress', (YLeaf(YType.str, 'rttMonStatsCollectAddress'), ['str'])),
                    ('rttmoncontrolenableerrors', (YLeaf(YType.int32, 'rttMonControlEnableErrors'), ['int'])),
                    ('rttmonstatsretrieveerrors', (YLeaf(YType.int32, 'rttMonStatsRetrieveErrors'), ['int'])),
                    ('rttmonstatscollectctrlenerrors', (YLeaf(YType.int32, 'rttMonStatsCollectCtrlEnErrors'), ['int'])),
                    ('rttmonstatscollectretrieveerrors', (YLeaf(YType.int32, 'rttMonStatsCollectRetrieveErrors'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonstatscapturestarttimeindex = None
                self.rttmonstatscapturepathindex = None
                self.rttmonstatscapturehopindex = None
                self.rttmonstatscollectnumdisconnects = None
                self.rttmonstatscollecttimeouts = None
                self.rttmonstatscollectbusies = None
                self.rttmonstatscollectnoconnections = None
                self.rttmonstatscollectdrops = None
                self.rttmonstatscollectsequenceerrors = None
                self.rttmonstatscollectverifyerrors = None
                self.rttmonstatscollectaddress = None
                self.rttmoncontrolenableerrors = None
                self.rttmonstatsretrieveerrors = None
                self.rttmonstatscollectctrlenerrors = None
                self.rttmonstatscollectretrieveerrors = None
                self._segment_path = lambda: "rttMonStatsCollectEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonStatsCaptureStartTimeIndex='" + str(self.rttmonstatscapturestarttimeindex) + "']" + "[rttMonStatsCapturePathIndex='" + str(self.rttmonstatscapturepathindex) + "']" + "[rttMonStatsCaptureHopIndex='" + str(self.rttmonstatscapturehopindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsCollectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonStatsCollectTable.RttMonStatsCollectEntry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatscapturepathindex', 'rttmonstatscapturehopindex', 'rttmonstatscollectnumdisconnects', 'rttmonstatscollecttimeouts', 'rttmonstatscollectbusies', 'rttmonstatscollectnoconnections', 'rttmonstatscollectdrops', 'rttmonstatscollectsequenceerrors', 'rttmonstatscollectverifyerrors', 'rttmonstatscollectaddress', 'rttmoncontrolenableerrors', 'rttmonstatsretrieveerrors', 'rttmonstatscollectctrlenerrors', 'rttmonstatscollectretrieveerrors'], name, value)




    class RttMonStatsTotalsTable(Entity):
        """
        The statistics totals database.
        
        This table has the exact same behavior as the
        rttMonStatsCaptureTable, except it only keeps
        60 minute group values.
        
        For a complete table description see
        the rttMonStatsCaptureTable object.
        
        .. attribute:: rttmonstatstotalsentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry has the exact same behavior as the  rttMonStatsCaptureEntry, except it only keeps 60 minute group values.  For a complete entry description see the rttMonStatsCaptureEntry object
        	**type**\: list of  		 :py:class:`RttMonStatsTotalsEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsTotalsTable.RttMonStatsTotalsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonStatsTotalsTable, self).__init__()

            self.yang_name = "rttMonStatsTotalsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonStatsTotalsEntry", ("rttmonstatstotalsentry", CISCORTTMONMIB.RttMonStatsTotalsTable.RttMonStatsTotalsEntry))])
            self._leafs = OrderedDict()

            self.rttmonstatstotalsentry = YList(self)
            self._segment_path = lambda: "rttMonStatsTotalsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonStatsTotalsTable, [], name, value)


        class RttMonStatsTotalsEntry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry has the exact same behavior as the 
            rttMonStatsCaptureEntry, except it only keeps
            60 minute group values.
            
            For a complete entry description see
            the rttMonStatsCaptureEntry object.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonStatsCaptureTable.RttMonStatsCaptureEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonstatstotalselapsedtime
            
            	The length of time since this conceptual statistics row was created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonstatstotalsinitiations
            
            	The number of RTT operations that have been initiated.  This number includes all RTT operations which succeed  or fail for whatever reason.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonStatsTotalsTable.RttMonStatsTotalsEntry, self).__init__()

                self.yang_name = "rttMonStatsTotalsEntry"
                self.yang_parent_name = "rttMonStatsTotalsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonstatscapturestarttimeindex', (YLeaf(YType.str, 'rttMonStatsCaptureStartTimeIndex'), ['int'])),
                    ('rttmonstatstotalselapsedtime', (YLeaf(YType.int32, 'rttMonStatsTotalsElapsedTime'), ['int'])),
                    ('rttmonstatstotalsinitiations', (YLeaf(YType.int32, 'rttMonStatsTotalsInitiations'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonstatscapturestarttimeindex = None
                self.rttmonstatstotalselapsedtime = None
                self.rttmonstatstotalsinitiations = None
                self._segment_path = lambda: "rttMonStatsTotalsEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonStatsCaptureStartTimeIndex='" + str(self.rttmonstatscapturestarttimeindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsTotalsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonStatsTotalsTable.RttMonStatsTotalsEntry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatstotalselapsedtime', 'rttmonstatstotalsinitiations'], name, value)




    class RttMonHTTPStatsTable(Entity):
        """
        The HTTP statistics collection database.
        
        The HTTP statistics table contains summarized information of
        the results for a conceptual RTT control row. A rolling
        accumulated history of this information is maintained in a 
        series of hourly 'group(s)'.
        
        The operation of this table is same as that of 
        rttMonStatsCaptureTable, except that this table can only 
        store a maximum of 2 hours of data.
        
        .. attribute:: rttmonhttpstatsentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry is created only if the rttMonCtrlAdminRttType  is http. The operation of this table is same as that of rttMonStatsCaptureTable
        	**type**\: list of  		 :py:class:`RttMonHTTPStatsEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonHTTPStatsTable.RttMonHTTPStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonHTTPStatsTable, self).__init__()

            self.yang_name = "rttMonHTTPStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonHTTPStatsEntry", ("rttmonhttpstatsentry", CISCORTTMONMIB.RttMonHTTPStatsTable.RttMonHTTPStatsEntry))])
            self._leafs = OrderedDict()

            self.rttmonhttpstatsentry = YList(self)
            self._segment_path = lambda: "rttMonHTTPStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonHTTPStatsTable, [], name, value)


        class RttMonHTTPStatsEntry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is http. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsstarttimeindex  (key)
            
            	This is the time when this row was created. This index uniquely identifies a HTTP Stats row in the  rttMonHTTPStatsTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatscompletions
            
            	The number of HTTP operations that have completed successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsoverthresholds
            
            	The number of HTTP operations that violate threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsrttsum
            
            	The sum of HTTP operations that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsrttsum2low
            
            	The sum of squares of the RTT's that are successfully measured (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsrttsum2high
            
            	The sum of squares of the RTT's that are successfully measured (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsrttmin
            
            	The minimum RTT taken to perform HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsrttmax
            
            	The maximum RTT taken to perform HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhttpstatsdnsrttsum
            
            	The sum of RTT taken to perform DNS query within the HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatstcpconnectrttsum
            
            	The sum of RTT taken to connect to the HTTP server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatstransactionrttsum
            
            	The sum of RTT taken to download the object specified by URL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsmessagebodyoctetssum
            
            	The sum of the size of the message body received as a response to the HTTP request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsdnsservertimeout
            
            	The number of requests that could not connect to the DNS Server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatstcpconnecttimeout
            
            	The number of requests that could not connect to the the HTTP Server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatstransactiontimeout
            
            	The number of requests that timed out during HTTP transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsdnsqueryerror
            
            	The number of requests that had DNS Query errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatshttperror
            
            	The number of requests that had HTTP errors while downloading the base page
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatserror
            
            	The number of occasions when a HTTP operation could not be initiated because an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhttpstatsbusies
            
            	The number of occasions when an HTTP operation could not be initiated because a previous HTTP operation has not been completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonHTTPStatsTable.RttMonHTTPStatsEntry, self).__init__()

                self.yang_name = "rttMonHTTPStatsEntry"
                self.yang_parent_name = "rttMonHTTPStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonhttpstatsstarttimeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonhttpstatsstarttimeindex', (YLeaf(YType.uint32, 'rttMonHTTPStatsStartTimeIndex'), ['int'])),
                    ('rttmonhttpstatscompletions', (YLeaf(YType.uint32, 'rttMonHTTPStatsCompletions'), ['int'])),
                    ('rttmonhttpstatsoverthresholds', (YLeaf(YType.uint32, 'rttMonHTTPStatsOverThresholds'), ['int'])),
                    ('rttmonhttpstatsrttsum', (YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum'), ['int'])),
                    ('rttmonhttpstatsrttsum2low', (YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum2Low'), ['int'])),
                    ('rttmonhttpstatsrttsum2high', (YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum2High'), ['int'])),
                    ('rttmonhttpstatsrttmin', (YLeaf(YType.uint32, 'rttMonHTTPStatsRTTMin'), ['int'])),
                    ('rttmonhttpstatsrttmax', (YLeaf(YType.uint32, 'rttMonHTTPStatsRTTMax'), ['int'])),
                    ('rttmonhttpstatsdnsrttsum', (YLeaf(YType.uint32, 'rttMonHTTPStatsDNSRTTSum'), ['int'])),
                    ('rttmonhttpstatstcpconnectrttsum', (YLeaf(YType.uint32, 'rttMonHTTPStatsTCPConnectRTTSum'), ['int'])),
                    ('rttmonhttpstatstransactionrttsum', (YLeaf(YType.uint32, 'rttMonHTTPStatsTransactionRTTSum'), ['int'])),
                    ('rttmonhttpstatsmessagebodyoctetssum', (YLeaf(YType.uint32, 'rttMonHTTPStatsMessageBodyOctetsSum'), ['int'])),
                    ('rttmonhttpstatsdnsservertimeout', (YLeaf(YType.uint32, 'rttMonHTTPStatsDNSServerTimeout'), ['int'])),
                    ('rttmonhttpstatstcpconnecttimeout', (YLeaf(YType.uint32, 'rttMonHTTPStatsTCPConnectTimeout'), ['int'])),
                    ('rttmonhttpstatstransactiontimeout', (YLeaf(YType.uint32, 'rttMonHTTPStatsTransactionTimeout'), ['int'])),
                    ('rttmonhttpstatsdnsqueryerror', (YLeaf(YType.uint32, 'rttMonHTTPStatsDNSQueryError'), ['int'])),
                    ('rttmonhttpstatshttperror', (YLeaf(YType.uint32, 'rttMonHTTPStatsHTTPError'), ['int'])),
                    ('rttmonhttpstatserror', (YLeaf(YType.uint32, 'rttMonHTTPStatsError'), ['int'])),
                    ('rttmonhttpstatsbusies', (YLeaf(YType.uint32, 'rttMonHTTPStatsBusies'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonhttpstatsstarttimeindex = None
                self.rttmonhttpstatscompletions = None
                self.rttmonhttpstatsoverthresholds = None
                self.rttmonhttpstatsrttsum = None
                self.rttmonhttpstatsrttsum2low = None
                self.rttmonhttpstatsrttsum2high = None
                self.rttmonhttpstatsrttmin = None
                self.rttmonhttpstatsrttmax = None
                self.rttmonhttpstatsdnsrttsum = None
                self.rttmonhttpstatstcpconnectrttsum = None
                self.rttmonhttpstatstransactionrttsum = None
                self.rttmonhttpstatsmessagebodyoctetssum = None
                self.rttmonhttpstatsdnsservertimeout = None
                self.rttmonhttpstatstcpconnecttimeout = None
                self.rttmonhttpstatstransactiontimeout = None
                self.rttmonhttpstatsdnsqueryerror = None
                self.rttmonhttpstatshttperror = None
                self.rttmonhttpstatserror = None
                self.rttmonhttpstatsbusies = None
                self._segment_path = lambda: "rttMonHTTPStatsEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonHTTPStatsStartTimeIndex='" + str(self.rttmonhttpstatsstarttimeindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonHTTPStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonHTTPStatsTable.RttMonHTTPStatsEntry, ['rttmonctrladminindex', 'rttmonhttpstatsstarttimeindex', 'rttmonhttpstatscompletions', 'rttmonhttpstatsoverthresholds', 'rttmonhttpstatsrttsum', 'rttmonhttpstatsrttsum2low', 'rttmonhttpstatsrttsum2high', 'rttmonhttpstatsrttmin', 'rttmonhttpstatsrttmax', 'rttmonhttpstatsdnsrttsum', 'rttmonhttpstatstcpconnectrttsum', 'rttmonhttpstatstransactionrttsum', 'rttmonhttpstatsmessagebodyoctetssum', 'rttmonhttpstatsdnsservertimeout', 'rttmonhttpstatstcpconnecttimeout', 'rttmonhttpstatstransactiontimeout', 'rttmonhttpstatsdnsqueryerror', 'rttmonhttpstatshttperror', 'rttmonhttpstatserror', 'rttmonhttpstatsbusies'], name, value)




    class RttMonJitterStatsTable(Entity):
        """
        The Jitter statistics collection database.
        
        The Jitter statistics table contains summarized information of
        the results for a conceptual RTT control row. A rolling
        accumulated history of this information is maintained in a 
        series of hourly 'group(s)'.
        
        The operation of this table is same as that of 
        rttMonStatsCaptureTable, except that this table will store 
        2 hours of data.
        
        .. attribute:: rttmonjitterstatsentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry is created only if the rttMonCtrlAdminRttType  is jitter. The operation of this table is same as that of rttMonStatsCaptureTable
        	**type**\: list of  		 :py:class:`RttMonJitterStatsEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonJitterStatsTable.RttMonJitterStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonJitterStatsTable, self).__init__()

            self.yang_name = "rttMonJitterStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonJitterStatsEntry", ("rttmonjitterstatsentry", CISCORTTMONMIB.RttMonJitterStatsTable.RttMonJitterStatsEntry))])
            self._leafs = OrderedDict()

            self.rttmonjitterstatsentry = YList(self)
            self._segment_path = lambda: "rttMonJitterStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonJitterStatsTable, [], name, value)


        class RttMonJitterStatsEntry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is jitter. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsstarttimeindex  (key)
            
            	The time when this row was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatscompletions
            
            	The number of jitter operation that have completed successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsoverthresholds
            
            	The number of jitter operations that violate threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsnumofrtt
            
            	The number of RTT's that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttsum
            
            	The sum of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsRTTSumHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttsum2low
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminofpositivessd
            
            	The minimum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxofpositivessd
            
            	The maximum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsnumofpositivessd
            
            	The sum of number of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2positivessdlow
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2positivessdhigh
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminofnegativessd
            
            	The minimum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxofnegativessd
            
            	The maximum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsnumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssumofnegativessd
            
            	The sum of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2negativessdlow
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2negativessdhigh
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsnumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2positivesdslow
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2positivesdshigh
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsnumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2negativesdslow
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatssum2negativesdshigh
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatspacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatspacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatspacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatspacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatspacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatserror
            
            	The number of occasions when a jitter operation could not be initiated because an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsbusies
            
            	The number of occasions when a jitter operation could not be initiated because a previous jitter operation has not been completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsumsd
            
            	The sum of one way times from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumSDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsum2sdlow
            
            	The sum of squares of one way times from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsum2sdhigh
            
            	The sum of squares of one way times from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowminsd
            
            	The minimum of all one way times from source to destination. rttMonJitterStatsOWMinSD object is superseded by rttMonJitterStatsOWMinSDNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxsd
            
            	The maximum of all one way times from source to destination. rttMonJitterStatsOWMaxSD object is superseded by rttMonJitterStatsOWMaxSDNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowsumds
            
            	The sum of one way times from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumDSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsum2dslow
            
            	The sum of squares of one way times from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsum2dshigh
            
            	The sum of squares of one way times from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowminds
            
            	The minimum of all one way times from destination to source. rttMonJitterStatsOWMinDS object is superseded by rttMonJitterStatsOWMinDSNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxds
            
            	The maximum of all one way times from destination to source. rttMonJitterStatsOWMaxDS object is superseded by rttMonJitterStatsOWMaxDSNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsnumofow
            
            	The number of one way times that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowminsdnew
            
            	The minimum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMinSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowmaxsdnew
            
            	The maximum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMaxSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowmindsnew
            
            	The minimum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMinDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowmaxdsnew
            
            	The maximum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMaxDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminofmos
            
            	The minimum of all MOS values for the jitter operations in hundreds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxofmos
            
            	The maximum of all MOS values for the jitter operations in hunderds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsminoficpif
            
            	The minimum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsmaxoficpif
            
            	The maximum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsiajout
            
            	Interarrival Jitter (RFC 1889) at responder
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsiajin
            
            	Interarrival Jitter (RFC 1889) at sender
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsavgjitter
            
            	The average of positive and negative jitter values for SD and DS direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsavgjittersd
            
            	The average of positive and negative jitter values in SD direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsavgjitterds
            
            	The average of positive and negative jitter values in DS direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsrttsumhigh
            
            	The sum of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsRTTSum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsumsdhigh
            
            	The sum of one way times from source to destination (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsOWSumSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonjitterstatsowsumdshigh
            
            	The sum of one way times from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonJitterStatsOWSumDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonJitterStatsTable.RttMonJitterStatsEntry, self).__init__()

                self.yang_name = "rttMonJitterStatsEntry"
                self.yang_parent_name = "rttMonJitterStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonjitterstatsstarttimeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonjitterstatsstarttimeindex', (YLeaf(YType.uint32, 'rttMonJitterStatsStartTimeIndex'), ['int'])),
                    ('rttmonjitterstatscompletions', (YLeaf(YType.uint32, 'rttMonJitterStatsCompletions'), ['int'])),
                    ('rttmonjitterstatsoverthresholds', (YLeaf(YType.uint32, 'rttMonJitterStatsOverThresholds'), ['int'])),
                    ('rttmonjitterstatsnumofrtt', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfRTT'), ['int'])),
                    ('rttmonjitterstatsrttsum', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum'), ['int'])),
                    ('rttmonjitterstatsrttsum2low', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum2Low'), ['int'])),
                    ('rttmonjitterstatsrttsum2high', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum2High'), ['int'])),
                    ('rttmonjitterstatsrttmin', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTMin'), ['int'])),
                    ('rttmonjitterstatsrttmax', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTMax'), ['int'])),
                    ('rttmonjitterstatsminofpositivessd', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfPositivesSD'), ['int'])),
                    ('rttmonjitterstatsmaxofpositivessd', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfPositivesSD'), ['int'])),
                    ('rttmonjitterstatsnumofpositivessd', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfPositivesSD'), ['int'])),
                    ('rttmonjitterstatssumofpositivessd', (YLeaf(YType.uint32, 'rttMonJitterStatsSumOfPositivesSD'), ['int'])),
                    ('rttmonjitterstatssum2positivessdlow', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesSDLow'), ['int'])),
                    ('rttmonjitterstatssum2positivessdhigh', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesSDHigh'), ['int'])),
                    ('rttmonjitterstatsminofnegativessd', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfNegativesSD'), ['int'])),
                    ('rttmonjitterstatsmaxofnegativessd', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfNegativesSD'), ['int'])),
                    ('rttmonjitterstatsnumofnegativessd', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfNegativesSD'), ['int'])),
                    ('rttmonjitterstatssumofnegativessd', (YLeaf(YType.uint32, 'rttMonJitterStatsSumOfNegativesSD'), ['int'])),
                    ('rttmonjitterstatssum2negativessdlow', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesSDLow'), ['int'])),
                    ('rttmonjitterstatssum2negativessdhigh', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesSDHigh'), ['int'])),
                    ('rttmonjitterstatsminofpositivesds', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfPositivesDS'), ['int'])),
                    ('rttmonjitterstatsmaxofpositivesds', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfPositivesDS'), ['int'])),
                    ('rttmonjitterstatsnumofpositivesds', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfPositivesDS'), ['int'])),
                    ('rttmonjitterstatssumofpositivesds', (YLeaf(YType.uint32, 'rttMonJitterStatsSumOfPositivesDS'), ['int'])),
                    ('rttmonjitterstatssum2positivesdslow', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesDSLow'), ['int'])),
                    ('rttmonjitterstatssum2positivesdshigh', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesDSHigh'), ['int'])),
                    ('rttmonjitterstatsminofnegativesds', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfNegativesDS'), ['int'])),
                    ('rttmonjitterstatsmaxofnegativesds', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfNegativesDS'), ['int'])),
                    ('rttmonjitterstatsnumofnegativesds', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfNegativesDS'), ['int'])),
                    ('rttmonjitterstatssumofnegativesds', (YLeaf(YType.uint32, 'rttMonJitterStatsSumOfNegativesDS'), ['int'])),
                    ('rttmonjitterstatssum2negativesdslow', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesDSLow'), ['int'])),
                    ('rttmonjitterstatssum2negativesdshigh', (YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesDSHigh'), ['int'])),
                    ('rttmonjitterstatspacketlosssd', (YLeaf(YType.uint32, 'rttMonJitterStatsPacketLossSD'), ['int'])),
                    ('rttmonjitterstatspacketlossds', (YLeaf(YType.uint32, 'rttMonJitterStatsPacketLossDS'), ['int'])),
                    ('rttmonjitterstatspacketoutofsequence', (YLeaf(YType.uint32, 'rttMonJitterStatsPacketOutOfSequence'), ['int'])),
                    ('rttmonjitterstatspacketmia', (YLeaf(YType.uint32, 'rttMonJitterStatsPacketMIA'), ['int'])),
                    ('rttmonjitterstatspacketlatearrival', (YLeaf(YType.uint32, 'rttMonJitterStatsPacketLateArrival'), ['int'])),
                    ('rttmonjitterstatserror', (YLeaf(YType.uint32, 'rttMonJitterStatsError'), ['int'])),
                    ('rttmonjitterstatsbusies', (YLeaf(YType.uint32, 'rttMonJitterStatsBusies'), ['int'])),
                    ('rttmonjitterstatsowsumsd', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSumSD'), ['int'])),
                    ('rttmonjitterstatsowsum2sdlow', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2SDLow'), ['int'])),
                    ('rttmonjitterstatsowsum2sdhigh', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2SDHigh'), ['int'])),
                    ('rttmonjitterstatsowminsd', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMinSD'), ['int'])),
                    ('rttmonjitterstatsowmaxsd', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxSD'), ['int'])),
                    ('rttmonjitterstatsowsumds', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSumDS'), ['int'])),
                    ('rttmonjitterstatsowsum2dslow', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2DSLow'), ['int'])),
                    ('rttmonjitterstatsowsum2dshigh', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2DSHigh'), ['int'])),
                    ('rttmonjitterstatsowminds', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMinDS'), ['int'])),
                    ('rttmonjitterstatsowmaxds', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxDS'), ['int'])),
                    ('rttmonjitterstatsnumofow', (YLeaf(YType.uint32, 'rttMonJitterStatsNumOfOW'), ['int'])),
                    ('rttmonjitterstatsowminsdnew', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMinSDNew'), ['int'])),
                    ('rttmonjitterstatsowmaxsdnew', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxSDNew'), ['int'])),
                    ('rttmonjitterstatsowmindsnew', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMinDSNew'), ['int'])),
                    ('rttmonjitterstatsowmaxdsnew', (YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxDSNew'), ['int'])),
                    ('rttmonjitterstatsminofmos', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfMOS'), ['int'])),
                    ('rttmonjitterstatsmaxofmos', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfMOS'), ['int'])),
                    ('rttmonjitterstatsminoficpif', (YLeaf(YType.uint32, 'rttMonJitterStatsMinOfICPIF'), ['int'])),
                    ('rttmonjitterstatsmaxoficpif', (YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfICPIF'), ['int'])),
                    ('rttmonjitterstatsiajout', (YLeaf(YType.uint32, 'rttMonJitterStatsIAJOut'), ['int'])),
                    ('rttmonjitterstatsiajin', (YLeaf(YType.uint32, 'rttMonJitterStatsIAJIn'), ['int'])),
                    ('rttmonjitterstatsavgjitter', (YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitter'), ['int'])),
                    ('rttmonjitterstatsavgjittersd', (YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitterSD'), ['int'])),
                    ('rttmonjitterstatsavgjitterds', (YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitterDS'), ['int'])),
                    ('rttmonjitterstatsunsyncrts', (YLeaf(YType.uint32, 'rttMonJitterStatsUnSyncRTs'), ['int'])),
                    ('rttmonjitterstatsrttsumhigh', (YLeaf(YType.uint32, 'rttMonJitterStatsRTTSumHigh'), ['int'])),
                    ('rttmonjitterstatsowsumsdhigh', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSumSDHigh'), ['int'])),
                    ('rttmonjitterstatsowsumdshigh', (YLeaf(YType.uint32, 'rttMonJitterStatsOWSumDSHigh'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonjitterstatsstarttimeindex = None
                self.rttmonjitterstatscompletions = None
                self.rttmonjitterstatsoverthresholds = None
                self.rttmonjitterstatsnumofrtt = None
                self.rttmonjitterstatsrttsum = None
                self.rttmonjitterstatsrttsum2low = None
                self.rttmonjitterstatsrttsum2high = None
                self.rttmonjitterstatsrttmin = None
                self.rttmonjitterstatsrttmax = None
                self.rttmonjitterstatsminofpositivessd = None
                self.rttmonjitterstatsmaxofpositivessd = None
                self.rttmonjitterstatsnumofpositivessd = None
                self.rttmonjitterstatssumofpositivessd = None
                self.rttmonjitterstatssum2positivessdlow = None
                self.rttmonjitterstatssum2positivessdhigh = None
                self.rttmonjitterstatsminofnegativessd = None
                self.rttmonjitterstatsmaxofnegativessd = None
                self.rttmonjitterstatsnumofnegativessd = None
                self.rttmonjitterstatssumofnegativessd = None
                self.rttmonjitterstatssum2negativessdlow = None
                self.rttmonjitterstatssum2negativessdhigh = None
                self.rttmonjitterstatsminofpositivesds = None
                self.rttmonjitterstatsmaxofpositivesds = None
                self.rttmonjitterstatsnumofpositivesds = None
                self.rttmonjitterstatssumofpositivesds = None
                self.rttmonjitterstatssum2positivesdslow = None
                self.rttmonjitterstatssum2positivesdshigh = None
                self.rttmonjitterstatsminofnegativesds = None
                self.rttmonjitterstatsmaxofnegativesds = None
                self.rttmonjitterstatsnumofnegativesds = None
                self.rttmonjitterstatssumofnegativesds = None
                self.rttmonjitterstatssum2negativesdslow = None
                self.rttmonjitterstatssum2negativesdshigh = None
                self.rttmonjitterstatspacketlosssd = None
                self.rttmonjitterstatspacketlossds = None
                self.rttmonjitterstatspacketoutofsequence = None
                self.rttmonjitterstatspacketmia = None
                self.rttmonjitterstatspacketlatearrival = None
                self.rttmonjitterstatserror = None
                self.rttmonjitterstatsbusies = None
                self.rttmonjitterstatsowsumsd = None
                self.rttmonjitterstatsowsum2sdlow = None
                self.rttmonjitterstatsowsum2sdhigh = None
                self.rttmonjitterstatsowminsd = None
                self.rttmonjitterstatsowmaxsd = None
                self.rttmonjitterstatsowsumds = None
                self.rttmonjitterstatsowsum2dslow = None
                self.rttmonjitterstatsowsum2dshigh = None
                self.rttmonjitterstatsowminds = None
                self.rttmonjitterstatsowmaxds = None
                self.rttmonjitterstatsnumofow = None
                self.rttmonjitterstatsowminsdnew = None
                self.rttmonjitterstatsowmaxsdnew = None
                self.rttmonjitterstatsowmindsnew = None
                self.rttmonjitterstatsowmaxdsnew = None
                self.rttmonjitterstatsminofmos = None
                self.rttmonjitterstatsmaxofmos = None
                self.rttmonjitterstatsminoficpif = None
                self.rttmonjitterstatsmaxoficpif = None
                self.rttmonjitterstatsiajout = None
                self.rttmonjitterstatsiajin = None
                self.rttmonjitterstatsavgjitter = None
                self.rttmonjitterstatsavgjittersd = None
                self.rttmonjitterstatsavgjitterds = None
                self.rttmonjitterstatsunsyncrts = None
                self.rttmonjitterstatsrttsumhigh = None
                self.rttmonjitterstatsowsumsdhigh = None
                self.rttmonjitterstatsowsumdshigh = None
                self._segment_path = lambda: "rttMonJitterStatsEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonJitterStatsStartTimeIndex='" + str(self.rttmonjitterstatsstarttimeindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonJitterStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonJitterStatsTable.RttMonJitterStatsEntry, ['rttmonctrladminindex', 'rttmonjitterstatsstarttimeindex', 'rttmonjitterstatscompletions', 'rttmonjitterstatsoverthresholds', 'rttmonjitterstatsnumofrtt', 'rttmonjitterstatsrttsum', 'rttmonjitterstatsrttsum2low', 'rttmonjitterstatsrttsum2high', 'rttmonjitterstatsrttmin', 'rttmonjitterstatsrttmax', 'rttmonjitterstatsminofpositivessd', 'rttmonjitterstatsmaxofpositivessd', 'rttmonjitterstatsnumofpositivessd', 'rttmonjitterstatssumofpositivessd', 'rttmonjitterstatssum2positivessdlow', 'rttmonjitterstatssum2positivessdhigh', 'rttmonjitterstatsminofnegativessd', 'rttmonjitterstatsmaxofnegativessd', 'rttmonjitterstatsnumofnegativessd', 'rttmonjitterstatssumofnegativessd', 'rttmonjitterstatssum2negativessdlow', 'rttmonjitterstatssum2negativessdhigh', 'rttmonjitterstatsminofpositivesds', 'rttmonjitterstatsmaxofpositivesds', 'rttmonjitterstatsnumofpositivesds', 'rttmonjitterstatssumofpositivesds', 'rttmonjitterstatssum2positivesdslow', 'rttmonjitterstatssum2positivesdshigh', 'rttmonjitterstatsminofnegativesds', 'rttmonjitterstatsmaxofnegativesds', 'rttmonjitterstatsnumofnegativesds', 'rttmonjitterstatssumofnegativesds', 'rttmonjitterstatssum2negativesdslow', 'rttmonjitterstatssum2negativesdshigh', 'rttmonjitterstatspacketlosssd', 'rttmonjitterstatspacketlossds', 'rttmonjitterstatspacketoutofsequence', 'rttmonjitterstatspacketmia', 'rttmonjitterstatspacketlatearrival', 'rttmonjitterstatserror', 'rttmonjitterstatsbusies', 'rttmonjitterstatsowsumsd', 'rttmonjitterstatsowsum2sdlow', 'rttmonjitterstatsowsum2sdhigh', 'rttmonjitterstatsowminsd', 'rttmonjitterstatsowmaxsd', 'rttmonjitterstatsowsumds', 'rttmonjitterstatsowsum2dslow', 'rttmonjitterstatsowsum2dshigh', 'rttmonjitterstatsowminds', 'rttmonjitterstatsowmaxds', 'rttmonjitterstatsnumofow', 'rttmonjitterstatsowminsdnew', 'rttmonjitterstatsowmaxsdnew', 'rttmonjitterstatsowmindsnew', 'rttmonjitterstatsowmaxdsnew', 'rttmonjitterstatsminofmos', 'rttmonjitterstatsmaxofmos', 'rttmonjitterstatsminoficpif', 'rttmonjitterstatsmaxoficpif', 'rttmonjitterstatsiajout', 'rttmonjitterstatsiajin', 'rttmonjitterstatsavgjitter', 'rttmonjitterstatsavgjittersd', 'rttmonjitterstatsavgjitterds', 'rttmonjitterstatsunsyncrts', 'rttmonjitterstatsrttsumhigh', 'rttmonjitterstatsowsumsdhigh', 'rttmonjitterstatsowsumdshigh'], name, value)




    class RttMonLpdGrpStatsTable(Entity):
        """
        The Auto SAA L3 MPLS VPN LPD Group Database.
        
        The LPD Group statistics table contains summarized performance
        statistics for the LPD group.
        
        LPD Group \- The set of 'single probes' which are subset of the
        'lspGroup' probe traversing set of paths between two PE end
        points are grouped together and called as the LPD group. The
        LPD group will be uniquely referenced by the LPD Group ID.
        
        A rolling accumulated history of this information is maintained
        in a series of hourly 'group(s)'.
        
        Each conceptual statistics row has a current hourly group, into
        which RTT results are accumulated. At the end of each hour a new
        hourly group is created which then becomes current. The
        counters and accumulators in the new group are initialized to
        zero. The previous group(s) is kept in the table until the table
        contains rttMplsVpnMonTypeLpdStatHours groups for the
        conceptual statistics row;  at this point, the oldest group is
        discarded and is replaced by the newly created one. The hourly
        group is uniquely identified by the
        rttMonLpdGrpStatsStartTimeIndex object.
        
        .. attribute:: rttmonlpdgrpstatsentry
        
        	A list of objects which accumulate the results of a set of RTT operations over a 60 minute time period.  The LPD group statistics table is a rollover table. When rttMonLpdGrpStatsStartTimeIndex groups exceeds the rttMplsVpnMonTypeLpdStatHours value, the oldest corresponding hourly group will be deleted and will be replaced with the new rttMonLpdGrpStatsStartTimeIndex hourly group.  The LPD group statistics table has two indices. Each described as follows\:  \- The first index correlates its entries to a LPD group via the    rttMonLpdGrpStatsGroupIndex object. \- The second index is a rollover group and it uniquely     identifies a 60 minute group. (The     rttMonLpdGrpStatsStartTimeIndex is used to make this value     unique.)
        	**type**\: list of  		 :py:class:`RttMonLpdGrpStatsEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLpdGrpStatsTable.RttMonLpdGrpStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonLpdGrpStatsTable, self).__init__()

            self.yang_name = "rttMonLpdGrpStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonLpdGrpStatsEntry", ("rttmonlpdgrpstatsentry", CISCORTTMONMIB.RttMonLpdGrpStatsTable.RttMonLpdGrpStatsEntry))])
            self._leafs = OrderedDict()

            self.rttmonlpdgrpstatsentry = YList(self)
            self._segment_path = lambda: "rttMonLpdGrpStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonLpdGrpStatsTable, [], name, value)


        class RttMonLpdGrpStatsEntry(Entity):
            """
            A list of objects which accumulate the results of a set of RTT
            operations over a 60 minute time period.
            
            The LPD group statistics table is a rollover table. When
            rttMonLpdGrpStatsStartTimeIndex groups exceeds the
            rttMplsVpnMonTypeLpdStatHours value, the oldest corresponding
            hourly group will be deleted and will be replaced with the new
            rttMonLpdGrpStatsStartTimeIndex hourly group.
            
            The LPD group statistics table has two indices. Each described
            as follows\:
            
            \- The first index correlates its entries to a LPD group via the
               rttMonLpdGrpStatsGroupIndex object.
            \- The second index is a rollover group and it uniquely 
               identifies a 60 minute group. (The 
               rttMonLpdGrpStatsStartTimeIndex is used to make this value 
               unique.)
            
            .. attribute:: rttmonlpdgrpstatsgroupindex  (key)
            
            	Uniquely identifies a row in rttMonLpdGrpStatsTable.  This is a pseudo\-random number which identifies a particular LPD group
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatsstarttimeindex  (key)
            
            	The time when this row was created.  This object is the second index of the rttMonLpdGrpStatsTable. When the number of rttMonLpdGrpStatsStartTimeIndex groups exceeds the rttMplsVpnMonTypeLpdStatHours value, the oldest rttMonLpdGrpStatsStartTimeIndex group will be removed and replaced with the new entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatstargetpe
            
            	The object is a string that specifies the address of the target PE for this LPD group
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatsnumofpass
            
            	This object represents the number of successfull completions of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense value is 'ok' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: passes
            
            .. attribute:: rttmonlpdgrpstatsnumoffail
            
            	This object represents the number of failed operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value other than 'ok' or 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: failures
            
            .. attribute:: rttmonlpdgrpstatsnumoftimeout
            
            	This object represents the number of timed out operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value of 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: timeouts
            
            .. attribute:: rttmonlpdgrpstatsavgrtt
            
            	The average RTT across all set of probes in the LPD group.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsminrtt
            
            	The minimum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsmaxrtt
            
            	The maximum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsminnumpaths
            
            	The minimum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatsmaxnumpaths
            
            	The maximum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatslpdstarttime
            
            	The time when the last LSP Path Discovery to the group was attempted.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: tenths of milliseconds
            
            .. attribute:: rttmonlpdgrpstatslpdfailoccurred
            
            	This object is set to true when the LSP Path Discovery to the target PE i.e. rttMonLpdGrpStatsTargetPE fails, and set to false when the LSP Path Discovery succeeds.  When this value changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdPathDiscovery' or 'lpdAll' a rttMonLpdDiscoveryNotification will be generated.  This object will be set to 'FALSE' on reset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatslpdfailcause
            
            	This object identifies the cause of failure for the LSP Path Discovery last attempted. It will be only valid if rttMonLpdGrpStatsLPDFailOccurred is set to true.  This object will be set to 'unknown' on reset
            	**type**\:  :py:class:`RttMplsVpnMonLpdFailureSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonLpdFailureSense>`
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatslpdcomptime
            
            	The completion time of the last successfull LSP Path Discovery to the target PE.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rttmonlpdgrpstatsgroupstatus
            
            	This object identifies the LPD Group status.  When the LPD Group status changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdGroupStatus' or 'lpdAll' a rttMonLpdGrpStatusNotification will be generated.  When the LPD Group status value is 'unknown' or changes to 'unknown' this notification will not be generated.  When LSP Path Discovery is enabled for a particular row in rttMplsVpnMonCtrlTable, 'single probes' in the 'lspGroup' probe cannot generate notifications independently but will be generating depending on the state of the group. Notifications  are only generated if the failure/restoration of an individual probe causes the state of the LPD Group to change.  This object will be set to 'unknown' on reset
            	**type**\:  :py:class:`RttMplsVpnMonLpdGrpStatus <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonLpdGrpStatus>`
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatsgroupprobeindex
            
            	This object identifies 'lspGroup' probe uniquely created for this particular LPD Group
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            	**units**\: identifier
            
            .. attribute:: rttmonlpdgrpstatspathids
            
            	A string which holds the list of information to uniquely identify the paths to the target PE. This information is used by the 'single probes' when testing the paths.  Following three parameters are needed to uniquely identify a  path   \- lsp\-selector (127.x.x.x)   \- outgoing\-interface (i/f)   \- label\-stack (s), if mutiple labels they will be colon (\:)     separated.  These parameters will be hyphen (\-) separated for a particular path. This set of information will be comma (,) separated for all the paths discovered as part of this LPD Group.  For example\: If there are 5 paths in the LPD group then this object will return all the identifier's to uniquely identify the path.  The output will look like '127.0.0.1\-Se3/0.1\-20\:18, 127.0.0.2\-Se3/0.1\-20,127.0.0.3\-Se3/0.1\-20,127.0.0.4\-Se3/0.1\-20, 127.0.0.5\-Se3/0.1\-20'.  This object will be set to '0' on reset
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatsprobestatus
            
            	A string which holds the latest operation return code for all the set of 'single probes' which are part of the LPD group. The return codes will be comma separated and will follow the same sequence of probes as followed in 'rttMonLpdGrpStatsPathIds'. The latest operation return code will be mapped to 'up','down' or 'unkwown'.  'up' \- Probe state is up when the rttMonLatestRttOperSense value is 'ok'. 'down' \- Probe state is down when the rttMonLatestRttOperSense has value other then 'ok' and 'other'. 'unknown' \- Probe state is unkown when the rttMonLatestRttOperSense value is 'other'.  For example\: If there are 5 paths in the LPD group then this object output will look like 'ok,ok,ok,down,down'.  This object will be set to '0' on reset
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonlpdgrpstatsresettime
            
            	This object specifies the time when this statistics row was last reset using the rttMonApplLpdGrpStatsReset object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonLpdGrpStatsTable.RttMonLpdGrpStatsEntry, self).__init__()

                self.yang_name = "rttMonLpdGrpStatsEntry"
                self.yang_parent_name = "rttMonLpdGrpStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonlpdgrpstatsgroupindex','rttmonlpdgrpstatsstarttimeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonlpdgrpstatsgroupindex', (YLeaf(YType.int32, 'rttMonLpdGrpStatsGroupIndex'), ['int'])),
                    ('rttmonlpdgrpstatsstarttimeindex', (YLeaf(YType.uint32, 'rttMonLpdGrpStatsStartTimeIndex'), ['int'])),
                    ('rttmonlpdgrpstatstargetpe', (YLeaf(YType.str, 'rttMonLpdGrpStatsTargetPE'), ['str'])),
                    ('rttmonlpdgrpstatsnumofpass', (YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfPass'), ['int'])),
                    ('rttmonlpdgrpstatsnumoffail', (YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfFail'), ['int'])),
                    ('rttmonlpdgrpstatsnumoftimeout', (YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfTimeout'), ['int'])),
                    ('rttmonlpdgrpstatsavgrtt', (YLeaf(YType.int32, 'rttMonLpdGrpStatsAvgRTT'), ['int'])),
                    ('rttmonlpdgrpstatsminrtt', (YLeaf(YType.int32, 'rttMonLpdGrpStatsMinRTT'), ['int'])),
                    ('rttmonlpdgrpstatsmaxrtt', (YLeaf(YType.int32, 'rttMonLpdGrpStatsMaxRTT'), ['int'])),
                    ('rttmonlpdgrpstatsminnumpaths', (YLeaf(YType.int32, 'rttMonLpdGrpStatsMinNumPaths'), ['int'])),
                    ('rttmonlpdgrpstatsmaxnumpaths', (YLeaf(YType.int32, 'rttMonLpdGrpStatsMaxNumPaths'), ['int'])),
                    ('rttmonlpdgrpstatslpdstarttime', (YLeaf(YType.uint32, 'rttMonLpdGrpStatsLPDStartTime'), ['int'])),
                    ('rttmonlpdgrpstatslpdfailoccurred', (YLeaf(YType.boolean, 'rttMonLpdGrpStatsLPDFailOccurred'), ['bool'])),
                    ('rttmonlpdgrpstatslpdfailcause', (YLeaf(YType.enumeration, 'rttMonLpdGrpStatsLPDFailCause'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMplsVpnMonLpdFailureSense', '')])),
                    ('rttmonlpdgrpstatslpdcomptime', (YLeaf(YType.int32, 'rttMonLpdGrpStatsLPDCompTime'), ['int'])),
                    ('rttmonlpdgrpstatsgroupstatus', (YLeaf(YType.enumeration, 'rttMonLpdGrpStatsGroupStatus'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttMplsVpnMonLpdGrpStatus', '')])),
                    ('rttmonlpdgrpstatsgroupprobeindex', (YLeaf(YType.int32, 'rttMonLpdGrpStatsGroupProbeIndex'), ['int'])),
                    ('rttmonlpdgrpstatspathids', (YLeaf(YType.str, 'rttMonLpdGrpStatsPathIds'), ['str'])),
                    ('rttmonlpdgrpstatsprobestatus', (YLeaf(YType.str, 'rttMonLpdGrpStatsProbeStatus'), ['str'])),
                    ('rttmonlpdgrpstatsresettime', (YLeaf(YType.uint32, 'rttMonLpdGrpStatsResetTime'), ['int'])),
                ])
                self.rttmonlpdgrpstatsgroupindex = None
                self.rttmonlpdgrpstatsstarttimeindex = None
                self.rttmonlpdgrpstatstargetpe = None
                self.rttmonlpdgrpstatsnumofpass = None
                self.rttmonlpdgrpstatsnumoffail = None
                self.rttmonlpdgrpstatsnumoftimeout = None
                self.rttmonlpdgrpstatsavgrtt = None
                self.rttmonlpdgrpstatsminrtt = None
                self.rttmonlpdgrpstatsmaxrtt = None
                self.rttmonlpdgrpstatsminnumpaths = None
                self.rttmonlpdgrpstatsmaxnumpaths = None
                self.rttmonlpdgrpstatslpdstarttime = None
                self.rttmonlpdgrpstatslpdfailoccurred = None
                self.rttmonlpdgrpstatslpdfailcause = None
                self.rttmonlpdgrpstatslpdcomptime = None
                self.rttmonlpdgrpstatsgroupstatus = None
                self.rttmonlpdgrpstatsgroupprobeindex = None
                self.rttmonlpdgrpstatspathids = None
                self.rttmonlpdgrpstatsprobestatus = None
                self.rttmonlpdgrpstatsresettime = None
                self._segment_path = lambda: "rttMonLpdGrpStatsEntry" + "[rttMonLpdGrpStatsGroupIndex='" + str(self.rttmonlpdgrpstatsgroupindex) + "']" + "[rttMonLpdGrpStatsStartTimeIndex='" + str(self.rttmonlpdgrpstatsstarttimeindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLpdGrpStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonLpdGrpStatsTable.RttMonLpdGrpStatsEntry, ['rttmonlpdgrpstatsgroupindex', 'rttmonlpdgrpstatsstarttimeindex', 'rttmonlpdgrpstatstargetpe', 'rttmonlpdgrpstatsnumofpass', 'rttmonlpdgrpstatsnumoffail', 'rttmonlpdgrpstatsnumoftimeout', 'rttmonlpdgrpstatsavgrtt', 'rttmonlpdgrpstatsminrtt', 'rttmonlpdgrpstatsmaxrtt', 'rttmonlpdgrpstatsminnumpaths', 'rttmonlpdgrpstatsmaxnumpaths', 'rttmonlpdgrpstatslpdstarttime', 'rttmonlpdgrpstatslpdfailoccurred', 'rttmonlpdgrpstatslpdfailcause', 'rttmonlpdgrpstatslpdcomptime', 'rttmonlpdgrpstatsgroupstatus', 'rttmonlpdgrpstatsgroupprobeindex', 'rttmonlpdgrpstatspathids', 'rttmonlpdgrpstatsprobestatus', 'rttmonlpdgrpstatsresettime'], name, value)




    class RttMonHistoryCollectionTable(Entity):
        """
        The history collection database.
        
        The history table contains a point by point rolling 
        history of the most recent RTT operations for each 
        conceptual RTT control row.  The rolling history of this 
        information is maintained in a series of 'live(s)', each
        containing a series of 'bucket(s)', each 'bucket' 
        contains a series of 'sample(s)'.
        
        Each conceptual history row can have lives.  A life is 
        defined by the rttMonCtrlOperRttLife object.  A new life 
        will be created when rttMonCtrlOperState transitions
        'active'.  When the number of lives become greater 
        than rttMonHistoryAdminNumLives the oldest life will be 
        discarded and a new life will be created by incrementing
        the index.
        
        The path exploration RTT operation will be kept as an
        entry in this table.
        
        .. attribute:: rttmonhistorycollectionentry
        
        	A list of history objects that are recorded for each RTT operation.  The history collection table has four indices.  Each  described as follows\:   \-  The first index correlates its entries to a        conceptual RTT control row via the        rttMonCtrlAdminIndex object.     \-  The second index uniquely identifies the results        of each 'life' as defined by the        rttMonCtrlOperRttLife object.     \-  The third index uniquely identifies the number of        buckets in a life.  A bucket will contain one        sample per bucket if the rttMonCtrlAdminRttType        object is set to any value       other than 'pathEcho'.  If the        rttMonCtrlAdminRttType object is set to        'pathEcho', a bucket will contain one sample per        hop along a path to the target (including the        target).     \-  The fourth index uniquely identifies the number of        samples in a bucket.   Again, if the        rttMonCtrlAdminRttType object is set to        'pathEcho', this value is associated with each        hop in an ascending order, thus for the        first hop on a path, this index will be 1, the        second will be 2 and so on.   For all other values       of rttMonCtrlAdminRttType this will be 1
        	**type**\: list of  		 :py:class:`RttMonHistoryCollectionEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonHistoryCollectionTable.RttMonHistoryCollectionEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonHistoryCollectionTable, self).__init__()

            self.yang_name = "rttMonHistoryCollectionTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonHistoryCollectionEntry", ("rttmonhistorycollectionentry", CISCORTTMONMIB.RttMonHistoryCollectionTable.RttMonHistoryCollectionEntry))])
            self._leafs = OrderedDict()

            self.rttmonhistorycollectionentry = YList(self)
            self._segment_path = lambda: "rttMonHistoryCollectionTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonHistoryCollectionTable, [], name, value)


        class RttMonHistoryCollectionEntry(Entity):
            """
            A list of history objects that are recorded for each
            RTT operation.
            
            The history collection table has four indices.  Each 
            described as follows\:
              \-  The first index correlates its entries to a 
                  conceptual RTT control row via the 
                  rttMonCtrlAdminIndex object.  
              \-  The second index uniquely identifies the results 
                  of each 'life' as defined by the 
                  rttMonCtrlOperRttLife object.  
              \-  The third index uniquely identifies the number of 
                  buckets in a life.  A bucket will contain one 
                  sample per bucket if the rttMonCtrlAdminRttType 
                  object is set to any value
                  other than 'pathEcho'.  If the 
                  rttMonCtrlAdminRttType object is set to 
                  'pathEcho', a bucket will contain one sample per 
                  hop along a path to the target (including the 
                  target).  
              \-  The fourth index uniquely identifies the number of 
                  samples in a bucket.   Again, if the 
                  rttMonCtrlAdminRttType object is set to 
                  'pathEcho', this value is associated with each 
                  hop in an ascending order, thus for the 
                  first hop on a path, this index will be 1, the 
                  second will be 2 and so on.   For all other values
                  of rttMonCtrlAdminRttType this will be 1.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionlifeindex  (key)
            
            	This uniquely defines a life for a conceptual history row.  For a particular value of rttMonHistoryCollectionLifeIndex, the agent assigns the first value of 1, the second value  of 2, and so on.  The sequence keeps incrementing,  despite older (lower) values being removed from the  table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionbucketindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this uniquely defines a bucket for a given value of  rttMonHistoryCollectionLifeIndex.  For all other  RttMonRttType this value will be the number of operations per a lifetime.  Thus, this object  increments on each operation attempt.  For a particular value of  rttMonHistoryCollectionLifeIndex, the agent assigns  the first value of 1, the second value of 2, and so  on.  The sequence keeps incrementing until the number of buckets equals rttMonHistoryAdminNumBuckets, after which the most recent rttMonHistoryAdminNumBuckets  buckets are retained (the index is incremented though)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionsampleindex  (key)
            
            	This uniquely defines a row for a given value of rttMonHistoryCollectionBucketIndex.  This object represents a hop along a path to the Target.  For a particular value of  rttMonHistoryCollectionBucketIndex, the agent assigns  the first value of 1, the second value of 2, and so on. The sequence keeps incrementing until the number of  samples equals rttMonHistoryAdminNumSamples, then no  new samples are created for the current  rttMonHistoryCollectionBucketIndex.  When the RttMonRttType is 'pathEcho', this value  directly represents the number of hops along a  path to a target, thus we can only support 512 hops. For all other values of RttMonRttType this object will be one
            	**type**\: int
            
            	**range:** 1..512
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionsampletime
            
            	The time that the RTT operation was initiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionaddress
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is a string which specifies the address of the target for the this RTT operation.  For all other values of RttMonRttType this string will be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectioncompletiontime
            
            	This is the operation completion time of the RTT operation.  If the RTT operation fails  (rttMonHistoryCollectionSense is any  value other than ok), this has a value of 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhistorycollectionsense
            
            	A sense code for the completion status of the RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionapplspecificsense
            
            	An application specific sense code for the completion status of the last RTT operation.  This  object will only be valid when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonhistorycollectionsensedescription
            
            	A sense description for the completion status of the last RTT operation when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonHistoryCollectionTable.RttMonHistoryCollectionEntry, self).__init__()

                self.yang_name = "rttMonHistoryCollectionEntry"
                self.yang_parent_name = "rttMonHistoryCollectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonhistorycollectionlifeindex','rttmonhistorycollectionbucketindex','rttmonhistorycollectionsampleindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonhistorycollectionlifeindex', (YLeaf(YType.int32, 'rttMonHistoryCollectionLifeIndex'), ['int'])),
                    ('rttmonhistorycollectionbucketindex', (YLeaf(YType.int32, 'rttMonHistoryCollectionBucketIndex'), ['int'])),
                    ('rttmonhistorycollectionsampleindex', (YLeaf(YType.int32, 'rttMonHistoryCollectionSampleIndex'), ['int'])),
                    ('rttmonhistorycollectionsampletime', (YLeaf(YType.uint32, 'rttMonHistoryCollectionSampleTime'), ['int'])),
                    ('rttmonhistorycollectionaddress', (YLeaf(YType.str, 'rttMonHistoryCollectionAddress'), ['str'])),
                    ('rttmonhistorycollectioncompletiontime', (YLeaf(YType.uint32, 'rttMonHistoryCollectionCompletionTime'), ['int'])),
                    ('rttmonhistorycollectionsense', (YLeaf(YType.enumeration, 'rttMonHistoryCollectionSense'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttResponseSense', '')])),
                    ('rttmonhistorycollectionapplspecificsense', (YLeaf(YType.int32, 'rttMonHistoryCollectionApplSpecificSense'), ['int'])),
                    ('rttmonhistorycollectionsensedescription', (YLeaf(YType.str, 'rttMonHistoryCollectionSenseDescription'), ['str'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonhistorycollectionlifeindex = None
                self.rttmonhistorycollectionbucketindex = None
                self.rttmonhistorycollectionsampleindex = None
                self.rttmonhistorycollectionsampletime = None
                self.rttmonhistorycollectionaddress = None
                self.rttmonhistorycollectioncompletiontime = None
                self.rttmonhistorycollectionsense = None
                self.rttmonhistorycollectionapplspecificsense = None
                self.rttmonhistorycollectionsensedescription = None
                self._segment_path = lambda: "rttMonHistoryCollectionEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonHistoryCollectionLifeIndex='" + str(self.rttmonhistorycollectionlifeindex) + "']" + "[rttMonHistoryCollectionBucketIndex='" + str(self.rttmonhistorycollectionbucketindex) + "']" + "[rttMonHistoryCollectionSampleIndex='" + str(self.rttmonhistorycollectionsampleindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonHistoryCollectionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonHistoryCollectionTable.RttMonHistoryCollectionEntry, ['rttmonctrladminindex', 'rttmonhistorycollectionlifeindex', 'rttmonhistorycollectionbucketindex', 'rttmonhistorycollectionsampleindex', 'rttmonhistorycollectionsampletime', 'rttmonhistorycollectionaddress', 'rttmonhistorycollectioncompletiontime', 'rttmonhistorycollectionsense', 'rttmonhistorycollectionapplspecificsense', 'rttmonhistorycollectionsensedescription'], name, value)




    class RttMonLatestHTTPOperTable(Entity):
        """
        A table which contains the status of latest HTTP RTT
        operation.
        
        .. attribute:: rttmonlatesthttpoperentry
        
        	A list of objects that record the latest HTTP RTT operation. This entry is created automatically after the  rttMonCtrlAdminEntry is created. Also the entry is  automatically deleted when rttMonCtrlAdminEntry is deleted
        	**type**\: list of  		 :py:class:`RttMonLatestHTTPOperEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLatestHTTPOperTable.RttMonLatestHTTPOperEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonLatestHTTPOperTable, self).__init__()

            self.yang_name = "rttMonLatestHTTPOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonLatestHTTPOperEntry", ("rttmonlatesthttpoperentry", CISCORTTMONMIB.RttMonLatestHTTPOperTable.RttMonLatestHTTPOperEntry))])
            self._leafs = OrderedDict()

            self.rttmonlatesthttpoperentry = YList(self)
            self._segment_path = lambda: "rttMonLatestHTTPOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonLatestHTTPOperTable, [], name, value)


        class RttMonLatestHTTPOperEntry(Entity):
            """
            A list of objects that record the latest HTTP RTT
            operation. This entry is created automatically after the 
            rttMonCtrlAdminEntry is created. Also the entry is 
            automatically deleted when rttMonCtrlAdminEntry is deleted.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpoperrtt
            
            	Round Trip Time taken to perform HTTP operation. This value is the sum of DNSRTT, TCPConnectRTT and TransactionRTT
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpoperdnsrtt
            
            	Round Trip Time taken to perform DNS query within the HTTP operation. If an IP Address is specified in the URL,  then DNSRTT is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpopertcpconnectrtt
            
            	Round Trip Time taken to connect to the HTTP server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpopertransactionrtt
            
            	Round Trip Time taken to download the object specified by the URL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpopermessagebodyoctets
            
            	The size of the message body received as a response to the HTTP request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttpopersense
            
            	An application specific sense code for the completion status of the latest RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatesthttperrorsensedescription
            
            	An sense description for the completion status of the latest RTT operation
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonLatestHTTPOperTable.RttMonLatestHTTPOperEntry, self).__init__()

                self.yang_name = "rttMonLatestHTTPOperEntry"
                self.yang_parent_name = "rttMonLatestHTTPOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonlatesthttpoperrtt', (YLeaf(YType.uint32, 'rttMonLatestHTTPOperRTT'), ['int'])),
                    ('rttmonlatesthttpoperdnsrtt', (YLeaf(YType.uint32, 'rttMonLatestHTTPOperDNSRTT'), ['int'])),
                    ('rttmonlatesthttpopertcpconnectrtt', (YLeaf(YType.uint32, 'rttMonLatestHTTPOperTCPConnectRTT'), ['int'])),
                    ('rttmonlatesthttpopertransactionrtt', (YLeaf(YType.uint32, 'rttMonLatestHTTPOperTransactionRTT'), ['int'])),
                    ('rttmonlatesthttpopermessagebodyoctets', (YLeaf(YType.uint32, 'rttMonLatestHTTPOperMessageBodyOctets'), ['int'])),
                    ('rttmonlatesthttpopersense', (YLeaf(YType.enumeration, 'rttMonLatestHTTPOperSense'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttResponseSense', '')])),
                    ('rttmonlatesthttperrorsensedescription', (YLeaf(YType.str, 'rttMonLatestHTTPErrorSenseDescription'), ['str'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonlatesthttpoperrtt = None
                self.rttmonlatesthttpoperdnsrtt = None
                self.rttmonlatesthttpopertcpconnectrtt = None
                self.rttmonlatesthttpopertransactionrtt = None
                self.rttmonlatesthttpopermessagebodyoctets = None
                self.rttmonlatesthttpopersense = None
                self.rttmonlatesthttperrorsensedescription = None
                self._segment_path = lambda: "rttMonLatestHTTPOperEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLatestHTTPOperTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonLatestHTTPOperTable.RttMonLatestHTTPOperEntry, ['rttmonctrladminindex', 'rttmonlatesthttpoperrtt', 'rttmonlatesthttpoperdnsrtt', 'rttmonlatesthttpopertcpconnectrtt', 'rttmonlatesthttpopertransactionrtt', 'rttmonlatesthttpopermessagebodyoctets', 'rttmonlatesthttpopersense', 'rttmonlatesthttperrorsensedescription'], name, value)




    class RttMonLatestJitterOperTable(Entity):
        """
        A table which contains the status of latest Jitter
        operation.
        
        .. attribute:: rttmonlatestjitteroperentry
        
        	A list of objects that record the latest Jitter operation
        	**type**\: list of  		 :py:class:`RttMonLatestJitterOperEntry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.RttMonLatestJitterOperTable, self).__init__()

            self.yang_name = "rttMonLatestJitterOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rttMonLatestJitterOperEntry", ("rttmonlatestjitteroperentry", CISCORTTMONMIB.RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry))])
            self._leafs = OrderedDict()

            self.rttmonlatestjitteroperentry = YList(self)
            self._segment_path = lambda: "rttMonLatestJitterOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.RttMonLatestJitterOperTable, [], name, value)


        class RttMonLatestJitterOperEntry(Entity):
            """
            A list of objects that record the latest Jitter
            operation.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonCtrlAdminTable.RttMonCtrlAdminEntry>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofrtt
            
            	The number of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttsum
            
            	The sum of Jitter RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSumHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttsum2
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSum2High
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperminofpositivessd
            
            	The minimum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropermaxofpositivessd
            
            	The maximum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersumofpositivessd
            
            	The sum of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersum2positivessd
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperminofnegativessd
            
            	The minimum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropermaxofnegativessd
            
            	The maximum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersumofnegativessd
            
            	The sum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersum2negativessd
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropermaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersum2positivesds
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropermaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersum2negativesds
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperpacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperpacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperpacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperpacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperpacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropersense
            
            	An application specific sense code for the completion status of the latest Jitter RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjittererrorsensedescription
            
            	An sense description for the completion status of the latest Jitter RTT operation
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsumsd
            
            	The sum of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumSDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsum2sd
            
            	The sum of squares of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2SDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowminsd
            
            	The minimum of all one way latency from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowmaxsd
            
            	The maximum of all one way latency from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsumds
            
            	The sum of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumDSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsum2ds
            
            	The sum of squares of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2DSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowminds
            
            	The minimum of all one way latency from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowmaxds
            
            	The maximum of all one way latency from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropernumofow
            
            	The number of successful one way latency measurements
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropermos
            
            	The MOS value for the latest jitter operation in hundreds. This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteropericpif
            
            	Represents ICPIF value for the latest jitter operation.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperiajout
            
            	Interarrival Jitter (RC1889) at responder
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperiajin
            
            	Interarrival Jitter (RFC1889) at source
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperavgjitter
            
            	The average of positive and negative jitter values in SD and DS direction for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperavgsdj
            
            	The average of positive and negative jitter values from source to destination for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperavgdsj
            
            	The average of positive and negative jitter values from destination to source for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowavgsd
            
            	The average latency value from source to destination
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowavgds
            
            	The average latency value from destination to source
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperntpstate
            
            	A value of sync(1) means sender and responder was in sync with NTP. The NTP sync means the total of NTP offset  on sender and responder is within configured tolerance level
            	**type**\:  :py:class:`RttMonLatestJitterOperNTPState <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry.RttMonLatestJitterOperNTPState>`
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttsumhigh
            
            	The sum of Jitter RTT's that are successfully measured. (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum2
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsumsdhigh
            
            	The sum of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSumSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsum2sdhigh
            
            	The sum of squares of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2SD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsumdshigh
            
            	The sum of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored  in rttMonLatestJitterOperOWSumDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rttmonlatestjitteroperowsum2dshigh
            
            	The sum of squares of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2DS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry, self).__init__()

                self.yang_name = "rttMonLatestJitterOperEntry"
                self.yang_parent_name = "rttMonLatestJitterOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', (YLeaf(YType.str, 'rttMonCtrlAdminIndex'), ['int'])),
                    ('rttmonlatestjitteropernumofrtt', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfRTT'), ['int'])),
                    ('rttmonlatestjitteroperrttsum', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum'), ['int'])),
                    ('rttmonlatestjitteroperrttsum2', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum2'), ['int'])),
                    ('rttmonlatestjitteroperrttmin', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTMin'), ['int'])),
                    ('rttmonlatestjitteroperrttmax', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTMax'), ['int'])),
                    ('rttmonlatestjitteroperminofpositivessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfPositivesSD'), ['int'])),
                    ('rttmonlatestjitteropermaxofpositivessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfPositivesSD'), ['int'])),
                    ('rttmonlatestjitteropernumofpositivessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfPositivesSD'), ['int'])),
                    ('rttmonlatestjitteropersumofpositivessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfPositivesSD'), ['int'])),
                    ('rttmonlatestjitteropersum2positivessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2PositivesSD'), ['int'])),
                    ('rttmonlatestjitteroperminofnegativessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfNegativesSD'), ['int'])),
                    ('rttmonlatestjitteropermaxofnegativessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfNegativesSD'), ['int'])),
                    ('rttmonlatestjitteropernumofnegativessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfNegativesSD'), ['int'])),
                    ('rttmonlatestjitteropersumofnegativessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfNegativesSD'), ['int'])),
                    ('rttmonlatestjitteropersum2negativessd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2NegativesSD'), ['int'])),
                    ('rttmonlatestjitteroperminofpositivesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfPositivesDS'), ['int'])),
                    ('rttmonlatestjitteropermaxofpositivesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfPositivesDS'), ['int'])),
                    ('rttmonlatestjitteropernumofpositivesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfPositivesDS'), ['int'])),
                    ('rttmonlatestjitteropersumofpositivesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfPositivesDS'), ['int'])),
                    ('rttmonlatestjitteropersum2positivesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2PositivesDS'), ['int'])),
                    ('rttmonlatestjitteroperminofnegativesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfNegativesDS'), ['int'])),
                    ('rttmonlatestjitteropermaxofnegativesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfNegativesDS'), ['int'])),
                    ('rttmonlatestjitteropernumofnegativesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfNegativesDS'), ['int'])),
                    ('rttmonlatestjitteropersumofnegativesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfNegativesDS'), ['int'])),
                    ('rttmonlatestjitteropersum2negativesds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2NegativesDS'), ['int'])),
                    ('rttmonlatestjitteroperpacketlosssd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLossSD'), ['int'])),
                    ('rttmonlatestjitteroperpacketlossds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLossDS'), ['int'])),
                    ('rttmonlatestjitteroperpacketoutofsequence', (YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketOutOfSequence'), ['int'])),
                    ('rttmonlatestjitteroperpacketmia', (YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketMIA'), ['int'])),
                    ('rttmonlatestjitteroperpacketlatearrival', (YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLateArrival'), ['int'])),
                    ('rttmonlatestjitteropersense', (YLeaf(YType.enumeration, 'rttMonLatestJitterOperSense'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB', 'RttResponseSense', '')])),
                    ('rttmonlatestjittererrorsensedescription', (YLeaf(YType.str, 'rttMonLatestJitterErrorSenseDescription'), ['str'])),
                    ('rttmonlatestjitteroperowsumsd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumSD'), ['int'])),
                    ('rttmonlatestjitteroperowsum2sd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2SD'), ['int'])),
                    ('rttmonlatestjitteroperowminsd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMinSD'), ['int'])),
                    ('rttmonlatestjitteroperowmaxsd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMaxSD'), ['int'])),
                    ('rttmonlatestjitteroperowsumds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumDS'), ['int'])),
                    ('rttmonlatestjitteroperowsum2ds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2DS'), ['int'])),
                    ('rttmonlatestjitteroperowminds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMinDS'), ['int'])),
                    ('rttmonlatestjitteroperowmaxds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMaxDS'), ['int'])),
                    ('rttmonlatestjitteropernumofow', (YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfOW'), ['int'])),
                    ('rttmonlatestjitteropermos', (YLeaf(YType.uint32, 'rttMonLatestJitterOperMOS'), ['int'])),
                    ('rttmonlatestjitteropericpif', (YLeaf(YType.uint32, 'rttMonLatestJitterOperICPIF'), ['int'])),
                    ('rttmonlatestjitteroperiajout', (YLeaf(YType.uint32, 'rttMonLatestJitterOperIAJOut'), ['int'])),
                    ('rttmonlatestjitteroperiajin', (YLeaf(YType.uint32, 'rttMonLatestJitterOperIAJIn'), ['int'])),
                    ('rttmonlatestjitteroperavgjitter', (YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgJitter'), ['int'])),
                    ('rttmonlatestjitteroperavgsdj', (YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgSDJ'), ['int'])),
                    ('rttmonlatestjitteroperavgdsj', (YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgDSJ'), ['int'])),
                    ('rttmonlatestjitteroperowavgsd', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWAvgSD'), ['int'])),
                    ('rttmonlatestjitteroperowavgds', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWAvgDS'), ['int'])),
                    ('rttmonlatestjitteroperntpstate', (YLeaf(YType.enumeration, 'rttMonLatestJitterOperNTPState'), [('ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB', 'CISCORTTMONMIB', 'RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry.RttMonLatestJitterOperNTPState')])),
                    ('rttmonlatestjitteroperunsyncrts', (YLeaf(YType.uint32, 'rttMonLatestJitterOperUnSyncRTs'), ['int'])),
                    ('rttmonlatestjitteroperrttsumhigh', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSumHigh'), ['int'])),
                    ('rttmonlatestjitteroperrttsum2high', (YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum2High'), ['int'])),
                    ('rttmonlatestjitteroperowsumsdhigh', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumSDHigh'), ['int'])),
                    ('rttmonlatestjitteroperowsum2sdhigh', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2SDHigh'), ['int'])),
                    ('rttmonlatestjitteroperowsumdshigh', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumDSHigh'), ['int'])),
                    ('rttmonlatestjitteroperowsum2dshigh', (YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2DSHigh'), ['int'])),
                ])
                self.rttmonctrladminindex = None
                self.rttmonlatestjitteropernumofrtt = None
                self.rttmonlatestjitteroperrttsum = None
                self.rttmonlatestjitteroperrttsum2 = None
                self.rttmonlatestjitteroperrttmin = None
                self.rttmonlatestjitteroperrttmax = None
                self.rttmonlatestjitteroperminofpositivessd = None
                self.rttmonlatestjitteropermaxofpositivessd = None
                self.rttmonlatestjitteropernumofpositivessd = None
                self.rttmonlatestjitteropersumofpositivessd = None
                self.rttmonlatestjitteropersum2positivessd = None
                self.rttmonlatestjitteroperminofnegativessd = None
                self.rttmonlatestjitteropermaxofnegativessd = None
                self.rttmonlatestjitteropernumofnegativessd = None
                self.rttmonlatestjitteropersumofnegativessd = None
                self.rttmonlatestjitteropersum2negativessd = None
                self.rttmonlatestjitteroperminofpositivesds = None
                self.rttmonlatestjitteropermaxofpositivesds = None
                self.rttmonlatestjitteropernumofpositivesds = None
                self.rttmonlatestjitteropersumofpositivesds = None
                self.rttmonlatestjitteropersum2positivesds = None
                self.rttmonlatestjitteroperminofnegativesds = None
                self.rttmonlatestjitteropermaxofnegativesds = None
                self.rttmonlatestjitteropernumofnegativesds = None
                self.rttmonlatestjitteropersumofnegativesds = None
                self.rttmonlatestjitteropersum2negativesds = None
                self.rttmonlatestjitteroperpacketlosssd = None
                self.rttmonlatestjitteroperpacketlossds = None
                self.rttmonlatestjitteroperpacketoutofsequence = None
                self.rttmonlatestjitteroperpacketmia = None
                self.rttmonlatestjitteroperpacketlatearrival = None
                self.rttmonlatestjitteropersense = None
                self.rttmonlatestjittererrorsensedescription = None
                self.rttmonlatestjitteroperowsumsd = None
                self.rttmonlatestjitteroperowsum2sd = None
                self.rttmonlatestjitteroperowminsd = None
                self.rttmonlatestjitteroperowmaxsd = None
                self.rttmonlatestjitteroperowsumds = None
                self.rttmonlatestjitteroperowsum2ds = None
                self.rttmonlatestjitteroperowminds = None
                self.rttmonlatestjitteroperowmaxds = None
                self.rttmonlatestjitteropernumofow = None
                self.rttmonlatestjitteropermos = None
                self.rttmonlatestjitteropericpif = None
                self.rttmonlatestjitteroperiajout = None
                self.rttmonlatestjitteroperiajin = None
                self.rttmonlatestjitteroperavgjitter = None
                self.rttmonlatestjitteroperavgsdj = None
                self.rttmonlatestjitteroperavgdsj = None
                self.rttmonlatestjitteroperowavgsd = None
                self.rttmonlatestjitteroperowavgds = None
                self.rttmonlatestjitteroperntpstate = None
                self.rttmonlatestjitteroperunsyncrts = None
                self.rttmonlatestjitteroperrttsumhigh = None
                self.rttmonlatestjitteroperrttsum2high = None
                self.rttmonlatestjitteroperowsumsdhigh = None
                self.rttmonlatestjitteroperowsum2sdhigh = None
                self.rttmonlatestjitteroperowsumdshigh = None
                self.rttmonlatestjitteroperowsum2dshigh = None
                self._segment_path = lambda: "rttMonLatestJitterOperEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLatestJitterOperTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.RttMonLatestJitterOperTable.RttMonLatestJitterOperEntry, ['rttmonctrladminindex', 'rttmonlatestjitteropernumofrtt', 'rttmonlatestjitteroperrttsum', 'rttmonlatestjitteroperrttsum2', 'rttmonlatestjitteroperrttmin', 'rttmonlatestjitteroperrttmax', 'rttmonlatestjitteroperminofpositivessd', 'rttmonlatestjitteropermaxofpositivessd', 'rttmonlatestjitteropernumofpositivessd', 'rttmonlatestjitteropersumofpositivessd', 'rttmonlatestjitteropersum2positivessd', 'rttmonlatestjitteroperminofnegativessd', 'rttmonlatestjitteropermaxofnegativessd', 'rttmonlatestjitteropernumofnegativessd', 'rttmonlatestjitteropersumofnegativessd', 'rttmonlatestjitteropersum2negativessd', 'rttmonlatestjitteroperminofpositivesds', 'rttmonlatestjitteropermaxofpositivesds', 'rttmonlatestjitteropernumofpositivesds', 'rttmonlatestjitteropersumofpositivesds', 'rttmonlatestjitteropersum2positivesds', 'rttmonlatestjitteroperminofnegativesds', 'rttmonlatestjitteropermaxofnegativesds', 'rttmonlatestjitteropernumofnegativesds', 'rttmonlatestjitteropersumofnegativesds', 'rttmonlatestjitteropersum2negativesds', 'rttmonlatestjitteroperpacketlosssd', 'rttmonlatestjitteroperpacketlossds', 'rttmonlatestjitteroperpacketoutofsequence', 'rttmonlatestjitteroperpacketmia', 'rttmonlatestjitteroperpacketlatearrival', 'rttmonlatestjitteropersense', 'rttmonlatestjittererrorsensedescription', 'rttmonlatestjitteroperowsumsd', 'rttmonlatestjitteroperowsum2sd', 'rttmonlatestjitteroperowminsd', 'rttmonlatestjitteroperowmaxsd', 'rttmonlatestjitteroperowsumds', 'rttmonlatestjitteroperowsum2ds', 'rttmonlatestjitteroperowminds', 'rttmonlatestjitteroperowmaxds', 'rttmonlatestjitteropernumofow', 'rttmonlatestjitteropermos', 'rttmonlatestjitteropericpif', 'rttmonlatestjitteroperiajout', 'rttmonlatestjitteroperiajin', 'rttmonlatestjitteroperavgjitter', 'rttmonlatestjitteroperavgsdj', 'rttmonlatestjitteroperavgdsj', 'rttmonlatestjitteroperowavgsd', 'rttmonlatestjitteroperowavgds', 'rttmonlatestjitteroperntpstate', 'rttmonlatestjitteroperunsyncrts', 'rttmonlatestjitteroperrttsumhigh', 'rttmonlatestjitteroperrttsum2high', 'rttmonlatestjitteroperowsumsdhigh', 'rttmonlatestjitteroperowsum2sdhigh', 'rttmonlatestjitteroperowsumdshigh', 'rttmonlatestjitteroperowsum2dshigh'], name, value)

            class RttMonLatestJitterOperNTPState(Enum):
                """
                RttMonLatestJitterOperNTPState (Enum Class)

                A value of sync(1) means sender and responder was in sync

                with NTP. The NTP sync means the total of NTP offset 

                on sender and responder is within configured tolerance level.

                .. data:: sync = 1

                .. data:: outOfSync = 2

                """

                sync = Enum.YLeaf(1, "sync")

                outOfSync = Enum.YLeaf(2, "outOfSync")




    def clone_ptr(self):
        self._top_entity = CISCORTTMONMIB()
        return self._top_entity



