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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoRttmonMib(Entity):
    """
    
    
    .. attribute:: rttmonappl
    
    	
    	**type**\:   :py:class:`Rttmonappl <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonappl>`
    
    .. attribute:: rttmonapplauthtable
    
    	A table which contains the definitions for key\-strings that will be used in authenticating RTR Control Protocol
    	**type**\:   :py:class:`Rttmonapplauthtable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplauthtable>`
    
    .. attribute:: rttmonapplpreconfigedtable
    
    	A table of which contains the previously configured Script Names and File IO targets.  These Script Names and File IO targets are installed via a different mechanism than this application, and are specific to each platform
    	**type**\:   :py:class:`Rttmonapplpreconfigedtable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplpreconfigedtable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmonapplsupportedprotocolstable
    
    	A table of which contains the supported Rtt Monitor Protocols.  See the RttMonProtocol textual convention  for the definition of each protocol
    	**type**\:   :py:class:`Rttmonapplsupportedprotocolstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplsupportedprotocolstable>`
    
    .. attribute:: rttmonapplsupportedrtttypestable
    
    	A table of which contains the supported Rtt Monitor Types.  See the RttMonRttType textual convention for the definition of each type
    	**type**\:   :py:class:`Rttmonapplsupportedrtttypestable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplsupportedrtttypestable>`
    
    .. attribute:: rttmonctrladmintable
    
    	A table of Round Trip Time (RTT) monitoring definitions.  The RTT administration control is in multiple tables.   This first table, is used to create a conceptual RTT  control row.  The following tables contain objects which  configure scheduling, information gathering, and  notification/trigger generation.  All of these tables  will create the same conceptual RTT control row as this  table using this tables' index as their own index.   This table is limited in size by the agent  implementation.  The object rttMonApplNumCtrlAdminEntry will reflect this tables maximum number of entries
    	**type**\:   :py:class:`Rttmonctrladmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable>`
    
    .. attribute:: rttmonechoadmintable
    
    	A table that contains Round Trip Time (RTT) specific definitions.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:   :py:class:`Rttmonechoadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable>`
    
    .. attribute:: rttmonechopathadmintable
    
    	A table to store the hop addresses in a Loose Source Routing path. Response times are computed along the specified path using ping.  This maximum table size is limited by the size of the  maximum number of hop addresses that can fit in an IP header, which is 8. The object rttMonEchoPathAdminEntry will reflect  this tables maximum number of entries.  This table is coupled with rttMonCtrlAdminStatus
    	**type**\:   :py:class:`Rttmonechopathadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechopathadmintable>`
    
    .. attribute:: rttmonfileioadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'fileIO' specific definitions.  When the RttMonRttType is not 'fileIO' this table is not valid.  This table is controlled via the  rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:   :py:class:`Rttmonfileioadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonfileioadmintable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmongeneratedopertable
    
    	This table contains information about the generated operation id as part of a parent IP SLA operation. The parent operation id is pseudo\-random number, selected by the management  station based on an operation started by the management  station,when creating a row via the rttMonCtrlAdminStatus object in the rttMonCtrlAdminTable table
    	**type**\:   :py:class:`Rttmongeneratedopertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmongeneratedopertable>`
    
    .. attribute:: rttmongrpscheduleadmintable
    
    	A table of Round Trip Time (RTT) monitoring group scheduling specific definitions. This table is used to create a conceptual group scheduling control row. The entries in this control row contain objects used to define group schedule configuration parameters.  The objects of this table will be used to schedule a group of probes identified by the conceptual rows of the rttMonCtrlAdminTable
    	**type**\:   :py:class:`Rttmongrpscheduleadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmongrpscheduleadmintable>`
    
    .. attribute:: rttmonhistorycollectiontable
    
    	The history collection database.  The history table contains a point by point rolling  history of the most recent RTT operations for each  conceptual RTT control row.  The rolling history of this  information is maintained in a series of 'live(s)', each containing a series of 'bucket(s)', each 'bucket'  contains a series of 'sample(s)'.  Each conceptual history row can have lives.  A life is  defined by the rttMonCtrlOperRttLife object.  A new life  will be created when rttMonCtrlOperState transitions 'active'.  When the number of lives become greater  than rttMonHistoryAdminNumLives the oldest life will be  discarded and a new life will be created by incrementing the index.  The path exploration RTT operation will be kept as an entry in this table
    	**type**\:   :py:class:`Rttmonhistorycollectiontable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonhistorycollectiontable>`
    
    .. attribute:: rttmonhttpstatstable
    
    	The HTTP statistics collection database.  The HTTP statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table can only  store a maximum of 2 hours of data
    	**type**\:   :py:class:`Rttmonhttpstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonhttpstatstable>`
    
    .. attribute:: rttmonjitterstatstable
    
    	The Jitter statistics collection database.  The Jitter statistics table contains summarized information of the results for a conceptual RTT control row. A rolling accumulated history of this information is maintained in a  series of hourly 'group(s)'.  The operation of this table is same as that of  rttMonStatsCaptureTable, except that this table will store  2 hours of data
    	**type**\:   :py:class:`Rttmonjitterstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonjitterstatstable>`
    
    .. attribute:: rttmonlatesthttpopertable
    
    	A table which contains the status of latest HTTP RTT operation
    	**type**\:   :py:class:`Rttmonlatesthttpopertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlatesthttpopertable>`
    
    .. attribute:: rttmonlatestjitteropertable
    
    	A table which contains the status of latest Jitter operation
    	**type**\:   :py:class:`Rttmonlatestjitteropertable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlatestjitteropertable>`
    
    .. attribute:: rttmonlpdgrpstatstable
    
    	The Auto SAA L3 MPLS VPN LPD Group Database.  The LPD Group statistics table contains summarized performance statistics for the LPD group.  LPD Group \- The set of 'single probes' which are subset of the 'lspGroup' probe traversing set of paths between two PE end points are grouped together and called as the LPD group. The LPD group will be uniquely referenced by the LPD Group ID.  A rolling accumulated history of this information is maintained in a series of hourly 'group(s)'.  Each conceptual statistics row has a current hourly group, into which RTT results are accumulated. At the end of each hour a new hourly group is created which then becomes current. The counters and accumulators in the new group are initialized to zero. The previous group(s) is kept in the table until the table contains rttMplsVpnMonTypeLpdStatHours groups for the conceptual statistics row;  at this point, the oldest group is discarded and is replaced by the newly created one. The hourly group is uniquely identified by the rttMonLpdGrpStatsStartTimeIndex object
    	**type**\:   :py:class:`Rttmonlpdgrpstatstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlpdgrpstatstable>`
    
    .. attribute:: rttmonreacttable
    
    	A table that contains the reaction configurations. Each conceptual row in rttMonReactTable corresponds to a reaction configured for the probe defined in rttMonCtrlAdminTable.  For each reaction configured for a probe there is an entry in the table.  Each Probe can have multiple reactions and hence there can be multiple rows for a particular probe.  This table is coupled with rttMonCtrlAdminTable
    	**type**\:   :py:class:`Rttmonreacttable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttable>`
    
    .. attribute:: rttmonreacttriggeradmintable
    
    	A table of which contains the list of conceptual RTT control rows that will start to collect data when a  reaction condition is violated and when  rttMonReactAdminActionType is set to one of the  following\:   \-  triggerOnly   \-  trapAndTrigger   \-  nmvtAndTrigger   \-  trapNmvtAndTrigger or when a reaction condition is violated and when any of the row in rttMonReactTable has rttMonReactActionType as one of the following\:   \- triggerOnly   \- trapAndTrigger  The goal of this table is to define one or more  additional conceptual RTT control rows that will become active and start to collect additional history and statistics (depending on the rows configuration values), when a problem has been detected.  If the conceptual RTT control row is undefined, and a  trigger occurs, no action will take place.    If the conceptual RTT control row is scheduled to start  at a later time, triggering that row will have no effect.  If the conceptual RTT control row is currently active,  triggering that row will have no effect on that row, but  the rttMonReactTriggerOperState object will transition to  'active'.  An entry in this table can only be triggered when it is not currently in a triggered state.  The object rttMonReactTriggerOperState will  reflect the state of each entry in this table
    	**type**\:   :py:class:`Rttmonreacttriggeradmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttriggeradmintable>`
    
    .. attribute:: rttmonscriptadmintable
    
    	A table of Round Trip Time (RTT) monitoring 'script' specific definitions.  When the RttMonRttType is not 'script' this table is not valid.  This table is controlled via the rttMonCtrlAdminTable.  Entries in this table are created via the rttMonCtrlAdminStatus object
    	**type**\:   :py:class:`Rttmonscriptadmintable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonscriptadmintable>`
    
    	**status**\: obsolete
    
    .. attribute:: rttmonstatscapturetable
    
    	The statistics capture database.  The statistics capture table contains summarized  information of the results for a conceptual RTT control  row.  A rolling accumulated history of this information  is maintained in a series of hourly 'group(s)'.  Each  'group' contains a series of 'path(s)', each 'path'  contains a series of 'hop(s)', each 'hop' contains a  series of 'statistics distribution bucket(s)'.  Each conceptual statistics row has a current hourly  group, into which RTT results are accumulated.  At the  end of each hour a new hourly group is created which  then becomes current.  The counters and accumulators in  the new group are initialized to zero.  The previous  group(s) is kept in the table until the table contains  rttMonStatisticsAdminNumHourGroups groups for the  conceptual statistics row;  at this point, the oldest  group is discarded and is replaced by the newly created  one.  The hourly group is uniquely identified by the  rttMonStatsCaptureStartTimeIndex object.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'inactive', the corresponding current hourly group in  this table is 'frozen', and a new hourly group is  created when activity is resumed.  If the activity for a conceptual RTT control row ceases  because the rttMonCtrlOperState object transitions to  'pending' this whole table will be cleared and reset to  its initial state.  When the RttMonRttType is 'pathEcho', the path  exploration RTT requests' statistics will not be  accumulated in this table.  NOTE\: When the RttMonRttType is 'pathEcho', a source to        target rttMonStatsCapturePathIndex path will be        created for each rttMonStatsCaptureStartTimeIndex        to hold all errors that occur when a specific path       had not been found or connection has not be setup.  Using this rttMonStatsCaptureTable, a managing  application can retrieve summarized data from accurately  measured periods, which is synchronized across multiple  conceptual RTT control rows.  With the new hourly group creation being performed on a 60 minute period, the  managing station has plenty of time to collect the data,  and need not be concerned with the vagaries of network  delays and lost PDU's when trying to get matching data.   Also, the managing station can spread the data gathering  over a longer period, which removes the need for a flood  of get requests in a short period which otherwise would  occur
    	**type**\:   :py:class:`Rttmonstatscapturetable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable>`
    
    .. attribute:: rttmonstatscollecttable
    
    	The statistics collection database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it does not keep statistical distribution information.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:   :py:class:`Rttmonstatscollecttable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscollecttable>`
    
    .. attribute:: rttmonstatstotalstable
    
    	The statistics totals database.  This table has the exact same behavior as the rttMonStatsCaptureTable, except it only keeps 60 minute group values.  For a complete table description see the rttMonStatsCaptureTable object
    	**type**\:   :py:class:`Rttmonstatstotalstable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatstotalstable>`
    
    .. attribute:: rttmplsvpnmonctrltable
    
    	A table of Auto SAA L3 MPLS VPN definitions.  The Auto SAA L3 MPLS VPN administration control is in multiple tables.  This first table, is used to create a conceptual Auto SAA L3 MPLS VPN control row.  The following tables contain objects which used in type specific configurations, scheduling and reaction configurations. All of these tables will create the same conceptual control row as this table using this table's index as their own index.  In order to a row in this table to become active the following objects must be defined.   rttMplsVpnMonCtrlRttType,   rttMplsVpnMonCtrlVrfName and   rttMplsVpnMonSchedulePeriod
    	**type**\:   :py:class:`Rttmplsvpnmonctrltable <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable>`
    
    

    """

    _prefix = 'CISCO-RTTMON-MIB'
    _revision = '2012-08-16'

    def __init__(self):
        super(CiscoRttmonMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RTTMON-MIB"
        self.yang_parent_name = "CISCO-RTTMON-MIB"

        self.rttmonappl = CiscoRttmonMib.Rttmonappl()
        self.rttmonappl.parent = self
        self._children_name_map["rttmonappl"] = "rttMonAppl"
        self._children_yang_names.add("rttMonAppl")

        self.rttmonapplauthtable = CiscoRttmonMib.Rttmonapplauthtable()
        self.rttmonapplauthtable.parent = self
        self._children_name_map["rttmonapplauthtable"] = "rttMonApplAuthTable"
        self._children_yang_names.add("rttMonApplAuthTable")

        self.rttmonapplpreconfigedtable = CiscoRttmonMib.Rttmonapplpreconfigedtable()
        self.rttmonapplpreconfigedtable.parent = self
        self._children_name_map["rttmonapplpreconfigedtable"] = "rttMonApplPreConfigedTable"
        self._children_yang_names.add("rttMonApplPreConfigedTable")

        self.rttmonapplsupportedprotocolstable = CiscoRttmonMib.Rttmonapplsupportedprotocolstable()
        self.rttmonapplsupportedprotocolstable.parent = self
        self._children_name_map["rttmonapplsupportedprotocolstable"] = "rttMonApplSupportedProtocolsTable"
        self._children_yang_names.add("rttMonApplSupportedProtocolsTable")

        self.rttmonapplsupportedrtttypestable = CiscoRttmonMib.Rttmonapplsupportedrtttypestable()
        self.rttmonapplsupportedrtttypestable.parent = self
        self._children_name_map["rttmonapplsupportedrtttypestable"] = "rttMonApplSupportedRttTypesTable"
        self._children_yang_names.add("rttMonApplSupportedRttTypesTable")

        self.rttmonctrladmintable = CiscoRttmonMib.Rttmonctrladmintable()
        self.rttmonctrladmintable.parent = self
        self._children_name_map["rttmonctrladmintable"] = "rttMonCtrlAdminTable"
        self._children_yang_names.add("rttMonCtrlAdminTable")

        self.rttmonechoadmintable = CiscoRttmonMib.Rttmonechoadmintable()
        self.rttmonechoadmintable.parent = self
        self._children_name_map["rttmonechoadmintable"] = "rttMonEchoAdminTable"
        self._children_yang_names.add("rttMonEchoAdminTable")

        self.rttmonechopathadmintable = CiscoRttmonMib.Rttmonechopathadmintable()
        self.rttmonechopathadmintable.parent = self
        self._children_name_map["rttmonechopathadmintable"] = "rttMonEchoPathAdminTable"
        self._children_yang_names.add("rttMonEchoPathAdminTable")

        self.rttmonfileioadmintable = CiscoRttmonMib.Rttmonfileioadmintable()
        self.rttmonfileioadmintable.parent = self
        self._children_name_map["rttmonfileioadmintable"] = "rttMonFileIOAdminTable"
        self._children_yang_names.add("rttMonFileIOAdminTable")

        self.rttmongeneratedopertable = CiscoRttmonMib.Rttmongeneratedopertable()
        self.rttmongeneratedopertable.parent = self
        self._children_name_map["rttmongeneratedopertable"] = "rttMonGeneratedOperTable"
        self._children_yang_names.add("rttMonGeneratedOperTable")

        self.rttmongrpscheduleadmintable = CiscoRttmonMib.Rttmongrpscheduleadmintable()
        self.rttmongrpscheduleadmintable.parent = self
        self._children_name_map["rttmongrpscheduleadmintable"] = "rttMonGrpScheduleAdminTable"
        self._children_yang_names.add("rttMonGrpScheduleAdminTable")

        self.rttmonhistorycollectiontable = CiscoRttmonMib.Rttmonhistorycollectiontable()
        self.rttmonhistorycollectiontable.parent = self
        self._children_name_map["rttmonhistorycollectiontable"] = "rttMonHistoryCollectionTable"
        self._children_yang_names.add("rttMonHistoryCollectionTable")

        self.rttmonhttpstatstable = CiscoRttmonMib.Rttmonhttpstatstable()
        self.rttmonhttpstatstable.parent = self
        self._children_name_map["rttmonhttpstatstable"] = "rttMonHTTPStatsTable"
        self._children_yang_names.add("rttMonHTTPStatsTable")

        self.rttmonjitterstatstable = CiscoRttmonMib.Rttmonjitterstatstable()
        self.rttmonjitterstatstable.parent = self
        self._children_name_map["rttmonjitterstatstable"] = "rttMonJitterStatsTable"
        self._children_yang_names.add("rttMonJitterStatsTable")

        self.rttmonlatesthttpopertable = CiscoRttmonMib.Rttmonlatesthttpopertable()
        self.rttmonlatesthttpopertable.parent = self
        self._children_name_map["rttmonlatesthttpopertable"] = "rttMonLatestHTTPOperTable"
        self._children_yang_names.add("rttMonLatestHTTPOperTable")

        self.rttmonlatestjitteropertable = CiscoRttmonMib.Rttmonlatestjitteropertable()
        self.rttmonlatestjitteropertable.parent = self
        self._children_name_map["rttmonlatestjitteropertable"] = "rttMonLatestJitterOperTable"
        self._children_yang_names.add("rttMonLatestJitterOperTable")

        self.rttmonlpdgrpstatstable = CiscoRttmonMib.Rttmonlpdgrpstatstable()
        self.rttmonlpdgrpstatstable.parent = self
        self._children_name_map["rttmonlpdgrpstatstable"] = "rttMonLpdGrpStatsTable"
        self._children_yang_names.add("rttMonLpdGrpStatsTable")

        self.rttmonreacttable = CiscoRttmonMib.Rttmonreacttable()
        self.rttmonreacttable.parent = self
        self._children_name_map["rttmonreacttable"] = "rttMonReactTable"
        self._children_yang_names.add("rttMonReactTable")

        self.rttmonreacttriggeradmintable = CiscoRttmonMib.Rttmonreacttriggeradmintable()
        self.rttmonreacttriggeradmintable.parent = self
        self._children_name_map["rttmonreacttriggeradmintable"] = "rttMonReactTriggerAdminTable"
        self._children_yang_names.add("rttMonReactTriggerAdminTable")

        self.rttmonscriptadmintable = CiscoRttmonMib.Rttmonscriptadmintable()
        self.rttmonscriptadmintable.parent = self
        self._children_name_map["rttmonscriptadmintable"] = "rttMonScriptAdminTable"
        self._children_yang_names.add("rttMonScriptAdminTable")

        self.rttmonstatscapturetable = CiscoRttmonMib.Rttmonstatscapturetable()
        self.rttmonstatscapturetable.parent = self
        self._children_name_map["rttmonstatscapturetable"] = "rttMonStatsCaptureTable"
        self._children_yang_names.add("rttMonStatsCaptureTable")

        self.rttmonstatscollecttable = CiscoRttmonMib.Rttmonstatscollecttable()
        self.rttmonstatscollecttable.parent = self
        self._children_name_map["rttmonstatscollecttable"] = "rttMonStatsCollectTable"
        self._children_yang_names.add("rttMonStatsCollectTable")

        self.rttmonstatstotalstable = CiscoRttmonMib.Rttmonstatstotalstable()
        self.rttmonstatstotalstable.parent = self
        self._children_name_map["rttmonstatstotalstable"] = "rttMonStatsTotalsTable"
        self._children_yang_names.add("rttMonStatsTotalsTable")

        self.rttmplsvpnmonctrltable = CiscoRttmonMib.Rttmplsvpnmonctrltable()
        self.rttmplsvpnmonctrltable.parent = self
        self._children_name_map["rttmplsvpnmonctrltable"] = "rttMplsVpnMonCtrlTable"
        self._children_yang_names.add("rttMplsVpnMonCtrlTable")


    class Rttmonappl(Entity):
        """
        
        
        .. attribute:: rttmonapplfreememlowwatermark
        
        	This object defines the amount of free memory a router must have in order to configure RTR. If RTR found out that the memory is falling below this mark, it will not allow new probes to be configured.  This value should not be set higher (or very close to) than  the free bytes available on the router
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rttmonappllatestseterror
        
        	An error description for the last error message caused by set.  Currently, it includes set error caused due to setting rttMonApplFreeMemLowWaterMark greater than the available free memory on the router or not enough memory left to create new probes
        	**type**\:  str
        
        .. attribute:: rttmonappllpdgrpstatsreset
        
        	This object is used to reset certain objects within the rttMonLpdGrpStatsTable.  When the object is set to value of an active LPD Group identifier the associated objects will be reset. The reset objects will be set to a value as specified in the object's description.  The following objects will not be reset. \- rttMonLpdGrpStatsTargetPE \- rttMonLpdGrpStatsGroupProbeIndex \- rttMonLpdGrpStatsGroupIndex \- rttMonLpdGrpStatsStartTimeIndex
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rttmonapplmaxpacketdatasize
        
        	The maximum size of the data portion an echo packet supported by this RTT application.  This is the maximum value that can be specified by (rttMonEchoAdminPktDataRequestSize + ARR Header) or  (rttMonEchoAdminPktDataResponseSize + ARR Header) in the rttMonCtrlAdminTable.  This object is undefined for conceptual RTT  control rows when the RttMonRttType object is set to 'fileIO' or 'script'
        	**type**\:  int
        
        	**range:** 0..16384
        
        	**units**\: octets
        
        .. attribute:: rttmonapplnumctrladminentry
        
        	This object defines the maximum number of entries that can be added to the rttMonCtrlAdminTable. It is calculated at the system init time. The value is impacted when rttMonApplFreeMemLowWaterMark is changed
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: rttmonapplpreconfigedreset
        
        	When set to 'reset' the RTT application will reset the Application Preconfigured MIB section.  This will force the RTT application to delete all entries in the rttMonApplPreConfigedTable and then to repopulate the table with the current configuration.  This provides a mechanism to load and unload user scripts and file paths
        	**type**\:   :py:class:`Rttreset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttreset>`
        
        	**status**\: obsolete
        
        .. attribute:: rttmonapplprobecapacity
        
        	This object defines the number of new probes that can be configured on a router. The number depends on the value  of rttMonApplFreeMemLowWaterMark, free bytes available on the router and the system configured rttMonCtrlAdminEntry number. Equation\: rttMonApplProbeCapacity =  MIN(((Free\_Bytes\_on\_the\_Router \- rttMonApplFreeMemLowWaterMark)/ Memory\_required\_by\_each\_probe), rttMonApplNumCtrlAdminEntry \-  Num\_of\_Probes\_already\_configured))
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: rttmonapplreset
        
        	When set to 'reset' the entire RTT application goes through a reset sequence, making a best  effort to revert to its startup condition.  Any  and all rows in the Overall Control Group will be immediately deleted, together with any associated rows in the Statistics Collection Group, and  History Collection Group.  All open connections  will also be closed.  Finally the  rttMonApplPreConfigedTable will reset (see  rttMonApplPreConfigedReset)
        	**type**\:   :py:class:`Rttreset <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttreset>`
        
        .. attribute:: rttmonapplresponder
        
        	Enable or disable RTR responder on the router
        	**type**\:  bool
        
        .. attribute:: rttmonappltimeoflastset
        
        	The last time at which a set operation occurred on any of the objects in this MIB.  The managing  application can inspect this value in order to  determine whether changes have been made without  retrieving the entire Administration portion of this MIB.  This object applies to all settable objects in this MIB, including the 'Reset' objects that could clear saved history/statistics
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: rttmonapplversion
        
        	Round Trip Time monitoring application version string.  The format will be\:  'Version.Release.Patch\-Level\: Textual\-Description'  For example\:  '1.0.0\: Initial RTT Application'
        	**type**\:  str
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonappl, self).__init__()

            self.yang_name = "rttMonAppl"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonapplfreememlowwatermark = YLeaf(YType.int32, "rttMonApplFreeMemLowWaterMark")

            self.rttmonappllatestseterror = YLeaf(YType.str, "rttMonApplLatestSetError")

            self.rttmonappllpdgrpstatsreset = YLeaf(YType.int32, "rttMonApplLpdGrpStatsReset")

            self.rttmonapplmaxpacketdatasize = YLeaf(YType.int32, "rttMonApplMaxPacketDataSize")

            self.rttmonapplnumctrladminentry = YLeaf(YType.int32, "rttMonApplNumCtrlAdminEntry")

            self.rttmonapplpreconfigedreset = YLeaf(YType.enumeration, "rttMonApplPreConfigedReset")

            self.rttmonapplprobecapacity = YLeaf(YType.int32, "rttMonApplProbeCapacity")

            self.rttmonapplreset = YLeaf(YType.enumeration, "rttMonApplReset")

            self.rttmonapplresponder = YLeaf(YType.boolean, "rttMonApplResponder")

            self.rttmonappltimeoflastset = YLeaf(YType.uint32, "rttMonApplTimeOfLastSet")

            self.rttmonapplversion = YLeaf(YType.str, "rttMonApplVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("rttmonapplfreememlowwatermark",
                            "rttmonappllatestseterror",
                            "rttmonappllpdgrpstatsreset",
                            "rttmonapplmaxpacketdatasize",
                            "rttmonapplnumctrladminentry",
                            "rttmonapplpreconfigedreset",
                            "rttmonapplprobecapacity",
                            "rttmonapplreset",
                            "rttmonapplresponder",
                            "rttmonappltimeoflastset",
                            "rttmonapplversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRttmonMib.Rttmonappl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonappl, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.rttmonapplfreememlowwatermark.is_set or
                self.rttmonappllatestseterror.is_set or
                self.rttmonappllpdgrpstatsreset.is_set or
                self.rttmonapplmaxpacketdatasize.is_set or
                self.rttmonapplnumctrladminentry.is_set or
                self.rttmonapplpreconfigedreset.is_set or
                self.rttmonapplprobecapacity.is_set or
                self.rttmonapplreset.is_set or
                self.rttmonapplresponder.is_set or
                self.rttmonappltimeoflastset.is_set or
                self.rttmonapplversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.rttmonapplfreememlowwatermark.yfilter != YFilter.not_set or
                self.rttmonappllatestseterror.yfilter != YFilter.not_set or
                self.rttmonappllpdgrpstatsreset.yfilter != YFilter.not_set or
                self.rttmonapplmaxpacketdatasize.yfilter != YFilter.not_set or
                self.rttmonapplnumctrladminentry.yfilter != YFilter.not_set or
                self.rttmonapplpreconfigedreset.yfilter != YFilter.not_set or
                self.rttmonapplprobecapacity.yfilter != YFilter.not_set or
                self.rttmonapplreset.yfilter != YFilter.not_set or
                self.rttmonapplresponder.yfilter != YFilter.not_set or
                self.rttmonappltimeoflastset.yfilter != YFilter.not_set or
                self.rttmonapplversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonAppl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.rttmonapplfreememlowwatermark.is_set or self.rttmonapplfreememlowwatermark.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplfreememlowwatermark.get_name_leafdata())
            if (self.rttmonappllatestseterror.is_set or self.rttmonappllatestseterror.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonappllatestseterror.get_name_leafdata())
            if (self.rttmonappllpdgrpstatsreset.is_set or self.rttmonappllpdgrpstatsreset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonappllpdgrpstatsreset.get_name_leafdata())
            if (self.rttmonapplmaxpacketdatasize.is_set or self.rttmonapplmaxpacketdatasize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplmaxpacketdatasize.get_name_leafdata())
            if (self.rttmonapplnumctrladminentry.is_set or self.rttmonapplnumctrladminentry.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplnumctrladminentry.get_name_leafdata())
            if (self.rttmonapplpreconfigedreset.is_set or self.rttmonapplpreconfigedreset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplpreconfigedreset.get_name_leafdata())
            if (self.rttmonapplprobecapacity.is_set or self.rttmonapplprobecapacity.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplprobecapacity.get_name_leafdata())
            if (self.rttmonapplreset.is_set or self.rttmonapplreset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplreset.get_name_leafdata())
            if (self.rttmonapplresponder.is_set or self.rttmonapplresponder.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplresponder.get_name_leafdata())
            if (self.rttmonappltimeoflastset.is_set or self.rttmonappltimeoflastset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonappltimeoflastset.get_name_leafdata())
            if (self.rttmonapplversion.is_set or self.rttmonapplversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rttmonapplversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonApplFreeMemLowWaterMark" or name == "rttMonApplLatestSetError" or name == "rttMonApplLpdGrpStatsReset" or name == "rttMonApplMaxPacketDataSize" or name == "rttMonApplNumCtrlAdminEntry" or name == "rttMonApplPreConfigedReset" or name == "rttMonApplProbeCapacity" or name == "rttMonApplReset" or name == "rttMonApplResponder" or name == "rttMonApplTimeOfLastSet" or name == "rttMonApplVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "rttMonApplFreeMemLowWaterMark"):
                self.rttmonapplfreememlowwatermark = value
                self.rttmonapplfreememlowwatermark.value_namespace = name_space
                self.rttmonapplfreememlowwatermark.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplLatestSetError"):
                self.rttmonappllatestseterror = value
                self.rttmonappllatestseterror.value_namespace = name_space
                self.rttmonappllatestseterror.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplLpdGrpStatsReset"):
                self.rttmonappllpdgrpstatsreset = value
                self.rttmonappllpdgrpstatsreset.value_namespace = name_space
                self.rttmonappllpdgrpstatsreset.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplMaxPacketDataSize"):
                self.rttmonapplmaxpacketdatasize = value
                self.rttmonapplmaxpacketdatasize.value_namespace = name_space
                self.rttmonapplmaxpacketdatasize.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplNumCtrlAdminEntry"):
                self.rttmonapplnumctrladminentry = value
                self.rttmonapplnumctrladminentry.value_namespace = name_space
                self.rttmonapplnumctrladminentry.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplPreConfigedReset"):
                self.rttmonapplpreconfigedreset = value
                self.rttmonapplpreconfigedreset.value_namespace = name_space
                self.rttmonapplpreconfigedreset.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplProbeCapacity"):
                self.rttmonapplprobecapacity = value
                self.rttmonapplprobecapacity.value_namespace = name_space
                self.rttmonapplprobecapacity.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplReset"):
                self.rttmonapplreset = value
                self.rttmonapplreset.value_namespace = name_space
                self.rttmonapplreset.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplResponder"):
                self.rttmonapplresponder = value
                self.rttmonapplresponder.value_namespace = name_space
                self.rttmonapplresponder.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplTimeOfLastSet"):
                self.rttmonappltimeoflastset = value
                self.rttmonappltimeoflastset.value_namespace = name_space
                self.rttmonappltimeoflastset.value_namespace_prefix = name_space_prefix
            if(value_path == "rttMonApplVersion"):
                self.rttmonapplversion = value
                self.rttmonapplversion.value_namespace = name_space
                self.rttmonapplversion.value_namespace_prefix = name_space_prefix


    class Rttmonapplsupportedrtttypestable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Types.
        
        See the RttMonRttType textual convention for
        the definition of each type.
        
        .. attribute:: rttmonapplsupportedrtttypesentry
        
        	A list that presents the valid Rtt Monitor Types
        	**type**\: list of    :py:class:`Rttmonapplsupportedrtttypesentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable, self).__init__()

            self.yang_name = "rttMonApplSupportedRttTypesTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonapplsupportedrtttypesentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable, self).__setattr__(name, value)


        class Rttmonapplsupportedrtttypesentry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Types.
            
            .. attribute:: rttmonapplsupportedrtttypes  <key>
            
            	This object indexes the supported 'RttMonRttType' types
            	**type**\:   :py:class:`Rttmonrtttype <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonrtttype>`
            
            .. attribute:: rttmonapplsupportedrtttypesvalid
            
            	This object defines the supported 'RttMonRttType' types
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry, self).__init__()

                self.yang_name = "rttMonApplSupportedRttTypesEntry"
                self.yang_parent_name = "rttMonApplSupportedRttTypesTable"

                self.rttmonapplsupportedrtttypes = YLeaf(YType.enumeration, "rttMonApplSupportedRttTypes")

                self.rttmonapplsupportedrtttypesvalid = YLeaf(YType.boolean, "rttMonApplSupportedRttTypesValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonapplsupportedrtttypes",
                                "rttmonapplsupportedrtttypesvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonapplsupportedrtttypes.is_set or
                    self.rttmonapplsupportedrtttypesvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonapplsupportedrtttypes.yfilter != YFilter.not_set or
                    self.rttmonapplsupportedrtttypesvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonApplSupportedRttTypesEntry" + "[rttMonApplSupportedRttTypes='" + self.rttmonapplsupportedrtttypes.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedRttTypesTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonapplsupportedrtttypes.is_set or self.rttmonapplsupportedrtttypes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplsupportedrtttypes.get_name_leafdata())
                if (self.rttmonapplsupportedrtttypesvalid.is_set or self.rttmonapplsupportedrtttypesvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplsupportedrtttypesvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonApplSupportedRttTypes" or name == "rttMonApplSupportedRttTypesValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonApplSupportedRttTypes"):
                    self.rttmonapplsupportedrtttypes = value
                    self.rttmonapplsupportedrtttypes.value_namespace = name_space
                    self.rttmonapplsupportedrtttypes.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplSupportedRttTypesValid"):
                    self.rttmonapplsupportedrtttypesvalid = value
                    self.rttmonapplsupportedrtttypesvalid.value_namespace = name_space
                    self.rttmonapplsupportedrtttypesvalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonapplsupportedrtttypesentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonapplsupportedrtttypesentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonApplSupportedRttTypesTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonApplSupportedRttTypesEntry"):
                for c in self.rttmonapplsupportedrtttypesentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonapplsupportedrtttypestable.Rttmonapplsupportedrtttypesentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonapplsupportedrtttypesentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonApplSupportedRttTypesEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonapplsupportedprotocolstable(Entity):
        """
        A table of which contains the supported Rtt
        Monitor Protocols.
        
        See the RttMonProtocol textual convention 
        for the definition of each protocol.
        
        .. attribute:: rttmonapplsupportedprotocolsentry
        
        	A list that presents the valid Rtt Monitor Protocols
        	**type**\: list of    :py:class:`Rttmonapplsupportedprotocolsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable, self).__init__()

            self.yang_name = "rttMonApplSupportedProtocolsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonapplsupportedprotocolsentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable, self).__setattr__(name, value)


        class Rttmonapplsupportedprotocolsentry(Entity):
            """
            A list that presents the valid Rtt Monitor
            Protocols.
            
            .. attribute:: rttmonapplsupportedprotocols  <key>
            
            	This object indexes the supported 'RttMonProtocol' protocols
            	**type**\:   :py:class:`Rttmonprotocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonprotocol>`
            
            .. attribute:: rttmonapplsupportedprotocolsvalid
            
            	This object defines the supported 'RttMonProtocol' protocols
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry, self).__init__()

                self.yang_name = "rttMonApplSupportedProtocolsEntry"
                self.yang_parent_name = "rttMonApplSupportedProtocolsTable"

                self.rttmonapplsupportedprotocols = YLeaf(YType.enumeration, "rttMonApplSupportedProtocols")

                self.rttmonapplsupportedprotocolsvalid = YLeaf(YType.boolean, "rttMonApplSupportedProtocolsValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonapplsupportedprotocols",
                                "rttmonapplsupportedprotocolsvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonapplsupportedprotocols.is_set or
                    self.rttmonapplsupportedprotocolsvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonapplsupportedprotocols.yfilter != YFilter.not_set or
                    self.rttmonapplsupportedprotocolsvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonApplSupportedProtocolsEntry" + "[rttMonApplSupportedProtocols='" + self.rttmonapplsupportedprotocols.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplSupportedProtocolsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonapplsupportedprotocols.is_set or self.rttmonapplsupportedprotocols.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplsupportedprotocols.get_name_leafdata())
                if (self.rttmonapplsupportedprotocolsvalid.is_set or self.rttmonapplsupportedprotocolsvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplsupportedprotocolsvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonApplSupportedProtocols" or name == "rttMonApplSupportedProtocolsValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonApplSupportedProtocols"):
                    self.rttmonapplsupportedprotocols = value
                    self.rttmonapplsupportedprotocols.value_namespace = name_space
                    self.rttmonapplsupportedprotocols.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplSupportedProtocolsValid"):
                    self.rttmonapplsupportedprotocolsvalid = value
                    self.rttmonapplsupportedprotocolsvalid.value_namespace = name_space
                    self.rttmonapplsupportedprotocolsvalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonapplsupportedprotocolsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonapplsupportedprotocolsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonApplSupportedProtocolsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonApplSupportedProtocolsEntry"):
                for c in self.rttmonapplsupportedprotocolsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonapplsupportedprotocolstable.Rttmonapplsupportedprotocolsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonapplsupportedprotocolsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonApplSupportedProtocolsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonapplpreconfigedtable(Entity):
        """
        A table of which contains the previously
        configured Script Names and File IO targets.
        
        These Script Names and File IO targets are installed
        via a different mechanism than this application, and
        are specific to each platform.
        
        .. attribute:: rttmonapplpreconfigedentry
        
        	A list of objects that describe the previously configured Script Names and File IO targets
        	**type**\: list of    :py:class:`Rttmonapplpreconfigedentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonapplpreconfigedtable, self).__init__()

            self.yang_name = "rttMonApplPreConfigedTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonapplpreconfigedentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonapplpreconfigedtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonapplpreconfigedtable, self).__setattr__(name, value)


        class Rttmonapplpreconfigedentry(Entity):
            """
            A list of objects that describe the previously
            configured Script Names and File IO targets.
            
            .. attribute:: rttmonapplpreconfigedtype  <key>
            
            	This is the type of value being stored in the rttMonApplPreConfigedName object
            	**type**\:   :py:class:`Rttmonapplpreconfigedtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry.Rttmonapplpreconfigedtype>`
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedname  <key>
            
            	This is either one of the following depending on the value of the rttMonApplPreConfigedType object\:   \- The file path to a server.  One of these file paths     must be used when defining an entry in the     rttMonFileIOAdminTable table with 'fileIO' as the     value of the rttMonCtrlAdminRttType object.   \- The script name to be used when generating RTT     operations.  One of these script names must be used     when defining an entry in the rttMonScriptAdminTable     table with 'script' as the value of the     rttMonCtrlAdminRttType object.  NOTE\:  For script names, command line parameters         can follow these names in the         rttMonScriptAdminTable table
            	**type**\:  str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonapplpreconfigedvalid
            
            	When this row exists, this value will be 'true'. This object exists only to create a valid row in this  table
            	**type**\:  bool
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry, self).__init__()

                self.yang_name = "rttMonApplPreConfigedEntry"
                self.yang_parent_name = "rttMonApplPreConfigedTable"

                self.rttmonapplpreconfigedtype = YLeaf(YType.enumeration, "rttMonApplPreConfigedType")

                self.rttmonapplpreconfigedname = YLeaf(YType.str, "rttMonApplPreConfigedName")

                self.rttmonapplpreconfigedvalid = YLeaf(YType.boolean, "rttMonApplPreConfigedValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonapplpreconfigedtype",
                                "rttmonapplpreconfigedname",
                                "rttmonapplpreconfigedvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry, self).__setattr__(name, value)

            class Rttmonapplpreconfigedtype(Enum):
                """
                Rttmonapplpreconfigedtype

                This is the type of value being stored in the

                rttMonApplPreConfigedName object.

                .. data:: filePath = 1

                .. data:: scriptName = 2

                """

                filePath = Enum.YLeaf(1, "filePath")

                scriptName = Enum.YLeaf(2, "scriptName")


            def has_data(self):
                return (
                    self.rttmonapplpreconfigedtype.is_set or
                    self.rttmonapplpreconfigedname.is_set or
                    self.rttmonapplpreconfigedvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonapplpreconfigedtype.yfilter != YFilter.not_set or
                    self.rttmonapplpreconfigedname.yfilter != YFilter.not_set or
                    self.rttmonapplpreconfigedvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonApplPreConfigedEntry" + "[rttMonApplPreConfigedType='" + self.rttmonapplpreconfigedtype.get() + "']" + "[rttMonApplPreConfigedName='" + self.rttmonapplpreconfigedname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplPreConfigedTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonapplpreconfigedtype.is_set or self.rttmonapplpreconfigedtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplpreconfigedtype.get_name_leafdata())
                if (self.rttmonapplpreconfigedname.is_set or self.rttmonapplpreconfigedname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplpreconfigedname.get_name_leafdata())
                if (self.rttmonapplpreconfigedvalid.is_set or self.rttmonapplpreconfigedvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplpreconfigedvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonApplPreConfigedType" or name == "rttMonApplPreConfigedName" or name == "rttMonApplPreConfigedValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonApplPreConfigedType"):
                    self.rttmonapplpreconfigedtype = value
                    self.rttmonapplpreconfigedtype.value_namespace = name_space
                    self.rttmonapplpreconfigedtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplPreConfigedName"):
                    self.rttmonapplpreconfigedname = value
                    self.rttmonapplpreconfigedname.value_namespace = name_space
                    self.rttmonapplpreconfigedname.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplPreConfigedValid"):
                    self.rttmonapplpreconfigedvalid = value
                    self.rttmonapplpreconfigedvalid.value_namespace = name_space
                    self.rttmonapplpreconfigedvalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonapplpreconfigedentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonapplpreconfigedentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonApplPreConfigedTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonApplPreConfigedEntry"):
                for c in self.rttmonapplpreconfigedentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonapplpreconfigedtable.Rttmonapplpreconfigedentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonapplpreconfigedentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonApplPreConfigedEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonapplauthtable(Entity):
        """
        A table which contains the definitions for key\-strings
        that will be used in authenticating RTR Control Protocol.
        
        .. attribute:: rttmonapplauthentry
        
        	A list that presents the valid parameters for Authenticating RTR Control Protocol
        	**type**\: list of    :py:class:`Rttmonapplauthentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonapplauthtable.Rttmonapplauthentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonapplauthtable, self).__init__()

            self.yang_name = "rttMonApplAuthTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonapplauthentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonapplauthtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonapplauthtable, self).__setattr__(name, value)


        class Rttmonapplauthentry(Entity):
            """
            A list that presents the valid parameters for Authenticating
            RTR Control Protocol.
            
            .. attribute:: rttmonapplauthindex  <key>
            
            	Uniquely identifies a row in the rttMonApplAuthTable. This is a pseudo\-random number selected by the management station when creating a row via the rttMonApplAuthStatus  object. If the pseudo\-random number is already in use, an  'inconsistentValue' is returned. Currently, only one row  can be created
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonapplauthkeychain
            
            	A string which represents the key\-chain name. If multiple key\-strings are specified, then the authenticator will  alternate between the specified strings
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring1
            
            	A string which represents a key\-string name whose id is 1
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring2
            
            	A string which represents a key\-string name whose id is 2
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring3
            
            	A string which represents a key\-string name whose id is 3
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring4
            
            	A string which represents a key\-string name whose id is 4
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthkeystring5
            
            	A string which represents a key\-string name whose id is 5
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: rttmonapplauthstatus
            
            	The status of the Authentication row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonapplauthtable.Rttmonapplauthentry, self).__init__()

                self.yang_name = "rttMonApplAuthEntry"
                self.yang_parent_name = "rttMonApplAuthTable"

                self.rttmonapplauthindex = YLeaf(YType.int32, "rttMonApplAuthIndex")

                self.rttmonapplauthkeychain = YLeaf(YType.str, "rttMonApplAuthKeyChain")

                self.rttmonapplauthkeystring1 = YLeaf(YType.str, "rttMonApplAuthKeyString1")

                self.rttmonapplauthkeystring2 = YLeaf(YType.str, "rttMonApplAuthKeyString2")

                self.rttmonapplauthkeystring3 = YLeaf(YType.str, "rttMonApplAuthKeyString3")

                self.rttmonapplauthkeystring4 = YLeaf(YType.str, "rttMonApplAuthKeyString4")

                self.rttmonapplauthkeystring5 = YLeaf(YType.str, "rttMonApplAuthKeyString5")

                self.rttmonapplauthstatus = YLeaf(YType.enumeration, "rttMonApplAuthStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonapplauthindex",
                                "rttmonapplauthkeychain",
                                "rttmonapplauthkeystring1",
                                "rttmonapplauthkeystring2",
                                "rttmonapplauthkeystring3",
                                "rttmonapplauthkeystring4",
                                "rttmonapplauthkeystring5",
                                "rttmonapplauthstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonapplauthtable.Rttmonapplauthentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonapplauthtable.Rttmonapplauthentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonapplauthindex.is_set or
                    self.rttmonapplauthkeychain.is_set or
                    self.rttmonapplauthkeystring1.is_set or
                    self.rttmonapplauthkeystring2.is_set or
                    self.rttmonapplauthkeystring3.is_set or
                    self.rttmonapplauthkeystring4.is_set or
                    self.rttmonapplauthkeystring5.is_set or
                    self.rttmonapplauthstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonapplauthindex.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeychain.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeystring1.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeystring2.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeystring3.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeystring4.yfilter != YFilter.not_set or
                    self.rttmonapplauthkeystring5.yfilter != YFilter.not_set or
                    self.rttmonapplauthstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonApplAuthEntry" + "[rttMonApplAuthIndex='" + self.rttmonapplauthindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonApplAuthTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonapplauthindex.is_set or self.rttmonapplauthindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthindex.get_name_leafdata())
                if (self.rttmonapplauthkeychain.is_set or self.rttmonapplauthkeychain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeychain.get_name_leafdata())
                if (self.rttmonapplauthkeystring1.is_set or self.rttmonapplauthkeystring1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeystring1.get_name_leafdata())
                if (self.rttmonapplauthkeystring2.is_set or self.rttmonapplauthkeystring2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeystring2.get_name_leafdata())
                if (self.rttmonapplauthkeystring3.is_set or self.rttmonapplauthkeystring3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeystring3.get_name_leafdata())
                if (self.rttmonapplauthkeystring4.is_set or self.rttmonapplauthkeystring4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeystring4.get_name_leafdata())
                if (self.rttmonapplauthkeystring5.is_set or self.rttmonapplauthkeystring5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthkeystring5.get_name_leafdata())
                if (self.rttmonapplauthstatus.is_set or self.rttmonapplauthstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonapplauthstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonApplAuthIndex" or name == "rttMonApplAuthKeyChain" or name == "rttMonApplAuthKeyString1" or name == "rttMonApplAuthKeyString2" or name == "rttMonApplAuthKeyString3" or name == "rttMonApplAuthKeyString4" or name == "rttMonApplAuthKeyString5" or name == "rttMonApplAuthStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonApplAuthIndex"):
                    self.rttmonapplauthindex = value
                    self.rttmonapplauthindex.value_namespace = name_space
                    self.rttmonapplauthindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyChain"):
                    self.rttmonapplauthkeychain = value
                    self.rttmonapplauthkeychain.value_namespace = name_space
                    self.rttmonapplauthkeychain.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyString1"):
                    self.rttmonapplauthkeystring1 = value
                    self.rttmonapplauthkeystring1.value_namespace = name_space
                    self.rttmonapplauthkeystring1.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyString2"):
                    self.rttmonapplauthkeystring2 = value
                    self.rttmonapplauthkeystring2.value_namespace = name_space
                    self.rttmonapplauthkeystring2.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyString3"):
                    self.rttmonapplauthkeystring3 = value
                    self.rttmonapplauthkeystring3.value_namespace = name_space
                    self.rttmonapplauthkeystring3.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyString4"):
                    self.rttmonapplauthkeystring4 = value
                    self.rttmonapplauthkeystring4.value_namespace = name_space
                    self.rttmonapplauthkeystring4.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthKeyString5"):
                    self.rttmonapplauthkeystring5 = value
                    self.rttmonapplauthkeystring5.value_namespace = name_space
                    self.rttmonapplauthkeystring5.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonApplAuthStatus"):
                    self.rttmonapplauthstatus = value
                    self.rttmonapplauthstatus.value_namespace = name_space
                    self.rttmonapplauthstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonapplauthentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonapplauthentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonApplAuthTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonApplAuthEntry"):
                for c in self.rttmonapplauthentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonapplauthtable.Rttmonapplauthentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonapplauthentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonApplAuthEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonctrladminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonctrladmintable, self).__init__()

            self.yang_name = "rttMonCtrlAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonctrladminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonctrladmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonctrladmintable, self).__setattr__(name, value)


        class Rttmonctrladminentry(Entity):
            """
            A base list of objects that define a conceptual RTT
            control row.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	Uniquely identifies a row in the rttMonCtrlAdminTable. This is a pseudo\-random number, selected by the management  station or auto\-generated based on  operation started by the  management station,when creating a row via  the rttMonCtrlAdminStatus object.  If the pseudo\-random   number is already in use an 'inconsistentValue' return code   will be returned when set operation is attempted
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonctrladminfrequency
            
            	Specifies the duration between initiating each RTT operation.   This object cannot be set to a value which would be a  shorter duration than rttMonCtrlAdminTimeout.  When the RttMonRttType specifies an operation that is synchronous in nature, it may happen that the next RTT  operation is blocked by a RTT operation which has not yet completed.  In this case, the value of a counter (rttMonStatsCollectBusies) in rttMonStatsCaptureTable is incremented in lieu of initiating a RTT operation, and  the next attempt will occur at the next rttMonCtrlAdminFrequency expiration.   NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'pathEcho', setting this value to a small        value for your network size may cause an operation        attempt (or multiple attempts) to be started         before the previous operation has finished.  In         this situation the rttMonStatsCollectBusies object        will be incremented in lieu of initiating a new         RTT operation, and the next attempt will occur at        the next rttMonCtrlAdminFrequency expiration.  When the rttMonCtrlAdminRttType object is defined to be 'pathEcho', the suggested value for this object  is greater than rttMonCtrlAdminTimeout times the  maximum number of expected hops to the target.  NOTE\:  When the rttMonCtrlAdminRttType object is defined         to be 'dhcp', the minimum allowed value for this        object is 10 seconds.  This restriction is due to        protocol limitations described in RFC 2131
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrladmingroupname
            
            	If the operation is created through auto measure group creation, then this string will specify the group name to which this operation is associated
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: rttmonctrladminnvgen
            
            	When set to true, this entry will be shown in 'show running' command and can be saved into Non\-volatile memory
            	**type**\:  bool
            
            .. attribute:: rttmonctrladminowner
            
            	Identifies the entity that created this table row
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: rttmonctrladminrtttype
            
            	The type of RTT operation to be performed.  This value must be set in the same PDU or before setting any type specific configuration.  Note\: The RTT operation 'lspGroup' cannot be created via this control row. It will be created automatically by Auto SAA L3 MPLS VPN when rttMplsVpnMonCtrlLpd is 'true'
            	**type**\:   :py:class:`Rttmonrtttype <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonrtttype>`
            
            .. attribute:: rttmonctrladminstatus
            
            	The status of the conceptual RTT control row.  In order for this object to become active, the following  row objects must be defined\:    \- rttMonCtrlAdminRttType Additionally\:  \- for echo, pathEcho based on 'ipIcmpEcho' and dlsw probes     rttMonEchoAdminProtocol and      rttMonEchoAdminTargetAddress;  \- for echo, pathEcho based on 'mplsLspPingAppl'     rttMonEchoAdminProtocol, rttMonEchoAdminTargetAddress      and rttMonEchoAdminLSPFECType  \- for udpEcho, tcpConnect and jitter probes     rttMonEchoAdminTargetAddress and     rttMonEchoAdminTargetPort  \- for http and ftp probe     rttMonEchoAdminURL   \- for dns probe     rttMonEchoAdminTargetAddressString      rttMonEchoAdminNameServer   \- dhcp probe doesn't require any additional objects  All other objects can assume default values. The  conceptual Rtt control row will be placed into a  'pending' state (via the rttMonCtrlOperState object) if rttMonScheduleAdminRttStartTime is not specified.  Most conceptual Rtt control row objects cannot be  modified once this conceptual Rtt control row has been  created.  The objects that can change are the following\:   \- Objects in the rttMonReactAdminTable can be modified    as needed without setting this object to     'notInService'.  \- Objects in the rttMonScheduleAdminTable can be     modified only when this object has the value of    'notInService'.  \- The rttMonCtrlOperState can be modified to control    the state of the probe.  Once this object is in 'active' status, it cannot be  set to 'notInService' while the rttMonCtrlOperState is in 'active' state.  Thus the rttMonCtrlOperState  object must be transitioned first.   This object can be set to 'destroy' from any value at any time
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rttmonctrladmintag
            
            	A string which is used by a managing application to identify the RTT target.  This string is inserted into trap notifications, but has no other significance to the  agent
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: rttmonctrladminthreshold
            
            	This object defines an administrative threshold limit. If the RTT operation time exceeds this limit and if the  conditions specified in rttMonReactAdminThresholdType or  rttMonHistoryAdminFilter are satisfied, a threshold is generated
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladmintimeout
            
            	Specifies the duration to wait for a RTT operation completion.  The value of this object cannot be set to  a value which would specify a duration exceeding  rttMonCtrlAdminFrequency.  For connection oriented protocols, this may cause the connection to be closed by the probe.  Once closed, it will be assumed that the connection reestablishment will be performed.  To prevent unwanted closure of connections, be sure to set this value to a realistic connection timeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonctrladminverifydata
            
            	When set to true, the resulting data in each RTT operation is compared with the expected data.  This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object.  Some RttMonRttTypes may not support this option.  When a type does not support this option, the agent will  transition this object to false.  It is the management applications responsibility to check for this  transition
            	**type**\:  bool
            
            .. attribute:: rttmonctrloperconnectionlostoccurred
            
            	This object will only change its value when the RttMonRttType is 'echo' or 'pathEcho'.  This object is set to true when the RTT connection fails  to be established or is lost, and set to false when a  connection is reestablished.  When the RttMonRttType is 'pathEcho', connection loss applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  When this value changes and  rttMonReactAdminConnectionEnable is true, a reaction  will occur.   If a trap is sent it is a  rttMonConnectionChangeNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'connectionLoss(8)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'connectionLoss'
            	**type**\:  bool
            
            .. attribute:: rttmonctrloperdiagtext
            
            	A string which can be used as an aid in tracing problems. The content of this field will depend on the type of  target (rttMonEchoAdminProtocol).   When rttMonEchoAdminProtocol is one of snaLU0EchoAppl, or  snaLU2EchoAppl this object contains the name of the  Logical Unit (LU) being used for this RTT session (from the HOST's point of view), once the session has been  established; this can then be used to correlate this  name to the connection information stored in the  Mainframe Host.  When rttMonEchoAdminProtocol is snaLU62EchoAppl, this  object contains the Logical Unit (LU) name being used for this RTT session, once the session has been established.   This name can be used by the management application to  correlate this objects value to the connection  information stored at this SNMP Agent via the APPC or  APPN mib.  When rttMonEchoAdminProtocol is not one of the  previously mentioned values, this value will be null.  It is primarily intended that this object contains  information which has significance to a human operator
            	**type**\:  str
            
            	**length:** 0..51
            
            .. attribute:: rttmonctrlopermodificationtime
            
            	This object is updated whenever an object in the conceptual RTT control row is changed or updated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrlopernumrtts
            
            	This is the total number of probe operations that have been attempted.     This value is incremented for each start of an RTT  operation.  Thus when rttMonCtrlAdminRttType is set to  'pathEcho' this value will be incremented by one and  not for very every hop along the path.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object.  This value is not effected by the rollover of a statistics hourly group
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonctrloperoctetsinuse
            
            	This object is the number of octets currently in use by this composite conceptual RTT row.  A composite conceptual row include the control, statistics, and  history conceptual rows combined.  (All octets that are addressed via the rttMonCtrlAdminIndex in this mib.)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrloperoverthresholdoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is changed by operation completion times over threshold, as defined by rttMonReactAdminThresholdType.   When this value changes, a reaction may occur, as defined  by rttMonReactAdminThresholdType.   If a trap is sent it is a rttMonThresholdNotification.  This object is set to true if the operation completion time exceeds the rttMonCtrlAdminThreshold and set to false when an operation completes under rttMonCtrlAdminThreshold. When this value changes, a reaction may occur, as defined by rttMonReactThresholdType.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'rtt'
            	**type**\:  bool
            
            .. attribute:: rttmonctrloperresettime
            
            	This object is set when the rttMonCtrlOperState is set to reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonctrloperrttlife
            
            	This object is decremented every second, until it reaches zero.  When the value of this object is zero RTT operations for this row are suspended.  This  object will either reach zero by a countdown or  it will transition to zero via setting the rttMonCtrlOperState.  When this object reaches zero the agent needs to  transition the rttMonCtrlOperState to 'inactive'.  REMEMBER\:  The value 2147483647 has a special             meaning.  When this object has the            value 2147483647, this object will            not decrement.  And thus the life             time will never.  When the rttMonCtrlOperState object is 'active' and  the rttMonReactTriggerOperState object transitions to  'active' this object will not be updated with the  current value of rttMonCrtlAdminRttLife object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmonctrloperstate
            
            	The RttMonOperStatus object is used to manage the 'state' of the probe that is implementing  conceptual RTT control row.  This status object has six defined values\:  reset(1)          \- reset this entry, transition                     to 'pending' orderlyStop(2)    \- shutdown this entry at the end                      of the next RTT operation attempt,                       transition to 'inactive' immediateStop(3)  \- shutdown this entry immediately                      (if possible), transition to                       'inactive' pending(4)        \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control either                       via the rttMonScheduleAdminTable                       or the rttMonReactAdminTable/                      rttMonReactTriggerAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      reseting this object, and second                      by creating a conceptual Rtt control                      row with the                       rttMonScheduleAdminRttStartTime                      object with the its special value inactive(5)       \- this value is not settable and                      this conceptual RTT control row is                       waiting for further control via                      the rttMonScheduleAdminTable;                      This object can transition to this                      value via two mechanisms, first by                      setting this object to 'orderlyStop'                      or 'immediateStop', second by                       the rttMonCtrlOperRttLife object                      reaching zero active(6)         \- this value is not settable and                      this conceptual RTT control row is                      currently active restart(7)        \- this value is only settable when the                      state is active. It clears the data                      of this entry and remain on active state.  The probes action when this object is set to 'reset'\:   \-  all rows in rttMonStatsCaptureTable that relate to        this conceptual RTT control row are destroyed and        the indices are set to 1   \-  if rttMonStatisticsAdminNumHourGroups is not zero, a        single new rttMonStatsCaptureTable row is created   \-  all rows in rttMonHistoryCaptureTable that relate        to this RTT definition are destroyed and the indices       are set to 1   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperRttLife is set to        rttMonScheduleAdminRttLife   \-  rttMonCtrlOperNumRtts is set to zero   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur   \-  the next RTT operation is controlled by the objects       in the rttMonScheduleAdminTable or the        rttMonReactAdminTable/rttMonReactTriggerAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending'   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections must be maintained  This can be used to synchronize various RTT  definitions, so that the RTT requests occur  simultaneously, or as simultaneously as possible.  The probes action when this object transitions to    'inactive' (via setting this object to 'orderlyStop'    or 'immediateStop' or by rttMonCtrlOperRttLife    reaching zero)\:   \-  all statistics and history collection information       table entries will be closed and kept   \-  implied history used for timeout or threshold       notification (see rttMonReactAdminThresholdType or       rttMonReactThresholdType)       is purged   \-  rttMonCtrlOperTimeoutOccurred,        rttMonCtrlOperOverThresholdOccurred, and        rttMonCtrlOperConnectionLostOccurred are set to        false; if this causes a change in the value of        either of these objects, resolution notifications        will not occur.   \-  the next RTT request is controlled by the objects       in the rttMonScheduleAdminTable   \-  if the rttMonReactTriggerOperState is 'active', it        will transition to 'pending' (this denotes that       the Trigger will be ready the next time this       object goes active)   \-  all rttMonReactTriggerAdminEntries pointing to       this conceptual entry with their        rttMonReactTriggerOperState object 'active',        will transition their OperState to 'pending'   \-  all open connections are to be closed and cleanup.               rttMonCtrlOperState                     STATE           +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+           \|      A       \|       B      \|      C      \| ACTION       \|  'pending'   \|  'inactive'  \|   'active'  \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|inconsistent\- \|   noError   \| \|  to 'reset'    \|              \| Value        \|             \| \|                \|    \-> A      \|              \|   \-> A      \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| OperState set  \|    noError   \|    noError   \|   noError   \| \|to 'orderlyStop'\|    \-> B      \|    \-> B      \|   \-> B      \| \|     or to      \|              \|              \|             \| \|'immediateStop' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  Event causes  \|    \-> C      \|    \-> B      \|   \-> C      \| \| Trigger State  \|              \|              \|   see (3)   \| \| to transition  \|              \|              \|             \| \| to 'active'    \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> C      \|    \-> C      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of one.        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> A      \|   see (1)   \| \| transitions to \|              \|              \|             \| \| 'active' &     \|              \|              \|             \| \| RttStartTime is\|              \|              \|             \| \| special value  \|              \|              \|             \| \| of less than   \|              \|              \|             \| \| current time,  \|              \|              \|             \| \| excluding one. \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> A      \|    \-> B      \|   see (2)   \| \| transitions to \|              \|              \|             \| \| 'notInService' \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus    \|    \-> B      \|    \-> B      \|   \-> B      \| \| transitions to \|              \|              \|             \| \| 'delete'       \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \| AdminStatus is \|    \-> C      \|    \-> C      \|   \-> C      \| \| 'active' & the \|              \|              \|   see (3)   \| \| RttStartTime   \|              \|              \|             \| \| arrives        \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|   RowAgeout    \|    \-> B      \|    \-> B      \|   \-> B      \| \|    expires     \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  OperRttLife   \|    N/A       \|    N/A       \|   \-> B      \| \| counts down to \|              \|              \|             \| \| zero           \|              \|              \|             \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-+  (1) \- rttMonCtrlOperState must have transitioned to 'inactive' or 'pending' before the rttMonCtrlAdminStatus can transition to 'active'.  See (2). (2) \- rttMonCtrlAdminStatus cannot transition to 'notInService' unless rttMonCtrlOperState has been previously forced to 'inactive' or 'pending'. (3) \- when this happens the rttMonCtrlOperRttLife will not be updated with the rttMonCtrlAdminRttLife.  NOTE\:  In order for all objects in a PDU to be set        at the same time, this object can not be        part of a multi\-bound PDU
            	**type**\:   :py:class:`Rttmonctrloperstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonctrloperstate>`
            
            .. attribute:: rttmonctrlopertimeoutoccurred
            
            	This object will change its value for all RttMonRttTypes.  This object is set to true when an operation times out,  and set to false when an operation completes under  rttMonCtrlAdminTimeout.  When this value changes, a  reaction may occur, as defined by  rttMonReactAdminTimeoutEnable.   When the RttMonRttType is 'pathEcho', this timeout applies only to the rttMonEchoAdminTargetAddress and not to intermediate hops to the Target.  If a trap is sent it is a rttMonTimeoutNotification.  When this value changes and any one of the rttMonReactTable row has rttMonReactVar object value as 'timeout(7)', a reaction may occur.  If a trap is sent it is rttMonNotification with rttMonReactVar value of 'timeout'
            	**type**\:  bool
            
            .. attribute:: rttmonctrloperverifyerroroccurred
            
            	This object is true if rttMonCtrlAdminVerifyData is set to true and data corruption occurs
            	**type**\:  bool
            
            .. attribute:: rttmonhistoryadminfilter
            
            	Defines a filter for adding RTT results to the history buffer\:  none          \- no history is recorded all           \- the results of all completion times                   and failed completions are recorded overThreshold \- the results of completion times                  over rttMonCtrlAdminThreshold are                   recorded. failures      \- the results of failed operations (only)                   are recorded
            	**type**\:   :py:class:`Rttmonhistoryadminfilter <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonhistoryadminfilter>`
            
            .. attribute:: rttmonhistoryadminnumbuckets
            
            	The maximum number of history buckets to record.  When the RttMonRttType is 'pathEcho'  this value directly  represents a path to a target.  For all other  RttMonRttTypes this value should be set to the number  of operations to keep per lifetime.  After rttMonHistoryAdminNumBuckets are filled, the  and the oldest entries are deleted and the most recent rttMonHistoryAdminNumBuckets buckets are retained
            	**type**\:  int
            
            	**range:** 1..60
            
            .. attribute:: rttmonhistoryadminnumlives
            
            	The maximum number of history lives to record.  A life is defined by the countdown (or transition) to zero  by the rttMonCtrlOperRttLife object.  A new life is created when the same conceptual RTT control row is restarted via the transition of the  rttMonCtrlOperRttLife object and its subsequent  countdown.  The value of zero will shut off all  rttMonHistoryAdminTable data collection
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: rttmonhistoryadminnumsamples
            
            	The maximum number of history samples to record per bucket.  When the RttMonRttType is 'pathEcho' this  value directly represents the number of hops along a  path to a target, thus we can only support 30 hops. For all other RttMonRttTypes this value will be  forced to one by the agent
            	**type**\:  int
            
            	**range:** 1..30
            
            .. attribute:: rttmonlatestrttoperaddress
            
            	When the RttMonRttType is 'echo', 'pathEcho', 'udpEcho', 'tcpConnect', 'dns' and 'dlsw' this is a string which specifies  the address of the target for this RTT operation.  When the  RttMonRttType is not one of these types this object will  be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\:  str
            
            .. attribute:: rttmonlatestrttoperapplspecificsense
            
            	An application specific sense code for the completion status of the latest RTT operation.  This  object will only be valid when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestrttopercompletiontime
            
            	The completion time of the latest RTT operation successfully completed.  The unit of this object will be microsecond when rttMonCtrlAdminRttType is set to 'jitter' and  rttMonEchoAdminPrecision is set to 'microsecond'. Otherwise, the unit of this object will be millisecond
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds/microseconds
            
            .. attribute:: rttmonlatestrttopersense
            
            	A sense code for the completion status of the latest RTT operation
            	**type**\:   :py:class:`Rttresponsesense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttresponsesense>`
            
            .. attribute:: rttmonlatestrttopersensedescription
            
            	A sense description for the completion status of the latest RTT operation when the  rttMonLatestRttOperSense object is set to  'applicationSpecific'
            	**type**\:  str
            
            .. attribute:: rttmonlatestrttopertime
            
            	The value of the agent system time at the time of the latest RTT operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonreactadminactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched  conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated nmvtOnly           \- an SNA NMVT is generated triggerOnly        \- all trigger actions defined for this                        entry are initiated trapAndNmvt        \- both a trap and an SNA NMVT are                        generated trapAndTrigger     \- both a trap and all trigger actions                        are initiated  nmvtAndTrigger     \- both a NMVT and all trigger actions                        are initiated trapNmvtAndTrigger \- a NMVT, trap, and all trigger actions                       are initiated  A trigger action is defined via the  rttMonReactTriggerAdminTable. rttMonReactAdminActionType object is superseded by rttMonReactActionType
            	**type**\:   :py:class:`Rttmonreactadminactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonreactadminactiontype>`
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminconnectionenable
            
            	If true, a reaction is generated when a RTT operation to a rttMonEchoAdminTargetAddress (echo type) causes  rttMonCtrlOperConnectionLostOccurred to change its  value.  Thus connections to intermediate hops will  not cause this value to change. rttMonReactAdminConnectionEnable object is superseded by rttMonReactVar
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount
            
            	This object defines the 'x' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount object is superseded by rttMonReactThresholdCountX
            	**type**\:  int
            
            	**range:** 1..16
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdcount2
            
            	This object defines the 'y' value of the xOfy condition specified in rttMonReactAdminThresholdType. rttMonReactAdminThresholdCount2 object is superseded by rttMonReactThresholdCountyY
            	**type**\:  int
            
            	**range:** 1..16
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdfalling
            
            	This object defines a threshold limit. If the RTT operation time falls below this limit and if the conditions specified in rttMonReactAdminThresholdType are satisfied, an  threshold is generated. rttMonReactAdminThresholdFalling object is superseded by rttMonReactThresholdFalling
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminthresholdtype
            
            	This object specifies the conditions under which rttMonCtrlOperOverThresholdOccurred is changed\:  NOTE\:  When the RttMonRttType is 'pathEcho' this         objects' value and all associated         object values are only valid when RTT         'echo' operations are to the        rttMonEchoAdminTargetAddress object address.  Thus        'pathEcho' operations to intermediate        hops will not cause this object to change.  never       \- rttMonCtrlOperOverThresholdOccurred is                 never set immediate   \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold;                 conversely                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                 falls below                 rttMonReactAdminThresholdFalling  consecutive \- rttMonCtrlOperOverThresholdOccurred is set                 to true when an operation completion time                 exceeds rttMonCtrlAdminThreshold on                 rttMonReactAdminThresholdCount consecutive                 RTT operations; conversely,                 rttMonCtrlOperOverThresholdOccurred is set                 to false when an operation completion time                falls under the                 rttMonReactAdminThresholdFalling                 for the same number of consecutive                 operations  xOfy        \- rttMonCtrlOperOverThresholdOccurred is set                 to true when x (as specified by                 rttMonReactAdminThresholdCount) out of the                 last y (as specified by                 rttMonReactAdminThresholdCount2)                 operation completion time exceeds                 rttMonCtrlAdminThreshold;                 conversely, it is set to false when x,                 out of the last y operation completion                time fall below                rttMonReactAdminThresholdFalling                NOTE\: When x > y, the probe will never                      generate a reaction. average     \- rttMonCtrlOperOverThresholdOccurred is set                 to true when the running average of the                 previous rttMonReactAdminThresholdCount                 operation completion times exceed                 rttMonCtrlAdminThreshold; conversely, it                 is set to false when the running average                 falls below the                 rttMonReactAdminThresholdFalling  If this value is changed by a management station,  rttMonCtrlOperOverThresholdOccurred is set to false, but  no reaction is generated if the prior value of  rttMonCtrlOperOverThresholdOccurred was true. rttMonReactAdminThresholdType object is superseded by rttMonReactThresholdType
            	**type**\:   :py:class:`Rttmonreactadminthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry.Rttmonreactadminthresholdtype>`
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadmintimeoutenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperTimeoutOccurred  to change its value.    When the RttMonRttType is 'pathEcho' timeouts to  intermediate hops will not cause  rttMonCtrlOperTimeoutOccurred to change its value. rttMonReactAdminTimeoutEnable object is superseded by rttMonReactVar
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonreactadminverifyerrorenable
            
            	If true, a reaction is generated when a RTT operation causes rttMonCtrlOperVerifyErrorOccurred  to change its value. rttMonReactAdminVerifyErrorEnable object is superseded by rttMonReactVar
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: rttmonscheduleadminconceptrowageout
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active'  state, this timer will be reset and suspended.  When  this conceptual RTT control row enters a state other  than 'active', the timer will be restarted.  NOTE\:  When a conceptual Rtt control row ages out, the         agent needs to remove the associated entries in         the rttMonReactTriggerAdminTable and         rttMonReactTriggerOperTable.  When this value is set to zero, this entry will never be aged out. rttMonScheduleAdminConceptRowAgeout object is superseded by rttMonScheduleAdminConceptRowAgeoutV2
            	**type**\:  int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            	**status**\: deprecated
            
            .. attribute:: rttmonscheduleadminconceptrowageoutv2
            
            	The amount of time this conceptual Rtt control row will exist when not in an 'active' rttMonCtrlOperState.  When this conceptual Rtt control row enters an 'active' state, this timer will be reset and suspended.  When this conceptual RTT control row enters a state other than 'active', the timer will be restarted.  NOTE\:  It is the same as rttMonScheduleAdminConceptRowAgeout        except DEFVAL is 0 to be consistent with CLI ageout        default.  When this value is set to zero, this entry will never be aged out
            	**type**\:  int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: rttmonscheduleadminrttlife
            
            	This object value will be placed into the rttMonCtrlOperRttLife object when the rttMonCtrlOperState object transitions to 'active' or 'pending'.  The value 2147483647 has a special meaning.  When this object is set to 2147483647, the  rttMonCtrlOperRttLife object will not decrement.   And thus the life time will never end
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmonscheduleadminrttrecurring
            
            	When set to true, this entry will be scheduled to run automatically for the specified duration equal to the life configured, at the same time daily.  This value cannot be set to true  (a) if rttMonScheduleAdminRttLife object has value greater or    equal to 86400 seconds. (b) if sum of values of rttMonScheduleAdminRttLife and    rttMonScheduleAdminConceptRowAgeout is less or equal to    86400 seconds
            	**type**\:  bool
            
            .. attribute:: rttmonscheduleadminrttstarttime
            
            	This is the time when this conceptional row will activate.    This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will  cause the activation of a conceptual Rtt row.  When an agent has the capability to determine date and  time, the agent should store this object as DateAndTime. This allows the agent to completely reset (restart) and still be able to start conceptual Rtt rows at the  intended time.  If the agent cannot keep date and time and the agent resets, all entries should take on one of the special value defined below.  The first special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'active' state when the rttMonCtrlAdminStatus  object transitions to active. This special value is defined to be a value of this object that, when initially set, is 1.  The second special value allows this conceptual Rtt  control row to immediately transition the  rttMonCtrlOperState object into 'pending' state when  the rttMonCtrlAdminStatus object transitions to active.   Also, when the rttMonCtrlOperRttLife counts down to zero  (and not when set to zero), this special value causes  this conceptual Rtt control row to  retransition the  rttMonCtrlOperState object into 'pending' state.  This  special value is defined to be a value of this object  that, when initially set, is smaller than the current sysUpTime. (With the exception of one, as defined in the previous paragraph)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatisticsadmindistinterval
            
            	The statistical distribution buckets interval.  Distribution Bucket Example\:  rttMonStatisticsAdminNumDistBuckets = 5 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1 \| Bucket 2 \| Bucket 3 \| Bucket 4 \| Bucket 5  \| \|  0\-9 ms  \| 10\-19 ms \| 20\-29 ms \| 30\-39 ms \| 40\-Inf ms \|  Odd Example\:  rttMonStatisticsAdminNumDistBuckets = 1 buckets rttMonStatisticsAdminDistInterval = 10 milliseconds  \| Bucket 1  \| \|  0\-Inf ms \|  Thus, this odd example shows that the value of  rttMonStatisticsAdminDistInterval does not apply when rttMonStatisticsAdminNumDistBuckets is one. This object is not applicable to http and jitter probes
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatisticsadminnumdistbuckets
            
            	The maximum number of statistical distribution Buckets to accumulate.  Since this index does not rollover, only the first rttMonStatisticsAdminNumDistBuckets will be kept.  The last rttMonStatisticsAdminNumDistBucket will contain all entries from its distribution interval start point to infinity. This object is not applicable  to http and jitter probes
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: rttmonstatisticsadminnumhops
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics hops to record per path group.   This value directly represents the number of hops along  a path to a target, thus we can only support 30 hops.   For all other RttMonRttTypes this value will be  forced to one by the agent.  Since this index does not rollover, only the first rttMonStatisticsAdminNumHops will be kept. This object  is applicable to pathEcho probes only
            	**type**\:  int
            
            	**range:** 1..30
            
            .. attribute:: rttmonstatisticsadminnumhourgroups
            
            	The maximum number of groups of paths to record. Specifically this is the number of hourly groups  to keep before rolling over.    The value of one is not advisable because the  group will close and immediately be deleted before the network management station will have the  opportunity to retrieve the statistics.   The value used in the rttMonStatsCaptureTable to  uniquely identify this group is the  rttMonStatsCaptureStartTimeIndex.  HTTP and Jitter probes store only two hours of data.  When this object is set to the value of zero all  rttMonStatsCaptureTable data capturing will be shut off
            	**type**\:  int
            
            	**range:** 0..25
            
            .. attribute:: rttmonstatisticsadminnumpaths
            
            	When RttMonRttType is 'pathEcho' this is the maximum number of statistics paths to record per hourly group.   This value directly represents the path to a target.   For all other RttMonRttTypes this value will be  forced to one by the agent.  NOTE\: For 'pathEcho' a source to target path will be        created to to hold all errors that occur when a        specific path or connection has not be found/setup.        Thus, it is advised to set this value greater       than one.  Since this index does not rollover, only the first rttMonStatisticsAdminNumPaths will be kept
            	**type**\:  int
            
            	**range:** 1..128
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry, self).__init__()

                self.yang_name = "rttMonCtrlAdminEntry"
                self.yang_parent_name = "rttMonCtrlAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.int32, "rttMonCtrlAdminIndex")

                self.rttmonctrladminfrequency = YLeaf(YType.int32, "rttMonCtrlAdminFrequency")

                self.rttmonctrladmingroupname = YLeaf(YType.str, "rttMonCtrlAdminGroupName")

                self.rttmonctrladminnvgen = YLeaf(YType.boolean, "rttMonCtrlAdminNvgen")

                self.rttmonctrladminowner = YLeaf(YType.str, "rttMonCtrlAdminOwner")

                self.rttmonctrladminrtttype = YLeaf(YType.enumeration, "rttMonCtrlAdminRttType")

                self.rttmonctrladminstatus = YLeaf(YType.enumeration, "rttMonCtrlAdminStatus")

                self.rttmonctrladmintag = YLeaf(YType.str, "rttMonCtrlAdminTag")

                self.rttmonctrladminthreshold = YLeaf(YType.int32, "rttMonCtrlAdminThreshold")

                self.rttmonctrladmintimeout = YLeaf(YType.int32, "rttMonCtrlAdminTimeout")

                self.rttmonctrladminverifydata = YLeaf(YType.boolean, "rttMonCtrlAdminVerifyData")

                self.rttmonctrloperconnectionlostoccurred = YLeaf(YType.boolean, "rttMonCtrlOperConnectionLostOccurred")

                self.rttmonctrloperdiagtext = YLeaf(YType.str, "rttMonCtrlOperDiagText")

                self.rttmonctrlopermodificationtime = YLeaf(YType.uint32, "rttMonCtrlOperModificationTime")

                self.rttmonctrlopernumrtts = YLeaf(YType.int32, "rttMonCtrlOperNumRtts")

                self.rttmonctrloperoctetsinuse = YLeaf(YType.uint32, "rttMonCtrlOperOctetsInUse")

                self.rttmonctrloperoverthresholdoccurred = YLeaf(YType.boolean, "rttMonCtrlOperOverThresholdOccurred")

                self.rttmonctrloperresettime = YLeaf(YType.uint32, "rttMonCtrlOperResetTime")

                self.rttmonctrloperrttlife = YLeaf(YType.int32, "rttMonCtrlOperRttLife")

                self.rttmonctrloperstate = YLeaf(YType.enumeration, "rttMonCtrlOperState")

                self.rttmonctrlopertimeoutoccurred = YLeaf(YType.boolean, "rttMonCtrlOperTimeoutOccurred")

                self.rttmonctrloperverifyerroroccurred = YLeaf(YType.boolean, "rttMonCtrlOperVerifyErrorOccurred")

                self.rttmonhistoryadminfilter = YLeaf(YType.enumeration, "rttMonHistoryAdminFilter")

                self.rttmonhistoryadminnumbuckets = YLeaf(YType.int32, "rttMonHistoryAdminNumBuckets")

                self.rttmonhistoryadminnumlives = YLeaf(YType.int32, "rttMonHistoryAdminNumLives")

                self.rttmonhistoryadminnumsamples = YLeaf(YType.int32, "rttMonHistoryAdminNumSamples")

                self.rttmonlatestrttoperaddress = YLeaf(YType.str, "rttMonLatestRttOperAddress")

                self.rttmonlatestrttoperapplspecificsense = YLeaf(YType.int32, "rttMonLatestRttOperApplSpecificSense")

                self.rttmonlatestrttopercompletiontime = YLeaf(YType.uint32, "rttMonLatestRttOperCompletionTime")

                self.rttmonlatestrttopersense = YLeaf(YType.enumeration, "rttMonLatestRttOperSense")

                self.rttmonlatestrttopersensedescription = YLeaf(YType.str, "rttMonLatestRttOperSenseDescription")

                self.rttmonlatestrttopertime = YLeaf(YType.uint32, "rttMonLatestRttOperTime")

                self.rttmonreactadminactiontype = YLeaf(YType.enumeration, "rttMonReactAdminActionType")

                self.rttmonreactadminconnectionenable = YLeaf(YType.boolean, "rttMonReactAdminConnectionEnable")

                self.rttmonreactadminthresholdcount = YLeaf(YType.int32, "rttMonReactAdminThresholdCount")

                self.rttmonreactadminthresholdcount2 = YLeaf(YType.int32, "rttMonReactAdminThresholdCount2")

                self.rttmonreactadminthresholdfalling = YLeaf(YType.int32, "rttMonReactAdminThresholdFalling")

                self.rttmonreactadminthresholdtype = YLeaf(YType.enumeration, "rttMonReactAdminThresholdType")

                self.rttmonreactadmintimeoutenable = YLeaf(YType.boolean, "rttMonReactAdminTimeoutEnable")

                self.rttmonreactadminverifyerrorenable = YLeaf(YType.boolean, "rttMonReactAdminVerifyErrorEnable")

                self.rttmonscheduleadminconceptrowageout = YLeaf(YType.int32, "rttMonScheduleAdminConceptRowAgeout")

                self.rttmonscheduleadminconceptrowageoutv2 = YLeaf(YType.int32, "rttMonScheduleAdminConceptRowAgeoutV2")

                self.rttmonscheduleadminrttlife = YLeaf(YType.int32, "rttMonScheduleAdminRttLife")

                self.rttmonscheduleadminrttrecurring = YLeaf(YType.boolean, "rttMonScheduleAdminRttRecurring")

                self.rttmonscheduleadminrttstarttime = YLeaf(YType.uint32, "rttMonScheduleAdminRttStartTime")

                self.rttmonstatisticsadmindistinterval = YLeaf(YType.int32, "rttMonStatisticsAdminDistInterval")

                self.rttmonstatisticsadminnumdistbuckets = YLeaf(YType.int32, "rttMonStatisticsAdminNumDistBuckets")

                self.rttmonstatisticsadminnumhops = YLeaf(YType.int32, "rttMonStatisticsAdminNumHops")

                self.rttmonstatisticsadminnumhourgroups = YLeaf(YType.int32, "rttMonStatisticsAdminNumHourGroups")

                self.rttmonstatisticsadminnumpaths = YLeaf(YType.int32, "rttMonStatisticsAdminNumPaths")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonctrladminfrequency",
                                "rttmonctrladmingroupname",
                                "rttmonctrladminnvgen",
                                "rttmonctrladminowner",
                                "rttmonctrladminrtttype",
                                "rttmonctrladminstatus",
                                "rttmonctrladmintag",
                                "rttmonctrladminthreshold",
                                "rttmonctrladmintimeout",
                                "rttmonctrladminverifydata",
                                "rttmonctrloperconnectionlostoccurred",
                                "rttmonctrloperdiagtext",
                                "rttmonctrlopermodificationtime",
                                "rttmonctrlopernumrtts",
                                "rttmonctrloperoctetsinuse",
                                "rttmonctrloperoverthresholdoccurred",
                                "rttmonctrloperresettime",
                                "rttmonctrloperrttlife",
                                "rttmonctrloperstate",
                                "rttmonctrlopertimeoutoccurred",
                                "rttmonctrloperverifyerroroccurred",
                                "rttmonhistoryadminfilter",
                                "rttmonhistoryadminnumbuckets",
                                "rttmonhistoryadminnumlives",
                                "rttmonhistoryadminnumsamples",
                                "rttmonlatestrttoperaddress",
                                "rttmonlatestrttoperapplspecificsense",
                                "rttmonlatestrttopercompletiontime",
                                "rttmonlatestrttopersense",
                                "rttmonlatestrttopersensedescription",
                                "rttmonlatestrttopertime",
                                "rttmonreactadminactiontype",
                                "rttmonreactadminconnectionenable",
                                "rttmonreactadminthresholdcount",
                                "rttmonreactadminthresholdcount2",
                                "rttmonreactadminthresholdfalling",
                                "rttmonreactadminthresholdtype",
                                "rttmonreactadmintimeoutenable",
                                "rttmonreactadminverifyerrorenable",
                                "rttmonscheduleadminconceptrowageout",
                                "rttmonscheduleadminconceptrowageoutv2",
                                "rttmonscheduleadminrttlife",
                                "rttmonscheduleadminrttrecurring",
                                "rttmonscheduleadminrttstarttime",
                                "rttmonstatisticsadmindistinterval",
                                "rttmonstatisticsadminnumdistbuckets",
                                "rttmonstatisticsadminnumhops",
                                "rttmonstatisticsadminnumhourgroups",
                                "rttmonstatisticsadminnumpaths") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry, self).__setattr__(name, value)

            class Rttmonctrloperstate(Enum):
                """
                Rttmonctrloperstate

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
                Rttmonhistoryadminfilter

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
                Rttmonreactadminactiontype

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
                Rttmonreactadminthresholdtype

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


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonctrladminfrequency.is_set or
                    self.rttmonctrladmingroupname.is_set or
                    self.rttmonctrladminnvgen.is_set or
                    self.rttmonctrladminowner.is_set or
                    self.rttmonctrladminrtttype.is_set or
                    self.rttmonctrladminstatus.is_set or
                    self.rttmonctrladmintag.is_set or
                    self.rttmonctrladminthreshold.is_set or
                    self.rttmonctrladmintimeout.is_set or
                    self.rttmonctrladminverifydata.is_set or
                    self.rttmonctrloperconnectionlostoccurred.is_set or
                    self.rttmonctrloperdiagtext.is_set or
                    self.rttmonctrlopermodificationtime.is_set or
                    self.rttmonctrlopernumrtts.is_set or
                    self.rttmonctrloperoctetsinuse.is_set or
                    self.rttmonctrloperoverthresholdoccurred.is_set or
                    self.rttmonctrloperresettime.is_set or
                    self.rttmonctrloperrttlife.is_set or
                    self.rttmonctrloperstate.is_set or
                    self.rttmonctrlopertimeoutoccurred.is_set or
                    self.rttmonctrloperverifyerroroccurred.is_set or
                    self.rttmonhistoryadminfilter.is_set or
                    self.rttmonhistoryadminnumbuckets.is_set or
                    self.rttmonhistoryadminnumlives.is_set or
                    self.rttmonhistoryadminnumsamples.is_set or
                    self.rttmonlatestrttoperaddress.is_set or
                    self.rttmonlatestrttoperapplspecificsense.is_set or
                    self.rttmonlatestrttopercompletiontime.is_set or
                    self.rttmonlatestrttopersense.is_set or
                    self.rttmonlatestrttopersensedescription.is_set or
                    self.rttmonlatestrttopertime.is_set or
                    self.rttmonreactadminactiontype.is_set or
                    self.rttmonreactadminconnectionenable.is_set or
                    self.rttmonreactadminthresholdcount.is_set or
                    self.rttmonreactadminthresholdcount2.is_set or
                    self.rttmonreactadminthresholdfalling.is_set or
                    self.rttmonreactadminthresholdtype.is_set or
                    self.rttmonreactadmintimeoutenable.is_set or
                    self.rttmonreactadminverifyerrorenable.is_set or
                    self.rttmonscheduleadminconceptrowageout.is_set or
                    self.rttmonscheduleadminconceptrowageoutv2.is_set or
                    self.rttmonscheduleadminrttlife.is_set or
                    self.rttmonscheduleadminrttrecurring.is_set or
                    self.rttmonscheduleadminrttstarttime.is_set or
                    self.rttmonstatisticsadmindistinterval.is_set or
                    self.rttmonstatisticsadminnumdistbuckets.is_set or
                    self.rttmonstatisticsadminnumhops.is_set or
                    self.rttmonstatisticsadminnumhourgroups.is_set or
                    self.rttmonstatisticsadminnumpaths.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonctrladminfrequency.yfilter != YFilter.not_set or
                    self.rttmonctrladmingroupname.yfilter != YFilter.not_set or
                    self.rttmonctrladminnvgen.yfilter != YFilter.not_set or
                    self.rttmonctrladminowner.yfilter != YFilter.not_set or
                    self.rttmonctrladminrtttype.yfilter != YFilter.not_set or
                    self.rttmonctrladminstatus.yfilter != YFilter.not_set or
                    self.rttmonctrladmintag.yfilter != YFilter.not_set or
                    self.rttmonctrladminthreshold.yfilter != YFilter.not_set or
                    self.rttmonctrladmintimeout.yfilter != YFilter.not_set or
                    self.rttmonctrladminverifydata.yfilter != YFilter.not_set or
                    self.rttmonctrloperconnectionlostoccurred.yfilter != YFilter.not_set or
                    self.rttmonctrloperdiagtext.yfilter != YFilter.not_set or
                    self.rttmonctrlopermodificationtime.yfilter != YFilter.not_set or
                    self.rttmonctrlopernumrtts.yfilter != YFilter.not_set or
                    self.rttmonctrloperoctetsinuse.yfilter != YFilter.not_set or
                    self.rttmonctrloperoverthresholdoccurred.yfilter != YFilter.not_set or
                    self.rttmonctrloperresettime.yfilter != YFilter.not_set or
                    self.rttmonctrloperrttlife.yfilter != YFilter.not_set or
                    self.rttmonctrloperstate.yfilter != YFilter.not_set or
                    self.rttmonctrlopertimeoutoccurred.yfilter != YFilter.not_set or
                    self.rttmonctrloperverifyerroroccurred.yfilter != YFilter.not_set or
                    self.rttmonhistoryadminfilter.yfilter != YFilter.not_set or
                    self.rttmonhistoryadminnumbuckets.yfilter != YFilter.not_set or
                    self.rttmonhistoryadminnumlives.yfilter != YFilter.not_set or
                    self.rttmonhistoryadminnumsamples.yfilter != YFilter.not_set or
                    self.rttmonlatestrttoperaddress.yfilter != YFilter.not_set or
                    self.rttmonlatestrttoperapplspecificsense.yfilter != YFilter.not_set or
                    self.rttmonlatestrttopercompletiontime.yfilter != YFilter.not_set or
                    self.rttmonlatestrttopersense.yfilter != YFilter.not_set or
                    self.rttmonlatestrttopersensedescription.yfilter != YFilter.not_set or
                    self.rttmonlatestrttopertime.yfilter != YFilter.not_set or
                    self.rttmonreactadminactiontype.yfilter != YFilter.not_set or
                    self.rttmonreactadminconnectionenable.yfilter != YFilter.not_set or
                    self.rttmonreactadminthresholdcount.yfilter != YFilter.not_set or
                    self.rttmonreactadminthresholdcount2.yfilter != YFilter.not_set or
                    self.rttmonreactadminthresholdfalling.yfilter != YFilter.not_set or
                    self.rttmonreactadminthresholdtype.yfilter != YFilter.not_set or
                    self.rttmonreactadmintimeoutenable.yfilter != YFilter.not_set or
                    self.rttmonreactadminverifyerrorenable.yfilter != YFilter.not_set or
                    self.rttmonscheduleadminconceptrowageout.yfilter != YFilter.not_set or
                    self.rttmonscheduleadminconceptrowageoutv2.yfilter != YFilter.not_set or
                    self.rttmonscheduleadminrttlife.yfilter != YFilter.not_set or
                    self.rttmonscheduleadminrttrecurring.yfilter != YFilter.not_set or
                    self.rttmonscheduleadminrttstarttime.yfilter != YFilter.not_set or
                    self.rttmonstatisticsadmindistinterval.yfilter != YFilter.not_set or
                    self.rttmonstatisticsadminnumdistbuckets.yfilter != YFilter.not_set or
                    self.rttmonstatisticsadminnumhops.yfilter != YFilter.not_set or
                    self.rttmonstatisticsadminnumhourgroups.yfilter != YFilter.not_set or
                    self.rttmonstatisticsadminnumpaths.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonCtrlAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonCtrlAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonctrladminfrequency.is_set or self.rttmonctrladminfrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminfrequency.get_name_leafdata())
                if (self.rttmonctrladmingroupname.is_set or self.rttmonctrladmingroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladmingroupname.get_name_leafdata())
                if (self.rttmonctrladminnvgen.is_set or self.rttmonctrladminnvgen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminnvgen.get_name_leafdata())
                if (self.rttmonctrladminowner.is_set or self.rttmonctrladminowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminowner.get_name_leafdata())
                if (self.rttmonctrladminrtttype.is_set or self.rttmonctrladminrtttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminrtttype.get_name_leafdata())
                if (self.rttmonctrladminstatus.is_set or self.rttmonctrladminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminstatus.get_name_leafdata())
                if (self.rttmonctrladmintag.is_set or self.rttmonctrladmintag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladmintag.get_name_leafdata())
                if (self.rttmonctrladminthreshold.is_set or self.rttmonctrladminthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminthreshold.get_name_leafdata())
                if (self.rttmonctrladmintimeout.is_set or self.rttmonctrladmintimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladmintimeout.get_name_leafdata())
                if (self.rttmonctrladminverifydata.is_set or self.rttmonctrladminverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminverifydata.get_name_leafdata())
                if (self.rttmonctrloperconnectionlostoccurred.is_set or self.rttmonctrloperconnectionlostoccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperconnectionlostoccurred.get_name_leafdata())
                if (self.rttmonctrloperdiagtext.is_set or self.rttmonctrloperdiagtext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperdiagtext.get_name_leafdata())
                if (self.rttmonctrlopermodificationtime.is_set or self.rttmonctrlopermodificationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrlopermodificationtime.get_name_leafdata())
                if (self.rttmonctrlopernumrtts.is_set or self.rttmonctrlopernumrtts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrlopernumrtts.get_name_leafdata())
                if (self.rttmonctrloperoctetsinuse.is_set or self.rttmonctrloperoctetsinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperoctetsinuse.get_name_leafdata())
                if (self.rttmonctrloperoverthresholdoccurred.is_set or self.rttmonctrloperoverthresholdoccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperoverthresholdoccurred.get_name_leafdata())
                if (self.rttmonctrloperresettime.is_set or self.rttmonctrloperresettime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperresettime.get_name_leafdata())
                if (self.rttmonctrloperrttlife.is_set or self.rttmonctrloperrttlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperrttlife.get_name_leafdata())
                if (self.rttmonctrloperstate.is_set or self.rttmonctrloperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperstate.get_name_leafdata())
                if (self.rttmonctrlopertimeoutoccurred.is_set or self.rttmonctrlopertimeoutoccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrlopertimeoutoccurred.get_name_leafdata())
                if (self.rttmonctrloperverifyerroroccurred.is_set or self.rttmonctrloperverifyerroroccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrloperverifyerroroccurred.get_name_leafdata())
                if (self.rttmonhistoryadminfilter.is_set or self.rttmonhistoryadminfilter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistoryadminfilter.get_name_leafdata())
                if (self.rttmonhistoryadminnumbuckets.is_set or self.rttmonhistoryadminnumbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistoryadminnumbuckets.get_name_leafdata())
                if (self.rttmonhistoryadminnumlives.is_set or self.rttmonhistoryadminnumlives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistoryadminnumlives.get_name_leafdata())
                if (self.rttmonhistoryadminnumsamples.is_set or self.rttmonhistoryadminnumsamples.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistoryadminnumsamples.get_name_leafdata())
                if (self.rttmonlatestrttoperaddress.is_set or self.rttmonlatestrttoperaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttoperaddress.get_name_leafdata())
                if (self.rttmonlatestrttoperapplspecificsense.is_set or self.rttmonlatestrttoperapplspecificsense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttoperapplspecificsense.get_name_leafdata())
                if (self.rttmonlatestrttopercompletiontime.is_set or self.rttmonlatestrttopercompletiontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttopercompletiontime.get_name_leafdata())
                if (self.rttmonlatestrttopersense.is_set or self.rttmonlatestrttopersense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttopersense.get_name_leafdata())
                if (self.rttmonlatestrttopersensedescription.is_set or self.rttmonlatestrttopersensedescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttopersensedescription.get_name_leafdata())
                if (self.rttmonlatestrttopertime.is_set or self.rttmonlatestrttopertime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestrttopertime.get_name_leafdata())
                if (self.rttmonreactadminactiontype.is_set or self.rttmonreactadminactiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminactiontype.get_name_leafdata())
                if (self.rttmonreactadminconnectionenable.is_set or self.rttmonreactadminconnectionenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminconnectionenable.get_name_leafdata())
                if (self.rttmonreactadminthresholdcount.is_set or self.rttmonreactadminthresholdcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminthresholdcount.get_name_leafdata())
                if (self.rttmonreactadminthresholdcount2.is_set or self.rttmonreactadminthresholdcount2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminthresholdcount2.get_name_leafdata())
                if (self.rttmonreactadminthresholdfalling.is_set or self.rttmonreactadminthresholdfalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminthresholdfalling.get_name_leafdata())
                if (self.rttmonreactadminthresholdtype.is_set or self.rttmonreactadminthresholdtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminthresholdtype.get_name_leafdata())
                if (self.rttmonreactadmintimeoutenable.is_set or self.rttmonreactadmintimeoutenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadmintimeoutenable.get_name_leafdata())
                if (self.rttmonreactadminverifyerrorenable.is_set or self.rttmonreactadminverifyerrorenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactadminverifyerrorenable.get_name_leafdata())
                if (self.rttmonscheduleadminconceptrowageout.is_set or self.rttmonscheduleadminconceptrowageout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscheduleadminconceptrowageout.get_name_leafdata())
                if (self.rttmonscheduleadminconceptrowageoutv2.is_set or self.rttmonscheduleadminconceptrowageoutv2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscheduleadminconceptrowageoutv2.get_name_leafdata())
                if (self.rttmonscheduleadminrttlife.is_set or self.rttmonscheduleadminrttlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscheduleadminrttlife.get_name_leafdata())
                if (self.rttmonscheduleadminrttrecurring.is_set or self.rttmonscheduleadminrttrecurring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscheduleadminrttrecurring.get_name_leafdata())
                if (self.rttmonscheduleadminrttstarttime.is_set or self.rttmonscheduleadminrttstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscheduleadminrttstarttime.get_name_leafdata())
                if (self.rttmonstatisticsadmindistinterval.is_set or self.rttmonstatisticsadmindistinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatisticsadmindistinterval.get_name_leafdata())
                if (self.rttmonstatisticsadminnumdistbuckets.is_set or self.rttmonstatisticsadminnumdistbuckets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatisticsadminnumdistbuckets.get_name_leafdata())
                if (self.rttmonstatisticsadminnumhops.is_set or self.rttmonstatisticsadminnumhops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatisticsadminnumhops.get_name_leafdata())
                if (self.rttmonstatisticsadminnumhourgroups.is_set or self.rttmonstatisticsadminnumhourgroups.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatisticsadminnumhourgroups.get_name_leafdata())
                if (self.rttmonstatisticsadminnumpaths.is_set or self.rttmonstatisticsadminnumpaths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatisticsadminnumpaths.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonCtrlAdminFrequency" or name == "rttMonCtrlAdminGroupName" or name == "rttMonCtrlAdminNvgen" or name == "rttMonCtrlAdminOwner" or name == "rttMonCtrlAdminRttType" or name == "rttMonCtrlAdminStatus" or name == "rttMonCtrlAdminTag" or name == "rttMonCtrlAdminThreshold" or name == "rttMonCtrlAdminTimeout" or name == "rttMonCtrlAdminVerifyData" or name == "rttMonCtrlOperConnectionLostOccurred" or name == "rttMonCtrlOperDiagText" or name == "rttMonCtrlOperModificationTime" or name == "rttMonCtrlOperNumRtts" or name == "rttMonCtrlOperOctetsInUse" or name == "rttMonCtrlOperOverThresholdOccurred" or name == "rttMonCtrlOperResetTime" or name == "rttMonCtrlOperRttLife" or name == "rttMonCtrlOperState" or name == "rttMonCtrlOperTimeoutOccurred" or name == "rttMonCtrlOperVerifyErrorOccurred" or name == "rttMonHistoryAdminFilter" or name == "rttMonHistoryAdminNumBuckets" or name == "rttMonHistoryAdminNumLives" or name == "rttMonHistoryAdminNumSamples" or name == "rttMonLatestRttOperAddress" or name == "rttMonLatestRttOperApplSpecificSense" or name == "rttMonLatestRttOperCompletionTime" or name == "rttMonLatestRttOperSense" or name == "rttMonLatestRttOperSenseDescription" or name == "rttMonLatestRttOperTime" or name == "rttMonReactAdminActionType" or name == "rttMonReactAdminConnectionEnable" or name == "rttMonReactAdminThresholdCount" or name == "rttMonReactAdminThresholdCount2" or name == "rttMonReactAdminThresholdFalling" or name == "rttMonReactAdminThresholdType" or name == "rttMonReactAdminTimeoutEnable" or name == "rttMonReactAdminVerifyErrorEnable" or name == "rttMonScheduleAdminConceptRowAgeout" or name == "rttMonScheduleAdminConceptRowAgeoutV2" or name == "rttMonScheduleAdminRttLife" or name == "rttMonScheduleAdminRttRecurring" or name == "rttMonScheduleAdminRttStartTime" or name == "rttMonStatisticsAdminDistInterval" or name == "rttMonStatisticsAdminNumDistBuckets" or name == "rttMonStatisticsAdminNumHops" or name == "rttMonStatisticsAdminNumHourGroups" or name == "rttMonStatisticsAdminNumPaths"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminFrequency"):
                    self.rttmonctrladminfrequency = value
                    self.rttmonctrladminfrequency.value_namespace = name_space
                    self.rttmonctrladminfrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminGroupName"):
                    self.rttmonctrladmingroupname = value
                    self.rttmonctrladmingroupname.value_namespace = name_space
                    self.rttmonctrladmingroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminNvgen"):
                    self.rttmonctrladminnvgen = value
                    self.rttmonctrladminnvgen.value_namespace = name_space
                    self.rttmonctrladminnvgen.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminOwner"):
                    self.rttmonctrladminowner = value
                    self.rttmonctrladminowner.value_namespace = name_space
                    self.rttmonctrladminowner.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminRttType"):
                    self.rttmonctrladminrtttype = value
                    self.rttmonctrladminrtttype.value_namespace = name_space
                    self.rttmonctrladminrtttype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminStatus"):
                    self.rttmonctrladminstatus = value
                    self.rttmonctrladminstatus.value_namespace = name_space
                    self.rttmonctrladminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminTag"):
                    self.rttmonctrladmintag = value
                    self.rttmonctrladmintag.value_namespace = name_space
                    self.rttmonctrladmintag.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminThreshold"):
                    self.rttmonctrladminthreshold = value
                    self.rttmonctrladminthreshold.value_namespace = name_space
                    self.rttmonctrladminthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminTimeout"):
                    self.rttmonctrladmintimeout = value
                    self.rttmonctrladmintimeout.value_namespace = name_space
                    self.rttmonctrladmintimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlAdminVerifyData"):
                    self.rttmonctrladminverifydata = value
                    self.rttmonctrladminverifydata.value_namespace = name_space
                    self.rttmonctrladminverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperConnectionLostOccurred"):
                    self.rttmonctrloperconnectionlostoccurred = value
                    self.rttmonctrloperconnectionlostoccurred.value_namespace = name_space
                    self.rttmonctrloperconnectionlostoccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperDiagText"):
                    self.rttmonctrloperdiagtext = value
                    self.rttmonctrloperdiagtext.value_namespace = name_space
                    self.rttmonctrloperdiagtext.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperModificationTime"):
                    self.rttmonctrlopermodificationtime = value
                    self.rttmonctrlopermodificationtime.value_namespace = name_space
                    self.rttmonctrlopermodificationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperNumRtts"):
                    self.rttmonctrlopernumrtts = value
                    self.rttmonctrlopernumrtts.value_namespace = name_space
                    self.rttmonctrlopernumrtts.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperOctetsInUse"):
                    self.rttmonctrloperoctetsinuse = value
                    self.rttmonctrloperoctetsinuse.value_namespace = name_space
                    self.rttmonctrloperoctetsinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperOverThresholdOccurred"):
                    self.rttmonctrloperoverthresholdoccurred = value
                    self.rttmonctrloperoverthresholdoccurred.value_namespace = name_space
                    self.rttmonctrloperoverthresholdoccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperResetTime"):
                    self.rttmonctrloperresettime = value
                    self.rttmonctrloperresettime.value_namespace = name_space
                    self.rttmonctrloperresettime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperRttLife"):
                    self.rttmonctrloperrttlife = value
                    self.rttmonctrloperrttlife.value_namespace = name_space
                    self.rttmonctrloperrttlife.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperState"):
                    self.rttmonctrloperstate = value
                    self.rttmonctrloperstate.value_namespace = name_space
                    self.rttmonctrloperstate.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperTimeoutOccurred"):
                    self.rttmonctrlopertimeoutoccurred = value
                    self.rttmonctrlopertimeoutoccurred.value_namespace = name_space
                    self.rttmonctrlopertimeoutoccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonCtrlOperVerifyErrorOccurred"):
                    self.rttmonctrloperverifyerroroccurred = value
                    self.rttmonctrloperverifyerroroccurred.value_namespace = name_space
                    self.rttmonctrloperverifyerroroccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryAdminFilter"):
                    self.rttmonhistoryadminfilter = value
                    self.rttmonhistoryadminfilter.value_namespace = name_space
                    self.rttmonhistoryadminfilter.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryAdminNumBuckets"):
                    self.rttmonhistoryadminnumbuckets = value
                    self.rttmonhistoryadminnumbuckets.value_namespace = name_space
                    self.rttmonhistoryadminnumbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryAdminNumLives"):
                    self.rttmonhistoryadminnumlives = value
                    self.rttmonhistoryadminnumlives.value_namespace = name_space
                    self.rttmonhistoryadminnumlives.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryAdminNumSamples"):
                    self.rttmonhistoryadminnumsamples = value
                    self.rttmonhistoryadminnumsamples.value_namespace = name_space
                    self.rttmonhistoryadminnumsamples.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperAddress"):
                    self.rttmonlatestrttoperaddress = value
                    self.rttmonlatestrttoperaddress.value_namespace = name_space
                    self.rttmonlatestrttoperaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperApplSpecificSense"):
                    self.rttmonlatestrttoperapplspecificsense = value
                    self.rttmonlatestrttoperapplspecificsense.value_namespace = name_space
                    self.rttmonlatestrttoperapplspecificsense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperCompletionTime"):
                    self.rttmonlatestrttopercompletiontime = value
                    self.rttmonlatestrttopercompletiontime.value_namespace = name_space
                    self.rttmonlatestrttopercompletiontime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperSense"):
                    self.rttmonlatestrttopersense = value
                    self.rttmonlatestrttopersense.value_namespace = name_space
                    self.rttmonlatestrttopersense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperSenseDescription"):
                    self.rttmonlatestrttopersensedescription = value
                    self.rttmonlatestrttopersensedescription.value_namespace = name_space
                    self.rttmonlatestrttopersensedescription.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestRttOperTime"):
                    self.rttmonlatestrttopertime = value
                    self.rttmonlatestrttopertime.value_namespace = name_space
                    self.rttmonlatestrttopertime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminActionType"):
                    self.rttmonreactadminactiontype = value
                    self.rttmonreactadminactiontype.value_namespace = name_space
                    self.rttmonreactadminactiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminConnectionEnable"):
                    self.rttmonreactadminconnectionenable = value
                    self.rttmonreactadminconnectionenable.value_namespace = name_space
                    self.rttmonreactadminconnectionenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminThresholdCount"):
                    self.rttmonreactadminthresholdcount = value
                    self.rttmonreactadminthresholdcount.value_namespace = name_space
                    self.rttmonreactadminthresholdcount.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminThresholdCount2"):
                    self.rttmonreactadminthresholdcount2 = value
                    self.rttmonreactadminthresholdcount2.value_namespace = name_space
                    self.rttmonreactadminthresholdcount2.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminThresholdFalling"):
                    self.rttmonreactadminthresholdfalling = value
                    self.rttmonreactadminthresholdfalling.value_namespace = name_space
                    self.rttmonreactadminthresholdfalling.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminThresholdType"):
                    self.rttmonreactadminthresholdtype = value
                    self.rttmonreactadminthresholdtype.value_namespace = name_space
                    self.rttmonreactadminthresholdtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminTimeoutEnable"):
                    self.rttmonreactadmintimeoutenable = value
                    self.rttmonreactadmintimeoutenable.value_namespace = name_space
                    self.rttmonreactadmintimeoutenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactAdminVerifyErrorEnable"):
                    self.rttmonreactadminverifyerrorenable = value
                    self.rttmonreactadminverifyerrorenable.value_namespace = name_space
                    self.rttmonreactadminverifyerrorenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScheduleAdminConceptRowAgeout"):
                    self.rttmonscheduleadminconceptrowageout = value
                    self.rttmonscheduleadminconceptrowageout.value_namespace = name_space
                    self.rttmonscheduleadminconceptrowageout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScheduleAdminConceptRowAgeoutV2"):
                    self.rttmonscheduleadminconceptrowageoutv2 = value
                    self.rttmonscheduleadminconceptrowageoutv2.value_namespace = name_space
                    self.rttmonscheduleadminconceptrowageoutv2.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScheduleAdminRttLife"):
                    self.rttmonscheduleadminrttlife = value
                    self.rttmonscheduleadminrttlife.value_namespace = name_space
                    self.rttmonscheduleadminrttlife.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScheduleAdminRttRecurring"):
                    self.rttmonscheduleadminrttrecurring = value
                    self.rttmonscheduleadminrttrecurring.value_namespace = name_space
                    self.rttmonscheduleadminrttrecurring.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScheduleAdminRttStartTime"):
                    self.rttmonscheduleadminrttstarttime = value
                    self.rttmonscheduleadminrttstarttime.value_namespace = name_space
                    self.rttmonscheduleadminrttstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatisticsAdminDistInterval"):
                    self.rttmonstatisticsadmindistinterval = value
                    self.rttmonstatisticsadmindistinterval.value_namespace = name_space
                    self.rttmonstatisticsadmindistinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatisticsAdminNumDistBuckets"):
                    self.rttmonstatisticsadminnumdistbuckets = value
                    self.rttmonstatisticsadminnumdistbuckets.value_namespace = name_space
                    self.rttmonstatisticsadminnumdistbuckets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatisticsAdminNumHops"):
                    self.rttmonstatisticsadminnumhops = value
                    self.rttmonstatisticsadminnumhops.value_namespace = name_space
                    self.rttmonstatisticsadminnumhops.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatisticsAdminNumHourGroups"):
                    self.rttmonstatisticsadminnumhourgroups = value
                    self.rttmonstatisticsadminnumhourgroups.value_namespace = name_space
                    self.rttmonstatisticsadminnumhourgroups.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatisticsAdminNumPaths"):
                    self.rttmonstatisticsadminnumpaths = value
                    self.rttmonstatisticsadminnumpaths.value_namespace = name_space
                    self.rttmonstatisticsadminnumpaths.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonctrladminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonctrladminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonCtrlAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonCtrlAdminEntry"):
                for c in self.rttmonctrladminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonctrladminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonCtrlAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonechoadmintable(Entity):
        """
        A table that contains Round Trip Time (RTT) specific
        definitions.
        
        This table is controlled via the 
        rttMonCtrlAdminTable.  Entries in this table are
        created via the rttMonCtrlAdminStatus object.
        
        .. attribute:: rttmonechoadminentry
        
        	A list of objects that define specific configuration for RttMonRttType conceptual Rtt control rows
        	**type**\: list of    :py:class:`Rttmonechoadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonechoadmintable, self).__init__()

            self.yang_name = "rttMonEchoAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonechoadminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonechoadmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonechoadmintable, self).__setattr__(name, value)


        class Rttmonechoadminentry(Entity):
            """
            A list of objects that define specific configuration for
            RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonechoadminaggburstcycles
            
            	This object indicates the number of burst cycles to be sent during the aggregate interval. This value is currently used for Y1731 SLM(Synthetic Loss Measurment) probe. This object is applicable to Y1731 SLM probe only
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminavailnumframes
            
            	This object indicates the number of frames over which to calculate the availability. This object is applicable to Y1731 SLM probe only
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadmincache
            
            	If this object is false then it means that HTTP request should not download cached pages. This means that the request should  be forwarded to the origin server. This object is applicable to http probe only
            	**type**\:  bool
            
            .. attribute:: rttmonechoadmincallduration
            
            	Duration of RTP/Video Probe session. This object is applicable to RTP and Video probe
            	**type**\:  int
            
            	**range:** 1..600
            
            .. attribute:: rttmonechoadmincallednumber
            
            	This string stores the called number of post dial delay. This object is applicable to voip post dial delay probe only. The number will be like the one actualy the user could dial. It has the number required by the local country dial plan, plus E.164 number. The maximum length is 24 digits. Only digit (0\-9) is allowed
            	**type**\:  str
            
            	**length:** 0..24
            
            .. attribute:: rttmonechoadmincodecinterval
            
            	This field represents the inter\-packet delay between packets and is in milliseconds. This object is applicable only to jitter probe which uses codec type
            	**type**\:  int
            
            	**range:** 0..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadmincodecnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is used only for jitter probe which uses codec type
            	**type**\:  int
            
            	**range:** 0..60000
            
            .. attribute:: rttmonechoadmincodecpayload
            
            	This object represents the number of octets that needs to be placed into the Data portion of the message. This value is used only for jitter probe which uses codec type
            	**type**\:  int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadmincodectype
            
            	Specifies the codec type to be used with jitter probe. This is applicable only for the jitter probe.  If codec\-type is configured the following parameters cannot be  configured. rttMonEchoAdminPktDataRequestSize rttMonEchoAdminInterval rttMonEchoAdminNumPackets
            	**type**\:   :py:class:`Rttmoncodectype <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmoncodectype>`
            
            .. attribute:: rttmonechoadmincontrolenable
            
            	If this object is enabled, then the RTR application will send control messages to a responder, residing on the  target router to respond to the data request packets being  sent by the source router. This object is not applicable to  echo, pathEcho, dns and http probes
            	**type**\:  bool
            
            .. attribute:: rttmonechoadmincontrolretry
            
            	This object specifies the maximum number of retries for control message
            	**type**\:  int
            
            	**range:** 1..5
            
            .. attribute:: rttmonechoadmincontroltimeout
            
            	This object specifies the wait duration before control message timeout
            	**type**\:  int
            
            	**range:** 1..10000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadmindetectpoint
            
            	A code that represents the detect point of post dial delay. This object is applicable to SAA post dial delay probe only
            	**type**\:   :py:class:`Rttmonoperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonoperation>`
            
            .. attribute:: rttmonechoadmindscp
            
            	This object represents the Differentiated Service Code Point (DSCP) QoS marking in the generated synthetic packets.  Value \- DiffServ Class     0 \- BE (default)    10 \- AF11    12 \- AF12    14 \- AF13    18 \- AF21    20 \- AF22    22 \- AF23    26 \- AF31    28 \- AF32    30 \- AF33    34 \- AF41    36 \- AF42    38 \- AF43     8 \- CS1    16 \- CS2    24 \- CS3    32 \- CS4    40 \- CS5    48 \- CS6    56 \- CS7    46 \- EF
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: rttmonechoadminemulatesourceaddress
            
            	This object specifies the IP address of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source IP address will by default be the same as rttMonEchoAdminSourceAddress. This object is applicable to video probes
            	**type**\:  str
            
            .. attribute:: rttmonechoadminemulatesourceport
            
            	This object represents the port number of the emulated source from which the synthetic packets would be generated. If this object is not specified, the emulated source port number will by default be the same as rttMonEchoAdminSourcePort. This object is applicable to video probes
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadminemulatetargetaddress
            
            	This object specifies the IP address of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target IP address will by default be the same as rttMonEchoAdminTargetAddress. This object is applicable to video probes
            	**type**\:  str
            
            .. attribute:: rttmonechoadminemulatetargetport
            
            	This object represents the port number of the emulated target by which the synthetic packets would be received. If this object is not specified, the emulated target port number will by default be the same as rttMonEchoAdminTargetPort. This object is applicable to video probes
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadminenableburst
            
            	This object indicates that packets will be sent in burst
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminendpointlistname
            
            	This object specifies the name of endpoint list which a probe uses to generate operations
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: rttmonechoadminethernetcos
            
            	This object specifies the class of service in an Ethernet packet header. It is only applicable to ethernetPing and  ethernetJitter operation
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: rttmonechoadmingkregistration
            
            	A boolean that represents VoIP GK registration delay. This object is applicable to SAA GK registration delay  probe only
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminhttpversion
            
            	A string which specifies the version number of the HTTP Server.  The syntax for the version string is  <major number>.<minor number> An example would be 1.0,  1.1 etc.,.  This object is applicable to http probe only
            	**type**\:  str
            
            	**length:** 3..10
            
            .. attribute:: rttmonechoadminicpifadvfactor
            
            	The advantage factor is dependant on the type of access and how the service is to be used. Conventional Wire\-line     0 Mobility within Building    5 Mobility within geographic area  10 Access to hard\-to\-reach location   20  This will be used while calculating the ICPIF values This valid only for Jitter while calculating the ICPIF value
            	**type**\:  int
            
            	**range:** 0..20
            
            .. attribute:: rttmonechoadminigmptreeinit
            
            	This object specifies number of packets to be sent for multicast tree setup. This object is applicable to multicast probe only
            	**type**\:  int
            
            	**range:** 0..10
            
            .. attribute:: rttmonechoadmininputinterface
            
            	This object represents the network input interface on the sender router where the synthetic packets are received from the emulated endpoint source. This is used for path congruence with correct feature processing at the sender router.  The user can get the InterfaceIndex number from ifIndex object by looking up in ifTable. In fact, it should be useful to first get the entry by the augmented table ifXTable which has ifName object which matches the interface name used on the router or switch equipment console
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonechoadmininterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for  Jitter probe. This object is applicable to jitter probe only
            	**type**\:  int
            
            	**range:** 0..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonechoadminlossrationumframes
            
            	This object indicates the number of frames over which to calculate the frame loss ratio. This object is applicable  to Y1731 SLM probe only
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminlspexp
            
            	This object represents the EXP value that needs to be put as precedence bit in the MPLS echo request IP header
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: rttmonechoadminlspfectype
            
            	The type of the target FEC for the RTT 'echo' and 'pathEcho' operations based on 'mplsLspPingAppl' RttMonProtocol.  ldpIpv4Prefix   \- LDP IPv4 prefix
            	**type**\:   :py:class:`Rttmonechoadminlspfectype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminlspfectype>`
            
            .. attribute:: rttmonechoadminlspnullshim
            
            	This object specifies if the explicit\-null label is to be added to LSP echo requests which are sent while performing RTT operation
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminlspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\:  int
            
            	**range:** 0..63 \| 255..None
            
            .. attribute:: rttmonechoadminlspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests
            	**type**\:   :py:class:`Rttmonlsppingreplymode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonlsppingreplymode>`
            
            .. attribute:: rttmonechoadminlspselector
            
            	A string which specifies a valid 127/8 address. This address is of the form 127.x.y.z. This address is not used to route the MPLS echo packet to the destination but is used for load balancing in cases where the IP payload's destination address is used for load balancing
            	**type**\:  str
            
            .. attribute:: rttmonechoadminlspttl
            
            	This object represents the TTL setting for MPLS echo request packets. For ping operation this represents the TTL value to be set in the echo request packet. For trace operation it represent the maximum ttl value that can be set in the echo request packets starting with TTL=1.  For 'echo' based on mplsLspPingAppl the default TTL will be set to 255, and for 'pathEcho' based on mplsLspPingAppl the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values to be used for 'echo' and 'pathEcho' based on 'mplsLspPingAppl'
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rttmonechoadminlspvccvid
            
            	This object specifies MPLS LSP pseudowire VCCV ID values between 1 to 2147483647.  Note\: This object cannot be set to value of 0. This default value specifies that VCCV is not set for this row
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonechoadminlsrenable
            
            	If this object is enabled then it means that the application calculates response time for a specific path, defined in rttMonEchoPathAdminEntry. This object is applicable to echo  probe only
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminmode
            
            	A code that represents the specific type of RTT operation. This object is applicable to ftp probe only
            	**type**\:   :py:class:`Rttmonoperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonoperation>`
            
            .. attribute:: rttmonechoadminnameserver
            
            	A string which specifies the ip address of the name\-server. This object is applicable to dns probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminnumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe.  This object is applicable to jitter probe only
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rttmonechoadminoperation
            
            	A code that represents the specific type of RTT operation. This object is applicable to http and ftp probe only
            	**type**\:   :py:class:`Rttmonoperation <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonoperation>`
            
            .. attribute:: rttmonechoadminowntpsynctolabs
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of NTP offsets on source and responder. The value specified is  microseconds. This value can be set only for jitter operation  with precision of microsecond
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rttmonechoadminowntpsynctolpct
            
            	This object specifies the total clock synchronization error on source and responder that is considered acceptable for  oneway measurement when NTP is used as clock synchronization  mechanism.  The total clock synchronization error is sum of  NTP offsets on source and responder. The value is expressed  as the percentage of actual oneway latency that is measured.  This value can be set only for jitter operation with precision  of microsecond
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: rttmonechoadminowntpsynctoltype
            
            	This object specifies whether the value in specified for oneway NTP sync tolerance is absolute value or percent value
            	**type**\:   :py:class:`Rttmonechoadminowntpsynctoltype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminowntpsynctoltype>`
            
            .. attribute:: rttmonechoadminpktdatarequestsize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the request  message, when using SNA protocols.  For non\-ARR protocols' RTT request/responses,  this value represents the native payload size.  REMEMBER\:  The ARR Header overhead is not included             in this value.  For echo probes the total packet size = (IP header(20) +  ICMP header(8) + 8 (internal timestamps) + request size).  For echo and pathEcho default request size is 28. For udp probe, default request size is 16 and for jitter  probe it is 32. For dlsw probes default request size is 0.  The minimum request size for echo and pathEcho is 28 bytes, for udp it is 4 and for jitter it is 16. For udp and jitter probes the maximum request size is 1500.  For ethernetPing the default request size is 66. For ethernetJitter the default request size is 51
            	**type**\:  int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmonechoadminpktdataresponsesize
            
            	This object represents the number of octets to be placed into the ARR Data portion of the response message. This value is passed to the RTT Echo Server via a field in the ARR Header.  For non\-ARR RTT request/response (i.e. ipIcmpecho) this value will be set by the agent to match the size of rttMonEchoAdminPktDataRequestSize, when native payloads are supported.  REMEMBER\:  The ARR Header overhead is not included             in this value.  This object is only supported by SNA protocols
            	**type**\:  int
            
            	**range:** 0..16384
            
            .. attribute:: rttmonechoadminprecision
            
            	This object specifies the accuracy of statistics that needs to be calculated milliseconds \- The accuracy of stats will be of milliseconds microseconds \- The accuracy of stats will be in microseconds. This value can be set only for jitter operation
            	**type**\:   :py:class:`Rttmonechoadminprecision <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminprecision>`
            
            .. attribute:: rttmonechoadminprobepakpriority
            
            	This object specifies the priority that will be assigned to probe packet.  This value can be set only for jitter  operation
            	**type**\:   :py:class:`Rttmonechoadminprobepakpriority <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminprobepakpriority>`
            
            .. attribute:: rttmonechoadminprotocol
            
            	Specifies the protocol to be used to perform the RTT operation. The following list defines what protocol  should be used for each probe type\:  echo, pathEcho   \- ipIcmpEcho / mplsLspPingAppl udpEcho          \- ipUdpEchoAppl tcpConnect       \- ipTcpConn http             \- httpAppl jitter           \- jitterAppl dlsw             \- dlswAppl dhcp             \- dhcpAppl ftp              \- ftpAppl mplsLspPing      \- mplsLspPingAppl voip             \- voipAppl video            \- videoAppl  When this protocol does not support the type, a 'badValue' error will be returned
            	**type**\:   :py:class:`Rttmonprotocol <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonprotocol>`
            
            .. attribute:: rttmonechoadminproxy
            
            	This string represents the proxy server information. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminreservedsp
            
            	This object represents the video traffic generation source.  be \: best effort using DSP but without reservation gs \: guaranteed service using DSP with reservation na \: not applicable for not using DSP
            	**type**\:   :py:class:`Rttmonechoadminreservedsp <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry.Rttmonechoadminreservedsp>`
            
            .. attribute:: rttmonechoadminsourceaddress
            
            	A string which specifies the IP address of the source. This object is applicable to all probes except dns, dlsw  and sna
            	**type**\:  str
            
            .. attribute:: rttmonechoadminsourcemacaddress
            
            	This object indicates the MAC address of the source device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminSourceMacAddress and rttMonEchoAdminSourceMPID may not be used in conjunction
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: rttmonechoadminsourcempid
            
            	This object indicates the source maintenance point ID.  It is only applicable to Y.1731 operation.  It will be set to zero for other types of opearations.  rttMonEchoAdminSourceMPID and rttMonEchoAdminSourceMacAddress may not be used in conjunction
            	**type**\:  int
            
            	**range:** 0..8191
            
            .. attribute:: rttmonechoadminsourceport
            
            	This object represents the source's port number. If this object is not specified, the application will get a  port allocated by the system. This object is applicable  to all probes except dns, dlsw and sna
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadminsourcevoiceport
            
            	A string which specifies the voice\-port on the source gateway. This object is applicable to RTP probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminssm
            
            	This object specifies if Source Specific Multicast is to be added. This object is applicable to multicast probe only
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminstring1
            
            	This string stores the content of HTTP raw request. If the request cannot fit into String1 then it should  be split and put in Strings 1 through 5.  This string stores the content of the DHCP raw option data.  The raw DHCP option data must be in HEX. If an odd number of characters are specified, a 0 will be appended to the end of the string.  Only DHCP option 82 (decimal) is allowed. Here is an example of a valid string\: 5208010610005A6F1234 Only rttMonEchoAdminString1 is used for dhcp, Strings 1 through 5 are not used.  This object is applicable to http and dhcp probe  types only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminstring2
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminstring3
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminstring4
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminstring5
            
            	This string stores the content of HTTP raw request. rttMonEchoAdminString1\-5 are concatenated to  form the HTTP raw request used in the RTT operation. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadmintargetaddress
            
            	A string which specifies the address of the target
            	**type**\:  str
            
            .. attribute:: rttmonechoadmintargetaddressstring
            
            	A string which specifies the address of the target. This string can be in IP address format or a hostname. This object is applicable to dns probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadmintargetdomainname
            
            	This object specifies the name of the domain in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation
            	**type**\:  str
            
            .. attribute:: rttmonechoadmintargetevc
            
            	This object specifies the Ethernet Virtual Connection in which the destination maintenance point lies. It is only  applicable to ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\:  str
            
            	**length:** 0..100
            
            .. attribute:: rttmonechoadmintargetmacaddress
            
            	This object indicates the MAC address of the target device. This object is only applicable for Y.1731 operations.  rttMonEchoAdminTargetMacAddress and rttMonEchoAdminTargetMPID may not be used in conjunction
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: rttmonechoadmintargetmepport
            
            	This object specifies that Port Level CFM testing towards an Outward/Down MEP will be used. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to NULL for other types of operations
            	**type**\:  bool
            
            .. attribute:: rttmonechoadmintargetmpid
            
            	This object specifies the destination maintenance point ID. It is only applicable to ethernetPing and ethernetJitter  operation. It will be set to 0 for other types of  operations
            	**type**\:  int
            
            	**range:** 0..8191
            
            .. attribute:: rttmonechoadmintargetport
            
            	This object represents the target's port number. This object is applicable to udpEcho, tcpConnect and jitter probes
            	**type**\:  int
            
            	**range:** 0..65536
            
            .. attribute:: rttmonechoadmintargetvlan
            
            	This object specifies the ID of the VLAN in which the destination maintenance point lies. It is only applicable to  ethernetPing and ethernetJitter operation.  It will be set to 0 for other types of operations
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: rttmonechoadmintos
            
            	This object represents the type of service octet in an IP header. This object is not applicable to dhcp, dns,  ethernetPing and ethernetJitter
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rttmonechoadmintstampoptimization
            
            	This object specifies whether timestamp optimization is enabled.  When the value is 'true' then timestamp optimization is enabled.  The probe will utilize lower layer (Hardware/Packet Processor) timestamping values to improve accuracy of statistics.  This value can be set only for udp jitter operation with precision of microsecond
            	**type**\:  bool
            
            .. attribute:: rttmonechoadminurl
            
            	A string which represents the URL to which a HTTP probe should communicate with. This object is applicable to http probe only
            	**type**\:  str
            
            .. attribute:: rttmonechoadminvideotrafficprofile
            
            	A string which represents the profile name to which a video probe should use. This object is applicable to video probe only
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: rttmonechoadminvrfname
            
            	This field is used to specify the VPN name in which the RTT operation will be used. For regular RTT operation this field should not be configured. The agent  will use this field to identify the VPN routing Table for this operation
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry, self).__init__()

                self.yang_name = "rttMonEchoAdminEntry"
                self.yang_parent_name = "rttMonEchoAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonechoadminaggburstcycles = YLeaf(YType.int32, "rttMonEchoAdminAggBurstCycles")

                self.rttmonechoadminavailnumframes = YLeaf(YType.int32, "rttMonEchoAdminAvailNumFrames")

                self.rttmonechoadmincache = YLeaf(YType.boolean, "rttMonEchoAdminCache")

                self.rttmonechoadmincallduration = YLeaf(YType.int32, "rttMonEchoAdminCallDuration")

                self.rttmonechoadmincallednumber = YLeaf(YType.str, "rttMonEchoAdminCalledNumber")

                self.rttmonechoadmincodecinterval = YLeaf(YType.int32, "rttMonEchoAdminCodecInterval")

                self.rttmonechoadmincodecnumpackets = YLeaf(YType.int32, "rttMonEchoAdminCodecNumPackets")

                self.rttmonechoadmincodecpayload = YLeaf(YType.int32, "rttMonEchoAdminCodecPayload")

                self.rttmonechoadmincodectype = YLeaf(YType.enumeration, "rttMonEchoAdminCodecType")

                self.rttmonechoadmincontrolenable = YLeaf(YType.boolean, "rttMonEchoAdminControlEnable")

                self.rttmonechoadmincontrolretry = YLeaf(YType.uint32, "rttMonEchoAdminControlRetry")

                self.rttmonechoadmincontroltimeout = YLeaf(YType.uint32, "rttMonEchoAdminControlTimeout")

                self.rttmonechoadmindetectpoint = YLeaf(YType.enumeration, "rttMonEchoAdminDetectPoint")

                self.rttmonechoadmindscp = YLeaf(YType.uint8, "rttMonEchoAdminDscp")

                self.rttmonechoadminemulatesourceaddress = YLeaf(YType.str, "rttMonEchoAdminEmulateSourceAddress")

                self.rttmonechoadminemulatesourceport = YLeaf(YType.int32, "rttMonEchoAdminEmulateSourcePort")

                self.rttmonechoadminemulatetargetaddress = YLeaf(YType.str, "rttMonEchoAdminEmulateTargetAddress")

                self.rttmonechoadminemulatetargetport = YLeaf(YType.int32, "rttMonEchoAdminEmulateTargetPort")

                self.rttmonechoadminenableburst = YLeaf(YType.boolean, "rttMonEchoAdminEnableBurst")

                self.rttmonechoadminendpointlistname = YLeaf(YType.str, "rttMonEchoAdminEndPointListName")

                self.rttmonechoadminethernetcos = YLeaf(YType.int32, "rttMonEchoAdminEthernetCOS")

                self.rttmonechoadmingkregistration = YLeaf(YType.boolean, "rttMonEchoAdminGKRegistration")

                self.rttmonechoadminhttpversion = YLeaf(YType.str, "rttMonEchoAdminHTTPVersion")

                self.rttmonechoadminicpifadvfactor = YLeaf(YType.int32, "rttMonEchoAdminICPIFAdvFactor")

                self.rttmonechoadminigmptreeinit = YLeaf(YType.uint32, "rttMonEchoAdminIgmpTreeInit")

                self.rttmonechoadmininputinterface = YLeaf(YType.int32, "rttMonEchoAdminInputInterface")

                self.rttmonechoadmininterval = YLeaf(YType.int32, "rttMonEchoAdminInterval")

                self.rttmonechoadminlossrationumframes = YLeaf(YType.int32, "rttMonEchoAdminLossRatioNumFrames")

                self.rttmonechoadminlspexp = YLeaf(YType.int32, "rttMonEchoAdminLSPExp")

                self.rttmonechoadminlspfectype = YLeaf(YType.enumeration, "rttMonEchoAdminLSPFECType")

                self.rttmonechoadminlspnullshim = YLeaf(YType.boolean, "rttMonEchoAdminLSPNullShim")

                self.rttmonechoadminlspreplydscp = YLeaf(YType.int32, "rttMonEchoAdminLSPReplyDscp")

                self.rttmonechoadminlspreplymode = YLeaf(YType.enumeration, "rttMonEchoAdminLSPReplyMode")

                self.rttmonechoadminlspselector = YLeaf(YType.str, "rttMonEchoAdminLSPSelector")

                self.rttmonechoadminlspttl = YLeaf(YType.int32, "rttMonEchoAdminLSPTTL")

                self.rttmonechoadminlspvccvid = YLeaf(YType.int32, "rttMonEchoAdminLSPVccvID")

                self.rttmonechoadminlsrenable = YLeaf(YType.boolean, "rttMonEchoAdminLSREnable")

                self.rttmonechoadminmode = YLeaf(YType.enumeration, "rttMonEchoAdminMode")

                self.rttmonechoadminnameserver = YLeaf(YType.str, "rttMonEchoAdminNameServer")

                self.rttmonechoadminnumpackets = YLeaf(YType.int32, "rttMonEchoAdminNumPackets")

                self.rttmonechoadminoperation = YLeaf(YType.enumeration, "rttMonEchoAdminOperation")

                self.rttmonechoadminowntpsynctolabs = YLeaf(YType.int32, "rttMonEchoAdminOWNTPSyncTolAbs")

                self.rttmonechoadminowntpsynctolpct = YLeaf(YType.int32, "rttMonEchoAdminOWNTPSyncTolPct")

                self.rttmonechoadminowntpsynctoltype = YLeaf(YType.enumeration, "rttMonEchoAdminOWNTPSyncTolType")

                self.rttmonechoadminpktdatarequestsize = YLeaf(YType.int32, "rttMonEchoAdminPktDataRequestSize")

                self.rttmonechoadminpktdataresponsesize = YLeaf(YType.int32, "rttMonEchoAdminPktDataResponseSize")

                self.rttmonechoadminprecision = YLeaf(YType.enumeration, "rttMonEchoAdminPrecision")

                self.rttmonechoadminprobepakpriority = YLeaf(YType.enumeration, "rttMonEchoAdminProbePakPriority")

                self.rttmonechoadminprotocol = YLeaf(YType.enumeration, "rttMonEchoAdminProtocol")

                self.rttmonechoadminproxy = YLeaf(YType.str, "rttMonEchoAdminProxy")

                self.rttmonechoadminreservedsp = YLeaf(YType.enumeration, "rttMonEchoAdminReserveDsp")

                self.rttmonechoadminsourceaddress = YLeaf(YType.str, "rttMonEchoAdminSourceAddress")

                self.rttmonechoadminsourcemacaddress = YLeaf(YType.str, "rttMonEchoAdminSourceMacAddress")

                self.rttmonechoadminsourcempid = YLeaf(YType.uint32, "rttMonEchoAdminSourceMPID")

                self.rttmonechoadminsourceport = YLeaf(YType.int32, "rttMonEchoAdminSourcePort")

                self.rttmonechoadminsourcevoiceport = YLeaf(YType.str, "rttMonEchoAdminSourceVoicePort")

                self.rttmonechoadminssm = YLeaf(YType.boolean, "rttMonEchoAdminSSM")

                self.rttmonechoadminstring1 = YLeaf(YType.str, "rttMonEchoAdminString1")

                self.rttmonechoadminstring2 = YLeaf(YType.str, "rttMonEchoAdminString2")

                self.rttmonechoadminstring3 = YLeaf(YType.str, "rttMonEchoAdminString3")

                self.rttmonechoadminstring4 = YLeaf(YType.str, "rttMonEchoAdminString4")

                self.rttmonechoadminstring5 = YLeaf(YType.str, "rttMonEchoAdminString5")

                self.rttmonechoadmintargetaddress = YLeaf(YType.str, "rttMonEchoAdminTargetAddress")

                self.rttmonechoadmintargetaddressstring = YLeaf(YType.str, "rttMonEchoAdminTargetAddressString")

                self.rttmonechoadmintargetdomainname = YLeaf(YType.str, "rttMonEchoAdminTargetDomainName")

                self.rttmonechoadmintargetevc = YLeaf(YType.str, "rttMonEchoAdminTargetEVC")

                self.rttmonechoadmintargetmacaddress = YLeaf(YType.str, "rttMonEchoAdminTargetMacAddress")

                self.rttmonechoadmintargetmepport = YLeaf(YType.boolean, "rttMonEchoAdminTargetMEPPort")

                self.rttmonechoadmintargetmpid = YLeaf(YType.uint32, "rttMonEchoAdminTargetMPID")

                self.rttmonechoadmintargetport = YLeaf(YType.int32, "rttMonEchoAdminTargetPort")

                self.rttmonechoadmintargetvlan = YLeaf(YType.int32, "rttMonEchoAdminTargetVLAN")

                self.rttmonechoadmintos = YLeaf(YType.int32, "rttMonEchoAdminTOS")

                self.rttmonechoadmintstampoptimization = YLeaf(YType.boolean, "rttMonEchoAdminTstampOptimization")

                self.rttmonechoadminurl = YLeaf(YType.str, "rttMonEchoAdminURL")

                self.rttmonechoadminvideotrafficprofile = YLeaf(YType.str, "rttMonEchoAdminVideoTrafficProfile")

                self.rttmonechoadminvrfname = YLeaf(YType.str, "rttMonEchoAdminVrfName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonechoadminaggburstcycles",
                                "rttmonechoadminavailnumframes",
                                "rttmonechoadmincache",
                                "rttmonechoadmincallduration",
                                "rttmonechoadmincallednumber",
                                "rttmonechoadmincodecinterval",
                                "rttmonechoadmincodecnumpackets",
                                "rttmonechoadmincodecpayload",
                                "rttmonechoadmincodectype",
                                "rttmonechoadmincontrolenable",
                                "rttmonechoadmincontrolretry",
                                "rttmonechoadmincontroltimeout",
                                "rttmonechoadmindetectpoint",
                                "rttmonechoadmindscp",
                                "rttmonechoadminemulatesourceaddress",
                                "rttmonechoadminemulatesourceport",
                                "rttmonechoadminemulatetargetaddress",
                                "rttmonechoadminemulatetargetport",
                                "rttmonechoadminenableburst",
                                "rttmonechoadminendpointlistname",
                                "rttmonechoadminethernetcos",
                                "rttmonechoadmingkregistration",
                                "rttmonechoadminhttpversion",
                                "rttmonechoadminicpifadvfactor",
                                "rttmonechoadminigmptreeinit",
                                "rttmonechoadmininputinterface",
                                "rttmonechoadmininterval",
                                "rttmonechoadminlossrationumframes",
                                "rttmonechoadminlspexp",
                                "rttmonechoadminlspfectype",
                                "rttmonechoadminlspnullshim",
                                "rttmonechoadminlspreplydscp",
                                "rttmonechoadminlspreplymode",
                                "rttmonechoadminlspselector",
                                "rttmonechoadminlspttl",
                                "rttmonechoadminlspvccvid",
                                "rttmonechoadminlsrenable",
                                "rttmonechoadminmode",
                                "rttmonechoadminnameserver",
                                "rttmonechoadminnumpackets",
                                "rttmonechoadminoperation",
                                "rttmonechoadminowntpsynctolabs",
                                "rttmonechoadminowntpsynctolpct",
                                "rttmonechoadminowntpsynctoltype",
                                "rttmonechoadminpktdatarequestsize",
                                "rttmonechoadminpktdataresponsesize",
                                "rttmonechoadminprecision",
                                "rttmonechoadminprobepakpriority",
                                "rttmonechoadminprotocol",
                                "rttmonechoadminproxy",
                                "rttmonechoadminreservedsp",
                                "rttmonechoadminsourceaddress",
                                "rttmonechoadminsourcemacaddress",
                                "rttmonechoadminsourcempid",
                                "rttmonechoadminsourceport",
                                "rttmonechoadminsourcevoiceport",
                                "rttmonechoadminssm",
                                "rttmonechoadminstring1",
                                "rttmonechoadminstring2",
                                "rttmonechoadminstring3",
                                "rttmonechoadminstring4",
                                "rttmonechoadminstring5",
                                "rttmonechoadmintargetaddress",
                                "rttmonechoadmintargetaddressstring",
                                "rttmonechoadmintargetdomainname",
                                "rttmonechoadmintargetevc",
                                "rttmonechoadmintargetmacaddress",
                                "rttmonechoadmintargetmepport",
                                "rttmonechoadmintargetmpid",
                                "rttmonechoadmintargetport",
                                "rttmonechoadmintargetvlan",
                                "rttmonechoadmintos",
                                "rttmonechoadmintstampoptimization",
                                "rttmonechoadminurl",
                                "rttmonechoadminvideotrafficprofile",
                                "rttmonechoadminvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry, self).__setattr__(name, value)

            class Rttmonechoadminlspfectype(Enum):
                """
                Rttmonechoadminlspfectype

                The type of the target FEC for the RTT 'echo' and 'pathEcho'

                operations based on 'mplsLspPingAppl' RttMonProtocol.

                ldpIpv4Prefix   \- LDP IPv4 prefix.

                .. data:: ldpIpv4Prefix = 1

                """

                ldpIpv4Prefix = Enum.YLeaf(1, "ldpIpv4Prefix")


            class Rttmonechoadminowntpsynctoltype(Enum):
                """
                Rttmonechoadminowntpsynctoltype

                This object specifies whether the value in specified for oneway

                NTP sync tolerance is absolute value or percent value

                .. data:: percent = 1

                .. data:: absolute = 2

                """

                percent = Enum.YLeaf(1, "percent")

                absolute = Enum.YLeaf(2, "absolute")


            class Rttmonechoadminprecision(Enum):
                """
                Rttmonechoadminprecision

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
                Rttmonechoadminprobepakpriority

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
                Rttmonechoadminreservedsp

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


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonechoadminaggburstcycles.is_set or
                    self.rttmonechoadminavailnumframes.is_set or
                    self.rttmonechoadmincache.is_set or
                    self.rttmonechoadmincallduration.is_set or
                    self.rttmonechoadmincallednumber.is_set or
                    self.rttmonechoadmincodecinterval.is_set or
                    self.rttmonechoadmincodecnumpackets.is_set or
                    self.rttmonechoadmincodecpayload.is_set or
                    self.rttmonechoadmincodectype.is_set or
                    self.rttmonechoadmincontrolenable.is_set or
                    self.rttmonechoadmincontrolretry.is_set or
                    self.rttmonechoadmincontroltimeout.is_set or
                    self.rttmonechoadmindetectpoint.is_set or
                    self.rttmonechoadmindscp.is_set or
                    self.rttmonechoadminemulatesourceaddress.is_set or
                    self.rttmonechoadminemulatesourceport.is_set or
                    self.rttmonechoadminemulatetargetaddress.is_set or
                    self.rttmonechoadminemulatetargetport.is_set or
                    self.rttmonechoadminenableburst.is_set or
                    self.rttmonechoadminendpointlistname.is_set or
                    self.rttmonechoadminethernetcos.is_set or
                    self.rttmonechoadmingkregistration.is_set or
                    self.rttmonechoadminhttpversion.is_set or
                    self.rttmonechoadminicpifadvfactor.is_set or
                    self.rttmonechoadminigmptreeinit.is_set or
                    self.rttmonechoadmininputinterface.is_set or
                    self.rttmonechoadmininterval.is_set or
                    self.rttmonechoadminlossrationumframes.is_set or
                    self.rttmonechoadminlspexp.is_set or
                    self.rttmonechoadminlspfectype.is_set or
                    self.rttmonechoadminlspnullshim.is_set or
                    self.rttmonechoadminlspreplydscp.is_set or
                    self.rttmonechoadminlspreplymode.is_set or
                    self.rttmonechoadminlspselector.is_set or
                    self.rttmonechoadminlspttl.is_set or
                    self.rttmonechoadminlspvccvid.is_set or
                    self.rttmonechoadminlsrenable.is_set or
                    self.rttmonechoadminmode.is_set or
                    self.rttmonechoadminnameserver.is_set or
                    self.rttmonechoadminnumpackets.is_set or
                    self.rttmonechoadminoperation.is_set or
                    self.rttmonechoadminowntpsynctolabs.is_set or
                    self.rttmonechoadminowntpsynctolpct.is_set or
                    self.rttmonechoadminowntpsynctoltype.is_set or
                    self.rttmonechoadminpktdatarequestsize.is_set or
                    self.rttmonechoadminpktdataresponsesize.is_set or
                    self.rttmonechoadminprecision.is_set or
                    self.rttmonechoadminprobepakpriority.is_set or
                    self.rttmonechoadminprotocol.is_set or
                    self.rttmonechoadminproxy.is_set or
                    self.rttmonechoadminreservedsp.is_set or
                    self.rttmonechoadminsourceaddress.is_set or
                    self.rttmonechoadminsourcemacaddress.is_set or
                    self.rttmonechoadminsourcempid.is_set or
                    self.rttmonechoadminsourceport.is_set or
                    self.rttmonechoadminsourcevoiceport.is_set or
                    self.rttmonechoadminssm.is_set or
                    self.rttmonechoadminstring1.is_set or
                    self.rttmonechoadminstring2.is_set or
                    self.rttmonechoadminstring3.is_set or
                    self.rttmonechoadminstring4.is_set or
                    self.rttmonechoadminstring5.is_set or
                    self.rttmonechoadmintargetaddress.is_set or
                    self.rttmonechoadmintargetaddressstring.is_set or
                    self.rttmonechoadmintargetdomainname.is_set or
                    self.rttmonechoadmintargetevc.is_set or
                    self.rttmonechoadmintargetmacaddress.is_set or
                    self.rttmonechoadmintargetmepport.is_set or
                    self.rttmonechoadmintargetmpid.is_set or
                    self.rttmonechoadmintargetport.is_set or
                    self.rttmonechoadmintargetvlan.is_set or
                    self.rttmonechoadmintos.is_set or
                    self.rttmonechoadmintstampoptimization.is_set or
                    self.rttmonechoadminurl.is_set or
                    self.rttmonechoadminvideotrafficprofile.is_set or
                    self.rttmonechoadminvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonechoadminaggburstcycles.yfilter != YFilter.not_set or
                    self.rttmonechoadminavailnumframes.yfilter != YFilter.not_set or
                    self.rttmonechoadmincache.yfilter != YFilter.not_set or
                    self.rttmonechoadmincallduration.yfilter != YFilter.not_set or
                    self.rttmonechoadmincallednumber.yfilter != YFilter.not_set or
                    self.rttmonechoadmincodecinterval.yfilter != YFilter.not_set or
                    self.rttmonechoadmincodecnumpackets.yfilter != YFilter.not_set or
                    self.rttmonechoadmincodecpayload.yfilter != YFilter.not_set or
                    self.rttmonechoadmincodectype.yfilter != YFilter.not_set or
                    self.rttmonechoadmincontrolenable.yfilter != YFilter.not_set or
                    self.rttmonechoadmincontrolretry.yfilter != YFilter.not_set or
                    self.rttmonechoadmincontroltimeout.yfilter != YFilter.not_set or
                    self.rttmonechoadmindetectpoint.yfilter != YFilter.not_set or
                    self.rttmonechoadmindscp.yfilter != YFilter.not_set or
                    self.rttmonechoadminemulatesourceaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadminemulatesourceport.yfilter != YFilter.not_set or
                    self.rttmonechoadminemulatetargetaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadminemulatetargetport.yfilter != YFilter.not_set or
                    self.rttmonechoadminenableburst.yfilter != YFilter.not_set or
                    self.rttmonechoadminendpointlistname.yfilter != YFilter.not_set or
                    self.rttmonechoadminethernetcos.yfilter != YFilter.not_set or
                    self.rttmonechoadmingkregistration.yfilter != YFilter.not_set or
                    self.rttmonechoadminhttpversion.yfilter != YFilter.not_set or
                    self.rttmonechoadminicpifadvfactor.yfilter != YFilter.not_set or
                    self.rttmonechoadminigmptreeinit.yfilter != YFilter.not_set or
                    self.rttmonechoadmininputinterface.yfilter != YFilter.not_set or
                    self.rttmonechoadmininterval.yfilter != YFilter.not_set or
                    self.rttmonechoadminlossrationumframes.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspexp.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspfectype.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspnullshim.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspreplydscp.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspreplymode.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspselector.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspttl.yfilter != YFilter.not_set or
                    self.rttmonechoadminlspvccvid.yfilter != YFilter.not_set or
                    self.rttmonechoadminlsrenable.yfilter != YFilter.not_set or
                    self.rttmonechoadminmode.yfilter != YFilter.not_set or
                    self.rttmonechoadminnameserver.yfilter != YFilter.not_set or
                    self.rttmonechoadminnumpackets.yfilter != YFilter.not_set or
                    self.rttmonechoadminoperation.yfilter != YFilter.not_set or
                    self.rttmonechoadminowntpsynctolabs.yfilter != YFilter.not_set or
                    self.rttmonechoadminowntpsynctolpct.yfilter != YFilter.not_set or
                    self.rttmonechoadminowntpsynctoltype.yfilter != YFilter.not_set or
                    self.rttmonechoadminpktdatarequestsize.yfilter != YFilter.not_set or
                    self.rttmonechoadminpktdataresponsesize.yfilter != YFilter.not_set or
                    self.rttmonechoadminprecision.yfilter != YFilter.not_set or
                    self.rttmonechoadminprobepakpriority.yfilter != YFilter.not_set or
                    self.rttmonechoadminprotocol.yfilter != YFilter.not_set or
                    self.rttmonechoadminproxy.yfilter != YFilter.not_set or
                    self.rttmonechoadminreservedsp.yfilter != YFilter.not_set or
                    self.rttmonechoadminsourceaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadminsourcemacaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadminsourcempid.yfilter != YFilter.not_set or
                    self.rttmonechoadminsourceport.yfilter != YFilter.not_set or
                    self.rttmonechoadminsourcevoiceport.yfilter != YFilter.not_set or
                    self.rttmonechoadminssm.yfilter != YFilter.not_set or
                    self.rttmonechoadminstring1.yfilter != YFilter.not_set or
                    self.rttmonechoadminstring2.yfilter != YFilter.not_set or
                    self.rttmonechoadminstring3.yfilter != YFilter.not_set or
                    self.rttmonechoadminstring4.yfilter != YFilter.not_set or
                    self.rttmonechoadminstring5.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetaddressstring.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetdomainname.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetevc.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetmacaddress.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetmepport.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetmpid.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetport.yfilter != YFilter.not_set or
                    self.rttmonechoadmintargetvlan.yfilter != YFilter.not_set or
                    self.rttmonechoadmintos.yfilter != YFilter.not_set or
                    self.rttmonechoadmintstampoptimization.yfilter != YFilter.not_set or
                    self.rttmonechoadminurl.yfilter != YFilter.not_set or
                    self.rttmonechoadminvideotrafficprofile.yfilter != YFilter.not_set or
                    self.rttmonechoadminvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonEchoAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonEchoAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonechoadminaggburstcycles.is_set or self.rttmonechoadminaggburstcycles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminaggburstcycles.get_name_leafdata())
                if (self.rttmonechoadminavailnumframes.is_set or self.rttmonechoadminavailnumframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminavailnumframes.get_name_leafdata())
                if (self.rttmonechoadmincache.is_set or self.rttmonechoadmincache.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincache.get_name_leafdata())
                if (self.rttmonechoadmincallduration.is_set or self.rttmonechoadmincallduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincallduration.get_name_leafdata())
                if (self.rttmonechoadmincallednumber.is_set or self.rttmonechoadmincallednumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincallednumber.get_name_leafdata())
                if (self.rttmonechoadmincodecinterval.is_set or self.rttmonechoadmincodecinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincodecinterval.get_name_leafdata())
                if (self.rttmonechoadmincodecnumpackets.is_set or self.rttmonechoadmincodecnumpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincodecnumpackets.get_name_leafdata())
                if (self.rttmonechoadmincodecpayload.is_set or self.rttmonechoadmincodecpayload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincodecpayload.get_name_leafdata())
                if (self.rttmonechoadmincodectype.is_set or self.rttmonechoadmincodectype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincodectype.get_name_leafdata())
                if (self.rttmonechoadmincontrolenable.is_set or self.rttmonechoadmincontrolenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincontrolenable.get_name_leafdata())
                if (self.rttmonechoadmincontrolretry.is_set or self.rttmonechoadmincontrolretry.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincontrolretry.get_name_leafdata())
                if (self.rttmonechoadmincontroltimeout.is_set or self.rttmonechoadmincontroltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmincontroltimeout.get_name_leafdata())
                if (self.rttmonechoadmindetectpoint.is_set or self.rttmonechoadmindetectpoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmindetectpoint.get_name_leafdata())
                if (self.rttmonechoadmindscp.is_set or self.rttmonechoadmindscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmindscp.get_name_leafdata())
                if (self.rttmonechoadminemulatesourceaddress.is_set or self.rttmonechoadminemulatesourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminemulatesourceaddress.get_name_leafdata())
                if (self.rttmonechoadminemulatesourceport.is_set or self.rttmonechoadminemulatesourceport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminemulatesourceport.get_name_leafdata())
                if (self.rttmonechoadminemulatetargetaddress.is_set or self.rttmonechoadminemulatetargetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminemulatetargetaddress.get_name_leafdata())
                if (self.rttmonechoadminemulatetargetport.is_set or self.rttmonechoadminemulatetargetport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminemulatetargetport.get_name_leafdata())
                if (self.rttmonechoadminenableburst.is_set or self.rttmonechoadminenableburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminenableburst.get_name_leafdata())
                if (self.rttmonechoadminendpointlistname.is_set or self.rttmonechoadminendpointlistname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminendpointlistname.get_name_leafdata())
                if (self.rttmonechoadminethernetcos.is_set or self.rttmonechoadminethernetcos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminethernetcos.get_name_leafdata())
                if (self.rttmonechoadmingkregistration.is_set or self.rttmonechoadmingkregistration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmingkregistration.get_name_leafdata())
                if (self.rttmonechoadminhttpversion.is_set or self.rttmonechoadminhttpversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminhttpversion.get_name_leafdata())
                if (self.rttmonechoadminicpifadvfactor.is_set or self.rttmonechoadminicpifadvfactor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminicpifadvfactor.get_name_leafdata())
                if (self.rttmonechoadminigmptreeinit.is_set or self.rttmonechoadminigmptreeinit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminigmptreeinit.get_name_leafdata())
                if (self.rttmonechoadmininputinterface.is_set or self.rttmonechoadmininputinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmininputinterface.get_name_leafdata())
                if (self.rttmonechoadmininterval.is_set or self.rttmonechoadmininterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmininterval.get_name_leafdata())
                if (self.rttmonechoadminlossrationumframes.is_set or self.rttmonechoadminlossrationumframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlossrationumframes.get_name_leafdata())
                if (self.rttmonechoadminlspexp.is_set or self.rttmonechoadminlspexp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspexp.get_name_leafdata())
                if (self.rttmonechoadminlspfectype.is_set or self.rttmonechoadminlspfectype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspfectype.get_name_leafdata())
                if (self.rttmonechoadminlspnullshim.is_set or self.rttmonechoadminlspnullshim.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspnullshim.get_name_leafdata())
                if (self.rttmonechoadminlspreplydscp.is_set or self.rttmonechoadminlspreplydscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspreplydscp.get_name_leafdata())
                if (self.rttmonechoadminlspreplymode.is_set or self.rttmonechoadminlspreplymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspreplymode.get_name_leafdata())
                if (self.rttmonechoadminlspselector.is_set or self.rttmonechoadminlspselector.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspselector.get_name_leafdata())
                if (self.rttmonechoadminlspttl.is_set or self.rttmonechoadminlspttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspttl.get_name_leafdata())
                if (self.rttmonechoadminlspvccvid.is_set or self.rttmonechoadminlspvccvid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlspvccvid.get_name_leafdata())
                if (self.rttmonechoadminlsrenable.is_set or self.rttmonechoadminlsrenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminlsrenable.get_name_leafdata())
                if (self.rttmonechoadminmode.is_set or self.rttmonechoadminmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminmode.get_name_leafdata())
                if (self.rttmonechoadminnameserver.is_set or self.rttmonechoadminnameserver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminnameserver.get_name_leafdata())
                if (self.rttmonechoadminnumpackets.is_set or self.rttmonechoadminnumpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminnumpackets.get_name_leafdata())
                if (self.rttmonechoadminoperation.is_set or self.rttmonechoadminoperation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminoperation.get_name_leafdata())
                if (self.rttmonechoadminowntpsynctolabs.is_set or self.rttmonechoadminowntpsynctolabs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminowntpsynctolabs.get_name_leafdata())
                if (self.rttmonechoadminowntpsynctolpct.is_set or self.rttmonechoadminowntpsynctolpct.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminowntpsynctolpct.get_name_leafdata())
                if (self.rttmonechoadminowntpsynctoltype.is_set or self.rttmonechoadminowntpsynctoltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminowntpsynctoltype.get_name_leafdata())
                if (self.rttmonechoadminpktdatarequestsize.is_set or self.rttmonechoadminpktdatarequestsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminpktdatarequestsize.get_name_leafdata())
                if (self.rttmonechoadminpktdataresponsesize.is_set or self.rttmonechoadminpktdataresponsesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminpktdataresponsesize.get_name_leafdata())
                if (self.rttmonechoadminprecision.is_set or self.rttmonechoadminprecision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminprecision.get_name_leafdata())
                if (self.rttmonechoadminprobepakpriority.is_set or self.rttmonechoadminprobepakpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminprobepakpriority.get_name_leafdata())
                if (self.rttmonechoadminprotocol.is_set or self.rttmonechoadminprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminprotocol.get_name_leafdata())
                if (self.rttmonechoadminproxy.is_set or self.rttmonechoadminproxy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminproxy.get_name_leafdata())
                if (self.rttmonechoadminreservedsp.is_set or self.rttmonechoadminreservedsp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminreservedsp.get_name_leafdata())
                if (self.rttmonechoadminsourceaddress.is_set or self.rttmonechoadminsourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminsourceaddress.get_name_leafdata())
                if (self.rttmonechoadminsourcemacaddress.is_set or self.rttmonechoadminsourcemacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminsourcemacaddress.get_name_leafdata())
                if (self.rttmonechoadminsourcempid.is_set or self.rttmonechoadminsourcempid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminsourcempid.get_name_leafdata())
                if (self.rttmonechoadminsourceport.is_set or self.rttmonechoadminsourceport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminsourceport.get_name_leafdata())
                if (self.rttmonechoadminsourcevoiceport.is_set or self.rttmonechoadminsourcevoiceport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminsourcevoiceport.get_name_leafdata())
                if (self.rttmonechoadminssm.is_set or self.rttmonechoadminssm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminssm.get_name_leafdata())
                if (self.rttmonechoadminstring1.is_set or self.rttmonechoadminstring1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminstring1.get_name_leafdata())
                if (self.rttmonechoadminstring2.is_set or self.rttmonechoadminstring2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminstring2.get_name_leafdata())
                if (self.rttmonechoadminstring3.is_set or self.rttmonechoadminstring3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminstring3.get_name_leafdata())
                if (self.rttmonechoadminstring4.is_set or self.rttmonechoadminstring4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminstring4.get_name_leafdata())
                if (self.rttmonechoadminstring5.is_set or self.rttmonechoadminstring5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminstring5.get_name_leafdata())
                if (self.rttmonechoadmintargetaddress.is_set or self.rttmonechoadmintargetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetaddress.get_name_leafdata())
                if (self.rttmonechoadmintargetaddressstring.is_set or self.rttmonechoadmintargetaddressstring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetaddressstring.get_name_leafdata())
                if (self.rttmonechoadmintargetdomainname.is_set or self.rttmonechoadmintargetdomainname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetdomainname.get_name_leafdata())
                if (self.rttmonechoadmintargetevc.is_set or self.rttmonechoadmintargetevc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetevc.get_name_leafdata())
                if (self.rttmonechoadmintargetmacaddress.is_set or self.rttmonechoadmintargetmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetmacaddress.get_name_leafdata())
                if (self.rttmonechoadmintargetmepport.is_set or self.rttmonechoadmintargetmepport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetmepport.get_name_leafdata())
                if (self.rttmonechoadmintargetmpid.is_set or self.rttmonechoadmintargetmpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetmpid.get_name_leafdata())
                if (self.rttmonechoadmintargetport.is_set or self.rttmonechoadmintargetport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetport.get_name_leafdata())
                if (self.rttmonechoadmintargetvlan.is_set or self.rttmonechoadmintargetvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintargetvlan.get_name_leafdata())
                if (self.rttmonechoadmintos.is_set or self.rttmonechoadmintos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintos.get_name_leafdata())
                if (self.rttmonechoadmintstampoptimization.is_set or self.rttmonechoadmintstampoptimization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadmintstampoptimization.get_name_leafdata())
                if (self.rttmonechoadminurl.is_set or self.rttmonechoadminurl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminurl.get_name_leafdata())
                if (self.rttmonechoadminvideotrafficprofile.is_set or self.rttmonechoadminvideotrafficprofile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminvideotrafficprofile.get_name_leafdata())
                if (self.rttmonechoadminvrfname.is_set or self.rttmonechoadminvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechoadminvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonEchoAdminAggBurstCycles" or name == "rttMonEchoAdminAvailNumFrames" or name == "rttMonEchoAdminCache" or name == "rttMonEchoAdminCallDuration" or name == "rttMonEchoAdminCalledNumber" or name == "rttMonEchoAdminCodecInterval" or name == "rttMonEchoAdminCodecNumPackets" or name == "rttMonEchoAdminCodecPayload" or name == "rttMonEchoAdminCodecType" or name == "rttMonEchoAdminControlEnable" or name == "rttMonEchoAdminControlRetry" or name == "rttMonEchoAdminControlTimeout" or name == "rttMonEchoAdminDetectPoint" or name == "rttMonEchoAdminDscp" or name == "rttMonEchoAdminEmulateSourceAddress" or name == "rttMonEchoAdminEmulateSourcePort" or name == "rttMonEchoAdminEmulateTargetAddress" or name == "rttMonEchoAdminEmulateTargetPort" or name == "rttMonEchoAdminEnableBurst" or name == "rttMonEchoAdminEndPointListName" or name == "rttMonEchoAdminEthernetCOS" or name == "rttMonEchoAdminGKRegistration" or name == "rttMonEchoAdminHTTPVersion" or name == "rttMonEchoAdminICPIFAdvFactor" or name == "rttMonEchoAdminIgmpTreeInit" or name == "rttMonEchoAdminInputInterface" or name == "rttMonEchoAdminInterval" or name == "rttMonEchoAdminLossRatioNumFrames" or name == "rttMonEchoAdminLSPExp" or name == "rttMonEchoAdminLSPFECType" or name == "rttMonEchoAdminLSPNullShim" or name == "rttMonEchoAdminLSPReplyDscp" or name == "rttMonEchoAdminLSPReplyMode" or name == "rttMonEchoAdminLSPSelector" or name == "rttMonEchoAdminLSPTTL" or name == "rttMonEchoAdminLSPVccvID" or name == "rttMonEchoAdminLSREnable" or name == "rttMonEchoAdminMode" or name == "rttMonEchoAdminNameServer" or name == "rttMonEchoAdminNumPackets" or name == "rttMonEchoAdminOperation" or name == "rttMonEchoAdminOWNTPSyncTolAbs" or name == "rttMonEchoAdminOWNTPSyncTolPct" or name == "rttMonEchoAdminOWNTPSyncTolType" or name == "rttMonEchoAdminPktDataRequestSize" or name == "rttMonEchoAdminPktDataResponseSize" or name == "rttMonEchoAdminPrecision" or name == "rttMonEchoAdminProbePakPriority" or name == "rttMonEchoAdminProtocol" or name == "rttMonEchoAdminProxy" or name == "rttMonEchoAdminReserveDsp" or name == "rttMonEchoAdminSourceAddress" or name == "rttMonEchoAdminSourceMacAddress" or name == "rttMonEchoAdminSourceMPID" or name == "rttMonEchoAdminSourcePort" or name == "rttMonEchoAdminSourceVoicePort" or name == "rttMonEchoAdminSSM" or name == "rttMonEchoAdminString1" or name == "rttMonEchoAdminString2" or name == "rttMonEchoAdminString3" or name == "rttMonEchoAdminString4" or name == "rttMonEchoAdminString5" or name == "rttMonEchoAdminTargetAddress" or name == "rttMonEchoAdminTargetAddressString" or name == "rttMonEchoAdminTargetDomainName" or name == "rttMonEchoAdminTargetEVC" or name == "rttMonEchoAdminTargetMacAddress" or name == "rttMonEchoAdminTargetMEPPort" or name == "rttMonEchoAdminTargetMPID" or name == "rttMonEchoAdminTargetPort" or name == "rttMonEchoAdminTargetVLAN" or name == "rttMonEchoAdminTOS" or name == "rttMonEchoAdminTstampOptimization" or name == "rttMonEchoAdminURL" or name == "rttMonEchoAdminVideoTrafficProfile" or name == "rttMonEchoAdminVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminAggBurstCycles"):
                    self.rttmonechoadminaggburstcycles = value
                    self.rttmonechoadminaggburstcycles.value_namespace = name_space
                    self.rttmonechoadminaggburstcycles.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminAvailNumFrames"):
                    self.rttmonechoadminavailnumframes = value
                    self.rttmonechoadminavailnumframes.value_namespace = name_space
                    self.rttmonechoadminavailnumframes.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCache"):
                    self.rttmonechoadmincache = value
                    self.rttmonechoadmincache.value_namespace = name_space
                    self.rttmonechoadmincache.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCallDuration"):
                    self.rttmonechoadmincallduration = value
                    self.rttmonechoadmincallduration.value_namespace = name_space
                    self.rttmonechoadmincallduration.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCalledNumber"):
                    self.rttmonechoadmincallednumber = value
                    self.rttmonechoadmincallednumber.value_namespace = name_space
                    self.rttmonechoadmincallednumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCodecInterval"):
                    self.rttmonechoadmincodecinterval = value
                    self.rttmonechoadmincodecinterval.value_namespace = name_space
                    self.rttmonechoadmincodecinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCodecNumPackets"):
                    self.rttmonechoadmincodecnumpackets = value
                    self.rttmonechoadmincodecnumpackets.value_namespace = name_space
                    self.rttmonechoadmincodecnumpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCodecPayload"):
                    self.rttmonechoadmincodecpayload = value
                    self.rttmonechoadmincodecpayload.value_namespace = name_space
                    self.rttmonechoadmincodecpayload.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminCodecType"):
                    self.rttmonechoadmincodectype = value
                    self.rttmonechoadmincodectype.value_namespace = name_space
                    self.rttmonechoadmincodectype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminControlEnable"):
                    self.rttmonechoadmincontrolenable = value
                    self.rttmonechoadmincontrolenable.value_namespace = name_space
                    self.rttmonechoadmincontrolenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminControlRetry"):
                    self.rttmonechoadmincontrolretry = value
                    self.rttmonechoadmincontrolretry.value_namespace = name_space
                    self.rttmonechoadmincontrolretry.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminControlTimeout"):
                    self.rttmonechoadmincontroltimeout = value
                    self.rttmonechoadmincontroltimeout.value_namespace = name_space
                    self.rttmonechoadmincontroltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminDetectPoint"):
                    self.rttmonechoadmindetectpoint = value
                    self.rttmonechoadmindetectpoint.value_namespace = name_space
                    self.rttmonechoadmindetectpoint.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminDscp"):
                    self.rttmonechoadmindscp = value
                    self.rttmonechoadmindscp.value_namespace = name_space
                    self.rttmonechoadmindscp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEmulateSourceAddress"):
                    self.rttmonechoadminemulatesourceaddress = value
                    self.rttmonechoadminemulatesourceaddress.value_namespace = name_space
                    self.rttmonechoadminemulatesourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEmulateSourcePort"):
                    self.rttmonechoadminemulatesourceport = value
                    self.rttmonechoadminemulatesourceport.value_namespace = name_space
                    self.rttmonechoadminemulatesourceport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEmulateTargetAddress"):
                    self.rttmonechoadminemulatetargetaddress = value
                    self.rttmonechoadminemulatetargetaddress.value_namespace = name_space
                    self.rttmonechoadminemulatetargetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEmulateTargetPort"):
                    self.rttmonechoadminemulatetargetport = value
                    self.rttmonechoadminemulatetargetport.value_namespace = name_space
                    self.rttmonechoadminemulatetargetport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEnableBurst"):
                    self.rttmonechoadminenableburst = value
                    self.rttmonechoadminenableburst.value_namespace = name_space
                    self.rttmonechoadminenableburst.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEndPointListName"):
                    self.rttmonechoadminendpointlistname = value
                    self.rttmonechoadminendpointlistname.value_namespace = name_space
                    self.rttmonechoadminendpointlistname.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminEthernetCOS"):
                    self.rttmonechoadminethernetcos = value
                    self.rttmonechoadminethernetcos.value_namespace = name_space
                    self.rttmonechoadminethernetcos.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminGKRegistration"):
                    self.rttmonechoadmingkregistration = value
                    self.rttmonechoadmingkregistration.value_namespace = name_space
                    self.rttmonechoadmingkregistration.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminHTTPVersion"):
                    self.rttmonechoadminhttpversion = value
                    self.rttmonechoadminhttpversion.value_namespace = name_space
                    self.rttmonechoadminhttpversion.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminICPIFAdvFactor"):
                    self.rttmonechoadminicpifadvfactor = value
                    self.rttmonechoadminicpifadvfactor.value_namespace = name_space
                    self.rttmonechoadminicpifadvfactor.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminIgmpTreeInit"):
                    self.rttmonechoadminigmptreeinit = value
                    self.rttmonechoadminigmptreeinit.value_namespace = name_space
                    self.rttmonechoadminigmptreeinit.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminInputInterface"):
                    self.rttmonechoadmininputinterface = value
                    self.rttmonechoadmininputinterface.value_namespace = name_space
                    self.rttmonechoadmininputinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminInterval"):
                    self.rttmonechoadmininterval = value
                    self.rttmonechoadmininterval.value_namespace = name_space
                    self.rttmonechoadmininterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLossRatioNumFrames"):
                    self.rttmonechoadminlossrationumframes = value
                    self.rttmonechoadminlossrationumframes.value_namespace = name_space
                    self.rttmonechoadminlossrationumframes.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPExp"):
                    self.rttmonechoadminlspexp = value
                    self.rttmonechoadminlspexp.value_namespace = name_space
                    self.rttmonechoadminlspexp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPFECType"):
                    self.rttmonechoadminlspfectype = value
                    self.rttmonechoadminlspfectype.value_namespace = name_space
                    self.rttmonechoadminlspfectype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPNullShim"):
                    self.rttmonechoadminlspnullshim = value
                    self.rttmonechoadminlspnullshim.value_namespace = name_space
                    self.rttmonechoadminlspnullshim.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPReplyDscp"):
                    self.rttmonechoadminlspreplydscp = value
                    self.rttmonechoadminlspreplydscp.value_namespace = name_space
                    self.rttmonechoadminlspreplydscp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPReplyMode"):
                    self.rttmonechoadminlspreplymode = value
                    self.rttmonechoadminlspreplymode.value_namespace = name_space
                    self.rttmonechoadminlspreplymode.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPSelector"):
                    self.rttmonechoadminlspselector = value
                    self.rttmonechoadminlspselector.value_namespace = name_space
                    self.rttmonechoadminlspselector.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPTTL"):
                    self.rttmonechoadminlspttl = value
                    self.rttmonechoadminlspttl.value_namespace = name_space
                    self.rttmonechoadminlspttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSPVccvID"):
                    self.rttmonechoadminlspvccvid = value
                    self.rttmonechoadminlspvccvid.value_namespace = name_space
                    self.rttmonechoadminlspvccvid.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminLSREnable"):
                    self.rttmonechoadminlsrenable = value
                    self.rttmonechoadminlsrenable.value_namespace = name_space
                    self.rttmonechoadminlsrenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminMode"):
                    self.rttmonechoadminmode = value
                    self.rttmonechoadminmode.value_namespace = name_space
                    self.rttmonechoadminmode.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminNameServer"):
                    self.rttmonechoadminnameserver = value
                    self.rttmonechoadminnameserver.value_namespace = name_space
                    self.rttmonechoadminnameserver.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminNumPackets"):
                    self.rttmonechoadminnumpackets = value
                    self.rttmonechoadminnumpackets.value_namespace = name_space
                    self.rttmonechoadminnumpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminOperation"):
                    self.rttmonechoadminoperation = value
                    self.rttmonechoadminoperation.value_namespace = name_space
                    self.rttmonechoadminoperation.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminOWNTPSyncTolAbs"):
                    self.rttmonechoadminowntpsynctolabs = value
                    self.rttmonechoadminowntpsynctolabs.value_namespace = name_space
                    self.rttmonechoadminowntpsynctolabs.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminOWNTPSyncTolPct"):
                    self.rttmonechoadminowntpsynctolpct = value
                    self.rttmonechoadminowntpsynctolpct.value_namespace = name_space
                    self.rttmonechoadminowntpsynctolpct.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminOWNTPSyncTolType"):
                    self.rttmonechoadminowntpsynctoltype = value
                    self.rttmonechoadminowntpsynctoltype.value_namespace = name_space
                    self.rttmonechoadminowntpsynctoltype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminPktDataRequestSize"):
                    self.rttmonechoadminpktdatarequestsize = value
                    self.rttmonechoadminpktdatarequestsize.value_namespace = name_space
                    self.rttmonechoadminpktdatarequestsize.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminPktDataResponseSize"):
                    self.rttmonechoadminpktdataresponsesize = value
                    self.rttmonechoadminpktdataresponsesize.value_namespace = name_space
                    self.rttmonechoadminpktdataresponsesize.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminPrecision"):
                    self.rttmonechoadminprecision = value
                    self.rttmonechoadminprecision.value_namespace = name_space
                    self.rttmonechoadminprecision.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminProbePakPriority"):
                    self.rttmonechoadminprobepakpriority = value
                    self.rttmonechoadminprobepakpriority.value_namespace = name_space
                    self.rttmonechoadminprobepakpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminProtocol"):
                    self.rttmonechoadminprotocol = value
                    self.rttmonechoadminprotocol.value_namespace = name_space
                    self.rttmonechoadminprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminProxy"):
                    self.rttmonechoadminproxy = value
                    self.rttmonechoadminproxy.value_namespace = name_space
                    self.rttmonechoadminproxy.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminReserveDsp"):
                    self.rttmonechoadminreservedsp = value
                    self.rttmonechoadminreservedsp.value_namespace = name_space
                    self.rttmonechoadminreservedsp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSourceAddress"):
                    self.rttmonechoadminsourceaddress = value
                    self.rttmonechoadminsourceaddress.value_namespace = name_space
                    self.rttmonechoadminsourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSourceMacAddress"):
                    self.rttmonechoadminsourcemacaddress = value
                    self.rttmonechoadminsourcemacaddress.value_namespace = name_space
                    self.rttmonechoadminsourcemacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSourceMPID"):
                    self.rttmonechoadminsourcempid = value
                    self.rttmonechoadminsourcempid.value_namespace = name_space
                    self.rttmonechoadminsourcempid.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSourcePort"):
                    self.rttmonechoadminsourceport = value
                    self.rttmonechoadminsourceport.value_namespace = name_space
                    self.rttmonechoadminsourceport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSourceVoicePort"):
                    self.rttmonechoadminsourcevoiceport = value
                    self.rttmonechoadminsourcevoiceport.value_namespace = name_space
                    self.rttmonechoadminsourcevoiceport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminSSM"):
                    self.rttmonechoadminssm = value
                    self.rttmonechoadminssm.value_namespace = name_space
                    self.rttmonechoadminssm.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminString1"):
                    self.rttmonechoadminstring1 = value
                    self.rttmonechoadminstring1.value_namespace = name_space
                    self.rttmonechoadminstring1.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminString2"):
                    self.rttmonechoadminstring2 = value
                    self.rttmonechoadminstring2.value_namespace = name_space
                    self.rttmonechoadminstring2.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminString3"):
                    self.rttmonechoadminstring3 = value
                    self.rttmonechoadminstring3.value_namespace = name_space
                    self.rttmonechoadminstring3.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminString4"):
                    self.rttmonechoadminstring4 = value
                    self.rttmonechoadminstring4.value_namespace = name_space
                    self.rttmonechoadminstring4.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminString5"):
                    self.rttmonechoadminstring5 = value
                    self.rttmonechoadminstring5.value_namespace = name_space
                    self.rttmonechoadminstring5.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetAddress"):
                    self.rttmonechoadmintargetaddress = value
                    self.rttmonechoadmintargetaddress.value_namespace = name_space
                    self.rttmonechoadmintargetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetAddressString"):
                    self.rttmonechoadmintargetaddressstring = value
                    self.rttmonechoadmintargetaddressstring.value_namespace = name_space
                    self.rttmonechoadmintargetaddressstring.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetDomainName"):
                    self.rttmonechoadmintargetdomainname = value
                    self.rttmonechoadmintargetdomainname.value_namespace = name_space
                    self.rttmonechoadmintargetdomainname.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetEVC"):
                    self.rttmonechoadmintargetevc = value
                    self.rttmonechoadmintargetevc.value_namespace = name_space
                    self.rttmonechoadmintargetevc.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetMacAddress"):
                    self.rttmonechoadmintargetmacaddress = value
                    self.rttmonechoadmintargetmacaddress.value_namespace = name_space
                    self.rttmonechoadmintargetmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetMEPPort"):
                    self.rttmonechoadmintargetmepport = value
                    self.rttmonechoadmintargetmepport.value_namespace = name_space
                    self.rttmonechoadmintargetmepport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetMPID"):
                    self.rttmonechoadmintargetmpid = value
                    self.rttmonechoadmintargetmpid.value_namespace = name_space
                    self.rttmonechoadmintargetmpid.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetPort"):
                    self.rttmonechoadmintargetport = value
                    self.rttmonechoadmintargetport.value_namespace = name_space
                    self.rttmonechoadmintargetport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTargetVLAN"):
                    self.rttmonechoadmintargetvlan = value
                    self.rttmonechoadmintargetvlan.value_namespace = name_space
                    self.rttmonechoadmintargetvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTOS"):
                    self.rttmonechoadmintos = value
                    self.rttmonechoadmintos.value_namespace = name_space
                    self.rttmonechoadmintos.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminTstampOptimization"):
                    self.rttmonechoadmintstampoptimization = value
                    self.rttmonechoadmintstampoptimization.value_namespace = name_space
                    self.rttmonechoadmintstampoptimization.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminURL"):
                    self.rttmonechoadminurl = value
                    self.rttmonechoadminurl.value_namespace = name_space
                    self.rttmonechoadminurl.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminVideoTrafficProfile"):
                    self.rttmonechoadminvideotrafficprofile = value
                    self.rttmonechoadminvideotrafficprofile.value_namespace = name_space
                    self.rttmonechoadminvideotrafficprofile.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoAdminVrfName"):
                    self.rttmonechoadminvrfname = value
                    self.rttmonechoadminvrfname.value_namespace = name_space
                    self.rttmonechoadminvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonechoadminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonechoadminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonEchoAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonEchoAdminEntry"):
                for c in self.rttmonechoadminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonechoadmintable.Rttmonechoadminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonechoadminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonEchoAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonfileioadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonfileioadmintable, self).__init__()

            self.yang_name = "rttMonFileIOAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonfileioadminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonfileioadmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonfileioadmintable, self).__setattr__(name, value)


        class Rttmonfileioadminentry(Entity):
            """
            A list of objects that define specific configuration for
            'fileIO' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonfileioadminaction
            
            	The File I/O action to be performed
            	**type**\:   :py:class:`Rttmonfileioadminaction <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry.Rttmonfileioadminaction>`
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminfilepath
            
            	The fully qualified file path that will be the target of the RTT operation.  This value must match one of the rttMonApplPreConfigedName entries
            	**type**\:  str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonfileioadminsize
            
            	The size of the file to write/read from the File Server
            	**type**\:   :py:class:`Rttmonfileioadminsize <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry.Rttmonfileioadminsize>`
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry, self).__init__()

                self.yang_name = "rttMonFileIOAdminEntry"
                self.yang_parent_name = "rttMonFileIOAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonfileioadminaction = YLeaf(YType.enumeration, "rttMonFileIOAdminAction")

                self.rttmonfileioadminfilepath = YLeaf(YType.str, "rttMonFileIOAdminFilePath")

                self.rttmonfileioadminsize = YLeaf(YType.enumeration, "rttMonFileIOAdminSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonfileioadminaction",
                                "rttmonfileioadminfilepath",
                                "rttmonfileioadminsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry, self).__setattr__(name, value)

            class Rttmonfileioadminaction(Enum):
                """
                Rttmonfileioadminaction

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
                Rttmonfileioadminsize

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


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonfileioadminaction.is_set or
                    self.rttmonfileioadminfilepath.is_set or
                    self.rttmonfileioadminsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonfileioadminaction.yfilter != YFilter.not_set or
                    self.rttmonfileioadminfilepath.yfilter != YFilter.not_set or
                    self.rttmonfileioadminsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonFileIOAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonFileIOAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonfileioadminaction.is_set or self.rttmonfileioadminaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonfileioadminaction.get_name_leafdata())
                if (self.rttmonfileioadminfilepath.is_set or self.rttmonfileioadminfilepath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonfileioadminfilepath.get_name_leafdata())
                if (self.rttmonfileioadminsize.is_set or self.rttmonfileioadminsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonfileioadminsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonFileIOAdminAction" or name == "rttMonFileIOAdminFilePath" or name == "rttMonFileIOAdminSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonFileIOAdminAction"):
                    self.rttmonfileioadminaction = value
                    self.rttmonfileioadminaction.value_namespace = name_space
                    self.rttmonfileioadminaction.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonFileIOAdminFilePath"):
                    self.rttmonfileioadminfilepath = value
                    self.rttmonfileioadminfilepath.value_namespace = name_space
                    self.rttmonfileioadminfilepath.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonFileIOAdminSize"):
                    self.rttmonfileioadminsize = value
                    self.rttmonfileioadminsize.value_namespace = name_space
                    self.rttmonfileioadminsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonfileioadminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonfileioadminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonFileIOAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonFileIOAdminEntry"):
                for c in self.rttmonfileioadminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonfileioadmintable.Rttmonfileioadminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonfileioadminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonFileIOAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonscriptadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonscriptadmintable.Rttmonscriptadminentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonscriptadmintable, self).__init__()

            self.yang_name = "rttMonScriptAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonscriptadminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonscriptadmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonscriptadmintable, self).__setattr__(name, value)


        class Rttmonscriptadminentry(Entity):
            """
            A list of objects that define specific configuration for
            'script' RttMonRttType conceptual Rtt control rows.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonscriptadmincmdlineparams
            
            	This will be the actual command line parameters passed to the rttMonScriptAdminName when being executed
            	**type**\:  str
            
            	**status**\: obsolete
            
            .. attribute:: rttmonscriptadminname
            
            	This will be the Name of the Script that will be used to generate RTT operations.    This object must match one of the  rttMonApplPreConfigedName entries
            	**type**\:  str
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonscriptadmintable.Rttmonscriptadminentry, self).__init__()

                self.yang_name = "rttMonScriptAdminEntry"
                self.yang_parent_name = "rttMonScriptAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonscriptadmincmdlineparams = YLeaf(YType.str, "rttMonScriptAdminCmdLineParams")

                self.rttmonscriptadminname = YLeaf(YType.str, "rttMonScriptAdminName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonscriptadmincmdlineparams",
                                "rttmonscriptadminname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonscriptadmintable.Rttmonscriptadminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonscriptadmintable.Rttmonscriptadminentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonscriptadmincmdlineparams.is_set or
                    self.rttmonscriptadminname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonscriptadmincmdlineparams.yfilter != YFilter.not_set or
                    self.rttmonscriptadminname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonScriptAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonScriptAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonscriptadmincmdlineparams.is_set or self.rttmonscriptadmincmdlineparams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscriptadmincmdlineparams.get_name_leafdata())
                if (self.rttmonscriptadminname.is_set or self.rttmonscriptadminname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonscriptadminname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonScriptAdminCmdLineParams" or name == "rttMonScriptAdminName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScriptAdminCmdLineParams"):
                    self.rttmonscriptadmincmdlineparams = value
                    self.rttmonscriptadmincmdlineparams.value_namespace = name_space
                    self.rttmonscriptadmincmdlineparams.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonScriptAdminName"):
                    self.rttmonscriptadminname = value
                    self.rttmonscriptadminname.value_namespace = name_space
                    self.rttmonscriptadminname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonscriptadminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonscriptadminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonScriptAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonScriptAdminEntry"):
                for c in self.rttmonscriptadminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonscriptadmintable.Rttmonscriptadminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonscriptadminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonScriptAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonreacttriggeradminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonreacttriggeradmintable, self).__init__()

            self.yang_name = "rttMonReactTriggerAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonreacttriggeradminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonreacttriggeradmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonreacttriggeradmintable, self).__setattr__(name, value)


        class Rttmonreacttriggeradminentry(Entity):
            """
            A list of objects that will be triggered when
            a reaction condition is violated.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonreacttriggeradminrttmonctrladminindex  <key>
            
            	This object points to a single conceptual Rtt control row.  If this row does not exist and this value is  triggered no action will result.  The conceptual Rtt control row will be triggered for the  rttMonCtrlOperRttLife length.  If this conceptual Rtt control row is already active, rttMonCtrlOperRttLife will not be updated, and its life will continue as previously  defined
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonreacttriggeradminstatus
            
            	This object is used to create Trigger entries
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rttmonreacttriggeroperstate
            
            	This object takes on the value active when its associated entry in the  rttMonReactTriggerAdminTable has been triggered.  When the associated entry in the rttMonReactTriggerAdminTable is not under a trigger state, this object will be pending.  When this object is in the active state this entry can not be retriggered
            	**type**\:   :py:class:`Rttmonreacttriggeroperstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry.Rttmonreacttriggeroperstate>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry, self).__init__()

                self.yang_name = "rttMonReactTriggerAdminEntry"
                self.yang_parent_name = "rttMonReactTriggerAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonreacttriggeradminrttmonctrladminindex = YLeaf(YType.int32, "rttMonReactTriggerAdminRttMonCtrlAdminIndex")

                self.rttmonreacttriggeradminstatus = YLeaf(YType.enumeration, "rttMonReactTriggerAdminStatus")

                self.rttmonreacttriggeroperstate = YLeaf(YType.enumeration, "rttMonReactTriggerOperState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonreacttriggeradminrttmonctrladminindex",
                                "rttmonreacttriggeradminstatus",
                                "rttmonreacttriggeroperstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry, self).__setattr__(name, value)

            class Rttmonreacttriggeroperstate(Enum):
                """
                Rttmonreacttriggeroperstate

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


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonreacttriggeradminrttmonctrladminindex.is_set or
                    self.rttmonreacttriggeradminstatus.is_set or
                    self.rttmonreacttriggeroperstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonreacttriggeradminrttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonreacttriggeradminstatus.yfilter != YFilter.not_set or
                    self.rttmonreacttriggeroperstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonReactTriggerAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonReactTriggerAdminRttMonCtrlAdminIndex='" + self.rttmonreacttriggeradminrttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonReactTriggerAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonreacttriggeradminrttmonctrladminindex.is_set or self.rttmonreacttriggeradminrttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreacttriggeradminrttmonctrladminindex.get_name_leafdata())
                if (self.rttmonreacttriggeradminstatus.is_set or self.rttmonreacttriggeradminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreacttriggeradminstatus.get_name_leafdata())
                if (self.rttmonreacttriggeroperstate.is_set or self.rttmonreacttriggeroperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreacttriggeroperstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonReactTriggerAdminRttMonCtrlAdminIndex" or name == "rttMonReactTriggerAdminStatus" or name == "rttMonReactTriggerOperState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactTriggerAdminRttMonCtrlAdminIndex"):
                    self.rttmonreacttriggeradminrttmonctrladminindex = value
                    self.rttmonreacttriggeradminrttmonctrladminindex.value_namespace = name_space
                    self.rttmonreacttriggeradminrttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactTriggerAdminStatus"):
                    self.rttmonreacttriggeradminstatus = value
                    self.rttmonreacttriggeradminstatus.value_namespace = name_space
                    self.rttmonreacttriggeradminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactTriggerOperState"):
                    self.rttmonreacttriggeroperstate = value
                    self.rttmonreacttriggeroperstate.value_namespace = name_space
                    self.rttmonreacttriggeroperstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonreacttriggeradminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonreacttriggeradminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonReactTriggerAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonReactTriggerAdminEntry"):
                for c in self.rttmonreacttriggeradminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonreacttriggeradmintable.Rttmonreacttriggeradminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonreacttriggeradminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonReactTriggerAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonechopathadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonechopathadmintable.Rttmonechopathadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonechopathadmintable, self).__init__()

            self.yang_name = "rttMonEchoPathAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonechopathadminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonechopathadmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonechopathadmintable, self).__setattr__(name, value)


        class Rttmonechopathadminentry(Entity):
            """
            A list of objects that define intermediate hop's IP Address.
            
            This entry can be added only if the rttMonCtrlAdminRttType is
            'echo'. The entry gets deleted when the corresponding RTR entry,
            which has an index of rttMonCtrlAdminIndex, is deleted.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonechopathadminhopindex  <key>
            
            	Uniquely identifies a row in the rttMonEchoPathAdminTable. This number represents the hop address number in a specific  ping path. All the indicies should start from 1 and must be  contiguous ie., entries should be  (say rttMonCtrlAdminIndex = 1)  1.1, 1.2, 1.3, they cannot be 1.1, 1.2, 1.4
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: rttmonechopathadminhopaddress
            
            	A string which specifies the address of an intermediate hop's IP Address for a RTT 'echo' operation
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonechopathadmintable.Rttmonechopathadminentry, self).__init__()

                self.yang_name = "rttMonEchoPathAdminEntry"
                self.yang_parent_name = "rttMonEchoPathAdminTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonechopathadminhopindex = YLeaf(YType.int32, "rttMonEchoPathAdminHopIndex")

                self.rttmonechopathadminhopaddress = YLeaf(YType.str, "rttMonEchoPathAdminHopAddress")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonechopathadminhopindex",
                                "rttmonechopathadminhopaddress") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonechopathadmintable.Rttmonechopathadminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonechopathadmintable.Rttmonechopathadminentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonechopathadminhopindex.is_set or
                    self.rttmonechopathadminhopaddress.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonechopathadminhopindex.yfilter != YFilter.not_set or
                    self.rttmonechopathadminhopaddress.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonEchoPathAdminEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonEchoPathAdminHopIndex='" + self.rttmonechopathadminhopindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonEchoPathAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonechopathadminhopindex.is_set or self.rttmonechopathadminhopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechopathadminhopindex.get_name_leafdata())
                if (self.rttmonechopathadminhopaddress.is_set or self.rttmonechopathadminhopaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonechopathadminhopaddress.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonEchoPathAdminHopIndex" or name == "rttMonEchoPathAdminHopAddress"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoPathAdminHopIndex"):
                    self.rttmonechopathadminhopindex = value
                    self.rttmonechopathadminhopindex.value_namespace = name_space
                    self.rttmonechopathadminhopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonEchoPathAdminHopAddress"):
                    self.rttmonechopathadminhopaddress = value
                    self.rttmonechopathadminhopaddress.value_namespace = name_space
                    self.rttmonechopathadminhopaddress.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonechopathadminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonechopathadminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonEchoPathAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonEchoPathAdminEntry"):
                for c in self.rttmonechopathadminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonechopathadmintable.Rttmonechopathadminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonechopathadminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonEchoPathAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmongrpscheduleadminentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmongrpscheduleadmintable, self).__init__()

            self.yang_name = "rttMonGrpScheduleAdminTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmongrpscheduleadminentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmongrpscheduleadmintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmongrpscheduleadmintable, self).__setattr__(name, value)


        class Rttmongrpscheduleadminentry(Entity):
            """
            A list of objects that define a conceptual group scheduling
            control row.
            
            .. attribute:: rttmongrpscheduleadminindex  <key>
            
            	Uniquely identifies a row in the rttMonGrpScheduleAdminTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMonGrpScheduleAdminStatus object. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmongrpscheduleadminadd
            
            	Addition of members to an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are added to the existing group
            	**type**\:  bool
            
            .. attribute:: rttmongrpscheduleadminageout
            
            	This object specifies the ageout value of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminConceptRowAgeout object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  When this value is set to zero, the probes listed in rttMonGrpScheduleAdminProbes, will never ageout
            	**type**\:  int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadmindelete
            
            	Removal of members from an existing group will be allowed if this object is set to TRUE (1). The members, IDs of which are mentioned in rttMonGrpScheduleAdminProbes object are removed from the existing group
            	**type**\:  bool
            
            .. attribute:: rttmongrpscheduleadminfreqmax
            
            	Specifies the max duration between initiating each RTT operation for all the probes specified in the group.  If this is 0 and rttMonGrpScheduleAdminFreqMin is also 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfreqmin
            
            	Specifies the min duration between initiating each RTT operation for all the probes specified in the group.  The value of this object cannot be greater than the value of rttMonGrpScheduleAdminFreqMax.  If this is 0 and rttMonGrpScheduleAdminFreqMax is 0 then rttMonGrpScheduleAdminFrequency becomes the fixed frequency
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminfrequency
            
            	Specifies the duration between initiating each RTT operation for all the probes specified in the group.  The value of this object is only effective when both rttMonGrpScheduleAdminFreqMax and rttMonGrpScheduleAdminFreqMin  have zero values
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminlife
            
            	This object specifies the life of all the probes included in the object rttMonGrpScheduleAdminProbes, that are getting group scheduled. This value will be placed into rttMonScheduleAdminRttLife object for each of the probes listed in rttMonGrpScheduleAdminProbes when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the probes listed in rttMonGrpScheduleAdminProbes,  will not decrement. And thus the life time of the probes will never end
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminperiod
            
            	Specifies the time duration over which all the probes have to be scheduled
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminprobes
            
            	A string which holds the different probes which are to be group scheduled. The probes can be specified in the following forms. (a) Individual ID's with comma separated as 23,45,34. (b) Range form including hyphens with multiple ranges being     separated by a comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25.  Any whitespace in the string is considered an error. Duplicates and overlapping ranges as an example 1,2,3,2\-10 are considered fine. For a single range like 1\-20 the upper value (in this example 20) must be greater than lower value (1), otherwise it's treated as an error. The agent will not normalize the list e.g., it will not change 1,2,1\-10 or even 1,2,3,4,5,6.. to 1\-10
            	**type**\:  str
            
            	**length:** 0..200
            
            .. attribute:: rttmongrpscheduleadminreset
            
            	When this is set to true then all members of this group will be stopped and rescheduled using the previously set values of this group
            	**type**\:  bool
            
            .. attribute:: rttmongrpscheduleadminstarttime
            
            	This is the time in seconds after which the member probes of this group specified in rttMonGrpScheduleAdminProbes will transition to active state
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmongrpscheduleadminstatus
            
            	The status of the conceptual RTT group schedule control row.  In order for this object to become active, the following row objects must be defined\:  \- rttMonGrpScheduleAdminProbes  \- rttMonGrpScheduleAdminPeriod All other objects can assume default values.  The conceptual RTT group schedule control row objects cannot be modified once this conceptual RTT group schedule control row has been created. Once this object is in 'active' status, it cannot be set to 'notInService'. When this object moves to 'active' state it will schedule the probes of the rttMonCtrlAdminTable which had been created using 'createAndWait'.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the probes of the rttMonCtrlAdminTable, which had been group scheduled by it earlier, before destroying the RTT group schedule control row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry, self).__init__()

                self.yang_name = "rttMonGrpScheduleAdminEntry"
                self.yang_parent_name = "rttMonGrpScheduleAdminTable"

                self.rttmongrpscheduleadminindex = YLeaf(YType.int32, "rttMonGrpScheduleAdminIndex")

                self.rttmongrpscheduleadminadd = YLeaf(YType.boolean, "rttMonGrpScheduleAdminAdd")

                self.rttmongrpscheduleadminageout = YLeaf(YType.int32, "rttMonGrpScheduleAdminAgeout")

                self.rttmongrpscheduleadmindelete = YLeaf(YType.boolean, "rttMonGrpScheduleAdminDelete")

                self.rttmongrpscheduleadminfreqmax = YLeaf(YType.int32, "rttMonGrpScheduleAdminFreqMax")

                self.rttmongrpscheduleadminfreqmin = YLeaf(YType.int32, "rttMonGrpScheduleAdminFreqMin")

                self.rttmongrpscheduleadminfrequency = YLeaf(YType.int32, "rttMonGrpScheduleAdminFrequency")

                self.rttmongrpscheduleadminlife = YLeaf(YType.int32, "rttMonGrpScheduleAdminLife")

                self.rttmongrpscheduleadminperiod = YLeaf(YType.int32, "rttMonGrpScheduleAdminPeriod")

                self.rttmongrpscheduleadminprobes = YLeaf(YType.str, "rttMonGrpScheduleAdminProbes")

                self.rttmongrpscheduleadminreset = YLeaf(YType.boolean, "rttMonGrpScheduleAdminReset")

                self.rttmongrpscheduleadminstarttime = YLeaf(YType.int32, "rttMonGrpScheduleAdminStartTime")

                self.rttmongrpscheduleadminstatus = YLeaf(YType.enumeration, "rttMonGrpScheduleAdminStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmongrpscheduleadminindex",
                                "rttmongrpscheduleadminadd",
                                "rttmongrpscheduleadminageout",
                                "rttmongrpscheduleadmindelete",
                                "rttmongrpscheduleadminfreqmax",
                                "rttmongrpscheduleadminfreqmin",
                                "rttmongrpscheduleadminfrequency",
                                "rttmongrpscheduleadminlife",
                                "rttmongrpscheduleadminperiod",
                                "rttmongrpscheduleadminprobes",
                                "rttmongrpscheduleadminreset",
                                "rttmongrpscheduleadminstarttime",
                                "rttmongrpscheduleadminstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmongrpscheduleadminindex.is_set or
                    self.rttmongrpscheduleadminadd.is_set or
                    self.rttmongrpscheduleadminageout.is_set or
                    self.rttmongrpscheduleadmindelete.is_set or
                    self.rttmongrpscheduleadminfreqmax.is_set or
                    self.rttmongrpscheduleadminfreqmin.is_set or
                    self.rttmongrpscheduleadminfrequency.is_set or
                    self.rttmongrpscheduleadminlife.is_set or
                    self.rttmongrpscheduleadminperiod.is_set or
                    self.rttmongrpscheduleadminprobes.is_set or
                    self.rttmongrpscheduleadminreset.is_set or
                    self.rttmongrpscheduleadminstarttime.is_set or
                    self.rttmongrpscheduleadminstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminindex.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminadd.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminageout.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadmindelete.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminfreqmax.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminfreqmin.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminfrequency.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminlife.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminperiod.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminprobes.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminreset.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminstarttime.yfilter != YFilter.not_set or
                    self.rttmongrpscheduleadminstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonGrpScheduleAdminEntry" + "[rttMonGrpScheduleAdminIndex='" + self.rttmongrpscheduleadminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonGrpScheduleAdminTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmongrpscheduleadminindex.is_set or self.rttmongrpscheduleadminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminindex.get_name_leafdata())
                if (self.rttmongrpscheduleadminadd.is_set or self.rttmongrpscheduleadminadd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminadd.get_name_leafdata())
                if (self.rttmongrpscheduleadminageout.is_set or self.rttmongrpscheduleadminageout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminageout.get_name_leafdata())
                if (self.rttmongrpscheduleadmindelete.is_set or self.rttmongrpscheduleadmindelete.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadmindelete.get_name_leafdata())
                if (self.rttmongrpscheduleadminfreqmax.is_set or self.rttmongrpscheduleadminfreqmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminfreqmax.get_name_leafdata())
                if (self.rttmongrpscheduleadminfreqmin.is_set or self.rttmongrpscheduleadminfreqmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminfreqmin.get_name_leafdata())
                if (self.rttmongrpscheduleadminfrequency.is_set or self.rttmongrpscheduleadminfrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminfrequency.get_name_leafdata())
                if (self.rttmongrpscheduleadminlife.is_set or self.rttmongrpscheduleadminlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminlife.get_name_leafdata())
                if (self.rttmongrpscheduleadminperiod.is_set or self.rttmongrpscheduleadminperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminperiod.get_name_leafdata())
                if (self.rttmongrpscheduleadminprobes.is_set or self.rttmongrpscheduleadminprobes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminprobes.get_name_leafdata())
                if (self.rttmongrpscheduleadminreset.is_set or self.rttmongrpscheduleadminreset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminreset.get_name_leafdata())
                if (self.rttmongrpscheduleadminstarttime.is_set or self.rttmongrpscheduleadminstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminstarttime.get_name_leafdata())
                if (self.rttmongrpscheduleadminstatus.is_set or self.rttmongrpscheduleadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongrpscheduleadminstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonGrpScheduleAdminIndex" or name == "rttMonGrpScheduleAdminAdd" or name == "rttMonGrpScheduleAdminAgeout" or name == "rttMonGrpScheduleAdminDelete" or name == "rttMonGrpScheduleAdminFreqMax" or name == "rttMonGrpScheduleAdminFreqMin" or name == "rttMonGrpScheduleAdminFrequency" or name == "rttMonGrpScheduleAdminLife" or name == "rttMonGrpScheduleAdminPeriod" or name == "rttMonGrpScheduleAdminProbes" or name == "rttMonGrpScheduleAdminReset" or name == "rttMonGrpScheduleAdminStartTime" or name == "rttMonGrpScheduleAdminStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonGrpScheduleAdminIndex"):
                    self.rttmongrpscheduleadminindex = value
                    self.rttmongrpscheduleadminindex.value_namespace = name_space
                    self.rttmongrpscheduleadminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminAdd"):
                    self.rttmongrpscheduleadminadd = value
                    self.rttmongrpscheduleadminadd.value_namespace = name_space
                    self.rttmongrpscheduleadminadd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminAgeout"):
                    self.rttmongrpscheduleadminageout = value
                    self.rttmongrpscheduleadminageout.value_namespace = name_space
                    self.rttmongrpscheduleadminageout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminDelete"):
                    self.rttmongrpscheduleadmindelete = value
                    self.rttmongrpscheduleadmindelete.value_namespace = name_space
                    self.rttmongrpscheduleadmindelete.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminFreqMax"):
                    self.rttmongrpscheduleadminfreqmax = value
                    self.rttmongrpscheduleadminfreqmax.value_namespace = name_space
                    self.rttmongrpscheduleadminfreqmax.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminFreqMin"):
                    self.rttmongrpscheduleadminfreqmin = value
                    self.rttmongrpscheduleadminfreqmin.value_namespace = name_space
                    self.rttmongrpscheduleadminfreqmin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminFrequency"):
                    self.rttmongrpscheduleadminfrequency = value
                    self.rttmongrpscheduleadminfrequency.value_namespace = name_space
                    self.rttmongrpscheduleadminfrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminLife"):
                    self.rttmongrpscheduleadminlife = value
                    self.rttmongrpscheduleadminlife.value_namespace = name_space
                    self.rttmongrpscheduleadminlife.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminPeriod"):
                    self.rttmongrpscheduleadminperiod = value
                    self.rttmongrpscheduleadminperiod.value_namespace = name_space
                    self.rttmongrpscheduleadminperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminProbes"):
                    self.rttmongrpscheduleadminprobes = value
                    self.rttmongrpscheduleadminprobes.value_namespace = name_space
                    self.rttmongrpscheduleadminprobes.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminReset"):
                    self.rttmongrpscheduleadminreset = value
                    self.rttmongrpscheduleadminreset.value_namespace = name_space
                    self.rttmongrpscheduleadminreset.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminStartTime"):
                    self.rttmongrpscheduleadminstarttime = value
                    self.rttmongrpscheduleadminstarttime.value_namespace = name_space
                    self.rttmongrpscheduleadminstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGrpScheduleAdminStatus"):
                    self.rttmongrpscheduleadminstatus = value
                    self.rttmongrpscheduleadminstatus.value_namespace = name_space
                    self.rttmongrpscheduleadminstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmongrpscheduleadminentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmongrpscheduleadminentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonGrpScheduleAdminTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonGrpScheduleAdminEntry"):
                for c in self.rttmongrpscheduleadminentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmongrpscheduleadmintable.Rttmongrpscheduleadminentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmongrpscheduleadminentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonGrpScheduleAdminEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmplsvpnmonctrlentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmplsvpnmonctrltable, self).__init__()

            self.yang_name = "rttMplsVpnMonCtrlTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmplsvpnmonctrlentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmplsvpnmonctrltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmplsvpnmonctrltable, self).__setattr__(name, value)


        class Rttmplsvpnmonctrlentry(Entity):
            """
            A base list of objects that define a conceptual Auto SAA L3
            MPLS VPN control row.
            
            .. attribute:: rttmplsvpnmonctrlindex  <key>
            
            	Uniquely identifies a row in the rttMplsVpnMonCtrlTable.  This is a pseudo\-random number selected by the management station when creating a row via the rttMplsVpnMonCtrlStatus object.  If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmplsvpnmonctrldelscanfactor
            
            	Specifies the frequency at which the automatic PE deletion should take place.  This object specifies the number of times of rttMonMplslmCtrlScanInterval (rttMplsVpnMonCtrlDelScanFactor \* rttMplsVpnMonCtrlScanInterval) to wait before removing the PEs. This object doesn't directly specify the explicit value to wait before removing the PEs that were down.  If this object set 0 the entries will never removed
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmplsvpnmonctrlexp
            
            	This object represents the EXP value that needs to be put as precedence bit of an IP header
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: rttmplsvpnmonctrllpd
            
            	When set to true, this implies that LPD (LSP Path Discovery) is enabled for this row.  The Auto SAA L3 MPLS VPN will find all the paths to each of the PE's and configure RTT operation with rttMonCtrlAdminRttType value as 'lspGroup'. The 'lspGroup' probe will walk through the list of set of information that uniquely identifies a path and send the LSP echo requests across them. All these LSP echo requests sent for 1st path, 2nd path etc. can be thought of as 'single probes' sent as a part of 'lspGroup'. These single probes will of type 'rttMplsVpnMonCtrlRttType'.  'lspGroup' probe is a superset of individual probes that will test multiple paths. For example Suppose there are 10 paths to the target. One 'lspGroup' probe will be created which will store all the information related to uniquely identify the 10 paths. When the 'lspGroup' probe will run it will sweep through the set of information for 1st path, 2nd path, 3rd path and so on till it has tested all the paths
            	**type**\:  bool
            
            .. attribute:: rttmplsvpnmonctrllpdcomptime
            
            	The completion time of the LSP Path Discovery for the entire set of PEs which are discovered for this Auto SAA.  This object will be applicable only when LSP Path Discovery is enabled for this row
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmonctrllpdgrplist
            
            	This object holds the list of LPD Group IDs that are created for this Auto SAA L3 MPLS VPN row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  The LPD Groups will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\:  str
            
            .. attribute:: rttmplsvpnmonctrlprobelist
            
            	This object holds the list of probes ID's that are created by the Auto SAA L3 MPLS VPN.  The probes will be specified in the following form. (a) Individual ID's with comma separated as 1,5,3. (b) Range form including hyphens with multiple ranges being     separated by comma as 1\-10,12\-34. (c) Mix of the above two forms as 1,2,4\-10,12,15,19\-25
            	**type**\:  str
            
            .. attribute:: rttmplsvpnmonctrlrequestsize
            
            	This object represents the native payload size that needs to be put on the packet.  This value will be configured as rttMonEchoAdminPktDataRequestSize for all the RTT operations configured by the current Auto SAA L3 MPLS VPN.  The minimum request size for jitter probe is 16. The maximum for jitter probe is 1500. The default request size is 32 for jitter probe.  For echo and pathEcho default request size is 28. The minimum request size for echo and pathEcho is 28 bytes
            	**type**\:  int
            
            	**range:** 0..16384
            
            	**units**\: octets
            
            .. attribute:: rttmplsvpnmonctrlrtttype
            
            	The type of RTT operation to be performed for Auto SAA L3 MPLS VPN.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  This value must be set before setting any other parameter configuration of an Auto SAA L3 MPLS VPN
            	**type**\:   :py:class:`Rttmplsvpnmonrtttype <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmplsvpnmonrtttype>`
            
            .. attribute:: rttmplsvpnmonctrlscaninterval
            
            	Specifies the frequency at which the automatic PE addition should take place if there is any for an Auto SAA L3 MPLS VPN.  New RTT operations corresponding to the new PEs discovered will be created and scheduled.  The default value for this object is 4 hours. The maximum value supported is 49 days
            	**type**\:  int
            
            	**range:** 1..70560
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmonctrlstatus
            
            	The status of the conceptual Auto SAA L3 MPLS VPN control row.  In order for this object to become active rttMplsVpnMonCtrlRttType,  rttMplsVpnMonCtrlVrfName and  rttMplsVpnMonSchedulePeriod objects must be defined. All other objects can assume default values.  If the object is set to 'createAndGo' rttMplsVpnMonCtrlRttType, rttMplsVpnMonCtrlVrfName and rttMplsVpnMonSchedulePeriod needs to be set along with rttMplsVpnMonCtrlStatus.  If the object is set to 'createAndWait' rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName needs to be set along with rttMplsVpnMonCtrlStatus. rttMplsVpnMonSchedulePeriod needs to be specified before setting rttMplsVpnMonCtrlStatus to 'active'.  The following objects cannot be modified after creating the Auto SAA L3 MPLS VPN conceptual row.   \- rttMplsVpnMonCtrlRttType  \- rttMplsVpnMonCtrlVrfName  The following objects can be modified even after creating the Auto SAA L3 MPLS VPN conceptual row by setting this object to 'notInService'   \- All other writable objects in rttMplsVpnMonCtrlTable except    rttMplsVpnMonCtrlRttType and rttMplsVpnMonCtrlVrfName.  \- Objects in the rttMplsVpnMonTypeTable.  \- Objects in the rttMplsVpnMonScheduleTable.  The following objects can be modified as needed without setting this object to 'notInService' even after creating the Auto SAA L3 MPLS VPN conceptual row.   \- Objects in rttMplsVpnMonReactTable.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop and destroy all the probes created by this Auto SAA L3 MPLS VPN before destroying Auto SAA L3 MPLS VPN control row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rttmplsvpnmonctrlstoragetype
            
            	The storage type of this conceptual row. When set to 'nonVolatile', this entry will be shown in 'show running' command and can be saved into Non\-volatile memory.  By Default the entry will not be saved into Non\-volatile memory.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: rttmplsvpnmonctrltag
            
            	A string which is used by a managing application to identify the RTT target.  This string will be configured as rttMonCtrlAdminTag for all the operations configured by this Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminTag in RTT operation
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: rttmplsvpnmonctrlthreshold
            
            	This object defines an administrative threshold limit.  This value will be configured as rttMonCtrlAdminThreshold for all the operations that will be configured by the current Auto SAA L3 MPLS VPN.  The usage of this value in Auto SAA L3 MPLS VPN is same as rttMonCtrlAdminThreshold
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrltimeout
            
            	Specifies the duration to wait for a RTT operation configured automatically by the Auto SAA L3 MPLS VPN to complete.   The value of this object cannot be set to a value which would specify a duration exceeding rttMplsVpnMonScheduleFrequency.  The usage of this value in Auto SAA L3 MPLS VPN is similar to rttMonCtrlAdminTimeout
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmonctrlverifydata
            
            	When set to true, the resulting data in each RTT operation created by the current Auto SAA L3 MPLS VPN is compared with the expected data. This includes checking header information (if possible) and exact packet size.  Any mismatch will be recorded in the rttMonStatsCollectVerifyErrors object of each RTT operation created by the current Auto SAA L3 MPLS VPN
            	**type**\:  bool
            
            .. attribute:: rttmplsvpnmonctrlvrfname
            
            	This field is used to specify the VPN name for which the Auto SAA L3 MPLS VPN RTT operation will be used.  This value must be set in the same PDU of rttMplsVpnMonCtrlStatus.  The Auto SAA L3 MPLS VPN will find the PEs participating in this VPN and configure RTT operation corresponding to value specified in rttMplsVpnMonCtrlRttType.  If the VPN corresponds to the value configured for this object doesn't exist 'inconsistentValue' error will be returned.  The value 'saa\-vrf\-all' has a special meaning. When this object is set to 'saa\-vrf\-all', all the VPNs in the PE will be discovered and Auto SAA L3 MPLS VPN will configure RTT operations corresponding to all these PEs with the value specified in rttMplsVpnMonCtrlRttType as type for those operations.  So, the user should avoid using this string for a particular VPN name when using this feature in order to avoid ambiguity
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: rttmplsvpnmonreactactiontype
            
            	The value corresponding to this object will be applied as rttMonReactAdminActionType of individual probes created by this Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactActionType of individual probes created by this Auto SAA L3 MPLS VPN
            	**type**\:   :py:class:`Rttmplsvpnmonreactactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactactiontype>`
            
            .. attribute:: rttmplsvpnmonreactconnectionenable
            
            	The value set for this will be applied as rttMonReactAdminConnectionEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'connectionLoss(8)'
            	**type**\:  bool
            
            .. attribute:: rttmplsvpnmonreactlpdnotifytype
            
            	This object specifies the type of LPD notifications to be generated for the current Auto SAA L3 MPLS VPN control row.  This object will be applicable only when LSP Path Discovery is enabled for this row.  There are two types of notifications supported for the LPD \- (a) rttMonLpdDiscoveryNotification \- This notification will     be sent on the failure of LSP Path Discovery to the     particular PE. Reversal of the failure will also result in     sending the notification. (b) rttMonLpdGrpStatusNotification \- Individual probes in an LPD     group will not generate notifications independently but will     be generating dependent on the state of the group. Any     individual probe can initiate the generation of a     notification, dependent on the state of the group.     Notifications are only generated if the failure/restoration     of an individual probe causes the state of the group to     change.  The Value 'none' will not cause any notifications to be sent.  The Value 'lpdPathDiscovery' will cause (a) to be sent.  The Value 'lpdGroupStatus' will cause (b) to be sent.  The Value 'lpdAll' will cause both (a) and (b) to sent depending on the failure conditions
            	**type**\:   :py:class:`Rttmplsvpnmonreactlpdnotifytype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactlpdnotifytype>`
            
            .. attribute:: rttmplsvpnmonreactlpdretrycount
            
            	This object value specifies the number of attempts to be performed before declaring the path as 'down'. Each 'single probe' which is part of 'lspGroup' probe will be retried these many times before marking it as 'down'.  This object will be applicable only when LSP Path Discovery is enabled for this row.    \- When rttMplsVpnMonTypeSecFreqType is not configured, the     failure count will be incremented at the next cycle of     'lspGroup' probe at interval's of     rttMplsVpnMonScheduleFrequency value.      For example\: Assume there are 10 paths discovered and on     the first run of the 'lspGroup' probe first two paths failed     and rest passed. On the second run all the probes will be      run again. The probes 1 and 2 will be retried till the     rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured.    \- When rttMplsVpnMonTypeSecFreqType value is anything other     than 'none', the retry will happen for the failed probes at     the rttMplsVpnMonTypeSecFreqValue and only the failed     probes will be retried.      For example\: Assume there are 10 paths discovered and on the     first run of the 'lspGroup' probe first two paths failed and     rest passed. The secondary frequency will be applied to the     failed probes. At secondary frequency interval the first two     probes will be run again. The probes 1 and 2 will be retried     till the rttMplsVpnMonReactLpdRetryCount value, and     then marked as 'down' and rttMonLpdGrpStatusNotification      will be sent if configured
            	**type**\:  int
            
            	**range:** 1..16
            
            	**units**\: attempts
            
            .. attribute:: rttmplsvpnmonreactthresholdcount
            
            	This object value will be applied as rttMonReactAdminThresholdCount for individual probes created by the Auto SAA L3 MPLS VPN.  This object value will be applied as rttMonReactThresholdCountX for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: rttmplsvpnmonreactthresholdtype
            
            	The value corresponding to this object will be applied as rttMonReactAdminThresholdType for individual probes created by the Auto SAA L3 MPLS VPN.  The value corresponding to this object will be applied as rttMonReactThresholdType for individual probes created by the Auto SAA L3 MPLS VPN
            	**type**\:   :py:class:`Rttmplsvpnmonreactthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmonreactthresholdtype>`
            
            .. attribute:: rttmplsvpnmonreacttimeoutenable
            
            	The value set for this will be applied as rttMonReactAdminTimeoutEnable for individual probes created by the Auto SAA L3 MPLS VPN.  When this object is set to true, rttMonReactVar for individual probes created by the Auto SAA L3 MPLS VPN will be set to 'timeout(7)'
            	**type**\:  bool
            
            .. attribute:: rttmplsvpnmonschedulefrequency
            
            	Specifies the duration between initiating each RTT operation configured by the Auto SAA L3 MPLS VPN.  This object cannot be set to a value which would be a shorter duration than rttMplsVpnMonCtrlTimeout.  The usage of this value in RTT operation is same as rttMonCtrlAdminFrequency
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonscheduleperiod
            
            	Specifies the time duration over which all the probes created by the current Auto SAA L3 MPLS VPN have to be scheduled.  This object must be set first before setting rttMplsVpnMonScheduleRttStartTime
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmonschedulerttstarttime
            
            	This is the time when this conceptual row will activate. rttMplsVpnMonSchedulePeriod object must be specified before setting this object.  This is the value of MIB\-II's sysUpTime in the future. When sysUpTime equals this value this object will cause the activation of a conceptual Auto SAA L3 MPLS VPN row.  When an agent has the capability to determine date and time, the agent should store this object as DateAndTime. This allows the agent to be able to activate conceptual Auto SAA L3 MPLS VPN row at the intended time.  If this object has value as 1, this means start the operation now itself. Value of 0 puts the operation in pending state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmplsvpnmontypedestport
            
            	This object represents the target's port number to which the packets need to be sent.  This value will be configured as target port for all the operations that is going to be configured   The usage of this value is same as rttMonEchoAdminTargetPort in RTT operation. This object is applicable to jitter type.  If this object is not being set random port will be used as destination port
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: rttmplsvpnmontypeinterval
            
            	This value represents the inter\-packet delay between packets and is in milliseconds. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminInterval
            	**type**\:  int
            
            	**range:** 1..60000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechointerval
            
            	This object specifies the send interval between LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\:  int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdechonullshim
            
            	This object specifies if the explicit\-null label is added to LSP echo requests which are sent while performing the LSP Path Discovery.  If set to TRUE all the probes configured as part of this control row will send the LSP echo requests with the explicit\-null label added
            	**type**\:  bool
            
            .. attribute:: rttmplsvpnmontypelpdechotimeout
            
            	This object specifies the timeout value for the LSP echo requests which are sent while performing the LSP Path  Discovery
            	**type**\:  int
            
            	**range:** 0..604800000
            
            	**units**\: milliseconds
            
            .. attribute:: rttmplsvpnmontypelpdmaxsessions
            
            	This object represents the number of concurrent path discovery requests that will be active at one time per MPLS VPN control row. This object is meant for reducing the time for discovery of all the paths to the target in a large customer network. However its value should be chosen such that it does not cause any performance impact.  Note\: If the customer network has low end routers in the Core it is recommended to keep this value low
            	**type**\:  int
            
            	**range:** 1..15
            
            .. attribute:: rttmplsvpnmontypelpdscanperiod
            
            	This object specifies the scan time for the completion of LSP Path Discovery for all the PEs discovered for this control row. If the scan period is exceeded on completion of the LSP Path Discovery for all the PEs, the next discovery will start immediately else it will wait till expiry of scan period.  For example\: If the value is set to 30 minutes then on start of the LSP Path Discovery a timestamp will be taken say T1. At the end of the tree trace discovery one more timestamp will be taken again say T2. If (T2\-T1) is greater than 30, the next discovery will start immediately else next discovery  will wait for [30 \- (T2\-T1)].  Note\: If the object is set to a special value of '0', it will force immediate start of the next discovery on all neighbours without any delay
            	**type**\:  int
            
            	**range:** 0..7200
            
            	**units**\: minutes
            
            .. attribute:: rttmplsvpnmontypelpdsesstimeout
            
            	This object specifies the maximum allowed duration of a particular tree trace request.  If no response is received in configured time the request will be considered a failure
            	**type**\:  int
            
            	**range:** 1..900
            
            	**units**\: seconds
            
            .. attribute:: rttmplsvpnmontypelpdstathours
            
            	The maximum number of hours of data to be kept per LPD group. The LPD group statistics will be kept in an hourly bucket. At the maximum there can be two buckets. The value of 'one' is not advisable because the group will close and immediately be deleted before the network management station will have the opportunity to retrieve the statistics.  The value used in the rttMplsVpnLpdGroupStatsTable to uniquely identify this group is the rttMonStatsCaptureStartTimeIndex.  Note\: When this object is set to the value of '0' all rttMplsVpnLpdGroupStatsTable data capturing will be shut off
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: rttmplsvpnmontypelspreplydscp
            
            	This object specifies the DSCP value to be set in the IP header of the LSP echo reply packet. The value of this object will be in range of DiffServ codepoint values between 0 to 63.  Note\: This object cannot be set to value of 255. This default value specifies that DSCP is not set for this row
            	**type**\:  int
            
            	**range:** 0..63 \| 255..None
            
            .. attribute:: rttmplsvpnmontypelspreplymode
            
            	This object specifies the reply mode for the LSP Echo requests originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho
            	**type**\:   :py:class:`Rttmonlsppingreplymode <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonlsppingreplymode>`
            
            .. attribute:: rttmplsvpnmontypelspselector
            
            	A string which specifies the address of the local host (127.X.X.X).  This object will be used as lsp\-selector in MPLS RTT operations configured by the Auto SAA L3 MPLS VPN.  When LSP Path Discovery is enabled for the row, this object will be used to indicate the base LSP selector value to be used in the LSP Path Discovery.  This value of this object is significant in MPLS load balancing scenario. This value will be used as one of the parameter in that load balancing
            	**type**\:  str
            
            .. attribute:: rttmplsvpnmontypelspttl
            
            	This object represents the TTL setting for MPLS echo request packets originated by the operations configured by the Auto SAA L3 MPLS VPN.  This object is currently used by echo and pathEcho.  For 'echo' the default TTL will be set to 255. For 'pathEcho' the default will be set to 30.  Note\: This object cannot be set to the value of 0. The default value of 0 signifies the default TTL values will be used for 'echo' and 'pathEcho'
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rttmplsvpnmontypenumpackets
            
            	This value represents the number of packets that need to be transmitted. This value is currently used for Jitter probe. This object is applicable to jitter probe only.  The usage of this value in RTT operation is same as rttMonEchoAdminNumPackets
            	**type**\:  int
            
            	**range:** 1..60000
            
            .. attribute:: rttmplsvpnmontypesecfreqtype
            
            	This object specifies the reaction type for which the rttMplsVpnMonTypeSecFreqValue should be applied.  The Value 'timeout' will cause secondary frequency to be set for frequency on timeout condition.  The Value 'connectionLoss' will cause secondary frequency to be set for frequency on connectionloss condition.  The Value 'both' will cause secondary frequency to be set for frequency on either of timeout/connectionloss condition.  Notifications must be configured on corresponding reaction type in order to rttMplsVpnMonTypeSecFreqValue get effect.  When LSP Path Discovery is enabled for this row the following rttMplsVpnMonReactLpdNotifyType notifications must be configured in order to rttMplsVpnMonTypeSecFreqValue get effect.   \- 'lpdGroupStatus' or 'lpdAll'.  Since the Frequency of the operation changes the stats will be collected in new bucket.  If any of the reaction type (timeout/connectionLoss) occurred for an operation configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the frequency of the operation will be changed to rttMplsVpnMonTypeSecFreqValue.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss).   2) A notification is configured for the same reaction type   (timeout/connectionLoss).  When LSP Path Discovery is enabled for this row, if any of the reaction type (timeout/connectionLoss) occurred for 'single probes' configured by this Auto SAA L3 MPLS VPN and the following conditions are satisfied, the secondary frequency rttMplsVpnMonTypeSecFreqValue will be applied to the 'lspGroup' probe.    1) rttMplsVpnMonTypeSecFreqType is set for a reaction type   (timeout/connectionLoss/both).   2) rttMplsVpnMonReactLpdNotifyType object must be set to   value of 'lpdGroupStatus' or 'lpdAll'.  The frequency of the individual operations will be restored to original frequency once the trap is sent
            	**type**\:   :py:class:`Rttmplsvpnmontypesecfreqtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry.Rttmplsvpnmontypesecfreqtype>`
            
            .. attribute:: rttmplsvpnmontypesecfreqvalue
            
            	This object represents the value that needs to be applied to secondary frequency of individual RTT operations configured by Auto SAA L3 MPLS VPN.  Setting rttMplsVpnMonTypeSecFreqValue without setting rttMplsVpnMonTypeSecFreqType will not have any effect
            	**type**\:  int
            
            	**range:** 1..604800
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry, self).__init__()

                self.yang_name = "rttMplsVpnMonCtrlEntry"
                self.yang_parent_name = "rttMplsVpnMonCtrlTable"

                self.rttmplsvpnmonctrlindex = YLeaf(YType.int32, "rttMplsVpnMonCtrlIndex")

                self.rttmplsvpnmonctrldelscanfactor = YLeaf(YType.int32, "rttMplsVpnMonCtrlDelScanFactor")

                self.rttmplsvpnmonctrlexp = YLeaf(YType.int32, "rttMplsVpnMonCtrlEXP")

                self.rttmplsvpnmonctrllpd = YLeaf(YType.boolean, "rttMplsVpnMonCtrlLpd")

                self.rttmplsvpnmonctrllpdcomptime = YLeaf(YType.int32, "rttMplsVpnMonCtrlLpdCompTime")

                self.rttmplsvpnmonctrllpdgrplist = YLeaf(YType.str, "rttMplsVpnMonCtrlLpdGrpList")

                self.rttmplsvpnmonctrlprobelist = YLeaf(YType.str, "rttMplsVpnMonCtrlProbeList")

                self.rttmplsvpnmonctrlrequestsize = YLeaf(YType.int32, "rttMplsVpnMonCtrlRequestSize")

                self.rttmplsvpnmonctrlrtttype = YLeaf(YType.enumeration, "rttMplsVpnMonCtrlRttType")

                self.rttmplsvpnmonctrlscaninterval = YLeaf(YType.int32, "rttMplsVpnMonCtrlScanInterval")

                self.rttmplsvpnmonctrlstatus = YLeaf(YType.enumeration, "rttMplsVpnMonCtrlStatus")

                self.rttmplsvpnmonctrlstoragetype = YLeaf(YType.enumeration, "rttMplsVpnMonCtrlStorageType")

                self.rttmplsvpnmonctrltag = YLeaf(YType.str, "rttMplsVpnMonCtrlTag")

                self.rttmplsvpnmonctrlthreshold = YLeaf(YType.int32, "rttMplsVpnMonCtrlThreshold")

                self.rttmplsvpnmonctrltimeout = YLeaf(YType.int32, "rttMplsVpnMonCtrlTimeout")

                self.rttmplsvpnmonctrlverifydata = YLeaf(YType.boolean, "rttMplsVpnMonCtrlVerifyData")

                self.rttmplsvpnmonctrlvrfname = YLeaf(YType.str, "rttMplsVpnMonCtrlVrfName")

                self.rttmplsvpnmonreactactiontype = YLeaf(YType.enumeration, "rttMplsVpnMonReactActionType")

                self.rttmplsvpnmonreactconnectionenable = YLeaf(YType.boolean, "rttMplsVpnMonReactConnectionEnable")

                self.rttmplsvpnmonreactlpdnotifytype = YLeaf(YType.enumeration, "rttMplsVpnMonReactLpdNotifyType")

                self.rttmplsvpnmonreactlpdretrycount = YLeaf(YType.int32, "rttMplsVpnMonReactLpdRetryCount")

                self.rttmplsvpnmonreactthresholdcount = YLeaf(YType.int32, "rttMplsVpnMonReactThresholdCount")

                self.rttmplsvpnmonreactthresholdtype = YLeaf(YType.enumeration, "rttMplsVpnMonReactThresholdType")

                self.rttmplsvpnmonreacttimeoutenable = YLeaf(YType.boolean, "rttMplsVpnMonReactTimeoutEnable")

                self.rttmplsvpnmonschedulefrequency = YLeaf(YType.int32, "rttMplsVpnMonScheduleFrequency")

                self.rttmplsvpnmonscheduleperiod = YLeaf(YType.int32, "rttMplsVpnMonSchedulePeriod")

                self.rttmplsvpnmonschedulerttstarttime = YLeaf(YType.uint32, "rttMplsVpnMonScheduleRttStartTime")

                self.rttmplsvpnmontypedestport = YLeaf(YType.int32, "rttMplsVpnMonTypeDestPort")

                self.rttmplsvpnmontypeinterval = YLeaf(YType.int32, "rttMplsVpnMonTypeInterval")

                self.rttmplsvpnmontypelpdechointerval = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdEchoInterval")

                self.rttmplsvpnmontypelpdechonullshim = YLeaf(YType.boolean, "rttMplsVpnMonTypeLpdEchoNullShim")

                self.rttmplsvpnmontypelpdechotimeout = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdEchoTimeout")

                self.rttmplsvpnmontypelpdmaxsessions = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdMaxSessions")

                self.rttmplsvpnmontypelpdscanperiod = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdScanPeriod")

                self.rttmplsvpnmontypelpdsesstimeout = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdSessTimeout")

                self.rttmplsvpnmontypelpdstathours = YLeaf(YType.int32, "rttMplsVpnMonTypeLpdStatHours")

                self.rttmplsvpnmontypelspreplydscp = YLeaf(YType.int32, "rttMplsVpnMonTypeLSPReplyDscp")

                self.rttmplsvpnmontypelspreplymode = YLeaf(YType.enumeration, "rttMplsVpnMonTypeLSPReplyMode")

                self.rttmplsvpnmontypelspselector = YLeaf(YType.str, "rttMplsVpnMonTypeLspSelector")

                self.rttmplsvpnmontypelspttl = YLeaf(YType.int32, "rttMplsVpnMonTypeLSPTTL")

                self.rttmplsvpnmontypenumpackets = YLeaf(YType.int32, "rttMplsVpnMonTypeNumPackets")

                self.rttmplsvpnmontypesecfreqtype = YLeaf(YType.enumeration, "rttMplsVpnMonTypeSecFreqType")

                self.rttmplsvpnmontypesecfreqvalue = YLeaf(YType.int32, "rttMplsVpnMonTypeSecFreqValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmplsvpnmonctrlindex",
                                "rttmplsvpnmonctrldelscanfactor",
                                "rttmplsvpnmonctrlexp",
                                "rttmplsvpnmonctrllpd",
                                "rttmplsvpnmonctrllpdcomptime",
                                "rttmplsvpnmonctrllpdgrplist",
                                "rttmplsvpnmonctrlprobelist",
                                "rttmplsvpnmonctrlrequestsize",
                                "rttmplsvpnmonctrlrtttype",
                                "rttmplsvpnmonctrlscaninterval",
                                "rttmplsvpnmonctrlstatus",
                                "rttmplsvpnmonctrlstoragetype",
                                "rttmplsvpnmonctrltag",
                                "rttmplsvpnmonctrlthreshold",
                                "rttmplsvpnmonctrltimeout",
                                "rttmplsvpnmonctrlverifydata",
                                "rttmplsvpnmonctrlvrfname",
                                "rttmplsvpnmonreactactiontype",
                                "rttmplsvpnmonreactconnectionenable",
                                "rttmplsvpnmonreactlpdnotifytype",
                                "rttmplsvpnmonreactlpdretrycount",
                                "rttmplsvpnmonreactthresholdcount",
                                "rttmplsvpnmonreactthresholdtype",
                                "rttmplsvpnmonreacttimeoutenable",
                                "rttmplsvpnmonschedulefrequency",
                                "rttmplsvpnmonscheduleperiod",
                                "rttmplsvpnmonschedulerttstarttime",
                                "rttmplsvpnmontypedestport",
                                "rttmplsvpnmontypeinterval",
                                "rttmplsvpnmontypelpdechointerval",
                                "rttmplsvpnmontypelpdechonullshim",
                                "rttmplsvpnmontypelpdechotimeout",
                                "rttmplsvpnmontypelpdmaxsessions",
                                "rttmplsvpnmontypelpdscanperiod",
                                "rttmplsvpnmontypelpdsesstimeout",
                                "rttmplsvpnmontypelpdstathours",
                                "rttmplsvpnmontypelspreplydscp",
                                "rttmplsvpnmontypelspreplymode",
                                "rttmplsvpnmontypelspselector",
                                "rttmplsvpnmontypelspttl",
                                "rttmplsvpnmontypenumpackets",
                                "rttmplsvpnmontypesecfreqtype",
                                "rttmplsvpnmontypesecfreqvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry, self).__setattr__(name, value)

            class Rttmplsvpnmonreactactiontype(Enum):
                """
                Rttmplsvpnmonreactactiontype

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
                Rttmplsvpnmonreactlpdnotifytype

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
                Rttmplsvpnmonreactthresholdtype

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
                Rttmplsvpnmontypesecfreqtype

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


            def has_data(self):
                return (
                    self.rttmplsvpnmonctrlindex.is_set or
                    self.rttmplsvpnmonctrldelscanfactor.is_set or
                    self.rttmplsvpnmonctrlexp.is_set or
                    self.rttmplsvpnmonctrllpd.is_set or
                    self.rttmplsvpnmonctrllpdcomptime.is_set or
                    self.rttmplsvpnmonctrllpdgrplist.is_set or
                    self.rttmplsvpnmonctrlprobelist.is_set or
                    self.rttmplsvpnmonctrlrequestsize.is_set or
                    self.rttmplsvpnmonctrlrtttype.is_set or
                    self.rttmplsvpnmonctrlscaninterval.is_set or
                    self.rttmplsvpnmonctrlstatus.is_set or
                    self.rttmplsvpnmonctrlstoragetype.is_set or
                    self.rttmplsvpnmonctrltag.is_set or
                    self.rttmplsvpnmonctrlthreshold.is_set or
                    self.rttmplsvpnmonctrltimeout.is_set or
                    self.rttmplsvpnmonctrlverifydata.is_set or
                    self.rttmplsvpnmonctrlvrfname.is_set or
                    self.rttmplsvpnmonreactactiontype.is_set or
                    self.rttmplsvpnmonreactconnectionenable.is_set or
                    self.rttmplsvpnmonreactlpdnotifytype.is_set or
                    self.rttmplsvpnmonreactlpdretrycount.is_set or
                    self.rttmplsvpnmonreactthresholdcount.is_set or
                    self.rttmplsvpnmonreactthresholdtype.is_set or
                    self.rttmplsvpnmonreacttimeoutenable.is_set or
                    self.rttmplsvpnmonschedulefrequency.is_set or
                    self.rttmplsvpnmonscheduleperiod.is_set or
                    self.rttmplsvpnmonschedulerttstarttime.is_set or
                    self.rttmplsvpnmontypedestport.is_set or
                    self.rttmplsvpnmontypeinterval.is_set or
                    self.rttmplsvpnmontypelpdechointerval.is_set or
                    self.rttmplsvpnmontypelpdechonullshim.is_set or
                    self.rttmplsvpnmontypelpdechotimeout.is_set or
                    self.rttmplsvpnmontypelpdmaxsessions.is_set or
                    self.rttmplsvpnmontypelpdscanperiod.is_set or
                    self.rttmplsvpnmontypelpdsesstimeout.is_set or
                    self.rttmplsvpnmontypelpdstathours.is_set or
                    self.rttmplsvpnmontypelspreplydscp.is_set or
                    self.rttmplsvpnmontypelspreplymode.is_set or
                    self.rttmplsvpnmontypelspselector.is_set or
                    self.rttmplsvpnmontypelspttl.is_set or
                    self.rttmplsvpnmontypenumpackets.is_set or
                    self.rttmplsvpnmontypesecfreqtype.is_set or
                    self.rttmplsvpnmontypesecfreqvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlindex.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrldelscanfactor.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlexp.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrllpd.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrllpdcomptime.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrllpdgrplist.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlprobelist.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlrequestsize.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlrtttype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlscaninterval.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlstatus.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlstoragetype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrltag.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlthreshold.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrltimeout.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlverifydata.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonctrlvrfname.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactactiontype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactconnectionenable.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactlpdnotifytype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactlpdretrycount.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactthresholdcount.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreactthresholdtype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonreacttimeoutenable.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonschedulefrequency.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonscheduleperiod.yfilter != YFilter.not_set or
                    self.rttmplsvpnmonschedulerttstarttime.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypedestport.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypeinterval.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdechointerval.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdechonullshim.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdechotimeout.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdmaxsessions.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdscanperiod.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdsesstimeout.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelpdstathours.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelspreplydscp.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelspreplymode.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelspselector.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypelspttl.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypenumpackets.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypesecfreqtype.yfilter != YFilter.not_set or
                    self.rttmplsvpnmontypesecfreqvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMplsVpnMonCtrlEntry" + "[rttMplsVpnMonCtrlIndex='" + self.rttmplsvpnmonctrlindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMplsVpnMonCtrlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmplsvpnmonctrlindex.is_set or self.rttmplsvpnmonctrlindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlindex.get_name_leafdata())
                if (self.rttmplsvpnmonctrldelscanfactor.is_set or self.rttmplsvpnmonctrldelscanfactor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrldelscanfactor.get_name_leafdata())
                if (self.rttmplsvpnmonctrlexp.is_set or self.rttmplsvpnmonctrlexp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlexp.get_name_leafdata())
                if (self.rttmplsvpnmonctrllpd.is_set or self.rttmplsvpnmonctrllpd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrllpd.get_name_leafdata())
                if (self.rttmplsvpnmonctrllpdcomptime.is_set or self.rttmplsvpnmonctrllpdcomptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrllpdcomptime.get_name_leafdata())
                if (self.rttmplsvpnmonctrllpdgrplist.is_set or self.rttmplsvpnmonctrllpdgrplist.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrllpdgrplist.get_name_leafdata())
                if (self.rttmplsvpnmonctrlprobelist.is_set or self.rttmplsvpnmonctrlprobelist.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlprobelist.get_name_leafdata())
                if (self.rttmplsvpnmonctrlrequestsize.is_set or self.rttmplsvpnmonctrlrequestsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlrequestsize.get_name_leafdata())
                if (self.rttmplsvpnmonctrlrtttype.is_set or self.rttmplsvpnmonctrlrtttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlrtttype.get_name_leafdata())
                if (self.rttmplsvpnmonctrlscaninterval.is_set or self.rttmplsvpnmonctrlscaninterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlscaninterval.get_name_leafdata())
                if (self.rttmplsvpnmonctrlstatus.is_set or self.rttmplsvpnmonctrlstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlstatus.get_name_leafdata())
                if (self.rttmplsvpnmonctrlstoragetype.is_set or self.rttmplsvpnmonctrlstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlstoragetype.get_name_leafdata())
                if (self.rttmplsvpnmonctrltag.is_set or self.rttmplsvpnmonctrltag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrltag.get_name_leafdata())
                if (self.rttmplsvpnmonctrlthreshold.is_set or self.rttmplsvpnmonctrlthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlthreshold.get_name_leafdata())
                if (self.rttmplsvpnmonctrltimeout.is_set or self.rttmplsvpnmonctrltimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrltimeout.get_name_leafdata())
                if (self.rttmplsvpnmonctrlverifydata.is_set or self.rttmplsvpnmonctrlverifydata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlverifydata.get_name_leafdata())
                if (self.rttmplsvpnmonctrlvrfname.is_set or self.rttmplsvpnmonctrlvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonctrlvrfname.get_name_leafdata())
                if (self.rttmplsvpnmonreactactiontype.is_set or self.rttmplsvpnmonreactactiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactactiontype.get_name_leafdata())
                if (self.rttmplsvpnmonreactconnectionenable.is_set or self.rttmplsvpnmonreactconnectionenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactconnectionenable.get_name_leafdata())
                if (self.rttmplsvpnmonreactlpdnotifytype.is_set or self.rttmplsvpnmonreactlpdnotifytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactlpdnotifytype.get_name_leafdata())
                if (self.rttmplsvpnmonreactlpdretrycount.is_set or self.rttmplsvpnmonreactlpdretrycount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactlpdretrycount.get_name_leafdata())
                if (self.rttmplsvpnmonreactthresholdcount.is_set or self.rttmplsvpnmonreactthresholdcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactthresholdcount.get_name_leafdata())
                if (self.rttmplsvpnmonreactthresholdtype.is_set or self.rttmplsvpnmonreactthresholdtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreactthresholdtype.get_name_leafdata())
                if (self.rttmplsvpnmonreacttimeoutenable.is_set or self.rttmplsvpnmonreacttimeoutenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonreacttimeoutenable.get_name_leafdata())
                if (self.rttmplsvpnmonschedulefrequency.is_set or self.rttmplsvpnmonschedulefrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonschedulefrequency.get_name_leafdata())
                if (self.rttmplsvpnmonscheduleperiod.is_set or self.rttmplsvpnmonscheduleperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonscheduleperiod.get_name_leafdata())
                if (self.rttmplsvpnmonschedulerttstarttime.is_set or self.rttmplsvpnmonschedulerttstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmonschedulerttstarttime.get_name_leafdata())
                if (self.rttmplsvpnmontypedestport.is_set or self.rttmplsvpnmontypedestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypedestport.get_name_leafdata())
                if (self.rttmplsvpnmontypeinterval.is_set or self.rttmplsvpnmontypeinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypeinterval.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdechointerval.is_set or self.rttmplsvpnmontypelpdechointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdechointerval.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdechonullshim.is_set or self.rttmplsvpnmontypelpdechonullshim.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdechonullshim.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdechotimeout.is_set or self.rttmplsvpnmontypelpdechotimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdechotimeout.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdmaxsessions.is_set or self.rttmplsvpnmontypelpdmaxsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdmaxsessions.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdscanperiod.is_set or self.rttmplsvpnmontypelpdscanperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdscanperiod.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdsesstimeout.is_set or self.rttmplsvpnmontypelpdsesstimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdsesstimeout.get_name_leafdata())
                if (self.rttmplsvpnmontypelpdstathours.is_set or self.rttmplsvpnmontypelpdstathours.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelpdstathours.get_name_leafdata())
                if (self.rttmplsvpnmontypelspreplydscp.is_set or self.rttmplsvpnmontypelspreplydscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelspreplydscp.get_name_leafdata())
                if (self.rttmplsvpnmontypelspreplymode.is_set or self.rttmplsvpnmontypelspreplymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelspreplymode.get_name_leafdata())
                if (self.rttmplsvpnmontypelspselector.is_set or self.rttmplsvpnmontypelspselector.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelspselector.get_name_leafdata())
                if (self.rttmplsvpnmontypelspttl.is_set or self.rttmplsvpnmontypelspttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypelspttl.get_name_leafdata())
                if (self.rttmplsvpnmontypenumpackets.is_set or self.rttmplsvpnmontypenumpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypenumpackets.get_name_leafdata())
                if (self.rttmplsvpnmontypesecfreqtype.is_set or self.rttmplsvpnmontypesecfreqtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypesecfreqtype.get_name_leafdata())
                if (self.rttmplsvpnmontypesecfreqvalue.is_set or self.rttmplsvpnmontypesecfreqvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmplsvpnmontypesecfreqvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMplsVpnMonCtrlIndex" or name == "rttMplsVpnMonCtrlDelScanFactor" or name == "rttMplsVpnMonCtrlEXP" or name == "rttMplsVpnMonCtrlLpd" or name == "rttMplsVpnMonCtrlLpdCompTime" or name == "rttMplsVpnMonCtrlLpdGrpList" or name == "rttMplsVpnMonCtrlProbeList" or name == "rttMplsVpnMonCtrlRequestSize" or name == "rttMplsVpnMonCtrlRttType" or name == "rttMplsVpnMonCtrlScanInterval" or name == "rttMplsVpnMonCtrlStatus" or name == "rttMplsVpnMonCtrlStorageType" or name == "rttMplsVpnMonCtrlTag" or name == "rttMplsVpnMonCtrlThreshold" or name == "rttMplsVpnMonCtrlTimeout" or name == "rttMplsVpnMonCtrlVerifyData" or name == "rttMplsVpnMonCtrlVrfName" or name == "rttMplsVpnMonReactActionType" or name == "rttMplsVpnMonReactConnectionEnable" or name == "rttMplsVpnMonReactLpdNotifyType" or name == "rttMplsVpnMonReactLpdRetryCount" or name == "rttMplsVpnMonReactThresholdCount" or name == "rttMplsVpnMonReactThresholdType" or name == "rttMplsVpnMonReactTimeoutEnable" or name == "rttMplsVpnMonScheduleFrequency" or name == "rttMplsVpnMonSchedulePeriod" or name == "rttMplsVpnMonScheduleRttStartTime" or name == "rttMplsVpnMonTypeDestPort" or name == "rttMplsVpnMonTypeInterval" or name == "rttMplsVpnMonTypeLpdEchoInterval" or name == "rttMplsVpnMonTypeLpdEchoNullShim" or name == "rttMplsVpnMonTypeLpdEchoTimeout" or name == "rttMplsVpnMonTypeLpdMaxSessions" or name == "rttMplsVpnMonTypeLpdScanPeriod" or name == "rttMplsVpnMonTypeLpdSessTimeout" or name == "rttMplsVpnMonTypeLpdStatHours" or name == "rttMplsVpnMonTypeLSPReplyDscp" or name == "rttMplsVpnMonTypeLSPReplyMode" or name == "rttMplsVpnMonTypeLspSelector" or name == "rttMplsVpnMonTypeLSPTTL" or name == "rttMplsVpnMonTypeNumPackets" or name == "rttMplsVpnMonTypeSecFreqType" or name == "rttMplsVpnMonTypeSecFreqValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMplsVpnMonCtrlIndex"):
                    self.rttmplsvpnmonctrlindex = value
                    self.rttmplsvpnmonctrlindex.value_namespace = name_space
                    self.rttmplsvpnmonctrlindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlDelScanFactor"):
                    self.rttmplsvpnmonctrldelscanfactor = value
                    self.rttmplsvpnmonctrldelscanfactor.value_namespace = name_space
                    self.rttmplsvpnmonctrldelscanfactor.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlEXP"):
                    self.rttmplsvpnmonctrlexp = value
                    self.rttmplsvpnmonctrlexp.value_namespace = name_space
                    self.rttmplsvpnmonctrlexp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlLpd"):
                    self.rttmplsvpnmonctrllpd = value
                    self.rttmplsvpnmonctrllpd.value_namespace = name_space
                    self.rttmplsvpnmonctrllpd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlLpdCompTime"):
                    self.rttmplsvpnmonctrllpdcomptime = value
                    self.rttmplsvpnmonctrllpdcomptime.value_namespace = name_space
                    self.rttmplsvpnmonctrllpdcomptime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlLpdGrpList"):
                    self.rttmplsvpnmonctrllpdgrplist = value
                    self.rttmplsvpnmonctrllpdgrplist.value_namespace = name_space
                    self.rttmplsvpnmonctrllpdgrplist.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlProbeList"):
                    self.rttmplsvpnmonctrlprobelist = value
                    self.rttmplsvpnmonctrlprobelist.value_namespace = name_space
                    self.rttmplsvpnmonctrlprobelist.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlRequestSize"):
                    self.rttmplsvpnmonctrlrequestsize = value
                    self.rttmplsvpnmonctrlrequestsize.value_namespace = name_space
                    self.rttmplsvpnmonctrlrequestsize.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlRttType"):
                    self.rttmplsvpnmonctrlrtttype = value
                    self.rttmplsvpnmonctrlrtttype.value_namespace = name_space
                    self.rttmplsvpnmonctrlrtttype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlScanInterval"):
                    self.rttmplsvpnmonctrlscaninterval = value
                    self.rttmplsvpnmonctrlscaninterval.value_namespace = name_space
                    self.rttmplsvpnmonctrlscaninterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlStatus"):
                    self.rttmplsvpnmonctrlstatus = value
                    self.rttmplsvpnmonctrlstatus.value_namespace = name_space
                    self.rttmplsvpnmonctrlstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlStorageType"):
                    self.rttmplsvpnmonctrlstoragetype = value
                    self.rttmplsvpnmonctrlstoragetype.value_namespace = name_space
                    self.rttmplsvpnmonctrlstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlTag"):
                    self.rttmplsvpnmonctrltag = value
                    self.rttmplsvpnmonctrltag.value_namespace = name_space
                    self.rttmplsvpnmonctrltag.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlThreshold"):
                    self.rttmplsvpnmonctrlthreshold = value
                    self.rttmplsvpnmonctrlthreshold.value_namespace = name_space
                    self.rttmplsvpnmonctrlthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlTimeout"):
                    self.rttmplsvpnmonctrltimeout = value
                    self.rttmplsvpnmonctrltimeout.value_namespace = name_space
                    self.rttmplsvpnmonctrltimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlVerifyData"):
                    self.rttmplsvpnmonctrlverifydata = value
                    self.rttmplsvpnmonctrlverifydata.value_namespace = name_space
                    self.rttmplsvpnmonctrlverifydata.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonCtrlVrfName"):
                    self.rttmplsvpnmonctrlvrfname = value
                    self.rttmplsvpnmonctrlvrfname.value_namespace = name_space
                    self.rttmplsvpnmonctrlvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactActionType"):
                    self.rttmplsvpnmonreactactiontype = value
                    self.rttmplsvpnmonreactactiontype.value_namespace = name_space
                    self.rttmplsvpnmonreactactiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactConnectionEnable"):
                    self.rttmplsvpnmonreactconnectionenable = value
                    self.rttmplsvpnmonreactconnectionenable.value_namespace = name_space
                    self.rttmplsvpnmonreactconnectionenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactLpdNotifyType"):
                    self.rttmplsvpnmonreactlpdnotifytype = value
                    self.rttmplsvpnmonreactlpdnotifytype.value_namespace = name_space
                    self.rttmplsvpnmonreactlpdnotifytype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactLpdRetryCount"):
                    self.rttmplsvpnmonreactlpdretrycount = value
                    self.rttmplsvpnmonreactlpdretrycount.value_namespace = name_space
                    self.rttmplsvpnmonreactlpdretrycount.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactThresholdCount"):
                    self.rttmplsvpnmonreactthresholdcount = value
                    self.rttmplsvpnmonreactthresholdcount.value_namespace = name_space
                    self.rttmplsvpnmonreactthresholdcount.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactThresholdType"):
                    self.rttmplsvpnmonreactthresholdtype = value
                    self.rttmplsvpnmonreactthresholdtype.value_namespace = name_space
                    self.rttmplsvpnmonreactthresholdtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonReactTimeoutEnable"):
                    self.rttmplsvpnmonreacttimeoutenable = value
                    self.rttmplsvpnmonreacttimeoutenable.value_namespace = name_space
                    self.rttmplsvpnmonreacttimeoutenable.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonScheduleFrequency"):
                    self.rttmplsvpnmonschedulefrequency = value
                    self.rttmplsvpnmonschedulefrequency.value_namespace = name_space
                    self.rttmplsvpnmonschedulefrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonSchedulePeriod"):
                    self.rttmplsvpnmonscheduleperiod = value
                    self.rttmplsvpnmonscheduleperiod.value_namespace = name_space
                    self.rttmplsvpnmonscheduleperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonScheduleRttStartTime"):
                    self.rttmplsvpnmonschedulerttstarttime = value
                    self.rttmplsvpnmonschedulerttstarttime.value_namespace = name_space
                    self.rttmplsvpnmonschedulerttstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeDestPort"):
                    self.rttmplsvpnmontypedestport = value
                    self.rttmplsvpnmontypedestport.value_namespace = name_space
                    self.rttmplsvpnmontypedestport.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeInterval"):
                    self.rttmplsvpnmontypeinterval = value
                    self.rttmplsvpnmontypeinterval.value_namespace = name_space
                    self.rttmplsvpnmontypeinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdEchoInterval"):
                    self.rttmplsvpnmontypelpdechointerval = value
                    self.rttmplsvpnmontypelpdechointerval.value_namespace = name_space
                    self.rttmplsvpnmontypelpdechointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdEchoNullShim"):
                    self.rttmplsvpnmontypelpdechonullshim = value
                    self.rttmplsvpnmontypelpdechonullshim.value_namespace = name_space
                    self.rttmplsvpnmontypelpdechonullshim.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdEchoTimeout"):
                    self.rttmplsvpnmontypelpdechotimeout = value
                    self.rttmplsvpnmontypelpdechotimeout.value_namespace = name_space
                    self.rttmplsvpnmontypelpdechotimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdMaxSessions"):
                    self.rttmplsvpnmontypelpdmaxsessions = value
                    self.rttmplsvpnmontypelpdmaxsessions.value_namespace = name_space
                    self.rttmplsvpnmontypelpdmaxsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdScanPeriod"):
                    self.rttmplsvpnmontypelpdscanperiod = value
                    self.rttmplsvpnmontypelpdscanperiod.value_namespace = name_space
                    self.rttmplsvpnmontypelpdscanperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdSessTimeout"):
                    self.rttmplsvpnmontypelpdsesstimeout = value
                    self.rttmplsvpnmontypelpdsesstimeout.value_namespace = name_space
                    self.rttmplsvpnmontypelpdsesstimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLpdStatHours"):
                    self.rttmplsvpnmontypelpdstathours = value
                    self.rttmplsvpnmontypelpdstathours.value_namespace = name_space
                    self.rttmplsvpnmontypelpdstathours.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLSPReplyDscp"):
                    self.rttmplsvpnmontypelspreplydscp = value
                    self.rttmplsvpnmontypelspreplydscp.value_namespace = name_space
                    self.rttmplsvpnmontypelspreplydscp.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLSPReplyMode"):
                    self.rttmplsvpnmontypelspreplymode = value
                    self.rttmplsvpnmontypelspreplymode.value_namespace = name_space
                    self.rttmplsvpnmontypelspreplymode.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLspSelector"):
                    self.rttmplsvpnmontypelspselector = value
                    self.rttmplsvpnmontypelspselector.value_namespace = name_space
                    self.rttmplsvpnmontypelspselector.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeLSPTTL"):
                    self.rttmplsvpnmontypelspttl = value
                    self.rttmplsvpnmontypelspttl.value_namespace = name_space
                    self.rttmplsvpnmontypelspttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeNumPackets"):
                    self.rttmplsvpnmontypenumpackets = value
                    self.rttmplsvpnmontypenumpackets.value_namespace = name_space
                    self.rttmplsvpnmontypenumpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeSecFreqType"):
                    self.rttmplsvpnmontypesecfreqtype = value
                    self.rttmplsvpnmontypesecfreqtype.value_namespace = name_space
                    self.rttmplsvpnmontypesecfreqtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMplsVpnMonTypeSecFreqValue"):
                    self.rttmplsvpnmontypesecfreqvalue = value
                    self.rttmplsvpnmontypesecfreqvalue.value_namespace = name_space
                    self.rttmplsvpnmontypesecfreqvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmplsvpnmonctrlentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmplsvpnmonctrlentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMplsVpnMonCtrlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMplsVpnMonCtrlEntry"):
                for c in self.rttmplsvpnmonctrlentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmplsvpnmonctrltable.Rttmplsvpnmonctrlentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmplsvpnmonctrlentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMplsVpnMonCtrlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonreactentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonreacttable, self).__init__()

            self.yang_name = "rttMonReactTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonreactentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonreacttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonreacttable, self).__setattr__(name, value)


        class Rttmonreactentry(Entity):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonreactconfigindex  <key>
            
            	This object along with rttMonCtrlAdminIndex identifies a particular reaction\-configuration for a particular probe. This is a pseudo\-random number selected by the management station when creating a row via the rttMonReactStatus. If the pseudo\-random number is already in use an 'inconsistentValue' return code will be returned when set operation is attempted
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonreactactiontype
            
            	Specifies what type(s), if any, of reaction(s) to generate if an operation violates one of the watched ( reaction\-configuration ) conditions\:  none               \- no reaction is generated trapOnly           \- a trap is generated triggerOnly        \- all trigger actions defined for this                      entry are initiated trapAndTrigger     \- both a trap and all trigger actions                      are initiated A trigger action is defined via the rttMonReactTriggerAdminTable
            	**type**\:   :py:class:`Rttmonreactactiontype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry.Rttmonreactactiontype>`
            
            .. attribute:: rttmonreactoccurred
            
            	This object is set to true when the configured threshold condition is violated as defined by rttMonReactThresholdType. It will be again set to 'false' if the condition reverses.  This object is set to true in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to true.  \- rttMonReactVar is set to connectionLoss and    rttMonCtrlOperConnectionLostOccurred set to true.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to true.  \- For all other values of rttMonReactVar, if the    corresponding value exceeds the configured    rttMonReactThresholdRising.   This object is set to false in the following conditions\:  \- rttMonReactVar is set to timeout and    rttMonCtrlOperTimeoutOccurred set to false.  \- rttMonReactVar is set to connectionLoss and     rttMonCtrlOperConnectionLostOccurred set to false.  \- rttMonReactVar is set to verifyError and    rttMonCtrlOperVerifyErrorOccurred is set to false.  \- For all other values of rttMonReactVar, if the    corresponding value fall below the configured     rttMonReactThresholdFalling.  When the RttMonRttType is 'pathEcho' or 'pathJitter', this object is applied only to the  rttMonEchoAdminTargetAddress and not to intermediate hops to the Target
            	**type**\:  bool
            
            .. attribute:: rttmonreactstatus
            
            	This objects indicates the status of the conceptual RTT Reaction Control Row.Only CreateAndGo and destroy  operations are permitted on the row.  When this object moves to active state, the conceptual row having the Reaction configuration for the probe is monitored and the notifications are generated when the threshold violation takes place.  In order for this object to become active rttMonReactVar must be defined. All other objects assume the default value.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration for the probes would exist. The reaction configuration for the probe is removed
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rttmonreactthresholdcountx
            
            	If rttMonReactThresholdType value is 'xOfy', this object defines the 'x' value.  If rttMonReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  rttMonReactOccurred as true.  If rttMonReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if rttMonReactThresholdType has value of 'never' and 'immediate'
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: rttmonreactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if rttMonReactThresholdType is 'xOfy'.  For other values of rttMonReactThresholdType, this object is not applicable
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: rttmonreactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the conditions specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 310.    'mosCQDS' is 310.    'rFactorDS' is 60.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.    'iaJitterSD' is 20.    'mosCQSD' is 310.    'rFactorSD' is 60.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of rttMonReactThresholdFalling will be 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in rttMonReactThresholdType are satisfied, a trap is generated.  Default value of rttMonReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'iaJitterDS' is 20.    'frameLossDS' is 10000.    'mosLQDS' is 400.    'mosCQDS' is 400.    'rFactorDS' is 80.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the rttMonReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  rttMonReactThresholdRising will be 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactthresholdtype
            
            	This object specifies the conditions under which the notification ( trap ) is sent.  never       \- rttMonReactOccurred is never set  immediate   \- rttMonReactOccurred is set to 'true' when the               value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,               mos etc ) violates the threshold.               Conversely, rttMonReactOccurred is set to 'false'               when the parameter ( e.g rtt, jitterAvg,               packetLossSD, mos etc ) is below the threshold               limits.  consecutive \- rttMonReactOccurred is set to true when the value               of parameter for which reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold for configured consecutive               times.               Conversely, rttMonReactOccurred is set to false               when the value of parameter ( e.g rtt, jitterAvg               packetLossSD, mos etc ) is below the threshold               limits for the same number of consecutive               operations.  xOfy        \- rttMonReactOccurred is set to true when x               ( as specified by rttMonReactThresholdCountX )               out of the last y ( as specified by               rttMonReacthresholdCountY ) times the value of               parameter for which the reaction is configured               ( e.g rtt, jitterAvg, packetLossSD, mos etc )               violates the threshold.               Conversely, it is set to false when x, out of the               last y times the value of parameter               ( e.g rtt, jitterAvg, packetLossSD, mos ) is               below the threshold limits.               NOTE\: When x > y, the probe will never                     generate a reaction.  average    \- rttMonReactOccurred is set to true when the              average ( rttMonReactThresholdCountX times )              value of parameter for which reaction is               configured ( e.g rtt, jitterAvg, packetLossSD,              mos etc ) violates the threshold condition.              Conversely, it is set to false when the              average value of parameter ( e.g rtt, jitterAvg,              packetLossSD, mos etc ) is below the threshold              limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:   :py:class:`Rttmonreactthresholdtype <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry.Rttmonreactthresholdtype>`
            
            .. attribute:: rttmonreactvalue
            
            	This object will be set when the configured threshold condition is violated as defined by rttMonReactThresholdType and holds the actual value that violated the configured threshold values.  This object is not valid for the following values of rttMonReactVar and It will be always 0\:   \- timeout   \- connectionLoss   \- verifyError
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonreactvar
            
            	This object specifies the type of reaction configured for a probe.  The reaction types 'rtt', 'timeout', and 'connectionLoss'  can be configured for all probe types.  The reaction type 'verifyError' can be configured for all  probe types except RTP probe type.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' and 'maxOfNegativeDS' can be configured for UDP jitter  and ICMP jitter probe types only.  The reaction types 'mos' and 'icpif' can be configured  for UDP jitter and ICMP jitter probe types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter, and  RTP probe types only.  The reaction types 'iaJitterDS', 'frameLossDS', 'mosLQDS',  'mosCQDS', 'rFactorDS', 'iaJitterSD', 'rFactorSD', 'mosCQSD'  can be configured for RTP probe type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter probe  type only
            	**type**\:   :py:class:`Rttmonreactvar <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmonreactvar>`
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry, self).__init__()

                self.yang_name = "rttMonReactEntry"
                self.yang_parent_name = "rttMonReactTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonreactconfigindex = YLeaf(YType.int32, "rttMonReactConfigIndex")

                self.rttmonreactactiontype = YLeaf(YType.enumeration, "rttMonReactActionType")

                self.rttmonreactoccurred = YLeaf(YType.boolean, "rttMonReactOccurred")

                self.rttmonreactstatus = YLeaf(YType.enumeration, "rttMonReactStatus")

                self.rttmonreactthresholdcountx = YLeaf(YType.int32, "rttMonReactThresholdCountX")

                self.rttmonreactthresholdcounty = YLeaf(YType.int32, "rttMonReactThresholdCountY")

                self.rttmonreactthresholdfalling = YLeaf(YType.int32, "rttMonReactThresholdFalling")

                self.rttmonreactthresholdrising = YLeaf(YType.int32, "rttMonReactThresholdRising")

                self.rttmonreactthresholdtype = YLeaf(YType.enumeration, "rttMonReactThresholdType")

                self.rttmonreactvalue = YLeaf(YType.int32, "rttMonReactValue")

                self.rttmonreactvar = YLeaf(YType.enumeration, "rttMonReactVar")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonreactconfigindex",
                                "rttmonreactactiontype",
                                "rttmonreactoccurred",
                                "rttmonreactstatus",
                                "rttmonreactthresholdcountx",
                                "rttmonreactthresholdcounty",
                                "rttmonreactthresholdfalling",
                                "rttmonreactthresholdrising",
                                "rttmonreactthresholdtype",
                                "rttmonreactvalue",
                                "rttmonreactvar") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry, self).__setattr__(name, value)

            class Rttmonreactactiontype(Enum):
                """
                Rttmonreactactiontype

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
                Rttmonreactthresholdtype

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


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonreactconfigindex.is_set or
                    self.rttmonreactactiontype.is_set or
                    self.rttmonreactoccurred.is_set or
                    self.rttmonreactstatus.is_set or
                    self.rttmonreactthresholdcountx.is_set or
                    self.rttmonreactthresholdcounty.is_set or
                    self.rttmonreactthresholdfalling.is_set or
                    self.rttmonreactthresholdrising.is_set or
                    self.rttmonreactthresholdtype.is_set or
                    self.rttmonreactvalue.is_set or
                    self.rttmonreactvar.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonreactconfigindex.yfilter != YFilter.not_set or
                    self.rttmonreactactiontype.yfilter != YFilter.not_set or
                    self.rttmonreactoccurred.yfilter != YFilter.not_set or
                    self.rttmonreactstatus.yfilter != YFilter.not_set or
                    self.rttmonreactthresholdcountx.yfilter != YFilter.not_set or
                    self.rttmonreactthresholdcounty.yfilter != YFilter.not_set or
                    self.rttmonreactthresholdfalling.yfilter != YFilter.not_set or
                    self.rttmonreactthresholdrising.yfilter != YFilter.not_set or
                    self.rttmonreactthresholdtype.yfilter != YFilter.not_set or
                    self.rttmonreactvalue.yfilter != YFilter.not_set or
                    self.rttmonreactvar.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonReactEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonReactConfigIndex='" + self.rttmonreactconfigindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonReactTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonreactconfigindex.is_set or self.rttmonreactconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactconfigindex.get_name_leafdata())
                if (self.rttmonreactactiontype.is_set or self.rttmonreactactiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactactiontype.get_name_leafdata())
                if (self.rttmonreactoccurred.is_set or self.rttmonreactoccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactoccurred.get_name_leafdata())
                if (self.rttmonreactstatus.is_set or self.rttmonreactstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactstatus.get_name_leafdata())
                if (self.rttmonreactthresholdcountx.is_set or self.rttmonreactthresholdcountx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactthresholdcountx.get_name_leafdata())
                if (self.rttmonreactthresholdcounty.is_set or self.rttmonreactthresholdcounty.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactthresholdcounty.get_name_leafdata())
                if (self.rttmonreactthresholdfalling.is_set or self.rttmonreactthresholdfalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactthresholdfalling.get_name_leafdata())
                if (self.rttmonreactthresholdrising.is_set or self.rttmonreactthresholdrising.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactthresholdrising.get_name_leafdata())
                if (self.rttmonreactthresholdtype.is_set or self.rttmonreactthresholdtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactthresholdtype.get_name_leafdata())
                if (self.rttmonreactvalue.is_set or self.rttmonreactvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactvalue.get_name_leafdata())
                if (self.rttmonreactvar.is_set or self.rttmonreactvar.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonreactvar.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonReactConfigIndex" or name == "rttMonReactActionType" or name == "rttMonReactOccurred" or name == "rttMonReactStatus" or name == "rttMonReactThresholdCountX" or name == "rttMonReactThresholdCountY" or name == "rttMonReactThresholdFalling" or name == "rttMonReactThresholdRising" or name == "rttMonReactThresholdType" or name == "rttMonReactValue" or name == "rttMonReactVar"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactConfigIndex"):
                    self.rttmonreactconfigindex = value
                    self.rttmonreactconfigindex.value_namespace = name_space
                    self.rttmonreactconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactActionType"):
                    self.rttmonreactactiontype = value
                    self.rttmonreactactiontype.value_namespace = name_space
                    self.rttmonreactactiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactOccurred"):
                    self.rttmonreactoccurred = value
                    self.rttmonreactoccurred.value_namespace = name_space
                    self.rttmonreactoccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactStatus"):
                    self.rttmonreactstatus = value
                    self.rttmonreactstatus.value_namespace = name_space
                    self.rttmonreactstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactThresholdCountX"):
                    self.rttmonreactthresholdcountx = value
                    self.rttmonreactthresholdcountx.value_namespace = name_space
                    self.rttmonreactthresholdcountx.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactThresholdCountY"):
                    self.rttmonreactthresholdcounty = value
                    self.rttmonreactthresholdcounty.value_namespace = name_space
                    self.rttmonreactthresholdcounty.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactThresholdFalling"):
                    self.rttmonreactthresholdfalling = value
                    self.rttmonreactthresholdfalling.value_namespace = name_space
                    self.rttmonreactthresholdfalling.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactThresholdRising"):
                    self.rttmonreactthresholdrising = value
                    self.rttmonreactthresholdrising.value_namespace = name_space
                    self.rttmonreactthresholdrising.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactThresholdType"):
                    self.rttmonreactthresholdtype = value
                    self.rttmonreactthresholdtype.value_namespace = name_space
                    self.rttmonreactthresholdtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactValue"):
                    self.rttmonreactvalue = value
                    self.rttmonreactvalue.value_namespace = name_space
                    self.rttmonreactvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonReactVar"):
                    self.rttmonreactvar = value
                    self.rttmonreactvar.value_namespace = name_space
                    self.rttmonreactvar.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonreactentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonreactentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonReactTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonReactEntry"):
                for c in self.rttmonreactentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonreacttable.Rttmonreactentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonreactentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonReactEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmongeneratedoperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmongeneratedopertable.Rttmongeneratedoperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmongeneratedopertable, self).__init__()

            self.yang_name = "rttMonGeneratedOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmongeneratedoperentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmongeneratedopertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmongeneratedopertable, self).__setattr__(name, value)


        class Rttmongeneratedoperentry(Entity):
            """
            An entry in the Generated Oper table corresponding to
            a child or generated operation as part of a parent
            IP SLA operation.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmongeneratedoperrespipaddrtype  <key>
            
            	The type of Internet address, IPv4 or IPv6, of a responder for an IP SLA operation
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: rttmongeneratedoperrespipaddr  <key>
            
            	The internet address of a responder for IP SLA operation. The type of this address is determined by the value of rttMonGeneratedOperRespIpAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: rttmongeneratedoperctrladminindex
            
            	This is a pseudo\-random number, auto\-generated based to identify a child operation based on a parent  operation started by the management station,when  creating a row via the rttMonCtrlAdminStatus object
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmongeneratedopertable.Rttmongeneratedoperentry, self).__init__()

                self.yang_name = "rttMonGeneratedOperEntry"
                self.yang_parent_name = "rttMonGeneratedOperTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmongeneratedoperrespipaddrtype = YLeaf(YType.enumeration, "rttMonGeneratedOperRespIpAddrType")

                self.rttmongeneratedoperrespipaddr = YLeaf(YType.str, "rttMonGeneratedOperRespIpAddr")

                self.rttmongeneratedoperctrladminindex = YLeaf(YType.uint32, "rttMonGeneratedOperCtrlAdminIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmongeneratedoperrespipaddrtype",
                                "rttmongeneratedoperrespipaddr",
                                "rttmongeneratedoperctrladminindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmongeneratedopertable.Rttmongeneratedoperentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmongeneratedopertable.Rttmongeneratedoperentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmongeneratedoperrespipaddrtype.is_set or
                    self.rttmongeneratedoperrespipaddr.is_set or
                    self.rttmongeneratedoperctrladminindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmongeneratedoperrespipaddrtype.yfilter != YFilter.not_set or
                    self.rttmongeneratedoperrespipaddr.yfilter != YFilter.not_set or
                    self.rttmongeneratedoperctrladminindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonGeneratedOperEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonGeneratedOperRespIpAddrType='" + self.rttmongeneratedoperrespipaddrtype.get() + "']" + "[rttMonGeneratedOperRespIpAddr='" + self.rttmongeneratedoperrespipaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonGeneratedOperTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmongeneratedoperrespipaddrtype.is_set or self.rttmongeneratedoperrespipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongeneratedoperrespipaddrtype.get_name_leafdata())
                if (self.rttmongeneratedoperrespipaddr.is_set or self.rttmongeneratedoperrespipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongeneratedoperrespipaddr.get_name_leafdata())
                if (self.rttmongeneratedoperctrladminindex.is_set or self.rttmongeneratedoperctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmongeneratedoperctrladminindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonGeneratedOperRespIpAddrType" or name == "rttMonGeneratedOperRespIpAddr" or name == "rttMonGeneratedOperCtrlAdminIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGeneratedOperRespIpAddrType"):
                    self.rttmongeneratedoperrespipaddrtype = value
                    self.rttmongeneratedoperrespipaddrtype.value_namespace = name_space
                    self.rttmongeneratedoperrespipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGeneratedOperRespIpAddr"):
                    self.rttmongeneratedoperrespipaddr = value
                    self.rttmongeneratedoperrespipaddr.value_namespace = name_space
                    self.rttmongeneratedoperrespipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonGeneratedOperCtrlAdminIndex"):
                    self.rttmongeneratedoperctrladminindex = value
                    self.rttmongeneratedoperctrladminindex.value_namespace = name_space
                    self.rttmongeneratedoperctrladminindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmongeneratedoperentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmongeneratedoperentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonGeneratedOperTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonGeneratedOperEntry"):
                for c in self.rttmongeneratedoperentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmongeneratedopertable.Rttmongeneratedoperentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmongeneratedoperentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonGeneratedOperEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonstatscaptureentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonstatscapturetable, self).__init__()

            self.yang_name = "rttMonStatsCaptureTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonstatscaptureentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonstatscapturetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonstatscapturetable, self).__setattr__(name, value)


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
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  <key>
            
            	The time when this row was created.  This object is the second index of the  rttMonStatsCaptureTable Table.  The the number of rttMonStatsCaptureStartTimeIndex   groups exceeds the rttMonStatisticsAdminNumHourGroups value, the oldest rttMonStatsCaptureStartTimeIndex  group will be removed and replaced with the new entry.  When the RttMonRttType is 'pathEcho', this object also  uniquely defines a group of paths.  See the  rttMonStatsCaptureEntry object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatscapturepathindex  <key>
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a path for a given value of  rttMonStatsCaptureStartTimeIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of  rttMonStatsCaptureStartTimeIndex, the agent assigns the first instance of a path a value of 1, then second  instance a value of 2, and so on.  The sequence keeps  incrementing until the number of paths equals  rttMonStatisticsAdminNumPaths value, then no new paths  are kept for the current rttMonStatsCaptureStartTimeIndex  group.  NOTE\: A source to target rttMonStatsCapturePathIndex       path will be created for each        rttMonStatsCaptureStartTimeIndex to hold all        errors that occur when a specific path or        connection has not be setup.  This value directly represents the path to a target. We can only support 128 paths
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: rttmonstatscapturehopindex  <key>
            
            	When the RttMonRttType is 'pathEcho', this object uniquely defines a hop for a given value of  rttMonStatsCapturePathIndex.  For all other values of RttMonRttType, this object will be one.  For a particular value of rttMonStatsCapturePathIndex, the agent assigns the first instance of a hop a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  hops equals rttMonStatisticsAdminNumHops value, then no new hops are kept for the current rttMonStatsCapturePathIndex.  This value directly represents a hop along the path to a target, thus we can only support 30 hops.  This value shows the order along the path to a target
            	**type**\:  int
            
            	**range:** 1..30
            
            .. attribute:: rttmonstatscapturedistindex  <key>
            
            	This object uniquely defines a statistical distribution bucket for a given value of rttMonStatsCaptureHopIndex.  For a particular value of rttMonStatsCaptureHopIndex, the agent assigns the first instance of a distribution a value of 1, then second instance a value of 2, and so on.  The sequence keeps incrementing until the number of  statistics distribution intervals equals  rttMonStatisticsAdminNumDistBuckets value, then all values that fall above the last interval will be placed into the last interval.  Each of these Statistics Distribution Buckets contain  the results of each completion as defined by  rttMonStatisticsAdminDistInterval object
            	**type**\:  int
            
            	**range:** 1..20
            
            .. attribute:: rttmonstatscapturecompletions
            
            	The number of RTT operations that have completed without an error and without timing out.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscapturecompletiontimemax
            
            	The maximum completion time of any RTT operation which completes successfully
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturecompletiontimemin
            
            	The minimum completion time of any RTT operation which completes successfully
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscaptureoverthresholds
            
            	The number of RTT operations successfully completed, but in excess of rttMonCtrlAdminThreshold.  This number is a subset of the accumulation of all  rttMonStatsCaptureCompletions.  The operation time  of these completed operations will be accumulated.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscapturesumcompletiontime
            
            	The accumulated completion time of RTT operations which complete successfully
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonstatscapturesumcompletiontime2high
            
            	The high order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  See the rttMonStatsCaptureSumCompletionTime2Low object for a definition of Low/High Order
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonstatscapturesumcompletiontime2low
            
            	The low order 32 bits of the accumulated squares of completion times (in milliseconds) of RTT  operations which complete successfully.  Low/High order is defined where the binary number will look as follows\: \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| High order 32 bits    \| Low order 32 bits     \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- For example the number 4294967296 would have all Low order bits as '0' and the rightmost High order bit will be 1 (zeros,1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry, self).__init__()

                self.yang_name = "rttMonStatsCaptureEntry"
                self.yang_parent_name = "rttMonStatsCaptureTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonstatscapturestarttimeindex = YLeaf(YType.uint32, "rttMonStatsCaptureStartTimeIndex")

                self.rttmonstatscapturepathindex = YLeaf(YType.int32, "rttMonStatsCapturePathIndex")

                self.rttmonstatscapturehopindex = YLeaf(YType.int32, "rttMonStatsCaptureHopIndex")

                self.rttmonstatscapturedistindex = YLeaf(YType.int32, "rttMonStatsCaptureDistIndex")

                self.rttmonstatscapturecompletions = YLeaf(YType.int32, "rttMonStatsCaptureCompletions")

                self.rttmonstatscapturecompletiontimemax = YLeaf(YType.uint32, "rttMonStatsCaptureCompletionTimeMax")

                self.rttmonstatscapturecompletiontimemin = YLeaf(YType.uint32, "rttMonStatsCaptureCompletionTimeMin")

                self.rttmonstatscaptureoverthresholds = YLeaf(YType.int32, "rttMonStatsCaptureOverThresholds")

                self.rttmonstatscapturesumcompletiontime = YLeaf(YType.uint32, "rttMonStatsCaptureSumCompletionTime")

                self.rttmonstatscapturesumcompletiontime2high = YLeaf(YType.uint32, "rttMonStatsCaptureSumCompletionTime2High")

                self.rttmonstatscapturesumcompletiontime2low = YLeaf(YType.uint32, "rttMonStatsCaptureSumCompletionTime2Low")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonstatscapturestarttimeindex",
                                "rttmonstatscapturepathindex",
                                "rttmonstatscapturehopindex",
                                "rttmonstatscapturedistindex",
                                "rttmonstatscapturecompletions",
                                "rttmonstatscapturecompletiontimemax",
                                "rttmonstatscapturecompletiontimemin",
                                "rttmonstatscaptureoverthresholds",
                                "rttmonstatscapturesumcompletiontime",
                                "rttmonstatscapturesumcompletiontime2high",
                                "rttmonstatscapturesumcompletiontime2low") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonstatscapturestarttimeindex.is_set or
                    self.rttmonstatscapturepathindex.is_set or
                    self.rttmonstatscapturehopindex.is_set or
                    self.rttmonstatscapturedistindex.is_set or
                    self.rttmonstatscapturecompletions.is_set or
                    self.rttmonstatscapturecompletiontimemax.is_set or
                    self.rttmonstatscapturecompletiontimemin.is_set or
                    self.rttmonstatscaptureoverthresholds.is_set or
                    self.rttmonstatscapturesumcompletiontime.is_set or
                    self.rttmonstatscapturesumcompletiontime2high.is_set or
                    self.rttmonstatscapturesumcompletiontime2low.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturepathindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturehopindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturedistindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturecompletions.yfilter != YFilter.not_set or
                    self.rttmonstatscapturecompletiontimemax.yfilter != YFilter.not_set or
                    self.rttmonstatscapturecompletiontimemin.yfilter != YFilter.not_set or
                    self.rttmonstatscaptureoverthresholds.yfilter != YFilter.not_set or
                    self.rttmonstatscapturesumcompletiontime.yfilter != YFilter.not_set or
                    self.rttmonstatscapturesumcompletiontime2high.yfilter != YFilter.not_set or
                    self.rttmonstatscapturesumcompletiontime2low.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonStatsCaptureEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonStatsCaptureStartTimeIndex='" + self.rttmonstatscapturestarttimeindex.get() + "']" + "[rttMonStatsCapturePathIndex='" + self.rttmonstatscapturepathindex.get() + "']" + "[rttMonStatsCaptureHopIndex='" + self.rttmonstatscapturehopindex.get() + "']" + "[rttMonStatsCaptureDistIndex='" + self.rttmonstatscapturedistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsCaptureTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonstatscapturestarttimeindex.is_set or self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturestarttimeindex.get_name_leafdata())
                if (self.rttmonstatscapturepathindex.is_set or self.rttmonstatscapturepathindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturepathindex.get_name_leafdata())
                if (self.rttmonstatscapturehopindex.is_set or self.rttmonstatscapturehopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturehopindex.get_name_leafdata())
                if (self.rttmonstatscapturedistindex.is_set or self.rttmonstatscapturedistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturedistindex.get_name_leafdata())
                if (self.rttmonstatscapturecompletions.is_set or self.rttmonstatscapturecompletions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturecompletions.get_name_leafdata())
                if (self.rttmonstatscapturecompletiontimemax.is_set or self.rttmonstatscapturecompletiontimemax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturecompletiontimemax.get_name_leafdata())
                if (self.rttmonstatscapturecompletiontimemin.is_set or self.rttmonstatscapturecompletiontimemin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturecompletiontimemin.get_name_leafdata())
                if (self.rttmonstatscaptureoverthresholds.is_set or self.rttmonstatscaptureoverthresholds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscaptureoverthresholds.get_name_leafdata())
                if (self.rttmonstatscapturesumcompletiontime.is_set or self.rttmonstatscapturesumcompletiontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturesumcompletiontime.get_name_leafdata())
                if (self.rttmonstatscapturesumcompletiontime2high.is_set or self.rttmonstatscapturesumcompletiontime2high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturesumcompletiontime2high.get_name_leafdata())
                if (self.rttmonstatscapturesumcompletiontime2low.is_set or self.rttmonstatscapturesumcompletiontime2low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturesumcompletiontime2low.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonStatsCaptureStartTimeIndex" or name == "rttMonStatsCapturePathIndex" or name == "rttMonStatsCaptureHopIndex" or name == "rttMonStatsCaptureDistIndex" or name == "rttMonStatsCaptureCompletions" or name == "rttMonStatsCaptureCompletionTimeMax" or name == "rttMonStatsCaptureCompletionTimeMin" or name == "rttMonStatsCaptureOverThresholds" or name == "rttMonStatsCaptureSumCompletionTime" or name == "rttMonStatsCaptureSumCompletionTime2High" or name == "rttMonStatsCaptureSumCompletionTime2Low"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureStartTimeIndex"):
                    self.rttmonstatscapturestarttimeindex = value
                    self.rttmonstatscapturestarttimeindex.value_namespace = name_space
                    self.rttmonstatscapturestarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCapturePathIndex"):
                    self.rttmonstatscapturepathindex = value
                    self.rttmonstatscapturepathindex.value_namespace = name_space
                    self.rttmonstatscapturepathindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureHopIndex"):
                    self.rttmonstatscapturehopindex = value
                    self.rttmonstatscapturehopindex.value_namespace = name_space
                    self.rttmonstatscapturehopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureDistIndex"):
                    self.rttmonstatscapturedistindex = value
                    self.rttmonstatscapturedistindex.value_namespace = name_space
                    self.rttmonstatscapturedistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureCompletions"):
                    self.rttmonstatscapturecompletions = value
                    self.rttmonstatscapturecompletions.value_namespace = name_space
                    self.rttmonstatscapturecompletions.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureCompletionTimeMax"):
                    self.rttmonstatscapturecompletiontimemax = value
                    self.rttmonstatscapturecompletiontimemax.value_namespace = name_space
                    self.rttmonstatscapturecompletiontimemax.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureCompletionTimeMin"):
                    self.rttmonstatscapturecompletiontimemin = value
                    self.rttmonstatscapturecompletiontimemin.value_namespace = name_space
                    self.rttmonstatscapturecompletiontimemin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureOverThresholds"):
                    self.rttmonstatscaptureoverthresholds = value
                    self.rttmonstatscaptureoverthresholds.value_namespace = name_space
                    self.rttmonstatscaptureoverthresholds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureSumCompletionTime"):
                    self.rttmonstatscapturesumcompletiontime = value
                    self.rttmonstatscapturesumcompletiontime.value_namespace = name_space
                    self.rttmonstatscapturesumcompletiontime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureSumCompletionTime2High"):
                    self.rttmonstatscapturesumcompletiontime2high = value
                    self.rttmonstatscapturesumcompletiontime2high.value_namespace = name_space
                    self.rttmonstatscapturesumcompletiontime2high.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureSumCompletionTime2Low"):
                    self.rttmonstatscapturesumcompletiontime2low = value
                    self.rttmonstatscapturesumcompletiontime2low.value_namespace = name_space
                    self.rttmonstatscapturesumcompletiontime2low.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonstatscaptureentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonstatscaptureentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonStatsCaptureTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonStatsCaptureEntry"):
                for c in self.rttmonstatscaptureentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonstatscaptureentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonStatsCaptureEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonstatscollectentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscollecttable.Rttmonstatscollectentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonstatscollecttable, self).__init__()

            self.yang_name = "rttMonStatsCollectTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonstatscollectentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonstatscollecttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonstatscollecttable, self).__setattr__(name, value)


        class Rttmonstatscollectentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry has the exact same behavior as the 
            rttMonStatsCaptureEntry, except it does not keep
            statistical distribution information.
            
            For a complete entry description see
            the rttMonStatsCaptureEntry object.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatscapturepathindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..128
            
            	**refers to**\:  :py:class:`rttmonstatscapturepathindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatscapturehopindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..30
            
            	**refers to**\:  :py:class:`rttmonstatscapturehopindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmoncontrolenableerrors
            
            	The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonControlEnableErrors object is superseded by rttMonStatsCollectCtrlEnErrors
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: rttmonstatscollectaddress
            
            	This object only applies when the RttMonRttType is 'echo', 'pathEcho', 'dlsw', 'udpEcho', 'tcpConnect'.   For all other values of the RttMonRttType, this will be  null.   The object is a string which specifies the address of  the target for the this RTT operation.  This address will be the address of the hop along the  path to the rttMonEchoAdminTargetAddress address,  including rttMonEchoAdminTargetAddress address, or just  the rttMonEchoAdminTargetAddress address, when the  path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type  of RTT operation selected, as specified by the  rttMonEchoAdminProtocol object
            	**type**\:  str
            
            .. attribute:: rttmonstatscollectbusies
            
            	The number of occasions when a RTT operation could not be initiated because a previous RTT operation has not  been completed.  When the RttMonRttType is 'pathEcho' this can occur for both connection oriented protocols and connectionless protocols.  When the RttMonRttType is 'echo' this can only occur for connection oriented protocols such as SNA.   When the initiation of a new operation cannot be started, this object will be incremented and the operation will be omitted.  (The next operation will start at the next  Frequency).  Since, a RTT operation was never initiated,  the completion time of these operations is not  accumulated, nor do they increment  rttMonStatsCaptureCompletions.  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the source  to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectctrlenerrors
            
            	The object is same as rttMonControlEnableErrors, with corrected name for consistency.  The number of occasions when control enable request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectdrops
            
            	The number of occasions when a RTT operation could not be initiated because some necessary internal resource  (for example memory, or SNA subsystem) was not available, or the operation completion could not be recognized.  Since a RTT operation was never initiated or was not recognized, the completion time of these operations  are not accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected  Distribution Bucket).  When the RttMonRttType is 'pathEcho', and this error  occurs and the rttMonStatsCapturePathIndex cannot be  determined, this error will be accumulated in the  source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectnoconnections
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is the number of occasions when a RTT operation could not be initiated because the connection to the target has not  been established.  For all other RttMonRttTypes this object will remain zero.  This cannot occur for connectionless protocols, but may occur for connection oriented protocols, such as SNA.  Since a RTT operation was never initiated, the completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions.   If this error occurs and the rttMonStatsCapturePathIndex cannot be determined, this error will be accumulated in the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectnumdisconnects
            
            	When the RttMonRttType is 'echo' or pathEcho', this object represents the number of times that the target or  hop along the path to a target became disconnected.  For all other values of RttMonRttType, this object will remain zero.  For connectionless protocols this has no meaning, and will consequently remain 0.  When rttMonEchoAdminProtocol is one of snaRUEcho, this is the number of times that an LU\-SSCP session was lost,  for snaLU0EchoAppl, snaLU2EchoAppl, snaLu62Echo, and for  snaLU62EchoAppl, this is the number of times that LU\-LU  session was lost.  Since this error does not indicate any information about the failure of an RTT operation, no response time  information for this instance will be recorded in the  appropriate objects.  If this error occurs and the rttMonStatsCapturePathIndex  cannot be determined, this error will be accumulated in  the source to target path, that will always exist.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectretrieveerrors
            
            	The object is same as rttMonStatsRetrieveErrors, with corrected name for consistency.  The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectsequenceerrors
            
            	When the RttMonRttType is 'echo' of 'pathEcho' this is the number of RTT operation completions received with  an unexpected sequence identifier.  For all other values of RttMonRttType this object will remain zero.  When this has occurred some of the possible reasons may be\:      \- a duplicate packet was received    \- a response was received after it had timed\-out    \- a corrupted packet was received and was not detected  The completion time of these operations are not  accumulated, nor do they increment  rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollecttimeouts
            
            	The number of occasions when a RTT operation was not completed before a timeout occurred, i.e. rttMonCtrlAdminTimeout was exceeded.  Since the RTT operation was never completed, the  completion time of these operations are not accumulated, nor do they increment rttMonStatsCaptureCompletions (in  any of the statistics distribution buckets).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatscollectverifyerrors
            
            	The number of RTT operation completions received with data that does not compare with the expected data.  The  completion time of these operations are not accumulated,  nor do they increment rttMonStatsCaptureCompletions (in the expected Distribution Bucket).  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatsretrieveerrors
            
            	The number of occasions when stats retrieval request failed. Currently it is used for multicast operation type.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object. rttMonStatsRetrieveErrors object is superseded by rttMonStatsCollectRetrieveErrors
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonstatscollecttable.Rttmonstatscollectentry, self).__init__()

                self.yang_name = "rttMonStatsCollectEntry"
                self.yang_parent_name = "rttMonStatsCollectTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonstatscapturestarttimeindex = YLeaf(YType.str, "rttMonStatsCaptureStartTimeIndex")

                self.rttmonstatscapturepathindex = YLeaf(YType.str, "rttMonStatsCapturePathIndex")

                self.rttmonstatscapturehopindex = YLeaf(YType.str, "rttMonStatsCaptureHopIndex")

                self.rttmoncontrolenableerrors = YLeaf(YType.int32, "rttMonControlEnableErrors")

                self.rttmonstatscollectaddress = YLeaf(YType.str, "rttMonStatsCollectAddress")

                self.rttmonstatscollectbusies = YLeaf(YType.int32, "rttMonStatsCollectBusies")

                self.rttmonstatscollectctrlenerrors = YLeaf(YType.int32, "rttMonStatsCollectCtrlEnErrors")

                self.rttmonstatscollectdrops = YLeaf(YType.int32, "rttMonStatsCollectDrops")

                self.rttmonstatscollectnoconnections = YLeaf(YType.int32, "rttMonStatsCollectNoConnections")

                self.rttmonstatscollectnumdisconnects = YLeaf(YType.int32, "rttMonStatsCollectNumDisconnects")

                self.rttmonstatscollectretrieveerrors = YLeaf(YType.int32, "rttMonStatsCollectRetrieveErrors")

                self.rttmonstatscollectsequenceerrors = YLeaf(YType.int32, "rttMonStatsCollectSequenceErrors")

                self.rttmonstatscollecttimeouts = YLeaf(YType.int32, "rttMonStatsCollectTimeouts")

                self.rttmonstatscollectverifyerrors = YLeaf(YType.int32, "rttMonStatsCollectVerifyErrors")

                self.rttmonstatsretrieveerrors = YLeaf(YType.int32, "rttMonStatsRetrieveErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonstatscapturestarttimeindex",
                                "rttmonstatscapturepathindex",
                                "rttmonstatscapturehopindex",
                                "rttmoncontrolenableerrors",
                                "rttmonstatscollectaddress",
                                "rttmonstatscollectbusies",
                                "rttmonstatscollectctrlenerrors",
                                "rttmonstatscollectdrops",
                                "rttmonstatscollectnoconnections",
                                "rttmonstatscollectnumdisconnects",
                                "rttmonstatscollectretrieveerrors",
                                "rttmonstatscollectsequenceerrors",
                                "rttmonstatscollecttimeouts",
                                "rttmonstatscollectverifyerrors",
                                "rttmonstatsretrieveerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonstatscollecttable.Rttmonstatscollectentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonstatscollecttable.Rttmonstatscollectentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonstatscapturestarttimeindex.is_set or
                    self.rttmonstatscapturepathindex.is_set or
                    self.rttmonstatscapturehopindex.is_set or
                    self.rttmoncontrolenableerrors.is_set or
                    self.rttmonstatscollectaddress.is_set or
                    self.rttmonstatscollectbusies.is_set or
                    self.rttmonstatscollectctrlenerrors.is_set or
                    self.rttmonstatscollectdrops.is_set or
                    self.rttmonstatscollectnoconnections.is_set or
                    self.rttmonstatscollectnumdisconnects.is_set or
                    self.rttmonstatscollectretrieveerrors.is_set or
                    self.rttmonstatscollectsequenceerrors.is_set or
                    self.rttmonstatscollecttimeouts.is_set or
                    self.rttmonstatscollectverifyerrors.is_set or
                    self.rttmonstatsretrieveerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturepathindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturehopindex.yfilter != YFilter.not_set or
                    self.rttmoncontrolenableerrors.yfilter != YFilter.not_set or
                    self.rttmonstatscollectaddress.yfilter != YFilter.not_set or
                    self.rttmonstatscollectbusies.yfilter != YFilter.not_set or
                    self.rttmonstatscollectctrlenerrors.yfilter != YFilter.not_set or
                    self.rttmonstatscollectdrops.yfilter != YFilter.not_set or
                    self.rttmonstatscollectnoconnections.yfilter != YFilter.not_set or
                    self.rttmonstatscollectnumdisconnects.yfilter != YFilter.not_set or
                    self.rttmonstatscollectretrieveerrors.yfilter != YFilter.not_set or
                    self.rttmonstatscollectsequenceerrors.yfilter != YFilter.not_set or
                    self.rttmonstatscollecttimeouts.yfilter != YFilter.not_set or
                    self.rttmonstatscollectverifyerrors.yfilter != YFilter.not_set or
                    self.rttmonstatsretrieveerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonStatsCollectEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonStatsCaptureStartTimeIndex='" + self.rttmonstatscapturestarttimeindex.get() + "']" + "[rttMonStatsCapturePathIndex='" + self.rttmonstatscapturepathindex.get() + "']" + "[rttMonStatsCaptureHopIndex='" + self.rttmonstatscapturehopindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsCollectTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonstatscapturestarttimeindex.is_set or self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturestarttimeindex.get_name_leafdata())
                if (self.rttmonstatscapturepathindex.is_set or self.rttmonstatscapturepathindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturepathindex.get_name_leafdata())
                if (self.rttmonstatscapturehopindex.is_set or self.rttmonstatscapturehopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturehopindex.get_name_leafdata())
                if (self.rttmoncontrolenableerrors.is_set or self.rttmoncontrolenableerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmoncontrolenableerrors.get_name_leafdata())
                if (self.rttmonstatscollectaddress.is_set or self.rttmonstatscollectaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectaddress.get_name_leafdata())
                if (self.rttmonstatscollectbusies.is_set or self.rttmonstatscollectbusies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectbusies.get_name_leafdata())
                if (self.rttmonstatscollectctrlenerrors.is_set or self.rttmonstatscollectctrlenerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectctrlenerrors.get_name_leafdata())
                if (self.rttmonstatscollectdrops.is_set or self.rttmonstatscollectdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectdrops.get_name_leafdata())
                if (self.rttmonstatscollectnoconnections.is_set or self.rttmonstatscollectnoconnections.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectnoconnections.get_name_leafdata())
                if (self.rttmonstatscollectnumdisconnects.is_set or self.rttmonstatscollectnumdisconnects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectnumdisconnects.get_name_leafdata())
                if (self.rttmonstatscollectretrieveerrors.is_set or self.rttmonstatscollectretrieveerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectretrieveerrors.get_name_leafdata())
                if (self.rttmonstatscollectsequenceerrors.is_set or self.rttmonstatscollectsequenceerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectsequenceerrors.get_name_leafdata())
                if (self.rttmonstatscollecttimeouts.is_set or self.rttmonstatscollecttimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollecttimeouts.get_name_leafdata())
                if (self.rttmonstatscollectverifyerrors.is_set or self.rttmonstatscollectverifyerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscollectverifyerrors.get_name_leafdata())
                if (self.rttmonstatsretrieveerrors.is_set or self.rttmonstatsretrieveerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatsretrieveerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonStatsCaptureStartTimeIndex" or name == "rttMonStatsCapturePathIndex" or name == "rttMonStatsCaptureHopIndex" or name == "rttMonControlEnableErrors" or name == "rttMonStatsCollectAddress" or name == "rttMonStatsCollectBusies" or name == "rttMonStatsCollectCtrlEnErrors" or name == "rttMonStatsCollectDrops" or name == "rttMonStatsCollectNoConnections" or name == "rttMonStatsCollectNumDisconnects" or name == "rttMonStatsCollectRetrieveErrors" or name == "rttMonStatsCollectSequenceErrors" or name == "rttMonStatsCollectTimeouts" or name == "rttMonStatsCollectVerifyErrors" or name == "rttMonStatsRetrieveErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureStartTimeIndex"):
                    self.rttmonstatscapturestarttimeindex = value
                    self.rttmonstatscapturestarttimeindex.value_namespace = name_space
                    self.rttmonstatscapturestarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCapturePathIndex"):
                    self.rttmonstatscapturepathindex = value
                    self.rttmonstatscapturepathindex.value_namespace = name_space
                    self.rttmonstatscapturepathindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureHopIndex"):
                    self.rttmonstatscapturehopindex = value
                    self.rttmonstatscapturehopindex.value_namespace = name_space
                    self.rttmonstatscapturehopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonControlEnableErrors"):
                    self.rttmoncontrolenableerrors = value
                    self.rttmoncontrolenableerrors.value_namespace = name_space
                    self.rttmoncontrolenableerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectAddress"):
                    self.rttmonstatscollectaddress = value
                    self.rttmonstatscollectaddress.value_namespace = name_space
                    self.rttmonstatscollectaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectBusies"):
                    self.rttmonstatscollectbusies = value
                    self.rttmonstatscollectbusies.value_namespace = name_space
                    self.rttmonstatscollectbusies.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectCtrlEnErrors"):
                    self.rttmonstatscollectctrlenerrors = value
                    self.rttmonstatscollectctrlenerrors.value_namespace = name_space
                    self.rttmonstatscollectctrlenerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectDrops"):
                    self.rttmonstatscollectdrops = value
                    self.rttmonstatscollectdrops.value_namespace = name_space
                    self.rttmonstatscollectdrops.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectNoConnections"):
                    self.rttmonstatscollectnoconnections = value
                    self.rttmonstatscollectnoconnections.value_namespace = name_space
                    self.rttmonstatscollectnoconnections.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectNumDisconnects"):
                    self.rttmonstatscollectnumdisconnects = value
                    self.rttmonstatscollectnumdisconnects.value_namespace = name_space
                    self.rttmonstatscollectnumdisconnects.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectRetrieveErrors"):
                    self.rttmonstatscollectretrieveerrors = value
                    self.rttmonstatscollectretrieveerrors.value_namespace = name_space
                    self.rttmonstatscollectretrieveerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectSequenceErrors"):
                    self.rttmonstatscollectsequenceerrors = value
                    self.rttmonstatscollectsequenceerrors.value_namespace = name_space
                    self.rttmonstatscollectsequenceerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectTimeouts"):
                    self.rttmonstatscollecttimeouts = value
                    self.rttmonstatscollecttimeouts.value_namespace = name_space
                    self.rttmonstatscollecttimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCollectVerifyErrors"):
                    self.rttmonstatscollectverifyerrors = value
                    self.rttmonstatscollectverifyerrors.value_namespace = name_space
                    self.rttmonstatscollectverifyerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsRetrieveErrors"):
                    self.rttmonstatsretrieveerrors = value
                    self.rttmonstatsretrieveerrors.value_namespace = name_space
                    self.rttmonstatsretrieveerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonstatscollectentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonstatscollectentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonStatsCollectTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonStatsCollectEntry"):
                for c in self.rttmonstatscollectentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonstatscollecttable.Rttmonstatscollectentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonstatscollectentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonStatsCollectEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonstatstotalsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatstotalstable.Rttmonstatstotalsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonstatstotalstable, self).__init__()

            self.yang_name = "rttMonStatsTotalsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonstatstotalsentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonstatstotalstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonstatstotalstable, self).__setattr__(name, value)


        class Rttmonstatstotalsentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry has the exact same behavior as the 
            rttMonStatsCaptureEntry, except it only keeps
            60 minute group values.
            
            For a complete entry description see
            the rttMonStatsCaptureEntry object.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonstatscapturestarttimeindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`rttmonstatscapturestarttimeindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonstatscapturetable.Rttmonstatscaptureentry>`
            
            .. attribute:: rttmonstatstotalselapsedtime
            
            	The length of time since this conceptual statistics row was created
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonstatstotalsinitiations
            
            	The number of RTT operations that have been initiated.  This number includes all RTT operations which succeed  or fail for whatever reason.  This object has the special behavior as defined by the ROLLOVER NOTE in the DESCRIPTION of the ciscoRttMonMIB object
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonstatstotalstable.Rttmonstatstotalsentry, self).__init__()

                self.yang_name = "rttMonStatsTotalsEntry"
                self.yang_parent_name = "rttMonStatsTotalsTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonstatscapturestarttimeindex = YLeaf(YType.str, "rttMonStatsCaptureStartTimeIndex")

                self.rttmonstatstotalselapsedtime = YLeaf(YType.int32, "rttMonStatsTotalsElapsedTime")

                self.rttmonstatstotalsinitiations = YLeaf(YType.int32, "rttMonStatsTotalsInitiations")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonstatscapturestarttimeindex",
                                "rttmonstatstotalselapsedtime",
                                "rttmonstatstotalsinitiations") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonstatstotalstable.Rttmonstatstotalsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonstatstotalstable.Rttmonstatstotalsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonstatscapturestarttimeindex.is_set or
                    self.rttmonstatstotalselapsedtime.is_set or
                    self.rttmonstatstotalsinitiations.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonstatstotalselapsedtime.yfilter != YFilter.not_set or
                    self.rttmonstatstotalsinitiations.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonStatsTotalsEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonStatsCaptureStartTimeIndex='" + self.rttmonstatscapturestarttimeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonStatsTotalsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonstatscapturestarttimeindex.is_set or self.rttmonstatscapturestarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatscapturestarttimeindex.get_name_leafdata())
                if (self.rttmonstatstotalselapsedtime.is_set or self.rttmonstatstotalselapsedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatstotalselapsedtime.get_name_leafdata())
                if (self.rttmonstatstotalsinitiations.is_set or self.rttmonstatstotalsinitiations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonstatstotalsinitiations.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonStatsCaptureStartTimeIndex" or name == "rttMonStatsTotalsElapsedTime" or name == "rttMonStatsTotalsInitiations"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsCaptureStartTimeIndex"):
                    self.rttmonstatscapturestarttimeindex = value
                    self.rttmonstatscapturestarttimeindex.value_namespace = name_space
                    self.rttmonstatscapturestarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsTotalsElapsedTime"):
                    self.rttmonstatstotalselapsedtime = value
                    self.rttmonstatstotalselapsedtime.value_namespace = name_space
                    self.rttmonstatstotalselapsedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonStatsTotalsInitiations"):
                    self.rttmonstatstotalsinitiations = value
                    self.rttmonstatstotalsinitiations.value_namespace = name_space
                    self.rttmonstatstotalsinitiations.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonstatstotalsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonstatstotalsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonStatsTotalsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonStatsTotalsEntry"):
                for c in self.rttmonstatstotalsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonstatstotalstable.Rttmonstatstotalsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonstatstotalsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonStatsTotalsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonhttpstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonhttpstatstable.Rttmonhttpstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonhttpstatstable, self).__init__()

            self.yang_name = "rttMonHTTPStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonhttpstatsentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonhttpstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonhttpstatstable, self).__setattr__(name, value)


        class Rttmonhttpstatsentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is http. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonhttpstatsstarttimeindex  <key>
            
            	This is the time when this row was created. This index uniquely identifies a HTTP Stats row in the  rttMonHTTPStatsTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsbusies
            
            	The number of occasions when an HTTP operation could not be initiated because a previous HTTP operation has not been completed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatscompletions
            
            	The number of HTTP operations that have completed successfully
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsdnsqueryerror
            
            	The number of requests that had DNS Query errors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsdnsrttsum
            
            	The sum of RTT taken to perform DNS query within the HTTP operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsdnsservertimeout
            
            	The number of requests that could not connect to the DNS Server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatserror
            
            	The number of occasions when a HTTP operation could not be initiated because an internal error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatshttperror
            
            	The number of requests that had HTTP errors while downloading the base page
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsmessagebodyoctetssum
            
            	The sum of the size of the message body received as a response to the HTTP request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsoverthresholds
            
            	The number of HTTP operations that violate threshold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttmax
            
            	The maximum RTT taken to perform HTTP operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhttpstatsrttmin
            
            	The minimum RTT taken to perform HTTP operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum
            
            	The sum of HTTP operations that are successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum2high
            
            	The sum of squares of the RTT's that are successfully measured (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatsrttsum2low
            
            	The sum of squares of the RTT's that are successfully measured (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstcpconnectrttsum
            
            	The sum of RTT taken to connect to the HTTP server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstcpconnecttimeout
            
            	The number of requests that could not connect to the the HTTP Server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstransactionrttsum
            
            	The sum of RTT taken to download the object specified by URL
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhttpstatstransactiontimeout
            
            	The number of requests that timed out during HTTP transaction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonhttpstatstable.Rttmonhttpstatsentry, self).__init__()

                self.yang_name = "rttMonHTTPStatsEntry"
                self.yang_parent_name = "rttMonHTTPStatsTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonhttpstatsstarttimeindex = YLeaf(YType.uint32, "rttMonHTTPStatsStartTimeIndex")

                self.rttmonhttpstatsbusies = YLeaf(YType.uint32, "rttMonHTTPStatsBusies")

                self.rttmonhttpstatscompletions = YLeaf(YType.uint32, "rttMonHTTPStatsCompletions")

                self.rttmonhttpstatsdnsqueryerror = YLeaf(YType.uint32, "rttMonHTTPStatsDNSQueryError")

                self.rttmonhttpstatsdnsrttsum = YLeaf(YType.uint32, "rttMonHTTPStatsDNSRTTSum")

                self.rttmonhttpstatsdnsservertimeout = YLeaf(YType.uint32, "rttMonHTTPStatsDNSServerTimeout")

                self.rttmonhttpstatserror = YLeaf(YType.uint32, "rttMonHTTPStatsError")

                self.rttmonhttpstatshttperror = YLeaf(YType.uint32, "rttMonHTTPStatsHTTPError")

                self.rttmonhttpstatsmessagebodyoctetssum = YLeaf(YType.uint32, "rttMonHTTPStatsMessageBodyOctetsSum")

                self.rttmonhttpstatsoverthresholds = YLeaf(YType.uint32, "rttMonHTTPStatsOverThresholds")

                self.rttmonhttpstatsrttmax = YLeaf(YType.uint32, "rttMonHTTPStatsRTTMax")

                self.rttmonhttpstatsrttmin = YLeaf(YType.uint32, "rttMonHTTPStatsRTTMin")

                self.rttmonhttpstatsrttsum = YLeaf(YType.uint32, "rttMonHTTPStatsRTTSum")

                self.rttmonhttpstatsrttsum2high = YLeaf(YType.uint32, "rttMonHTTPStatsRTTSum2High")

                self.rttmonhttpstatsrttsum2low = YLeaf(YType.uint32, "rttMonHTTPStatsRTTSum2Low")

                self.rttmonhttpstatstcpconnectrttsum = YLeaf(YType.uint32, "rttMonHTTPStatsTCPConnectRTTSum")

                self.rttmonhttpstatstcpconnecttimeout = YLeaf(YType.uint32, "rttMonHTTPStatsTCPConnectTimeout")

                self.rttmonhttpstatstransactionrttsum = YLeaf(YType.uint32, "rttMonHTTPStatsTransactionRTTSum")

                self.rttmonhttpstatstransactiontimeout = YLeaf(YType.uint32, "rttMonHTTPStatsTransactionTimeout")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonhttpstatsstarttimeindex",
                                "rttmonhttpstatsbusies",
                                "rttmonhttpstatscompletions",
                                "rttmonhttpstatsdnsqueryerror",
                                "rttmonhttpstatsdnsrttsum",
                                "rttmonhttpstatsdnsservertimeout",
                                "rttmonhttpstatserror",
                                "rttmonhttpstatshttperror",
                                "rttmonhttpstatsmessagebodyoctetssum",
                                "rttmonhttpstatsoverthresholds",
                                "rttmonhttpstatsrttmax",
                                "rttmonhttpstatsrttmin",
                                "rttmonhttpstatsrttsum",
                                "rttmonhttpstatsrttsum2high",
                                "rttmonhttpstatsrttsum2low",
                                "rttmonhttpstatstcpconnectrttsum",
                                "rttmonhttpstatstcpconnecttimeout",
                                "rttmonhttpstatstransactionrttsum",
                                "rttmonhttpstatstransactiontimeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonhttpstatstable.Rttmonhttpstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonhttpstatstable.Rttmonhttpstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonhttpstatsstarttimeindex.is_set or
                    self.rttmonhttpstatsbusies.is_set or
                    self.rttmonhttpstatscompletions.is_set or
                    self.rttmonhttpstatsdnsqueryerror.is_set or
                    self.rttmonhttpstatsdnsrttsum.is_set or
                    self.rttmonhttpstatsdnsservertimeout.is_set or
                    self.rttmonhttpstatserror.is_set or
                    self.rttmonhttpstatshttperror.is_set or
                    self.rttmonhttpstatsmessagebodyoctetssum.is_set or
                    self.rttmonhttpstatsoverthresholds.is_set or
                    self.rttmonhttpstatsrttmax.is_set or
                    self.rttmonhttpstatsrttmin.is_set or
                    self.rttmonhttpstatsrttsum.is_set or
                    self.rttmonhttpstatsrttsum2high.is_set or
                    self.rttmonhttpstatsrttsum2low.is_set or
                    self.rttmonhttpstatstcpconnectrttsum.is_set or
                    self.rttmonhttpstatstcpconnecttimeout.is_set or
                    self.rttmonhttpstatstransactionrttsum.is_set or
                    self.rttmonhttpstatstransactiontimeout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsstarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsbusies.yfilter != YFilter.not_set or
                    self.rttmonhttpstatscompletions.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsdnsqueryerror.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsdnsrttsum.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsdnsservertimeout.yfilter != YFilter.not_set or
                    self.rttmonhttpstatserror.yfilter != YFilter.not_set or
                    self.rttmonhttpstatshttperror.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsmessagebodyoctetssum.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsoverthresholds.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsrttmax.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsrttmin.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsrttsum.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsrttsum2high.yfilter != YFilter.not_set or
                    self.rttmonhttpstatsrttsum2low.yfilter != YFilter.not_set or
                    self.rttmonhttpstatstcpconnectrttsum.yfilter != YFilter.not_set or
                    self.rttmonhttpstatstcpconnecttimeout.yfilter != YFilter.not_set or
                    self.rttmonhttpstatstransactionrttsum.yfilter != YFilter.not_set or
                    self.rttmonhttpstatstransactiontimeout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonHTTPStatsEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonHTTPStatsStartTimeIndex='" + self.rttmonhttpstatsstarttimeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonHTTPStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonhttpstatsstarttimeindex.is_set or self.rttmonhttpstatsstarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsstarttimeindex.get_name_leafdata())
                if (self.rttmonhttpstatsbusies.is_set or self.rttmonhttpstatsbusies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsbusies.get_name_leafdata())
                if (self.rttmonhttpstatscompletions.is_set or self.rttmonhttpstatscompletions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatscompletions.get_name_leafdata())
                if (self.rttmonhttpstatsdnsqueryerror.is_set or self.rttmonhttpstatsdnsqueryerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsdnsqueryerror.get_name_leafdata())
                if (self.rttmonhttpstatsdnsrttsum.is_set or self.rttmonhttpstatsdnsrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsdnsrttsum.get_name_leafdata())
                if (self.rttmonhttpstatsdnsservertimeout.is_set or self.rttmonhttpstatsdnsservertimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsdnsservertimeout.get_name_leafdata())
                if (self.rttmonhttpstatserror.is_set or self.rttmonhttpstatserror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatserror.get_name_leafdata())
                if (self.rttmonhttpstatshttperror.is_set or self.rttmonhttpstatshttperror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatshttperror.get_name_leafdata())
                if (self.rttmonhttpstatsmessagebodyoctetssum.is_set or self.rttmonhttpstatsmessagebodyoctetssum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsmessagebodyoctetssum.get_name_leafdata())
                if (self.rttmonhttpstatsoverthresholds.is_set or self.rttmonhttpstatsoverthresholds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsoverthresholds.get_name_leafdata())
                if (self.rttmonhttpstatsrttmax.is_set or self.rttmonhttpstatsrttmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsrttmax.get_name_leafdata())
                if (self.rttmonhttpstatsrttmin.is_set or self.rttmonhttpstatsrttmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsrttmin.get_name_leafdata())
                if (self.rttmonhttpstatsrttsum.is_set or self.rttmonhttpstatsrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsrttsum.get_name_leafdata())
                if (self.rttmonhttpstatsrttsum2high.is_set or self.rttmonhttpstatsrttsum2high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsrttsum2high.get_name_leafdata())
                if (self.rttmonhttpstatsrttsum2low.is_set or self.rttmonhttpstatsrttsum2low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatsrttsum2low.get_name_leafdata())
                if (self.rttmonhttpstatstcpconnectrttsum.is_set or self.rttmonhttpstatstcpconnectrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatstcpconnectrttsum.get_name_leafdata())
                if (self.rttmonhttpstatstcpconnecttimeout.is_set or self.rttmonhttpstatstcpconnecttimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatstcpconnecttimeout.get_name_leafdata())
                if (self.rttmonhttpstatstransactionrttsum.is_set or self.rttmonhttpstatstransactionrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatstransactionrttsum.get_name_leafdata())
                if (self.rttmonhttpstatstransactiontimeout.is_set or self.rttmonhttpstatstransactiontimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhttpstatstransactiontimeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonHTTPStatsStartTimeIndex" or name == "rttMonHTTPStatsBusies" or name == "rttMonHTTPStatsCompletions" or name == "rttMonHTTPStatsDNSQueryError" or name == "rttMonHTTPStatsDNSRTTSum" or name == "rttMonHTTPStatsDNSServerTimeout" or name == "rttMonHTTPStatsError" or name == "rttMonHTTPStatsHTTPError" or name == "rttMonHTTPStatsMessageBodyOctetsSum" or name == "rttMonHTTPStatsOverThresholds" or name == "rttMonHTTPStatsRTTMax" or name == "rttMonHTTPStatsRTTMin" or name == "rttMonHTTPStatsRTTSum" or name == "rttMonHTTPStatsRTTSum2High" or name == "rttMonHTTPStatsRTTSum2Low" or name == "rttMonHTTPStatsTCPConnectRTTSum" or name == "rttMonHTTPStatsTCPConnectTimeout" or name == "rttMonHTTPStatsTransactionRTTSum" or name == "rttMonHTTPStatsTransactionTimeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsStartTimeIndex"):
                    self.rttmonhttpstatsstarttimeindex = value
                    self.rttmonhttpstatsstarttimeindex.value_namespace = name_space
                    self.rttmonhttpstatsstarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsBusies"):
                    self.rttmonhttpstatsbusies = value
                    self.rttmonhttpstatsbusies.value_namespace = name_space
                    self.rttmonhttpstatsbusies.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsCompletions"):
                    self.rttmonhttpstatscompletions = value
                    self.rttmonhttpstatscompletions.value_namespace = name_space
                    self.rttmonhttpstatscompletions.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsDNSQueryError"):
                    self.rttmonhttpstatsdnsqueryerror = value
                    self.rttmonhttpstatsdnsqueryerror.value_namespace = name_space
                    self.rttmonhttpstatsdnsqueryerror.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsDNSRTTSum"):
                    self.rttmonhttpstatsdnsrttsum = value
                    self.rttmonhttpstatsdnsrttsum.value_namespace = name_space
                    self.rttmonhttpstatsdnsrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsDNSServerTimeout"):
                    self.rttmonhttpstatsdnsservertimeout = value
                    self.rttmonhttpstatsdnsservertimeout.value_namespace = name_space
                    self.rttmonhttpstatsdnsservertimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsError"):
                    self.rttmonhttpstatserror = value
                    self.rttmonhttpstatserror.value_namespace = name_space
                    self.rttmonhttpstatserror.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsHTTPError"):
                    self.rttmonhttpstatshttperror = value
                    self.rttmonhttpstatshttperror.value_namespace = name_space
                    self.rttmonhttpstatshttperror.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsMessageBodyOctetsSum"):
                    self.rttmonhttpstatsmessagebodyoctetssum = value
                    self.rttmonhttpstatsmessagebodyoctetssum.value_namespace = name_space
                    self.rttmonhttpstatsmessagebodyoctetssum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsOverThresholds"):
                    self.rttmonhttpstatsoverthresholds = value
                    self.rttmonhttpstatsoverthresholds.value_namespace = name_space
                    self.rttmonhttpstatsoverthresholds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsRTTMax"):
                    self.rttmonhttpstatsrttmax = value
                    self.rttmonhttpstatsrttmax.value_namespace = name_space
                    self.rttmonhttpstatsrttmax.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsRTTMin"):
                    self.rttmonhttpstatsrttmin = value
                    self.rttmonhttpstatsrttmin.value_namespace = name_space
                    self.rttmonhttpstatsrttmin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsRTTSum"):
                    self.rttmonhttpstatsrttsum = value
                    self.rttmonhttpstatsrttsum.value_namespace = name_space
                    self.rttmonhttpstatsrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsRTTSum2High"):
                    self.rttmonhttpstatsrttsum2high = value
                    self.rttmonhttpstatsrttsum2high.value_namespace = name_space
                    self.rttmonhttpstatsrttsum2high.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsRTTSum2Low"):
                    self.rttmonhttpstatsrttsum2low = value
                    self.rttmonhttpstatsrttsum2low.value_namespace = name_space
                    self.rttmonhttpstatsrttsum2low.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsTCPConnectRTTSum"):
                    self.rttmonhttpstatstcpconnectrttsum = value
                    self.rttmonhttpstatstcpconnectrttsum.value_namespace = name_space
                    self.rttmonhttpstatstcpconnectrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsTCPConnectTimeout"):
                    self.rttmonhttpstatstcpconnecttimeout = value
                    self.rttmonhttpstatstcpconnecttimeout.value_namespace = name_space
                    self.rttmonhttpstatstcpconnecttimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsTransactionRTTSum"):
                    self.rttmonhttpstatstransactionrttsum = value
                    self.rttmonhttpstatstransactionrttsum.value_namespace = name_space
                    self.rttmonhttpstatstransactionrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHTTPStatsTransactionTimeout"):
                    self.rttmonhttpstatstransactiontimeout = value
                    self.rttmonhttpstatstransactiontimeout.value_namespace = name_space
                    self.rttmonhttpstatstransactiontimeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonhttpstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonhttpstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonHTTPStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonHTTPStatsEntry"):
                for c in self.rttmonhttpstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonhttpstatstable.Rttmonhttpstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonhttpstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonHTTPStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonjitterstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonjitterstatstable.Rttmonjitterstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonjitterstatstable, self).__init__()

            self.yang_name = "rttMonJitterStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonjitterstatsentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonjitterstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonjitterstatstable, self).__setattr__(name, value)


        class Rttmonjitterstatsentry(Entity):
            """
            A list of objects which accumulate the results of a
            series of RTT operations over a 60 minute time period.
            
            This entry is created only if the rttMonCtrlAdminRttType 
            is jitter. The operation of this table is same as that of
            rttMonStatsCaptureTable.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonjitterstatsstarttimeindex  <key>
            
            	The time when this row was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjitter
            
            	The average of positive and negative jitter values for SD and DS direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjitterds
            
            	The average of positive and negative jitter values in DS direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsavgjittersd
            
            	The average of positive and negative jitter values in SD direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsbusies
            
            	The number of occasions when a jitter operation could not be initiated because a previous jitter operation has not been completed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatscompletions
            
            	The number of jitter operation that have completed successfully
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatserror
            
            	The number of occasions when a jitter operation could not be initiated because an internal error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsiajin
            
            	Interarrival Jitter (RFC 1889) at sender
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsiajout
            
            	Interarrival Jitter (RFC 1889) at responder
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxoficpif
            
            	The maximum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofmos
            
            	The maximum of all MOS values for the jitter operations in hunderds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonjitterstatsmaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofnegativessd
            
            	The maximum of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsmaxofpositivessd
            
            	The maximum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminoficpif
            
            	The minimum of all ICPIF values for the jitter operations.  This value will be 93 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofmos
            
            	The minimum of all MOS values for the jitter operations in hundreds.  This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonjitterstatsminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofnegativessd
            
            	The minimum of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsminofpositivessd
            
            	The minimum of absolute values of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofow
            
            	The number of one way times that are successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofpositivessd
            
            	The sum of number of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsnumofrtt
            
            	The number of RTT's that are successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsoverthresholds
            
            	The number of jitter operations that violate threshold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowmaxds
            
            	The maximum of all one way times from destination to source. rttMonJitterStatsOWMaxDS object is superseded by rttMonJitterStatsOWMaxDSNew
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxdsnew
            
            	The maximum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMaxDS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowmaxsd
            
            	The maximum of all one way times from source to destination. rttMonJitterStatsOWMaxSD object is superseded by rttMonJitterStatsOWMaxSDNew
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmaxsdnew
            
            	The maximum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMaxSD
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowminds
            
            	The minimum of all one way times from destination to source. rttMonJitterStatsOWMinDS object is superseded by rttMonJitterStatsOWMinDSNew
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowmindsnew
            
            	The minimum of all one way times from destination to source. Replaces deprecated rttMonJitterStatsOWMinDS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowminsd
            
            	The minimum of all one way times from source to destination. rttMonJitterStatsOWMinSD object is superseded by rttMonJitterStatsOWMinSDNew
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: rttmonjitterstatsowminsdnew
            
            	The minimum of all one way times from source to destination. Replaces deprecated rttMonJitterStatsOWMinSD
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2dshigh
            
            	The sum of squares of one way times from destination to source (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2dslow
            
            	The sum of squares of one way times from destination to source (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2sdhigh
            
            	The sum of squares of one way times from source to destination (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsum2sdlow
            
            	The sum of squares of one way times from source to destination (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumds
            
            	The sum of one way times from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumDSHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumdshigh
            
            	The sum of one way times from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonJitterStatsOWSumDS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumsd
            
            	The sum of one way times from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsOWSumSDHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsowsumsdhigh
            
            	The sum of one way times from source to destination (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsOWSumSD
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatspacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum
            
            	The sum of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonJitterStatsRTTSumHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsum2low
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsrttsumhigh
            
            	The sum of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are  stored in rttMonJitterStatsRTTSum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativesdshigh
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativesdslow
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativessdhigh
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2negativessdlow
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivesdshigh
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivesdslow
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivessdhigh
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (high order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssum2positivessdlow
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination (low order 32 bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofnegativessd
            
            	The sum of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatssumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonjitterstatsunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonjitterstatstable.Rttmonjitterstatsentry, self).__init__()

                self.yang_name = "rttMonJitterStatsEntry"
                self.yang_parent_name = "rttMonJitterStatsTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonjitterstatsstarttimeindex = YLeaf(YType.uint32, "rttMonJitterStatsStartTimeIndex")

                self.rttmonjitterstatsavgjitter = YLeaf(YType.uint32, "rttMonJitterStatsAvgJitter")

                self.rttmonjitterstatsavgjitterds = YLeaf(YType.uint32, "rttMonJitterStatsAvgJitterDS")

                self.rttmonjitterstatsavgjittersd = YLeaf(YType.uint32, "rttMonJitterStatsAvgJitterSD")

                self.rttmonjitterstatsbusies = YLeaf(YType.uint32, "rttMonJitterStatsBusies")

                self.rttmonjitterstatscompletions = YLeaf(YType.uint32, "rttMonJitterStatsCompletions")

                self.rttmonjitterstatserror = YLeaf(YType.uint32, "rttMonJitterStatsError")

                self.rttmonjitterstatsiajin = YLeaf(YType.uint32, "rttMonJitterStatsIAJIn")

                self.rttmonjitterstatsiajout = YLeaf(YType.uint32, "rttMonJitterStatsIAJOut")

                self.rttmonjitterstatsmaxoficpif = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfICPIF")

                self.rttmonjitterstatsmaxofmos = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfMOS")

                self.rttmonjitterstatsmaxofnegativesds = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfNegativesDS")

                self.rttmonjitterstatsmaxofnegativessd = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfNegativesSD")

                self.rttmonjitterstatsmaxofpositivesds = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfPositivesDS")

                self.rttmonjitterstatsmaxofpositivessd = YLeaf(YType.uint32, "rttMonJitterStatsMaxOfPositivesSD")

                self.rttmonjitterstatsminoficpif = YLeaf(YType.uint32, "rttMonJitterStatsMinOfICPIF")

                self.rttmonjitterstatsminofmos = YLeaf(YType.uint32, "rttMonJitterStatsMinOfMOS")

                self.rttmonjitterstatsminofnegativesds = YLeaf(YType.uint32, "rttMonJitterStatsMinOfNegativesDS")

                self.rttmonjitterstatsminofnegativessd = YLeaf(YType.uint32, "rttMonJitterStatsMinOfNegativesSD")

                self.rttmonjitterstatsminofpositivesds = YLeaf(YType.uint32, "rttMonJitterStatsMinOfPositivesDS")

                self.rttmonjitterstatsminofpositivessd = YLeaf(YType.uint32, "rttMonJitterStatsMinOfPositivesSD")

                self.rttmonjitterstatsnumofnegativesds = YLeaf(YType.uint32, "rttMonJitterStatsNumOfNegativesDS")

                self.rttmonjitterstatsnumofnegativessd = YLeaf(YType.uint32, "rttMonJitterStatsNumOfNegativesSD")

                self.rttmonjitterstatsnumofow = YLeaf(YType.uint32, "rttMonJitterStatsNumOfOW")

                self.rttmonjitterstatsnumofpositivesds = YLeaf(YType.uint32, "rttMonJitterStatsNumOfPositivesDS")

                self.rttmonjitterstatsnumofpositivessd = YLeaf(YType.uint32, "rttMonJitterStatsNumOfPositivesSD")

                self.rttmonjitterstatsnumofrtt = YLeaf(YType.uint32, "rttMonJitterStatsNumOfRTT")

                self.rttmonjitterstatsoverthresholds = YLeaf(YType.uint32, "rttMonJitterStatsOverThresholds")

                self.rttmonjitterstatsowmaxds = YLeaf(YType.uint32, "rttMonJitterStatsOWMaxDS")

                self.rttmonjitterstatsowmaxdsnew = YLeaf(YType.uint32, "rttMonJitterStatsOWMaxDSNew")

                self.rttmonjitterstatsowmaxsd = YLeaf(YType.uint32, "rttMonJitterStatsOWMaxSD")

                self.rttmonjitterstatsowmaxsdnew = YLeaf(YType.uint32, "rttMonJitterStatsOWMaxSDNew")

                self.rttmonjitterstatsowminds = YLeaf(YType.uint32, "rttMonJitterStatsOWMinDS")

                self.rttmonjitterstatsowmindsnew = YLeaf(YType.uint32, "rttMonJitterStatsOWMinDSNew")

                self.rttmonjitterstatsowminsd = YLeaf(YType.uint32, "rttMonJitterStatsOWMinSD")

                self.rttmonjitterstatsowminsdnew = YLeaf(YType.uint32, "rttMonJitterStatsOWMinSDNew")

                self.rttmonjitterstatsowsum2dshigh = YLeaf(YType.uint32, "rttMonJitterStatsOWSum2DSHigh")

                self.rttmonjitterstatsowsum2dslow = YLeaf(YType.uint32, "rttMonJitterStatsOWSum2DSLow")

                self.rttmonjitterstatsowsum2sdhigh = YLeaf(YType.uint32, "rttMonJitterStatsOWSum2SDHigh")

                self.rttmonjitterstatsowsum2sdlow = YLeaf(YType.uint32, "rttMonJitterStatsOWSum2SDLow")

                self.rttmonjitterstatsowsumds = YLeaf(YType.uint32, "rttMonJitterStatsOWSumDS")

                self.rttmonjitterstatsowsumdshigh = YLeaf(YType.uint32, "rttMonJitterStatsOWSumDSHigh")

                self.rttmonjitterstatsowsumsd = YLeaf(YType.uint32, "rttMonJitterStatsOWSumSD")

                self.rttmonjitterstatsowsumsdhigh = YLeaf(YType.uint32, "rttMonJitterStatsOWSumSDHigh")

                self.rttmonjitterstatspacketlatearrival = YLeaf(YType.uint32, "rttMonJitterStatsPacketLateArrival")

                self.rttmonjitterstatspacketlossds = YLeaf(YType.uint32, "rttMonJitterStatsPacketLossDS")

                self.rttmonjitterstatspacketlosssd = YLeaf(YType.uint32, "rttMonJitterStatsPacketLossSD")

                self.rttmonjitterstatspacketmia = YLeaf(YType.uint32, "rttMonJitterStatsPacketMIA")

                self.rttmonjitterstatspacketoutofsequence = YLeaf(YType.uint32, "rttMonJitterStatsPacketOutOfSequence")

                self.rttmonjitterstatsrttmax = YLeaf(YType.uint32, "rttMonJitterStatsRTTMax")

                self.rttmonjitterstatsrttmin = YLeaf(YType.uint32, "rttMonJitterStatsRTTMin")

                self.rttmonjitterstatsrttsum = YLeaf(YType.uint32, "rttMonJitterStatsRTTSum")

                self.rttmonjitterstatsrttsum2high = YLeaf(YType.uint32, "rttMonJitterStatsRTTSum2High")

                self.rttmonjitterstatsrttsum2low = YLeaf(YType.uint32, "rttMonJitterStatsRTTSum2Low")

                self.rttmonjitterstatsrttsumhigh = YLeaf(YType.uint32, "rttMonJitterStatsRTTSumHigh")

                self.rttmonjitterstatssum2negativesdshigh = YLeaf(YType.uint32, "rttMonJitterStatsSum2NegativesDSHigh")

                self.rttmonjitterstatssum2negativesdslow = YLeaf(YType.uint32, "rttMonJitterStatsSum2NegativesDSLow")

                self.rttmonjitterstatssum2negativessdhigh = YLeaf(YType.uint32, "rttMonJitterStatsSum2NegativesSDHigh")

                self.rttmonjitterstatssum2negativessdlow = YLeaf(YType.uint32, "rttMonJitterStatsSum2NegativesSDLow")

                self.rttmonjitterstatssum2positivesdshigh = YLeaf(YType.uint32, "rttMonJitterStatsSum2PositivesDSHigh")

                self.rttmonjitterstatssum2positivesdslow = YLeaf(YType.uint32, "rttMonJitterStatsSum2PositivesDSLow")

                self.rttmonjitterstatssum2positivessdhigh = YLeaf(YType.uint32, "rttMonJitterStatsSum2PositivesSDHigh")

                self.rttmonjitterstatssum2positivessdlow = YLeaf(YType.uint32, "rttMonJitterStatsSum2PositivesSDLow")

                self.rttmonjitterstatssumofnegativesds = YLeaf(YType.uint32, "rttMonJitterStatsSumOfNegativesDS")

                self.rttmonjitterstatssumofnegativessd = YLeaf(YType.uint32, "rttMonJitterStatsSumOfNegativesSD")

                self.rttmonjitterstatssumofpositivesds = YLeaf(YType.uint32, "rttMonJitterStatsSumOfPositivesDS")

                self.rttmonjitterstatssumofpositivessd = YLeaf(YType.uint32, "rttMonJitterStatsSumOfPositivesSD")

                self.rttmonjitterstatsunsyncrts = YLeaf(YType.uint32, "rttMonJitterStatsUnSyncRTs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonjitterstatsstarttimeindex",
                                "rttmonjitterstatsavgjitter",
                                "rttmonjitterstatsavgjitterds",
                                "rttmonjitterstatsavgjittersd",
                                "rttmonjitterstatsbusies",
                                "rttmonjitterstatscompletions",
                                "rttmonjitterstatserror",
                                "rttmonjitterstatsiajin",
                                "rttmonjitterstatsiajout",
                                "rttmonjitterstatsmaxoficpif",
                                "rttmonjitterstatsmaxofmos",
                                "rttmonjitterstatsmaxofnegativesds",
                                "rttmonjitterstatsmaxofnegativessd",
                                "rttmonjitterstatsmaxofpositivesds",
                                "rttmonjitterstatsmaxofpositivessd",
                                "rttmonjitterstatsminoficpif",
                                "rttmonjitterstatsminofmos",
                                "rttmonjitterstatsminofnegativesds",
                                "rttmonjitterstatsminofnegativessd",
                                "rttmonjitterstatsminofpositivesds",
                                "rttmonjitterstatsminofpositivessd",
                                "rttmonjitterstatsnumofnegativesds",
                                "rttmonjitterstatsnumofnegativessd",
                                "rttmonjitterstatsnumofow",
                                "rttmonjitterstatsnumofpositivesds",
                                "rttmonjitterstatsnumofpositivessd",
                                "rttmonjitterstatsnumofrtt",
                                "rttmonjitterstatsoverthresholds",
                                "rttmonjitterstatsowmaxds",
                                "rttmonjitterstatsowmaxdsnew",
                                "rttmonjitterstatsowmaxsd",
                                "rttmonjitterstatsowmaxsdnew",
                                "rttmonjitterstatsowminds",
                                "rttmonjitterstatsowmindsnew",
                                "rttmonjitterstatsowminsd",
                                "rttmonjitterstatsowminsdnew",
                                "rttmonjitterstatsowsum2dshigh",
                                "rttmonjitterstatsowsum2dslow",
                                "rttmonjitterstatsowsum2sdhigh",
                                "rttmonjitterstatsowsum2sdlow",
                                "rttmonjitterstatsowsumds",
                                "rttmonjitterstatsowsumdshigh",
                                "rttmonjitterstatsowsumsd",
                                "rttmonjitterstatsowsumsdhigh",
                                "rttmonjitterstatspacketlatearrival",
                                "rttmonjitterstatspacketlossds",
                                "rttmonjitterstatspacketlosssd",
                                "rttmonjitterstatspacketmia",
                                "rttmonjitterstatspacketoutofsequence",
                                "rttmonjitterstatsrttmax",
                                "rttmonjitterstatsrttmin",
                                "rttmonjitterstatsrttsum",
                                "rttmonjitterstatsrttsum2high",
                                "rttmonjitterstatsrttsum2low",
                                "rttmonjitterstatsrttsumhigh",
                                "rttmonjitterstatssum2negativesdshigh",
                                "rttmonjitterstatssum2negativesdslow",
                                "rttmonjitterstatssum2negativessdhigh",
                                "rttmonjitterstatssum2negativessdlow",
                                "rttmonjitterstatssum2positivesdshigh",
                                "rttmonjitterstatssum2positivesdslow",
                                "rttmonjitterstatssum2positivessdhigh",
                                "rttmonjitterstatssum2positivessdlow",
                                "rttmonjitterstatssumofnegativesds",
                                "rttmonjitterstatssumofnegativessd",
                                "rttmonjitterstatssumofpositivesds",
                                "rttmonjitterstatssumofpositivessd",
                                "rttmonjitterstatsunsyncrts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonjitterstatstable.Rttmonjitterstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonjitterstatstable.Rttmonjitterstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonjitterstatsstarttimeindex.is_set or
                    self.rttmonjitterstatsavgjitter.is_set or
                    self.rttmonjitterstatsavgjitterds.is_set or
                    self.rttmonjitterstatsavgjittersd.is_set or
                    self.rttmonjitterstatsbusies.is_set or
                    self.rttmonjitterstatscompletions.is_set or
                    self.rttmonjitterstatserror.is_set or
                    self.rttmonjitterstatsiajin.is_set or
                    self.rttmonjitterstatsiajout.is_set or
                    self.rttmonjitterstatsmaxoficpif.is_set or
                    self.rttmonjitterstatsmaxofmos.is_set or
                    self.rttmonjitterstatsmaxofnegativesds.is_set or
                    self.rttmonjitterstatsmaxofnegativessd.is_set or
                    self.rttmonjitterstatsmaxofpositivesds.is_set or
                    self.rttmonjitterstatsmaxofpositivessd.is_set or
                    self.rttmonjitterstatsminoficpif.is_set or
                    self.rttmonjitterstatsminofmos.is_set or
                    self.rttmonjitterstatsminofnegativesds.is_set or
                    self.rttmonjitterstatsminofnegativessd.is_set or
                    self.rttmonjitterstatsminofpositivesds.is_set or
                    self.rttmonjitterstatsminofpositivessd.is_set or
                    self.rttmonjitterstatsnumofnegativesds.is_set or
                    self.rttmonjitterstatsnumofnegativessd.is_set or
                    self.rttmonjitterstatsnumofow.is_set or
                    self.rttmonjitterstatsnumofpositivesds.is_set or
                    self.rttmonjitterstatsnumofpositivessd.is_set or
                    self.rttmonjitterstatsnumofrtt.is_set or
                    self.rttmonjitterstatsoverthresholds.is_set or
                    self.rttmonjitterstatsowmaxds.is_set or
                    self.rttmonjitterstatsowmaxdsnew.is_set or
                    self.rttmonjitterstatsowmaxsd.is_set or
                    self.rttmonjitterstatsowmaxsdnew.is_set or
                    self.rttmonjitterstatsowminds.is_set or
                    self.rttmonjitterstatsowmindsnew.is_set or
                    self.rttmonjitterstatsowminsd.is_set or
                    self.rttmonjitterstatsowminsdnew.is_set or
                    self.rttmonjitterstatsowsum2dshigh.is_set or
                    self.rttmonjitterstatsowsum2dslow.is_set or
                    self.rttmonjitterstatsowsum2sdhigh.is_set or
                    self.rttmonjitterstatsowsum2sdlow.is_set or
                    self.rttmonjitterstatsowsumds.is_set or
                    self.rttmonjitterstatsowsumdshigh.is_set or
                    self.rttmonjitterstatsowsumsd.is_set or
                    self.rttmonjitterstatsowsumsdhigh.is_set or
                    self.rttmonjitterstatspacketlatearrival.is_set or
                    self.rttmonjitterstatspacketlossds.is_set or
                    self.rttmonjitterstatspacketlosssd.is_set or
                    self.rttmonjitterstatspacketmia.is_set or
                    self.rttmonjitterstatspacketoutofsequence.is_set or
                    self.rttmonjitterstatsrttmax.is_set or
                    self.rttmonjitterstatsrttmin.is_set or
                    self.rttmonjitterstatsrttsum.is_set or
                    self.rttmonjitterstatsrttsum2high.is_set or
                    self.rttmonjitterstatsrttsum2low.is_set or
                    self.rttmonjitterstatsrttsumhigh.is_set or
                    self.rttmonjitterstatssum2negativesdshigh.is_set or
                    self.rttmonjitterstatssum2negativesdslow.is_set or
                    self.rttmonjitterstatssum2negativessdhigh.is_set or
                    self.rttmonjitterstatssum2negativessdlow.is_set or
                    self.rttmonjitterstatssum2positivesdshigh.is_set or
                    self.rttmonjitterstatssum2positivesdslow.is_set or
                    self.rttmonjitterstatssum2positivessdhigh.is_set or
                    self.rttmonjitterstatssum2positivessdlow.is_set or
                    self.rttmonjitterstatssumofnegativesds.is_set or
                    self.rttmonjitterstatssumofnegativessd.is_set or
                    self.rttmonjitterstatssumofpositivesds.is_set or
                    self.rttmonjitterstatssumofpositivessd.is_set or
                    self.rttmonjitterstatsunsyncrts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsstarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsavgjitter.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsavgjitterds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsavgjittersd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsbusies.yfilter != YFilter.not_set or
                    self.rttmonjitterstatscompletions.yfilter != YFilter.not_set or
                    self.rttmonjitterstatserror.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsiajin.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsiajout.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxoficpif.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxofmos.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsmaxofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminoficpif.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminofmos.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsminofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsnumofrtt.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsoverthresholds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowmaxds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowmaxdsnew.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowmaxsd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowmaxsdnew.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowminds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowmindsnew.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowminsd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowminsdnew.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsum2dshigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsum2dslow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsum2sdhigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsum2sdlow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsumds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsumdshigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsumsd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsowsumsdhigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatspacketlatearrival.yfilter != YFilter.not_set or
                    self.rttmonjitterstatspacketlossds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatspacketlosssd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatspacketmia.yfilter != YFilter.not_set or
                    self.rttmonjitterstatspacketoutofsequence.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttmax.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttmin.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttsum.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttsum2high.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttsum2low.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsrttsumhigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2negativesdshigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2negativesdslow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2negativessdhigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2negativessdlow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2positivesdshigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2positivesdslow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2positivessdhigh.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssum2positivessdlow.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssumofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssumofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssumofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonjitterstatssumofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonjitterstatsunsyncrts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonJitterStatsEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonJitterStatsStartTimeIndex='" + self.rttmonjitterstatsstarttimeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonJitterStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonjitterstatsstarttimeindex.is_set or self.rttmonjitterstatsstarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsstarttimeindex.get_name_leafdata())
                if (self.rttmonjitterstatsavgjitter.is_set or self.rttmonjitterstatsavgjitter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsavgjitter.get_name_leafdata())
                if (self.rttmonjitterstatsavgjitterds.is_set or self.rttmonjitterstatsavgjitterds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsavgjitterds.get_name_leafdata())
                if (self.rttmonjitterstatsavgjittersd.is_set or self.rttmonjitterstatsavgjittersd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsavgjittersd.get_name_leafdata())
                if (self.rttmonjitterstatsbusies.is_set or self.rttmonjitterstatsbusies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsbusies.get_name_leafdata())
                if (self.rttmonjitterstatscompletions.is_set or self.rttmonjitterstatscompletions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatscompletions.get_name_leafdata())
                if (self.rttmonjitterstatserror.is_set or self.rttmonjitterstatserror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatserror.get_name_leafdata())
                if (self.rttmonjitterstatsiajin.is_set or self.rttmonjitterstatsiajin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsiajin.get_name_leafdata())
                if (self.rttmonjitterstatsiajout.is_set or self.rttmonjitterstatsiajout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsiajout.get_name_leafdata())
                if (self.rttmonjitterstatsmaxoficpif.is_set or self.rttmonjitterstatsmaxoficpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxoficpif.get_name_leafdata())
                if (self.rttmonjitterstatsmaxofmos.is_set or self.rttmonjitterstatsmaxofmos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxofmos.get_name_leafdata())
                if (self.rttmonjitterstatsmaxofnegativesds.is_set or self.rttmonjitterstatsmaxofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxofnegativesds.get_name_leafdata())
                if (self.rttmonjitterstatsmaxofnegativessd.is_set or self.rttmonjitterstatsmaxofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxofnegativessd.get_name_leafdata())
                if (self.rttmonjitterstatsmaxofpositivesds.is_set or self.rttmonjitterstatsmaxofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxofpositivesds.get_name_leafdata())
                if (self.rttmonjitterstatsmaxofpositivessd.is_set or self.rttmonjitterstatsmaxofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsmaxofpositivessd.get_name_leafdata())
                if (self.rttmonjitterstatsminoficpif.is_set or self.rttmonjitterstatsminoficpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminoficpif.get_name_leafdata())
                if (self.rttmonjitterstatsminofmos.is_set or self.rttmonjitterstatsminofmos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminofmos.get_name_leafdata())
                if (self.rttmonjitterstatsminofnegativesds.is_set or self.rttmonjitterstatsminofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminofnegativesds.get_name_leafdata())
                if (self.rttmonjitterstatsminofnegativessd.is_set or self.rttmonjitterstatsminofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminofnegativessd.get_name_leafdata())
                if (self.rttmonjitterstatsminofpositivesds.is_set or self.rttmonjitterstatsminofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminofpositivesds.get_name_leafdata())
                if (self.rttmonjitterstatsminofpositivessd.is_set or self.rttmonjitterstatsminofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsminofpositivessd.get_name_leafdata())
                if (self.rttmonjitterstatsnumofnegativesds.is_set or self.rttmonjitterstatsnumofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofnegativesds.get_name_leafdata())
                if (self.rttmonjitterstatsnumofnegativessd.is_set or self.rttmonjitterstatsnumofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofnegativessd.get_name_leafdata())
                if (self.rttmonjitterstatsnumofow.is_set or self.rttmonjitterstatsnumofow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofow.get_name_leafdata())
                if (self.rttmonjitterstatsnumofpositivesds.is_set or self.rttmonjitterstatsnumofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofpositivesds.get_name_leafdata())
                if (self.rttmonjitterstatsnumofpositivessd.is_set or self.rttmonjitterstatsnumofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofpositivessd.get_name_leafdata())
                if (self.rttmonjitterstatsnumofrtt.is_set or self.rttmonjitterstatsnumofrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsnumofrtt.get_name_leafdata())
                if (self.rttmonjitterstatsoverthresholds.is_set or self.rttmonjitterstatsoverthresholds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsoverthresholds.get_name_leafdata())
                if (self.rttmonjitterstatsowmaxds.is_set or self.rttmonjitterstatsowmaxds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowmaxds.get_name_leafdata())
                if (self.rttmonjitterstatsowmaxdsnew.is_set or self.rttmonjitterstatsowmaxdsnew.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowmaxdsnew.get_name_leafdata())
                if (self.rttmonjitterstatsowmaxsd.is_set or self.rttmonjitterstatsowmaxsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowmaxsd.get_name_leafdata())
                if (self.rttmonjitterstatsowmaxsdnew.is_set or self.rttmonjitterstatsowmaxsdnew.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowmaxsdnew.get_name_leafdata())
                if (self.rttmonjitterstatsowminds.is_set or self.rttmonjitterstatsowminds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowminds.get_name_leafdata())
                if (self.rttmonjitterstatsowmindsnew.is_set or self.rttmonjitterstatsowmindsnew.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowmindsnew.get_name_leafdata())
                if (self.rttmonjitterstatsowminsd.is_set or self.rttmonjitterstatsowminsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowminsd.get_name_leafdata())
                if (self.rttmonjitterstatsowminsdnew.is_set or self.rttmonjitterstatsowminsdnew.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowminsdnew.get_name_leafdata())
                if (self.rttmonjitterstatsowsum2dshigh.is_set or self.rttmonjitterstatsowsum2dshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsum2dshigh.get_name_leafdata())
                if (self.rttmonjitterstatsowsum2dslow.is_set or self.rttmonjitterstatsowsum2dslow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsum2dslow.get_name_leafdata())
                if (self.rttmonjitterstatsowsum2sdhigh.is_set or self.rttmonjitterstatsowsum2sdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsum2sdhigh.get_name_leafdata())
                if (self.rttmonjitterstatsowsum2sdlow.is_set or self.rttmonjitterstatsowsum2sdlow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsum2sdlow.get_name_leafdata())
                if (self.rttmonjitterstatsowsumds.is_set or self.rttmonjitterstatsowsumds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsumds.get_name_leafdata())
                if (self.rttmonjitterstatsowsumdshigh.is_set or self.rttmonjitterstatsowsumdshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsumdshigh.get_name_leafdata())
                if (self.rttmonjitterstatsowsumsd.is_set or self.rttmonjitterstatsowsumsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsumsd.get_name_leafdata())
                if (self.rttmonjitterstatsowsumsdhigh.is_set or self.rttmonjitterstatsowsumsdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsowsumsdhigh.get_name_leafdata())
                if (self.rttmonjitterstatspacketlatearrival.is_set or self.rttmonjitterstatspacketlatearrival.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatspacketlatearrival.get_name_leafdata())
                if (self.rttmonjitterstatspacketlossds.is_set or self.rttmonjitterstatspacketlossds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatspacketlossds.get_name_leafdata())
                if (self.rttmonjitterstatspacketlosssd.is_set or self.rttmonjitterstatspacketlosssd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatspacketlosssd.get_name_leafdata())
                if (self.rttmonjitterstatspacketmia.is_set or self.rttmonjitterstatspacketmia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatspacketmia.get_name_leafdata())
                if (self.rttmonjitterstatspacketoutofsequence.is_set or self.rttmonjitterstatspacketoutofsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatspacketoutofsequence.get_name_leafdata())
                if (self.rttmonjitterstatsrttmax.is_set or self.rttmonjitterstatsrttmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttmax.get_name_leafdata())
                if (self.rttmonjitterstatsrttmin.is_set or self.rttmonjitterstatsrttmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttmin.get_name_leafdata())
                if (self.rttmonjitterstatsrttsum.is_set or self.rttmonjitterstatsrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttsum.get_name_leafdata())
                if (self.rttmonjitterstatsrttsum2high.is_set or self.rttmonjitterstatsrttsum2high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttsum2high.get_name_leafdata())
                if (self.rttmonjitterstatsrttsum2low.is_set or self.rttmonjitterstatsrttsum2low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttsum2low.get_name_leafdata())
                if (self.rttmonjitterstatsrttsumhigh.is_set or self.rttmonjitterstatsrttsumhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsrttsumhigh.get_name_leafdata())
                if (self.rttmonjitterstatssum2negativesdshigh.is_set or self.rttmonjitterstatssum2negativesdshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2negativesdshigh.get_name_leafdata())
                if (self.rttmonjitterstatssum2negativesdslow.is_set or self.rttmonjitterstatssum2negativesdslow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2negativesdslow.get_name_leafdata())
                if (self.rttmonjitterstatssum2negativessdhigh.is_set or self.rttmonjitterstatssum2negativessdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2negativessdhigh.get_name_leafdata())
                if (self.rttmonjitterstatssum2negativessdlow.is_set or self.rttmonjitterstatssum2negativessdlow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2negativessdlow.get_name_leafdata())
                if (self.rttmonjitterstatssum2positivesdshigh.is_set or self.rttmonjitterstatssum2positivesdshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2positivesdshigh.get_name_leafdata())
                if (self.rttmonjitterstatssum2positivesdslow.is_set or self.rttmonjitterstatssum2positivesdslow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2positivesdslow.get_name_leafdata())
                if (self.rttmonjitterstatssum2positivessdhigh.is_set or self.rttmonjitterstatssum2positivessdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2positivessdhigh.get_name_leafdata())
                if (self.rttmonjitterstatssum2positivessdlow.is_set or self.rttmonjitterstatssum2positivessdlow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssum2positivessdlow.get_name_leafdata())
                if (self.rttmonjitterstatssumofnegativesds.is_set or self.rttmonjitterstatssumofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssumofnegativesds.get_name_leafdata())
                if (self.rttmonjitterstatssumofnegativessd.is_set or self.rttmonjitterstatssumofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssumofnegativessd.get_name_leafdata())
                if (self.rttmonjitterstatssumofpositivesds.is_set or self.rttmonjitterstatssumofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssumofpositivesds.get_name_leafdata())
                if (self.rttmonjitterstatssumofpositivessd.is_set or self.rttmonjitterstatssumofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatssumofpositivessd.get_name_leafdata())
                if (self.rttmonjitterstatsunsyncrts.is_set or self.rttmonjitterstatsunsyncrts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonjitterstatsunsyncrts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonJitterStatsStartTimeIndex" or name == "rttMonJitterStatsAvgJitter" or name == "rttMonJitterStatsAvgJitterDS" or name == "rttMonJitterStatsAvgJitterSD" or name == "rttMonJitterStatsBusies" or name == "rttMonJitterStatsCompletions" or name == "rttMonJitterStatsError" or name == "rttMonJitterStatsIAJIn" or name == "rttMonJitterStatsIAJOut" or name == "rttMonJitterStatsMaxOfICPIF" or name == "rttMonJitterStatsMaxOfMOS" or name == "rttMonJitterStatsMaxOfNegativesDS" or name == "rttMonJitterStatsMaxOfNegativesSD" or name == "rttMonJitterStatsMaxOfPositivesDS" or name == "rttMonJitterStatsMaxOfPositivesSD" or name == "rttMonJitterStatsMinOfICPIF" or name == "rttMonJitterStatsMinOfMOS" or name == "rttMonJitterStatsMinOfNegativesDS" or name == "rttMonJitterStatsMinOfNegativesSD" or name == "rttMonJitterStatsMinOfPositivesDS" or name == "rttMonJitterStatsMinOfPositivesSD" or name == "rttMonJitterStatsNumOfNegativesDS" or name == "rttMonJitterStatsNumOfNegativesSD" or name == "rttMonJitterStatsNumOfOW" or name == "rttMonJitterStatsNumOfPositivesDS" or name == "rttMonJitterStatsNumOfPositivesSD" or name == "rttMonJitterStatsNumOfRTT" or name == "rttMonJitterStatsOverThresholds" or name == "rttMonJitterStatsOWMaxDS" or name == "rttMonJitterStatsOWMaxDSNew" or name == "rttMonJitterStatsOWMaxSD" or name == "rttMonJitterStatsOWMaxSDNew" or name == "rttMonJitterStatsOWMinDS" or name == "rttMonJitterStatsOWMinDSNew" or name == "rttMonJitterStatsOWMinSD" or name == "rttMonJitterStatsOWMinSDNew" or name == "rttMonJitterStatsOWSum2DSHigh" or name == "rttMonJitterStatsOWSum2DSLow" or name == "rttMonJitterStatsOWSum2SDHigh" or name == "rttMonJitterStatsOWSum2SDLow" or name == "rttMonJitterStatsOWSumDS" or name == "rttMonJitterStatsOWSumDSHigh" or name == "rttMonJitterStatsOWSumSD" or name == "rttMonJitterStatsOWSumSDHigh" or name == "rttMonJitterStatsPacketLateArrival" or name == "rttMonJitterStatsPacketLossDS" or name == "rttMonJitterStatsPacketLossSD" or name == "rttMonJitterStatsPacketMIA" or name == "rttMonJitterStatsPacketOutOfSequence" or name == "rttMonJitterStatsRTTMax" or name == "rttMonJitterStatsRTTMin" or name == "rttMonJitterStatsRTTSum" or name == "rttMonJitterStatsRTTSum2High" or name == "rttMonJitterStatsRTTSum2Low" or name == "rttMonJitterStatsRTTSumHigh" or name == "rttMonJitterStatsSum2NegativesDSHigh" or name == "rttMonJitterStatsSum2NegativesDSLow" or name == "rttMonJitterStatsSum2NegativesSDHigh" or name == "rttMonJitterStatsSum2NegativesSDLow" or name == "rttMonJitterStatsSum2PositivesDSHigh" or name == "rttMonJitterStatsSum2PositivesDSLow" or name == "rttMonJitterStatsSum2PositivesSDHigh" or name == "rttMonJitterStatsSum2PositivesSDLow" or name == "rttMonJitterStatsSumOfNegativesDS" or name == "rttMonJitterStatsSumOfNegativesSD" or name == "rttMonJitterStatsSumOfPositivesDS" or name == "rttMonJitterStatsSumOfPositivesSD" or name == "rttMonJitterStatsUnSyncRTs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsStartTimeIndex"):
                    self.rttmonjitterstatsstarttimeindex = value
                    self.rttmonjitterstatsstarttimeindex.value_namespace = name_space
                    self.rttmonjitterstatsstarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsAvgJitter"):
                    self.rttmonjitterstatsavgjitter = value
                    self.rttmonjitterstatsavgjitter.value_namespace = name_space
                    self.rttmonjitterstatsavgjitter.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsAvgJitterDS"):
                    self.rttmonjitterstatsavgjitterds = value
                    self.rttmonjitterstatsavgjitterds.value_namespace = name_space
                    self.rttmonjitterstatsavgjitterds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsAvgJitterSD"):
                    self.rttmonjitterstatsavgjittersd = value
                    self.rttmonjitterstatsavgjittersd.value_namespace = name_space
                    self.rttmonjitterstatsavgjittersd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsBusies"):
                    self.rttmonjitterstatsbusies = value
                    self.rttmonjitterstatsbusies.value_namespace = name_space
                    self.rttmonjitterstatsbusies.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsCompletions"):
                    self.rttmonjitterstatscompletions = value
                    self.rttmonjitterstatscompletions.value_namespace = name_space
                    self.rttmonjitterstatscompletions.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsError"):
                    self.rttmonjitterstatserror = value
                    self.rttmonjitterstatserror.value_namespace = name_space
                    self.rttmonjitterstatserror.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsIAJIn"):
                    self.rttmonjitterstatsiajin = value
                    self.rttmonjitterstatsiajin.value_namespace = name_space
                    self.rttmonjitterstatsiajin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsIAJOut"):
                    self.rttmonjitterstatsiajout = value
                    self.rttmonjitterstatsiajout.value_namespace = name_space
                    self.rttmonjitterstatsiajout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfICPIF"):
                    self.rttmonjitterstatsmaxoficpif = value
                    self.rttmonjitterstatsmaxoficpif.value_namespace = name_space
                    self.rttmonjitterstatsmaxoficpif.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfMOS"):
                    self.rttmonjitterstatsmaxofmos = value
                    self.rttmonjitterstatsmaxofmos.value_namespace = name_space
                    self.rttmonjitterstatsmaxofmos.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfNegativesDS"):
                    self.rttmonjitterstatsmaxofnegativesds = value
                    self.rttmonjitterstatsmaxofnegativesds.value_namespace = name_space
                    self.rttmonjitterstatsmaxofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfNegativesSD"):
                    self.rttmonjitterstatsmaxofnegativessd = value
                    self.rttmonjitterstatsmaxofnegativessd.value_namespace = name_space
                    self.rttmonjitterstatsmaxofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfPositivesDS"):
                    self.rttmonjitterstatsmaxofpositivesds = value
                    self.rttmonjitterstatsmaxofpositivesds.value_namespace = name_space
                    self.rttmonjitterstatsmaxofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMaxOfPositivesSD"):
                    self.rttmonjitterstatsmaxofpositivessd = value
                    self.rttmonjitterstatsmaxofpositivessd.value_namespace = name_space
                    self.rttmonjitterstatsmaxofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfICPIF"):
                    self.rttmonjitterstatsminoficpif = value
                    self.rttmonjitterstatsminoficpif.value_namespace = name_space
                    self.rttmonjitterstatsminoficpif.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfMOS"):
                    self.rttmonjitterstatsminofmos = value
                    self.rttmonjitterstatsminofmos.value_namespace = name_space
                    self.rttmonjitterstatsminofmos.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfNegativesDS"):
                    self.rttmonjitterstatsminofnegativesds = value
                    self.rttmonjitterstatsminofnegativesds.value_namespace = name_space
                    self.rttmonjitterstatsminofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfNegativesSD"):
                    self.rttmonjitterstatsminofnegativessd = value
                    self.rttmonjitterstatsminofnegativessd.value_namespace = name_space
                    self.rttmonjitterstatsminofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfPositivesDS"):
                    self.rttmonjitterstatsminofpositivesds = value
                    self.rttmonjitterstatsminofpositivesds.value_namespace = name_space
                    self.rttmonjitterstatsminofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsMinOfPositivesSD"):
                    self.rttmonjitterstatsminofpositivessd = value
                    self.rttmonjitterstatsminofpositivessd.value_namespace = name_space
                    self.rttmonjitterstatsminofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfNegativesDS"):
                    self.rttmonjitterstatsnumofnegativesds = value
                    self.rttmonjitterstatsnumofnegativesds.value_namespace = name_space
                    self.rttmonjitterstatsnumofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfNegativesSD"):
                    self.rttmonjitterstatsnumofnegativessd = value
                    self.rttmonjitterstatsnumofnegativessd.value_namespace = name_space
                    self.rttmonjitterstatsnumofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfOW"):
                    self.rttmonjitterstatsnumofow = value
                    self.rttmonjitterstatsnumofow.value_namespace = name_space
                    self.rttmonjitterstatsnumofow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfPositivesDS"):
                    self.rttmonjitterstatsnumofpositivesds = value
                    self.rttmonjitterstatsnumofpositivesds.value_namespace = name_space
                    self.rttmonjitterstatsnumofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfPositivesSD"):
                    self.rttmonjitterstatsnumofpositivessd = value
                    self.rttmonjitterstatsnumofpositivessd.value_namespace = name_space
                    self.rttmonjitterstatsnumofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsNumOfRTT"):
                    self.rttmonjitterstatsnumofrtt = value
                    self.rttmonjitterstatsnumofrtt.value_namespace = name_space
                    self.rttmonjitterstatsnumofrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOverThresholds"):
                    self.rttmonjitterstatsoverthresholds = value
                    self.rttmonjitterstatsoverthresholds.value_namespace = name_space
                    self.rttmonjitterstatsoverthresholds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMaxDS"):
                    self.rttmonjitterstatsowmaxds = value
                    self.rttmonjitterstatsowmaxds.value_namespace = name_space
                    self.rttmonjitterstatsowmaxds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMaxDSNew"):
                    self.rttmonjitterstatsowmaxdsnew = value
                    self.rttmonjitterstatsowmaxdsnew.value_namespace = name_space
                    self.rttmonjitterstatsowmaxdsnew.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMaxSD"):
                    self.rttmonjitterstatsowmaxsd = value
                    self.rttmonjitterstatsowmaxsd.value_namespace = name_space
                    self.rttmonjitterstatsowmaxsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMaxSDNew"):
                    self.rttmonjitterstatsowmaxsdnew = value
                    self.rttmonjitterstatsowmaxsdnew.value_namespace = name_space
                    self.rttmonjitterstatsowmaxsdnew.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMinDS"):
                    self.rttmonjitterstatsowminds = value
                    self.rttmonjitterstatsowminds.value_namespace = name_space
                    self.rttmonjitterstatsowminds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMinDSNew"):
                    self.rttmonjitterstatsowmindsnew = value
                    self.rttmonjitterstatsowmindsnew.value_namespace = name_space
                    self.rttmonjitterstatsowmindsnew.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMinSD"):
                    self.rttmonjitterstatsowminsd = value
                    self.rttmonjitterstatsowminsd.value_namespace = name_space
                    self.rttmonjitterstatsowminsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWMinSDNew"):
                    self.rttmonjitterstatsowminsdnew = value
                    self.rttmonjitterstatsowminsdnew.value_namespace = name_space
                    self.rttmonjitterstatsowminsdnew.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSum2DSHigh"):
                    self.rttmonjitterstatsowsum2dshigh = value
                    self.rttmonjitterstatsowsum2dshigh.value_namespace = name_space
                    self.rttmonjitterstatsowsum2dshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSum2DSLow"):
                    self.rttmonjitterstatsowsum2dslow = value
                    self.rttmonjitterstatsowsum2dslow.value_namespace = name_space
                    self.rttmonjitterstatsowsum2dslow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSum2SDHigh"):
                    self.rttmonjitterstatsowsum2sdhigh = value
                    self.rttmonjitterstatsowsum2sdhigh.value_namespace = name_space
                    self.rttmonjitterstatsowsum2sdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSum2SDLow"):
                    self.rttmonjitterstatsowsum2sdlow = value
                    self.rttmonjitterstatsowsum2sdlow.value_namespace = name_space
                    self.rttmonjitterstatsowsum2sdlow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSumDS"):
                    self.rttmonjitterstatsowsumds = value
                    self.rttmonjitterstatsowsumds.value_namespace = name_space
                    self.rttmonjitterstatsowsumds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSumDSHigh"):
                    self.rttmonjitterstatsowsumdshigh = value
                    self.rttmonjitterstatsowsumdshigh.value_namespace = name_space
                    self.rttmonjitterstatsowsumdshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSumSD"):
                    self.rttmonjitterstatsowsumsd = value
                    self.rttmonjitterstatsowsumsd.value_namespace = name_space
                    self.rttmonjitterstatsowsumsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsOWSumSDHigh"):
                    self.rttmonjitterstatsowsumsdhigh = value
                    self.rttmonjitterstatsowsumsdhigh.value_namespace = name_space
                    self.rttmonjitterstatsowsumsdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsPacketLateArrival"):
                    self.rttmonjitterstatspacketlatearrival = value
                    self.rttmonjitterstatspacketlatearrival.value_namespace = name_space
                    self.rttmonjitterstatspacketlatearrival.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsPacketLossDS"):
                    self.rttmonjitterstatspacketlossds = value
                    self.rttmonjitterstatspacketlossds.value_namespace = name_space
                    self.rttmonjitterstatspacketlossds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsPacketLossSD"):
                    self.rttmonjitterstatspacketlosssd = value
                    self.rttmonjitterstatspacketlosssd.value_namespace = name_space
                    self.rttmonjitterstatspacketlosssd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsPacketMIA"):
                    self.rttmonjitterstatspacketmia = value
                    self.rttmonjitterstatspacketmia.value_namespace = name_space
                    self.rttmonjitterstatspacketmia.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsPacketOutOfSequence"):
                    self.rttmonjitterstatspacketoutofsequence = value
                    self.rttmonjitterstatspacketoutofsequence.value_namespace = name_space
                    self.rttmonjitterstatspacketoutofsequence.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTMax"):
                    self.rttmonjitterstatsrttmax = value
                    self.rttmonjitterstatsrttmax.value_namespace = name_space
                    self.rttmonjitterstatsrttmax.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTMin"):
                    self.rttmonjitterstatsrttmin = value
                    self.rttmonjitterstatsrttmin.value_namespace = name_space
                    self.rttmonjitterstatsrttmin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTSum"):
                    self.rttmonjitterstatsrttsum = value
                    self.rttmonjitterstatsrttsum.value_namespace = name_space
                    self.rttmonjitterstatsrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTSum2High"):
                    self.rttmonjitterstatsrttsum2high = value
                    self.rttmonjitterstatsrttsum2high.value_namespace = name_space
                    self.rttmonjitterstatsrttsum2high.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTSum2Low"):
                    self.rttmonjitterstatsrttsum2low = value
                    self.rttmonjitterstatsrttsum2low.value_namespace = name_space
                    self.rttmonjitterstatsrttsum2low.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsRTTSumHigh"):
                    self.rttmonjitterstatsrttsumhigh = value
                    self.rttmonjitterstatsrttsumhigh.value_namespace = name_space
                    self.rttmonjitterstatsrttsumhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2NegativesDSHigh"):
                    self.rttmonjitterstatssum2negativesdshigh = value
                    self.rttmonjitterstatssum2negativesdshigh.value_namespace = name_space
                    self.rttmonjitterstatssum2negativesdshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2NegativesDSLow"):
                    self.rttmonjitterstatssum2negativesdslow = value
                    self.rttmonjitterstatssum2negativesdslow.value_namespace = name_space
                    self.rttmonjitterstatssum2negativesdslow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2NegativesSDHigh"):
                    self.rttmonjitterstatssum2negativessdhigh = value
                    self.rttmonjitterstatssum2negativessdhigh.value_namespace = name_space
                    self.rttmonjitterstatssum2negativessdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2NegativesSDLow"):
                    self.rttmonjitterstatssum2negativessdlow = value
                    self.rttmonjitterstatssum2negativessdlow.value_namespace = name_space
                    self.rttmonjitterstatssum2negativessdlow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2PositivesDSHigh"):
                    self.rttmonjitterstatssum2positivesdshigh = value
                    self.rttmonjitterstatssum2positivesdshigh.value_namespace = name_space
                    self.rttmonjitterstatssum2positivesdshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2PositivesDSLow"):
                    self.rttmonjitterstatssum2positivesdslow = value
                    self.rttmonjitterstatssum2positivesdslow.value_namespace = name_space
                    self.rttmonjitterstatssum2positivesdslow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2PositivesSDHigh"):
                    self.rttmonjitterstatssum2positivessdhigh = value
                    self.rttmonjitterstatssum2positivessdhigh.value_namespace = name_space
                    self.rttmonjitterstatssum2positivessdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSum2PositivesSDLow"):
                    self.rttmonjitterstatssum2positivessdlow = value
                    self.rttmonjitterstatssum2positivessdlow.value_namespace = name_space
                    self.rttmonjitterstatssum2positivessdlow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSumOfNegativesDS"):
                    self.rttmonjitterstatssumofnegativesds = value
                    self.rttmonjitterstatssumofnegativesds.value_namespace = name_space
                    self.rttmonjitterstatssumofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSumOfNegativesSD"):
                    self.rttmonjitterstatssumofnegativessd = value
                    self.rttmonjitterstatssumofnegativessd.value_namespace = name_space
                    self.rttmonjitterstatssumofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSumOfPositivesDS"):
                    self.rttmonjitterstatssumofpositivesds = value
                    self.rttmonjitterstatssumofpositivesds.value_namespace = name_space
                    self.rttmonjitterstatssumofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsSumOfPositivesSD"):
                    self.rttmonjitterstatssumofpositivessd = value
                    self.rttmonjitterstatssumofpositivessd.value_namespace = name_space
                    self.rttmonjitterstatssumofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonJitterStatsUnSyncRTs"):
                    self.rttmonjitterstatsunsyncrts = value
                    self.rttmonjitterstatsunsyncrts.value_namespace = name_space
                    self.rttmonjitterstatsunsyncrts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonjitterstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonjitterstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonJitterStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonJitterStatsEntry"):
                for c in self.rttmonjitterstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonjitterstatstable.Rttmonjitterstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonjitterstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonJitterStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonlpdgrpstatsentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonlpdgrpstatstable, self).__init__()

            self.yang_name = "rttMonLpdGrpStatsTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonlpdgrpstatsentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonlpdgrpstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonlpdgrpstatstable, self).__setattr__(name, value)


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
            
            .. attribute:: rttmonlpdgrpstatsgroupindex  <key>
            
            	Uniquely identifies a row in rttMonLpdGrpStatsTable.  This is a pseudo\-random number which identifies a particular LPD group
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonlpdgrpstatsstarttimeindex  <key>
            
            	The time when this row was created.  This object is the second index of the rttMonLpdGrpStatsTable. When the number of rttMonLpdGrpStatsStartTimeIndex groups exceeds the rttMplsVpnMonTypeLpdStatHours value, the oldest rttMonLpdGrpStatsStartTimeIndex group will be removed and replaced with the new entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlpdgrpstatsavgrtt
            
            	The average RTT across all set of probes in the LPD group.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsgroupprobeindex
            
            	This object identifies 'lspGroup' probe uniquely created for this particular LPD Group
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: identifier
            
            .. attribute:: rttmonlpdgrpstatsgroupstatus
            
            	This object identifies the LPD Group status.  When the LPD Group status changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdGroupStatus' or 'lpdAll' a rttMonLpdGrpStatusNotification will be generated.  When the LPD Group status value is 'unknown' or changes to 'unknown' this notification will not be generated.  When LSP Path Discovery is enabled for a particular row in rttMplsVpnMonCtrlTable, 'single probes' in the 'lspGroup' probe cannot generate notifications independently but will be generating depending on the state of the group. Notifications  are only generated if the failure/restoration of an individual probe causes the state of the LPD Group to change.  This object will be set to 'unknown' on reset
            	**type**\:   :py:class:`Rttmplsvpnmonlpdgrpstatus <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmplsvpnmonlpdgrpstatus>`
            
            .. attribute:: rttmonlpdgrpstatslpdcomptime
            
            	The completion time of the last successfull LSP Path Discovery to the target PE.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: rttmonlpdgrpstatslpdfailcause
            
            	This object identifies the cause of failure for the LSP Path Discovery last attempted. It will be only valid if rttMonLpdGrpStatsLPDFailOccurred is set to true.  This object will be set to 'unknown' on reset
            	**type**\:   :py:class:`Rttmplsvpnmonlpdfailuresense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttmplsvpnmonlpdfailuresense>`
            
            .. attribute:: rttmonlpdgrpstatslpdfailoccurred
            
            	This object is set to true when the LSP Path Discovery to the target PE i.e. rttMonLpdGrpStatsTargetPE fails, and set to false when the LSP Path Discovery succeeds.  When this value changes and rttMplsVpnMonReactLpdNotifyType is set to 'lpdPathDiscovery' or 'lpdAll' a rttMonLpdDiscoveryNotification will be generated.  This object will be set to 'FALSE' on reset
            	**type**\:  bool
            
            .. attribute:: rttmonlpdgrpstatslpdstarttime
            
            	The time when the last LSP Path Discovery to the group was attempted.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: tenths of milliseconds
            
            .. attribute:: rttmonlpdgrpstatsmaxnumpaths
            
            	The maximum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatsmaxrtt
            
            	The maximum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsminnumpaths
            
            	The minimum number of active paths discovered to the rttMonLpdGrpStatsTargetPE target.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: paths
            
            .. attribute:: rttmonlpdgrpstatsminrtt
            
            	The minimum of RTT's for all set of probes in the LPD group that were successfully measured.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonlpdgrpstatsnumoffail
            
            	This object represents the number of failed operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value other than 'ok' or 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: failures
            
            .. attribute:: rttmonlpdgrpstatsnumofpass
            
            	This object represents the number of successfull completions of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense value is 'ok' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: passes
            
            .. attribute:: rttmonlpdgrpstatsnumoftimeout
            
            	This object represents the number of timed out operations of 'single probes' for all the set of paths in the LPD group.  Whenever the rttMonLatestRttOperSense has a value of 'timeout' for a particular probe in the LPD Group this object will be incremented.  This object will be set to '0' on reset
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: timeouts
            
            .. attribute:: rttmonlpdgrpstatspathids
            
            	A string which holds the list of information to uniquely identify the paths to the target PE. This information is used by the 'single probes' when testing the paths.  Following three parameters are needed to uniquely identify a  path   \- lsp\-selector (127.x.x.x)   \- outgoing\-interface (i/f)   \- label\-stack (s), if mutiple labels they will be colon (\:)     separated.  These parameters will be hyphen (\-) separated for a particular path. This set of information will be comma (,) separated for all the paths discovered as part of this LPD Group.  For example\: If there are 5 paths in the LPD group then this object will return all the identifier's to uniquely identify the path.  The output will look like '127.0.0.1\-Se3/0.1\-20\:18, 127.0.0.2\-Se3/0.1\-20,127.0.0.3\-Se3/0.1\-20,127.0.0.4\-Se3/0.1\-20, 127.0.0.5\-Se3/0.1\-20'.  This object will be set to '0' on reset
            	**type**\:  str
            
            .. attribute:: rttmonlpdgrpstatsprobestatus
            
            	A string which holds the latest operation return code for all the set of 'single probes' which are part of the LPD group. The return codes will be comma separated and will follow the same sequence of probes as followed in 'rttMonLpdGrpStatsPathIds'. The latest operation return code will be mapped to 'up','down' or 'unkwown'.  'up' \- Probe state is up when the rttMonLatestRttOperSense value is 'ok'. 'down' \- Probe state is down when the rttMonLatestRttOperSense has value other then 'ok' and 'other'. 'unknown' \- Probe state is unkown when the rttMonLatestRttOperSense value is 'other'.  For example\: If there are 5 paths in the LPD group then this object output will look like 'ok,ok,ok,down,down'.  This object will be set to '0' on reset
            	**type**\:  str
            
            .. attribute:: rttmonlpdgrpstatsresettime
            
            	This object specifies the time when this statistics row was last reset using the rttMonApplLpdGrpStatsReset object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlpdgrpstatstargetpe
            
            	The object is a string that specifies the address of the target PE for this LPD group
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry, self).__init__()

                self.yang_name = "rttMonLpdGrpStatsEntry"
                self.yang_parent_name = "rttMonLpdGrpStatsTable"

                self.rttmonlpdgrpstatsgroupindex = YLeaf(YType.int32, "rttMonLpdGrpStatsGroupIndex")

                self.rttmonlpdgrpstatsstarttimeindex = YLeaf(YType.uint32, "rttMonLpdGrpStatsStartTimeIndex")

                self.rttmonlpdgrpstatsavgrtt = YLeaf(YType.int32, "rttMonLpdGrpStatsAvgRTT")

                self.rttmonlpdgrpstatsgroupprobeindex = YLeaf(YType.int32, "rttMonLpdGrpStatsGroupProbeIndex")

                self.rttmonlpdgrpstatsgroupstatus = YLeaf(YType.enumeration, "rttMonLpdGrpStatsGroupStatus")

                self.rttmonlpdgrpstatslpdcomptime = YLeaf(YType.int32, "rttMonLpdGrpStatsLPDCompTime")

                self.rttmonlpdgrpstatslpdfailcause = YLeaf(YType.enumeration, "rttMonLpdGrpStatsLPDFailCause")

                self.rttmonlpdgrpstatslpdfailoccurred = YLeaf(YType.boolean, "rttMonLpdGrpStatsLPDFailOccurred")

                self.rttmonlpdgrpstatslpdstarttime = YLeaf(YType.uint32, "rttMonLpdGrpStatsLPDStartTime")

                self.rttmonlpdgrpstatsmaxnumpaths = YLeaf(YType.int32, "rttMonLpdGrpStatsMaxNumPaths")

                self.rttmonlpdgrpstatsmaxrtt = YLeaf(YType.int32, "rttMonLpdGrpStatsMaxRTT")

                self.rttmonlpdgrpstatsminnumpaths = YLeaf(YType.int32, "rttMonLpdGrpStatsMinNumPaths")

                self.rttmonlpdgrpstatsminrtt = YLeaf(YType.int32, "rttMonLpdGrpStatsMinRTT")

                self.rttmonlpdgrpstatsnumoffail = YLeaf(YType.int32, "rttMonLpdGrpStatsNumOfFail")

                self.rttmonlpdgrpstatsnumofpass = YLeaf(YType.int32, "rttMonLpdGrpStatsNumOfPass")

                self.rttmonlpdgrpstatsnumoftimeout = YLeaf(YType.int32, "rttMonLpdGrpStatsNumOfTimeout")

                self.rttmonlpdgrpstatspathids = YLeaf(YType.str, "rttMonLpdGrpStatsPathIds")

                self.rttmonlpdgrpstatsprobestatus = YLeaf(YType.str, "rttMonLpdGrpStatsProbeStatus")

                self.rttmonlpdgrpstatsresettime = YLeaf(YType.uint32, "rttMonLpdGrpStatsResetTime")

                self.rttmonlpdgrpstatstargetpe = YLeaf(YType.str, "rttMonLpdGrpStatsTargetPE")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonlpdgrpstatsgroupindex",
                                "rttmonlpdgrpstatsstarttimeindex",
                                "rttmonlpdgrpstatsavgrtt",
                                "rttmonlpdgrpstatsgroupprobeindex",
                                "rttmonlpdgrpstatsgroupstatus",
                                "rttmonlpdgrpstatslpdcomptime",
                                "rttmonlpdgrpstatslpdfailcause",
                                "rttmonlpdgrpstatslpdfailoccurred",
                                "rttmonlpdgrpstatslpdstarttime",
                                "rttmonlpdgrpstatsmaxnumpaths",
                                "rttmonlpdgrpstatsmaxrtt",
                                "rttmonlpdgrpstatsminnumpaths",
                                "rttmonlpdgrpstatsminrtt",
                                "rttmonlpdgrpstatsnumoffail",
                                "rttmonlpdgrpstatsnumofpass",
                                "rttmonlpdgrpstatsnumoftimeout",
                                "rttmonlpdgrpstatspathids",
                                "rttmonlpdgrpstatsprobestatus",
                                "rttmonlpdgrpstatsresettime",
                                "rttmonlpdgrpstatstargetpe") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonlpdgrpstatsgroupindex.is_set or
                    self.rttmonlpdgrpstatsstarttimeindex.is_set or
                    self.rttmonlpdgrpstatsavgrtt.is_set or
                    self.rttmonlpdgrpstatsgroupprobeindex.is_set or
                    self.rttmonlpdgrpstatsgroupstatus.is_set or
                    self.rttmonlpdgrpstatslpdcomptime.is_set or
                    self.rttmonlpdgrpstatslpdfailcause.is_set or
                    self.rttmonlpdgrpstatslpdfailoccurred.is_set or
                    self.rttmonlpdgrpstatslpdstarttime.is_set or
                    self.rttmonlpdgrpstatsmaxnumpaths.is_set or
                    self.rttmonlpdgrpstatsmaxrtt.is_set or
                    self.rttmonlpdgrpstatsminnumpaths.is_set or
                    self.rttmonlpdgrpstatsminrtt.is_set or
                    self.rttmonlpdgrpstatsnumoffail.is_set or
                    self.rttmonlpdgrpstatsnumofpass.is_set or
                    self.rttmonlpdgrpstatsnumoftimeout.is_set or
                    self.rttmonlpdgrpstatspathids.is_set or
                    self.rttmonlpdgrpstatsprobestatus.is_set or
                    self.rttmonlpdgrpstatsresettime.is_set or
                    self.rttmonlpdgrpstatstargetpe.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsgroupindex.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsstarttimeindex.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsavgrtt.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsgroupprobeindex.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsgroupstatus.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatslpdcomptime.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatslpdfailcause.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatslpdfailoccurred.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatslpdstarttime.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsmaxnumpaths.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsmaxrtt.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsminnumpaths.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsminrtt.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsnumoffail.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsnumofpass.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsnumoftimeout.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatspathids.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsprobestatus.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatsresettime.yfilter != YFilter.not_set or
                    self.rttmonlpdgrpstatstargetpe.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonLpdGrpStatsEntry" + "[rttMonLpdGrpStatsGroupIndex='" + self.rttmonlpdgrpstatsgroupindex.get() + "']" + "[rttMonLpdGrpStatsStartTimeIndex='" + self.rttmonlpdgrpstatsstarttimeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLpdGrpStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonlpdgrpstatsgroupindex.is_set or self.rttmonlpdgrpstatsgroupindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsgroupindex.get_name_leafdata())
                if (self.rttmonlpdgrpstatsstarttimeindex.is_set or self.rttmonlpdgrpstatsstarttimeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsstarttimeindex.get_name_leafdata())
                if (self.rttmonlpdgrpstatsavgrtt.is_set or self.rttmonlpdgrpstatsavgrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsavgrtt.get_name_leafdata())
                if (self.rttmonlpdgrpstatsgroupprobeindex.is_set or self.rttmonlpdgrpstatsgroupprobeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsgroupprobeindex.get_name_leafdata())
                if (self.rttmonlpdgrpstatsgroupstatus.is_set or self.rttmonlpdgrpstatsgroupstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsgroupstatus.get_name_leafdata())
                if (self.rttmonlpdgrpstatslpdcomptime.is_set or self.rttmonlpdgrpstatslpdcomptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatslpdcomptime.get_name_leafdata())
                if (self.rttmonlpdgrpstatslpdfailcause.is_set or self.rttmonlpdgrpstatslpdfailcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatslpdfailcause.get_name_leafdata())
                if (self.rttmonlpdgrpstatslpdfailoccurred.is_set or self.rttmonlpdgrpstatslpdfailoccurred.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatslpdfailoccurred.get_name_leafdata())
                if (self.rttmonlpdgrpstatslpdstarttime.is_set or self.rttmonlpdgrpstatslpdstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatslpdstarttime.get_name_leafdata())
                if (self.rttmonlpdgrpstatsmaxnumpaths.is_set or self.rttmonlpdgrpstatsmaxnumpaths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsmaxnumpaths.get_name_leafdata())
                if (self.rttmonlpdgrpstatsmaxrtt.is_set or self.rttmonlpdgrpstatsmaxrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsmaxrtt.get_name_leafdata())
                if (self.rttmonlpdgrpstatsminnumpaths.is_set or self.rttmonlpdgrpstatsminnumpaths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsminnumpaths.get_name_leafdata())
                if (self.rttmonlpdgrpstatsminrtt.is_set or self.rttmonlpdgrpstatsminrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsminrtt.get_name_leafdata())
                if (self.rttmonlpdgrpstatsnumoffail.is_set or self.rttmonlpdgrpstatsnumoffail.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsnumoffail.get_name_leafdata())
                if (self.rttmonlpdgrpstatsnumofpass.is_set or self.rttmonlpdgrpstatsnumofpass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsnumofpass.get_name_leafdata())
                if (self.rttmonlpdgrpstatsnumoftimeout.is_set or self.rttmonlpdgrpstatsnumoftimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsnumoftimeout.get_name_leafdata())
                if (self.rttmonlpdgrpstatspathids.is_set or self.rttmonlpdgrpstatspathids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatspathids.get_name_leafdata())
                if (self.rttmonlpdgrpstatsprobestatus.is_set or self.rttmonlpdgrpstatsprobestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsprobestatus.get_name_leafdata())
                if (self.rttmonlpdgrpstatsresettime.is_set or self.rttmonlpdgrpstatsresettime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatsresettime.get_name_leafdata())
                if (self.rttmonlpdgrpstatstargetpe.is_set or self.rttmonlpdgrpstatstargetpe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlpdgrpstatstargetpe.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonLpdGrpStatsGroupIndex" or name == "rttMonLpdGrpStatsStartTimeIndex" or name == "rttMonLpdGrpStatsAvgRTT" or name == "rttMonLpdGrpStatsGroupProbeIndex" or name == "rttMonLpdGrpStatsGroupStatus" or name == "rttMonLpdGrpStatsLPDCompTime" or name == "rttMonLpdGrpStatsLPDFailCause" or name == "rttMonLpdGrpStatsLPDFailOccurred" or name == "rttMonLpdGrpStatsLPDStartTime" or name == "rttMonLpdGrpStatsMaxNumPaths" or name == "rttMonLpdGrpStatsMaxRTT" or name == "rttMonLpdGrpStatsMinNumPaths" or name == "rttMonLpdGrpStatsMinRTT" or name == "rttMonLpdGrpStatsNumOfFail" or name == "rttMonLpdGrpStatsNumOfPass" or name == "rttMonLpdGrpStatsNumOfTimeout" or name == "rttMonLpdGrpStatsPathIds" or name == "rttMonLpdGrpStatsProbeStatus" or name == "rttMonLpdGrpStatsResetTime" or name == "rttMonLpdGrpStatsTargetPE"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonLpdGrpStatsGroupIndex"):
                    self.rttmonlpdgrpstatsgroupindex = value
                    self.rttmonlpdgrpstatsgroupindex.value_namespace = name_space
                    self.rttmonlpdgrpstatsgroupindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsStartTimeIndex"):
                    self.rttmonlpdgrpstatsstarttimeindex = value
                    self.rttmonlpdgrpstatsstarttimeindex.value_namespace = name_space
                    self.rttmonlpdgrpstatsstarttimeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsAvgRTT"):
                    self.rttmonlpdgrpstatsavgrtt = value
                    self.rttmonlpdgrpstatsavgrtt.value_namespace = name_space
                    self.rttmonlpdgrpstatsavgrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsGroupProbeIndex"):
                    self.rttmonlpdgrpstatsgroupprobeindex = value
                    self.rttmonlpdgrpstatsgroupprobeindex.value_namespace = name_space
                    self.rttmonlpdgrpstatsgroupprobeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsGroupStatus"):
                    self.rttmonlpdgrpstatsgroupstatus = value
                    self.rttmonlpdgrpstatsgroupstatus.value_namespace = name_space
                    self.rttmonlpdgrpstatsgroupstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsLPDCompTime"):
                    self.rttmonlpdgrpstatslpdcomptime = value
                    self.rttmonlpdgrpstatslpdcomptime.value_namespace = name_space
                    self.rttmonlpdgrpstatslpdcomptime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsLPDFailCause"):
                    self.rttmonlpdgrpstatslpdfailcause = value
                    self.rttmonlpdgrpstatslpdfailcause.value_namespace = name_space
                    self.rttmonlpdgrpstatslpdfailcause.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsLPDFailOccurred"):
                    self.rttmonlpdgrpstatslpdfailoccurred = value
                    self.rttmonlpdgrpstatslpdfailoccurred.value_namespace = name_space
                    self.rttmonlpdgrpstatslpdfailoccurred.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsLPDStartTime"):
                    self.rttmonlpdgrpstatslpdstarttime = value
                    self.rttmonlpdgrpstatslpdstarttime.value_namespace = name_space
                    self.rttmonlpdgrpstatslpdstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsMaxNumPaths"):
                    self.rttmonlpdgrpstatsmaxnumpaths = value
                    self.rttmonlpdgrpstatsmaxnumpaths.value_namespace = name_space
                    self.rttmonlpdgrpstatsmaxnumpaths.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsMaxRTT"):
                    self.rttmonlpdgrpstatsmaxrtt = value
                    self.rttmonlpdgrpstatsmaxrtt.value_namespace = name_space
                    self.rttmonlpdgrpstatsmaxrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsMinNumPaths"):
                    self.rttmonlpdgrpstatsminnumpaths = value
                    self.rttmonlpdgrpstatsminnumpaths.value_namespace = name_space
                    self.rttmonlpdgrpstatsminnumpaths.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsMinRTT"):
                    self.rttmonlpdgrpstatsminrtt = value
                    self.rttmonlpdgrpstatsminrtt.value_namespace = name_space
                    self.rttmonlpdgrpstatsminrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsNumOfFail"):
                    self.rttmonlpdgrpstatsnumoffail = value
                    self.rttmonlpdgrpstatsnumoffail.value_namespace = name_space
                    self.rttmonlpdgrpstatsnumoffail.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsNumOfPass"):
                    self.rttmonlpdgrpstatsnumofpass = value
                    self.rttmonlpdgrpstatsnumofpass.value_namespace = name_space
                    self.rttmonlpdgrpstatsnumofpass.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsNumOfTimeout"):
                    self.rttmonlpdgrpstatsnumoftimeout = value
                    self.rttmonlpdgrpstatsnumoftimeout.value_namespace = name_space
                    self.rttmonlpdgrpstatsnumoftimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsPathIds"):
                    self.rttmonlpdgrpstatspathids = value
                    self.rttmonlpdgrpstatspathids.value_namespace = name_space
                    self.rttmonlpdgrpstatspathids.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsProbeStatus"):
                    self.rttmonlpdgrpstatsprobestatus = value
                    self.rttmonlpdgrpstatsprobestatus.value_namespace = name_space
                    self.rttmonlpdgrpstatsprobestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsResetTime"):
                    self.rttmonlpdgrpstatsresettime = value
                    self.rttmonlpdgrpstatsresettime.value_namespace = name_space
                    self.rttmonlpdgrpstatsresettime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLpdGrpStatsTargetPE"):
                    self.rttmonlpdgrpstatstargetpe = value
                    self.rttmonlpdgrpstatstargetpe.value_namespace = name_space
                    self.rttmonlpdgrpstatstargetpe.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonlpdgrpstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonlpdgrpstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonLpdGrpStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonLpdGrpStatsEntry"):
                for c in self.rttmonlpdgrpstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonlpdgrpstatstable.Rttmonlpdgrpstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonlpdgrpstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonLpdGrpStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Rttmonhistorycollectionentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonhistorycollectiontable, self).__init__()

            self.yang_name = "rttMonHistoryCollectionTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonhistorycollectionentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonhistorycollectiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonhistorycollectiontable, self).__setattr__(name, value)


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
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonhistorycollectionlifeindex  <key>
            
            	This uniquely defines a life for a conceptual history row.  For a particular value of rttMonHistoryCollectionLifeIndex, the agent assigns the first value of 1, the second value  of 2, and so on.  The sequence keeps incrementing,  despite older (lower) values being removed from the  table
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonhistorycollectionbucketindex  <key>
            
            	When the RttMonRttType is 'pathEcho', this uniquely defines a bucket for a given value of  rttMonHistoryCollectionLifeIndex.  For all other  RttMonRttType this value will be the number of operations per a lifetime.  Thus, this object  increments on each operation attempt.  For a particular value of  rttMonHistoryCollectionLifeIndex, the agent assigns  the first value of 1, the second value of 2, and so  on.  The sequence keeps incrementing until the number of buckets equals rttMonHistoryAdminNumBuckets, after which the most recent rttMonHistoryAdminNumBuckets  buckets are retained (the index is incremented though)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rttmonhistorycollectionsampleindex  <key>
            
            	This uniquely defines a row for a given value of rttMonHistoryCollectionBucketIndex.  This object represents a hop along a path to the Target.  For a particular value of  rttMonHistoryCollectionBucketIndex, the agent assigns  the first value of 1, the second value of 2, and so on. The sequence keeps incrementing until the number of  samples equals rttMonHistoryAdminNumSamples, then no  new samples are created for the current  rttMonHistoryCollectionBucketIndex.  When the RttMonRttType is 'pathEcho', this value  directly represents the number of hops along a  path to a target, thus we can only support 512 hops. For all other values of RttMonRttType this object will be one
            	**type**\:  int
            
            	**range:** 1..512
            
            .. attribute:: rttmonhistorycollectionaddress
            
            	When the RttMonRttType is 'echo' or 'pathEcho' this is a string which specifies the address of the target for the this RTT operation.  For all other values of RttMonRttType this string will be null.  This address will be the address of the hop along the path to the rttMonEchoAdminTargetAddress address, including rttMonEchoAdminTargetAddress address, or just the rttMonEchoAdminTargetAddress address, when the path information is not collected.  This behavior is defined by the rttMonCtrlAdminRttType object.  The interpretation of this string depends on the type of RTT operation selected, as specified by the rttMonEchoAdminProtocol object.  See rttMonEchoAdminTargetAddress for a complete description
            	**type**\:  str
            
            .. attribute:: rttmonhistorycollectionapplspecificsense
            
            	An application specific sense code for the completion status of the last RTT operation.  This  object will only be valid when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'.  Otherwise, this object's  value is not valid
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonhistorycollectioncompletiontime
            
            	This is the operation completion time of the RTT operation.  If the RTT operation fails  (rttMonHistoryCollectionSense is any  value other than ok), this has a value of 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: rttmonhistorycollectionsampletime
            
            	The time that the RTT operation was initiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonhistorycollectionsense
            
            	A sense code for the completion status of the RTT operation
            	**type**\:   :py:class:`Rttresponsesense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttresponsesense>`
            
            .. attribute:: rttmonhistorycollectionsensedescription
            
            	A sense description for the completion status of the last RTT operation when the  rttMonHistoryCollectionSense object is set to  'applicationSpecific'
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry, self).__init__()

                self.yang_name = "rttMonHistoryCollectionEntry"
                self.yang_parent_name = "rttMonHistoryCollectionTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonhistorycollectionlifeindex = YLeaf(YType.int32, "rttMonHistoryCollectionLifeIndex")

                self.rttmonhistorycollectionbucketindex = YLeaf(YType.int32, "rttMonHistoryCollectionBucketIndex")

                self.rttmonhistorycollectionsampleindex = YLeaf(YType.int32, "rttMonHistoryCollectionSampleIndex")

                self.rttmonhistorycollectionaddress = YLeaf(YType.str, "rttMonHistoryCollectionAddress")

                self.rttmonhistorycollectionapplspecificsense = YLeaf(YType.int32, "rttMonHistoryCollectionApplSpecificSense")

                self.rttmonhistorycollectioncompletiontime = YLeaf(YType.uint32, "rttMonHistoryCollectionCompletionTime")

                self.rttmonhistorycollectionsampletime = YLeaf(YType.uint32, "rttMonHistoryCollectionSampleTime")

                self.rttmonhistorycollectionsense = YLeaf(YType.enumeration, "rttMonHistoryCollectionSense")

                self.rttmonhistorycollectionsensedescription = YLeaf(YType.str, "rttMonHistoryCollectionSenseDescription")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonhistorycollectionlifeindex",
                                "rttmonhistorycollectionbucketindex",
                                "rttmonhistorycollectionsampleindex",
                                "rttmonhistorycollectionaddress",
                                "rttmonhistorycollectionapplspecificsense",
                                "rttmonhistorycollectioncompletiontime",
                                "rttmonhistorycollectionsampletime",
                                "rttmonhistorycollectionsense",
                                "rttmonhistorycollectionsensedescription") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonhistorycollectionlifeindex.is_set or
                    self.rttmonhistorycollectionbucketindex.is_set or
                    self.rttmonhistorycollectionsampleindex.is_set or
                    self.rttmonhistorycollectionaddress.is_set or
                    self.rttmonhistorycollectionapplspecificsense.is_set or
                    self.rttmonhistorycollectioncompletiontime.is_set or
                    self.rttmonhistorycollectionsampletime.is_set or
                    self.rttmonhistorycollectionsense.is_set or
                    self.rttmonhistorycollectionsensedescription.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionlifeindex.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionbucketindex.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionsampleindex.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionaddress.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionapplspecificsense.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectioncompletiontime.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionsampletime.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionsense.yfilter != YFilter.not_set or
                    self.rttmonhistorycollectionsensedescription.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonHistoryCollectionEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + "[rttMonHistoryCollectionLifeIndex='" + self.rttmonhistorycollectionlifeindex.get() + "']" + "[rttMonHistoryCollectionBucketIndex='" + self.rttmonhistorycollectionbucketindex.get() + "']" + "[rttMonHistoryCollectionSampleIndex='" + self.rttmonhistorycollectionsampleindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonHistoryCollectionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonhistorycollectionlifeindex.is_set or self.rttmonhistorycollectionlifeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionlifeindex.get_name_leafdata())
                if (self.rttmonhistorycollectionbucketindex.is_set or self.rttmonhistorycollectionbucketindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionbucketindex.get_name_leafdata())
                if (self.rttmonhistorycollectionsampleindex.is_set or self.rttmonhistorycollectionsampleindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionsampleindex.get_name_leafdata())
                if (self.rttmonhistorycollectionaddress.is_set or self.rttmonhistorycollectionaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionaddress.get_name_leafdata())
                if (self.rttmonhistorycollectionapplspecificsense.is_set or self.rttmonhistorycollectionapplspecificsense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionapplspecificsense.get_name_leafdata())
                if (self.rttmonhistorycollectioncompletiontime.is_set or self.rttmonhistorycollectioncompletiontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectioncompletiontime.get_name_leafdata())
                if (self.rttmonhistorycollectionsampletime.is_set or self.rttmonhistorycollectionsampletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionsampletime.get_name_leafdata())
                if (self.rttmonhistorycollectionsense.is_set or self.rttmonhistorycollectionsense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionsense.get_name_leafdata())
                if (self.rttmonhistorycollectionsensedescription.is_set or self.rttmonhistorycollectionsensedescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonhistorycollectionsensedescription.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonHistoryCollectionLifeIndex" or name == "rttMonHistoryCollectionBucketIndex" or name == "rttMonHistoryCollectionSampleIndex" or name == "rttMonHistoryCollectionAddress" or name == "rttMonHistoryCollectionApplSpecificSense" or name == "rttMonHistoryCollectionCompletionTime" or name == "rttMonHistoryCollectionSampleTime" or name == "rttMonHistoryCollectionSense" or name == "rttMonHistoryCollectionSenseDescription"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionLifeIndex"):
                    self.rttmonhistorycollectionlifeindex = value
                    self.rttmonhistorycollectionlifeindex.value_namespace = name_space
                    self.rttmonhistorycollectionlifeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionBucketIndex"):
                    self.rttmonhistorycollectionbucketindex = value
                    self.rttmonhistorycollectionbucketindex.value_namespace = name_space
                    self.rttmonhistorycollectionbucketindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionSampleIndex"):
                    self.rttmonhistorycollectionsampleindex = value
                    self.rttmonhistorycollectionsampleindex.value_namespace = name_space
                    self.rttmonhistorycollectionsampleindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionAddress"):
                    self.rttmonhistorycollectionaddress = value
                    self.rttmonhistorycollectionaddress.value_namespace = name_space
                    self.rttmonhistorycollectionaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionApplSpecificSense"):
                    self.rttmonhistorycollectionapplspecificsense = value
                    self.rttmonhistorycollectionapplspecificsense.value_namespace = name_space
                    self.rttmonhistorycollectionapplspecificsense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionCompletionTime"):
                    self.rttmonhistorycollectioncompletiontime = value
                    self.rttmonhistorycollectioncompletiontime.value_namespace = name_space
                    self.rttmonhistorycollectioncompletiontime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionSampleTime"):
                    self.rttmonhistorycollectionsampletime = value
                    self.rttmonhistorycollectionsampletime.value_namespace = name_space
                    self.rttmonhistorycollectionsampletime.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionSense"):
                    self.rttmonhistorycollectionsense = value
                    self.rttmonhistorycollectionsense.value_namespace = name_space
                    self.rttmonhistorycollectionsense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonHistoryCollectionSenseDescription"):
                    self.rttmonhistorycollectionsensedescription = value
                    self.rttmonhistorycollectionsensedescription.value_namespace = name_space
                    self.rttmonhistorycollectionsensedescription.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonhistorycollectionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonhistorycollectionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonHistoryCollectionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonHistoryCollectionEntry"):
                for c in self.rttmonhistorycollectionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonhistorycollectiontable.Rttmonhistorycollectionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonhistorycollectionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonHistoryCollectionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonlatesthttpopertable(Entity):
        """
        A table which contains the status of latest HTTP RTT
        operation.
        
        .. attribute:: rttmonlatesthttpoperentry
        
        	A list of objects that record the latest HTTP RTT operation. This entry is created automatically after the  rttMonCtrlAdminEntry is created. Also the entry is  automatically deleted when rttMonCtrlAdminEntry is deleted
        	**type**\: list of    :py:class:`Rttmonlatesthttpoperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonlatesthttpopertable, self).__init__()

            self.yang_name = "rttMonLatestHTTPOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonlatesthttpoperentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonlatesthttpopertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonlatesthttpopertable, self).__setattr__(name, value)


        class Rttmonlatesthttpoperentry(Entity):
            """
            A list of objects that record the latest HTTP RTT
            operation. This entry is created automatically after the 
            rttMonCtrlAdminEntry is created. Also the entry is 
            automatically deleted when rttMonCtrlAdminEntry is deleted.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonlatesthttperrorsensedescription
            
            	An sense description for the completion status of the latest RTT operation
            	**type**\:  str
            
            .. attribute:: rttmonlatesthttpoperdnsrtt
            
            	Round Trip Time taken to perform DNS query within the HTTP operation. If an IP Address is specified in the URL,  then DNSRTT is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopermessagebodyoctets
            
            	The size of the message body received as a response to the HTTP request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpoperrtt
            
            	Round Trip Time taken to perform HTTP operation. This value is the sum of DNSRTT, TCPConnectRTT and TransactionRTT
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopersense
            
            	An application specific sense code for the completion status of the latest RTT operation
            	**type**\:   :py:class:`Rttresponsesense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttresponsesense>`
            
            .. attribute:: rttmonlatesthttpopertcpconnectrtt
            
            	Round Trip Time taken to connect to the HTTP server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatesthttpopertransactionrtt
            
            	Round Trip Time taken to download the object specified by the URL
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry, self).__init__()

                self.yang_name = "rttMonLatestHTTPOperEntry"
                self.yang_parent_name = "rttMonLatestHTTPOperTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonlatesthttperrorsensedescription = YLeaf(YType.str, "rttMonLatestHTTPErrorSenseDescription")

                self.rttmonlatesthttpoperdnsrtt = YLeaf(YType.uint32, "rttMonLatestHTTPOperDNSRTT")

                self.rttmonlatesthttpopermessagebodyoctets = YLeaf(YType.uint32, "rttMonLatestHTTPOperMessageBodyOctets")

                self.rttmonlatesthttpoperrtt = YLeaf(YType.uint32, "rttMonLatestHTTPOperRTT")

                self.rttmonlatesthttpopersense = YLeaf(YType.enumeration, "rttMonLatestHTTPOperSense")

                self.rttmonlatesthttpopertcpconnectrtt = YLeaf(YType.uint32, "rttMonLatestHTTPOperTCPConnectRTT")

                self.rttmonlatesthttpopertransactionrtt = YLeaf(YType.uint32, "rttMonLatestHTTPOperTransactionRTT")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonlatesthttperrorsensedescription",
                                "rttmonlatesthttpoperdnsrtt",
                                "rttmonlatesthttpopermessagebodyoctets",
                                "rttmonlatesthttpoperrtt",
                                "rttmonlatesthttpopersense",
                                "rttmonlatesthttpopertcpconnectrtt",
                                "rttmonlatesthttpopertransactionrtt") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonlatesthttperrorsensedescription.is_set or
                    self.rttmonlatesthttpoperdnsrtt.is_set or
                    self.rttmonlatesthttpopermessagebodyoctets.is_set or
                    self.rttmonlatesthttpoperrtt.is_set or
                    self.rttmonlatesthttpopersense.is_set or
                    self.rttmonlatesthttpopertcpconnectrtt.is_set or
                    self.rttmonlatesthttpopertransactionrtt.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonlatesthttperrorsensedescription.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpoperdnsrtt.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpopermessagebodyoctets.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpoperrtt.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpopersense.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpopertcpconnectrtt.yfilter != YFilter.not_set or
                    self.rttmonlatesthttpopertransactionrtt.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonLatestHTTPOperEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLatestHTTPOperTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonlatesthttperrorsensedescription.is_set or self.rttmonlatesthttperrorsensedescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttperrorsensedescription.get_name_leafdata())
                if (self.rttmonlatesthttpoperdnsrtt.is_set or self.rttmonlatesthttpoperdnsrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpoperdnsrtt.get_name_leafdata())
                if (self.rttmonlatesthttpopermessagebodyoctets.is_set or self.rttmonlatesthttpopermessagebodyoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpopermessagebodyoctets.get_name_leafdata())
                if (self.rttmonlatesthttpoperrtt.is_set or self.rttmonlatesthttpoperrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpoperrtt.get_name_leafdata())
                if (self.rttmonlatesthttpopersense.is_set or self.rttmonlatesthttpopersense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpopersense.get_name_leafdata())
                if (self.rttmonlatesthttpopertcpconnectrtt.is_set or self.rttmonlatesthttpopertcpconnectrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpopertcpconnectrtt.get_name_leafdata())
                if (self.rttmonlatesthttpopertransactionrtt.is_set or self.rttmonlatesthttpopertransactionrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatesthttpopertransactionrtt.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonLatestHTTPErrorSenseDescription" or name == "rttMonLatestHTTPOperDNSRTT" or name == "rttMonLatestHTTPOperMessageBodyOctets" or name == "rttMonLatestHTTPOperRTT" or name == "rttMonLatestHTTPOperSense" or name == "rttMonLatestHTTPOperTCPConnectRTT" or name == "rttMonLatestHTTPOperTransactionRTT"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPErrorSenseDescription"):
                    self.rttmonlatesthttperrorsensedescription = value
                    self.rttmonlatesthttperrorsensedescription.value_namespace = name_space
                    self.rttmonlatesthttperrorsensedescription.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperDNSRTT"):
                    self.rttmonlatesthttpoperdnsrtt = value
                    self.rttmonlatesthttpoperdnsrtt.value_namespace = name_space
                    self.rttmonlatesthttpoperdnsrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperMessageBodyOctets"):
                    self.rttmonlatesthttpopermessagebodyoctets = value
                    self.rttmonlatesthttpopermessagebodyoctets.value_namespace = name_space
                    self.rttmonlatesthttpopermessagebodyoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperRTT"):
                    self.rttmonlatesthttpoperrtt = value
                    self.rttmonlatesthttpoperrtt.value_namespace = name_space
                    self.rttmonlatesthttpoperrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperSense"):
                    self.rttmonlatesthttpopersense = value
                    self.rttmonlatesthttpopersense.value_namespace = name_space
                    self.rttmonlatesthttpopersense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperTCPConnectRTT"):
                    self.rttmonlatesthttpopertcpconnectrtt = value
                    self.rttmonlatesthttpopertcpconnectrtt.value_namespace = name_space
                    self.rttmonlatesthttpopertcpconnectrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestHTTPOperTransactionRTT"):
                    self.rttmonlatesthttpopertransactionrtt = value
                    self.rttmonlatesthttpopertransactionrtt.value_namespace = name_space
                    self.rttmonlatesthttpopertransactionrtt.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonlatesthttpoperentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonlatesthttpoperentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonLatestHTTPOperTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonLatestHTTPOperEntry"):
                for c in self.rttmonlatesthttpoperentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonlatesthttpopertable.Rttmonlatesthttpoperentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonlatesthttpoperentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonLatestHTTPOperEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rttmonlatestjitteropertable(Entity):
        """
        A table which contains the status of latest Jitter
        operation.
        
        .. attribute:: rttmonlatestjitteroperentry
        
        	A list of objects that record the latest Jitter operation
        	**type**\: list of    :py:class:`Rttmonlatestjitteroperentry <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry>`
        
        

        """

        _prefix = 'CISCO-RTTMON-MIB'
        _revision = '2012-08-16'

        def __init__(self):
            super(CiscoRttmonMib.Rttmonlatestjitteropertable, self).__init__()

            self.yang_name = "rttMonLatestJitterOperTable"
            self.yang_parent_name = "CISCO-RTTMON-MIB"

            self.rttmonlatestjitteroperentry = YList(self)

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
                        super(CiscoRttmonMib.Rttmonlatestjitteropertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRttmonMib.Rttmonlatestjitteropertable, self).__setattr__(name, value)


        class Rttmonlatestjitteroperentry(Entity):
            """
            A list of objects that record the latest Jitter
            operation.
            
            .. attribute:: rttmonctrladminindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`rttmonctrladminindex <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonctrladmintable.Rttmonctrladminentry>`
            
            .. attribute:: rttmonlatestjittererrorsensedescription
            
            	An sense description for the completion status of the latest Jitter RTT operation
            	**type**\:  str
            
            .. attribute:: rttmonlatestjitteroperavgdsj
            
            	The average of positive and negative jitter values from destination to source for latest operation
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperavgjitter
            
            	The average of positive and negative jitter values in SD and DS direction for latest operation
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperavgsdj
            
            	The average of positive and negative jitter values from source to destination for latest operation
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperiajin
            
            	Interarrival Jitter (RFC1889) at source
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperiajout
            
            	Interarrival Jitter (RC1889) at responder
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteropericpif
            
            	Represents ICPIF value for the latest jitter operation.  This value will be 93 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteropermaxofnegativesds
            
            	The maximum of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofnegativessd
            
            	The maximum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofpositivesds
            
            	The maximum of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermaxofpositivessd
            
            	The maximum of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofnegativesds
            
            	The minimum of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofnegativessd
            
            	The minimum of absolute values of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofpositivesds
            
            	The minimum of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperminofpositivessd
            
            	The minimum of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropermos
            
            	The MOS value for the latest jitter operation in hundreds. This value will be 0 if   \- rttMonEchoAdminCodecType of the operation is notApplicable   \- the operation is not started   \- the operation is started but failed This value will be 1 for packet loss of 10% or more
            	**type**\:  int
            
            	**range:** 0..None \| 100..500
            
            .. attribute:: rttmonlatestjitteroperntpstate
            
            	A value of sync(1) means sender and responder was in sync with NTP. The NTP sync means the total of NTP offset  on sender and responder is within configured tolerance level
            	**type**\:   :py:class:`Rttmonlatestjitteroperntpstate <ydk.models.cisco_ios_xe.CISCO_RTTMON_MIB.CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry.Rttmonlatestjitteroperntpstate>`
            
            .. attribute:: rttmonlatestjitteropernumofnegativesds
            
            	The sum of number of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofnegativessd
            
            	The sum of number of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofow
            
            	The number of successful one way latency measurements
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofpositivesds
            
            	The sum of number of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofpositivessd
            
            	The sum of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropernumofrtt
            
            	The number of RTT's that were successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowavgds
            
            	The average latency value from destination to source
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperowavgsd
            
            	The average latency value from source to destination
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rttmonlatestjitteroperowmaxds
            
            	The maximum of all one way latency from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowmaxsd
            
            	The maximum of all one way latency from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowminds
            
            	The minimum of all one way latency from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowminsd
            
            	The minimum of all one way latency from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2ds
            
            	The sum of squares of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2DSHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2dshigh
            
            	The sum of squares of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2DS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2sd
            
            	The sum of squares of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSum2SDHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsum2sdhigh
            
            	The sum of squares of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSum2SD
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumds
            
            	The sum of one way latency from destination to source (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumDSHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumdshigh
            
            	The sum of one way latency from destination to source (high order 32 bits). The low order 32 bits are stored  in rttMonLatestJitterOperOWSumDS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumsd
            
            	The sum of one way latency from source to destination (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperOWSumSDHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperowsumsdhigh
            
            	The sum of one way latency from source to destination (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperOWSumSD
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlatearrival
            
            	The number of packets that arrived after the timeout
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlossds
            
            	The number of packets lost when sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketlosssd
            
            	The number of packets lost when sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketmia
            
            	The number of packets that are lost for which we cannot determine the direction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperpacketoutofsequence
            
            	The number of packets arrived out of sequence
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttmax
            
            	The maximum of RTT's that were successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttmin
            
            	The minimum of RTT's that were successfully measured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum
            
            	The sum of Jitter RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSumHigh
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum2
            
            	The sum of squares of RTT's that are successfully measured (low order 32 bits). The high order 32 bits are stored in rttMonLatestJitterOperRTTSum2High
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsum2high
            
            	The sum of squares of RTT's that are successfully measured (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum2
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperrttsumhigh
            
            	The sum of Jitter RTT's that are successfully measured. (high order 32 bits). The low order 32 bits are stored in rttMonLatestJitterOperRTTSum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersense
            
            	An application specific sense code for the completion status of the latest Jitter RTT operation
            	**type**\:   :py:class:`Rttresponsesense <ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB.Rttresponsesense>`
            
            .. attribute:: rttmonlatestjitteropersum2negativesds
            
            	The sum of squares of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2negativessd
            
            	The sum of square of RTT's of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2positivesds
            
            	The sum of squares of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersum2positivessd
            
            	The sum of square of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofnegativesds
            
            	The sum of RTT's of all negative jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofnegativessd
            
            	The sum of all negative jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofpositivesds
            
            	The sum of RTT's of all positive jitter values from packets sent from destination to source
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteropersumofpositivessd
            
            	The sum of RTT's of all positive jitter values from packets sent from source to destination
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rttmonlatestjitteroperunsyncrts
            
            	The number of RTT operations that have completed with sender and responder out of sync with NTP. The NTP sync means  the total of NTP offset on sender and responder is within  configured tolerance level
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-RTTMON-MIB'
            _revision = '2012-08-16'

            def __init__(self):
                super(CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry, self).__init__()

                self.yang_name = "rttMonLatestJitterOperEntry"
                self.yang_parent_name = "rttMonLatestJitterOperTable"

                self.rttmonctrladminindex = YLeaf(YType.str, "rttMonCtrlAdminIndex")

                self.rttmonlatestjittererrorsensedescription = YLeaf(YType.str, "rttMonLatestJitterErrorSenseDescription")

                self.rttmonlatestjitteroperavgdsj = YLeaf(YType.uint32, "rttMonLatestJitterOperAvgDSJ")

                self.rttmonlatestjitteroperavgjitter = YLeaf(YType.uint32, "rttMonLatestJitterOperAvgJitter")

                self.rttmonlatestjitteroperavgsdj = YLeaf(YType.uint32, "rttMonLatestJitterOperAvgSDJ")

                self.rttmonlatestjitteroperiajin = YLeaf(YType.uint32, "rttMonLatestJitterOperIAJIn")

                self.rttmonlatestjitteroperiajout = YLeaf(YType.uint32, "rttMonLatestJitterOperIAJOut")

                self.rttmonlatestjitteropericpif = YLeaf(YType.uint32, "rttMonLatestJitterOperICPIF")

                self.rttmonlatestjitteropermaxofnegativesds = YLeaf(YType.uint32, "rttMonLatestJitterOperMaxOfNegativesDS")

                self.rttmonlatestjitteropermaxofnegativessd = YLeaf(YType.uint32, "rttMonLatestJitterOperMaxOfNegativesSD")

                self.rttmonlatestjitteropermaxofpositivesds = YLeaf(YType.uint32, "rttMonLatestJitterOperMaxOfPositivesDS")

                self.rttmonlatestjitteropermaxofpositivessd = YLeaf(YType.uint32, "rttMonLatestJitterOperMaxOfPositivesSD")

                self.rttmonlatestjitteroperminofnegativesds = YLeaf(YType.uint32, "rttMonLatestJitterOperMinOfNegativesDS")

                self.rttmonlatestjitteroperminofnegativessd = YLeaf(YType.uint32, "rttMonLatestJitterOperMinOfNegativesSD")

                self.rttmonlatestjitteroperminofpositivesds = YLeaf(YType.uint32, "rttMonLatestJitterOperMinOfPositivesDS")

                self.rttmonlatestjitteroperminofpositivessd = YLeaf(YType.uint32, "rttMonLatestJitterOperMinOfPositivesSD")

                self.rttmonlatestjitteropermos = YLeaf(YType.uint32, "rttMonLatestJitterOperMOS")

                self.rttmonlatestjitteroperntpstate = YLeaf(YType.enumeration, "rttMonLatestJitterOperNTPState")

                self.rttmonlatestjitteropernumofnegativesds = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfNegativesDS")

                self.rttmonlatestjitteropernumofnegativessd = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfNegativesSD")

                self.rttmonlatestjitteropernumofow = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfOW")

                self.rttmonlatestjitteropernumofpositivesds = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfPositivesDS")

                self.rttmonlatestjitteropernumofpositivessd = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfPositivesSD")

                self.rttmonlatestjitteropernumofrtt = YLeaf(YType.uint32, "rttMonLatestJitterOperNumOfRTT")

                self.rttmonlatestjitteroperowavgds = YLeaf(YType.uint32, "rttMonLatestJitterOperOWAvgDS")

                self.rttmonlatestjitteroperowavgsd = YLeaf(YType.uint32, "rttMonLatestJitterOperOWAvgSD")

                self.rttmonlatestjitteroperowmaxds = YLeaf(YType.uint32, "rttMonLatestJitterOperOWMaxDS")

                self.rttmonlatestjitteroperowmaxsd = YLeaf(YType.uint32, "rttMonLatestJitterOperOWMaxSD")

                self.rttmonlatestjitteroperowminds = YLeaf(YType.uint32, "rttMonLatestJitterOperOWMinDS")

                self.rttmonlatestjitteroperowminsd = YLeaf(YType.uint32, "rttMonLatestJitterOperOWMinSD")

                self.rttmonlatestjitteroperowsum2ds = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSum2DS")

                self.rttmonlatestjitteroperowsum2dshigh = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSum2DSHigh")

                self.rttmonlatestjitteroperowsum2sd = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSum2SD")

                self.rttmonlatestjitteroperowsum2sdhigh = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSum2SDHigh")

                self.rttmonlatestjitteroperowsumds = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSumDS")

                self.rttmonlatestjitteroperowsumdshigh = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSumDSHigh")

                self.rttmonlatestjitteroperowsumsd = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSumSD")

                self.rttmonlatestjitteroperowsumsdhigh = YLeaf(YType.uint32, "rttMonLatestJitterOperOWSumSDHigh")

                self.rttmonlatestjitteroperpacketlatearrival = YLeaf(YType.uint32, "rttMonLatestJitterOperPacketLateArrival")

                self.rttmonlatestjitteroperpacketlossds = YLeaf(YType.uint32, "rttMonLatestJitterOperPacketLossDS")

                self.rttmonlatestjitteroperpacketlosssd = YLeaf(YType.uint32, "rttMonLatestJitterOperPacketLossSD")

                self.rttmonlatestjitteroperpacketmia = YLeaf(YType.uint32, "rttMonLatestJitterOperPacketMIA")

                self.rttmonlatestjitteroperpacketoutofsequence = YLeaf(YType.uint32, "rttMonLatestJitterOperPacketOutOfSequence")

                self.rttmonlatestjitteroperrttmax = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTMax")

                self.rttmonlatestjitteroperrttmin = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTMin")

                self.rttmonlatestjitteroperrttsum = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTSum")

                self.rttmonlatestjitteroperrttsum2 = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTSum2")

                self.rttmonlatestjitteroperrttsum2high = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTSum2High")

                self.rttmonlatestjitteroperrttsumhigh = YLeaf(YType.uint32, "rttMonLatestJitterOperRTTSumHigh")

                self.rttmonlatestjitteropersense = YLeaf(YType.enumeration, "rttMonLatestJitterOperSense")

                self.rttmonlatestjitteropersum2negativesds = YLeaf(YType.uint32, "rttMonLatestJitterOperSum2NegativesDS")

                self.rttmonlatestjitteropersum2negativessd = YLeaf(YType.uint32, "rttMonLatestJitterOperSum2NegativesSD")

                self.rttmonlatestjitteropersum2positivesds = YLeaf(YType.uint32, "rttMonLatestJitterOperSum2PositivesDS")

                self.rttmonlatestjitteropersum2positivessd = YLeaf(YType.uint32, "rttMonLatestJitterOperSum2PositivesSD")

                self.rttmonlatestjitteropersumofnegativesds = YLeaf(YType.uint32, "rttMonLatestJitterOperSumOfNegativesDS")

                self.rttmonlatestjitteropersumofnegativessd = YLeaf(YType.uint32, "rttMonLatestJitterOperSumOfNegativesSD")

                self.rttmonlatestjitteropersumofpositivesds = YLeaf(YType.uint32, "rttMonLatestJitterOperSumOfPositivesDS")

                self.rttmonlatestjitteropersumofpositivessd = YLeaf(YType.uint32, "rttMonLatestJitterOperSumOfPositivesSD")

                self.rttmonlatestjitteroperunsyncrts = YLeaf(YType.uint32, "rttMonLatestJitterOperUnSyncRTs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rttmonctrladminindex",
                                "rttmonlatestjittererrorsensedescription",
                                "rttmonlatestjitteroperavgdsj",
                                "rttmonlatestjitteroperavgjitter",
                                "rttmonlatestjitteroperavgsdj",
                                "rttmonlatestjitteroperiajin",
                                "rttmonlatestjitteroperiajout",
                                "rttmonlatestjitteropericpif",
                                "rttmonlatestjitteropermaxofnegativesds",
                                "rttmonlatestjitteropermaxofnegativessd",
                                "rttmonlatestjitteropermaxofpositivesds",
                                "rttmonlatestjitteropermaxofpositivessd",
                                "rttmonlatestjitteroperminofnegativesds",
                                "rttmonlatestjitteroperminofnegativessd",
                                "rttmonlatestjitteroperminofpositivesds",
                                "rttmonlatestjitteroperminofpositivessd",
                                "rttmonlatestjitteropermos",
                                "rttmonlatestjitteroperntpstate",
                                "rttmonlatestjitteropernumofnegativesds",
                                "rttmonlatestjitteropernumofnegativessd",
                                "rttmonlatestjitteropernumofow",
                                "rttmonlatestjitteropernumofpositivesds",
                                "rttmonlatestjitteropernumofpositivessd",
                                "rttmonlatestjitteropernumofrtt",
                                "rttmonlatestjitteroperowavgds",
                                "rttmonlatestjitteroperowavgsd",
                                "rttmonlatestjitteroperowmaxds",
                                "rttmonlatestjitteroperowmaxsd",
                                "rttmonlatestjitteroperowminds",
                                "rttmonlatestjitteroperowminsd",
                                "rttmonlatestjitteroperowsum2ds",
                                "rttmonlatestjitteroperowsum2dshigh",
                                "rttmonlatestjitteroperowsum2sd",
                                "rttmonlatestjitteroperowsum2sdhigh",
                                "rttmonlatestjitteroperowsumds",
                                "rttmonlatestjitteroperowsumdshigh",
                                "rttmonlatestjitteroperowsumsd",
                                "rttmonlatestjitteroperowsumsdhigh",
                                "rttmonlatestjitteroperpacketlatearrival",
                                "rttmonlatestjitteroperpacketlossds",
                                "rttmonlatestjitteroperpacketlosssd",
                                "rttmonlatestjitteroperpacketmia",
                                "rttmonlatestjitteroperpacketoutofsequence",
                                "rttmonlatestjitteroperrttmax",
                                "rttmonlatestjitteroperrttmin",
                                "rttmonlatestjitteroperrttsum",
                                "rttmonlatestjitteroperrttsum2",
                                "rttmonlatestjitteroperrttsum2high",
                                "rttmonlatestjitteroperrttsumhigh",
                                "rttmonlatestjitteropersense",
                                "rttmonlatestjitteropersum2negativesds",
                                "rttmonlatestjitteropersum2negativessd",
                                "rttmonlatestjitteropersum2positivesds",
                                "rttmonlatestjitteropersum2positivessd",
                                "rttmonlatestjitteropersumofnegativesds",
                                "rttmonlatestjitteropersumofnegativessd",
                                "rttmonlatestjitteropersumofpositivesds",
                                "rttmonlatestjitteropersumofpositivessd",
                                "rttmonlatestjitteroperunsyncrts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry, self).__setattr__(name, value)

            class Rttmonlatestjitteroperntpstate(Enum):
                """
                Rttmonlatestjitteroperntpstate

                A value of sync(1) means sender and responder was in sync

                with NTP. The NTP sync means the total of NTP offset 

                on sender and responder is within configured tolerance level.

                .. data:: sync = 1

                .. data:: outOfSync = 2

                """

                sync = Enum.YLeaf(1, "sync")

                outOfSync = Enum.YLeaf(2, "outOfSync")


            def has_data(self):
                return (
                    self.rttmonctrladminindex.is_set or
                    self.rttmonlatestjittererrorsensedescription.is_set or
                    self.rttmonlatestjitteroperavgdsj.is_set or
                    self.rttmonlatestjitteroperavgjitter.is_set or
                    self.rttmonlatestjitteroperavgsdj.is_set or
                    self.rttmonlatestjitteroperiajin.is_set or
                    self.rttmonlatestjitteroperiajout.is_set or
                    self.rttmonlatestjitteropericpif.is_set or
                    self.rttmonlatestjitteropermaxofnegativesds.is_set or
                    self.rttmonlatestjitteropermaxofnegativessd.is_set or
                    self.rttmonlatestjitteropermaxofpositivesds.is_set or
                    self.rttmonlatestjitteropermaxofpositivessd.is_set or
                    self.rttmonlatestjitteroperminofnegativesds.is_set or
                    self.rttmonlatestjitteroperminofnegativessd.is_set or
                    self.rttmonlatestjitteroperminofpositivesds.is_set or
                    self.rttmonlatestjitteroperminofpositivessd.is_set or
                    self.rttmonlatestjitteropermos.is_set or
                    self.rttmonlatestjitteroperntpstate.is_set or
                    self.rttmonlatestjitteropernumofnegativesds.is_set or
                    self.rttmonlatestjitteropernumofnegativessd.is_set or
                    self.rttmonlatestjitteropernumofow.is_set or
                    self.rttmonlatestjitteropernumofpositivesds.is_set or
                    self.rttmonlatestjitteropernumofpositivessd.is_set or
                    self.rttmonlatestjitteropernumofrtt.is_set or
                    self.rttmonlatestjitteroperowavgds.is_set or
                    self.rttmonlatestjitteroperowavgsd.is_set or
                    self.rttmonlatestjitteroperowmaxds.is_set or
                    self.rttmonlatestjitteroperowmaxsd.is_set or
                    self.rttmonlatestjitteroperowminds.is_set or
                    self.rttmonlatestjitteroperowminsd.is_set or
                    self.rttmonlatestjitteroperowsum2ds.is_set or
                    self.rttmonlatestjitteroperowsum2dshigh.is_set or
                    self.rttmonlatestjitteroperowsum2sd.is_set or
                    self.rttmonlatestjitteroperowsum2sdhigh.is_set or
                    self.rttmonlatestjitteroperowsumds.is_set or
                    self.rttmonlatestjitteroperowsumdshigh.is_set or
                    self.rttmonlatestjitteroperowsumsd.is_set or
                    self.rttmonlatestjitteroperowsumsdhigh.is_set or
                    self.rttmonlatestjitteroperpacketlatearrival.is_set or
                    self.rttmonlatestjitteroperpacketlossds.is_set or
                    self.rttmonlatestjitteroperpacketlosssd.is_set or
                    self.rttmonlatestjitteroperpacketmia.is_set or
                    self.rttmonlatestjitteroperpacketoutofsequence.is_set or
                    self.rttmonlatestjitteroperrttmax.is_set or
                    self.rttmonlatestjitteroperrttmin.is_set or
                    self.rttmonlatestjitteroperrttsum.is_set or
                    self.rttmonlatestjitteroperrttsum2.is_set or
                    self.rttmonlatestjitteroperrttsum2high.is_set or
                    self.rttmonlatestjitteroperrttsumhigh.is_set or
                    self.rttmonlatestjitteropersense.is_set or
                    self.rttmonlatestjitteropersum2negativesds.is_set or
                    self.rttmonlatestjitteropersum2negativessd.is_set or
                    self.rttmonlatestjitteropersum2positivesds.is_set or
                    self.rttmonlatestjitteropersum2positivessd.is_set or
                    self.rttmonlatestjitteropersumofnegativesds.is_set or
                    self.rttmonlatestjitteropersumofnegativessd.is_set or
                    self.rttmonlatestjitteropersumofpositivesds.is_set or
                    self.rttmonlatestjitteropersumofpositivessd.is_set or
                    self.rttmonlatestjitteroperunsyncrts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rttmonctrladminindex.yfilter != YFilter.not_set or
                    self.rttmonlatestjittererrorsensedescription.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperavgdsj.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperavgjitter.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperavgsdj.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperiajin.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperiajout.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropericpif.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropermaxofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropermaxofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropermaxofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropermaxofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperminofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperminofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperminofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperminofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropermos.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperntpstate.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofow.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropernumofrtt.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowavgds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowavgsd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowmaxds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowmaxsd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowminds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowminsd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsum2ds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsum2dshigh.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsum2sd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsum2sdhigh.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsumds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsumdshigh.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsumsd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperowsumsdhigh.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperpacketlatearrival.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperpacketlossds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperpacketlosssd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperpacketmia.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperpacketoutofsequence.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttmax.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttmin.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttsum.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttsum2.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttsum2high.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperrttsumhigh.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersense.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersum2negativesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersum2negativessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersum2positivesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersum2positivessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersumofnegativesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersumofnegativessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersumofpositivesds.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteropersumofpositivessd.yfilter != YFilter.not_set or
                    self.rttmonlatestjitteroperunsyncrts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rttMonLatestJitterOperEntry" + "[rttMonCtrlAdminIndex='" + self.rttmonctrladminindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/rttMonLatestJitterOperTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rttmonctrladminindex.is_set or self.rttmonctrladminindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonctrladminindex.get_name_leafdata())
                if (self.rttmonlatestjittererrorsensedescription.is_set or self.rttmonlatestjittererrorsensedescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjittererrorsensedescription.get_name_leafdata())
                if (self.rttmonlatestjitteroperavgdsj.is_set or self.rttmonlatestjitteroperavgdsj.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperavgdsj.get_name_leafdata())
                if (self.rttmonlatestjitteroperavgjitter.is_set or self.rttmonlatestjitteroperavgjitter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperavgjitter.get_name_leafdata())
                if (self.rttmonlatestjitteroperavgsdj.is_set or self.rttmonlatestjitteroperavgsdj.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperavgsdj.get_name_leafdata())
                if (self.rttmonlatestjitteroperiajin.is_set or self.rttmonlatestjitteroperiajin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperiajin.get_name_leafdata())
                if (self.rttmonlatestjitteroperiajout.is_set or self.rttmonlatestjitteroperiajout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperiajout.get_name_leafdata())
                if (self.rttmonlatestjitteropericpif.is_set or self.rttmonlatestjitteropericpif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropericpif.get_name_leafdata())
                if (self.rttmonlatestjitteropermaxofnegativesds.is_set or self.rttmonlatestjitteropermaxofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropermaxofnegativesds.get_name_leafdata())
                if (self.rttmonlatestjitteropermaxofnegativessd.is_set or self.rttmonlatestjitteropermaxofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropermaxofnegativessd.get_name_leafdata())
                if (self.rttmonlatestjitteropermaxofpositivesds.is_set or self.rttmonlatestjitteropermaxofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropermaxofpositivesds.get_name_leafdata())
                if (self.rttmonlatestjitteropermaxofpositivessd.is_set or self.rttmonlatestjitteropermaxofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropermaxofpositivessd.get_name_leafdata())
                if (self.rttmonlatestjitteroperminofnegativesds.is_set or self.rttmonlatestjitteroperminofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperminofnegativesds.get_name_leafdata())
                if (self.rttmonlatestjitteroperminofnegativessd.is_set or self.rttmonlatestjitteroperminofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperminofnegativessd.get_name_leafdata())
                if (self.rttmonlatestjitteroperminofpositivesds.is_set or self.rttmonlatestjitteroperminofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperminofpositivesds.get_name_leafdata())
                if (self.rttmonlatestjitteroperminofpositivessd.is_set or self.rttmonlatestjitteroperminofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperminofpositivessd.get_name_leafdata())
                if (self.rttmonlatestjitteropermos.is_set or self.rttmonlatestjitteropermos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropermos.get_name_leafdata())
                if (self.rttmonlatestjitteroperntpstate.is_set or self.rttmonlatestjitteroperntpstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperntpstate.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofnegativesds.is_set or self.rttmonlatestjitteropernumofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofnegativesds.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofnegativessd.is_set or self.rttmonlatestjitteropernumofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofnegativessd.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofow.is_set or self.rttmonlatestjitteropernumofow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofow.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofpositivesds.is_set or self.rttmonlatestjitteropernumofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofpositivesds.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofpositivessd.is_set or self.rttmonlatestjitteropernumofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofpositivessd.get_name_leafdata())
                if (self.rttmonlatestjitteropernumofrtt.is_set or self.rttmonlatestjitteropernumofrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropernumofrtt.get_name_leafdata())
                if (self.rttmonlatestjitteroperowavgds.is_set or self.rttmonlatestjitteroperowavgds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowavgds.get_name_leafdata())
                if (self.rttmonlatestjitteroperowavgsd.is_set or self.rttmonlatestjitteroperowavgsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowavgsd.get_name_leafdata())
                if (self.rttmonlatestjitteroperowmaxds.is_set or self.rttmonlatestjitteroperowmaxds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowmaxds.get_name_leafdata())
                if (self.rttmonlatestjitteroperowmaxsd.is_set or self.rttmonlatestjitteroperowmaxsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowmaxsd.get_name_leafdata())
                if (self.rttmonlatestjitteroperowminds.is_set or self.rttmonlatestjitteroperowminds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowminds.get_name_leafdata())
                if (self.rttmonlatestjitteroperowminsd.is_set or self.rttmonlatestjitteroperowminsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowminsd.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsum2ds.is_set or self.rttmonlatestjitteroperowsum2ds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsum2ds.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsum2dshigh.is_set or self.rttmonlatestjitteroperowsum2dshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsum2dshigh.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsum2sd.is_set or self.rttmonlatestjitteroperowsum2sd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsum2sd.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsum2sdhigh.is_set or self.rttmonlatestjitteroperowsum2sdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsum2sdhigh.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsumds.is_set or self.rttmonlatestjitteroperowsumds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsumds.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsumdshigh.is_set or self.rttmonlatestjitteroperowsumdshigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsumdshigh.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsumsd.is_set or self.rttmonlatestjitteroperowsumsd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsumsd.get_name_leafdata())
                if (self.rttmonlatestjitteroperowsumsdhigh.is_set or self.rttmonlatestjitteroperowsumsdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperowsumsdhigh.get_name_leafdata())
                if (self.rttmonlatestjitteroperpacketlatearrival.is_set or self.rttmonlatestjitteroperpacketlatearrival.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperpacketlatearrival.get_name_leafdata())
                if (self.rttmonlatestjitteroperpacketlossds.is_set or self.rttmonlatestjitteroperpacketlossds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperpacketlossds.get_name_leafdata())
                if (self.rttmonlatestjitteroperpacketlosssd.is_set or self.rttmonlatestjitteroperpacketlosssd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperpacketlosssd.get_name_leafdata())
                if (self.rttmonlatestjitteroperpacketmia.is_set or self.rttmonlatestjitteroperpacketmia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperpacketmia.get_name_leafdata())
                if (self.rttmonlatestjitteroperpacketoutofsequence.is_set or self.rttmonlatestjitteroperpacketoutofsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperpacketoutofsequence.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttmax.is_set or self.rttmonlatestjitteroperrttmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttmax.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttmin.is_set or self.rttmonlatestjitteroperrttmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttmin.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttsum.is_set or self.rttmonlatestjitteroperrttsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttsum.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttsum2.is_set or self.rttmonlatestjitteroperrttsum2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttsum2.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttsum2high.is_set or self.rttmonlatestjitteroperrttsum2high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttsum2high.get_name_leafdata())
                if (self.rttmonlatestjitteroperrttsumhigh.is_set or self.rttmonlatestjitteroperrttsumhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperrttsumhigh.get_name_leafdata())
                if (self.rttmonlatestjitteropersense.is_set or self.rttmonlatestjitteropersense.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersense.get_name_leafdata())
                if (self.rttmonlatestjitteropersum2negativesds.is_set or self.rttmonlatestjitteropersum2negativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersum2negativesds.get_name_leafdata())
                if (self.rttmonlatestjitteropersum2negativessd.is_set or self.rttmonlatestjitteropersum2negativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersum2negativessd.get_name_leafdata())
                if (self.rttmonlatestjitteropersum2positivesds.is_set or self.rttmonlatestjitteropersum2positivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersum2positivesds.get_name_leafdata())
                if (self.rttmonlatestjitteropersum2positivessd.is_set or self.rttmonlatestjitteropersum2positivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersum2positivessd.get_name_leafdata())
                if (self.rttmonlatestjitteropersumofnegativesds.is_set or self.rttmonlatestjitteropersumofnegativesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersumofnegativesds.get_name_leafdata())
                if (self.rttmonlatestjitteropersumofnegativessd.is_set or self.rttmonlatestjitteropersumofnegativessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersumofnegativessd.get_name_leafdata())
                if (self.rttmonlatestjitteropersumofpositivesds.is_set or self.rttmonlatestjitteropersumofpositivesds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersumofpositivesds.get_name_leafdata())
                if (self.rttmonlatestjitteropersumofpositivessd.is_set or self.rttmonlatestjitteropersumofpositivessd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteropersumofpositivessd.get_name_leafdata())
                if (self.rttmonlatestjitteroperunsyncrts.is_set or self.rttmonlatestjitteroperunsyncrts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rttmonlatestjitteroperunsyncrts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rttMonCtrlAdminIndex" or name == "rttMonLatestJitterErrorSenseDescription" or name == "rttMonLatestJitterOperAvgDSJ" or name == "rttMonLatestJitterOperAvgJitter" or name == "rttMonLatestJitterOperAvgSDJ" or name == "rttMonLatestJitterOperIAJIn" or name == "rttMonLatestJitterOperIAJOut" or name == "rttMonLatestJitterOperICPIF" or name == "rttMonLatestJitterOperMaxOfNegativesDS" or name == "rttMonLatestJitterOperMaxOfNegativesSD" or name == "rttMonLatestJitterOperMaxOfPositivesDS" or name == "rttMonLatestJitterOperMaxOfPositivesSD" or name == "rttMonLatestJitterOperMinOfNegativesDS" or name == "rttMonLatestJitterOperMinOfNegativesSD" or name == "rttMonLatestJitterOperMinOfPositivesDS" or name == "rttMonLatestJitterOperMinOfPositivesSD" or name == "rttMonLatestJitterOperMOS" or name == "rttMonLatestJitterOperNTPState" or name == "rttMonLatestJitterOperNumOfNegativesDS" or name == "rttMonLatestJitterOperNumOfNegativesSD" or name == "rttMonLatestJitterOperNumOfOW" or name == "rttMonLatestJitterOperNumOfPositivesDS" or name == "rttMonLatestJitterOperNumOfPositivesSD" or name == "rttMonLatestJitterOperNumOfRTT" or name == "rttMonLatestJitterOperOWAvgDS" or name == "rttMonLatestJitterOperOWAvgSD" or name == "rttMonLatestJitterOperOWMaxDS" or name == "rttMonLatestJitterOperOWMaxSD" or name == "rttMonLatestJitterOperOWMinDS" or name == "rttMonLatestJitterOperOWMinSD" or name == "rttMonLatestJitterOperOWSum2DS" or name == "rttMonLatestJitterOperOWSum2DSHigh" or name == "rttMonLatestJitterOperOWSum2SD" or name == "rttMonLatestJitterOperOWSum2SDHigh" or name == "rttMonLatestJitterOperOWSumDS" or name == "rttMonLatestJitterOperOWSumDSHigh" or name == "rttMonLatestJitterOperOWSumSD" or name == "rttMonLatestJitterOperOWSumSDHigh" or name == "rttMonLatestJitterOperPacketLateArrival" or name == "rttMonLatestJitterOperPacketLossDS" or name == "rttMonLatestJitterOperPacketLossSD" or name == "rttMonLatestJitterOperPacketMIA" or name == "rttMonLatestJitterOperPacketOutOfSequence" or name == "rttMonLatestJitterOperRTTMax" or name == "rttMonLatestJitterOperRTTMin" or name == "rttMonLatestJitterOperRTTSum" or name == "rttMonLatestJitterOperRTTSum2" or name == "rttMonLatestJitterOperRTTSum2High" or name == "rttMonLatestJitterOperRTTSumHigh" or name == "rttMonLatestJitterOperSense" or name == "rttMonLatestJitterOperSum2NegativesDS" or name == "rttMonLatestJitterOperSum2NegativesSD" or name == "rttMonLatestJitterOperSum2PositivesDS" or name == "rttMonLatestJitterOperSum2PositivesSD" or name == "rttMonLatestJitterOperSumOfNegativesDS" or name == "rttMonLatestJitterOperSumOfNegativesSD" or name == "rttMonLatestJitterOperSumOfPositivesDS" or name == "rttMonLatestJitterOperSumOfPositivesSD" or name == "rttMonLatestJitterOperUnSyncRTs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rttMonCtrlAdminIndex"):
                    self.rttmonctrladminindex = value
                    self.rttmonctrladminindex.value_namespace = name_space
                    self.rttmonctrladminindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterErrorSenseDescription"):
                    self.rttmonlatestjittererrorsensedescription = value
                    self.rttmonlatestjittererrorsensedescription.value_namespace = name_space
                    self.rttmonlatestjittererrorsensedescription.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperAvgDSJ"):
                    self.rttmonlatestjitteroperavgdsj = value
                    self.rttmonlatestjitteroperavgdsj.value_namespace = name_space
                    self.rttmonlatestjitteroperavgdsj.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperAvgJitter"):
                    self.rttmonlatestjitteroperavgjitter = value
                    self.rttmonlatestjitteroperavgjitter.value_namespace = name_space
                    self.rttmonlatestjitteroperavgjitter.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperAvgSDJ"):
                    self.rttmonlatestjitteroperavgsdj = value
                    self.rttmonlatestjitteroperavgsdj.value_namespace = name_space
                    self.rttmonlatestjitteroperavgsdj.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperIAJIn"):
                    self.rttmonlatestjitteroperiajin = value
                    self.rttmonlatestjitteroperiajin.value_namespace = name_space
                    self.rttmonlatestjitteroperiajin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperIAJOut"):
                    self.rttmonlatestjitteroperiajout = value
                    self.rttmonlatestjitteroperiajout.value_namespace = name_space
                    self.rttmonlatestjitteroperiajout.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperICPIF"):
                    self.rttmonlatestjitteropericpif = value
                    self.rttmonlatestjitteropericpif.value_namespace = name_space
                    self.rttmonlatestjitteropericpif.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMaxOfNegativesDS"):
                    self.rttmonlatestjitteropermaxofnegativesds = value
                    self.rttmonlatestjitteropermaxofnegativesds.value_namespace = name_space
                    self.rttmonlatestjitteropermaxofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMaxOfNegativesSD"):
                    self.rttmonlatestjitteropermaxofnegativessd = value
                    self.rttmonlatestjitteropermaxofnegativessd.value_namespace = name_space
                    self.rttmonlatestjitteropermaxofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMaxOfPositivesDS"):
                    self.rttmonlatestjitteropermaxofpositivesds = value
                    self.rttmonlatestjitteropermaxofpositivesds.value_namespace = name_space
                    self.rttmonlatestjitteropermaxofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMaxOfPositivesSD"):
                    self.rttmonlatestjitteropermaxofpositivessd = value
                    self.rttmonlatestjitteropermaxofpositivessd.value_namespace = name_space
                    self.rttmonlatestjitteropermaxofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMinOfNegativesDS"):
                    self.rttmonlatestjitteroperminofnegativesds = value
                    self.rttmonlatestjitteroperminofnegativesds.value_namespace = name_space
                    self.rttmonlatestjitteroperminofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMinOfNegativesSD"):
                    self.rttmonlatestjitteroperminofnegativessd = value
                    self.rttmonlatestjitteroperminofnegativessd.value_namespace = name_space
                    self.rttmonlatestjitteroperminofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMinOfPositivesDS"):
                    self.rttmonlatestjitteroperminofpositivesds = value
                    self.rttmonlatestjitteroperminofpositivesds.value_namespace = name_space
                    self.rttmonlatestjitteroperminofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMinOfPositivesSD"):
                    self.rttmonlatestjitteroperminofpositivessd = value
                    self.rttmonlatestjitteroperminofpositivessd.value_namespace = name_space
                    self.rttmonlatestjitteroperminofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperMOS"):
                    self.rttmonlatestjitteropermos = value
                    self.rttmonlatestjitteropermos.value_namespace = name_space
                    self.rttmonlatestjitteropermos.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNTPState"):
                    self.rttmonlatestjitteroperntpstate = value
                    self.rttmonlatestjitteroperntpstate.value_namespace = name_space
                    self.rttmonlatestjitteroperntpstate.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfNegativesDS"):
                    self.rttmonlatestjitteropernumofnegativesds = value
                    self.rttmonlatestjitteropernumofnegativesds.value_namespace = name_space
                    self.rttmonlatestjitteropernumofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfNegativesSD"):
                    self.rttmonlatestjitteropernumofnegativessd = value
                    self.rttmonlatestjitteropernumofnegativessd.value_namespace = name_space
                    self.rttmonlatestjitteropernumofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfOW"):
                    self.rttmonlatestjitteropernumofow = value
                    self.rttmonlatestjitteropernumofow.value_namespace = name_space
                    self.rttmonlatestjitteropernumofow.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfPositivesDS"):
                    self.rttmonlatestjitteropernumofpositivesds = value
                    self.rttmonlatestjitteropernumofpositivesds.value_namespace = name_space
                    self.rttmonlatestjitteropernumofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfPositivesSD"):
                    self.rttmonlatestjitteropernumofpositivessd = value
                    self.rttmonlatestjitteropernumofpositivessd.value_namespace = name_space
                    self.rttmonlatestjitteropernumofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperNumOfRTT"):
                    self.rttmonlatestjitteropernumofrtt = value
                    self.rttmonlatestjitteropernumofrtt.value_namespace = name_space
                    self.rttmonlatestjitteropernumofrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWAvgDS"):
                    self.rttmonlatestjitteroperowavgds = value
                    self.rttmonlatestjitteroperowavgds.value_namespace = name_space
                    self.rttmonlatestjitteroperowavgds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWAvgSD"):
                    self.rttmonlatestjitteroperowavgsd = value
                    self.rttmonlatestjitteroperowavgsd.value_namespace = name_space
                    self.rttmonlatestjitteroperowavgsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWMaxDS"):
                    self.rttmonlatestjitteroperowmaxds = value
                    self.rttmonlatestjitteroperowmaxds.value_namespace = name_space
                    self.rttmonlatestjitteroperowmaxds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWMaxSD"):
                    self.rttmonlatestjitteroperowmaxsd = value
                    self.rttmonlatestjitteroperowmaxsd.value_namespace = name_space
                    self.rttmonlatestjitteroperowmaxsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWMinDS"):
                    self.rttmonlatestjitteroperowminds = value
                    self.rttmonlatestjitteroperowminds.value_namespace = name_space
                    self.rttmonlatestjitteroperowminds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWMinSD"):
                    self.rttmonlatestjitteroperowminsd = value
                    self.rttmonlatestjitteroperowminsd.value_namespace = name_space
                    self.rttmonlatestjitteroperowminsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSum2DS"):
                    self.rttmonlatestjitteroperowsum2ds = value
                    self.rttmonlatestjitteroperowsum2ds.value_namespace = name_space
                    self.rttmonlatestjitteroperowsum2ds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSum2DSHigh"):
                    self.rttmonlatestjitteroperowsum2dshigh = value
                    self.rttmonlatestjitteroperowsum2dshigh.value_namespace = name_space
                    self.rttmonlatestjitteroperowsum2dshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSum2SD"):
                    self.rttmonlatestjitteroperowsum2sd = value
                    self.rttmonlatestjitteroperowsum2sd.value_namespace = name_space
                    self.rttmonlatestjitteroperowsum2sd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSum2SDHigh"):
                    self.rttmonlatestjitteroperowsum2sdhigh = value
                    self.rttmonlatestjitteroperowsum2sdhigh.value_namespace = name_space
                    self.rttmonlatestjitteroperowsum2sdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSumDS"):
                    self.rttmonlatestjitteroperowsumds = value
                    self.rttmonlatestjitteroperowsumds.value_namespace = name_space
                    self.rttmonlatestjitteroperowsumds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSumDSHigh"):
                    self.rttmonlatestjitteroperowsumdshigh = value
                    self.rttmonlatestjitteroperowsumdshigh.value_namespace = name_space
                    self.rttmonlatestjitteroperowsumdshigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSumSD"):
                    self.rttmonlatestjitteroperowsumsd = value
                    self.rttmonlatestjitteroperowsumsd.value_namespace = name_space
                    self.rttmonlatestjitteroperowsumsd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperOWSumSDHigh"):
                    self.rttmonlatestjitteroperowsumsdhigh = value
                    self.rttmonlatestjitteroperowsumsdhigh.value_namespace = name_space
                    self.rttmonlatestjitteroperowsumsdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperPacketLateArrival"):
                    self.rttmonlatestjitteroperpacketlatearrival = value
                    self.rttmonlatestjitteroperpacketlatearrival.value_namespace = name_space
                    self.rttmonlatestjitteroperpacketlatearrival.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperPacketLossDS"):
                    self.rttmonlatestjitteroperpacketlossds = value
                    self.rttmonlatestjitteroperpacketlossds.value_namespace = name_space
                    self.rttmonlatestjitteroperpacketlossds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperPacketLossSD"):
                    self.rttmonlatestjitteroperpacketlosssd = value
                    self.rttmonlatestjitteroperpacketlosssd.value_namespace = name_space
                    self.rttmonlatestjitteroperpacketlosssd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperPacketMIA"):
                    self.rttmonlatestjitteroperpacketmia = value
                    self.rttmonlatestjitteroperpacketmia.value_namespace = name_space
                    self.rttmonlatestjitteroperpacketmia.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperPacketOutOfSequence"):
                    self.rttmonlatestjitteroperpacketoutofsequence = value
                    self.rttmonlatestjitteroperpacketoutofsequence.value_namespace = name_space
                    self.rttmonlatestjitteroperpacketoutofsequence.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTMax"):
                    self.rttmonlatestjitteroperrttmax = value
                    self.rttmonlatestjitteroperrttmax.value_namespace = name_space
                    self.rttmonlatestjitteroperrttmax.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTMin"):
                    self.rttmonlatestjitteroperrttmin = value
                    self.rttmonlatestjitteroperrttmin.value_namespace = name_space
                    self.rttmonlatestjitteroperrttmin.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTSum"):
                    self.rttmonlatestjitteroperrttsum = value
                    self.rttmonlatestjitteroperrttsum.value_namespace = name_space
                    self.rttmonlatestjitteroperrttsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTSum2"):
                    self.rttmonlatestjitteroperrttsum2 = value
                    self.rttmonlatestjitteroperrttsum2.value_namespace = name_space
                    self.rttmonlatestjitteroperrttsum2.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTSum2High"):
                    self.rttmonlatestjitteroperrttsum2high = value
                    self.rttmonlatestjitteroperrttsum2high.value_namespace = name_space
                    self.rttmonlatestjitteroperrttsum2high.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperRTTSumHigh"):
                    self.rttmonlatestjitteroperrttsumhigh = value
                    self.rttmonlatestjitteroperrttsumhigh.value_namespace = name_space
                    self.rttmonlatestjitteroperrttsumhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSense"):
                    self.rttmonlatestjitteropersense = value
                    self.rttmonlatestjitteropersense.value_namespace = name_space
                    self.rttmonlatestjitteropersense.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSum2NegativesDS"):
                    self.rttmonlatestjitteropersum2negativesds = value
                    self.rttmonlatestjitteropersum2negativesds.value_namespace = name_space
                    self.rttmonlatestjitteropersum2negativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSum2NegativesSD"):
                    self.rttmonlatestjitteropersum2negativessd = value
                    self.rttmonlatestjitteropersum2negativessd.value_namespace = name_space
                    self.rttmonlatestjitteropersum2negativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSum2PositivesDS"):
                    self.rttmonlatestjitteropersum2positivesds = value
                    self.rttmonlatestjitteropersum2positivesds.value_namespace = name_space
                    self.rttmonlatestjitteropersum2positivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSum2PositivesSD"):
                    self.rttmonlatestjitteropersum2positivessd = value
                    self.rttmonlatestjitteropersum2positivessd.value_namespace = name_space
                    self.rttmonlatestjitteropersum2positivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSumOfNegativesDS"):
                    self.rttmonlatestjitteropersumofnegativesds = value
                    self.rttmonlatestjitteropersumofnegativesds.value_namespace = name_space
                    self.rttmonlatestjitteropersumofnegativesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSumOfNegativesSD"):
                    self.rttmonlatestjitteropersumofnegativessd = value
                    self.rttmonlatestjitteropersumofnegativessd.value_namespace = name_space
                    self.rttmonlatestjitteropersumofnegativessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSumOfPositivesDS"):
                    self.rttmonlatestjitteropersumofpositivesds = value
                    self.rttmonlatestjitteropersumofpositivesds.value_namespace = name_space
                    self.rttmonlatestjitteropersumofpositivesds.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperSumOfPositivesSD"):
                    self.rttmonlatestjitteropersumofpositivessd = value
                    self.rttmonlatestjitteropersumofpositivessd.value_namespace = name_space
                    self.rttmonlatestjitteropersumofpositivessd.value_namespace_prefix = name_space_prefix
                if(value_path == "rttMonLatestJitterOperUnSyncRTs"):
                    self.rttmonlatestjitteroperunsyncrts = value
                    self.rttmonlatestjitteroperunsyncrts.value_namespace = name_space
                    self.rttmonlatestjitteroperunsyncrts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rttmonlatestjitteroperentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rttmonlatestjitteroperentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rttMonLatestJitterOperTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rttMonLatestJitterOperEntry"):
                for c in self.rttmonlatestjitteroperentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRttmonMib.Rttmonlatestjitteropertable.Rttmonlatestjitteroperentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rttmonlatestjitteroperentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rttMonLatestJitterOperEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.rttmonappl is not None and self.rttmonappl.has_data()) or
            (self.rttmonapplauthtable is not None and self.rttmonapplauthtable.has_data()) or
            (self.rttmonapplpreconfigedtable is not None and self.rttmonapplpreconfigedtable.has_data()) or
            (self.rttmonapplsupportedprotocolstable is not None and self.rttmonapplsupportedprotocolstable.has_data()) or
            (self.rttmonapplsupportedrtttypestable is not None and self.rttmonapplsupportedrtttypestable.has_data()) or
            (self.rttmonctrladmintable is not None and self.rttmonctrladmintable.has_data()) or
            (self.rttmonechoadmintable is not None and self.rttmonechoadmintable.has_data()) or
            (self.rttmonechopathadmintable is not None and self.rttmonechopathadmintable.has_data()) or
            (self.rttmonfileioadmintable is not None and self.rttmonfileioadmintable.has_data()) or
            (self.rttmongeneratedopertable is not None and self.rttmongeneratedopertable.has_data()) or
            (self.rttmongrpscheduleadmintable is not None and self.rttmongrpscheduleadmintable.has_data()) or
            (self.rttmonhistorycollectiontable is not None and self.rttmonhistorycollectiontable.has_data()) or
            (self.rttmonhttpstatstable is not None and self.rttmonhttpstatstable.has_data()) or
            (self.rttmonjitterstatstable is not None and self.rttmonjitterstatstable.has_data()) or
            (self.rttmonlatesthttpopertable is not None and self.rttmonlatesthttpopertable.has_data()) or
            (self.rttmonlatestjitteropertable is not None and self.rttmonlatestjitteropertable.has_data()) or
            (self.rttmonlpdgrpstatstable is not None and self.rttmonlpdgrpstatstable.has_data()) or
            (self.rttmonreacttable is not None and self.rttmonreacttable.has_data()) or
            (self.rttmonreacttriggeradmintable is not None and self.rttmonreacttriggeradmintable.has_data()) or
            (self.rttmonscriptadmintable is not None and self.rttmonscriptadmintable.has_data()) or
            (self.rttmonstatscapturetable is not None and self.rttmonstatscapturetable.has_data()) or
            (self.rttmonstatscollecttable is not None and self.rttmonstatscollecttable.has_data()) or
            (self.rttmonstatstotalstable is not None and self.rttmonstatstotalstable.has_data()) or
            (self.rttmplsvpnmonctrltable is not None and self.rttmplsvpnmonctrltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.rttmonappl is not None and self.rttmonappl.has_operation()) or
            (self.rttmonapplauthtable is not None and self.rttmonapplauthtable.has_operation()) or
            (self.rttmonapplpreconfigedtable is not None and self.rttmonapplpreconfigedtable.has_operation()) or
            (self.rttmonapplsupportedprotocolstable is not None and self.rttmonapplsupportedprotocolstable.has_operation()) or
            (self.rttmonapplsupportedrtttypestable is not None and self.rttmonapplsupportedrtttypestable.has_operation()) or
            (self.rttmonctrladmintable is not None and self.rttmonctrladmintable.has_operation()) or
            (self.rttmonechoadmintable is not None and self.rttmonechoadmintable.has_operation()) or
            (self.rttmonechopathadmintable is not None and self.rttmonechopathadmintable.has_operation()) or
            (self.rttmonfileioadmintable is not None and self.rttmonfileioadmintable.has_operation()) or
            (self.rttmongeneratedopertable is not None and self.rttmongeneratedopertable.has_operation()) or
            (self.rttmongrpscheduleadmintable is not None and self.rttmongrpscheduleadmintable.has_operation()) or
            (self.rttmonhistorycollectiontable is not None and self.rttmonhistorycollectiontable.has_operation()) or
            (self.rttmonhttpstatstable is not None and self.rttmonhttpstatstable.has_operation()) or
            (self.rttmonjitterstatstable is not None and self.rttmonjitterstatstable.has_operation()) or
            (self.rttmonlatesthttpopertable is not None and self.rttmonlatesthttpopertable.has_operation()) or
            (self.rttmonlatestjitteropertable is not None and self.rttmonlatestjitteropertable.has_operation()) or
            (self.rttmonlpdgrpstatstable is not None and self.rttmonlpdgrpstatstable.has_operation()) or
            (self.rttmonreacttable is not None and self.rttmonreacttable.has_operation()) or
            (self.rttmonreacttriggeradmintable is not None and self.rttmonreacttriggeradmintable.has_operation()) or
            (self.rttmonscriptadmintable is not None and self.rttmonscriptadmintable.has_operation()) or
            (self.rttmonstatscapturetable is not None and self.rttmonstatscapturetable.has_operation()) or
            (self.rttmonstatscollecttable is not None and self.rttmonstatscollecttable.has_operation()) or
            (self.rttmonstatstotalstable is not None and self.rttmonstatstotalstable.has_operation()) or
            (self.rttmplsvpnmonctrltable is not None and self.rttmplsvpnmonctrltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-RTTMON-MIB:CISCO-RTTMON-MIB" + path_buffer

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

        if (child_yang_name == "rttMonAppl"):
            if (self.rttmonappl is None):
                self.rttmonappl = CiscoRttmonMib.Rttmonappl()
                self.rttmonappl.parent = self
                self._children_name_map["rttmonappl"] = "rttMonAppl"
            return self.rttmonappl

        if (child_yang_name == "rttMonApplAuthTable"):
            if (self.rttmonapplauthtable is None):
                self.rttmonapplauthtable = CiscoRttmonMib.Rttmonapplauthtable()
                self.rttmonapplauthtable.parent = self
                self._children_name_map["rttmonapplauthtable"] = "rttMonApplAuthTable"
            return self.rttmonapplauthtable

        if (child_yang_name == "rttMonApplPreConfigedTable"):
            if (self.rttmonapplpreconfigedtable is None):
                self.rttmonapplpreconfigedtable = CiscoRttmonMib.Rttmonapplpreconfigedtable()
                self.rttmonapplpreconfigedtable.parent = self
                self._children_name_map["rttmonapplpreconfigedtable"] = "rttMonApplPreConfigedTable"
            return self.rttmonapplpreconfigedtable

        if (child_yang_name == "rttMonApplSupportedProtocolsTable"):
            if (self.rttmonapplsupportedprotocolstable is None):
                self.rttmonapplsupportedprotocolstable = CiscoRttmonMib.Rttmonapplsupportedprotocolstable()
                self.rttmonapplsupportedprotocolstable.parent = self
                self._children_name_map["rttmonapplsupportedprotocolstable"] = "rttMonApplSupportedProtocolsTable"
            return self.rttmonapplsupportedprotocolstable

        if (child_yang_name == "rttMonApplSupportedRttTypesTable"):
            if (self.rttmonapplsupportedrtttypestable is None):
                self.rttmonapplsupportedrtttypestable = CiscoRttmonMib.Rttmonapplsupportedrtttypestable()
                self.rttmonapplsupportedrtttypestable.parent = self
                self._children_name_map["rttmonapplsupportedrtttypestable"] = "rttMonApplSupportedRttTypesTable"
            return self.rttmonapplsupportedrtttypestable

        if (child_yang_name == "rttMonCtrlAdminTable"):
            if (self.rttmonctrladmintable is None):
                self.rttmonctrladmintable = CiscoRttmonMib.Rttmonctrladmintable()
                self.rttmonctrladmintable.parent = self
                self._children_name_map["rttmonctrladmintable"] = "rttMonCtrlAdminTable"
            return self.rttmonctrladmintable

        if (child_yang_name == "rttMonEchoAdminTable"):
            if (self.rttmonechoadmintable is None):
                self.rttmonechoadmintable = CiscoRttmonMib.Rttmonechoadmintable()
                self.rttmonechoadmintable.parent = self
                self._children_name_map["rttmonechoadmintable"] = "rttMonEchoAdminTable"
            return self.rttmonechoadmintable

        if (child_yang_name == "rttMonEchoPathAdminTable"):
            if (self.rttmonechopathadmintable is None):
                self.rttmonechopathadmintable = CiscoRttmonMib.Rttmonechopathadmintable()
                self.rttmonechopathadmintable.parent = self
                self._children_name_map["rttmonechopathadmintable"] = "rttMonEchoPathAdminTable"
            return self.rttmonechopathadmintable

        if (child_yang_name == "rttMonFileIOAdminTable"):
            if (self.rttmonfileioadmintable is None):
                self.rttmonfileioadmintable = CiscoRttmonMib.Rttmonfileioadmintable()
                self.rttmonfileioadmintable.parent = self
                self._children_name_map["rttmonfileioadmintable"] = "rttMonFileIOAdminTable"
            return self.rttmonfileioadmintable

        if (child_yang_name == "rttMonGeneratedOperTable"):
            if (self.rttmongeneratedopertable is None):
                self.rttmongeneratedopertable = CiscoRttmonMib.Rttmongeneratedopertable()
                self.rttmongeneratedopertable.parent = self
                self._children_name_map["rttmongeneratedopertable"] = "rttMonGeneratedOperTable"
            return self.rttmongeneratedopertable

        if (child_yang_name == "rttMonGrpScheduleAdminTable"):
            if (self.rttmongrpscheduleadmintable is None):
                self.rttmongrpscheduleadmintable = CiscoRttmonMib.Rttmongrpscheduleadmintable()
                self.rttmongrpscheduleadmintable.parent = self
                self._children_name_map["rttmongrpscheduleadmintable"] = "rttMonGrpScheduleAdminTable"
            return self.rttmongrpscheduleadmintable

        if (child_yang_name == "rttMonHistoryCollectionTable"):
            if (self.rttmonhistorycollectiontable is None):
                self.rttmonhistorycollectiontable = CiscoRttmonMib.Rttmonhistorycollectiontable()
                self.rttmonhistorycollectiontable.parent = self
                self._children_name_map["rttmonhistorycollectiontable"] = "rttMonHistoryCollectionTable"
            return self.rttmonhistorycollectiontable

        if (child_yang_name == "rttMonHTTPStatsTable"):
            if (self.rttmonhttpstatstable is None):
                self.rttmonhttpstatstable = CiscoRttmonMib.Rttmonhttpstatstable()
                self.rttmonhttpstatstable.parent = self
                self._children_name_map["rttmonhttpstatstable"] = "rttMonHTTPStatsTable"
            return self.rttmonhttpstatstable

        if (child_yang_name == "rttMonJitterStatsTable"):
            if (self.rttmonjitterstatstable is None):
                self.rttmonjitterstatstable = CiscoRttmonMib.Rttmonjitterstatstable()
                self.rttmonjitterstatstable.parent = self
                self._children_name_map["rttmonjitterstatstable"] = "rttMonJitterStatsTable"
            return self.rttmonjitterstatstable

        if (child_yang_name == "rttMonLatestHTTPOperTable"):
            if (self.rttmonlatesthttpopertable is None):
                self.rttmonlatesthttpopertable = CiscoRttmonMib.Rttmonlatesthttpopertable()
                self.rttmonlatesthttpopertable.parent = self
                self._children_name_map["rttmonlatesthttpopertable"] = "rttMonLatestHTTPOperTable"
            return self.rttmonlatesthttpopertable

        if (child_yang_name == "rttMonLatestJitterOperTable"):
            if (self.rttmonlatestjitteropertable is None):
                self.rttmonlatestjitteropertable = CiscoRttmonMib.Rttmonlatestjitteropertable()
                self.rttmonlatestjitteropertable.parent = self
                self._children_name_map["rttmonlatestjitteropertable"] = "rttMonLatestJitterOperTable"
            return self.rttmonlatestjitteropertable

        if (child_yang_name == "rttMonLpdGrpStatsTable"):
            if (self.rttmonlpdgrpstatstable is None):
                self.rttmonlpdgrpstatstable = CiscoRttmonMib.Rttmonlpdgrpstatstable()
                self.rttmonlpdgrpstatstable.parent = self
                self._children_name_map["rttmonlpdgrpstatstable"] = "rttMonLpdGrpStatsTable"
            return self.rttmonlpdgrpstatstable

        if (child_yang_name == "rttMonReactTable"):
            if (self.rttmonreacttable is None):
                self.rttmonreacttable = CiscoRttmonMib.Rttmonreacttable()
                self.rttmonreacttable.parent = self
                self._children_name_map["rttmonreacttable"] = "rttMonReactTable"
            return self.rttmonreacttable

        if (child_yang_name == "rttMonReactTriggerAdminTable"):
            if (self.rttmonreacttriggeradmintable is None):
                self.rttmonreacttriggeradmintable = CiscoRttmonMib.Rttmonreacttriggeradmintable()
                self.rttmonreacttriggeradmintable.parent = self
                self._children_name_map["rttmonreacttriggeradmintable"] = "rttMonReactTriggerAdminTable"
            return self.rttmonreacttriggeradmintable

        if (child_yang_name == "rttMonScriptAdminTable"):
            if (self.rttmonscriptadmintable is None):
                self.rttmonscriptadmintable = CiscoRttmonMib.Rttmonscriptadmintable()
                self.rttmonscriptadmintable.parent = self
                self._children_name_map["rttmonscriptadmintable"] = "rttMonScriptAdminTable"
            return self.rttmonscriptadmintable

        if (child_yang_name == "rttMonStatsCaptureTable"):
            if (self.rttmonstatscapturetable is None):
                self.rttmonstatscapturetable = CiscoRttmonMib.Rttmonstatscapturetable()
                self.rttmonstatscapturetable.parent = self
                self._children_name_map["rttmonstatscapturetable"] = "rttMonStatsCaptureTable"
            return self.rttmonstatscapturetable

        if (child_yang_name == "rttMonStatsCollectTable"):
            if (self.rttmonstatscollecttable is None):
                self.rttmonstatscollecttable = CiscoRttmonMib.Rttmonstatscollecttable()
                self.rttmonstatscollecttable.parent = self
                self._children_name_map["rttmonstatscollecttable"] = "rttMonStatsCollectTable"
            return self.rttmonstatscollecttable

        if (child_yang_name == "rttMonStatsTotalsTable"):
            if (self.rttmonstatstotalstable is None):
                self.rttmonstatstotalstable = CiscoRttmonMib.Rttmonstatstotalstable()
                self.rttmonstatstotalstable.parent = self
                self._children_name_map["rttmonstatstotalstable"] = "rttMonStatsTotalsTable"
            return self.rttmonstatstotalstable

        if (child_yang_name == "rttMplsVpnMonCtrlTable"):
            if (self.rttmplsvpnmonctrltable is None):
                self.rttmplsvpnmonctrltable = CiscoRttmonMib.Rttmplsvpnmonctrltable()
                self.rttmplsvpnmonctrltable.parent = self
                self._children_name_map["rttmplsvpnmonctrltable"] = "rttMplsVpnMonCtrlTable"
            return self.rttmplsvpnmonctrltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "rttMonAppl" or name == "rttMonApplAuthTable" or name == "rttMonApplPreConfigedTable" or name == "rttMonApplSupportedProtocolsTable" or name == "rttMonApplSupportedRttTypesTable" or name == "rttMonCtrlAdminTable" or name == "rttMonEchoAdminTable" or name == "rttMonEchoPathAdminTable" or name == "rttMonFileIOAdminTable" or name == "rttMonGeneratedOperTable" or name == "rttMonGrpScheduleAdminTable" or name == "rttMonHistoryCollectionTable" or name == "rttMonHTTPStatsTable" or name == "rttMonJitterStatsTable" or name == "rttMonLatestHTTPOperTable" or name == "rttMonLatestJitterOperTable" or name == "rttMonLpdGrpStatsTable" or name == "rttMonReactTable" or name == "rttMonReactTriggerAdminTable" or name == "rttMonScriptAdminTable" or name == "rttMonStatsCaptureTable" or name == "rttMonStatsCollectTable" or name == "rttMonStatsTotalsTable" or name == "rttMplsVpnMonCtrlTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoRttmonMib()
        return self._top_entity

