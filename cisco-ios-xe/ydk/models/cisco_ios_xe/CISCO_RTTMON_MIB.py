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
    
    	
    	**type**\:  :py:class:`Rttmonappl <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonappl>`
    
    .. attribute:: rttmonapplsupportedrtttypestable
    
    	A table of which contains the supported Rtt Monitor Types.  See the RttMonRttType textual convention for the definition of each type
    	**type**\:  :py:class:`Rttmonapplsupportedrtttypestable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplsupportedrtttypestable>`
    
    .. attribute:: rttmonapplsupportedprotocolstable
    
    	A table of which contains the supported Rtt Monitor Protocols.  See the RttMonProtocol textual convention  for the definition of each protocol
    	**type**\:  :py:class:`Rttmonapplsupportedprotocolstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplsupportedprotocolstable>`
    
    .. attribute:: rttmonapplpreconfigedtable
    
    	A table of which contains the previously configured Script Names and File IO targets.  These Script Names and File IO targets are installed via a different mechanism than this application, and are specific to each platform
    	**type**\:  :py:class:`Rttmonapplpreconfigedtable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplpreconfigedtable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmonapplauthtable
    
    	A table which contains the definitions for key\-strings that will be used in authenticating RTR Control Protocol
    	**type**\:  :py:class:`Rttmonapplauthtable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplauthtable>`
    
    .. attribute:: rttmonctrladmintable
    
    	A table of Round Trip Time (RTT) monitoring definitions.  The RTT administration control is in multiple tables.   This first table, is used to create a conceptual RTT  control row.  The following tables contain objects which  configure scheduling, information gathering, and  notification/trigger generation.  All of these tables  will create the same conceptual RTT control row as this  table using this tables' index as their own index.   This table is limited in size by the agent  implementation.  The object rttMonApplNumCtrlAdminEntry will reflect this tables maximum number of entries
    	**type**\:  :py:class:`Rttmonctrladmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable>`
    
    .. attribute:: rttmonechoadmintable
    
    	A table that contains Round Trip Time (RTT) specific definitions.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`Rttmonechoadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable>`
    
    .. attribute:: rttmonfileioadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'fileIO' specific definitions.  When the RttMonRttType is not 'fileIO' this table is not valid.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`Rttmonfileioadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonfileioadmintable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmonscriptadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'script' specific definitions.  When the RttMonRttType is not 'script' this table is not valid.  This table is controlled via the rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:  :py:class:`Rttmonscriptadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonscriptadmintable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmonreacttriggeradmintable
    
    	A table of which contains the list of conceptual RTT control rows that will start to collect data when a  reaction condition is violated and when  rttMonReactAdminActionType is set to one of the  following\:   \-  triggerOnly   \-  trapAndTrigger   \-  nmvtAndTrigger   \-  trapNmvtAndTrigger or when a reaction condition is violated and when any of the row in rttMonReactTable has rttMonReactActionType as one of the following\:   \- triggerOnly   \- trapAndTrigger  The goal of this table is to define one or more  additional conceptual RTT control rows that will become active and start to collect additional history and statistics (depending on the rows configuration values), when a problem has been detected.  If the conceptual RTT control row is undefined, and a  trigger occurs, no action will take place.    If the conceptual RTT control row is scheduled to start  at a later time, triggering that row will have no effect.  If the conceptual RTT control row is currently active,  triggering that row will have no effect on that row, but  the rttMonReactTriggerOperState object will transition to  'active'.  An entry in this table can only be triggered when it is not currently in a triggered state.  The object rttMonReactTriggerOperState will  reflect the state of each entry in this table
    	**type**\:  :py:class:`Rttmonreacttriggeradmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttriggeradmintable>`
    
    .. attribute:: rttmonechopathadmintable
    
    	A table to store the hop addresses in a Loose Source Routing path. Response times are computed along the specified path using ping.  This maximum table size is limited by the size of the  maximum number of hop addresses that can fit in an IP header, which is 8. The object rttMonEchoPathAdminEntry will reflect  this tables maximum number of entries.  This table is coupled with rttMonCtrlAdminStatus
    	**type**\:  :py:class:`Rttmonechopathadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechopathadmintable>`
    
    .. attribute:: rttmongrpscheduleadmintable
    
    	A table of Round Trip Time (RTT) monitoring group scheduling specific definitions. This table is used to create a conceptual group scheduling control row. The entries in this control row contain objects used to define group schedule configuration parameters.  The objects of this table will be used to schedule a group of probes identified by the conceptual rows of the rttMonCtrlAdminTable
    	**type**\:  :py:class:`Rttmongrpscheduleadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmongrpscheduleadmintable>`
    
    .. attribute:: rttmplsvpnmonctrltable
    
    	A table of Auto SAA L3 MPLS VPN definitions.  The Auto SAA L3 MPLS VPN administration control is in multiple tables.  This first table, is used to create a conceptual Auto SAA L3 MPLS VPN control row.  The following tables contain objects which used in type specific configurations, scheduling and reaction configurations. All of these tables will create the same conceptual control row as this table using this table's index as their own index.  In order to a row in this table to become active the following objects must be defined.   rttMplsVpnMonCtrlRttType,   rttMplsVpnMonCtrlVrfName and   rttMplsVpnMonSchedulePeriod
    	**type**\:  :py:class:`Rttmplsvpnmonctrltable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable>`
    
    .. attribute:: rttmonreacttable
    
    	A table that contains the reaction configurations. Each conceptual row in rttMonReactTable corresponds to a reaction configured for the probe defined in rttMonCtrlAdminTable.  For each reaction configured for a probe there is an entry in the table.  Each Probe can have multiple reactions and hence there can be multiple rows for a particular probe.  This table is coupled with rttMonCtrlAdminTable
    	**type**\:  :py:class:`Rttmonreacttable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttable>`
    
    .. attribute:: rttmongeneratedopertable
    
    	This table contains information about the generated operation id as part of a parent IP SLA operation. The parent operation id is pseudo\-random number, selected by the management  station based on an operation started by the management  station,when creating a row via the rttMonCtrlAdminStatus object in the rttMonCtrlAdminTable table
    	**type**\:  :py:class:`Rttmongeneratedopertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmongeneratedopertable>`
    
    .. attribute:: rttmonstatscapturetable
    
    	The statistics capture database.  The statistics capture table contains summarized  information of the results for a conceptual RTT control  row.  A rolling accumulated history of this information  is maintained in a series of hourly 'group(s)'.  Each  'group' contains a series of 'path(s)', each 'path'  contains a series of 'hop(s)', each 'hop' contains a  series of 'statistics distribution bucket(s)'.  Each conceptual statistics row has a current hourly  group, into which RTT results are accumulated.  At the  end of each hour a new hourly group is created which  then becomes current.  The counters and accumulators in  the new group are initialized to zero.  The previous  group(s) is kept in the table until the table contains  rttMonStatisticsAdminNumHourGroups groups for the  conceptual statistics row;  at this point, the oldest  group is discarded and is replaced by the newly created  one.  The hourly group is uniquely identified by the  rttMonStatsCaptureStartTimeIndex object.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'inactive', the corresponding current hourly group in  this table is 'frozen', and a new hourly group is  created when activity is resumed.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'pending' this whole table will be cleared and reset to  its initial state.  When the RttMonRttType is 'pathEcho', the path  exploration RTT requests' statistics will not be  accumulated in this table.  NOTE\: When the RttMonRttType is 'pathEcho', a source to        target rttMonStatsCapturePathIndex path will be        created for each rttMonStatsCaptureStartTimeIndex        to hold all errors that occur when a specific path       had not been found or connection has not be setup.  Using this rttMonStatsCaptureTable, a managing  application can retrieve summarized data from accurately  measured periods, which is synchronized across multiple  conceptual RTT control rows.  With the new hourly group creation being performed on a 60 minute period, the  managing station has plenty of time to collect the data,  and need not be concerned with the vagaries of network  delays and lost PDU's when trying to get matching data.   Also, the managing station can spread the data gathering  over a longer period, which removes the need for a flood  of get requests in a short period which otherwise would  occur
    	**type**\:  :py:class:`Rttmonstatscapturetable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable>`
    
    .. attribute:: rttmonstatscollecttable
    
    	The statistics collection database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it does not keep statistical distribution information.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:  :py:class:`Rttmonstatscollecttable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscollecttable>`
    
    .. attribute:: rttmonstatstotalstable
    
    	The statistics totals database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it only keeps 60 minute group values.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:  :py:class:`Rttmonstatstotalstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatstotalstable>`
    
    .. attribute:: rttmonhttpstatstable
    
    	The HTTP statistics collection database.  The HTTP statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table can only  store a maximum of 2 hours of data
    	**type**\:  :py:class:`Rttmonhttpstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonhttpstatstable>`
    
    .. attribute:: rttmonjitterstatstable
    
    	The Jitter statistics collection database.  The Jitter statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table will store  2 hours of data
    	**type**\:  :py:class:`Rttmonjitterstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonjitterstatstable>`
    
    .. attribute:: rttmonlpdgrpstatstable
    
    	The Auto SAA L3 MPLS VPN LPD Group Database.  The LPD Group statistics table contains summarized performance statistics for the LPD group.  LPD Group \- The set of 'single probes' which are subset of the 'lspGroup' probe traversing set of paths between two PE end points are grouped together and called as the LPD group. The LPD group will be uniquely referenced by the LPD Group ID.  A rolling accumulated history of this information is maintained in a series of hourly 'group(s)'.  Each conceptual statistics row has a current hourly group, into which RTT results are accumulated. At the end of each hour a new hourly group is created which then becomes current. The counters and accumulators in the new group are initialized to zero. The previous group(s) is kept in the table until the table contains rttMplsVpnMonTypeLpdStatHours groups for the conceptual statistics row;  at this point, the oldest group is discarded and is replaced by the newly created one. The hourly group is uniquely identified by the rttMonLpdGrpStatsStartTimeIndex object
    	**type**\:  :py:class:`Rttmonlpdgrpstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlpdgrpstatstable>`
    
    .. attribute:: rttmonhistorycollectiontable
    
    	The history collection database.  The history table contains a point by point rolling  history of the most recent RTT operations for each  conceptual RTT control row.  The rolling history of this  information is maintained in a series of 'live(s)', each containing a series of 'bucket(s)', each 'bucket'  contains a series of 'sample(s)'.  Each conceptual history row can have lives.  A life is  defined by the rttMonCtrlOperRttLife object.  A new life  will be created when rttMonCtrlOperState transitions 'active'.  When the number of lives become greater  than rttMonHistoryAdminNumLives the oldest life will be  discarded and a new life will be created by incrementing the index.  The path exploration RTT operation will be kept as an entry in this table
    	**type**\:  :py:class:`Rttmonhistorycollectiontable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonhistorycollectiontable>`
    
    .. attribute:: rttmonlatesthttpopertable
    
    	A table which contains the status of latest HTTP RTT operation
    	**type**\:  :py:class:`Rttmonlatesthttpopertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlatesthttpopertable>`
    
    .. attribute:: rttmonlatestjitteropertable
    
    	A table which contains the status of latest Jitter operation
    	**type**\:  :py:class:`Rttmonlatestjitteropertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlatestjitteropertable>`
    
    

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
        self._child_container_classes = OrderedDict([("rttMonAppl", ("rttmonappl", CISCORTTMONMIB.Rttmonappl)), ("rttMonApplSupportedRttTypesTable", ("rttmonapplsupportedrtttypestable", CISCORTTMONMIB.Rttmonapplsupportedrtttypestable)), ("rttMonApplSupportedProtocolsTable", ("rttmonapplsupportedprotocolstable", CISCORTTMONMIB.Rttmonapplsupportedprotocolstable)), ("rttMonApplPreConfigedTable", ("rttmonapplpreconfigedtable", CISCORTTMONMIB.Rttmonapplpreconfigedtable)), ("rttMonApplAuthTable", ("rttmonapplauthtable", CISCORTTMONMIB.Rttmonapplauthtable)), ("rttMonCtrlAdminTable", ("rttmonctrladmintable", CISCORTTMONMIB.Rttmonctrladmintable)), ("rttMonEchoAdminTable", ("rttmonechoadmintable", CISCORTTMONMIB.Rttmonechoadmintable)), ("rttMonFileIOAdminTable", ("rttmonfileioadmintable", CISCORTTMONMIB.Rttmonfileioadmintable)), ("rttMonScriptAdminTable", ("rttmonscriptadmintable", CISCORTTMONMIB.Rttmonscriptadmintable)), ("rttMonReactTriggerAdminTable", ("rttmonreacttriggeradmintable", CISCORTTMONMIB.Rttmonreacttriggeradmintable)), ("rttMonEchoPathAdminTable", ("rttmonechopathadmintable", CISCORTTMONMIB.Rttmonechopathadmintable)), ("rttMonGrpScheduleAdminTable", ("rttmongrpscheduleadmintable", CISCORTTMONMIB.Rttmongrpscheduleadmintable)), ("rttMplsVpnMonCtrlTable", ("rttmplsvpnmonctrltable", CISCORTTMONMIB.Rttmplsvpnmonctrltable)), ("rttMonReactTable", ("rttmonreacttable", CISCORTTMONMIB.Rttmonreacttable)), ("rttMonGeneratedOperTable", ("rttmongeneratedopertable", CISCORTTMONMIB.Rttmongeneratedopertable)), ("rttMonStatsCaptureTable", ("rttmonstatscapturetable", CISCORTTMONMIB.Rttmonstatscapturetable)), ("rttMonStatsCollectTable", ("rttmonstatscollecttable", CISCORTTMONMIB.Rttmonstatscollecttable)), ("rttMonStatsTotalsTable", ("rttmonstatstotalstable", CISCORTTMONMIB.Rttmonstatstotalstable)), ("rttMonHTTPStatsTable", ("rttmonhttpstatstable", CISCORTTMONMIB.Rttmonhttpstatstable)), ("rttMonJitterStatsTable", ("rttmonjitterstatstable", CISCORTTMONMIB.Rttmonjitterstatstable)), ("rttMonLpdGrpStatsTable", ("rttmonlpdgrpstatstable", CISCORTTMONMIB.Rttmonlpdgrpstatstable)), ("rttMonHistoryCollectionTable", ("rttmonhistorycollectiontable", CISCORTTMONMIB.Rttmonhistorycollectiontable)), ("rttMonLatestHTTPOperTable", ("rttmonlatesthttpopertable", CISCORTTMONMIB.Rttmonlatesthttpopertable)), ("rttMonLatestJitterOperTable", ("rttmonlatestjitteropertable", CISCORTTMONMIB.Rttmonlatestjitteropertable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.rttmonappl = CISCORTTMONMIB.Rttmonappl()
        self.rttmonappl.parent = self
        self._children_name_map["rttmonappl"] = "rttMonAppl"
        self._children_yang_names.add("rttMonAppl")

        self.rttmonapplsupportedrtttypestable = CISCORTTMONMIB.Rttmonapplsupportedrtttypestable()
        self.rttmonapplsupportedrtttypestable.parent = self
        self._children_name_map["rttmonapplsupportedrtttypestable"] = "rttMonApplSupportedRttTypesTable"
        self._children_yang_names.add("rttMonApplSupportedRttTypesTable")

        self.rttmonapplsupportedprotocolstable = CISCORTTMONMIB.Rttmonapplsupportedprotocolstable()
        self.rttmonapplsupportedprotocolstable.parent = self
        self._children_name_map["rttmonapplsupportedprotocolstable"] = "rttMonApplSupportedProtocolsTable"
        self._children_yang_names.add("rttMonApplSupportedProtocolsTable")

        self.rttmonapplpreconfigedtable = CISCORTTMONMIB.Rttmonapplpreconfigedtable()
        self.rttmonapplpreconfigedtable.parent = self
        self._children_name_map["rttmonapplpreconfigedtable"] = "rttMonApplPreConfigedTable"
        self._children_yang_names.add("rttMonApplPreConfigedTable")

        self.rttmonapplauthtable = CISCORTTMONMIB.Rttmonapplauthtable()
        self.rttmonapplauthtable.parent = self
        self._children_name_map["rttmonapplauthtable"] = "rttMonApplAuthTable"
        self._children_yang_names.add("rttMonApplAuthTable")

        self.rttmonctrladmintable = CISCORTTMONMIB.Rttmonctrladmintable()
        self.rttmonctrladmintable.parent = self
        self._children_name_map["rttmonctrladmintable"] = "rttMonCtrlAdminTable"
        self._children_yang_names.add("rttMonCtrlAdminTable")

        self.rttmonechoadmintable = CISCORTTMONMIB.Rttmonechoadmintable()
        self.rttmonechoadmintable.parent = self
        self._children_name_map["rttmonechoadmintable"] = "rttMonEchoAdminTable"
        self._children_yang_names.add("rttMonEchoAdminTable")

        self.rttmonfileioadmintable = CISCORTTMONMIB.Rttmonfileioadmintable()
        self.rttmonfileioadmintable.parent = self
        self._children_name_map["rttmonfileioadmintable"] = "rttMonFileIOAdminTable"
        self._children_yang_names.add("rttMonFileIOAdminTable")

        self.rttmonscriptadmintable = CISCORTTMONMIB.Rttmonscriptadmintable()
        self.rttmonscriptadmintable.parent = self
        self._children_name_map["rttmonscriptadmintable"] = "rttMonScriptAdminTable"
        self._children_yang_names.add("rttMonScriptAdminTable")

        self.rttmonreacttriggeradmintable = CISCORTTMONMIB.Rttmonreacttriggeradmintable()
        self.rttmonreacttriggeradmintable.parent = self
        self._children_name_map["rttmonreacttriggeradmintable"] = "rttMonReactTriggerAdminTable"
        self._children_yang_names.add("rttMonReactTriggerAdminTable")

        self.rttmonechopathadmintable = CISCORTTMONMIB.Rttmonechopathadmintable()
        self.rttmonechopathadmintable.parent = self
        self._children_name_map["rttmonechopathadmintable"] = "rttMonEchoPathAdminTable"
        self._children_yang_names.add("rttMonEchoPathAdminTable")

        self.rttmongrpscheduleadmintable = CISCORTTMONMIB.Rttmongrpscheduleadmintable()
        self.rttmongrpscheduleadmintable.parent = self
        self._children_name_map["rttmongrpscheduleadmintable"] = "rttMonGrpScheduleAdminTable"
        self._children_yang_names.add("rttMonGrpScheduleAdminTable")

        self.rttmplsvpnmonctrltable = CISCORTTMONMIB.Rttmplsvpnmonctrltable()
        self.rttmplsvpnmonctrltable.parent = self
        self._children_name_map["rttmplsvpnmonctrltable"] = "rttMplsVpnMonCtrlTable"
        self._children_yang_names.add("rttMplsVpnMonCtrlTable")

        self.rttmonreacttable = CISCORTTMONMIB.Rttmonreacttable()
        self.rttmonreacttable.parent = self
        self._children_name_map["rttmonreacttable"] = "rttMonReactTable"
        self._children_yang_names.add("rttMonReactTable")

        self.rttmongeneratedopertable = CISCORTTMONMIB.Rttmongeneratedopertable()
        self.rttmongeneratedopertable.parent = self
        self._children_name_map["rttmongeneratedopertable"] = "rttMonGeneratedOperTable"
        self._children_yang_names.add("rttMonGeneratedOperTable")

        self.rttmonstatscapturetable = CISCORTTMONMIB.Rttmonstatscapturetable()
        self.rttmonstatscapturetable.parent = self
        self._children_name_map["rttmonstatscapturetable"] = "rttMonStatsCaptureTable"
        self._children_yang_names.add("rttMonStatsCaptureTable")

        self.rttmonstatscollecttable = CISCORTTMONMIB.Rttmonstatscollecttable()
        self.rttmonstatscollecttable.parent = self
        self._children_name_map["rttmonstatscollecttable"] = "rttMonStatsCollectTable"
        self._children_yang_names.add("rttMonStatsCollectTable")

        self.rttmonstatstotalstable = CISCORTTMONMIB.Rttmonstatstotalstable()
        self.rttmonstatstotalstable.parent = self
        self._children_name_map["rttmonstatstotalstable"] = "rttMonStatsTotalsTable"
        self._children_yang_names.add("rttMonStatsTotalsTable")

        self.rttmonhttpstatstable = CISCORTTMONMIB.Rttmonhttpstatstable()
        self.rttmonhttpstatstable.parent = self
        self._children_name_map["rttmonhttpstatstable"] = "rttMonHTTPStatsTable"
        self._children_yang_names.add("rttMonHTTPStatsTable")

        self.rttmonjitterstatstable = CISCORTTMONMIB.Rttmonjitterstatstable()
        self.rttmonjitterstatstable.parent = self
        self._children_name_map["rttmonjitterstatstable"] = "rttMonJitterStatsTable"
        self._children_yang_names.add("rttMonJitterStatsTable")

        self.rttmonlpdgrpstatstable = CISCORTTMONMIB.Rttmonlpdgrpstatstable()
        self.rttmonlpdgrpstatstable.parent = self
        self._children_name_map["rttmonlpdgrpstatstable"] = "rttMonLpdGrpStatsTable"
        self._children_yang_names.add("rttMonLpdGrpStatsTable")

        self.rttmonhistorycollectiontable = CISCORTTMONMIB.Rttmonhistorycollectiontable()
        self.rttmonhistorycollectiontable.parent = self
        self._children_name_map["rttmonhistorycollectiontable"] = "rttMonHistoryCollectionTable"
        self._children_yang_names.add("rttMonHistoryCollectionTable")

        self.rttmonlatesthttpopertable = CISCORTTMONMIB.Rttmonlatesthttpopertable()
        self.rttmonlatesthttpopertable.parent = self
        self._children_name_map["rttmonlatesthttpopertable"] = "rttMonLatestHTTPOperTable"
        self._children_yang_names.add("rttMonLatestHTTPOperTable")

        self.rttmonlatestjitteropertable = CISCORTTMONMIB.Rttmonlatestjitteropertable()
        self.rttmonlatestjitteropertable.parent = self
        self._children_name_map["rttmonlatestjitteropertable"] = "rttMonLatestJitterOperTable"
        self._children_yang_names.add("rttMonLatestJitterOperTable")
        self._segment_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB"


    class Rttmonappl(Entity):
        """
        
        
        .. attribute:: rttmonapplversion
        
        	Round Trip Time monitoring application version string.  The format will be\:  'Version.Release.Patch\-Level\: Textual\-Description'  For example\:  '1.0.0\: Initial RTT Application'
        	**type**\: str
        
        .. attribute:: rttmonapplmaxpacketdatasize
        
        	The maximum size of the data portion an echo packet supported by this RTT application.  This is the maximum value that can be specified by (rttMonEchoAdminPktDataRequestSize + ARR Header) or  (rttMonEchoAdminPktDataResponseSize + ARR Header) in the rttMonCtrlAdminTable.  This object is undefined for conceptual RTT  control rows when the RttMonRttType object is set to 'fileIO' or 'script'
        	**type**\: int
        
        	**range:** 0..16384
        
        	**units**\: octets
        
        .. attribute:: rttmonappltimeoflastset
        
        	The last time at which a set operation occurred on any of the objects in this MIB.  The managing  application can inspect this value in order to  determine whether changes have been made without  retrieving the entire Administration portion of this MIB.  This object applies to all settable objects in this MIB, including the 'Reset' objects that could clear saved history/statistics
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rttmonapplnumctrladminentry
        
        	This object defines the maximum number of entries that can be added to the rttMonCtrlAdminTable. It is calculated at the system init time. The value is impacted when rttMonApplFreeMemLowWaterMark is changed
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: rttmonapplreset
        
        	When set to 'reset' the entire RTT application goes through a reset sequence, making a best  effort to revert to its startup condition.  Any  and all rows in the Overall Control Group will be immediately deleted, together with any associated rows in the Statistics Collection Group, and  History Collection Group.  All open connections  will also be closed.  Finally the  rttMonApplPreConfigedTable will reset (see  rttMonApplPreConfigedReset)
        	**type**\:  :py:class:`RttReset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttReset>`
        
        .. attribute:: rttmonapplpreconfigedreset
        
        	When set to 'reset' the RTT application will reset the Application Preconfigured MIB section.  This will force the RTT application to delete all entries in the rttMonApplPreConfigedTable and then to repopulate the table with the current configuration.  This provides a mechanism to load and unload user scripts and file paths
        	**type**\:  :py:class:`RttReset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttReset>`
        
        	**status**\: obsolete
        
        .. attribute:: rttmonapplprobecapacity
        
        	This object defines the number of new probes that can be configured on a router. The number depends on the value  of rttMonApplFreeMemLowWaterMark, free bytes available on the router and the system configured rttMonCtrlAdminEntry number. Equation\: rttMonApplProbeCapacity =  MIN(((Free\_Bytes\_on\_the\_Router \- rttMonApplFreeMemLowWaterMark)/ Memory\_required\_by\_each\_probe), rttMonApplNumCtrlAdminEntry \-  Num\_of\_Probes\_already\_configured))
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: rttmonapplfreememlowwatermark
        
        	This object defines the amount of free memory a router must have in order to configure RTR. If RTR found out that the memory is falling below this mark, it will not allow new probes to be configured.  This value should not be set higher (or very close to) than  the free bytes available on the router
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: rttmonappllatestseterror
        
        	An error description for the last error message caused by set.  Currently, it includes set error caused due to setting rttMonApplFreeMemLowWaterMark greater than the available free memory on the router or not enough memory left to create new probes
        	**type**\: str
        
        .. attribute:: rttmonapplresponder
        
        	Enable or disable RTR responder on the router
        	**type**\: bool
        
        .. attribute:: rttmonappllpdgrpstatsreset
        
        	This object is used to reset certain objects within the rttMonLpdGrpStatsTable.  When the object is set to value of an active LPD Group identifier the associated objects will be reset. The reset objects will be set to a value as specified in the object's description.  The following objects will not be reset. \- rttMonLpdGrpStatsTargetPE \- rttMonLpdGrpStatsGroupProbeIndex \- rttMonLpdGrpStatsGroupIndex \- rttMonLpdGrpStatsStartTimeIndex
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonappl, self).__init__()

            self.yang_name = "rttMonAppl"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('rttmonapplversion', YLeaf(YType.str, 'rttMonApplVersion')),
                ('rttmonapplmaxpacketdatasize', YLeaf(YType.int32, 'rttMonApplMaxPacketDataSize')),
                ('rttmonappltimeoflastset', YLeaf(YType.uint32, 'rttMonApplTimeOfLastSet')),
                ('rttmonapplnumctrladminentry', YLeaf(YType.int32, 'rttMonApplNumCtrlAdminEntry')),
                ('rttmonapplreset', YLeaf(YType.enumeration, 'rttMonApplReset')),
                ('rttmonapplpreconfigedreset', YLeaf(YType.enumeration, 'rttMonApplPreConfigedReset')),
                ('rttmonapplprobecapacity', YLeaf(YType.int32, 'rttMonApplProbeCapacity')),
                ('rttmonapplfreememlowwatermark', YLeaf(YType.int32, 'rttMonApplFreeMemLowWaterMark')),
                ('rttmonappllatestseterror', YLeaf(YType.str, 'rttMonApplLatestSetError')),
                ('rttmonapplresponder', YLeaf(YType.boolean, 'rttMonApplResponder')),
                ('rttmonappllpdgrpstatsreset', YLeaf(YType.int32, 'rttMonApplLpdGrpStatsReset')),
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

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonappl, ['rttmonapplversion', 'rttmonapplmaxpacketdatasize', 'rttmonappltimeoflastset', 'rttmonapplnumctrladminentry', 'rttmonapplreset', 'rttmonapplpreconfigedreset', 'rttmonapplprobecapacity', 'rttmonapplfreememlowwatermark', 'rttmonappllatestseterror', 'rttmonapplresponder', 'rttmonappllpdgrpstatsreset'], name, value)


    class Rttmonapplsupportedrtttypestable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Types.
        
        See the RttMonRttType textual convention for
        the definition of each type.
        
        .. attribute:: rttmonapplsupportedrtttypesentry
        
        	A list that presents the valid Rtt Monitor Types
        	**type**\: list of  		 :py:class:`Rttmonapplsupportedrtttypesentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonapplsupportedrtttypestable, self).__init__()

            self.yang_name = "rttMonApplSupportedRttTypesTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonApplSupportedRttTypesEntry", ("rttmonapplsupportedrtttypesentry", CISCORTTMONMIB.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry))])
            self._leafs = OrderedDict()

            self.rttmonapplsupportedrtttypesentry = YList(self)
            self._segment_path = lambda: "rttMonApplSupportedRttTypesTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonapplsupportedrtttypestable, [], name, value)


        class Rttmonapplsupportedrtttypesentry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Types.
            
            .. attribute:: rttmonapplsupportedrtttypes  (key)
            
            	This object indexes the supported 'RttMonRttType' types
            	**type**\:  :py:class:`RttMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonRttType>`
            
            .. attribute:: rttmonapplsupportedrtttypesvalid
            
            	This object defines the supported 'RttMonRttType' types
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry, self).__init__()

                self.yang_name = "rttMonApplSupportedRttTypesEntry"
                self.yang_parent_name = "rttMonApplSupportedRttTypesTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplsupportedrtttypes']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplsupportedrtttypes', YLeaf(YType.enumeration, 'rttMonApplSupportedRttTypes')),
                    ('rttmonapplsupportedrtttypesvalid', YLeaf(YType.boolean, 'rttMonApplSupportedRttTypesValid')),
                ])
                self.rttmonapplsupportedrtttypes = None
                self.rttmonapplsupportedrtttypesvalid = None
                self._segment_path = lambda: "rttMonApplSupportedRttTypesEntry" + "[rttMonApplSupportedRttTypes='" + str(self.rttmonapplsupportedrtttypes) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedRttTypesTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry, ['rttmonapplsupportedrtttypes', 'rttmonapplsupportedrtttypesvalid'], name, value)


    class Rttmonapplsupportedprotocolstable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Protocols.
        
        See the RttMonProtocol textual convention 
        for the definition of each protocol.
        
        .. attribute:: rttmonapplsupportedprotocolsentry
        
        	A list that presents the valid Rtt Monitor Protocols
        	**type**\: list of  		 :py:class:`Rttmonapplsupportedprotocolsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonapplsupportedprotocolstable, self).__init__()

            self.yang_name = "rttMonApplSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonApplSupportedProtocolsEntry", ("rttmonapplsupportedprotocolsentry", CISCORTTMONMIB.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry))])
            self._leafs = OrderedDict()

            self.rttmonapplsupportedprotocolsentry = YList(self)
            self._segment_path = lambda: "rttMonApplSupportedProtocolsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonapplsupportedprotocolstable, [], name, value)


        class Rttmonapplsupportedprotocolsentry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Protocols.
            
            .. attribute:: rttmonapplsupportedprotocols  (key)
            
            	This object indexes the supported 'RttMonProtocol' protocols
            	**type**\:  :py:class:`RttMonProtocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonProtocol>`
            
            .. attribute:: rttmonapplsupportedprotocolsvalid
            
            	This object defines the supported 'RttMonProtocol' protocols
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry, self).__init__()

                self.yang_name = "rttMonApplSupportedProtocolsEntry"
                self.yang_parent_name = "rttMonApplSupportedProtocolsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplsupportedprotocols']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplsupportedprotocols', YLeaf(YType.enumeration, 'rttMonApplSupportedProtocols')),
                    ('rttmonapplsupportedprotocolsvalid', YLeaf(YType.boolean, 'rttMonApplSupportedProtocolsValid')),
                ])
                self.rttmonapplsupportedprotocols = None
                self.rttmonapplsupportedprotocolsvalid = None
                self._segment_path = lambda: "rttMonApplSupportedProtocolsEntry" + "[rttMonApplSupportedProtocols='" + str(self.rttmonapplsupportedprotocols) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedProtocolsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry, ['rttmonapplsupportedprotocols', 'rttmonapplsupportedprotocolsvalid'], name, value)


    class Rttmonapplpreconfigedtable(Entity):
        """
        A table of which contains the previously
        configured Script Names and File IO targets.
        
        These Script Names and File IO targets are installed
        via a different mechanism than this application, and
        are specific to each platform.
        
        .. attribute:: rttmonapplpreconfigedentry
        
        	A list of objects that describe the previously configured Script Names and File IO targets
        	**type**\: list of  		 :py:class:`Rttmonapplpreconfigedentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonapplpreconfigedtable, self).__init__()

            self.yang_name = "rttMonApplPreConfigedTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonApplPreConfigedEntry", ("rttmonapplpreconfigedentry", CISCORTTMONMIB.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry))])
            self._leafs = OrderedDict()

            self.rttmonapplpreconfigedentry = YList(self)
            self._segment_path = lambda: "rttMonApplPreConfigedTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonapplpreconfigedtable, [], name, value)


        class Rttmonapplpreconfigedentry(Entity):
            """
            A list of objects that describe the previously
            configured Script Names and File IO targets.
            
            .. attribute:: rttmonapplpreconfigedtype  (key)
            
            	This is the type of value being stored in the rttMonApplPreConfigedName object
            	**type**\:  :py:class:`Rttmonapplpreconfigedtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry.Rttmonapplpreconfigedtype>`
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedname  (key)
            
            	This is either one of the following depending on the value of the rttMonApplPreConfigedType object\:   \- The file path to a server.  One of these file paths     must be used when defining an entry in the     rttMonFileIOAdminTable table with 'fileIO' as the     value of the rttMonCtrlAdminRttType object.   \- The script name to be used when generating RTT     operations.  One of these script names must be used     when defining an entry in the rttMonScriptAdminTable     table with 'script' as the value of the     rttMonCtrlAdminRttType object.  NOTE\:  For script names, command line parameters         can follow these names in the         rttMonScriptAdminTable table
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedvalid
            
            	When this row exists, this value will be 'true'. This object exists only to create a valid row in this  table
            	**type**\: bool
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry, self).__init__()

                self.yang_name = "rttMonApplPreConfigedEntry"
                self.yang_parent_name = "rttMonApplPreConfigedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplpreconfigedtype','rttmonapplpreconfigedname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplpreconfigedtype', YLeaf(YType.enumeration, 'rttMonApplPreConfigedType')),
                    ('rttmonapplpreconfigedname', YLeaf(YType.str, 'rttMonApplPreConfigedName')),
                    ('rttmonapplpreconfigedvalid', YLeaf(YType.boolean, 'rttMonApplPreConfigedValid')),
                ])
                self.rttmonapplpreconfigedtype = None
                self.rttmonapplpreconfigedname = None
                self.rttmonapplpreconfigedvalid = None
                self._segment_path = lambda: "rttMonApplPreConfigedEntry" + "[rttMonApplPreConfigedType='" + str(self.rttmonapplpreconfigedtype) + "']" + "[rttMonApplPreConfigedName='" + str(self.rttmonapplpreconfigedname) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplPreConfigedTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry, ['rttmonapplpreconfigedtype', 'rttmonapplpreconfigedname', 'rttmonapplpreconfigedvalid'], name, value)

            class Rttmonapplpreconfigedtype(Enum):
                """
                Rttmonapplpreconfigedtype (Enum Class)

                This is the type of value being stored in the

                rttMonApplPreConfigedName object.

                .. data:: filePath = 1

                .. data:: scriptName = 2

                """

                filePath = Enum.YLeaf(1, "filePath")

                scriptName = Enum.YLeaf(2, "scriptName")



    class Rttmonapplauthtable(Entity):
        """
        A table which contains the definitions for key\-strings
        that will be used in authenticating RTR Control Protocol.
        
        .. attribute:: rttmonapplauthentry
        
        	A list that presents the valid parameters for Authenticating RTR Control Protocol
        	**type**\: list of  		 :py:class:`Rttmonapplauthentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonapplauthtable.Rttmonapplauthentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonapplauthtable, self).__init__()

            self.yang_name = "rttMonApplAuthTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonApplAuthEntry", ("rttmonapplauthentry", CISCORTTMONMIB.Rttmonapplauthtable.Rttmonapplauthentry))])
            self._leafs = OrderedDict()

            self.rttmonapplauthentry = YList(self)
            self._segment_path = lambda: "rttMonApplAuthTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonapplauthtable, [], name, value)


        class Rttmonapplauthentry(Entity):
            """
            A list that presents the valid parameters for Authenticating
            RTR Control Protocol.
            
            .. attribute:: rttmonapplauthindex  (key)
            
            	Uniquely identifies a row in the rttMonApplAuthTable. This is a pseudo\-random number selected by the management station when creating a row via the rttMonApplAuthStatus  object. If the pseudo\-random number is already in use, an  'inconsistentValue' is returned. Currently, only one row  can be created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonapplauthkeychain
            
            	A string which represents the key\-chain name. If multiple key\-strings are specified, then the authenticator will  alternate between the specified strings
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring1
            
            	A string which represents a key\-string name whose id is 1
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring2
            
            	A string which represents a key\-string name whose id is 2
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring3
            
            	A string which represents a key\-string name whose id is 3
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring4
            
            	A string which represents a key\-string name whose id is 4
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring5
            
            	A string which represents a key\-string name whose id is 5
            	**type**\: str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthstatus
            
            	The status of the Authentication row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonapplauthtable.Rttmonapplauthentry, self).__init__()

                self.yang_name = "rttMonApplAuthEntry"
                self.yang_parent_name = "rttMonApplAuthTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonapplauthindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonapplauthindex', YLeaf(YType.int32, 'rttMonApplAuthIndex')),
                    ('rttmonapplauthkeychain', YLeaf(YType.str, 'rttMonApplAuthKeyChain')),
                    ('rttmonapplauthkeystring1', YLeaf(YType.str, 'rttMonApplAuthKeyString1')),
                    ('rttmonapplauthkeystring2', YLeaf(YType.str, 'rttMonApplAuthKeyString2')),
                    ('rttmonapplauthkeystring3', YLeaf(YType.str, 'rttMonApplAuthKeyString3')),
                    ('rttmonapplauthkeystring4', YLeaf(YType.str, 'rttMonApplAuthKeyString4')),
                    ('rttmonapplauthkeystring5', YLeaf(YType.str, 'rttMonApplAuthKeyString5')),
                    ('rttmonapplauthstatus', YLeaf(YType.enumeration, 'rttMonApplAuthStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonapplauthtable.Rttmonapplauthentry, ['rttmonapplauthindex', 'rttmonapplauthkeychain', 'rttmonapplauthkeystring1', 'rttmonapplauthkeystring2', 'rttmonapplauthkeystring3', 'rttmonapplauthkeystring4', 'rttmonapplauthkeystring5', 'rttmonapplauthstatus'], name, value)


    class Rttmonctrladmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonctrladminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonctrladmintable, self).__init__()

            self.yang_name = "rttMonCtrlAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonCtrlAdminEntry", ("rttmonctrladminentry", CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry))])
            self._leafs = OrderedDict()

            self.rttmonctrladminentry = YList(self)
            self._segment_path = lambda: "rttMonCtrlAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonctrladmintable, [], name, value)


        class Rttmonctrladminentry(Entity):
            """
            A base list of objects that define a conceptual RTT
            control row.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	Uniquely identifies a row in the rttMonCtrlAdminTable. This is a pseudo\-random number, selected by the management  station or auto\-generated based on  operation started by the  management station,when creating a row via  the rttMonCtrlAdminStatus object.  If the pseudo\-random   number is already in use an 'inconsistentValue' return code   will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonctrladminowner
            
            	Identifies the entity that created this table row
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: rttmonctrladmintag
            
            	A string which is used by a managing application to identify the RTT target.  This string is inserted into trap notifications, but has no other significance to the  agent
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: rttmonctrladminrtttype
            
            	The type of RTT operation to be performed.  This value must be set in the same PDU or before setting any type specific configuration.  Note\: The RTT operation 'lspGroup' cannot be created via this control row. It will be created automatically by Auto SAA L3 MPLS VPN when rttMplsVpnMonCtrlLpd is 'true'
            	**type**\:  :py:class:`RttMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonRttType>`
            
            .. attribute:: rttmonctrladminthreshold
            
            	This object defines an administrative threshold limit. If the RTT operation time exceeds this limit and if the  conditions specified in rttMonReactAdminThresholdType or  rttMonHistoryAdminFilter are satisfied, a threshold is generated
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladminfrequency
            
            	Specifies the duration between initiating each RTT operation.   This object cannot be set to a value which would be a  shorter duration than rttMonCtrlAdminTimeout.  When the RttMonRttType specifies an operation that is synchronous in nature, it may happen that the next RTT  operation is blocked by a RTT operation which has not yet completed.  In this case, the value of a counter (rttMonStatsCollectBusies) in rttMonStatsCaptureTable is incremented in lieu of initiating a RTT operation, and  the next attempt will occur at the next rttMonCtrlAdminFrequency expiration.   NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'pathEcho', setting this value to a small        value for your network size may cause an operation        attempt (or multiple attempts) to be started         before the previous operation has finished.  In         this situation the rttMonStatsCollectBusies object        will be incremented in lieu of initiating a new         RTT operation, and the next attempt will occur at        the next rttMonCtrlAdminFrequency expiration.  When the rttMonCtrlAdminRttType object is defined to be 'pathEcho', the suggested value for this object  is greater than rttMonCtrlAdminTimeout times the  maximum number of expected hops to the target.  NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'dhcp', the minimum allowed value for this        object is 10 seconds.  This restriction is due to        protocol limitations described in RFC 2131
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrladmintimeout
            
            	Specifies the duration to wait for a RTT operation completion.  The value of this object cannot be set to  a value which would specify a duration exceeding  rttMonCtrlAdminFrequency.  For connection oriented protocols, this may cause the connection to be closed by the probe.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladminverifydata
            
            	When set to true, the resulting data in each RTT operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object.  Some RttMonRttTypes may not support this option.  When a type does not support this option, the agent will  transition this object to false.  It is the management applications responsibility to check for this  transition
            	**type**\: bool
            
            .. attribute:: rttmonctrladminstatus
            
            	The status of the conceptual RTT control row.  In order for this object to become active, the following  row objects must be defined\:    \- rttMonCtrlAdminRttType Additionally\:  \- for echo, pathEcho based on 'ipIcmpEcho' and dlsw probes     rttMonEchoAdminProtocol and      rttMonEchoAdminTargetAddress;  \- for echo, pathEcho based on 'mplsLspPingAppl'     rttMonEchoAdminProtocol, rttMonEchoAdminTargetAddress      and rttMonEchoAdminLSPFECType  \- for udpEcho, tcpConnect and jitter probes     rttMonEchoAdminTargetAddress and     rttMonEchoAdminTargetPort  \- for http and ftp probe     rttMonEchoAdminURL   \- for dns probe     rttMonEchoAdminTargetAddressString      rttMonEchoAdminNameServer   \- dhcp probe doesn't require any additional objects  All other objects can assume default values. The  conceptual Rtt control row will be placed into a  'pending' state (via the rttMonCtrlOperState object) if rttMonScheduleAdminRttStartTime is not specified.  Most conceptual Rtt control row objects cannot be  modified once this conceptual Rtt control row has been  created.  The objects that can change are the following\:   \- Objects in the rttMonReactAdminTable can be modified    as needed without setting this object to     'notInService'.  \- Objects in the rttMonScheduleAdminTable can be     modified only when this object has the value of    'notInService'.  \- The rttMonCtrlOperState can be modified to control    the state of the probe.  Once this object is in 'active' status, it cannot be  set to 'notInService' while the rttMonCtrlOperState is in 'active' state.  Thus the rttMonCtrlOperState  object must be transitioned first.   This object can be set to 'destroy' from any value at any time
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rttmonctrladminnvgen
            
            	When set to true, this entry will be shown in 'show running' command and can be saved into Non\-volatile memory
            	**type**\: bool
            
            .. attribute:: rttmonctrladmingroupname
            
            	If the operation is created through auto measure group creation, then this string will specify the group name to which this operation is associated
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: rttmonscheduleadminrttlife
            
            	This object value will be placed into the rttMonCtrlOperRttLife object when the rttMonCtrlOperState object transitions to 'active' or 'pending'.  The value 2147483647 has a special meaning.  When this object is set to 2147483647, the  rttMonCtrlOperRttLife object will not decrement.   And thus the life time will never end
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmonscheduleadminrttstarttime
            
            	This is the time when this conceptional row will activate.    This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will  cause the activation of a conceptual Rtt row.  When an agent has the capability to determine date and  time, the agent should store this object as DateAndTime. This allows the agent to completely reset (restart) and still be able to start conceptual Rtt rows at the  intended time.  If the agent cannot keep date and time and the agent resets, all entries should take on one of the special value defined below.  The first special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'active' state when the rttMonCtrlAdminStatus  object transitions to active. This special value is defined to be a value of this object that, when initially set, is 1.  The second special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'pending' state when  the rttMonCtrlAdminStatus object transitions to active.   Also, when the rttMonCtrlOperRttLife counts down to zero  (and not when set to zero), this special value causes  this conceptual Rtt control row to  retransition the  rttMonCtrlOperState object into 'pending' state.  This  special value is defined to be a value of this object  that, when initially set, is smaller than the current sysUpTime. (With the exception of one, as defined in the previous paragraph)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonscheduleadminconceptrowageout
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active'  state, this timer will be reset and suspended.  When  this conceptual RTT control row enters a state other  than 'active', the timer will be restarted.  NOTE\:  When a conceptual Rtt control row ages out, the         agent needs to remove the associated entries in         the rttMonReactTriggerAdminTable and         rttMonReactTriggerOperTable.  When this value is set to zero, this entry will never be aged out. rttMonScheduleAdminConceptRowAgeout object is superseded by rttMonScheduleAdminConceptRowAgeoutV2
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonscheduleadminrttrecurring
            
            	When set to true, this entry will be scheduled to run automatically for the specified duration equal to the life configured, at the same time daily.  This value cannot be set to true  (a) if rttMonScheduleAdminRttLife object has value greater or    equal to 86400 seconds. (b) if sum of values of rttMonScheduleAdminRttLife and    rttMonScheduleAdminConceptRowAgeout is less or equal to    86400 seconds
            	**type**\: bool
            
            .. attribute:: rttmonscheduleadminconceptrowageoutv2
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active' state, this timer will be reset and suspended.  When this conceptual RTT control row enters a state other than 'active', the timer will be restarted.  NOTE\:  It is the same as rttMonScheduleAdminConceptRowAgeout        except DEFVAL is 0 to be consistent with CLI ageout        default.  When this value is set to zero, this entry will never be aged out
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: rttmonreactadminconnectionenable
            
            	If true, a reaction is generated when a RTT operation to a rttMonEchoAdminTargetAddress (echo type) causes  rttMonCtrlOperConnectionLostOccurred to change its  value.  Thus connections to intermediate hops will  not cause this value to change. rttMonReactAdminConnectionEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadmintimeoutenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperTimeoutOccurred  to change its value.    When the RttMonRttType is 'pathEcho' timeouts to  intermediate hops will not cause  rttMonCtrlOperTimeoutOccurred to change its value. rttMonReactAdminTimeoutEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdtype
            
            	This object specifies the conditions under which rttMonCtrlOperOverThresholdOccurred is changed\:  NOTE\:  When the RttMonRttType is 'pathEcho' this         objects' value and all associated         object values are only valid when RTT         'echo' operations are to the        rttMonEchoAdminTargetAddress object address.  Thus        'pathEcho' operations to intermediate        hops will not cause this object to change.  never       \- rttMonCtrlOperOverThresholdOccurred is                 never set immediate   \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold;                 conversely                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                 falls below                 rttMonReactAdminThresholdFalling  consecutive \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold on                 rttMonReactAdminThresholdCount consecutive                 RTT operations; conversely,                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                falls under the                 rttMonReactAdminThresholdFalling                 for the same number of consecutive                 operations  xOfy        \- rttMonCtrlOperOverThresholdOccurred is set                 to true when x (as specified by                 rttMonReactAdminThresholdCount) out of the                 last y (as specified by                 rttMonReactAdminThresholdCount2)                 operation completion time exceeds                 rttMonCtrlAdminThreshold;                 conversely, it is set to false when x,                 out of the last y operation completion                time fall below                rttMonReactAdminThresholdFalling                NOTE\: When x > y, the probe will never                      generate a reaction. average     \- rttMonCtrlOperOverThresholdOccurred is set                 to true when the running average of the                 previous rttMonReactAdminThresholdCount                 operation completion times exceed                 rttMonCtrlAdminThreshold; conversely, it                 is set to false when the running average                 falls below the                 rttMonReactAdminThresholdFalling  If this value is changed by a management station,  rttMonCtrlOperOverThresholdOccurred is set to false, but  no reaction is generated if the prior value of  rttMonCtrlOperOverThresholdOccurred was true. rttMonReactAdminThresholdType object is superseded by rttMonReactThresholdType
            	**type**\:  :py:class:`Rttmonreactadminthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonreactadminthresholdtype>`
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdfalling
            
            	This object defines a threshold limit. If the RTT operation time falls below this limit and if the conditions specified in rttMonReactAdminThresholdType are satisfied, an  threshold is generated. rttMonReactAdminThresholdFalling object is superseded by rttMonReactThresholdFalling
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount
            
            	This object defines the 'x' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount object is superseded by rttMonReactThresholdCountX
            	**type**\: int
            
            	**range:** 1..16
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount2
            
            	This object defines the 'y' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount2 object is superseded by rttMonReactThresholdCountyY
            	**type**\: int
            
            	**range:** 1..16
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched  conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated nmvtOnly           \- an SNA NMVT is generated triggerOnly        \- all trigger actions defined for this                        entry are initiated trapAndNmvt        \- both a trap and an SNA NMVT are                        generated trapAndTrigger     \- both a trap and all trigger actions                        are initiated  nmvtAndTrigger     \- both a NMVT and all trigger actions                        are initiated trapNmvtAndTrigger \- a NMVT, trap, and all trigger actions                       are initiated  A trigger action is defined via the  rttMonReactTriggerAdminTable. rttMonReactAdminActionType object is superseded by rttMonReactActionType
            	**type**\:  :py:class:`Rttmonreactadminactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonreactadminactiontype>`
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminverifyerrorenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperVerifyErrorOccurred  to change its value. rttMonReactAdminVerifyErrorEnable object is superseded by rttMonReactVar
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatisticsadminnumhourgroups
            
            	The maximum number of groups of paths to record. Specifically this is the number of hourly groups  to keep before rolling over.    The value of one is not advisable because the  group will close and immediately be deleted before the network management station will have the  opportunity to retrieve the statistics.   The value used in the rttMonStatsCaptureTable to  uniquely identify this group is the  rttMonStatsCaptureStartTimeIndex.  HTTP and Jitter probes store only two hours of data.  When this object is set to the value of zero all  rttMonStatsCaptureTable data capturing will be shut off
            	**type**\: int
            
            	**range:** 0..25
            
            .. attribute:: rttmonstatisticsadminnumpaths
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics paths to record per hourly group.   This value directly represents the path to a target.   For all other RttMonRttTypes this value will be  forced to one by the agent.  NOTE\: For 'pathEcho' a source to target path will be        created to to hold all errors that occur when a        specific path or connection has not be found/setup.        Thus, it is advised to set this value greater       than one.  Since this index does not rollover, only the first rttMonStatisticsAdminNumPaths will be kept
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: rttmonstatisticsadminnumhops
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics hops to record per path group.   This value directly represents the number of hops along  a path to a target, thus we can only support 30 hops.   For all other RttMonRttTypes this value will be  forced to one by the agent.  Since this index does not rollover, only the first rttMonStatisticsAdminNumHops will be kept. This object  is applicable to pathEcho probes only
            	**type**\: int
            
            	**range:** 1..30
            
            .. attribute:: rttmonstatisticsadminnumdistbuckets
            
            	The maximum number of statistical distribution Buckets to accumulate.  Since this index does not rollover, only the first rttMonStatisticsAdminNumDistBuckets will be kept.  The last rttMonStatisticsAdminNumDistBucket will contain all entries from its distribution interval start point to infinity. This object is not applicable  to http and jitter probes
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: rttmonstatisticsadmindistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  rttMonStatisticsAdminNumDistBuckets = 5 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  rttMonStatisticsAdminNumDistBuckets = 1 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of  rttMonStatisticsAdminDistInterval does not apply when rttMonStatisticsAdminNumDistBuckets is one. This object is not applicable to http and jitter probes
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhistoryadminnumlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the rttMonCtrlOperRttLife object.  A new life is created when the same conceptual RTT control row is restarted via the transition of the  rttMonCtrlOperRttLife object and its subsequent  countdown.  The value of zero will shut off all  rttMonHistoryAdminTable data collection
            	**type**\: int
            
            	**range:** 0..2
            
            .. attribute:: rttmonhistoryadminnumbuckets
            
            	The maximum number of history buckets to record.  When the RttMonRttType is 'pathEcho'  this value directly  represents a path to a target.  For all other  RttMonRttTypes this value should be set to the number  of operations to keep per lifetime.  After rttMonHistoryAdminNumBuckets are filled, the  and the oldest entries are deleted and the most recent rttMonHistoryAdminNumBuckets buckets are retained
            	**type**\: int
            
            	**range:** 1..60
            
            .. attribute:: rttmonhistoryadminnumsamples
            
            	The maximum number of history samples to record per bucket.  When the RttMonRttType is 'pathEcho' this  value directly represents the number of hops along a  path to a target, thus we can only support 30 hops. For all other RttMonRttTypes this value will be  forced to one by the agent
            	**type**\: int
            
            	**range:** 1..30
            
            .. attribute:: rttmonhistoryadminfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none          \- no history is recorded all           \- the results of all completion times                   and failed completions are recorded overThreshold \- the results of completion times                  over rttMonCtrlAdminThreshold are                   recorded. failures      \- the results of failed operations (only)                   are recorded
            	**type**\:  :py:class:`Rttmonhistoryadminfilter <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonhistoryadminfilter>`
            
            .. attribute:: rttmonctrlopermodificationtime
            
            	This object is updated whenever an object in the conceptual RTT control row is changed or updated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrloperdiagtext
            
            	A string which can be used as an aid in tracing problems. The content of this field will depend on the type of  target (rttMonEchoAdminProtocol).   When rttMonEchoAdminProtocol is one of snaLU0EchoAppl, or  snaLU2EchoAppl this object contains the name of the  Logical Unit (LU) being used for this RTT session (from the HOST's point of view), once the session has been  established; this can then be used to correlate this  name to the connection information stored in the  Mainframe Host.  When rttMonEchoAdminProtocol is snaLU62EchoAppl, this  object contains the Logical Unit (LU) name being used for this RTT session, once the session has been established.   This name can be used by the management application to  correlate this objects value to the connection  information stored at this SNMP Agent via the APPC or  APPN mib.  When rttMonEchoAdminProtocol is not one of the  previously mentioned values, this value will be null.  It is primarily intended that this object contains  information which has significance to a human operator
            	**type**\: str
            
            	**length:** 0..51
            
            .. attribute:: rttmonctrloperresettime
            
            	This object is set when the rttMonCtrlOperState is set to reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrloperoctetsinuse
            
            	This object is the number of octets currently in use by this composite conceptual RTT row.  A composite conceptual row include the control, statistics, and  history conceptual rows combined.  (All octets that are addressed via the rttMonCtrlAdminIndex in this mib.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrloperconnectionlostoccurred
            
            	This object will only change its value when the RttMonRttType is 'echo' or 'pathEcho'.  This object is set to true when the RTT connection fails  to be established or is lost, and set to false when a  connection is reestablished.  When the RttMonRttType is 'pathEcho', connection loss applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  When this value changes and  rttMonReactAdminConnectionEnable is true, a reaction  will occur.   If a trap is sent it is a  rttMonConnectionChangeNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'connectionLoss(8)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'connectionLoss'
            	**type**\: bool
            
            .. attribute:: rttmonctrlopertimeoutoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is set to true when an operation times out,  and set to false when an operation completes under  rttMonCtrlAdminTimeout.  When this value changes, a  reaction may occur, as defined by  rttMonReactAdminTimeoutEnable.   When the RttMonRttType is 'pathEcho', this timeout applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  If a trap is sent it is a rttMonTimeoutNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'timeout(7)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'timeout'
            	**type**\: bool
            
            .. attribute:: rttmonctrloperoverthresholdoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is changed by operation completion times over threshold, as defined by rttMonReactAdminThresholdType.   When this value changes, a reaction may occur, as defined  by rttMonReactAdminThresholdType.   If a trap is sent it is a rttMonThresholdNotification.  This object is set to true if the operation completion time exceeds the rttMonCtrlAdminThreshold and set to false when an operation completes under rttMonCtrlAdminThreshold. When this value changes, a reaction may occur, as defined by rttMonReactThresholdType.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'rtt'
            	**type**\: bool
            
            .. attribute:: rttmonctrlopernumrtts
            
            	This is the total number of probe operations that have been attempted.     This value is incremented for each start of an RTT  operation.  Thus when rttMonCtrlAdminRttType is set to  'pathEcho' this value will be incremented by one and  not for very every hop along the path.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object.  This value is not effected by the rollover of a statistics hourly group
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonctrloperrttlife
            
            	This object is decremented every second, until it reaches zero.  When the value of this object is zero RTT operations for this row are suspended.  This  object will either reach zero by a countdown or  it will transition to zero via setting the rttMonCtrlOperState.  When this object reaches zero the agent needs to  transition the rttMonCtrlOperState to 'inactive'.  REMEMBER\:  The value 2147483647 has a special             meaning.  When this object has the            value 2147483647, this object will            not decrement.  And thus the life             time will never.  When the rttMonCtrlOperState object is 'active' and  the rttMonReactTriggerOperState object transitions to  'active' this object will not be updated with the  current value of rttMonCrtlAdminRttLife object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrloperstate
            
            	The RttMonOperStatus object is used to manage the 'state' of the probe that is implementing  conceptual RTT control row.  This status object has six defined values\:  reset(1)          \- reset this entry, transition                     to 'pending' orderlyStop(2)    \- shutdown this entry at the end                      of the next RTT operation attempt,                       transition to 'inactive' immediateStop(3)  \- shutdown this entry immediately                      (if possible), transition to                       'inactive' pending(4)        \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control either                       via the rttMonScheduleAdminTable                       or the rttMonReactAdminTable/                      rttMonReactTriggerAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      reseting this object, and second                      by creating a conceptual Rtt control                      row with the                       rttMonScheduleAdminRttStartTime                      object with the its special value inactive(5)       \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control via                      the rttMonScheduleAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      setting this object to 'orderlyStop'                      or 'immediateStop', second by                       the rttMonCtrlOperRttLife object                      reaching zero active(6)         \- this value is not settable and                      this conceptual RTT control row is                      currently active restart(7)        \- this value is only settable when the                      state is active. It clears the data                      of this entry and remain on active state.  The probes action when this object is set to 'reset'\:   \-  all rows in rttMonStatsCaptureTable that relate to        this conceptual RTT control row are destroyed and        the indices are set to 1   \-  if rttMonStatisticsAdminNumHourGroups is not zero, a        single new rttMonStatsCaptureTable row is created   \-  all rows in rttMonHistoryCaptureTable that relate        to this RTT definition are destroyed and the indices       are set to 1   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperRttLife is set to        rttMonScheduleAdminRttLife   \-  rttMonCtrlOperNumRtts is set to zero   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur   \-  the next RTT operation is controlled by the objects       in the rttMonScheduleAdminTable or the        rttMonReactAdminTable/rttMonReactTriggerAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending'   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections must be maintained  This can be used to synchronize various RTT  definitions, so that the RTT requests occur  simultaneously, or as simultaneously as possible.  The probes action when this object transitions to    'inactive' (via setting this object to 'orderlyStop'    or 'immediateStop' or by rttMonCtrlOperRttLife    reaching zero)\:   \-  all statistics and history collection information       table entries will be closed and kept   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur.   \-  the next RTT request is controlled by the objects       in the rttMonScheduleAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending' (this denotes that       the Trigger will be ready the next time this       object goes active)   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections are to be closed and cleanup.               rttMonCtrlOperState                     STATE           +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+           \|      A       \|       B      \|      C      \| ACTION       \|  'pending'   \|  'inactive'  \|   'active'  \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|inconsistent\- \|   noError   \| \|  to 'reset'    \|              \| Value        \|             \| \|                \|    \-> A      \|              \|   \-> A      \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|    noError   \|   noError   \| \|to 'orderlyStop'\|    \-> B      \|    \-> B      \|   \-> B      \| \|     or to      \|              \|              \|             \| \|'immediateStop' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  Event causes  \|    \-> C      \|    \-> B      \|   \-> C      \| \| Trigger State  \|              \|              \|   see (3)   \| \| to transition  \|              \|              \|             \| \| to 'active'    \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> C      \|    \-> C      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of one.        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> A      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of less than   \|              \|              \|             \| \| current time,  \|              \|              \|             \| \| excluding one. \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> B      \|   see (2)   \| \| transitions to \|              \|              \|             \| \| 'notInService' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> B      \|    \-> B      \|   \-> B      \| \| transitions to \|              \|              \|             \| \| 'delete'       \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus is \|    \-> C      \|    \-> C      \|   \-> C      \| \| 'active' & the \|              \|              \|   see (3)   \| \| RttStartTime   \|              \|              \|             \| \| arrives        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|   RowAgeout    \|    \-> B      \|    \-> B      \|   \-> B      \| \|    expires     \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  OperRttLife   \|    N/A       \|    N/A       \|   \-> B      \| \| counts down to \|              \|              \|             \| \| zero           \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+  (1) \- rttMonCtrlOperState must have transitioned to 'inactive' or 'pending' before the rttMonCtrlAdminStatus can transition to 'active'.  See (2). (2) \- rttMonCtrlAdminStatus cannot transition to 'notInService' unless rttMonCtrlOperState has been previously forced to 'inactive' or 'pending'. (3) \- when this happens the rttMonCtrlOperRttLife will not be updated with the rttMonCtrlAdminRttLife.  NOTE\:  In order for all objects in a PDU to be set        at the same time, this object can not be        part of a multi\-bound PDU
            	**type**\:  :py:class:`Rttmonctrloperstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonctrloperstate>`
            
            .. attribute:: rttmonctrloperverifyerroroccurred
            
            	This object is true if rttMonCtrlAdminVerifyData is set to true and data corruption occurs
            	**type**\: bool
            
            .. attribute:: rttmonlatestrttopercompletiontime
            
            	The completion time of the latest RTT operation successfully completed.  The unit of this object will be microsecond when rttMonCtrlAdminRttType is set to 'jitter' and  rttMonEchoAdminPrecision is set to 'microsecond'. Otherwise, the unit of this object will be millisecond
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds/microseconds
            
            .. attribute:: rttmonlatestrttopersense
            
            	A sense code for the completion status of the latest RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            .. attribute:: rttmonlatestrttoperapplspecificsense
            
            	An application specific sense code for the completion status of the latest RTT operation.  This  object will only be valid when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestrttopersensedescription
            
            	A sense description for the completion status of the latest RTT operation when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'
            	**type**\: str
            
            .. attribute:: rttmonlatestrttopertime
            
            	The value of the agent system time at the time of the latest RTT operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestrttoperaddress
            
            	When the RttMonRttType is 'echo', 'pathEcho', 'udpEcho', 'tcpConnect', 'dns' and 'dlsw' this is a string which specifies  the address of the target for this RTT operation.  When the  RttMonRttType is not one of these types this object will  be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry, self).__init__()

                self.yang_name = "rttMonCtrlAdminEntry"
                self.yang_parent_name = "rttMonCtrlAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.int32, 'rttMonCtrlAdminIndex')),
                    ('rttmonctrladminowner', YLeaf(YType.str, 'rttMonCtrlAdminOwner')),
                    ('rttmonctrladmintag', YLeaf(YType.str, 'rttMonCtrlAdminTag')),
                    ('rttmonctrladminrtttype', YLeaf(YType.enumeration, 'rttMonCtrlAdminRttType')),
                    ('rttmonctrladminthreshold', YLeaf(YType.int32, 'rttMonCtrlAdminThreshold')),
                    ('rttmonctrladminfrequency', YLeaf(YType.int32, 'rttMonCtrlAdminFrequency')),
                    ('rttmonctrladmintimeout', YLeaf(YType.int32, 'rttMonCtrlAdminTimeout')),
                    ('rttmonctrladminverifydata', YLeaf(YType.boolean, 'rttMonCtrlAdminVerifyData')),
                    ('rttmonctrladminstatus', YLeaf(YType.enumeration, 'rttMonCtrlAdminStatus')),
                    ('rttmonctrladminnvgen', YLeaf(YType.boolean, 'rttMonCtrlAdminNvgen')),
                    ('rttmonctrladmingroupname', YLeaf(YType.str, 'rttMonCtrlAdminGroupName')),
                    ('rttmonscheduleadminrttlife', YLeaf(YType.int32, 'rttMonScheduleAdminRttLife')),
                    ('rttmonscheduleadminrttstarttime', YLeaf(YType.uint32, 'rttMonScheduleAdminRttStartTime')),
                    ('rttmonscheduleadminconceptrowageout', YLeaf(YType.int32, 'rttMonScheduleAdminConceptRowAgeout')),
                    ('rttmonscheduleadminrttrecurring', YLeaf(YType.boolean, 'rttMonScheduleAdminRttRecurring')),
                    ('rttmonscheduleadminconceptrowageoutv2', YLeaf(YType.int32, 'rttMonScheduleAdminConceptRowAgeoutV2')),
                    ('rttmonreactadminconnectionenable', YLeaf(YType.boolean, 'rttMonReactAdminConnectionEnable')),
                    ('rttmonreactadmintimeoutenable', YLeaf(YType.boolean, 'rttMonReactAdminTimeoutEnable')),
                    ('rttmonreactadminthresholdtype', YLeaf(YType.enumeration, 'rttMonReactAdminThresholdType')),
                    ('rttmonreactadminthresholdfalling', YLeaf(YType.int32, 'rttMonReactAdminThresholdFalling')),
                    ('rttmonreactadminthresholdcount', YLeaf(YType.int32, 'rttMonReactAdminThresholdCount')),
                    ('rttmonreactadminthresholdcount2', YLeaf(YType.int32, 'rttMonReactAdminThresholdCount2')),
                    ('rttmonreactadminactiontype', YLeaf(YType.enumeration, 'rttMonReactAdminActionType')),
                    ('rttmonreactadminverifyerrorenable', YLeaf(YType.boolean, 'rttMonReactAdminVerifyErrorEnable')),
                    ('rttmonstatisticsadminnumhourgroups', YLeaf(YType.int32, 'rttMonStatisticsAdminNumHourGroups')),
                    ('rttmonstatisticsadminnumpaths', YLeaf(YType.int32, 'rttMonStatisticsAdminNumPaths')),
                    ('rttmonstatisticsadminnumhops', YLeaf(YType.int32, 'rttMonStatisticsAdminNumHops')),
                    ('rttmonstatisticsadminnumdistbuckets', YLeaf(YType.int32, 'rttMonStatisticsAdminNumDistBuckets')),
                    ('rttmonstatisticsadmindistinterval', YLeaf(YType.int32, 'rttMonStatisticsAdminDistInterval')),
                    ('rttmonhistoryadminnumlives', YLeaf(YType.int32, 'rttMonHistoryAdminNumLives')),
                    ('rttmonhistoryadminnumbuckets', YLeaf(YType.int32, 'rttMonHistoryAdminNumBuckets')),
                    ('rttmonhistoryadminnumsamples', YLeaf(YType.int32, 'rttMonHistoryAdminNumSamples')),
                    ('rttmonhistoryadminfilter', YLeaf(YType.enumeration, 'rttMonHistoryAdminFilter')),
                    ('rttmonctrlopermodificationtime', YLeaf(YType.uint32, 'rttMonCtrlOperModificationTime')),
                    ('rttmonctrloperdiagtext', YLeaf(YType.str, 'rttMonCtrlOperDiagText')),
                    ('rttmonctrloperresettime', YLeaf(YType.uint32, 'rttMonCtrlOperResetTime')),
                    ('rttmonctrloperoctetsinuse', YLeaf(YType.uint32, 'rttMonCtrlOperOctetsInUse')),
                    ('rttmonctrloperconnectionlostoccurred', YLeaf(YType.boolean, 'rttMonCtrlOperConnectionLostOccurred')),
                    ('rttmonctrlopertimeoutoccurred', YLeaf(YType.boolean, 'rttMonCtrlOperTimeoutOccurred')),
                    ('rttmonctrloperoverthresholdoccurred', YLeaf(YType.boolean, 'rttMonCtrlOperOverThresholdOccurred')),
                    ('rttmonctrlopernumrtts', YLeaf(YType.int32, 'rttMonCtrlOperNumRtts')),
                    ('rttmonctrloperrttlife', YLeaf(YType.int32, 'rttMonCtrlOperRttLife')),
                    ('rttmonctrloperstate', YLeaf(YType.enumeration, 'rttMonCtrlOperState')),
                    ('rttmonctrloperverifyerroroccurred', YLeaf(YType.boolean, 'rttMonCtrlOperVerifyErrorOccurred')),
                    ('rttmonlatestrttopercompletiontime', YLeaf(YType.uint32, 'rttMonLatestRttOperCompletionTime')),
                    ('rttmonlatestrttopersense', YLeaf(YType.enumeration, 'rttMonLatestRttOperSense')),
                    ('rttmonlatestrttoperapplspecificsense', YLeaf(YType.int32, 'rttMonLatestRttOperApplSpecificSense')),
                    ('rttmonlatestrttopersensedescription', YLeaf(YType.str, 'rttMonLatestRttOperSenseDescription')),
                    ('rttmonlatestrttopertime', YLeaf(YType.uint32, 'rttMonLatestRttOperTime')),
                    ('rttmonlatestrttoperaddress', YLeaf(YType.str, 'rttMonLatestRttOperAddress')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry, ['rttmonctrladminindex', 'rttmonctrladminowner', 'rttmonctrladmintag', 'rttmonctrladminrtttype', 'rttmonctrladminthreshold', 'rttmonctrladminfrequency', 'rttmonctrladmintimeout', 'rttmonctrladminverifydata', 'rttmonctrladminstatus', 'rttmonctrladminnvgen', 'rttmonctrladmingroupname', 'rttmonscheduleadminrttlife', 'rttmonscheduleadminrttstarttime', 'rttmonscheduleadminconceptrowageout', 'rttmonscheduleadminrttrecurring', 'rttmonscheduleadminconceptrowageoutv2', 'rttmonreactadminconnectionenable', 'rttmonreactadmintimeoutenable', 'rttmonreactadminthresholdtype', 'rttmonreactadminthresholdfalling', 'rttmonreactadminthresholdcount', 'rttmonreactadminthresholdcount2', 'rttmonreactadminactiontype', 'rttmonreactadminverifyerrorenable', 'rttmonstatisticsadminnumhourgroups', 'rttmonstatisticsadminnumpaths', 'rttmonstatisticsadminnumhops', 'rttmonstatisticsadminnumdistbuckets', 'rttmonstatisticsadmindistinterval', 'rttmonhistoryadminnumlives', 'rttmonhistoryadminnumbuckets', 'rttmonhistoryadminnumsamples', 'rttmonhistoryadminfilter', 'rttmonctrlopermodificationtime', 'rttmonctrloperdiagtext', 'rttmonctrloperresettime', 'rttmonctrloperoctetsinuse', 'rttmonctrloperconnectionlostoccurred', 'rttmonctrlopertimeoutoccurred', 'rttmonctrloperoverthresholdoccurred', 'rttmonctrlopernumrtts', 'rttmonctrloperrttlife', 'rttmonctrloperstate', 'rttmonctrloperverifyerroroccurred', 'rttmonlatestrttopercompletiontime', 'rttmonlatestrttopersense', 'rttmonlatestrttoperapplspecificsense', 'rttmonlatestrttopersensedescription', 'rttmonlatestrttopertime', 'rttmonlatestrttoperaddress'], name, value)

            class Rttmonctrloperstate(Enum):
                """
                Rttmonctrloperstate (Enum Class)

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


            class Rttmonhistoryadminfilter(Enum):
                """
                Rttmonhistoryadminfilter (Enum Class)

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


            class Rttmonreactadminactiontype(Enum):
                """
                Rttmonreactadminactiontype (Enum Class)

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


            class Rttmonreactadminthresholdtype(Enum):
                """
                Rttmonreactadminthresholdtype (Enum Class)

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



    class Rttmonechoadmintable(Entity):
        """
        A table that contains Round Trip Time (RTT) specific
        definitions.
        
        This table is controlled via the 
        rttMonCtrlAdminTable.  Entries in this table are
        created via the rttMonCtrlAdminStatus object.
        
        .. attribute:: rttmonechoadminentry
        
        	A list of objects that define specific configuration for RttMonRttType conceptual Rtt control rows
        	**type**\: list of  		 :py:class:`Rttmonechoadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonechoadmintable, self).__init__()

            self.yang_name = "rttMonEchoAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonEchoAdminEntry", ("rttmonechoadminentry", CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry))])
            self._leafs = OrderedDict()

            self.rttmonechoadminentry = YList(self)
            self._segment_path = lambda: "rttMonEchoAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonechoadmintable, [], name, value)


        class Rttmonechoadminentry(Entity):
            """
            A list of objects that define specific configuration for
            RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonechoadminprotocol
            
            	Specifies the protocol to be used to perform the RTT operation. The following list defines what protocol  should be used for each probe type\:  echo, pathEcho   \- ipIcmpEcho / mplsLspPingAppl udpEcho          \- ipUdpEchoAppl tcpConnect       \- ipTcpConn http             \- httpAppl jitter           \- jitterAppl dlsw             \- dlswAppl dhcp             \- dhcpAppl ftp              \- ftpAppl mplsLspPing      \- mplsLspPingAppl voip             \- voipAppl video            \- videoAppl  When this protocol does not support the type, a 'badValue' error will be returned
            	**type**\:  :py:class:`RttMonProtocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonProtocol>`
            
            .. attribute:: rttmonechoadmintargetaddress
            
            	A string which specifies the address of the target
            	**type**\: str
            
            .. attribute:: rttmonechoadminpktdatarequestsize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request  message, when using SNA protocols.  For non\-ARR protocols' RTT request/responses,  this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included             in this value.  For echo probes the total packet size = (IP header(20) +  ICMP header(8) + 8 (internal timestamps) + request size).  For echo and pathEcho default request size is 28. For udp probe, default request size is 16 and for jitter  probe it is 32. For dlsw probes default request size is 0.  The minimum request size for echo and pathEcho is 28 bytes, for udp it is 4 and for jitter it is 16. For udp and jitter probes the maximum request size is 1500.  For ethernetPing the default request size is 66. For ethernetJitter the default request size is 51
            	**type**\: int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadminpktdataresponsesize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the response message. This value is passed to the RTT Echo Server via a field in the ARR Header.  For non\-ARR RTT request/response (i.e. ipIcmpecho) this value will be set by the agent to match the size of rttMonEchoAdminPktDataRequestSize, when native payloads are supported.  REMEMBER\:  The ARR Header overhead is not included             in this value.  This object is only supported by SNA protocols
            	**type**\: int
            
            	**range:** 0..16384
            
            .. attribute:: rttmonechoadmintargetport
            
            	This object represents the target's port number. This object is applicable to udpEcho, tcpConnect and jitter probes
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadminsourceaddress
            
            	A string which specifies the IP address of the source. This object is applicable to all probes except dns, dlsw  and sna
            	**type**\: str
            
            .. attribute:: rttmonechoadminsourceport
            
            	This object represents the source's port number. If this object is not specified, the application will get a  port allocated by the system. This object is applicable  to all probes except dns, dlsw and sna
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadmincontrolenable
            
            	If this object is enabled, then the RTR application will send control messages to a responder, residing on the  target router to respond to the data request packets being  sent by the source router. This object is not applicable to  echo, pathEcho, dns and http probes
            	**type**\: bool
            
            .. attribute:: rttmonechoadmintos
            
            	This object represents the type of service octet in an IP header. This object is not applicable to dhcp, dns,  ethernetPing and ethernetJitter
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rttmonechoadminlsrenable
            
            	If this object is enabled then it means that the application calculates response time for a specific path, defined in rttMonEchoPathAdminEntry. This object is applicable to echo  probe only
            	**type**\: bool
            
            .. attribute:: rttmonechoadmintargetaddressstring
            
            	A string which specifies the address of the target. This string can be in IP address format or a hostname. This object is applicable to dns probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminnameserver
            
            	A string which specifies the ip address of the name\-server. This object is applicable to dns probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminoperation
            
            	A code that represents the specific type of RTT operation. This object is applicable to http and ftp probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            .. attribute:: rttmonechoadminhttpversion
            
            	A string which specifies the version number of the HTTP Server.  The syntax for the version string is  <major number>.<minor number> An example would be 1.0,  1.1 etc.,.  This object is applicable to http probe only
            	**type**\: str
            
            	**length:** 3..10
            
            .. attribute:: rttmonechoadminurl
            
            	A string which represents the URL to which a HTTP probe should communicate with. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadmincache
            
            	If this object is false then it means that HTTP request should not download cached pages. This means that the request should  be forwarded to the origin server. This object is applicable to http probe only
            	**type**\: bool
            
            .. attribute:: rttmonechoadmininterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for  Jitter probe. This object is applicable to jitter probe only
            	**type**\: int
            
            	**range:** 0..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadminnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe.  This object is applicable to jitter probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminproxy
            
            	This string represents the proxy server information. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminstring1
            
            	This string stores the content of HTTP raw request. If the request cannot fit into String1 then it should  be split and put in Strings 1 through 5.  This string stores the content of the DHCP raw option data.  The raw DHCP option data must be in HEX. If an odd number of characters are specified, a 0 will be appended to the end of the string.  Only DHCP option 82 (decimal) is allowed. Here is an example of a valid string\: 5208010610005A6F1234 Only rttMonEchoAdminString1 is used for dhcp, Strings 1 through 5 are not used.  This object is applicable to http and dhcp probe  types only
            	**type**\: str
            
            .. attribute:: rttmonechoadminstring2
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminstring3
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminstring4
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminstring5
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadminmode
            
            	A code that represents the specific type of RTT operation. This object is applicable to ftp probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            .. attribute:: rttmonechoadminvrfname
            
            	This field is used to specify the VPN name in which the RTT operation will be used. For regular RTT operation this field should not be configured. The agent  will use this field to identify the VPN routing Table for this operation
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: rttmonechoadmincodectype
            
            	Specifies the codec type to be used with jitter probe. This is applicable only for the jitter probe.  If codec\-type is configured the following parameters cannot be  configured. rttMonEchoAdminPktDataRequestSize rttMonEchoAdminInterval rttMonEchoAdminNumPackets
            	**type**\:  :py:class:`RttMonCodecType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonCodecType>`
            
            .. attribute:: rttmonechoadmincodecinterval
            
            	This field represents the inter\-packet delay between packets and is in milliseconds. This object is applicable only to jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadmincodecpayload
            
            	This object represents the number of octets that needs to be placed into the Data portion of the message. This value is used only for jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadmincodecnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is used only for jitter probe which uses codec type
            	**type**\: int
            
            	**range:** 0..60000
            
            .. attribute:: rttmonechoadminicpifadvfactor
            
            	The advantage factor is dependant on the type of access and how the service is to be used. Conventional Wire\-line     0 Mobility within Building    5 Mobility within geographic area  10 Access to hard\-to\-reach location   20  This will be used while calculating the ICPIF values This valid only for Jitter while calculating the ICPIF value
            	**type**\: int
            
            	**range:** 0..20
            
            .. attribute:: rttmonechoadminlspfectype
            
            	The type of the target FEC for the RTT 'echo' and 'pathEcho' operations based on 'mplsLspPingAppl' RttMonProtocol.  ldpIpv4Prefix   \- LDP IPv4 prefix
            	**type**\:  :py:class:`Rttmonechoadminlspfectype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminlspfectype>`
            
            .. attribute:: rttmonechoadminlspselector
            
            	A string which specifies a valid 127/8 address. This address is of the form 127.x.y.z. This address is not used to route the MPLS echo packet to the destination but is used for load balancing in cases where the IP payload's destination address is used for load balancing
            	**type**\: str
            
            .. attribute:: rttmonechoadminlspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests
            	**type**\:  :py:class:`RttMonLSPPingReplyMode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonLSPPingReplyMode>`
            
            .. attribute:: rttmonechoadminlspttl
            
            	This object represents the TTL setting for MPLS echo request packets. For ping operation this represents the TTL value to be set in the echo request packet. For trace operation it represent the maximum ttl value that can be set in the echo request packets starting with TTL=1.  For 'echo' based on mplsLspPingAppl the default TTL will be set to 255, and for 'pathEcho' based on mplsLspPingAppl the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values to be used for 'echo' and 'pathEcho' based on 'mplsLspPingAppl'
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rttmonechoadminlspexp
            
            	This object represents the EXP value that needs to be put as precedence bit in the MPLS echo request IP header
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: rttmonechoadminprecision
            
            	This object specifies the accuracy of statistics that needs to be calculated milliseconds \- The accuracy of stats will be of milliseconds microseconds \- The accuracy of stats will be in microseconds. This value can be set only for jitter operation
            	**type**\:  :py:class:`Rttmonechoadminprecision <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminprecision>`
            
            .. attribute:: rttmonechoadminprobepakpriority
            
            	This object specifies the priority that will be assigned to probe packet.  This value can be set only for jitter  operation
            	**type**\:  :py:class:`Rttmonechoadminprobepakpriority <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminprobepakpriority>`
            
            .. attribute:: rttmonechoadminowntpsynctolabs
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of NTP offsets on source and responder. The value specified is  microseconds. This value can be set only for jitter operation  with precision of microsecond
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rttmonechoadminowntpsynctolpct
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of  NTP offsets on source and responder. The value is expressed  as the percentage of actual oneway latency that is measured.  This value can be set only for jitter operation with precision  of microsecond
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: rttmonechoadminowntpsynctoltype
            
            	This object specifies whether the value in specified for oneway NTP sync tolerance is absolute value or percent value
            	**type**\:  :py:class:`Rttmonechoadminowntpsynctoltype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminowntpsynctoltype>`
            
            .. attribute:: rttmonechoadmincallednumber
            
            	This string stores the called number of post dial delay. This object is applicable to voip post dial delay probe only. The number will be like the one actualy the user could dial. It has the number required by the local country dial plan, plus E.164 number. The maximum length is 24 digits. Only digit (0\-9) is allowed
            	**type**\: str
            
            	**length:** 0..24
            
            .. attribute:: rttmonechoadmindetectpoint
            
            	A code that represents the detect point of post dial delay. This object is applicable to SAA post dial delay probe only
            	**type**\:  :py:class:`RttMonOperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonOperation>`
            
            .. attribute:: rttmonechoadmingkregistration
            
            	A boolean that represents VoIP GK registration delay. This object is applicable to SAA GK registration delay  probe only
            	**type**\: bool
            
            .. attribute:: rttmonechoadminsourcevoiceport
            
            	A string which specifies the voice\-port on the source gateway. This object is applicable to RTP probe only
            	**type**\: str
            
            .. attribute:: rttmonechoadmincallduration
            
            	Duration of RTP/Video Probe session. This object is applicable to RTP and Video probe
            	**type**\: int
            
            	**range:** 1..600
            
            .. attribute:: rttmonechoadminlspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\: int
            
            	**range:** 0..63 \| 255..None
            
            .. attribute:: rttmonechoadminlspnullshim
            
            	This object specifies if the explicit\-null label is to be added to LSP echo requests which are sent while performing RTT operation
            	**type**\: bool
            
            .. attribute:: rttmonechoadmintargetmpid
            
            	This object specifies the destination maintenance point ID. It is only applicable to ethernetPing and ethernetJitter  operation. It will be set to 0 for other types of  operations
            	**type**\: int
            
            	**range:** 0..8191
            
            .. attribute:: rttmonechoadmintargetdomainname
            
            	This object specifies the name of the domain in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation
            	**type**\: str
            
            .. attribute:: rttmonechoadmintargetvlan
            
            	This object specifies the ID of the VLAN in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to 0 for other types of operations
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: rttmonechoadminethernetcos
            
            	This object specifies the class of service in an Ethernet packet header. It is only applicable to ethernetPing and  ethernetJitter operation
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: rttmonechoadminlspvccvid
            
            	This object specifies MPLS LSP pseudowire VCCV ID values between 1 to 2147483647.  Note\: This object cannot be set to value of 0. This default value specifies that VCCV is not set for this row
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonechoadmintargetevc
            
            	This object specifies the Ethernet Virtual Connection in which the destination maintenance point lies. It is only  applicable to ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\: str
            
            	**length:** 0..100
            
            .. attribute:: rttmonechoadmintargetmepport
            
            	This object specifies that Port Level CFM testing towards an Outward/Down MEP will be used. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\: bool
            
            .. attribute:: rttmonechoadminvideotrafficprofile
            
            	A string which represents the profile name to which a video probe should use. This object is applicable to video probe only
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: rttmonechoadmindscp
            
            	This object represents the Differentiated Service Code Point (DSCP) QoS marking in the generated synthetic packets.  Value \- DiffServ Class     0 \- BE (default)    10 \- AF11    12 \- AF12    14 \- AF13    18 \- AF21    20 \- AF22    22 \- AF23    26 \- AF31    28 \- AF32    30 \- AF33    34 \- AF41    36 \- AF42    38 \- AF43     8 \- CS1    16 \- CS2    24 \- CS3    32 \- CS4    40 \- CS5    48 \- CS6    56 \- CS7    46 \- EF
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: rttmonechoadminreservedsp
            
            	This object represents the video traffic generation source.  be \: best effort using DSP but without reservation gs \: guaranteed service using DSP with reservation na \: not applicable for not using DSP
            	**type**\:  :py:class:`Rttmonechoadminreservedsp <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminreservedsp>`
            
            .. attribute:: rttmonechoadmininputinterface
            
            	This object represents the network input interface on the sender router where the synthetic packets are received from the emulated endpoint source. This is used for path congruence with correct feature processing at the sender router.  The user can get the InterfaceIndex number from ifIndex object by looking up in ifTable. In fact, it should be useful to first get the entry by the augmented table ifXTable which has ifName object which matches the interface name used on the router or switch equipment console
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonechoadminemulatesourceaddress
            
            	This object specifies the IP address of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source IP address will by default be the same as rttMonEchoAdminSourceAddress. This object is applicable to video probes
            	**type**\: str
            
            .. attribute:: rttmonechoadminemulatesourceport
            
            	This object represents the port number of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source port number will by default be the same as rttMonEchoAdminSourcePort. This object is applicable to video probes
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadminemulatetargetaddress
            
            	This object specifies the IP address of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target IP address will by default be the same as rttMonEchoAdminTargetAddress. This object is applicable to video probes
            	**type**\: str
            
            .. attribute:: rttmonechoadminemulatetargetport
            
            	This object represents the port number of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target port number will by default be the same as rttMonEchoAdminTargetPort. This object is applicable to video probes
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadmintargetmacaddress
            
            	This object indicates the MAC address of the target device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminTargetMacAddress and rttMonEchoAdminTargetMPID may not be used in conjunction
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: rttmonechoadminsourcemacaddress
            
            	This object indicates the MAC address of the source device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminSourceMacAddress and rttMonEchoAdminSourceMPID may not be used in conjunction
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: rttmonechoadminsourcempid
            
            	This object indicates the source maintenance point ID.  It is only applicable to Y.1731 operation.  It will be set to zero for other types of opearations.  rttMonEchoAdminSourceMPID and rttMonEchoAdminSourceMacAddress may not be used in conjunction
            	**type**\: int
            
            	**range:** 0..8191
            
            .. attribute:: rttmonechoadminendpointlistname
            
            	This object specifies the name of endpoint list which a probe uses to generate operations
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: rttmonechoadminssm
            
            	This object specifies if Source Specific Multicast is to be added. This object is applicable to multicast probe only
            	**type**\: bool
            
            .. attribute:: rttmonechoadmincontrolretry
            
            	This object specifies the maximum number of retries for control message
            	**type**\: int
            
            	**range:** 1..5
            
            .. attribute:: rttmonechoadmincontroltimeout
            
            	This object specifies the wait duration before control message timeout
            	**type**\: int
            
            	**range:** 1..10000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadminigmptreeinit
            
            	This object specifies number of packets to be sent for multicast tree setup. This object is applicable to multicast probe only
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: rttmonechoadminenableburst
            
            	This object indicates that packets will be sent in burst
            	**type**\: bool
            
            .. attribute:: rttmonechoadminaggburstcycles
            
            	This object indicates the number of burst cycles to be sent during the aggregate interval. This value is currently used for Y1731 SLM(Synthetic Loss Measurment) probe. This object is applicable to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminlossrationumframes
            
            	This object indicates the number of frames over which to calculate the frame loss ratio. This object is applicable  to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminavailnumframes
            
            	This object indicates the number of frames over which to calculate the availability. This object is applicable to Y1731 SLM probe only
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadmintstampoptimization
            
            	This object specifies whether timestamp optimization is enabled.  When the value is 'true' then timestamp optimization is enabled.  The probe will utilize lower layer (Hardware/Packet Processor) timestamping values to improve accuracy of statistics.  This value can be set only for udp jitter operation with precision of microsecond
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry, self).__init__()

                self.yang_name = "rttMonEchoAdminEntry"
                self.yang_parent_name = "rttMonEchoAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonechoadminprotocol', YLeaf(YType.enumeration, 'rttMonEchoAdminProtocol')),
                    ('rttmonechoadmintargetaddress', YLeaf(YType.str, 'rttMonEchoAdminTargetAddress')),
                    ('rttmonechoadminpktdatarequestsize', YLeaf(YType.int32, 'rttMonEchoAdminPktDataRequestSize')),
                    ('rttmonechoadminpktdataresponsesize', YLeaf(YType.int32, 'rttMonEchoAdminPktDataResponseSize')),
                    ('rttmonechoadmintargetport', YLeaf(YType.int32, 'rttMonEchoAdminTargetPort')),
                    ('rttmonechoadminsourceaddress', YLeaf(YType.str, 'rttMonEchoAdminSourceAddress')),
                    ('rttmonechoadminsourceport', YLeaf(YType.int32, 'rttMonEchoAdminSourcePort')),
                    ('rttmonechoadmincontrolenable', YLeaf(YType.boolean, 'rttMonEchoAdminControlEnable')),
                    ('rttmonechoadmintos', YLeaf(YType.int32, 'rttMonEchoAdminTOS')),
                    ('rttmonechoadminlsrenable', YLeaf(YType.boolean, 'rttMonEchoAdminLSREnable')),
                    ('rttmonechoadmintargetaddressstring', YLeaf(YType.str, 'rttMonEchoAdminTargetAddressString')),
                    ('rttmonechoadminnameserver', YLeaf(YType.str, 'rttMonEchoAdminNameServer')),
                    ('rttmonechoadminoperation', YLeaf(YType.enumeration, 'rttMonEchoAdminOperation')),
                    ('rttmonechoadminhttpversion', YLeaf(YType.str, 'rttMonEchoAdminHTTPVersion')),
                    ('rttmonechoadminurl', YLeaf(YType.str, 'rttMonEchoAdminURL')),
                    ('rttmonechoadmincache', YLeaf(YType.boolean, 'rttMonEchoAdminCache')),
                    ('rttmonechoadmininterval', YLeaf(YType.int32, 'rttMonEchoAdminInterval')),
                    ('rttmonechoadminnumpackets', YLeaf(YType.int32, 'rttMonEchoAdminNumPackets')),
                    ('rttmonechoadminproxy', YLeaf(YType.str, 'rttMonEchoAdminProxy')),
                    ('rttmonechoadminstring1', YLeaf(YType.str, 'rttMonEchoAdminString1')),
                    ('rttmonechoadminstring2', YLeaf(YType.str, 'rttMonEchoAdminString2')),
                    ('rttmonechoadminstring3', YLeaf(YType.str, 'rttMonEchoAdminString3')),
                    ('rttmonechoadminstring4', YLeaf(YType.str, 'rttMonEchoAdminString4')),
                    ('rttmonechoadminstring5', YLeaf(YType.str, 'rttMonEchoAdminString5')),
                    ('rttmonechoadminmode', YLeaf(YType.enumeration, 'rttMonEchoAdminMode')),
                    ('rttmonechoadminvrfname', YLeaf(YType.str, 'rttMonEchoAdminVrfName')),
                    ('rttmonechoadmincodectype', YLeaf(YType.enumeration, 'rttMonEchoAdminCodecType')),
                    ('rttmonechoadmincodecinterval', YLeaf(YType.int32, 'rttMonEchoAdminCodecInterval')),
                    ('rttmonechoadmincodecpayload', YLeaf(YType.int32, 'rttMonEchoAdminCodecPayload')),
                    ('rttmonechoadmincodecnumpackets', YLeaf(YType.int32, 'rttMonEchoAdminCodecNumPackets')),
                    ('rttmonechoadminicpifadvfactor', YLeaf(YType.int32, 'rttMonEchoAdminICPIFAdvFactor')),
                    ('rttmonechoadminlspfectype', YLeaf(YType.enumeration, 'rttMonEchoAdminLSPFECType')),
                    ('rttmonechoadminlspselector', YLeaf(YType.str, 'rttMonEchoAdminLSPSelector')),
                    ('rttmonechoadminlspreplymode', YLeaf(YType.enumeration, 'rttMonEchoAdminLSPReplyMode')),
                    ('rttmonechoadminlspttl', YLeaf(YType.int32, 'rttMonEchoAdminLSPTTL')),
                    ('rttmonechoadminlspexp', YLeaf(YType.int32, 'rttMonEchoAdminLSPExp')),
                    ('rttmonechoadminprecision', YLeaf(YType.enumeration, 'rttMonEchoAdminPrecision')),
                    ('rttmonechoadminprobepakpriority', YLeaf(YType.enumeration, 'rttMonEchoAdminProbePakPriority')),
                    ('rttmonechoadminowntpsynctolabs', YLeaf(YType.int32, 'rttMonEchoAdminOWNTPSyncTolAbs')),
                    ('rttmonechoadminowntpsynctolpct', YLeaf(YType.int32, 'rttMonEchoAdminOWNTPSyncTolPct')),
                    ('rttmonechoadminowntpsynctoltype', YLeaf(YType.enumeration, 'rttMonEchoAdminOWNTPSyncTolType')),
                    ('rttmonechoadmincallednumber', YLeaf(YType.str, 'rttMonEchoAdminCalledNumber')),
                    ('rttmonechoadmindetectpoint', YLeaf(YType.enumeration, 'rttMonEchoAdminDetectPoint')),
                    ('rttmonechoadmingkregistration', YLeaf(YType.boolean, 'rttMonEchoAdminGKRegistration')),
                    ('rttmonechoadminsourcevoiceport', YLeaf(YType.str, 'rttMonEchoAdminSourceVoicePort')),
                    ('rttmonechoadmincallduration', YLeaf(YType.int32, 'rttMonEchoAdminCallDuration')),
                    ('rttmonechoadminlspreplydscp', YLeaf(YType.int32, 'rttMonEchoAdminLSPReplyDscp')),
                    ('rttmonechoadminlspnullshim', YLeaf(YType.boolean, 'rttMonEchoAdminLSPNullShim')),
                    ('rttmonechoadmintargetmpid', YLeaf(YType.uint32, 'rttMonEchoAdminTargetMPID')),
                    ('rttmonechoadmintargetdomainname', YLeaf(YType.str, 'rttMonEchoAdminTargetDomainName')),
                    ('rttmonechoadmintargetvlan', YLeaf(YType.int32, 'rttMonEchoAdminTargetVLAN')),
                    ('rttmonechoadminethernetcos', YLeaf(YType.int32, 'rttMonEchoAdminEthernetCOS')),
                    ('rttmonechoadminlspvccvid', YLeaf(YType.int32, 'rttMonEchoAdminLSPVccvID')),
                    ('rttmonechoadmintargetevc', YLeaf(YType.str, 'rttMonEchoAdminTargetEVC')),
                    ('rttmonechoadmintargetmepport', YLeaf(YType.boolean, 'rttMonEchoAdminTargetMEPPort')),
                    ('rttmonechoadminvideotrafficprofile', YLeaf(YType.str, 'rttMonEchoAdminVideoTrafficProfile')),
                    ('rttmonechoadmindscp', YLeaf(YType.uint8, 'rttMonEchoAdminDscp')),
                    ('rttmonechoadminreservedsp', YLeaf(YType.enumeration, 'rttMonEchoAdminReserveDsp')),
                    ('rttmonechoadmininputinterface', YLeaf(YType.int32, 'rttMonEchoAdminInputInterface')),
                    ('rttmonechoadminemulatesourceaddress', YLeaf(YType.str, 'rttMonEchoAdminEmulateSourceAddress')),
                    ('rttmonechoadminemulatesourceport', YLeaf(YType.int32, 'rttMonEchoAdminEmulateSourcePort')),
                    ('rttmonechoadminemulatetargetaddress', YLeaf(YType.str, 'rttMonEchoAdminEmulateTargetAddress')),
                    ('rttmonechoadminemulatetargetport', YLeaf(YType.int32, 'rttMonEchoAdminEmulateTargetPort')),
                    ('rttmonechoadmintargetmacaddress', YLeaf(YType.str, 'rttMonEchoAdminTargetMacAddress')),
                    ('rttmonechoadminsourcemacaddress', YLeaf(YType.str, 'rttMonEchoAdminSourceMacAddress')),
                    ('rttmonechoadminsourcempid', YLeaf(YType.uint32, 'rttMonEchoAdminSourceMPID')),
                    ('rttmonechoadminendpointlistname', YLeaf(YType.str, 'rttMonEchoAdminEndPointListName')),
                    ('rttmonechoadminssm', YLeaf(YType.boolean, 'rttMonEchoAdminSSM')),
                    ('rttmonechoadmincontrolretry', YLeaf(YType.uint32, 'rttMonEchoAdminControlRetry')),
                    ('rttmonechoadmincontroltimeout', YLeaf(YType.uint32, 'rttMonEchoAdminControlTimeout')),
                    ('rttmonechoadminigmptreeinit', YLeaf(YType.uint32, 'rttMonEchoAdminIgmpTreeInit')),
                    ('rttmonechoadminenableburst', YLeaf(YType.boolean, 'rttMonEchoAdminEnableBurst')),
                    ('rttmonechoadminaggburstcycles', YLeaf(YType.int32, 'rttMonEchoAdminAggBurstCycles')),
                    ('rttmonechoadminlossrationumframes', YLeaf(YType.int32, 'rttMonEchoAdminLossRatioNumFrames')),
                    ('rttmonechoadminavailnumframes', YLeaf(YType.int32, 'rttMonEchoAdminAvailNumFrames')),
                    ('rttmonechoadmintstampoptimization', YLeaf(YType.boolean, 'rttMonEchoAdminTstampOptimization')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonechoadmintable.Rttmonechoadminentry, ['rttmonctrladminindex', 'rttmonechoadminprotocol', 'rttmonechoadmintargetaddress', 'rttmonechoadminpktdatarequestsize', 'rttmonechoadminpktdataresponsesize', 'rttmonechoadmintargetport', 'rttmonechoadminsourceaddress', 'rttmonechoadminsourceport', 'rttmonechoadmincontrolenable', 'rttmonechoadmintos', 'rttmonechoadminlsrenable', 'rttmonechoadmintargetaddressstring', 'rttmonechoadminnameserver', 'rttmonechoadminoperation', 'rttmonechoadminhttpversion', 'rttmonechoadminurl', 'rttmonechoadmincache', 'rttmonechoadmininterval', 'rttmonechoadminnumpackets', 'rttmonechoadminproxy', 'rttmonechoadminstring1', 'rttmonechoadminstring2', 'rttmonechoadminstring3', 'rttmonechoadminstring4', 'rttmonechoadminstring5', 'rttmonechoadminmode', 'rttmonechoadminvrfname', 'rttmonechoadmincodectype', 'rttmonechoadmincodecinterval', 'rttmonechoadmincodecpayload', 'rttmonechoadmincodecnumpackets', 'rttmonechoadminicpifadvfactor', 'rttmonechoadminlspfectype', 'rttmonechoadminlspselector', 'rttmonechoadminlspreplymode', 'rttmonechoadminlspttl', 'rttmonechoadminlspexp', 'rttmonechoadminprecision', 'rttmonechoadminprobepakpriority', 'rttmonechoadminowntpsynctolabs', 'rttmonechoadminowntpsynctolpct', 'rttmonechoadminowntpsynctoltype', 'rttmonechoadmincallednumber', 'rttmonechoadmindetectpoint', 'rttmonechoadmingkregistration', 'rttmonechoadminsourcevoiceport', 'rttmonechoadmincallduration', 'rttmonechoadminlspreplydscp', 'rttmonechoadminlspnullshim', 'rttmonechoadmintargetmpid', 'rttmonechoadmintargetdomainname', 'rttmonechoadmintargetvlan', 'rttmonechoadminethernetcos', 'rttmonechoadminlspvccvid', 'rttmonechoadmintargetevc', 'rttmonechoadmintargetmepport', 'rttmonechoadminvideotrafficprofile', 'rttmonechoadmindscp', 'rttmonechoadminreservedsp', 'rttmonechoadmininputinterface', 'rttmonechoadminemulatesourceaddress', 'rttmonechoadminemulatesourceport', 'rttmonechoadminemulatetargetaddress', 'rttmonechoadminemulatetargetport', 'rttmonechoadmintargetmacaddress', 'rttmonechoadminsourcemacaddress', 'rttmonechoadminsourcempid', 'rttmonechoadminendpointlistname', 'rttmonechoadminssm', 'rttmonechoadmincontrolretry', 'rttmonechoadmincontroltimeout', 'rttmonechoadminigmptreeinit', 'rttmonechoadminenableburst', 'rttmonechoadminaggburstcycles', 'rttmonechoadminlossrationumframes', 'rttmonechoadminavailnumframes', 'rttmonechoadmintstampoptimization'], name, value)

            class Rttmonechoadminlspfectype(Enum):
                """
                Rttmonechoadminlspfectype (Enum Class)

                The type of the target FEC for the RTT 'echo' and 'pathEcho'

                operations based on 'mplsLspPingAppl' RttMonProtocol.

                ldpIpv4Prefix   \- LDP IPv4 prefix.

                .. data:: ldpIpv4Prefix = 1

                """

                ldpIpv4Prefix = Enum.YLeaf(1, "ldpIpv4Prefix")


            class Rttmonechoadminowntpsynctoltype(Enum):
                """
                Rttmonechoadminowntpsynctoltype (Enum Class)

                This object specifies whether the value in specified for oneway

                NTP sync tolerance is absolute value or percent value

                .. data:: percent = 1

                .. data:: absolute = 2

                """

                percent = Enum.YLeaf(1, "percent")

                absolute = Enum.YLeaf(2, "absolute")


            class Rttmonechoadminprecision(Enum):
                """
                Rttmonechoadminprecision (Enum Class)

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


            class Rttmonechoadminprobepakpriority(Enum):
                """
                Rttmonechoadminprobepakpriority (Enum Class)

                This object specifies the priority that will be assigned

                to probe packet.  This value can be set only for jitter 

                operation

                .. data:: normal = 1

                .. data:: high = 2

                """

                normal = Enum.YLeaf(1, "normal")

                high = Enum.YLeaf(2, "high")


            class Rttmonechoadminreservedsp(Enum):
                """
                Rttmonechoadminreservedsp (Enum Class)

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



    class Rttmonfileioadmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonfileioadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonfileioadmintable, self).__init__()

            self.yang_name = "rttMonFileIOAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonFileIOAdminEntry", ("rttmonfileioadminentry", CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry))])
            self._leafs = OrderedDict()

            self.rttmonfileioadminentry = YList(self)
            self._segment_path = lambda: "rttMonFileIOAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonfileioadmintable, [], name, value)


        class Rttmonfileioadminentry(Entity):
            """
            A list of objects that define specific configuration for
            'fileIO' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonfileioadminfilepath
            
            	The fully qualified file path that will be the target of the RTT operation.  This value must match one of the rttMonApplPreConfigedName entries
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminsize
            
            	The size of the file to write/read from the File Server
            	**type**\:  :py:class:`Rttmonfileioadminsize <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry.Rttmonfileioadminsize>`
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminaction
            
            	The File I/O action to be performed
            	**type**\:  :py:class:`Rttmonfileioadminaction <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry.Rttmonfileioadminaction>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry, self).__init__()

                self.yang_name = "rttMonFileIOAdminEntry"
                self.yang_parent_name = "rttMonFileIOAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonfileioadminfilepath', YLeaf(YType.str, 'rttMonFileIOAdminFilePath')),
                    ('rttmonfileioadminsize', YLeaf(YType.enumeration, 'rttMonFileIOAdminSize')),
                    ('rttmonfileioadminaction', YLeaf(YType.enumeration, 'rttMonFileIOAdminAction')),
                ])
                self.rttmonctrladminindex = None
                self.rttmonfileioadminfilepath = None
                self.rttmonfileioadminsize = None
                self.rttmonfileioadminaction = None
                self._segment_path = lambda: "rttMonFileIOAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonFileIOAdminTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonfileioadmintable.Rttmonfileioadminentry, ['rttmonctrladminindex', 'rttmonfileioadminfilepath', 'rttmonfileioadminsize', 'rttmonfileioadminaction'], name, value)

            class Rttmonfileioadminaction(Enum):
                """
                Rttmonfileioadminaction (Enum Class)

                The File I/O action to be performed.

                .. data:: write = 1

                .. data:: read = 2

                .. data:: writeRead = 3

                """

                write = Enum.YLeaf(1, "write")

                read = Enum.YLeaf(2, "read")

                writeRead = Enum.YLeaf(3, "writeRead")


            class Rttmonfileioadminsize(Enum):
                """
                Rttmonfileioadminsize (Enum Class)

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



    class Rttmonscriptadmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonscriptadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonscriptadmintable.Rttmonscriptadminentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonscriptadmintable, self).__init__()

            self.yang_name = "rttMonScriptAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonScriptAdminEntry", ("rttmonscriptadminentry", CISCORTTMONMIB.Rttmonscriptadmintable.Rttmonscriptadminentry))])
            self._leafs = OrderedDict()

            self.rttmonscriptadminentry = YList(self)
            self._segment_path = lambda: "rttMonScriptAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonscriptadmintable, [], name, value)


        class Rttmonscriptadminentry(Entity):
            """
            A list of objects that define specific configuration for
            'script' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonscriptadminname
            
            	This will be the Name of the Script that will be used to generate RTT operations.    This object must match one of the  rttMonApplPreConfigedName entries
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonscriptadmincmdlineparams
            
            	This will be the actual command line parameters passed to the rttMonScriptAdminName when being executed
            	**type**\: str
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonscriptadmintable.Rttmonscriptadminentry, self).__init__()

                self.yang_name = "rttMonScriptAdminEntry"
                self.yang_parent_name = "rttMonScriptAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonscriptadminname', YLeaf(YType.str, 'rttMonScriptAdminName')),
                    ('rttmonscriptadmincmdlineparams', YLeaf(YType.str, 'rttMonScriptAdminCmdLineParams')),
                ])
                self.rttmonctrladminindex = None
                self.rttmonscriptadminname = None
                self.rttmonscriptadmincmdlineparams = None
                self._segment_path = lambda: "rttMonScriptAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonScriptAdminTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonscriptadmintable.Rttmonscriptadminentry, ['rttmonctrladminindex', 'rttmonscriptadminname', 'rttmonscriptadmincmdlineparams'], name, value)


    class Rttmonreacttriggeradmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonreacttriggeradminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonreacttriggeradmintable, self).__init__()

            self.yang_name = "rttMonReactTriggerAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonReactTriggerAdminEntry", ("rttmonreacttriggeradminentry", CISCORTTMONMIB.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry))])
            self._leafs = OrderedDict()

            self.rttmonreacttriggeradminentry = YList(self)
            self._segment_path = lambda: "rttMonReactTriggerAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonreacttriggeradmintable, [], name, value)


        class Rttmonreacttriggeradminentry(Entity):
            """
            A list of objects that will be triggered when
            a reaction condition is violated.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonreacttriggeradminrttmonctrladminindex  (key)
            
            	This object points to a single conceptual Rtt control row.  If this row does not exist and this value is  triggered no action will result.  The conceptual Rtt control row will be triggered for the  rttMonCtrlOperRttLife length.  If this conceptual Rtt control row is already active, rttMonCtrlOperRttLife will not be updated, and its life will continue as previously  defined
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonreacttriggeradminstatus
            
            	This object is used to create Trigger entries
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rttmonreacttriggeroperstate
            
            	This object takes on the value active when its associated entry in the  rttMonReactTriggerAdminTable has been triggered.  When the associated entry in the rttMonReactTriggerAdminTable is not under a trigger state, this object will be pending.  When this object is in the active state this entry can not be retriggered
            	**type**\:  :py:class:`Rttmonreacttriggeroperstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry.Rttmonreacttriggeroperstate>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry, self).__init__()

                self.yang_name = "rttMonReactTriggerAdminEntry"
                self.yang_parent_name = "rttMonReactTriggerAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonreacttriggeradminrttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonreacttriggeradminrttmonctrladminindex', YLeaf(YType.int32, 'rttMonReactTriggerAdminRttMonCtrlAdminIndex')),
                    ('rttmonreacttriggeradminstatus', YLeaf(YType.enumeration, 'rttMonReactTriggerAdminStatus')),
                    ('rttmonreacttriggeroperstate', YLeaf(YType.enumeration, 'rttMonReactTriggerOperState')),
                ])
                self.rttmonctrladminindex = None
                self.rttmonreacttriggeradminrttmonctrladminindex = None
                self.rttmonreacttriggeradminstatus = None
                self.rttmonreacttriggeroperstate = None
                self._segment_path = lambda: "rttMonReactTriggerAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonReactTriggerAdminRttMonCtrlAdminIndex='" + str(self.rttmonreacttriggeradminrttmonctrladminindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonReactTriggerAdminTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry, ['rttmonctrladminindex', 'rttmonreacttriggeradminrttmonctrladminindex', 'rttmonreacttriggeradminstatus', 'rttmonreacttriggeroperstate'], name, value)

            class Rttmonreacttriggeroperstate(Enum):
                """
                Rttmonreacttriggeroperstate (Enum Class)

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



    class Rttmonechopathadmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonechopathadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonechopathadmintable.Rttmonechopathadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonechopathadmintable, self).__init__()

            self.yang_name = "rttMonEchoPathAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonEchoPathAdminEntry", ("rttmonechopathadminentry", CISCORTTMONMIB.Rttmonechopathadmintable.Rttmonechopathadminentry))])
            self._leafs = OrderedDict()

            self.rttmonechopathadminentry = YList(self)
            self._segment_path = lambda: "rttMonEchoPathAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonechopathadmintable, [], name, value)


        class Rttmonechopathadminentry(Entity):
            """
            A list of objects that define intermediate hop's IP Address.
            
            This entry can be added only if the rttMonCtrlAdminRttType is
            'echo'. The entry gets deleted when the corresponding RTR entry,
            which has an index of rttMonCtrlAdminIndex, is deleted.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonechopathadminhopindex  (key)
            
            	Uniquely identifies a row in the rttMonEchoPathAdminTable. This number represents the hop address number in a specific  ping path. All the indicies should start from 1 and must be  contiguous ie., entries should be  (say rttMonCtrlAdminIndex = 1)  1.1, 1.2, 1.3, they cannot be 1.1, 1.2, 1.4
            	**type**\: int
            
            	**range:** 1..8
            
            .. attribute:: rttmonechopathadminhopaddress
            
            	A string which specifies the address of an intermediate hop's IP Address for a RTT 'echo' operation
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonechopathadmintable.Rttmonechopathadminentry, self).__init__()

                self.yang_name = "rttMonEchoPathAdminEntry"
                self.yang_parent_name = "rttMonEchoPathAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonechopathadminhopindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonechopathadminhopindex', YLeaf(YType.int32, 'rttMonEchoPathAdminHopIndex')),
                    ('rttmonechopathadminhopaddress', YLeaf(YType.str, 'rttMonEchoPathAdminHopAddress')),
                ])
                self.rttmonctrladminindex = None
                self.rttmonechopathadminhopindex = None
                self.rttmonechopathadminhopaddress = None
                self._segment_path = lambda: "rttMonEchoPathAdminEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonEchoPathAdminHopIndex='" + str(self.rttmonechopathadminhopindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonEchoPathAdminTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonechopathadmintable.Rttmonechopathadminentry, ['rttmonctrladminindex', 'rttmonechopathadminhopindex', 'rttmonechopathadminhopaddress'], name, value)


    class Rttmongrpscheduleadmintable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmongrpscheduleadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmongrpscheduleadmintable, self).__init__()

            self.yang_name = "rttMonGrpScheduleAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonGrpScheduleAdminEntry", ("rttmongrpscheduleadminentry", CISCORTTMONMIB.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry))])
            self._leafs = OrderedDict()

            self.rttmongrpscheduleadminentry = YList(self)
            self._segment_path = lambda: "rttMonGrpScheduleAdminTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmongrpscheduleadmintable, [], name, value)


        class Rttmongrpscheduleadminentry(Entity):
            """
            A list of objects that define a conceptual group scheduling
            control row.
            
            .. attribute:: rttmongrpscheduleadminindex  (key)
            
            	Uniquely identifies a row in the rttMonGrpScheduleAdminTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMonGrpScheduleAdminStatus object. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmongrpscheduleadminprobes
            
            	A string which holds the different probes which are to be group scheduled. The probes can be specified in the following forms. (a) Individual ID's with comma separated as 23,45,34. (b) Range form including hyphens with multiple ranges being     separated by a comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25.  Any whitespace in the string is considered an error. Duplicates and overlapping ranges as an example 1,2,3,2\-10 are considered fine. For a single range like 1\-20 the upper value (in this example 20) must be greater than lower value (1), otherwise it's treated as an error. The agent will not normalize the list e.g., it will not change 1,2,1\-10 or even 1,2,3,4,5,6.. to 1\-10
            	**type**\: str
            
            	**length:** 0..200
            
            .. attribute:: rttmongrpscheduleadminperiod
            
            	Specifies the time duration over which all the probes have to be scheduled
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfrequency
            
            	Specifies the duration between initiating each RTT operation for all the probes specified in the group.  The value of this object is only effective when both rttMonGrpScheduleAdminFreqMax and rttMonGrpScheduleAdminFreqMin  have zero values
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminlife
            
            	This object specifies the life of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminRttLife object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the probes listed in rttMonGrpScheduleAdminProbes,  will not decrement. And thus the life time of the probes will never end
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminageout
            
            	This object specifies the ageout value of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminConceptRowAgeout object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  When this value is set to zero, the probes listed in rttMonGrpScheduleAdminProbes, will never ageout
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminstatus
            
            	The status of the conceptual RTT group schedule control row.  In order for this object to become active, the following row objects must be defined\:  \- rttMonGrpScheduleAdminProbes  \- rttMonGrpScheduleAdminPeriod All other objects can assume default values.  The conceptual RTT group schedule control row objects cannot be modified once this conceptual RTT group schedule control row has been created. Once this object is in 'active' status, it cannot be set to 'notInService'. When this object moves to 'active' state it will schedule the probes of the rttMonCtrlAdminTable which had been created using 'createAndWait'.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the probes of the rttMonCtrlAdminTable, which had been group scheduled by it earlier, before destroying the RTT group schedule control row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rttmongrpscheduleadminfreqmax
            
            	Specifies the max duration between initiating each RTT operation for all the probes specified in the group.  If this is 0 and rttMonGrpScheduleAdminFreqMin is also 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfreqmin
            
            	Specifies the min duration between initiating each RTT operation for all the probes specified in the group.  The value of this object cannot be greater than the value of rttMonGrpScheduleAdminFreqMax.  If this is 0 and rttMonGrpScheduleAdminFreqMax is 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminstarttime
            
            	This is the time in seconds after which the member probes of this group specified in rttMonGrpScheduleAdminProbes will transition to active state
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminadd
            
            	Addition of members to an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are added to the existing group
            	**type**\: bool
            
            .. attribute:: rttmongrpscheduleadmindelete
            
            	Removal of members from an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are removed from the existing group
            	**type**\: bool
            
            .. attribute:: rttmongrpscheduleadminreset
            
            	When this is set to true then all members of this group will be stopped and rescheduled using the previously set values of this group
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry, self).__init__()

                self.yang_name = "rttMonGrpScheduleAdminEntry"
                self.yang_parent_name = "rttMonGrpScheduleAdminTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmongrpscheduleadminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmongrpscheduleadminindex', YLeaf(YType.int32, 'rttMonGrpScheduleAdminIndex')),
                    ('rttmongrpscheduleadminprobes', YLeaf(YType.str, 'rttMonGrpScheduleAdminProbes')),
                    ('rttmongrpscheduleadminperiod', YLeaf(YType.int32, 'rttMonGrpScheduleAdminPeriod')),
                    ('rttmongrpscheduleadminfrequency', YLeaf(YType.int32, 'rttMonGrpScheduleAdminFrequency')),
                    ('rttmongrpscheduleadminlife', YLeaf(YType.int32, 'rttMonGrpScheduleAdminLife')),
                    ('rttmongrpscheduleadminageout', YLeaf(YType.int32, 'rttMonGrpScheduleAdminAgeout')),
                    ('rttmongrpscheduleadminstatus', YLeaf(YType.enumeration, 'rttMonGrpScheduleAdminStatus')),
                    ('rttmongrpscheduleadminfreqmax', YLeaf(YType.int32, 'rttMonGrpScheduleAdminFreqMax')),
                    ('rttmongrpscheduleadminfreqmin', YLeaf(YType.int32, 'rttMonGrpScheduleAdminFreqMin')),
                    ('rttmongrpscheduleadminstarttime', YLeaf(YType.int32, 'rttMonGrpScheduleAdminStartTime')),
                    ('rttmongrpscheduleadminadd', YLeaf(YType.boolean, 'rttMonGrpScheduleAdminAdd')),
                    ('rttmongrpscheduleadmindelete', YLeaf(YType.boolean, 'rttMonGrpScheduleAdminDelete')),
                    ('rttmongrpscheduleadminreset', YLeaf(YType.boolean, 'rttMonGrpScheduleAdminReset')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry, ['rttmongrpscheduleadminindex', 'rttmongrpscheduleadminprobes', 'rttmongrpscheduleadminperiod', 'rttmongrpscheduleadminfrequency', 'rttmongrpscheduleadminlife', 'rttmongrpscheduleadminageout', 'rttmongrpscheduleadminstatus', 'rttmongrpscheduleadminfreqmax', 'rttmongrpscheduleadminfreqmin', 'rttmongrpscheduleadminstarttime', 'rttmongrpscheduleadminadd', 'rttmongrpscheduleadmindelete', 'rttmongrpscheduleadminreset'], name, value)


    class Rttmplsvpnmonctrltable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmplsvpnmonctrlentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmplsvpnmonctrltable, self).__init__()

            self.yang_name = "rttMplsVpnMonCtrlTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMplsVpnMonCtrlEntry", ("rttmplsvpnmonctrlentry", CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry))])
            self._leafs = OrderedDict()

            self.rttmplsvpnmonctrlentry = YList(self)
            self._segment_path = lambda: "rttMplsVpnMonCtrlTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmplsvpnmonctrltable, [], name, value)


        class Rttmplsvpnmonctrlentry(Entity):
            """
            A base list of objects that define a conceptual Auto SAA L3
            MPLS VPN control row.
            
            .. attribute:: rttmplsvpnmonctrlindex  (key)
            
            	Uniquely identifies a row in the rttMplsVpnMonCtrlTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMplsVpnMonCtrlStatus object.  If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmplsvpnmonctrlrtttype
            
            	The type of RTT operation to be performed for Auto SAA L3 MPLS VPN.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  This value must be set before setting any other parameter configuration of an Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`RttMplsVpnMonRttType <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonRttType>`
            
            .. attribute:: rttmplsvpnmonctrlvrfname
            
            	This field is used to specify the VPN name for which the Auto SAA L3 MPLS VPN RTT operation will be used.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  The Auto SAA L3 MPLS VPN will find the PEs participating in this VPN and configure RTT operation corresponding to value specified in rttMplsVpnMonCtrlRttType.  If the VPN corresponds to the value configured for this object doesn't exist 'inconsistentValue' error will be returned.  The value 'saa\-vrf\-all' has a special meaning. When this object is set to 'saa\-vrf\-all', all the VPNs in the PE will be discovered and Auto SAA L3 MPLS VPN will configure RTT operations corresponding to all these PEs with the value specified in rttMplsVpnMonCtrlRttType as type for those operations.  So, the user should avoid using this string for a particular VPN name when using this feature in order to avoid ambiguity
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: rttmplsvpnmonctrltag
            
            	A string which is used by a managing application to identify the RTT target.  This string will be configured as rttMonCtrlAdminTag for all the operations configured by this Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminTag in RTT operation
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: rttmplsvpnmonctrlthreshold
            
            	This object defines an administrative threshold limit.  This value will be configured as rttMonCtrlAdminThreshold for all the operations that will be configured by the current Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminThreshold
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrltimeout
            
            	Specifies the duration to wait for a RTT operation configured automatically by the Auto SAA L3 MPLS VPN to complete.   The value of this object cannot be set to a value which would specify a duration exceeding rttMplsVpnMonScheduleFrequency.  The usage of this value in Auto SAA L3 MPLS VPN is similar to rttMonCtrlAdminTimeout
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrlscaninterval
            
            	Specifies the frequency at which the automatic PE addition should take place if there is any for an Auto SAA L3 MPLS VPN.  New RTT operations corresponding to the new PEs discovered will be created and scheduled.  The default value for this object is 4 hours. The maximum value supported is 49 days
            	**type**\: int
            
            	**range:** 1..70560
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmonctrldelscanfactor
            
            	Specifies the frequency at which the automatic PE deletion should take place.  This object specifies the number of times of rttMonMplslmCtrlScanInterval (rttMplsVpnMonCtrlDelScanFactor \* rttMplsVpnMonCtrlScanInterval) to wait before removing the PEs. This object doesn't directly specify the explicit value to wait before removing the PEs that were down.  If this object set 0 the entries will never removed
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmplsvpnmonctrlexp
            
            	This object represents the EXP value that needs to be put as precedence bit of an IP header
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: rttmplsvpnmonctrlrequestsize
            
            	This object represents the native payload size that needs to be put on the packet.  This value will be configured as rttMonEchoAdminPktDataRequestSize for all the RTT operations configured by the current Auto SAA L3 MPLS VPN.  The minimum request size for jitter probe is 16. The maximum for jitter probe is 1500. The default request size is 32 for jitter probe.  For echo and pathEcho default request size is 28. The minimum request size for echo and pathEcho is 28 bytes
            	**type**\: int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmplsvpnmonctrlverifydata
            
            	When set to true, the resulting data in each RTT operation created by the current Auto SAA L3 MPLS VPN is compared with the expected data. This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object of each RTT operation created by the current Auto SAA L3 MPLS VPN
            	**type**\: bool
            
            .. attribute:: rttmplsvpnmonctrlstoragetype
            
            	The storage type of this conceptual row. When set to 'nonVolatile', this entry will be shown in 'show running' command and can be saved into Non\-volatile memory.  By Default the entry will not be saved into Non\-volatile memory.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: rttmplsvpnmonctrlprobelist
            
            	This object holds the list of probes ID's that are created by the Auto SAA L3 MPLS VPN.  The probes will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\: str
            
            .. attribute:: rttmplsvpnmonctrlstatus
            
            	The status of the conceptual Auto SAA L3 MPLS VPN control row.  In order for this object to become active rttMplsVpnMonCtrlRttType,  rttMplsVpnMonCtrlVrfName and  rttMplsVpnMonSchedulePeriod objects must be defined. All other objects can assume default values.  If the object is set to 'createAndGo' rttMplsVpnMonCtrlRttType, rttMplsVpnMonCtrlVrfName and rttMplsVpnMonSchedulePeriod needs to be set along with rttMplsVpnMonCtrlStatus.  If the object is set to 'createAndWait' rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName needs to be set along with rttMplsVpnMonCtrlStatus. rttMplsVpnMonSchedulePeriod needs to be specified before setting rttMplsVpnMonCtrlStatus to 'active'.  The following objects cannot be modified after creating the Auto SAA L3 MPLS VPN conceptual row.   \- rttMplsVpnMonCtrlRttType  \- rttMplsVpnMonCtrlVrfName  The following objects can be modified even after creating the Auto SAA L3 MPLS VPN conceptual row by setting this object to 'notInService'   \- All other writable objects in rttMplsVpnMonCtrlTable except    rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName.  \- Objects in the rttMplsVpnMonTypeTable.  \- Objects in the rttMplsVpnMonScheduleTable.  The following objects can be modified as needed without setting this object to 'notInService' even after creating the Auto SAA L3 MPLS VPN conceptual row.   \- Objects in rttMplsVpnMonReactTable.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop and destroy all the probes created by this Auto SAA L3 MPLS VPN before destroying Auto SAA L3 MPLS VPN control row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rttmplsvpnmonctrllpd
            
            	When set to true, this implies that LPD (LSP Path Discovery) is enabled for this row.  The Auto SAA L3 MPLS VPN will find all the paths to each of the PE's and configure RTT operation with rttMonCtrlAdminRttType value as 'lspGroup'. The 'lspGroup' probe will walk through the list of set of information that uniquely identifies a path and send the LSP echo requests across them. All these LSP echo requests sent for 1st path, 2nd path etc. can be thought of as 'single probes' sent as a part of 'lspGroup'. These single probes will of type 'rttMplsVpnMonCtrlRttType'.  'lspGroup' probe is a superset of individual probes that will test multiple paths. For example Suppose there are 10 paths to the target. One 'lspGroup' probe will be created which will store all the information related to uniquely identify the 10 paths. When the 'lspGroup' probe will run it will sweep through the set of information for 1st path, 2nd path, 3rd path and so on till it has tested all the paths
            	**type**\: bool
            
            .. attribute:: rttmplsvpnmonctrllpdgrplist
            
            	This object holds the list of LPD Group IDs that are created for this Auto SAA L3 MPLS VPN row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  The LPD Groups will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\: str
            
            .. attribute:: rttmplsvpnmonctrllpdcomptime
            
            	The completion time of the LSP Path Discovery for the entire set of PEs which are discovered for this Auto SAA.  This object will be applicable only when LSP Path Discovery is enabled for this row
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmontypeinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminInterval
            	**type**\: int
            
            	**range:** 1..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypenumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminNumPackets
            	**type**\: int
            
            	**range:** 1..60000
            
            .. attribute:: rttmplsvpnmontypedestport
            
            	This object represents the target's port number to which the packets need to be sent.  This value will be configured as target port for all the operations that is going to be configured   The usage of this value is same as rttMonEchoAdminTargetPort in RTT operation. This object is applicable to jitter type.  If this object is not being set random port will be used as destination port
            	**type**\: int
            
            	**range:** 1..65536
            
            .. attribute:: rttmplsvpnmontypesecfreqtype
            
            	This object specifies the reaction type for which the rttMplsVpnMonTypeSecFreqValue should be applied.  The Value 'timeout' will cause secondary frequency to be set for frequency on timeout condition.  The Value 'connectionLoss' will cause secondary frequency to be set for frequency on connectionloss condition.  The Value 'both' will cause secondary frequency to be set for frequency on either of timeout/connectionloss condition.  Notifications must be configured on corresponding reaction type in order to rttMplsVpnMonTypeSecFreqValue get effect.  When LSP Path Discovery is enabled for this row the following rttMplsVpnMonReactLpdNotifyType notifications must be configured in order to rttMplsVpnMonTypeSecFreqValue get effect.   \- 'lpdGroupStatus' or 'lpdAll'.  Since the Frequency of the operation changes the stats will be collected in new bucket.  If any of the reaction type (timeout/connectionLoss) occurred for an operation configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the frequency of the operation will be changed to rttMplsVpnMonTypeSecFreqValue.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss).   2) A notification is configured for the same reaction type   (timeout/connectionLoss).  When LSP Path Discovery is enabled for this row, if any of the reaction type (timeout/connectionLoss) occurred for 'single probes' configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the secondary frequency rttMplsVpnMonTypeSecFreqValue will be applied to the 'lspGroup' probe.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss/both).   2) rttMplsVpnMonReactLpdNotifyType object must be set to   value of 'lpdGroupStatus' or 'lpdAll'.  The frequency of the individual operations will be restored to original frequency once the trap is sent
            	**type**\:  :py:class:`Rttmplsvpnmontypesecfreqtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmontypesecfreqtype>`
            
            .. attribute:: rttmplsvpnmontypesecfreqvalue
            
            	This object represents the value that needs to be applied to secondary frequency of individual RTT operations configured by Auto SAA L3 MPLS VPN.  Setting rttMplsVpnMonTypeSecFreqValue without setting rttMplsVpnMonTypeSecFreqType will not have any effect
            	**type**\: int
            
            	**range:** 1..604800
            
            .. attribute:: rttmplsvpnmontypelspselector
            
            	A string which specifies the address of the local host (127.X.X.X).  This object will be used as lsp\-selector in MPLS RTT operations configured by the Auto SAA L3 MPLS VPN.  When LSP Path Discovery is enabled for the row, this object will be used to indicate the base LSP selector value to be used in the LSP Path Discovery.  This value of this object is significant in MPLS load balancing scenario. This value will be used as one of the parameter in that load balancing
            	**type**\: str
            
            .. attribute:: rttmplsvpnmontypelspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho
            	**type**\:  :py:class:`RttMonLSPPingReplyMode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonLSPPingReplyMode>`
            
            .. attribute:: rttmplsvpnmontypelspttl
            
            	This object represents the TTL setting for MPLS echo request packets originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho.  For 'echo' the default TTL will be set to 255. For 'pathEcho' the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values will be used for 'echo' and 'pathEcho'
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rttmplsvpnmontypelspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\: int
            
            	**range:** 0..63 \| 255..None
            
            .. attribute:: rttmplsvpnmontypelpdmaxsessions
            
            	This object represents the number of concurrent path discovery requests that will be active at one time per MPLS VPN control row. This object is meant for reducing the time for discovery of all the paths to the target in a large customer network. However its value should be chosen such that it does not cause any performance impact.  Note\: If the customer network has low end routers in the Core it is recommended to keep this value low
            	**type**\: int
            
            	**range:** 1..15
            
            .. attribute:: rttmplsvpnmontypelpdsesstimeout
            
            	This object specifies the maximum allowed duration of a particular tree trace request.  If no response is received in configured time the request will be considered a failure
            	**type**\: int
            
            	**range:** 1..900
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmontypelpdechotimeout
            
            	This object specifies the timeout value for the LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\: int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechointerval
            
            	This object specifies the send interval between LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\: int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechonullshim
            
            	This object specifies if the explicit\-null label is added to LSP echo requests which are sent while performing the LSP Path Discovery.  If set to TRUE all the probes configured as part of this control row will send the LSP echo requests with the explicit\-null label added
            	**type**\: bool
            
            .. attribute:: rttmplsvpnmontypelpdscanperiod
            
            	This object specifies the scan time for the completion of LSP Path Discovery for all the PEs discovered for this control row. If the scan period is exceeded on completion of the LSP Path Discovery for all the PEs, the next discovery will start immediately else it will wait till expiry of scan period.  For example\: If the value is set to 30 minutes then on start of the LSP Path Discovery a timestamp will be taken say T1. At the end of the tree trace discovery one more timestamp will be taken again say T2. If (T2\-T1) is greater than 30, the next discovery will start immediately else next discovery  will wait for [30 \- (T2\-T1)].  Note\: If the object is set to a special value of '0', it will force immediate start of the next discovery on all neighbours without any delay
            	**type**\: int
            
            	**range:** 0..7200
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmontypelpdstathours
            
            	The maximum number of hours of data to be kept per LPD group. The LPD group statistics will be kept in an hourly bucket. At the maximum there can be two buckets. The value of 'one' is not advisable because the group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value used in the rttMplsVpnLpdGroupStatsTable to uniquely identify this group is the rttMonStatsCaptureStartTimeIndex.  Note\: When this object is set to the value of '0' all rttMplsVpnLpdGroupStatsTable data capturing will be shut off
            	**type**\: int
            
            	**range:** 0..2
            
            .. attribute:: rttmplsvpnmonschedulerttstarttime
            
            	This is the time when this conceptual row will activate. rttMplsVpnMonSchedulePeriod object must be specified before setting this object.  This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will cause the activation of a conceptual Auto SAA L3 MPLS VPN row.  When an agent has the capability to determine date and time, the agent should store this object as DateAndTime. This allows the agent to be able to activate conceptual Auto SAA L3 MPLS VPN row at the intended time.  If this object has value as 1, this means start the operation now itself. Value of 0 puts the operation in pending state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmplsvpnmonscheduleperiod
            
            	Specifies the time duration over which all the probes created by the current Auto SAA L3 MPLS VPN have to be scheduled.  This object must be set first before setting rttMplsVpnMonScheduleRttStartTime
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonschedulefrequency
            
            	Specifies the duration between initiating each RTT operation configured by the Auto SAA L3 MPLS VPN.  This object cannot be set to a value which would be a shorter duration than rttMplsVpnMonCtrlTimeout.  The usage of this value in RTT operation is same as rttMonCtrlAdminFrequency
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonreactconnectionenable
            
            	The value set for this will be applied as rttMonReactAdminConnectionEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'connectionLoss(8)'
            	**type**\: bool
            
            .. attribute:: rttmplsvpnmonreacttimeoutenable
            
            	The value set for this will be applied as rttMonReactAdminTimeoutEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'timeout(7)'
            	**type**\: bool
            
            .. attribute:: rttmplsvpnmonreactthresholdtype
            
            	The value corresponding to this object will be applied as rttMonReactAdminThresholdType for individual probes created by the Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactThresholdType for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`Rttmplsvpnmonreactthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactthresholdtype>`
            
            .. attribute:: rttmplsvpnmonreactthresholdcount
            
            	This object value will be applied as rttMonReactAdminThresholdCount for individual probes created by the Auto SAA L3 MPLS VPN.  This object value will be applied as rttMonReactThresholdCountX for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: rttmplsvpnmonreactactiontype
            
            	The value corresponding to this object will be applied as rttMonReactAdminActionType of individual probes created by this Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactActionType of individual probes created by this Auto SAA L3 MPLS VPN
            	**type**\:  :py:class:`Rttmplsvpnmonreactactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactactiontype>`
            
            .. attribute:: rttmplsvpnmonreactlpdnotifytype
            
            	This object specifies the type of LPD notifications to be generated for the current Auto SAA L3 MPLS VPN control row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  There are two types of notifications supported for the LPD \- (a) rttMonLpdDiscoveryNotification \- This notification will     be sent on the failure of LSP Path Discovery to the     particular PE. Reversal of the failure will also result in     sending the notification. (b) rttMonLpdGrpStatusNotification \- Individual probes in an LPD     group will not generate notifications independently but will     be generating dependent on the state of the group. Any     individual probe can initiate the generation of a     notification, dependent on the state of the group.     Notifications are only generated if the failure/restoration     of an individual probe causes the state of the group to     change.  The Value 'none' will not cause any notifications to be sent.  The Value 'lpdPathDiscovery' will cause (a) to be sent.  The Value 'lpdGroupStatus' will cause (b) to be sent.  The Value 'lpdAll' will cause both (a) and (b) to sent depending on the failure conditions
            	**type**\:  :py:class:`Rttmplsvpnmonreactlpdnotifytype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactlpdnotifytype>`
            
            .. attribute:: rttmplsvpnmonreactlpdretrycount
            
            	This object value specifies the number of attempts to be performed before declaring the path as 'down'. Each 'single probe' which is part of 'lspGroup' probe will be retried these many times before marking it as 'down'.  This object will be applicable only when LSP Path Discovery is enabled for this row.    \- When rttMplsVpnMonTypeSecFreqType is not configured, the     failure count will be incremented at the next cycle of     'lspGroup' probe at interval's of     rttMplsVpnMonScheduleFrequency value.      For example\: Assume there are 10 paths discovered and on     the first run of the 'lspGroup' probe first two paths failed     and rest passed. On the second run all the probes will be      run again. The probes 1 and 2 will be retried till the     rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured.    \- When rttMplsVpnMonTypeSecFreqType value is anything other     than 'none', the retry will happen for the failed probes at     the rttMplsVpnMonTypeSecFreqValue and only the failed     probes will be retried.      For example\: Assume there are 10 paths discovered and on the     first run of the 'lspGroup' probe first two paths failed and     rest passed. The secondary frequency will be applied to the     failed probes. At secondary frequency interval the first two     probes will be run again. The probes 1 and 2 will be retried     till the rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured
            	**type**\: int
            
            	**range:** 1..16
            
            	**units**\: attempts
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry, self).__init__()

                self.yang_name = "rttMplsVpnMonCtrlEntry"
                self.yang_parent_name = "rttMplsVpnMonCtrlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmplsvpnmonctrlindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmplsvpnmonctrlindex', YLeaf(YType.int32, 'rttMplsVpnMonCtrlIndex')),
                    ('rttmplsvpnmonctrlrtttype', YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlRttType')),
                    ('rttmplsvpnmonctrlvrfname', YLeaf(YType.str, 'rttMplsVpnMonCtrlVrfName')),
                    ('rttmplsvpnmonctrltag', YLeaf(YType.str, 'rttMplsVpnMonCtrlTag')),
                    ('rttmplsvpnmonctrlthreshold', YLeaf(YType.int32, 'rttMplsVpnMonCtrlThreshold')),
                    ('rttmplsvpnmonctrltimeout', YLeaf(YType.int32, 'rttMplsVpnMonCtrlTimeout')),
                    ('rttmplsvpnmonctrlscaninterval', YLeaf(YType.int32, 'rttMplsVpnMonCtrlScanInterval')),
                    ('rttmplsvpnmonctrldelscanfactor', YLeaf(YType.int32, 'rttMplsVpnMonCtrlDelScanFactor')),
                    ('rttmplsvpnmonctrlexp', YLeaf(YType.int32, 'rttMplsVpnMonCtrlEXP')),
                    ('rttmplsvpnmonctrlrequestsize', YLeaf(YType.int32, 'rttMplsVpnMonCtrlRequestSize')),
                    ('rttmplsvpnmonctrlverifydata', YLeaf(YType.boolean, 'rttMplsVpnMonCtrlVerifyData')),
                    ('rttmplsvpnmonctrlstoragetype', YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlStorageType')),
                    ('rttmplsvpnmonctrlprobelist', YLeaf(YType.str, 'rttMplsVpnMonCtrlProbeList')),
                    ('rttmplsvpnmonctrlstatus', YLeaf(YType.enumeration, 'rttMplsVpnMonCtrlStatus')),
                    ('rttmplsvpnmonctrllpd', YLeaf(YType.boolean, 'rttMplsVpnMonCtrlLpd')),
                    ('rttmplsvpnmonctrllpdgrplist', YLeaf(YType.str, 'rttMplsVpnMonCtrlLpdGrpList')),
                    ('rttmplsvpnmonctrllpdcomptime', YLeaf(YType.int32, 'rttMplsVpnMonCtrlLpdCompTime')),
                    ('rttmplsvpnmontypeinterval', YLeaf(YType.int32, 'rttMplsVpnMonTypeInterval')),
                    ('rttmplsvpnmontypenumpackets', YLeaf(YType.int32, 'rttMplsVpnMonTypeNumPackets')),
                    ('rttmplsvpnmontypedestport', YLeaf(YType.int32, 'rttMplsVpnMonTypeDestPort')),
                    ('rttmplsvpnmontypesecfreqtype', YLeaf(YType.enumeration, 'rttMplsVpnMonTypeSecFreqType')),
                    ('rttmplsvpnmontypesecfreqvalue', YLeaf(YType.int32, 'rttMplsVpnMonTypeSecFreqValue')),
                    ('rttmplsvpnmontypelspselector', YLeaf(YType.str, 'rttMplsVpnMonTypeLspSelector')),
                    ('rttmplsvpnmontypelspreplymode', YLeaf(YType.enumeration, 'rttMplsVpnMonTypeLSPReplyMode')),
                    ('rttmplsvpnmontypelspttl', YLeaf(YType.int32, 'rttMplsVpnMonTypeLSPTTL')),
                    ('rttmplsvpnmontypelspreplydscp', YLeaf(YType.int32, 'rttMplsVpnMonTypeLSPReplyDscp')),
                    ('rttmplsvpnmontypelpdmaxsessions', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdMaxSessions')),
                    ('rttmplsvpnmontypelpdsesstimeout', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdSessTimeout')),
                    ('rttmplsvpnmontypelpdechotimeout', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdEchoTimeout')),
                    ('rttmplsvpnmontypelpdechointerval', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdEchoInterval')),
                    ('rttmplsvpnmontypelpdechonullshim', YLeaf(YType.boolean, 'rttMplsVpnMonTypeLpdEchoNullShim')),
                    ('rttmplsvpnmontypelpdscanperiod', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdScanPeriod')),
                    ('rttmplsvpnmontypelpdstathours', YLeaf(YType.int32, 'rttMplsVpnMonTypeLpdStatHours')),
                    ('rttmplsvpnmonschedulerttstarttime', YLeaf(YType.uint32, 'rttMplsVpnMonScheduleRttStartTime')),
                    ('rttmplsvpnmonscheduleperiod', YLeaf(YType.int32, 'rttMplsVpnMonSchedulePeriod')),
                    ('rttmplsvpnmonschedulefrequency', YLeaf(YType.int32, 'rttMplsVpnMonScheduleFrequency')),
                    ('rttmplsvpnmonreactconnectionenable', YLeaf(YType.boolean, 'rttMplsVpnMonReactConnectionEnable')),
                    ('rttmplsvpnmonreacttimeoutenable', YLeaf(YType.boolean, 'rttMplsVpnMonReactTimeoutEnable')),
                    ('rttmplsvpnmonreactthresholdtype', YLeaf(YType.enumeration, 'rttMplsVpnMonReactThresholdType')),
                    ('rttmplsvpnmonreactthresholdcount', YLeaf(YType.int32, 'rttMplsVpnMonReactThresholdCount')),
                    ('rttmplsvpnmonreactactiontype', YLeaf(YType.enumeration, 'rttMplsVpnMonReactActionType')),
                    ('rttmplsvpnmonreactlpdnotifytype', YLeaf(YType.enumeration, 'rttMplsVpnMonReactLpdNotifyType')),
                    ('rttmplsvpnmonreactlpdretrycount', YLeaf(YType.int32, 'rttMplsVpnMonReactLpdRetryCount')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry, ['rttmplsvpnmonctrlindex', 'rttmplsvpnmonctrlrtttype', 'rttmplsvpnmonctrlvrfname', 'rttmplsvpnmonctrltag', 'rttmplsvpnmonctrlthreshold', 'rttmplsvpnmonctrltimeout', 'rttmplsvpnmonctrlscaninterval', 'rttmplsvpnmonctrldelscanfactor', 'rttmplsvpnmonctrlexp', 'rttmplsvpnmonctrlrequestsize', 'rttmplsvpnmonctrlverifydata', 'rttmplsvpnmonctrlstoragetype', 'rttmplsvpnmonctrlprobelist', 'rttmplsvpnmonctrlstatus', 'rttmplsvpnmonctrllpd', 'rttmplsvpnmonctrllpdgrplist', 'rttmplsvpnmonctrllpdcomptime', 'rttmplsvpnmontypeinterval', 'rttmplsvpnmontypenumpackets', 'rttmplsvpnmontypedestport', 'rttmplsvpnmontypesecfreqtype', 'rttmplsvpnmontypesecfreqvalue', 'rttmplsvpnmontypelspselector', 'rttmplsvpnmontypelspreplymode', 'rttmplsvpnmontypelspttl', 'rttmplsvpnmontypelspreplydscp', 'rttmplsvpnmontypelpdmaxsessions', 'rttmplsvpnmontypelpdsesstimeout', 'rttmplsvpnmontypelpdechotimeout', 'rttmplsvpnmontypelpdechointerval', 'rttmplsvpnmontypelpdechonullshim', 'rttmplsvpnmontypelpdscanperiod', 'rttmplsvpnmontypelpdstathours', 'rttmplsvpnmonschedulerttstarttime', 'rttmplsvpnmonscheduleperiod', 'rttmplsvpnmonschedulefrequency', 'rttmplsvpnmonreactconnectionenable', 'rttmplsvpnmonreacttimeoutenable', 'rttmplsvpnmonreactthresholdtype', 'rttmplsvpnmonreactthresholdcount', 'rttmplsvpnmonreactactiontype', 'rttmplsvpnmonreactlpdnotifytype', 'rttmplsvpnmonreactlpdretrycount'], name, value)

            class Rttmplsvpnmonreactactiontype(Enum):
                """
                Rttmplsvpnmonreactactiontype (Enum Class)

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


            class Rttmplsvpnmonreactlpdnotifytype(Enum):
                """
                Rttmplsvpnmonreactlpdnotifytype (Enum Class)

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


            class Rttmplsvpnmonreactthresholdtype(Enum):
                """
                Rttmplsvpnmonreactthresholdtype (Enum Class)

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


            class Rttmplsvpnmontypesecfreqtype(Enum):
                """
                Rttmplsvpnmontypesecfreqtype (Enum Class)

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



    class Rttmonreacttable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonreactentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonreacttable, self).__init__()

            self.yang_name = "rttMonReactTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonReactEntry", ("rttmonreactentry", CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry))])
            self._leafs = OrderedDict()

            self.rttmonreactentry = YList(self)
            self._segment_path = lambda: "rttMonReactTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonreacttable, [], name, value)


        class Rttmonreactentry(Entity):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonreactconfigindex  (key)
            
            	This object along with rttMonCtrlAdminIndex identifies a particular reaction\-configuration for a particular probe. This is a pseudo\-random number selected by the management station when creating a row via the rttMonReactStatus. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonreactvar
            
            	This object specifies the type of reaction configured for a probe.  The reaction types 'rtt', 'timeout', and 'connectionLoss'  can be configured for all probe types.  The reaction type 'verifyError' can be configured for all  probe types except RTP probe type.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' and 'maxOfNegativeDS' can be configured for UDP jitter  and ICMP jitter probe types only.  The reaction types 'mos' and 'icpif' can be configured  for UDP jitter and ICMP jitter probe types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter, and  RTP probe types only.  The reaction types 'iaJitterDS', 'frameLossDS', 'mosLQDS',  'mosCQDS', 'rFactorDS', 'iaJitterSD', 'rFactorSD', 'mosCQSD'  can be configured for RTP probe type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter probe  type only
            	**type**\:  :py:class:`RttMonReactVar <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMonReactVar>`
            
            .. attribute:: rttmonreactthresholdtype
            
            	This object specifies the conditions under which the notification ( trap ) is sent.  never       \- rttMonReactOccurred is never set  immediate   \- rttMonReactOccurred is set to 'true' when the               value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,               mos etc ) violates the threshold.               Conversely, rttMonReactOccurred is set to 'false'               when the parameter ( e.g rtt, jitterAvg,               packetLossSD, mos etc ) is below the threshold               limits.  consecutive \- rttMonReactOccurred is set to true when the value               of parameter for which reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold for configured consecutive               times.               Conversely, rttMonReactOccurred is set to false               when the value of parameter ( e.g rtt, jitterAvg               packetLossSD, mos etc ) is below the threshold               limits for the same number of consecutive               operations.  xOfy        \- rttMonReactOccurred is set to true when x               ( as specified by rttMonReactThresholdCountX )               out of the last y ( as specified by               rttMonReacthresholdCountY ) times the value of               parameter for which the reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold.               Conversely, it is set to false when x, out of the               last y times the value of parameter               ( e.g rtt, jitterAvg, packetLossSD, mos ) is               below the threshold limits.               NOTE\: When x > y, the probe will never                     generate a reaction.  average    \- rttMonReactOccurred is set to true when the              average ( rttMonReactThresholdCountX times )              value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,              mos etc ) violates the threshold condition.              Conversely, it is set to false when the              average value of parameter ( e.g rtt, jitterAvg,              packetLossSD, mos etc ) is below the threshold              limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:  :py:class:`Rttmonreactthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry.Rttmonreactthresholdtype>`
            
            .. attribute:: rttmonreactactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched ( reaction\-configuration ) conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated triggerOnly        \- all trigger actions defined for this                      entry are initiated trapAndTrigger     \- both a trap and all trigger actions                      are initiated A trigger action is defined via the rttMonReactTriggerAdminTable
            	**type**\:  :py:class:`Rttmonreactactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry.Rttmonreactactiontype>`
            
            .. attribute:: rttmonreactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 400.    'mosCQDS' is 400.    'rFactorDS' is 80.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  rttMonReactThresholdRising will be 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the conditions specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 310.    'mosCQDS' is 310.    'rFactorDS' is 60.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.    'iaJitterSD' is 20.    'mosCQSD' is 310.    'rFactorSD' is 60.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of rttMonReactThresholdFalling will be 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactthresholdcountx
            
            	If rttMonReactThresholdType value is 'xOfy', this object defines the 'x' value.  If rttMonReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  rttMonReactOccurred as true.  If rttMonReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if rttMonReactThresholdType has value of 'never' and 'immediate'
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: rttmonreactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if rttMonReactThresholdType is 'xOfy'.  For other values of rttMonReactThresholdType, this object is not applicable
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: rttmonreactvalue
            
            	This object will be set when the configured threshold condition is violated as defined by rttMonReactThresholdType and holds the actual value that violated the configured threshold values.  This object is not valid for the following values of rttMonReactVar and It will be always 0\:   \- timeout   \- connectionLoss   \- verifyError
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactoccurred
            
            	This object is set to true when the configured threshold condition is violated as defined by rttMonReactThresholdType. It will be again set to 'false' if the condition reverses.  This object is set to true in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to true.  \- rttMonReactVar is set to connectionLoss and    rttMonCtrlOperConnectionLostOccurred set to true.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to true.  \- For all other values of rttMonReactVar, if the    corresponding value exceeds the configured    rttMonReactThresholdRising.   This object is set to false in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to false.  \- rttMonReactVar is set to connectionLoss and     rttMonCtrlOperConnectionLostOccurred set to false.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to false.  \- For all other values of rttMonReactVar, if the    corresponding value fall below the configured     rttMonReactThresholdFalling.  When the RttMonRttType is 'pathEcho' or 'pathJitter', this object is applied only to the  rttMonEchoAdminTargetAddress and not to intermediate hops to the Target
            	**type**\: bool
            
            .. attribute:: rttmonreactstatus
            
            	This objects indicates the status of the conceptual RTT Reaction Control Row.Only CreateAndGo and destroy  operations are permitted on the row.  When this object moves to active state, the conceptual row having the Reaction configuration for the probe is monitored and the notifications are generated when the threshold violation takes place.  In order for this object to become active rttMonReactVar must be defined. All other objects assume the default value.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration for the probes would exist. The reaction configuration for the probe is removed
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry, self).__init__()

                self.yang_name = "rttMonReactEntry"
                self.yang_parent_name = "rttMonReactTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonreactconfigindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonreactconfigindex', YLeaf(YType.int32, 'rttMonReactConfigIndex')),
                    ('rttmonreactvar', YLeaf(YType.enumeration, 'rttMonReactVar')),
                    ('rttmonreactthresholdtype', YLeaf(YType.enumeration, 'rttMonReactThresholdType')),
                    ('rttmonreactactiontype', YLeaf(YType.enumeration, 'rttMonReactActionType')),
                    ('rttmonreactthresholdrising', YLeaf(YType.int32, 'rttMonReactThresholdRising')),
                    ('rttmonreactthresholdfalling', YLeaf(YType.int32, 'rttMonReactThresholdFalling')),
                    ('rttmonreactthresholdcountx', YLeaf(YType.int32, 'rttMonReactThresholdCountX')),
                    ('rttmonreactthresholdcounty', YLeaf(YType.int32, 'rttMonReactThresholdCountY')),
                    ('rttmonreactvalue', YLeaf(YType.int32, 'rttMonReactValue')),
                    ('rttmonreactoccurred', YLeaf(YType.boolean, 'rttMonReactOccurred')),
                    ('rttmonreactstatus', YLeaf(YType.enumeration, 'rttMonReactStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonreacttable.Rttmonreactentry, ['rttmonctrladminindex', 'rttmonreactconfigindex', 'rttmonreactvar', 'rttmonreactthresholdtype', 'rttmonreactactiontype', 'rttmonreactthresholdrising', 'rttmonreactthresholdfalling', 'rttmonreactthresholdcountx', 'rttmonreactthresholdcounty', 'rttmonreactvalue', 'rttmonreactoccurred', 'rttmonreactstatus'], name, value)

            class Rttmonreactactiontype(Enum):
                """
                Rttmonreactactiontype (Enum Class)

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


            class Rttmonreactthresholdtype(Enum):
                """
                Rttmonreactthresholdtype (Enum Class)

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



    class Rttmongeneratedopertable(Entity):
        """
        This table contains information about the generated
        operation id as part of a parent IP SLA operation. The parent
        operation id is pseudo\-random number, selected by the management 
        station based on an operation started by the management 
        station,when creating a row via the rttMonCtrlAdminStatus
        object in the rttMonCtrlAdminTable table.
        
        .. attribute:: rttmongeneratedoperentry
        
        	An entry in the Generated Oper table corresponding to a child or generated operation as part of a parent IP SLA operation
        	**type**\: list of  		 :py:class:`Rttmongeneratedoperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmongeneratedopertable.Rttmongeneratedoperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmongeneratedopertable, self).__init__()

            self.yang_name = "rttMonGeneratedOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonGeneratedOperEntry", ("rttmongeneratedoperentry", CISCORTTMONMIB.Rttmongeneratedopertable.Rttmongeneratedoperentry))])
            self._leafs = OrderedDict()

            self.rttmongeneratedoperentry = YList(self)
            self._segment_path = lambda: "rttMonGeneratedOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmongeneratedopertable, [], name, value)


        class Rttmongeneratedoperentry(Entity):
            """
            An entry in the Generated Oper table corresponding to
            a child or generated operation as part of a parent
            IP SLA operation.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmongeneratedoperrespipaddrtype  (key)
            
            	The type of Internet address, IPv4 or IPv6, of a responder for an IP SLA operation
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: rttmongeneratedoperrespipaddr  (key)
            
            	The internet address of a responder for IP SLA operation. The type of this address is determined by the value of rttMonGeneratedOperRespIpAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: rttmongeneratedoperctrladminindex
            
            	This is a pseudo\-random number, auto\-generated based to identify a child operation based on a parent  operation started by the management station,when  creating a row via the rttMonCtrlAdminStatus object
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmongeneratedopertable.Rttmongeneratedoperentry, self).__init__()

                self.yang_name = "rttMonGeneratedOperEntry"
                self.yang_parent_name = "rttMonGeneratedOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmongeneratedoperrespipaddrtype','rttmongeneratedoperrespipaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmongeneratedoperrespipaddrtype', YLeaf(YType.enumeration, 'rttMonGeneratedOperRespIpAddrType')),
                    ('rttmongeneratedoperrespipaddr', YLeaf(YType.str, 'rttMonGeneratedOperRespIpAddr')),
                    ('rttmongeneratedoperctrladminindex', YLeaf(YType.uint32, 'rttMonGeneratedOperCtrlAdminIndex')),
                ])
                self.rttmonctrladminindex = None
                self.rttmongeneratedoperrespipaddrtype = None
                self.rttmongeneratedoperrespipaddr = None
                self.rttmongeneratedoperctrladminindex = None
                self._segment_path = lambda: "rttMonGeneratedOperEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonGeneratedOperRespIpAddrType='" + str(self.rttmongeneratedoperrespipaddrtype) + "']" + "[rttMonGeneratedOperRespIpAddr='" + str(self.rttmongeneratedoperrespipaddr) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonGeneratedOperTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmongeneratedopertable.Rttmongeneratedoperentry, ['rttmonctrladminindex', 'rttmongeneratedoperrespipaddrtype', 'rttmongeneratedoperrespipaddr', 'rttmongeneratedoperctrladminindex'], name, value)


    class Rttmonstatscapturetable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonstatscaptureentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonstatscapturetable, self).__init__()

            self.yang_name = "rttMonStatsCaptureTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonStatsCaptureEntry", ("rttmonstatscaptureentry", CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry))])
            self._leafs = OrderedDict()

            self.rttmonstatscaptureentry = YList(self)
            self._segment_path = lambda: "rttMonStatsCaptureTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonstatscapturetable, [], name, value)


        class Rttmonstatscaptureentry(Entity):
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
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	The time when this row was created.  This object is the second index of the  rttMonStatsCaptureTable Table.  The the number of rttMonStatsCaptureStartTimeIndex   groups exceeds the rttMonStatisticsAdminNumHourGroups value, the oldest rttMonStatsCaptureStartTimeIndex  group will be removed and replaced with the new entry.  When the RttMonRttType is 'pathEcho', this object also  uniquely defines a group of paths.  See the  rttMonStatsCaptureEntry object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatscapturepathindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a path for a given value of  rttMonStatsCaptureStartTimeIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of  rttMonStatsCaptureStartTimeIndex, the agent assigns the first instance of a path a value of 1, then second  instance a value of 2, and so on.  The sequence keeps  incrementing until the number of paths equals  rttMonStatisticsAdminNumPaths value, then no new paths  are kept for the current rttMonStatsCaptureStartTimeIndex  group.  NOTE\: A source to target rttMonStatsCapturePathIndex       path will be created for each        rttMonStatsCaptureStartTimeIndex to hold all        errors that occur when a specific path or        connection has not be setup.  This value directly represents the path to a target. We can only support 128 paths
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: rttmonstatscapturehopindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a hop for a given value of  rttMonStatsCapturePathIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of rttMonStatsCapturePathIndex, the agent assigns the first instance of a hop a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  hops equals rttMonStatisticsAdminNumHops value, then no new hops are kept for the current rttMonStatsCapturePathIndex.  This value directly represents a hop along the path to a target, thus we can only support 30 hops.  This value shows the order along the path to a target
            	**type**\: int
            
            	**range:** 1..30
            
            .. attribute:: rttmonstatscapturedistindex  (key)
            
            	This object uniquely defines a statistical distribution bucket for a given value of rttMonStatsCaptureHopIndex.  For a particular value of rttMonStatsCaptureHopIndex, the agent assigns the first instance of a distribution a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  statistics distribution intervals equals  rttMonStatisticsAdminNumDistBuckets value, then all values that fall above the last interval will be placed into the last interval.  Each of these Statistics Distribution Buckets contain  the results of each completion as defined by  rttMonStatisticsAdminDistInterval object
            	**type**\: int
            
            	**range:** 1..20
            
            .. attribute:: rttmonstatscapturecompletions
            
            	The number of RTT operations that have completed without an error and without timing out.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscaptureoverthresholds
            
            	The number of RTT operations successfully completed, but in excess of rttMonCtrlAdminThreshold.  This number is a subset of the accumulation of all  rttMonStatsCaptureCompletions.  The operation time  of these completed operations will be accumulated.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscapturesumcompletiontime
            
            	The accumulated completion time of RTT operations which complete successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturesumcompletiontime2low
            
            	The low order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  Low/High order is defined where the binary number will look as follows\: \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| High order 32 bits    \| Low order 32 bits     \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- For example the number 4294967296 would have all Low order bits as '0' and the rightmost High order bit will be 1 (zeros,1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatscapturesumcompletiontime2high
            
            	The high order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  See the rttMonStatsCaptureSumCompletionTime2Low object for a definition of Low/High Order
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatscapturecompletiontimemax
            
            	The maximum completion time of any RTT operation which completes successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturecompletiontimemin
            
            	The minimum completion time of any RTT operation which completes successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry, self).__init__()

                self.yang_name = "rttMonStatsCaptureEntry"
                self.yang_parent_name = "rttMonStatsCaptureTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex','rttmonstatscapturepathindex','rttmonstatscapturehopindex','rttmonstatscapturedistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonstatscapturestarttimeindex', YLeaf(YType.uint32, 'rttMonStatsCaptureStartTimeIndex')),
                    ('rttmonstatscapturepathindex', YLeaf(YType.int32, 'rttMonStatsCapturePathIndex')),
                    ('rttmonstatscapturehopindex', YLeaf(YType.int32, 'rttMonStatsCaptureHopIndex')),
                    ('rttmonstatscapturedistindex', YLeaf(YType.int32, 'rttMonStatsCaptureDistIndex')),
                    ('rttmonstatscapturecompletions', YLeaf(YType.int32, 'rttMonStatsCaptureCompletions')),
                    ('rttmonstatscaptureoverthresholds', YLeaf(YType.int32, 'rttMonStatsCaptureOverThresholds')),
                    ('rttmonstatscapturesumcompletiontime', YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime')),
                    ('rttmonstatscapturesumcompletiontime2low', YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime2Low')),
                    ('rttmonstatscapturesumcompletiontime2high', YLeaf(YType.uint32, 'rttMonStatsCaptureSumCompletionTime2High')),
                    ('rttmonstatscapturecompletiontimemax', YLeaf(YType.uint32, 'rttMonStatsCaptureCompletionTimeMax')),
                    ('rttmonstatscapturecompletiontimemin', YLeaf(YType.uint32, 'rttMonStatsCaptureCompletionTimeMin')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatscapturepathindex', 'rttmonstatscapturehopindex', 'rttmonstatscapturedistindex', 'rttmonstatscapturecompletions', 'rttmonstatscaptureoverthresholds', 'rttmonstatscapturesumcompletiontime', 'rttmonstatscapturesumcompletiontime2low', 'rttmonstatscapturesumcompletiontime2high', 'rttmonstatscapturecompletiontimemax', 'rttmonstatscapturecompletiontimemin'], name, value)


    class Rttmonstatscollecttable(Entity):
        """
        The statistics collection database.
        
        This table has the exact same behavior as the
        rttMonStatsCaptureTable, except it does not keep
        statistical distribution information.
        
        For a complete table description see
        the rttMonStatsCaptureTable object.
        
        .. attribute:: rttmonstatscollectentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry has the exact same behavior as the  rttMonStatsCaptureEntry, except it does not keep statistical distribution information.  For a complete entry description see the rttMonStatsCaptureEntry object
        	**type**\: list of  		 :py:class:`Rttmonstatscollectentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscollecttable.Rttmonstatscollectentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonstatscollecttable, self).__init__()

            self.yang_name = "rttMonStatsCollectTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonStatsCollectEntry", ("rttmonstatscollectentry", CISCORTTMONMIB.Rttmonstatscollecttable.Rttmonstatscollectentry))])
            self._leafs = OrderedDict()

            self.rttmonstatscollectentry = YList(self)
            self._segment_path = lambda: "rttMonStatsCollectTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonstatscollecttable, [], name, value)


        class Rttmonstatscollectentry(Entity):
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
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatscapturepathindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..128
            
            	**refers to**\:  :py:class:`rttmonstatscapturepathindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatscapturehopindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..30
            
            	**refers to**\:  :py:class:`rttmonstatscapturehopindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatscollectnumdisconnects
            
            	When the RttMonRttType is 'echo' or pathEcho', this object represents the number of times that the target or  hop along the path to a target became disconnected.  For all other values of RttMonRttType, this object will remain zero.  For connectionless protocols this has no meaning, and will consequently remain 0.  When rttMonEchoAdminProtocol is one of snaRUEcho, this is the number of times that an LU\-SSCP session was lost,  for snaLU0EchoAppl, snaLU2EchoAppl, snaLu62Echo, and for  snaLU62EchoAppl, this is the number of times that LU\-LU  session was lost.  Since this error does not indicate any information about the failure of an RTT operation, no response time  information for this instance will be recorded in the  appropriate objects.  If this error occurs and the rttMonStatsCapturePathIndex  cannot be determined, this error will be accumulated in  the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollecttimeouts
            
            	The number of occasions when a RTT operation was not completed before a timeout occurred, i.e. rttMonCtrlAdminTimeout was exceeded.  Since the RTT operation was never completed, the  completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions (in  any of the statistics distribution buckets).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectbusies
            
            	The number of occasions when a RTT operation could not be initiated because a previous RTT operation has not  been completed.  When the RttMonRttType is 'pathEcho' this can occur for both connection oriented protocols and connectionless protocols.  When the RttMonRttType is 'echo' this can only occur for connection oriented protocols such as SNA.   When the initiation of a new operation cannot be started, this object will be incremented and the operation will be omitted.  (The next operation will start at the next  Frequency).  Since, a RTT operation was never initiated,  the completion time of these operations is not  accumulated, nor do they increment  rttMonStatsCaptureCompletions.  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the source  to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectnoconnections
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is the number of occasions when a RTT operation could not be initiated because the connection to the target has not  been established.  For all other RttMonRttTypes this object will remain zero.  This cannot occur for connectionless protocols, but may occur for connection oriented protocols, such as SNA.  Since a RTT operation was never initiated, the completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions.   If this error occurs and the rttMonStatsCapturePathIndex cannot be determined, this error will be accumulated in the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectdrops
            
            	The number of occasions when a RTT operation could not be initiated because some necessary internal resource  (for example memory, or SNA subsystem) was not available, or the operation completion could not be recognized.  Since a RTT operation was never initiated or was not recognized, the completion time of these operations  are not accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected  Distribution Bucket).  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the  source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectsequenceerrors
            
            	When the RttMonRttType is 'echo' of 'pathEcho' this is the number of RTT operation completions received with  an unexpected sequence identifier.  For all other values of RttMonRttType this object will remain zero.  When this has occurred some of the possible reasons may be\:      \- a duplicate packet was received    \- a response was received after it had timed\-out    \- a corrupted packet was received and was not detected  The completion time of these operations are not  accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectverifyerrors
            
            	The number of RTT operation completions received with data that does not compare with the expected data.  The  completion time of these operations are not accumulated,  nor do they increment rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectaddress
            
            	This object only applies when the RttMonRttType is 'echo', 'pathEcho', 'dlsw', 'udpEcho', 'tcpConnect'.   For all other values of the RttMonRttType, this will be  null.   The object is a string which specifies the address of  the target for the this RTT operation.  This address will be the address of the hop along the  path to the rttMonEchoAdminTargetAddress address,  including rttMonEchoAdminTargetAddress address, or just  the rttMonEchoAdminTargetAddress address, when the  path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type  of RTT operation selected, as specified by the  rttMonEchoAdminProtocol object
            	**type**\: str
            
            .. attribute:: rttmoncontrolenableerrors
            
            	The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonControlEnableErrors object is superseded by rttMonStatsCollectCtrlEnErrors
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatsretrieveerrors
            
            	The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonStatsRetrieveErrors object is superseded by rttMonStatsCollectRetrieveErrors
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatscollectctrlenerrors
            
            	The object is same as rttMonControlEnableErrors, with corrected name for consistency.  The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectretrieveerrors
            
            	The object is same as rttMonStatsRetrieveErrors, with corrected name for consistency.  The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonstatscollecttable.Rttmonstatscollectentry, self).__init__()

                self.yang_name = "rttMonStatsCollectEntry"
                self.yang_parent_name = "rttMonStatsCollectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex','rttmonstatscapturepathindex','rttmonstatscapturehopindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonstatscapturestarttimeindex', YLeaf(YType.str, 'rttMonStatsCaptureStartTimeIndex')),
                    ('rttmonstatscapturepathindex', YLeaf(YType.str, 'rttMonStatsCapturePathIndex')),
                    ('rttmonstatscapturehopindex', YLeaf(YType.str, 'rttMonStatsCaptureHopIndex')),
                    ('rttmonstatscollectnumdisconnects', YLeaf(YType.int32, 'rttMonStatsCollectNumDisconnects')),
                    ('rttmonstatscollecttimeouts', YLeaf(YType.int32, 'rttMonStatsCollectTimeouts')),
                    ('rttmonstatscollectbusies', YLeaf(YType.int32, 'rttMonStatsCollectBusies')),
                    ('rttmonstatscollectnoconnections', YLeaf(YType.int32, 'rttMonStatsCollectNoConnections')),
                    ('rttmonstatscollectdrops', YLeaf(YType.int32, 'rttMonStatsCollectDrops')),
                    ('rttmonstatscollectsequenceerrors', YLeaf(YType.int32, 'rttMonStatsCollectSequenceErrors')),
                    ('rttmonstatscollectverifyerrors', YLeaf(YType.int32, 'rttMonStatsCollectVerifyErrors')),
                    ('rttmonstatscollectaddress', YLeaf(YType.str, 'rttMonStatsCollectAddress')),
                    ('rttmoncontrolenableerrors', YLeaf(YType.int32, 'rttMonControlEnableErrors')),
                    ('rttmonstatsretrieveerrors', YLeaf(YType.int32, 'rttMonStatsRetrieveErrors')),
                    ('rttmonstatscollectctrlenerrors', YLeaf(YType.int32, 'rttMonStatsCollectCtrlEnErrors')),
                    ('rttmonstatscollectretrieveerrors', YLeaf(YType.int32, 'rttMonStatsCollectRetrieveErrors')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonstatscollecttable.Rttmonstatscollectentry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatscapturepathindex', 'rttmonstatscapturehopindex', 'rttmonstatscollectnumdisconnects', 'rttmonstatscollecttimeouts', 'rttmonstatscollectbusies', 'rttmonstatscollectnoconnections', 'rttmonstatscollectdrops', 'rttmonstatscollectsequenceerrors', 'rttmonstatscollectverifyerrors', 'rttmonstatscollectaddress', 'rttmoncontrolenableerrors', 'rttmonstatsretrieveerrors', 'rttmonstatscollectctrlenerrors', 'rttmonstatscollectretrieveerrors'], name, value)


    class Rttmonstatstotalstable(Entity):
        """
        The statistics totals database.
        
        This table has the exact same behavior as the
        rttMonStatsCaptureTable, except it only keeps
        60 minute group values.
        
        For a complete table description see
        the rttMonStatsCaptureTable object.
        
        .. attribute:: rttmonstatstotalsentry
        
        	A list of objects which accumulate the results of a series of RTT operations over a 60 minute time period.  This entry has the exact same behavior as the  rttMonStatsCaptureEntry, except it only keeps 60 minute group values.  For a complete entry description see the rttMonStatsCaptureEntry object
        	**type**\: list of  		 :py:class:`Rttmonstatstotalsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatstotalstable.Rttmonstatstotalsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonstatstotalstable, self).__init__()

            self.yang_name = "rttMonStatsTotalsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonStatsTotalsEntry", ("rttmonstatstotalsentry", CISCORTTMONMIB.Rttmonstatstotalstable.Rttmonstatstotalsentry))])
            self._leafs = OrderedDict()

            self.rttmonstatstotalsentry = YList(self)
            self._segment_path = lambda: "rttMonStatsTotalsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonstatstotalstable, [], name, value)


        class Rttmonstatstotalsentry(Entity):
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
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatstotalselapsedtime
            
            	The length of time since this conceptual statistics row was created
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatstotalsinitiations
            
            	The number of RTT operations that have been initiated.  This number includes all RTT operations which succeed  or fail for whatever reason.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonstatstotalstable.Rttmonstatstotalsentry, self).__init__()

                self.yang_name = "rttMonStatsTotalsEntry"
                self.yang_parent_name = "rttMonStatsTotalsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonstatscapturestarttimeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonstatscapturestarttimeindex', YLeaf(YType.str, 'rttMonStatsCaptureStartTimeIndex')),
                    ('rttmonstatstotalselapsedtime', YLeaf(YType.int32, 'rttMonStatsTotalsElapsedTime')),
                    ('rttmonstatstotalsinitiations', YLeaf(YType.int32, 'rttMonStatsTotalsInitiations')),
                ])
                self.rttmonctrladminindex = None
                self.rttmonstatscapturestarttimeindex = None
                self.rttmonstatstotalselapsedtime = None
                self.rttmonstatstotalsinitiations = None
                self._segment_path = lambda: "rttMonStatsTotalsEntry" + "[rttMonCtrlAdminIndex='" + str(self.rttmonctrladminindex) + "']" + "[rttMonStatsCaptureStartTimeIndex='" + str(self.rttmonstatscapturestarttimeindex) + "']"
                self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsTotalsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonstatstotalstable.Rttmonstatstotalsentry, ['rttmonctrladminindex', 'rttmonstatscapturestarttimeindex', 'rttmonstatstotalselapsedtime', 'rttmonstatstotalsinitiations'], name, value)


    class Rttmonhttpstatstable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonhttpstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonhttpstatstable.Rttmonhttpstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonhttpstatstable, self).__init__()

            self.yang_name = "rttMonHTTPStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonHTTPStatsEntry", ("rttmonhttpstatsentry", CISCORTTMONMIB.Rttmonhttpstatstable.Rttmonhttpstatsentry))])
            self._leafs = OrderedDict()

            self.rttmonhttpstatsentry = YList(self)
            self._segment_path = lambda: "rttMonHTTPStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonhttpstatstable, [], name, value)


        class Rttmonhttpstatsentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is http. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonhttpstatsstarttimeindex  (key)
            
            	This is the time when this row was created. This index uniquely identifies a HTTP Stats row in the  rttMonHTTPStatsTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatscompletions
            
            	The number of HTTP operations that have completed successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsoverthresholds
            
            	The number of HTTP operations that violate threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum
            
            	The sum of HTTP operations that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum2low
            
            	The sum of squares of the RTT's that are successfully measured (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum2high
            
            	The sum of squares of the RTT's that are successfully measured (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttmin
            
            	The minimum RTT taken to perform HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttmax
            
            	The maximum RTT taken to perform HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhttpstatsdnsrttsum
            
            	The sum of RTT taken to perform DNS query within the HTTP operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstcpconnectrttsum
            
            	The sum of RTT taken to connect to the HTTP server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstransactionrttsum
            
            	The sum of RTT taken to download the object specified by URL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsmessagebodyoctetssum
            
            	The sum of the size of the message body received as a response to the HTTP request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsdnsservertimeout
            
            	The number of requests that could not connect to the DNS Server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstcpconnecttimeout
            
            	The number of requests that could not connect to the the HTTP Server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstransactiontimeout
            
            	The number of requests that timed out during HTTP transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsdnsqueryerror
            
            	The number of requests that had DNS Query errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatshttperror
            
            	The number of requests that had HTTP errors while downloading the base page
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatserror
            
            	The number of occasions when a HTTP operation could not be initiated because an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsbusies
            
            	The number of occasions when an HTTP operation could not be initiated because a previous HTTP operation has not been completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonhttpstatstable.Rttmonhttpstatsentry, self).__init__()

                self.yang_name = "rttMonHTTPStatsEntry"
                self.yang_parent_name = "rttMonHTTPStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonhttpstatsstarttimeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonhttpstatsstarttimeindex', YLeaf(YType.uint32, 'rttMonHTTPStatsStartTimeIndex')),
                    ('rttmonhttpstatscompletions', YLeaf(YType.uint32, 'rttMonHTTPStatsCompletions')),
                    ('rttmonhttpstatsoverthresholds', YLeaf(YType.uint32, 'rttMonHTTPStatsOverThresholds')),
                    ('rttmonhttpstatsrttsum', YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum')),
                    ('rttmonhttpstatsrttsum2low', YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum2Low')),
                    ('rttmonhttpstatsrttsum2high', YLeaf(YType.uint32, 'rttMonHTTPStatsRTTSum2High')),
                    ('rttmonhttpstatsrttmin', YLeaf(YType.uint32, 'rttMonHTTPStatsRTTMin')),
                    ('rttmonhttpstatsrttmax', YLeaf(YType.uint32, 'rttMonHTTPStatsRTTMax')),
                    ('rttmonhttpstatsdnsrttsum', YLeaf(YType.uint32, 'rttMonHTTPStatsDNSRTTSum')),
                    ('rttmonhttpstatstcpconnectrttsum', YLeaf(YType.uint32, 'rttMonHTTPStatsTCPConnectRTTSum')),
                    ('rttmonhttpstatstransactionrttsum', YLeaf(YType.uint32, 'rttMonHTTPStatsTransactionRTTSum')),
                    ('rttmonhttpstatsmessagebodyoctetssum', YLeaf(YType.uint32, 'rttMonHTTPStatsMessageBodyOctetsSum')),
                    ('rttmonhttpstatsdnsservertimeout', YLeaf(YType.uint32, 'rttMonHTTPStatsDNSServerTimeout')),
                    ('rttmonhttpstatstcpconnecttimeout', YLeaf(YType.uint32, 'rttMonHTTPStatsTCPConnectTimeout')),
                    ('rttmonhttpstatstransactiontimeout', YLeaf(YType.uint32, 'rttMonHTTPStatsTransactionTimeout')),
                    ('rttmonhttpstatsdnsqueryerror', YLeaf(YType.uint32, 'rttMonHTTPStatsDNSQueryError')),
                    ('rttmonhttpstatshttperror', YLeaf(YType.uint32, 'rttMonHTTPStatsHTTPError')),
                    ('rttmonhttpstatserror', YLeaf(YType.uint32, 'rttMonHTTPStatsError')),
                    ('rttmonhttpstatsbusies', YLeaf(YType.uint32, 'rttMonHTTPStatsBusies')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonhttpstatstable.Rttmonhttpstatsentry, ['rttmonctrladminindex', 'rttmonhttpstatsstarttimeindex', 'rttmonhttpstatscompletions', 'rttmonhttpstatsoverthresholds', 'rttmonhttpstatsrttsum', 'rttmonhttpstatsrttsum2low', 'rttmonhttpstatsrttsum2high', 'rttmonhttpstatsrttmin', 'rttmonhttpstatsrttmax', 'rttmonhttpstatsdnsrttsum', 'rttmonhttpstatstcpconnectrttsum', 'rttmonhttpstatstransactionrttsum', 'rttmonhttpstatsmessagebodyoctetssum', 'rttmonhttpstatsdnsservertimeout', 'rttmonhttpstatstcpconnecttimeout', 'rttmonhttpstatstransactiontimeout', 'rttmonhttpstatsdnsqueryerror', 'rttmonhttpstatshttperror', 'rttmonhttpstatserror', 'rttmonhttpstatsbusies'], name, value)


    class Rttmonjitterstatstable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonjitterstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonjitterstatstable.Rttmonjitterstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonjitterstatstable, self).__init__()

            self.yang_name = "rttMonJitterStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonJitterStatsEntry", ("rttmonjitterstatsentry", CISCORTTMONMIB.Rttmonjitterstatstable.Rttmonjitterstatsentry))])
            self._leafs = OrderedDict()

            self.rttmonjitterstatsentry = YList(self)
            self._segment_path = lambda: "rttMonJitterStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonjitterstatstable, [], name, value)


        class Rttmonjitterstatsentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is jitter. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonjitterstatsstarttimeindex  (key)
            
            	The time when this row was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatscompletions
            
            	The number of jitter operation that have completed successfully
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsoverthresholds
            
            	The number of jitter operations that violate threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofrtt
            
            	The number of RTT's that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum
            
            	The sum of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsRTTSumHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum2low
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofpositivessd
            
            	The minimum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofpositivessd
            
            	The maximum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofpositivessd
            
            	The sum of number of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivessdlow
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivessdhigh
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofnegativessd
            
            	The minimum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofnegativessd
            
            	The maximum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofnegativessd
            
            	The sum of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativessdlow
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativessdhigh
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivesdslow
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivesdshigh
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativesdslow
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativesdshigh
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatserror
            
            	The number of occasions when a jitter operation could not be initiated because an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsbusies
            
            	The number of occasions when a jitter operation could not be initiated because a previous jitter operation has not been completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumsd
            
            	The sum of one way times from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumSDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2sdlow
            
            	The sum of squares of one way times from source to destination (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2sdhigh
            
            	The sum of squares of one way times from source to destination (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowminsd
            
            	The minimum of all one way times from source to destination. rttMonJitterStatsOWMinSD object is superseded by rttMonJitterStatsOWMinSDNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxsd
            
            	The maximum of all one way times from source to destination. rttMonJitterStatsOWMaxSD object is superseded by rttMonJitterStatsOWMaxSDNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowsumds
            
            	The sum of one way times from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumDSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2dslow
            
            	The sum of squares of one way times from destination to source (low order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2dshigh
            
            	The sum of squares of one way times from destination to source (high order 32 bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowminds
            
            	The minimum of all one way times from destination to source. rttMonJitterStatsOWMinDS object is superseded by rttMonJitterStatsOWMinDSNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxds
            
            	The maximum of all one way times from destination to source. rttMonJitterStatsOWMaxDS object is superseded by rttMonJitterStatsOWMaxDSNew
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsnumofow
            
            	The number of one way times that are successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowminsdnew
            
            	The minimum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMinSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowmaxsdnew
            
            	The maximum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMaxSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowmindsnew
            
            	The minimum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMinDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowmaxdsnew
            
            	The maximum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMaxDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofmos
            
            	The minimum of all MOS values for the jitter operations in hundreds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonjitterstatsmaxofmos
            
            	The maximum of all MOS values for the jitter operations in hunderds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonjitterstatsminoficpif
            
            	The minimum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxoficpif
            
            	The maximum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsiajout
            
            	Interarrival Jitter (RFC 1889) at responder
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsiajin
            
            	Interarrival Jitter (RFC 1889) at sender
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjitter
            
            	The average of positive and negative jitter values for SD and DS direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjittersd
            
            	The average of positive and negative jitter values in SD direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjitterds
            
            	The average of positive and negative jitter values in DS direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsumhigh
            
            	The sum of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsRTTSum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumsdhigh
            
            	The sum of one way times from source to destination (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsOWSumSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumdshigh
            
            	The sum of one way times from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonJitterStatsOWSumDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonjitterstatstable.Rttmonjitterstatsentry, self).__init__()

                self.yang_name = "rttMonJitterStatsEntry"
                self.yang_parent_name = "rttMonJitterStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonjitterstatsstarttimeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonjitterstatsstarttimeindex', YLeaf(YType.uint32, 'rttMonJitterStatsStartTimeIndex')),
                    ('rttmonjitterstatscompletions', YLeaf(YType.uint32, 'rttMonJitterStatsCompletions')),
                    ('rttmonjitterstatsoverthresholds', YLeaf(YType.uint32, 'rttMonJitterStatsOverThresholds')),
                    ('rttmonjitterstatsnumofrtt', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfRTT')),
                    ('rttmonjitterstatsrttsum', YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum')),
                    ('rttmonjitterstatsrttsum2low', YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum2Low')),
                    ('rttmonjitterstatsrttsum2high', YLeaf(YType.uint32, 'rttMonJitterStatsRTTSum2High')),
                    ('rttmonjitterstatsrttmin', YLeaf(YType.uint32, 'rttMonJitterStatsRTTMin')),
                    ('rttmonjitterstatsrttmax', YLeaf(YType.uint32, 'rttMonJitterStatsRTTMax')),
                    ('rttmonjitterstatsminofpositivessd', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfPositivesSD')),
                    ('rttmonjitterstatsmaxofpositivessd', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfPositivesSD')),
                    ('rttmonjitterstatsnumofpositivessd', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfPositivesSD')),
                    ('rttmonjitterstatssumofpositivessd', YLeaf(YType.uint32, 'rttMonJitterStatsSumOfPositivesSD')),
                    ('rttmonjitterstatssum2positivessdlow', YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesSDLow')),
                    ('rttmonjitterstatssum2positivessdhigh', YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesSDHigh')),
                    ('rttmonjitterstatsminofnegativessd', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfNegativesSD')),
                    ('rttmonjitterstatsmaxofnegativessd', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfNegativesSD')),
                    ('rttmonjitterstatsnumofnegativessd', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfNegativesSD')),
                    ('rttmonjitterstatssumofnegativessd', YLeaf(YType.uint32, 'rttMonJitterStatsSumOfNegativesSD')),
                    ('rttmonjitterstatssum2negativessdlow', YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesSDLow')),
                    ('rttmonjitterstatssum2negativessdhigh', YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesSDHigh')),
                    ('rttmonjitterstatsminofpositivesds', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfPositivesDS')),
                    ('rttmonjitterstatsmaxofpositivesds', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfPositivesDS')),
                    ('rttmonjitterstatsnumofpositivesds', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfPositivesDS')),
                    ('rttmonjitterstatssumofpositivesds', YLeaf(YType.uint32, 'rttMonJitterStatsSumOfPositivesDS')),
                    ('rttmonjitterstatssum2positivesdslow', YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesDSLow')),
                    ('rttmonjitterstatssum2positivesdshigh', YLeaf(YType.uint32, 'rttMonJitterStatsSum2PositivesDSHigh')),
                    ('rttmonjitterstatsminofnegativesds', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfNegativesDS')),
                    ('rttmonjitterstatsmaxofnegativesds', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfNegativesDS')),
                    ('rttmonjitterstatsnumofnegativesds', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfNegativesDS')),
                    ('rttmonjitterstatssumofnegativesds', YLeaf(YType.uint32, 'rttMonJitterStatsSumOfNegativesDS')),
                    ('rttmonjitterstatssum2negativesdslow', YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesDSLow')),
                    ('rttmonjitterstatssum2negativesdshigh', YLeaf(YType.uint32, 'rttMonJitterStatsSum2NegativesDSHigh')),
                    ('rttmonjitterstatspacketlosssd', YLeaf(YType.uint32, 'rttMonJitterStatsPacketLossSD')),
                    ('rttmonjitterstatspacketlossds', YLeaf(YType.uint32, 'rttMonJitterStatsPacketLossDS')),
                    ('rttmonjitterstatspacketoutofsequence', YLeaf(YType.uint32, 'rttMonJitterStatsPacketOutOfSequence')),
                    ('rttmonjitterstatspacketmia', YLeaf(YType.uint32, 'rttMonJitterStatsPacketMIA')),
                    ('rttmonjitterstatspacketlatearrival', YLeaf(YType.uint32, 'rttMonJitterStatsPacketLateArrival')),
                    ('rttmonjitterstatserror', YLeaf(YType.uint32, 'rttMonJitterStatsError')),
                    ('rttmonjitterstatsbusies', YLeaf(YType.uint32, 'rttMonJitterStatsBusies')),
                    ('rttmonjitterstatsowsumsd', YLeaf(YType.uint32, 'rttMonJitterStatsOWSumSD')),
                    ('rttmonjitterstatsowsum2sdlow', YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2SDLow')),
                    ('rttmonjitterstatsowsum2sdhigh', YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2SDHigh')),
                    ('rttmonjitterstatsowminsd', YLeaf(YType.uint32, 'rttMonJitterStatsOWMinSD')),
                    ('rttmonjitterstatsowmaxsd', YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxSD')),
                    ('rttmonjitterstatsowsumds', YLeaf(YType.uint32, 'rttMonJitterStatsOWSumDS')),
                    ('rttmonjitterstatsowsum2dslow', YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2DSLow')),
                    ('rttmonjitterstatsowsum2dshigh', YLeaf(YType.uint32, 'rttMonJitterStatsOWSum2DSHigh')),
                    ('rttmonjitterstatsowminds', YLeaf(YType.uint32, 'rttMonJitterStatsOWMinDS')),
                    ('rttmonjitterstatsowmaxds', YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxDS')),
                    ('rttmonjitterstatsnumofow', YLeaf(YType.uint32, 'rttMonJitterStatsNumOfOW')),
                    ('rttmonjitterstatsowminsdnew', YLeaf(YType.uint32, 'rttMonJitterStatsOWMinSDNew')),
                    ('rttmonjitterstatsowmaxsdnew', YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxSDNew')),
                    ('rttmonjitterstatsowmindsnew', YLeaf(YType.uint32, 'rttMonJitterStatsOWMinDSNew')),
                    ('rttmonjitterstatsowmaxdsnew', YLeaf(YType.uint32, 'rttMonJitterStatsOWMaxDSNew')),
                    ('rttmonjitterstatsminofmos', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfMOS')),
                    ('rttmonjitterstatsmaxofmos', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfMOS')),
                    ('rttmonjitterstatsminoficpif', YLeaf(YType.uint32, 'rttMonJitterStatsMinOfICPIF')),
                    ('rttmonjitterstatsmaxoficpif', YLeaf(YType.uint32, 'rttMonJitterStatsMaxOfICPIF')),
                    ('rttmonjitterstatsiajout', YLeaf(YType.uint32, 'rttMonJitterStatsIAJOut')),
                    ('rttmonjitterstatsiajin', YLeaf(YType.uint32, 'rttMonJitterStatsIAJIn')),
                    ('rttmonjitterstatsavgjitter', YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitter')),
                    ('rttmonjitterstatsavgjittersd', YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitterSD')),
                    ('rttmonjitterstatsavgjitterds', YLeaf(YType.uint32, 'rttMonJitterStatsAvgJitterDS')),
                    ('rttmonjitterstatsunsyncrts', YLeaf(YType.uint32, 'rttMonJitterStatsUnSyncRTs')),
                    ('rttmonjitterstatsrttsumhigh', YLeaf(YType.uint32, 'rttMonJitterStatsRTTSumHigh')),
                    ('rttmonjitterstatsowsumsdhigh', YLeaf(YType.uint32, 'rttMonJitterStatsOWSumSDHigh')),
                    ('rttmonjitterstatsowsumdshigh', YLeaf(YType.uint32, 'rttMonJitterStatsOWSumDSHigh')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonjitterstatstable.Rttmonjitterstatsentry, ['rttmonctrladminindex', 'rttmonjitterstatsstarttimeindex', 'rttmonjitterstatscompletions', 'rttmonjitterstatsoverthresholds', 'rttmonjitterstatsnumofrtt', 'rttmonjitterstatsrttsum', 'rttmonjitterstatsrttsum2low', 'rttmonjitterstatsrttsum2high', 'rttmonjitterstatsrttmin', 'rttmonjitterstatsrttmax', 'rttmonjitterstatsminofpositivessd', 'rttmonjitterstatsmaxofpositivessd', 'rttmonjitterstatsnumofpositivessd', 'rttmonjitterstatssumofpositivessd', 'rttmonjitterstatssum2positivessdlow', 'rttmonjitterstatssum2positivessdhigh', 'rttmonjitterstatsminofnegativessd', 'rttmonjitterstatsmaxofnegativessd', 'rttmonjitterstatsnumofnegativessd', 'rttmonjitterstatssumofnegativessd', 'rttmonjitterstatssum2negativessdlow', 'rttmonjitterstatssum2negativessdhigh', 'rttmonjitterstatsminofpositivesds', 'rttmonjitterstatsmaxofpositivesds', 'rttmonjitterstatsnumofpositivesds', 'rttmonjitterstatssumofpositivesds', 'rttmonjitterstatssum2positivesdslow', 'rttmonjitterstatssum2positivesdshigh', 'rttmonjitterstatsminofnegativesds', 'rttmonjitterstatsmaxofnegativesds', 'rttmonjitterstatsnumofnegativesds', 'rttmonjitterstatssumofnegativesds', 'rttmonjitterstatssum2negativesdslow', 'rttmonjitterstatssum2negativesdshigh', 'rttmonjitterstatspacketlosssd', 'rttmonjitterstatspacketlossds', 'rttmonjitterstatspacketoutofsequence', 'rttmonjitterstatspacketmia', 'rttmonjitterstatspacketlatearrival', 'rttmonjitterstatserror', 'rttmonjitterstatsbusies', 'rttmonjitterstatsowsumsd', 'rttmonjitterstatsowsum2sdlow', 'rttmonjitterstatsowsum2sdhigh', 'rttmonjitterstatsowminsd', 'rttmonjitterstatsowmaxsd', 'rttmonjitterstatsowsumds', 'rttmonjitterstatsowsum2dslow', 'rttmonjitterstatsowsum2dshigh', 'rttmonjitterstatsowminds', 'rttmonjitterstatsowmaxds', 'rttmonjitterstatsnumofow', 'rttmonjitterstatsowminsdnew', 'rttmonjitterstatsowmaxsdnew', 'rttmonjitterstatsowmindsnew', 'rttmonjitterstatsowmaxdsnew', 'rttmonjitterstatsminofmos', 'rttmonjitterstatsmaxofmos', 'rttmonjitterstatsminoficpif', 'rttmonjitterstatsmaxoficpif', 'rttmonjitterstatsiajout', 'rttmonjitterstatsiajin', 'rttmonjitterstatsavgjitter', 'rttmonjitterstatsavgjittersd', 'rttmonjitterstatsavgjitterds', 'rttmonjitterstatsunsyncrts', 'rttmonjitterstatsrttsumhigh', 'rttmonjitterstatsowsumsdhigh', 'rttmonjitterstatsowsumdshigh'], name, value)


    class Rttmonlpdgrpstatstable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonlpdgrpstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonlpdgrpstatstable, self).__init__()

            self.yang_name = "rttMonLpdGrpStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonLpdGrpStatsEntry", ("rttmonlpdgrpstatsentry", CISCORTTMONMIB.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry))])
            self._leafs = OrderedDict()

            self.rttmonlpdgrpstatsentry = YList(self)
            self._segment_path = lambda: "rttMonLpdGrpStatsTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonlpdgrpstatstable, [], name, value)


        class Rttmonlpdgrpstatsentry(Entity):
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
            
            .. attribute:: rttmonlpdgrpstatsstarttimeindex  (key)
            
            	The time when this row was created.  This object is the second index of the rttMonLpdGrpStatsTable. When the number of rttMonLpdGrpStatsStartTimeIndex groups exceeds the rttMplsVpnMonTypeLpdStatHours value, the oldest rttMonLpdGrpStatsStartTimeIndex group will be removed and replaced with the new entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlpdgrpstatstargetpe
            
            	The object is a string that specifies the address of the target PE for this LPD group
            	**type**\: str
            
            .. attribute:: rttmonlpdgrpstatsnumofpass
            
            	This object represents the number of successfull completions of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense value is 'ok' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: passes
            
            .. attribute:: rttmonlpdgrpstatsnumoffail
            
            	This object represents the number of failed operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value other than 'ok' or 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: failures
            
            .. attribute:: rttmonlpdgrpstatsnumoftimeout
            
            	This object represents the number of timed out operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value of 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: timeouts
            
            .. attribute:: rttmonlpdgrpstatsavgrtt
            
            	The average RTT across all set of probes in the LPD group.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsminrtt
            
            	The minimum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsmaxrtt
            
            	The maximum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsminnumpaths
            
            	The minimum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatsmaxnumpaths
            
            	The maximum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatslpdstarttime
            
            	The time when the last LSP Path Discovery to the group was attempted.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: tenths of milliseconds
            
            .. attribute:: rttmonlpdgrpstatslpdfailoccurred
            
            	This object is set to true when the LSP Path Discovery to the target PE i.e. rttMonLpdGrpStatsTargetPE fails, and set to false when the LSP Path Discovery succeeds.  When this value changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdPathDiscovery' or 'lpdAll' a rttMonLpdDiscoveryNotification will be generated.  This object will be set to 'FALSE' on reset
            	**type**\: bool
            
            .. attribute:: rttmonlpdgrpstatslpdfailcause
            
            	This object identifies the cause of failure for the LSP Path Discovery last attempted. It will be only valid if rttMonLpdGrpStatsLPDFailOccurred is set to true.  This object will be set to 'unknown' on reset
            	**type**\:  :py:class:`RttMplsVpnMonLpdFailureSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonLpdFailureSense>`
            
            .. attribute:: rttmonlpdgrpstatslpdcomptime
            
            	The completion time of the last successfull LSP Path Discovery to the target PE.  This object will be set to '0' on reset
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: rttmonlpdgrpstatsgroupstatus
            
            	This object identifies the LPD Group status.  When the LPD Group status changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdGroupStatus' or 'lpdAll' a rttMonLpdGrpStatusNotification will be generated.  When the LPD Group status value is 'unknown' or changes to 'unknown' this notification will not be generated.  When LSP Path Discovery is enabled for a particular row in rttMplsVpnMonCtrlTable, 'single probes' in the 'lspGroup' probe cannot generate notifications independently but will be generating depending on the state of the group. Notifications  are only generated if the failure/restoration of an individual probe causes the state of the LPD Group to change.  This object will be set to 'unknown' on reset
            	**type**\:  :py:class:`RttMplsVpnMonLpdGrpStatus <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttMplsVpnMonLpdGrpStatus>`
            
            .. attribute:: rttmonlpdgrpstatsgroupprobeindex
            
            	This object identifies 'lspGroup' probe uniquely created for this particular LPD Group
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: identifier
            
            .. attribute:: rttmonlpdgrpstatspathids
            
            	A string which holds the list of information to uniquely identify the paths to the target PE. This information is used by the 'single probes' when testing the paths.  Following three parameters are needed to uniquely identify a  path   \- lsp\-selector (127.x.x.x)   \- outgoing\-interface (i/f)   \- label\-stack (s), if mutiple labels they will be colon (\:)     separated.  These parameters will be hyphen (\-) separated for a particular path. This set of information will be comma (,) separated for all the paths discovered as part of this LPD Group.  For example\: If there are 5 paths in the LPD group then this object will return all the identifier's to uniquely identify the path.  The output will look like '127.0.0.1\-Se3/0.1\-20\:18, 127.0.0.2\-Se3/0.1\-20,127.0.0.3\-Se3/0.1\-20,127.0.0.4\-Se3/0.1\-20, 127.0.0.5\-Se3/0.1\-20'.  This object will be set to '0' on reset
            	**type**\: str
            
            .. attribute:: rttmonlpdgrpstatsprobestatus
            
            	A string which holds the latest operation return code for all the set of 'single probes' which are part of the LPD group. The return codes will be comma separated and will follow the same sequence of probes as followed in 'rttMonLpdGrpStatsPathIds'. The latest operation return code will be mapped to 'up','down' or 'unkwown'.  'up' \- Probe state is up when the rttMonLatestRttOperSense value is 'ok'. 'down' \- Probe state is down when the rttMonLatestRttOperSense has value other then 'ok' and 'other'. 'unknown' \- Probe state is unkown when the rttMonLatestRttOperSense value is 'other'.  For example\: If there are 5 paths in the LPD group then this object output will look like 'ok,ok,ok,down,down'.  This object will be set to '0' on reset
            	**type**\: str
            
            .. attribute:: rttmonlpdgrpstatsresettime
            
            	This object specifies the time when this statistics row was last reset using the rttMonApplLpdGrpStatsReset object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry, self).__init__()

                self.yang_name = "rttMonLpdGrpStatsEntry"
                self.yang_parent_name = "rttMonLpdGrpStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonlpdgrpstatsgroupindex','rttmonlpdgrpstatsstarttimeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonlpdgrpstatsgroupindex', YLeaf(YType.int32, 'rttMonLpdGrpStatsGroupIndex')),
                    ('rttmonlpdgrpstatsstarttimeindex', YLeaf(YType.uint32, 'rttMonLpdGrpStatsStartTimeIndex')),
                    ('rttmonlpdgrpstatstargetpe', YLeaf(YType.str, 'rttMonLpdGrpStatsTargetPE')),
                    ('rttmonlpdgrpstatsnumofpass', YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfPass')),
                    ('rttmonlpdgrpstatsnumoffail', YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfFail')),
                    ('rttmonlpdgrpstatsnumoftimeout', YLeaf(YType.int32, 'rttMonLpdGrpStatsNumOfTimeout')),
                    ('rttmonlpdgrpstatsavgrtt', YLeaf(YType.int32, 'rttMonLpdGrpStatsAvgRTT')),
                    ('rttmonlpdgrpstatsminrtt', YLeaf(YType.int32, 'rttMonLpdGrpStatsMinRTT')),
                    ('rttmonlpdgrpstatsmaxrtt', YLeaf(YType.int32, 'rttMonLpdGrpStatsMaxRTT')),
                    ('rttmonlpdgrpstatsminnumpaths', YLeaf(YType.int32, 'rttMonLpdGrpStatsMinNumPaths')),
                    ('rttmonlpdgrpstatsmaxnumpaths', YLeaf(YType.int32, 'rttMonLpdGrpStatsMaxNumPaths')),
                    ('rttmonlpdgrpstatslpdstarttime', YLeaf(YType.uint32, 'rttMonLpdGrpStatsLPDStartTime')),
                    ('rttmonlpdgrpstatslpdfailoccurred', YLeaf(YType.boolean, 'rttMonLpdGrpStatsLPDFailOccurred')),
                    ('rttmonlpdgrpstatslpdfailcause', YLeaf(YType.enumeration, 'rttMonLpdGrpStatsLPDFailCause')),
                    ('rttmonlpdgrpstatslpdcomptime', YLeaf(YType.int32, 'rttMonLpdGrpStatsLPDCompTime')),
                    ('rttmonlpdgrpstatsgroupstatus', YLeaf(YType.enumeration, 'rttMonLpdGrpStatsGroupStatus')),
                    ('rttmonlpdgrpstatsgroupprobeindex', YLeaf(YType.int32, 'rttMonLpdGrpStatsGroupProbeIndex')),
                    ('rttmonlpdgrpstatspathids', YLeaf(YType.str, 'rttMonLpdGrpStatsPathIds')),
                    ('rttmonlpdgrpstatsprobestatus', YLeaf(YType.str, 'rttMonLpdGrpStatsProbeStatus')),
                    ('rttmonlpdgrpstatsresettime', YLeaf(YType.uint32, 'rttMonLpdGrpStatsResetTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry, ['rttmonlpdgrpstatsgroupindex', 'rttmonlpdgrpstatsstarttimeindex', 'rttmonlpdgrpstatstargetpe', 'rttmonlpdgrpstatsnumofpass', 'rttmonlpdgrpstatsnumoffail', 'rttmonlpdgrpstatsnumoftimeout', 'rttmonlpdgrpstatsavgrtt', 'rttmonlpdgrpstatsminrtt', 'rttmonlpdgrpstatsmaxrtt', 'rttmonlpdgrpstatsminnumpaths', 'rttmonlpdgrpstatsmaxnumpaths', 'rttmonlpdgrpstatslpdstarttime', 'rttmonlpdgrpstatslpdfailoccurred', 'rttmonlpdgrpstatslpdfailcause', 'rttmonlpdgrpstatslpdcomptime', 'rttmonlpdgrpstatsgroupstatus', 'rttmonlpdgrpstatsgroupprobeindex', 'rttmonlpdgrpstatspathids', 'rttmonlpdgrpstatsprobestatus', 'rttmonlpdgrpstatsresettime'], name, value)


    class Rttmonhistorycollectiontable(Entity):
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
        	**type**\: list of  		 :py:class:`Rttmonhistorycollectionentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonhistorycollectiontable, self).__init__()

            self.yang_name = "rttMonHistoryCollectionTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonHistoryCollectionEntry", ("rttmonhistorycollectionentry", CISCORTTMONMIB.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry))])
            self._leafs = OrderedDict()

            self.rttmonhistorycollectionentry = YList(self)
            self._segment_path = lambda: "rttMonHistoryCollectionTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonhistorycollectiontable, [], name, value)


        class Rttmonhistorycollectionentry(Entity):
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
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonhistorycollectionlifeindex  (key)
            
            	This uniquely defines a life for a conceptual history row.  For a particular value of rttMonHistoryCollectionLifeIndex, the agent assigns the first value of 1, the second value  of 2, and so on.  The sequence keeps incrementing,  despite older (lower) values being removed from the  table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonhistorycollectionbucketindex  (key)
            
            	When the RttMonRttType is 'pathEcho', this uniquely defines a bucket for a given value of  rttMonHistoryCollectionLifeIndex.  For all other  RttMonRttType this value will be the number of operations per a lifetime.  Thus, this object  increments on each operation attempt.  For a particular value of  rttMonHistoryCollectionLifeIndex, the agent assigns  the first value of 1, the second value of 2, and so  on.  The sequence keeps incrementing until the number of buckets equals rttMonHistoryAdminNumBuckets, after which the most recent rttMonHistoryAdminNumBuckets  buckets are retained (the index is incremented though)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonhistorycollectionsampleindex  (key)
            
            	This uniquely defines a row for a given value of rttMonHistoryCollectionBucketIndex.  This object represents a hop along a path to the Target.  For a particular value of  rttMonHistoryCollectionBucketIndex, the agent assigns  the first value of 1, the second value of 2, and so on. The sequence keeps incrementing until the number of  samples equals rttMonHistoryAdminNumSamples, then no  new samples are created for the current  rttMonHistoryCollectionBucketIndex.  When the RttMonRttType is 'pathEcho', this value  directly represents the number of hops along a  path to a target, thus we can only support 512 hops. For all other values of RttMonRttType this object will be one
            	**type**\: int
            
            	**range:** 1..512
            
            .. attribute:: rttmonhistorycollectionsampletime
            
            	The time that the RTT operation was initiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhistorycollectionaddress
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is a string which specifies the address of the target for the this RTT operation.  For all other values of RttMonRttType this string will be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\: str
            
            .. attribute:: rttmonhistorycollectioncompletiontime
            
            	This is the operation completion time of the RTT operation.  If the RTT operation fails  (rttMonHistoryCollectionSense is any  value other than ok), this has a value of 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhistorycollectionsense
            
            	A sense code for the completion status of the RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            .. attribute:: rttmonhistorycollectionapplspecificsense
            
            	An application specific sense code for the completion status of the last RTT operation.  This  object will only be valid when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonhistorycollectionsensedescription
            
            	A sense description for the completion status of the last RTT operation when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry, self).__init__()

                self.yang_name = "rttMonHistoryCollectionEntry"
                self.yang_parent_name = "rttMonHistoryCollectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex','rttmonhistorycollectionlifeindex','rttmonhistorycollectionbucketindex','rttmonhistorycollectionsampleindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonhistorycollectionlifeindex', YLeaf(YType.int32, 'rttMonHistoryCollectionLifeIndex')),
                    ('rttmonhistorycollectionbucketindex', YLeaf(YType.int32, 'rttMonHistoryCollectionBucketIndex')),
                    ('rttmonhistorycollectionsampleindex', YLeaf(YType.int32, 'rttMonHistoryCollectionSampleIndex')),
                    ('rttmonhistorycollectionsampletime', YLeaf(YType.uint32, 'rttMonHistoryCollectionSampleTime')),
                    ('rttmonhistorycollectionaddress', YLeaf(YType.str, 'rttMonHistoryCollectionAddress')),
                    ('rttmonhistorycollectioncompletiontime', YLeaf(YType.uint32, 'rttMonHistoryCollectionCompletionTime')),
                    ('rttmonhistorycollectionsense', YLeaf(YType.enumeration, 'rttMonHistoryCollectionSense')),
                    ('rttmonhistorycollectionapplspecificsense', YLeaf(YType.int32, 'rttMonHistoryCollectionApplSpecificSense')),
                    ('rttmonhistorycollectionsensedescription', YLeaf(YType.str, 'rttMonHistoryCollectionSenseDescription')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry, ['rttmonctrladminindex', 'rttmonhistorycollectionlifeindex', 'rttmonhistorycollectionbucketindex', 'rttmonhistorycollectionsampleindex', 'rttmonhistorycollectionsampletime', 'rttmonhistorycollectionaddress', 'rttmonhistorycollectioncompletiontime', 'rttmonhistorycollectionsense', 'rttmonhistorycollectionapplspecificsense', 'rttmonhistorycollectionsensedescription'], name, value)


    class Rttmonlatesthttpopertable(Entity):
        """
        A table which contains the status of latest HTTP RTT
        operation.
        
        .. attribute:: rttmonlatesthttpoperentry
        
        	A list of objects that record the latest HTTP RTT operation. This entry is created automatically after the  rttMonCtrlAdminEntry is created. Also the entry is  automatically deleted when rttMonCtrlAdminEntry is deleted
        	**type**\: list of  		 :py:class:`Rttmonlatesthttpoperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonlatesthttpopertable, self).__init__()

            self.yang_name = "rttMonLatestHTTPOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonLatestHTTPOperEntry", ("rttmonlatesthttpoperentry", CISCORTTMONMIB.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry))])
            self._leafs = OrderedDict()

            self.rttmonlatesthttpoperentry = YList(self)
            self._segment_path = lambda: "rttMonLatestHTTPOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonlatesthttpopertable, [], name, value)


        class Rttmonlatesthttpoperentry(Entity):
            """
            A list of objects that record the latest HTTP RTT
            operation. This entry is created automatically after the 
            rttMonCtrlAdminEntry is created. Also the entry is 
            automatically deleted when rttMonCtrlAdminEntry is deleted.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonlatesthttpoperrtt
            
            	Round Trip Time taken to perform HTTP operation. This value is the sum of DNSRTT, TCPConnectRTT and TransactionRTT
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpoperdnsrtt
            
            	Round Trip Time taken to perform DNS query within the HTTP operation. If an IP Address is specified in the URL,  then DNSRTT is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopertcpconnectrtt
            
            	Round Trip Time taken to connect to the HTTP server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopertransactionrtt
            
            	Round Trip Time taken to download the object specified by the URL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopermessagebodyoctets
            
            	The size of the message body received as a response to the HTTP request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopersense
            
            	An application specific sense code for the completion status of the latest RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            .. attribute:: rttmonlatesthttperrorsensedescription
            
            	An sense description for the completion status of the latest RTT operation
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry, self).__init__()

                self.yang_name = "rttMonLatestHTTPOperEntry"
                self.yang_parent_name = "rttMonLatestHTTPOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonlatesthttpoperrtt', YLeaf(YType.uint32, 'rttMonLatestHTTPOperRTT')),
                    ('rttmonlatesthttpoperdnsrtt', YLeaf(YType.uint32, 'rttMonLatestHTTPOperDNSRTT')),
                    ('rttmonlatesthttpopertcpconnectrtt', YLeaf(YType.uint32, 'rttMonLatestHTTPOperTCPConnectRTT')),
                    ('rttmonlatesthttpopertransactionrtt', YLeaf(YType.uint32, 'rttMonLatestHTTPOperTransactionRTT')),
                    ('rttmonlatesthttpopermessagebodyoctets', YLeaf(YType.uint32, 'rttMonLatestHTTPOperMessageBodyOctets')),
                    ('rttmonlatesthttpopersense', YLeaf(YType.enumeration, 'rttMonLatestHTTPOperSense')),
                    ('rttmonlatesthttperrorsensedescription', YLeaf(YType.str, 'rttMonLatestHTTPErrorSenseDescription')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry, ['rttmonctrladminindex', 'rttmonlatesthttpoperrtt', 'rttmonlatesthttpoperdnsrtt', 'rttmonlatesthttpopertcpconnectrtt', 'rttmonlatesthttpopertransactionrtt', 'rttmonlatesthttpopermessagebodyoctets', 'rttmonlatesthttpopersense', 'rttmonlatesthttperrorsensedescription'], name, value)


    class Rttmonlatestjitteropertable(Entity):
        """
        A table which contains the status of latest Jitter
        operation.
        
        .. attribute:: rttmonlatestjitteroperentry
        
        	A list of objects that record the latest Jitter operation
        	**type**\: list of  		 :py:class:`Rttmonlatestjitteroperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CISCORTTMONMIB.Rttmonlatestjitteropertable, self).__init__()

            self.yang_name = "rttMonLatestJitterOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rttMonLatestJitterOperEntry", ("rttmonlatestjitteroperentry", CISCORTTMONMIB.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry))])
            self._leafs = OrderedDict()

            self.rttmonlatestjitteroperentry = YList(self)
            self._segment_path = lambda: "rttMonLatestJitterOperTable"
            self._absolute_path = lambda: "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORTTMONMIB.Rttmonlatestjitteropertable, [], name, value)


        class Rttmonlatestjitteroperentry(Entity):
            """
            A list of objects that record the latest Jitter
            operation.
            
            .. attribute:: rttmonctrladminindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonlatestjitteropernumofrtt
            
            	The number of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum
            
            	The sum of Jitter RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSumHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum2
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSum2High
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofpositivessd
            
            	The minimum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofpositivessd
            
            	The maximum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofpositivessd
            
            	The sum of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2positivessd
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofnegativessd
            
            	The minimum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofnegativessd
            
            	The maximum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofnegativessd
            
            	The sum of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2negativessd
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2positivesds
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2negativesds
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersense
            
            	An application specific sense code for the completion status of the latest Jitter RTT operation
            	**type**\:  :py:class:`RttResponseSense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.RttResponseSense>`
            
            .. attribute:: rttmonlatestjittererrorsensedescription
            
            	An sense description for the completion status of the latest Jitter RTT operation
            	**type**\: str
            
            .. attribute:: rttmonlatestjitteroperowsumsd
            
            	The sum of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumSDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2sd
            
            	The sum of squares of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2SDHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowminsd
            
            	The minimum of all one way latency from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowmaxsd
            
            	The maximum of all one way latency from source to destination
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumds
            
            	The sum of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumDSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2ds
            
            	The sum of squares of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2DSHigh
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowminds
            
            	The minimum of all one way latency from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowmaxds
            
            	The maximum of all one way latency from destination to source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofow
            
            	The number of successful one way latency measurements
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermos
            
            	The MOS value for the latest jitter operation in hundreds. This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonlatestjitteropericpif
            
            	Represents ICPIF value for the latest jitter operation.  This value will be 93 for packet loss of 10% or more
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperiajout
            
            	Interarrival Jitter (RC1889) at responder
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperiajin
            
            	Interarrival Jitter (RFC1889) at source
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperavgjitter
            
            	The average of positive and negative jitter values in SD and DS direction for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperavgsdj
            
            	The average of positive and negative jitter values from source to destination for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperavgdsj
            
            	The average of positive and negative jitter values from destination to source for latest operation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperowavgsd
            
            	The average latency value from source to destination
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperowavgds
            
            	The average latency value from destination to source
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperntpstate
            
            	A value of sync(1) means sender and responder was in sync with NTP. The NTP sync means the total of NTP offset  on sender and responder is within configured tolerance level
            	**type**\:  :py:class:`Rttmonlatestjitteroperntpstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CISCORTTMONMIB.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry.Rttmonlatestjitteroperntpstate>`
            
            .. attribute:: rttmonlatestjitteroperunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsumhigh
            
            	The sum of Jitter RTT's that are successfully measured. (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum2
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumsdhigh
            
            	The sum of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSumSD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2sdhigh
            
            	The sum of squares of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2SD
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumdshigh
            
            	The sum of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored  in rttMonLatestJitterOperOWSumDS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2dshigh
            
            	The sum of squares of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2DS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CISCORTTMONMIB.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry, self).__init__()

                self.yang_name = "rttMonLatestJitterOperEntry"
                self.yang_parent_name = "rttMonLatestJitterOperTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rttmonctrladminindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rttmonctrladminindex', YLeaf(YType.str, 'rttMonCtrlAdminIndex')),
                    ('rttmonlatestjitteropernumofrtt', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfRTT')),
                    ('rttmonlatestjitteroperrttsum', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum')),
                    ('rttmonlatestjitteroperrttsum2', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum2')),
                    ('rttmonlatestjitteroperrttmin', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTMin')),
                    ('rttmonlatestjitteroperrttmax', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTMax')),
                    ('rttmonlatestjitteroperminofpositivessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfPositivesSD')),
                    ('rttmonlatestjitteropermaxofpositivessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfPositivesSD')),
                    ('rttmonlatestjitteropernumofpositivessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfPositivesSD')),
                    ('rttmonlatestjitteropersumofpositivessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfPositivesSD')),
                    ('rttmonlatestjitteropersum2positivessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2PositivesSD')),
                    ('rttmonlatestjitteroperminofnegativessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfNegativesSD')),
                    ('rttmonlatestjitteropermaxofnegativessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfNegativesSD')),
                    ('rttmonlatestjitteropernumofnegativessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfNegativesSD')),
                    ('rttmonlatestjitteropersumofnegativessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfNegativesSD')),
                    ('rttmonlatestjitteropersum2negativessd', YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2NegativesSD')),
                    ('rttmonlatestjitteroperminofpositivesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfPositivesDS')),
                    ('rttmonlatestjitteropermaxofpositivesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfPositivesDS')),
                    ('rttmonlatestjitteropernumofpositivesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfPositivesDS')),
                    ('rttmonlatestjitteropersumofpositivesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfPositivesDS')),
                    ('rttmonlatestjitteropersum2positivesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2PositivesDS')),
                    ('rttmonlatestjitteroperminofnegativesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperMinOfNegativesDS')),
                    ('rttmonlatestjitteropermaxofnegativesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperMaxOfNegativesDS')),
                    ('rttmonlatestjitteropernumofnegativesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfNegativesDS')),
                    ('rttmonlatestjitteropersumofnegativesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperSumOfNegativesDS')),
                    ('rttmonlatestjitteropersum2negativesds', YLeaf(YType.uint32, 'rttMonLatestJitterOperSum2NegativesDS')),
                    ('rttmonlatestjitteroperpacketlosssd', YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLossSD')),
                    ('rttmonlatestjitteroperpacketlossds', YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLossDS')),
                    ('rttmonlatestjitteroperpacketoutofsequence', YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketOutOfSequence')),
                    ('rttmonlatestjitteroperpacketmia', YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketMIA')),
                    ('rttmonlatestjitteroperpacketlatearrival', YLeaf(YType.uint32, 'rttMonLatestJitterOperPacketLateArrival')),
                    ('rttmonlatestjitteropersense', YLeaf(YType.enumeration, 'rttMonLatestJitterOperSense')),
                    ('rttmonlatestjittererrorsensedescription', YLeaf(YType.str, 'rttMonLatestJitterErrorSenseDescription')),
                    ('rttmonlatestjitteroperowsumsd', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumSD')),
                    ('rttmonlatestjitteroperowsum2sd', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2SD')),
                    ('rttmonlatestjitteroperowminsd', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMinSD')),
                    ('rttmonlatestjitteroperowmaxsd', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMaxSD')),
                    ('rttmonlatestjitteroperowsumds', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumDS')),
                    ('rttmonlatestjitteroperowsum2ds', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2DS')),
                    ('rttmonlatestjitteroperowminds', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMinDS')),
                    ('rttmonlatestjitteroperowmaxds', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWMaxDS')),
                    ('rttmonlatestjitteropernumofow', YLeaf(YType.uint32, 'rttMonLatestJitterOperNumOfOW')),
                    ('rttmonlatestjitteropermos', YLeaf(YType.uint32, 'rttMonLatestJitterOperMOS')),
                    ('rttmonlatestjitteropericpif', YLeaf(YType.uint32, 'rttMonLatestJitterOperICPIF')),
                    ('rttmonlatestjitteroperiajout', YLeaf(YType.uint32, 'rttMonLatestJitterOperIAJOut')),
                    ('rttmonlatestjitteroperiajin', YLeaf(YType.uint32, 'rttMonLatestJitterOperIAJIn')),
                    ('rttmonlatestjitteroperavgjitter', YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgJitter')),
                    ('rttmonlatestjitteroperavgsdj', YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgSDJ')),
                    ('rttmonlatestjitteroperavgdsj', YLeaf(YType.uint32, 'rttMonLatestJitterOperAvgDSJ')),
                    ('rttmonlatestjitteroperowavgsd', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWAvgSD')),
                    ('rttmonlatestjitteroperowavgds', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWAvgDS')),
                    ('rttmonlatestjitteroperntpstate', YLeaf(YType.enumeration, 'rttMonLatestJitterOperNTPState')),
                    ('rttmonlatestjitteroperunsyncrts', YLeaf(YType.uint32, 'rttMonLatestJitterOperUnSyncRTs')),
                    ('rttmonlatestjitteroperrttsumhigh', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSumHigh')),
                    ('rttmonlatestjitteroperrttsum2high', YLeaf(YType.uint32, 'rttMonLatestJitterOperRTTSum2High')),
                    ('rttmonlatestjitteroperowsumsdhigh', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumSDHigh')),
                    ('rttmonlatestjitteroperowsum2sdhigh', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2SDHigh')),
                    ('rttmonlatestjitteroperowsumdshigh', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSumDSHigh')),
                    ('rttmonlatestjitteroperowsum2dshigh', YLeaf(YType.uint32, 'rttMonLatestJitterOperOWSum2DSHigh')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORTTMONMIB.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry, ['rttmonctrladminindex', 'rttmonlatestjitteropernumofrtt', 'rttmonlatestjitteroperrttsum', 'rttmonlatestjitteroperrttsum2', 'rttmonlatestjitteroperrttmin', 'rttmonlatestjitteroperrttmax', 'rttmonlatestjitteroperminofpositivessd', 'rttmonlatestjitteropermaxofpositivessd', 'rttmonlatestjitteropernumofpositivessd', 'rttmonlatestjitteropersumofpositivessd', 'rttmonlatestjitteropersum2positivessd', 'rttmonlatestjitteroperminofnegativessd', 'rttmonlatestjitteropermaxofnegativessd', 'rttmonlatestjitteropernumofnegativessd', 'rttmonlatestjitteropersumofnegativessd', 'rttmonlatestjitteropersum2negativessd', 'rttmonlatestjitteroperminofpositivesds', 'rttmonlatestjitteropermaxofpositivesds', 'rttmonlatestjitteropernumofpositivesds', 'rttmonlatestjitteropersumofpositivesds', 'rttmonlatestjitteropersum2positivesds', 'rttmonlatestjitteroperminofnegativesds', 'rttmonlatestjitteropermaxofnegativesds', 'rttmonlatestjitteropernumofnegativesds', 'rttmonlatestjitteropersumofnegativesds', 'rttmonlatestjitteropersum2negativesds', 'rttmonlatestjitteroperpacketlosssd', 'rttmonlatestjitteroperpacketlossds', 'rttmonlatestjitteroperpacketoutofsequence', 'rttmonlatestjitteroperpacketmia', 'rttmonlatestjitteroperpacketlatearrival', 'rttmonlatestjitteropersense', 'rttmonlatestjittererrorsensedescription', 'rttmonlatestjitteroperowsumsd', 'rttmonlatestjitteroperowsum2sd', 'rttmonlatestjitteroperowminsd', 'rttmonlatestjitteroperowmaxsd', 'rttmonlatestjitteroperowsumds', 'rttmonlatestjitteroperowsum2ds', 'rttmonlatestjitteroperowminds', 'rttmonlatestjitteroperowmaxds', 'rttmonlatestjitteropernumofow', 'rttmonlatestjitteropermos', 'rttmonlatestjitteropericpif', 'rttmonlatestjitteroperiajout', 'rttmonlatestjitteroperiajin', 'rttmonlatestjitteroperavgjitter', 'rttmonlatestjitteroperavgsdj', 'rttmonlatestjitteroperavgdsj', 'rttmonlatestjitteroperowavgsd', 'rttmonlatestjitteroperowavgds', 'rttmonlatestjitteroperntpstate', 'rttmonlatestjitteroperunsyncrts', 'rttmonlatestjitteroperrttsumhigh', 'rttmonlatestjitteroperrttsum2high', 'rttmonlatestjitteroperowsumsdhigh', 'rttmonlatestjitteroperowsum2sdhigh', 'rttmonlatestjitteroperowsumdshigh', 'rttmonlatestjitteroperowsum2dshigh'], name, value)

            class Rttmonlatestjitteroperntpstate(Enum):
                """
                Rttmonlatestjitteroperntpstate (Enum Class)

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

