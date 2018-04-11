""" CISCO_IETF_PW_MIB 

This MIB contains managed object definitions for Pseudo 
Wire operation as in\: Pate, P., et al, <draft\-ietf\-pwe3\- 
framework>, Xiao, X., et al, <draft\-ietf\-pwe3\- 
requirements>, Martini, L., et al, <draft\-martini\- 
l2circuit\-trans\-mpls>, and Martini, L., et al, 
<draft\-martini\-l2circuit\-encap\-mpls>. 

The indexes for this MIB are also used to index the PSN\- 
specific tables and the VC\-specific tables. The VC Type 
dictates which VC\-specific MIB to use. For example, a  
'cep' VC Type requires the use the configuration and status  
tables within the CEP\-MIB. 

This MIB enable the use of any underlying packet switched  
network (PSN). Specific tables for the MPLS PSN is 
currently defined in a separate CISCO\-IETF\-PW\-MPLS\-MIB. 
Tables to support other PSNs (IP, L2TP for example) will 
be added to this MIB in future revisions. 

At the time of publication of this version, there are no  
PWE3 WG documents for all features and objects in this MIB, 
and the MIB is therefore subject to change based on the WG  
progress.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIETFPWMIB(Entity):
    """
    
    
    .. attribute:: cpwvcobjects
    
    	
    	**type**\:  :py:class:`Cpwvcobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcobjects>`
    
    .. attribute:: cpwvctable
    
    	This table specifies information for connecting various  emulated services to various tunnel type
    	**type**\:  :py:class:`Cpwvctable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable>`
    
    .. attribute:: cpwvcperfcurrenttable
    
    	This table provides per\-VC performance information for the   current interval
    	**type**\:  :py:class:`Cpwvcperfcurrenttable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperfcurrenttable>`
    
    .. attribute:: cpwvcperfintervaltable
    
    	This table provides per\-VC performance information for   each interval
    	**type**\:  :py:class:`Cpwvcperfintervaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperfintervaltable>`
    
    .. attribute:: cpwvcperftotaltable
    
    	This table provides per\-VC Performance information from VC   start time
    	**type**\:  :py:class:`Cpwvcperftotaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperftotaltable>`
    
    .. attribute:: cpwvcidmappingtable
    
    	This table provides reverse mapping of the existing VCs   based on vc type and VC ID ordering. This table is   typically useful for EMS ordered query of existing VCs
    	**type**\:  :py:class:`Cpwvcidmappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcidmappingtable>`
    
    .. attribute:: cpwvcpeermappingtable
    
    	This table provides reverse mapping of the existing VCs   based on vc type and VC ID ordering. This table is   typically useful for EMS ordered query of existing VCs
    	**type**\:  :py:class:`Cpwvcpeermappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcpeermappingtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-MIB'
    _revision = '2004-03-17'

    def __init__(self):
        super(CISCOIETFPWMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cpwVcObjects", ("cpwvcobjects", CISCOIETFPWMIB.Cpwvcobjects)), ("cpwVcTable", ("cpwvctable", CISCOIETFPWMIB.Cpwvctable)), ("cpwVcPerfCurrentTable", ("cpwvcperfcurrenttable", CISCOIETFPWMIB.Cpwvcperfcurrenttable)), ("cpwVcPerfIntervalTable", ("cpwvcperfintervaltable", CISCOIETFPWMIB.Cpwvcperfintervaltable)), ("cpwVcPerfTotalTable", ("cpwvcperftotaltable", CISCOIETFPWMIB.Cpwvcperftotaltable)), ("cpwVcIdMappingTable", ("cpwvcidmappingtable", CISCOIETFPWMIB.Cpwvcidmappingtable)), ("cpwVcPeerMappingTable", ("cpwvcpeermappingtable", CISCOIETFPWMIB.Cpwvcpeermappingtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpwvcobjects = CISCOIETFPWMIB.Cpwvcobjects()
        self.cpwvcobjects.parent = self
        self._children_name_map["cpwvcobjects"] = "cpwVcObjects"
        self._children_yang_names.add("cpwVcObjects")

        self.cpwvctable = CISCOIETFPWMIB.Cpwvctable()
        self.cpwvctable.parent = self
        self._children_name_map["cpwvctable"] = "cpwVcTable"
        self._children_yang_names.add("cpwVcTable")

        self.cpwvcperfcurrenttable = CISCOIETFPWMIB.Cpwvcperfcurrenttable()
        self.cpwvcperfcurrenttable.parent = self
        self._children_name_map["cpwvcperfcurrenttable"] = "cpwVcPerfCurrentTable"
        self._children_yang_names.add("cpwVcPerfCurrentTable")

        self.cpwvcperfintervaltable = CISCOIETFPWMIB.Cpwvcperfintervaltable()
        self.cpwvcperfintervaltable.parent = self
        self._children_name_map["cpwvcperfintervaltable"] = "cpwVcPerfIntervalTable"
        self._children_yang_names.add("cpwVcPerfIntervalTable")

        self.cpwvcperftotaltable = CISCOIETFPWMIB.Cpwvcperftotaltable()
        self.cpwvcperftotaltable.parent = self
        self._children_name_map["cpwvcperftotaltable"] = "cpwVcPerfTotalTable"
        self._children_yang_names.add("cpwVcPerfTotalTable")

        self.cpwvcidmappingtable = CISCOIETFPWMIB.Cpwvcidmappingtable()
        self.cpwvcidmappingtable.parent = self
        self._children_name_map["cpwvcidmappingtable"] = "cpwVcIdMappingTable"
        self._children_yang_names.add("cpwVcIdMappingTable")

        self.cpwvcpeermappingtable = CISCOIETFPWMIB.Cpwvcpeermappingtable()
        self.cpwvcpeermappingtable.parent = self
        self._children_name_map["cpwvcpeermappingtable"] = "cpwVcPeerMappingTable"
        self._children_yang_names.add("cpwVcPeerMappingTable")
        self._segment_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB"


    class Cpwvcobjects(Entity):
        """
        
        
        .. attribute:: cpwvcindexnext
        
        	This object contains an appropriate value to be used  for cpwVcIndex when creating entries in the  cpwVcTable. The value 0 indicates that no  unassigned entries are available.  To obtain the  value of cpwVcIndex for a new entry in the  cpwVcTable, the manager issues a management  protocol retrieval operation to obtain the current  value of cpwVcIndex.  After each retrieval  operation, the agent should modify the value to  reflect the next unassigned index.  After a manager  retrieves a value the agent will determine through  its local policy when this index value will be made  available for reuse
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcperftotalerrorpackets
        
        	Counter for number of error at VC level processing, for   example packets received with unknown VC label
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cpwvcupdownnotifenable
        
        	If this object is set to true(1), then it enables the emission of cpwVcUp and cpwVcDown notifications; otherwise these notifications are not emitted
        	**type**\: bool
        
        .. attribute:: cpwvcnotifrate
        
        	This object defines the maximum number of PW VC notifications that can be emitted from the device per second
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcobjects, self).__init__()

            self.yang_name = "cpwVcObjects"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpwvcindexnext', YLeaf(YType.uint32, 'cpwVcIndexNext')),
                ('cpwvcperftotalerrorpackets', YLeaf(YType.uint64, 'cpwVcPerfTotalErrorPackets')),
                ('cpwvcupdownnotifenable', YLeaf(YType.boolean, 'cpwVcUpDownNotifEnable')),
                ('cpwvcnotifrate', YLeaf(YType.uint32, 'cpwVcNotifRate')),
            ])
            self.cpwvcindexnext = None
            self.cpwvcperftotalerrorpackets = None
            self.cpwvcupdownnotifenable = None
            self.cpwvcnotifrate = None
            self._segment_path = lambda: "cpwVcObjects"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcobjects, ['cpwvcindexnext', 'cpwvcperftotalerrorpackets', 'cpwvcupdownnotifenable', 'cpwvcnotifrate'], name, value)


    class Cpwvctable(Entity):
        """
        This table specifies information for connecting various 
        emulated services to various tunnel type.
        
        .. attribute:: cpwvcentry
        
        	A row in this table represents an emulated virtual  connection (VC) across a packet network. It is indexed by  cpwVcIndex, which uniquely identifying a singular   connection. 
        	**type**\: list of  		 :py:class:`Cpwvcentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvctable, self).__init__()

            self.yang_name = "cpwVcTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcEntry", ("cpwvcentry", CISCOIETFPWMIB.Cpwvctable.Cpwvcentry))])
            self._leafs = OrderedDict()

            self.cpwvcentry = YList(self)
            self._segment_path = lambda: "cpwVcTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvctable, [], name, value)


        class Cpwvcentry(Entity):
            """
            A row in this table represents an emulated virtual 
            connection (VC) across a packet network. It is indexed by 
            cpwVcIndex, which uniquely identifying a singular  
            connection. 
            
            .. attribute:: cpwvcindex  (key)
            
            	Index for the conceptual row identifying a VC within   this PW Emulation VC table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvctype
            
            	This value indicate the service to be carried over  this VC.   Note\: the exact set of VC types is yet to be worked   out by the WG. 
            	**type**\:  :py:class:`CpwVcType <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwVcType>`
            
            .. attribute:: cpwvcowner
            
            	Set by the operator to indicate the protocol responsible   for establishing this VC. Value 'manual' is used in all  cases where no maintenance protocol (PW signaling) is used   to set\-up the VC, i.e. require configuration of entries in  the VC tables including VC labels, etc. The value   'maintenanceProtocol' is used in case of standard  signaling of the VC for the specific PSN, for example LDP  for MPLS PSN as specified in <draft\- draft\-martini\-  l2circuit\-trans\-mpls> or L2TP control protocol.   Value 'other' is used for other types of signaling
            	**type**\:  :py:class:`Cpwvcowner <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry.Cpwvcowner>`
            
            .. attribute:: cpwvcpsntype
            
            	Set by the operator to indicate the PSN type on which this   VC will be carried. Based on this object, the relevant PSN   table entries are created in the in the PSN specific MIB   modules. For example, if mpls(1) is defined, the agent   create an entry in cpwVcMplsTable, which further define the   MPLS PSN configuration.  Note\: the exact set of PSN types is yet to be worked   out by the WG. 
            	**type**\:  :py:class:`Cpwvcpsntype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry.Cpwvcpsntype>`
            
            .. attribute:: cpwvcsetuppriority
            
            	This object define the relative set\-up priority of the VC    in a lowest\-to\-highest fashion, where 0 is the highest   priority. VCs with the same priority are treated with  equal priority. Dropped VC will be set 'dormant' (as  indicated in cpwVcOperStatus).  This value is significant if there are competing resources  between VCs and the implementation support this feature.  If not supported or not relevant, the value of zero MUST  be used
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcholdingpriority
            
            	This object define the relative holding priority of the VC    in a lowest\-to\-highest fashion, where 0 is the highest   priority. VCs with the same priority are treated with  equal priority. Dropped VC will be set 'dormant' (as  indicated in cpwVcOperStatus).  This value is significant if there are competing resources  between VCs and the implementation support this feature.  If not supported or not relevant, the value of zero MUST  be used
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcinboundmode
            
            	This object is used to enable greater security for   implementation that use per platform VC label space. In   strict mode, packets coming from the PSN are accepted only   from tunnels that are associated to the same VC via the   inbound tunnel table in the case of MPLS, or as identified   by the source IP address in case of L2TP or IP PSN. The   entries in the inbound tunnel table are either explicitly   configured or implicitly known by the maintenance protocol   used for VC set\-up.   If such association is not known, not configured or not   desired, loose mode should be configured, and the node   should accept the packet based on the VC label only   regardless of the outer tunnel used to carry the VC
            	**type**\:  :py:class:`Cpwvcinboundmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry.Cpwvcinboundmode>`
            
            .. attribute:: cpwvcpeeraddrtype
            
            	Denotes the address type of the peer node maintenance  protocol (signaling) address if PW maintenance protocol is  used for the VC creation. It should be set to   'unknown' if PE/PW maintenance protocol is not used,   i.e. cpwVcOwner is set to 'manual'. 
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cpwvcpeeraddr
            
            	This object contains the value of of the peer node address  of the PW/PE maintenance protocol entity. This object   should contain a value of 0 if not relevant (manual   configuration of the VC)
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcid
            
            	Used in the outgoing VC ID field within the 'Virtual  Circuit FEC Element' when LDP signaling is used or PW ID   AVP for L2TP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvclocalgroupid
            
            	Used in the Group ID field sent to the peer PWES   within the maintenance protocol used for VC setup,   zero if not used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvccontrolword
            
            	Define if the control word will be sent with each packet by   the local node
            	**type**\: bool
            
            .. attribute:: cpwvclocalifmtu
            
            	If not equal zero, the optional IfMtu object in the   maintenance protocol will be sent with this value,   representing the locally supported MTU size over the   interface (or the virtual interface) associated with the   VC
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvclocalifstring
            
            	Each VC is associated to an interface (or a virtual   interface) in the ifTable of the node as part of the  service configuration. This object defines if the   maintenance protocol will send the interface's name as  appears on the ifTable in the name object as part of the  maintenance protocol. If set to false, the optional element  will not be sent
            	**type**\: bool
            
            .. attribute:: cpwvcremotegroupid
            
            	Obtained from the Group ID field as received via the   maintenance protocol used for VC setup, zero if not used.   Value of 0xFFFF shall be used if the object is yet to be   defined by the VC maintenance protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcremotecontrolword
            
            	If maintenance protocol is used for VC establishment, this   parameter indicates the received status of the control word   usage, i.e. if packets will be received with control word  or not. The value of 'notYetKnown' is used while the  maintenance protocol has not yet received the indication   from the remote node.  In manual configuration of the VC this parameters indicate   to the local node what is the expected encapsulation for  the received packets. 
            	**type**\:  :py:class:`Cpwvcremotecontrolword <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry.Cpwvcremotecontrolword>`
            
            .. attribute:: cpwvcremoteifmtu
            
            	The remote interface MTU as (optionally) received from the  remote node via the maintenance protocol. Should be zero if  this parameter is not available or not used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcremoteifstring
            
            	Indicate the interface description string as received by  the maintenance protocol, MUST be NULL string if not   applicable or not known yet
            	**type**\: str
            
            	**length:** 0..80
            
            .. attribute:: cpwvcoutboundvclabel
            
            	The VC label used in the outbound direction (i.e. toward   the PSN). It may be set up manually if owner is 'manual' or   automatically otherwise. Examples\: For MPLS PSN, it   represents the 20 bits of VC tag, for L2TP it represent the  32 bits Session ID.  If the label is not yet known (signaling in process), the   object should return a value of 0xFFFF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcinboundvclabel
            
            	The VC label used in the inbound direction (i.e. packets   received from the PSN. It may be set up manually if owner  is 'manual' or automatically otherwise.   Examples\: For MPLS PSN, it represents the 20 bits of VC  tag, for L2TP it represent the 32 bits Session ID.  If the label is not yet known (signaling in process), the   object should return a value of 0xFFFF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcname
            
            	The canonical name assigned to the VC
            	**type**\: str
            
            .. attribute:: cpwvcdescr
            
            	A textual string containing information about the VC.   If there is no description this object contains a zero  length string
            	**type**\: str
            
            .. attribute:: cpwvccreatetime
            
            	System time when this VC was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcuptime
            
            	Number of consecutive ticks this VC has been 'up' in  both directions together (i.e. 'up' is observed in   cpwVcOperStatus.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcadminstatus
            
            	The desired operational status of this VC
            	**type**\:  :py:class:`Cpwvcadminstatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry.Cpwvcadminstatus>`
            
            .. attribute:: cpwvcoperstatus
            
            	Indicates the actual combined operational status of this   VC. It is 'up' if both cpwVcInboundOperStatus and   cpwVcOutboundOperStatus are in 'up' state. For all other   values, if the VCs in both directions are of the same  value it reflects that value, otherwise it is set to the  most severe status out of the two statuses. The order of   severance from most severe to less severe is\: unknown,   notPresent, down, lowerLayerDown, dormant, testing, up.  The operator may consult the per direction OperStatus for  fault isolation per direction
            	**type**\:  :py:class:`CpwOperStatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwOperStatus>`
            
            .. attribute:: cpwvcinboundoperstatus
            
            	Indicates the actual operational status of this VC in the   inbound direction.   \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                     passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:  :py:class:`CpwOperStatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwOperStatus>`
            
            .. attribute:: cpwvcoutboundoperstatus
            
            	Indicates the actual operational status of this VC in the   outbound direction  \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                    passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:  :py:class:`CpwOperStatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwOperStatus>`
            
            .. attribute:: cpwvctimeelapsed
            
            	The number of seconds, including partial seconds,  that have elapsed since the beginning of the current  measurement period. If, for some reason, such as an  adjustment in the system's time\-of\-day clock, the  current interval exceeds the maximum value, the  agent will return the maximum value
            	**type**\: int
            
            	**range:** 1..900
            
            .. attribute:: cpwvcvalidintervals
            
            	The number of previous 15\-minute intervals  for which data was collected.   An agent with PW capability must be capable of supporting at   least n intervals. The minimum value of n is 4, The default   of n is 32 and the maximum value of n is 96.  The value will be <n> unless the measurement was (re\-)   started within the last (<n>\*15) minutes, in which case the   value will be the number of complete 15 minute intervals for   which the agent has at least some data. In certain cases   (e.g., in the case where the agent is a proxy) it is   possible that some intervals are unavailable.  In this case,   this interval is the maximum interval number for which data   is available. 
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: cpwvcrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cpwvcstoragetype
            
            	This variable indicates the storage type for this  object
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvctable.Cpwvcentry, self).__init__()

                self.yang_name = "cpwVcEntry"
                self.yang_parent_name = "cpwVcTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.uint32, 'cpwVcIndex')),
                    ('cpwvctype', YLeaf(YType.enumeration, 'cpwVcType')),
                    ('cpwvcowner', YLeaf(YType.enumeration, 'cpwVcOwner')),
                    ('cpwvcpsntype', YLeaf(YType.enumeration, 'cpwVcPsnType')),
                    ('cpwvcsetuppriority', YLeaf(YType.int32, 'cpwVcSetUpPriority')),
                    ('cpwvcholdingpriority', YLeaf(YType.int32, 'cpwVcHoldingPriority')),
                    ('cpwvcinboundmode', YLeaf(YType.enumeration, 'cpwVcInboundMode')),
                    ('cpwvcpeeraddrtype', YLeaf(YType.enumeration, 'cpwVcPeerAddrType')),
                    ('cpwvcpeeraddr', YLeaf(YType.str, 'cpwVcPeerAddr')),
                    ('cpwvcid', YLeaf(YType.uint32, 'cpwVcID')),
                    ('cpwvclocalgroupid', YLeaf(YType.uint32, 'cpwVcLocalGroupID')),
                    ('cpwvccontrolword', YLeaf(YType.boolean, 'cpwVcControlWord')),
                    ('cpwvclocalifmtu', YLeaf(YType.uint32, 'cpwVcLocalIfMtu')),
                    ('cpwvclocalifstring', YLeaf(YType.boolean, 'cpwVcLocalIfString')),
                    ('cpwvcremotegroupid', YLeaf(YType.uint32, 'cpwVcRemoteGroupID')),
                    ('cpwvcremotecontrolword', YLeaf(YType.enumeration, 'cpwVcRemoteControlWord')),
                    ('cpwvcremoteifmtu', YLeaf(YType.uint32, 'cpwVcRemoteIfMtu')),
                    ('cpwvcremoteifstring', YLeaf(YType.str, 'cpwVcRemoteIfString')),
                    ('cpwvcoutboundvclabel', YLeaf(YType.uint32, 'cpwVcOutboundVcLabel')),
                    ('cpwvcinboundvclabel', YLeaf(YType.uint32, 'cpwVcInboundVcLabel')),
                    ('cpwvcname', YLeaf(YType.str, 'cpwVcName')),
                    ('cpwvcdescr', YLeaf(YType.str, 'cpwVcDescr')),
                    ('cpwvccreatetime', YLeaf(YType.uint32, 'cpwVcCreateTime')),
                    ('cpwvcuptime', YLeaf(YType.uint32, 'cpwVcUpTime')),
                    ('cpwvcadminstatus', YLeaf(YType.enumeration, 'cpwVcAdminStatus')),
                    ('cpwvcoperstatus', YLeaf(YType.enumeration, 'cpwVcOperStatus')),
                    ('cpwvcinboundoperstatus', YLeaf(YType.enumeration, 'cpwVcInboundOperStatus')),
                    ('cpwvcoutboundoperstatus', YLeaf(YType.enumeration, 'cpwVcOutboundOperStatus')),
                    ('cpwvctimeelapsed', YLeaf(YType.int32, 'cpwVcTimeElapsed')),
                    ('cpwvcvalidintervals', YLeaf(YType.int32, 'cpwVcValidIntervals')),
                    ('cpwvcrowstatus', YLeaf(YType.enumeration, 'cpwVcRowStatus')),
                    ('cpwvcstoragetype', YLeaf(YType.enumeration, 'cpwVcStorageType')),
                ])
                self.cpwvcindex = None
                self.cpwvctype = None
                self.cpwvcowner = None
                self.cpwvcpsntype = None
                self.cpwvcsetuppriority = None
                self.cpwvcholdingpriority = None
                self.cpwvcinboundmode = None
                self.cpwvcpeeraddrtype = None
                self.cpwvcpeeraddr = None
                self.cpwvcid = None
                self.cpwvclocalgroupid = None
                self.cpwvccontrolword = None
                self.cpwvclocalifmtu = None
                self.cpwvclocalifstring = None
                self.cpwvcremotegroupid = None
                self.cpwvcremotecontrolword = None
                self.cpwvcremoteifmtu = None
                self.cpwvcremoteifstring = None
                self.cpwvcoutboundvclabel = None
                self.cpwvcinboundvclabel = None
                self.cpwvcname = None
                self.cpwvcdescr = None
                self.cpwvccreatetime = None
                self.cpwvcuptime = None
                self.cpwvcadminstatus = None
                self.cpwvcoperstatus = None
                self.cpwvcinboundoperstatus = None
                self.cpwvcoutboundoperstatus = None
                self.cpwvctimeelapsed = None
                self.cpwvcvalidintervals = None
                self.cpwvcrowstatus = None
                self.cpwvcstoragetype = None
                self._segment_path = lambda: "cpwVcEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvctable.Cpwvcentry, ['cpwvcindex', 'cpwvctype', 'cpwvcowner', 'cpwvcpsntype', 'cpwvcsetuppriority', 'cpwvcholdingpriority', 'cpwvcinboundmode', 'cpwvcpeeraddrtype', 'cpwvcpeeraddr', 'cpwvcid', 'cpwvclocalgroupid', 'cpwvccontrolword', 'cpwvclocalifmtu', 'cpwvclocalifstring', 'cpwvcremotegroupid', 'cpwvcremotecontrolword', 'cpwvcremoteifmtu', 'cpwvcremoteifstring', 'cpwvcoutboundvclabel', 'cpwvcinboundvclabel', 'cpwvcname', 'cpwvcdescr', 'cpwvccreatetime', 'cpwvcuptime', 'cpwvcadminstatus', 'cpwvcoperstatus', 'cpwvcinboundoperstatus', 'cpwvcoutboundoperstatus', 'cpwvctimeelapsed', 'cpwvcvalidintervals', 'cpwvcrowstatus', 'cpwvcstoragetype'], name, value)

            class Cpwvcadminstatus(Enum):
                """
                Cpwvcadminstatus (Enum Class)

                The desired operational status of this VC.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Cpwvcinboundmode(Enum):
                """
                Cpwvcinboundmode (Enum Class)

                This object is used to enable greater security for  

                implementation that use per platform VC label space. In  

                strict mode, packets coming from the PSN are accepted only  

                from tunnels that are associated to the same VC via the  

                inbound tunnel table in the case of MPLS, or as identified  

                by the source IP address in case of L2TP or IP PSN. The  

                entries in the inbound tunnel table are either explicitly  

                configured or implicitly known by the maintenance protocol  

                used for VC set\-up. 

                If such association is not known, not configured or not  

                desired, loose mode should be configured, and the node  

                should accept the packet based on the VC label only  

                regardless of the outer tunnel used to carry the VC.

                .. data:: loose = 1

                .. data:: strict = 2

                """

                loose = Enum.YLeaf(1, "loose")

                strict = Enum.YLeaf(2, "strict")


            class Cpwvcowner(Enum):
                """
                Cpwvcowner (Enum Class)

                Set by the operator to indicate the protocol responsible  

                for establishing this VC. Value 'manual' is used in all 

                cases where no maintenance protocol (PW signaling) is used  

                to set\-up the VC, i.e. require configuration of entries in 

                the VC tables including VC labels, etc. The value  

                'maintenanceProtocol' is used in case of standard 

                signaling of the VC for the specific PSN, for example LDP 

                for MPLS PSN as specified in <draft\- draft\-martini\- 

                l2circuit\-trans\-mpls> or L2TP control protocol.  

                Value 'other' is used for other types of signaling.

                .. data:: manual = 1

                .. data:: maintenanceProtocol = 2

                .. data:: other = 3

                """

                manual = Enum.YLeaf(1, "manual")

                maintenanceProtocol = Enum.YLeaf(2, "maintenanceProtocol")

                other = Enum.YLeaf(3, "other")


            class Cpwvcpsntype(Enum):
                """
                Cpwvcpsntype (Enum Class)

                Set by the operator to indicate the PSN type on which this  

                VC will be carried. Based on this object, the relevant PSN  

                table entries are created in the in the PSN specific MIB  

                modules. For example, if mpls(1) is defined, the agent  

                create an entry in cpwVcMplsTable, which further define the  

                MPLS PSN configuration. 

                Note\: the exact set of PSN types is yet to be worked  

                out by the WG. 

                .. data:: mpls = 1

                .. data:: l2tp = 2

                .. data:: ip = 3

                .. data:: mplsOverIp = 4

                .. data:: gre = 5

                .. data:: other = 6

                """

                mpls = Enum.YLeaf(1, "mpls")

                l2tp = Enum.YLeaf(2, "l2tp")

                ip = Enum.YLeaf(3, "ip")

                mplsOverIp = Enum.YLeaf(4, "mplsOverIp")

                gre = Enum.YLeaf(5, "gre")

                other = Enum.YLeaf(6, "other")


            class Cpwvcremotecontrolword(Enum):
                """
                Cpwvcremotecontrolword (Enum Class)

                If maintenance protocol is used for VC establishment, this  

                parameter indicates the received status of the control word  

                usage, i.e. if packets will be received with control word 

                or not. The value of 'notYetKnown' is used while the 

                maintenance protocol has not yet received the indication  

                from the remote node. 

                In manual configuration of the VC this parameters indicate  

                to the local node what is the expected encapsulation for 

                the received packets. 

                .. data:: noControlWord = 1

                .. data:: withControlWord = 2

                .. data:: notYetKnown = 3

                """

                noControlWord = Enum.YLeaf(1, "noControlWord")

                withControlWord = Enum.YLeaf(2, "withControlWord")

                notYetKnown = Enum.YLeaf(3, "notYetKnown")



    class Cpwvcperfcurrenttable(Entity):
        """
        This table provides per\-VC performance information for the  
        current interval.
        
        .. attribute:: cpwvcperfcurrententry
        
        	An entry in this table is created by the agent for  every VC
        	**type**\: list of  		 :py:class:`Cpwvcperfcurrententry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperfcurrenttable.Cpwvcperfcurrententry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcperfcurrenttable, self).__init__()

            self.yang_name = "cpwVcPerfCurrentTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcPerfCurrentEntry", ("cpwvcperfcurrententry", CISCOIETFPWMIB.Cpwvcperfcurrenttable.Cpwvcperfcurrententry))])
            self._leafs = OrderedDict()

            self.cpwvcperfcurrententry = YList(self)
            self._segment_path = lambda: "cpwVcPerfCurrentTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcperfcurrenttable, [], name, value)


        class Cpwvcperfcurrententry(Entity):
            """
            An entry in this table is created by the agent for 
            every VC.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperfcurrentinhcpackets
            
            	High capacity counter for number of packets received  by the VC (from the PSN) in the current 15 minute  interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentinhcbytes
            
            	High capacity counter for number of bytes received  by the VC (from the PSN) in the current 15 minute  interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentouthcpackets
            
            	High capacity counter for number of packets forwarded  by the VC (to the PSN) in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentouthcbytes
            
            	High capacity counter for number of bytes forwarded  by the VC (to the PSN) in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvcperfcurrenttable.Cpwvcperfcurrententry, self).__init__()

                self.yang_name = "cpwVcPerfCurrentEntry"
                self.yang_parent_name = "cpwVcPerfCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcperfcurrentinhcpackets', YLeaf(YType.uint64, 'cpwVcPerfCurrentInHCPackets')),
                    ('cpwvcperfcurrentinhcbytes', YLeaf(YType.uint64, 'cpwVcPerfCurrentInHCBytes')),
                    ('cpwvcperfcurrentouthcpackets', YLeaf(YType.uint64, 'cpwVcPerfCurrentOutHCPackets')),
                    ('cpwvcperfcurrentouthcbytes', YLeaf(YType.uint64, 'cpwVcPerfCurrentOutHCBytes')),
                ])
                self.cpwvcindex = None
                self.cpwvcperfcurrentinhcpackets = None
                self.cpwvcperfcurrentinhcbytes = None
                self.cpwvcperfcurrentouthcpackets = None
                self.cpwvcperfcurrentouthcbytes = None
                self._segment_path = lambda: "cpwVcPerfCurrentEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfCurrentTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvcperfcurrenttable.Cpwvcperfcurrententry, ['cpwvcindex', 'cpwvcperfcurrentinhcpackets', 'cpwvcperfcurrentinhcbytes', 'cpwvcperfcurrentouthcpackets', 'cpwvcperfcurrentouthcbytes'], name, value)


    class Cpwvcperfintervaltable(Entity):
        """
        This table provides per\-VC performance information for  
        each interval.
        
        .. attribute:: cpwvcperfintervalentry
        
        	An entry in this table is created agent for every VC
        	**type**\: list of  		 :py:class:`Cpwvcperfintervalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperfintervaltable.Cpwvcperfintervalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcperfintervaltable, self).__init__()

            self.yang_name = "cpwVcPerfIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcPerfIntervalEntry", ("cpwvcperfintervalentry", CISCOIETFPWMIB.Cpwvcperfintervaltable.Cpwvcperfintervalentry))])
            self._leafs = OrderedDict()

            self.cpwvcperfintervalentry = YList(self)
            self._segment_path = lambda: "cpwVcPerfIntervalTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcperfintervaltable, [], name, value)


        class Cpwvcperfintervalentry(Entity):
            """
            An entry in this table is created agent for every VC.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperfintervalnumber  (key)
            
            	A number N, between 1 and 96, which identifies the  interval for which the set of statistics is available.  The interval identified by 1 is the most recently  completed 15 minute interval, and the interval identified  by N is the interval immediately preceding the one  identified by N\-1.  The minimum range of N is 1 through 4. The default range  is 1 to 32. The maximum range of N is 1 through 96. 
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: cpwvcperfintervalvaliddata
            
            	This variable indicates if the data for this interval  is valid
            	**type**\: bool
            
            .. attribute:: cpwvcperfintervaltimeelapsed
            
            	The duration of a particular interval in seconds.  Adjustments in the system's time\-of\-day clock, may  cause the interval to be greater or less than the  normal value. Therefore this actual interval value  is provided
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwvcperfintervalinhcpackets
            
            	High capacity counter for number of packets received by  the VC (from the PSN) in a particular 15\-minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalinhcbytes
            
            	High capacity counter for number of bytes received by the   VC (from the PSN) in a particular 15\-minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalouthcpackets
            
            	High capacity counter for number of packets forwarded by   the VC (to the PSN) in a particular 15\-minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalouthcbytes
            
            	High capacity counter for number of bytes forwarded by the   VC (to the PSN) in a particular 15\-minute interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvcperfintervaltable.Cpwvcperfintervalentry, self).__init__()

                self.yang_name = "cpwVcPerfIntervalEntry"
                self.yang_parent_name = "cpwVcPerfIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcperfintervalnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcperfintervalnumber', YLeaf(YType.int32, 'cpwVcPerfIntervalNumber')),
                    ('cpwvcperfintervalvaliddata', YLeaf(YType.boolean, 'cpwVcPerfIntervalValidData')),
                    ('cpwvcperfintervaltimeelapsed', YLeaf(YType.int32, 'cpwVcPerfIntervalTimeElapsed')),
                    ('cpwvcperfintervalinhcpackets', YLeaf(YType.uint64, 'cpwVcPerfIntervalInHCPackets')),
                    ('cpwvcperfintervalinhcbytes', YLeaf(YType.uint64, 'cpwVcPerfIntervalInHCBytes')),
                    ('cpwvcperfintervalouthcpackets', YLeaf(YType.uint64, 'cpwVcPerfIntervalOutHCPackets')),
                    ('cpwvcperfintervalouthcbytes', YLeaf(YType.uint64, 'cpwVcPerfIntervalOutHCBytes')),
                ])
                self.cpwvcindex = None
                self.cpwvcperfintervalnumber = None
                self.cpwvcperfintervalvaliddata = None
                self.cpwvcperfintervaltimeelapsed = None
                self.cpwvcperfintervalinhcpackets = None
                self.cpwvcperfintervalinhcbytes = None
                self.cpwvcperfintervalouthcpackets = None
                self.cpwvcperfintervalouthcbytes = None
                self._segment_path = lambda: "cpwVcPerfIntervalEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwVcPerfIntervalNumber='" + str(self.cpwvcperfintervalnumber) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfIntervalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvcperfintervaltable.Cpwvcperfintervalentry, ['cpwvcindex', 'cpwvcperfintervalnumber', 'cpwvcperfintervalvaliddata', 'cpwvcperfintervaltimeelapsed', 'cpwvcperfintervalinhcpackets', 'cpwvcperfintervalinhcbytes', 'cpwvcperfintervalouthcpackets', 'cpwvcperfintervalouthcbytes'], name, value)


    class Cpwvcperftotaltable(Entity):
        """
        This table provides per\-VC Performance information from VC  
        start time.
        
        .. attribute:: cpwvcperftotalentry
        
        	An entry in this table is created agent for every VC
        	**type**\: list of  		 :py:class:`Cpwvcperftotalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcperftotaltable.Cpwvcperftotalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcperftotaltable, self).__init__()

            self.yang_name = "cpwVcPerfTotalTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcPerfTotalEntry", ("cpwvcperftotalentry", CISCOIETFPWMIB.Cpwvcperftotaltable.Cpwvcperftotalentry))])
            self._leafs = OrderedDict()

            self.cpwvcperftotalentry = YList(self)
            self._segment_path = lambda: "cpwVcPerfTotalTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcperftotaltable, [], name, value)


        class Cpwvcperftotalentry(Entity):
            """
            An entry in this table is created agent for every VC.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperftotalinhcpackets
            
            	High capacity counter for number of packets received by the   VC (from the PSN)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalinhcbytes
            
            	High capacity counter for number of bytes received by the   VC (from the PSN)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalouthcpackets
            
            	High capacity counter for number of packets forwarded by   the VC (to the PSN)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalouthcbytes
            
            	High capacity counter for number of bytes forwarded by the   VC (to the PSN)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotaldiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at  which any one or more of this row Counter32 or  Counter64 suffered a discontinuity. If no such  discontinuities have occurred since the last re\-  initialization of the local management subsystem, then  this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvcperftotaltable.Cpwvcperftotalentry, self).__init__()

                self.yang_name = "cpwVcPerfTotalEntry"
                self.yang_parent_name = "cpwVcPerfTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcperftotalinhcpackets', YLeaf(YType.uint64, 'cpwVcPerfTotalInHCPackets')),
                    ('cpwvcperftotalinhcbytes', YLeaf(YType.uint64, 'cpwVcPerfTotalInHCBytes')),
                    ('cpwvcperftotalouthcpackets', YLeaf(YType.uint64, 'cpwVcPerfTotalOutHCPackets')),
                    ('cpwvcperftotalouthcbytes', YLeaf(YType.uint64, 'cpwVcPerfTotalOutHCBytes')),
                    ('cpwvcperftotaldiscontinuitytime', YLeaf(YType.uint32, 'cpwVcPerfTotalDiscontinuityTime')),
                ])
                self.cpwvcindex = None
                self.cpwvcperftotalinhcpackets = None
                self.cpwvcperftotalinhcbytes = None
                self.cpwvcperftotalouthcpackets = None
                self.cpwvcperftotalouthcbytes = None
                self.cpwvcperftotaldiscontinuitytime = None
                self._segment_path = lambda: "cpwVcPerfTotalEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvcperftotaltable.Cpwvcperftotalentry, ['cpwvcindex', 'cpwvcperftotalinhcpackets', 'cpwvcperftotalinhcbytes', 'cpwvcperftotalouthcpackets', 'cpwvcperftotalouthcbytes', 'cpwvcperftotaldiscontinuitytime'], name, value)


    class Cpwvcidmappingtable(Entity):
        """
        This table provides reverse mapping of the existing VCs  
        based on vc type and VC ID ordering. This table is  
        typically useful for EMS ordered query of existing VCs.
        
        .. attribute:: cpwvcidmappingentry
        
        	An entry in this table is created by the agent for every   VC configured by the cpwVcTable
        	**type**\: list of  		 :py:class:`Cpwvcidmappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcidmappingtable.Cpwvcidmappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcidmappingtable, self).__init__()

            self.yang_name = "cpwVcIdMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcIdMappingEntry", ("cpwvcidmappingentry", CISCOIETFPWMIB.Cpwvcidmappingtable.Cpwvcidmappingentry))])
            self._leafs = OrderedDict()

            self.cpwvcidmappingentry = YList(self)
            self._segment_path = lambda: "cpwVcIdMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcidmappingtable, [], name, value)


        class Cpwvcidmappingentry(Entity):
            """
            An entry in this table is created by the agent for every  
            VC configured by the cpwVcTable.
            
            .. attribute:: cpwvcidmappingvctype  (key)
            
            	The VC type (indicate the service) of this VC
            	**type**\:  :py:class:`CpwVcType <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwVcType>`
            
            .. attribute:: cpwvcidmappingvcid  (key)
            
            	The VC ID of this VC. Zero if the VC is configured   manually
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcidmappingpeeraddrtype  (key)
            
            	IP address type of the peer node
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cpwvcidmappingpeeraddr  (key)
            
            	IP address type of the peer node
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcidmappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvcidmappingtable.Cpwvcidmappingentry, self).__init__()

                self.yang_name = "cpwVcIdMappingEntry"
                self.yang_parent_name = "cpwVcIdMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcidmappingvctype','cpwvcidmappingvcid','cpwvcidmappingpeeraddrtype','cpwvcidmappingpeeraddr','cpwvcidmappingvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcidmappingvctype', YLeaf(YType.enumeration, 'cpwVcIdMappingVcType')),
                    ('cpwvcidmappingvcid', YLeaf(YType.uint32, 'cpwVcIdMappingVcID')),
                    ('cpwvcidmappingpeeraddrtype', YLeaf(YType.enumeration, 'cpwVcIdMappingPeerAddrType')),
                    ('cpwvcidmappingpeeraddr', YLeaf(YType.str, 'cpwVcIdMappingPeerAddr')),
                    ('cpwvcidmappingvcindex', YLeaf(YType.uint32, 'cpwVcIdMappingVcIndex')),
                ])
                self.cpwvcidmappingvctype = None
                self.cpwvcidmappingvcid = None
                self.cpwvcidmappingpeeraddrtype = None
                self.cpwvcidmappingpeeraddr = None
                self.cpwvcidmappingvcindex = None
                self._segment_path = lambda: "cpwVcIdMappingEntry" + "[cpwVcIdMappingVcType='" + str(self.cpwvcidmappingvctype) + "']" + "[cpwVcIdMappingVcID='" + str(self.cpwvcidmappingvcid) + "']" + "[cpwVcIdMappingPeerAddrType='" + str(self.cpwvcidmappingpeeraddrtype) + "']" + "[cpwVcIdMappingPeerAddr='" + str(self.cpwvcidmappingpeeraddr) + "']" + "[cpwVcIdMappingVcIndex='" + str(self.cpwvcidmappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcIdMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvcidmappingtable.Cpwvcidmappingentry, ['cpwvcidmappingvctype', 'cpwvcidmappingvcid', 'cpwvcidmappingpeeraddrtype', 'cpwvcidmappingpeeraddr', 'cpwvcidmappingvcindex'], name, value)


    class Cpwvcpeermappingtable(Entity):
        """
        This table provides reverse mapping of the existing VCs  
        based on vc type and VC ID ordering. This table is  
        typically useful for EMS ordered query of existing VCs.
        
        .. attribute:: cpwvcpeermappingentry
        
        	An entry in this table is created by the agent for every   VC configured in cpwVcTable
        	**type**\: list of  		 :py:class:`Cpwvcpeermappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvcpeermappingtable.Cpwvcpeermappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            super(CISCOIETFPWMIB.Cpwvcpeermappingtable, self).__init__()

            self.yang_name = "cpwVcPeerMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcPeerMappingEntry", ("cpwvcpeermappingentry", CISCOIETFPWMIB.Cpwvcpeermappingtable.Cpwvcpeermappingentry))])
            self._leafs = OrderedDict()

            self.cpwvcpeermappingentry = YList(self)
            self._segment_path = lambda: "cpwVcPeerMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMIB.Cpwvcpeermappingtable, [], name, value)


        class Cpwvcpeermappingentry(Entity):
            """
            An entry in this table is created by the agent for every  
            VC configured in cpwVcTable.
            
            .. attribute:: cpwvcpeermappingpeeraddrtype  (key)
            
            	IP address type of the peer node
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cpwvcpeermappingpeeraddr  (key)
            
            	IP address type of the peer node
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcpeermappingvctype  (key)
            
            	The VC type (indicate the service) of this VC
            	**type**\:  :py:class:`CpwVcType <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwVcType>`
            
            .. attribute:: cpwvcpeermappingvcid  (key)
            
            	The VC ID of this VC. Zero if the VC is configured   manually
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcpeermappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                super(CISCOIETFPWMIB.Cpwvcpeermappingtable.Cpwvcpeermappingentry, self).__init__()

                self.yang_name = "cpwVcPeerMappingEntry"
                self.yang_parent_name = "cpwVcPeerMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcpeermappingpeeraddrtype','cpwvcpeermappingpeeraddr','cpwvcpeermappingvctype','cpwvcpeermappingvcid','cpwvcpeermappingvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcpeermappingpeeraddrtype', YLeaf(YType.enumeration, 'cpwVcPeerMappingPeerAddrType')),
                    ('cpwvcpeermappingpeeraddr', YLeaf(YType.str, 'cpwVcPeerMappingPeerAddr')),
                    ('cpwvcpeermappingvctype', YLeaf(YType.enumeration, 'cpwVcPeerMappingVcType')),
                    ('cpwvcpeermappingvcid', YLeaf(YType.uint32, 'cpwVcPeerMappingVcID')),
                    ('cpwvcpeermappingvcindex', YLeaf(YType.uint32, 'cpwVcPeerMappingVcIndex')),
                ])
                self.cpwvcpeermappingpeeraddrtype = None
                self.cpwvcpeermappingpeeraddr = None
                self.cpwvcpeermappingvctype = None
                self.cpwvcpeermappingvcid = None
                self.cpwvcpeermappingvcindex = None
                self._segment_path = lambda: "cpwVcPeerMappingEntry" + "[cpwVcPeerMappingPeerAddrType='" + str(self.cpwvcpeermappingpeeraddrtype) + "']" + "[cpwVcPeerMappingPeerAddr='" + str(self.cpwvcpeermappingpeeraddr) + "']" + "[cpwVcPeerMappingVcType='" + str(self.cpwvcpeermappingvctype) + "']" + "[cpwVcPeerMappingVcID='" + str(self.cpwvcpeermappingvcid) + "']" + "[cpwVcPeerMappingVcIndex='" + str(self.cpwvcpeermappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPeerMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMIB.Cpwvcpeermappingtable.Cpwvcpeermappingentry, ['cpwvcpeermappingpeeraddrtype', 'cpwvcpeermappingpeeraddr', 'cpwvcpeermappingvctype', 'cpwvcpeermappingvcid', 'cpwvcpeermappingvcindex'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIETFPWMIB()
        return self._top_entity

