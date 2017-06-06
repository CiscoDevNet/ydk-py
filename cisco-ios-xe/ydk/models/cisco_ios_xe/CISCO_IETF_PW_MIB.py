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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfPwMib(object):
    """
    
    
    .. attribute:: cpwvcidmappingtable
    
    	This table provides reverse mapping of the existing VCs   based on vc type and VC ID ordering. This table is   typically useful for EMS ordered query of existing VCs
    	**type**\:   :py:class:`Cpwvcidmappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcidmappingtable>`
    
    .. attribute:: cpwvcobjects
    
    	
    	**type**\:   :py:class:`Cpwvcobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcobjects>`
    
    .. attribute:: cpwvcpeermappingtable
    
    	This table provides reverse mapping of the existing VCs   based on vc type and VC ID ordering. This table is   typically useful for EMS ordered query of existing VCs
    	**type**\:   :py:class:`Cpwvcpeermappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcpeermappingtable>`
    
    .. attribute:: cpwvcperfcurrenttable
    
    	This table provides per\-VC performance information for the   current interval
    	**type**\:   :py:class:`Cpwvcperfcurrenttable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperfcurrenttable>`
    
    .. attribute:: cpwvcperfintervaltable
    
    	This table provides per\-VC performance information for   each interval
    	**type**\:   :py:class:`Cpwvcperfintervaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperfintervaltable>`
    
    .. attribute:: cpwvcperftotaltable
    
    	This table provides per\-VC Performance information from VC   start time
    	**type**\:   :py:class:`Cpwvcperftotaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperftotaltable>`
    
    .. attribute:: cpwvctable
    
    	This table specifies information for connecting various  emulated services to various tunnel type
    	**type**\:   :py:class:`Cpwvctable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-MIB'
    _revision = '2004-03-17'

    def __init__(self):
        self.cpwvcidmappingtable = CiscoIetfPwMib.Cpwvcidmappingtable()
        self.cpwvcidmappingtable.parent = self
        self.cpwvcobjects = CiscoIetfPwMib.Cpwvcobjects()
        self.cpwvcobjects.parent = self
        self.cpwvcpeermappingtable = CiscoIetfPwMib.Cpwvcpeermappingtable()
        self.cpwvcpeermappingtable.parent = self
        self.cpwvcperfcurrenttable = CiscoIetfPwMib.Cpwvcperfcurrenttable()
        self.cpwvcperfcurrenttable.parent = self
        self.cpwvcperfintervaltable = CiscoIetfPwMib.Cpwvcperfintervaltable()
        self.cpwvcperfintervaltable.parent = self
        self.cpwvcperftotaltable = CiscoIetfPwMib.Cpwvcperftotaltable()
        self.cpwvcperftotaltable.parent = self
        self.cpwvctable = CiscoIetfPwMib.Cpwvctable()
        self.cpwvctable.parent = self


    class Cpwvcobjects(object):
        """
        
        
        .. attribute:: cpwvcindexnext
        
        	This object contains an appropriate value to be used  for cpwVcIndex when creating entries in the  cpwVcTable. The value 0 indicates that no  unassigned entries are available.  To obtain the  value of cpwVcIndex for a new entry in the  cpwVcTable, the manager issues a management  protocol retrieval operation to obtain the current  value of cpwVcIndex.  After each retrieval  operation, the agent should modify the value to  reflect the next unassigned index.  After a manager  retrieves a value the agent will determine through  its local policy when this index value will be made  available for reuse
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcnotifrate
        
        	This object defines the maximum number of PW VC notifications that can be emitted from the device per second
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcperftotalerrorpackets
        
        	Counter for number of error at VC level processing, for   example packets received with unknown VC label
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cpwvcupdownnotifenable
        
        	If this object is set to true(1), then it enables the emission of cpwVcUp and cpwVcDown notifications; otherwise these notifications are not emitted
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcindexnext = None
            self.cpwvcnotifrate = None
            self.cpwvcperftotalerrorpackets = None
            self.cpwvcupdownnotifenable = None

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcindexnext is not None:
                return True

            if self.cpwvcnotifrate is not None:
                return True

            if self.cpwvcperftotalerrorpackets is not None:
                return True

            if self.cpwvcupdownnotifenable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcobjects']['meta_info']


    class Cpwvctable(object):
        """
        This table specifies information for connecting various 
        emulated services to various tunnel type.
        
        .. attribute:: cpwvcentry
        
        	A row in this table represents an emulated virtual  connection (VC) across a packet network. It is indexed by  cpwVcIndex, which uniquely identifying a singular   connection. 
        	**type**\: list of    :py:class:`Cpwvcentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcentry = YList()
            self.cpwvcentry.parent = self
            self.cpwvcentry.name = 'cpwvcentry'


        class Cpwvcentry(object):
            """
            A row in this table represents an emulated virtual 
            connection (VC) across a packet network. It is indexed by 
            cpwVcIndex, which uniquely identifying a singular  
            connection. 
            
            .. attribute:: cpwvcindex  <key>
            
            	Index for the conceptual row identifying a VC within   this PW Emulation VC table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcadminstatus
            
            	The desired operational status of this VC
            	**type**\:   :py:class:`CpwvcadminstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcadminstatusEnum>`
            
            .. attribute:: cpwvccontrolword
            
            	Define if the control word will be sent with each packet by   the local node
            	**type**\:  bool
            
            .. attribute:: cpwvccreatetime
            
            	System time when this VC was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcdescr
            
            	A textual string containing information about the VC.   If there is no description this object contains a zero  length string
            	**type**\:  str
            
            .. attribute:: cpwvcholdingpriority
            
            	This object define the relative holding priority of the VC    in a lowest\-to\-highest fashion, where 0 is the highest   priority. VCs with the same priority are treated with  equal priority. Dropped VC will be set 'dormant' (as  indicated in cpwVcOperStatus).  This value is significant if there are competing resources  between VCs and the implementation support this feature.  If not supported or not relevant, the value of zero MUST  be used
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcid
            
            	Used in the outgoing VC ID field within the 'Virtual  Circuit FEC Element' when LDP signaling is used or PW ID   AVP for L2TP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcinboundmode
            
            	This object is used to enable greater security for   implementation that use per platform VC label space. In   strict mode, packets coming from the PSN are accepted only   from tunnels that are associated to the same VC via the   inbound tunnel table in the case of MPLS, or as identified   by the source IP address in case of L2TP or IP PSN. The   entries in the inbound tunnel table are either explicitly   configured or implicitly known by the maintenance protocol   used for VC set\-up.   If such association is not known, not configured or not   desired, loose mode should be configured, and the node   should accept the packet based on the VC label only   regardless of the outer tunnel used to carry the VC
            	**type**\:   :py:class:`CpwvcinboundmodeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcinboundmodeEnum>`
            
            .. attribute:: cpwvcinboundoperstatus
            
            	Indicates the actual operational status of this VC in the   inbound direction.   \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                     passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:   :py:class:`CpwoperstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwoperstatusEnum>`
            
            .. attribute:: cpwvcinboundvclabel
            
            	The VC label used in the inbound direction (i.e. packets   received from the PSN. It may be set up manually if owner  is 'manual' or automatically otherwise.   Examples\: For MPLS PSN, it represents the 20 bits of VC  tag, for L2TP it represent the 32 bits Session ID.  If the label is not yet known (signaling in process), the   object should return a value of 0xFFFF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvclocalgroupid
            
            	Used in the Group ID field sent to the peer PWES   within the maintenance protocol used for VC setup,   zero if not used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvclocalifmtu
            
            	If not equal zero, the optional IfMtu object in the   maintenance protocol will be sent with this value,   representing the locally supported MTU size over the   interface (or the virtual interface) associated with the   VC
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvclocalifstring
            
            	Each VC is associated to an interface (or a virtual   interface) in the ifTable of the node as part of the  service configuration. This object defines if the   maintenance protocol will send the interface's name as  appears on the ifTable in the name object as part of the  maintenance protocol. If set to false, the optional element  will not be sent
            	**type**\:  bool
            
            .. attribute:: cpwvcname
            
            	The canonical name assigned to the VC
            	**type**\:  str
            
            .. attribute:: cpwvcoperstatus
            
            	Indicates the actual combined operational status of this   VC. It is 'up' if both cpwVcInboundOperStatus and   cpwVcOutboundOperStatus are in 'up' state. For all other   values, if the VCs in both directions are of the same  value it reflects that value, otherwise it is set to the  most severe status out of the two statuses. The order of   severance from most severe to less severe is\: unknown,   notPresent, down, lowerLayerDown, dormant, testing, up.  The operator may consult the per direction OperStatus for  fault isolation per direction
            	**type**\:   :py:class:`CpwoperstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwoperstatusEnum>`
            
            .. attribute:: cpwvcoutboundoperstatus
            
            	Indicates the actual operational status of this VC in the   outbound direction  \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                    passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:   :py:class:`CpwoperstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwoperstatusEnum>`
            
            .. attribute:: cpwvcoutboundvclabel
            
            	The VC label used in the outbound direction (i.e. toward   the PSN). It may be set up manually if owner is 'manual' or   automatically otherwise. Examples\: For MPLS PSN, it   represents the 20 bits of VC tag, for L2TP it represent the  32 bits Session ID.  If the label is not yet known (signaling in process), the   object should return a value of 0xFFFF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcowner
            
            	Set by the operator to indicate the protocol responsible   for establishing this VC. Value 'manual' is used in all  cases where no maintenance protocol (PW signaling) is used   to set\-up the VC, i.e. require configuration of entries in  the VC tables including VC labels, etc. The value   'maintenanceProtocol' is used in case of standard  signaling of the VC for the specific PSN, for example LDP  for MPLS PSN as specified in <draft\- draft\-martini\-  l2circuit\-trans\-mpls> or L2TP control protocol.   Value 'other' is used for other types of signaling
            	**type**\:   :py:class:`CpwvcownerEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcownerEnum>`
            
            .. attribute:: cpwvcpeeraddr
            
            	This object contains the value of of the peer node address  of the PW/PE maintenance protocol entity. This object   should contain a value of 0 if not relevant (manual   configuration of the VC)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcpeeraddrtype
            
            	Denotes the address type of the peer node maintenance  protocol (signaling) address if PW maintenance protocol is  used for the VC creation. It should be set to   'unknown' if PE/PW maintenance protocol is not used,   i.e. cpwVcOwner is set to 'manual'. 
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cpwvcpsntype
            
            	Set by the operator to indicate the PSN type on which this   VC will be carried. Based on this object, the relevant PSN   table entries are created in the in the PSN specific MIB   modules. For example, if mpls(1) is defined, the agent   create an entry in cpwVcMplsTable, which further define the   MPLS PSN configuration.  Note\: the exact set of PSN types is yet to be worked   out by the WG. 
            	**type**\:   :py:class:`CpwvcpsntypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcpsntypeEnum>`
            
            .. attribute:: cpwvcremotecontrolword
            
            	If maintenance protocol is used for VC establishment, this   parameter indicates the received status of the control word   usage, i.e. if packets will be received with control word  or not. The value of 'notYetKnown' is used while the  maintenance protocol has not yet received the indication   from the remote node.  In manual configuration of the VC this parameters indicate   to the local node what is the expected encapsulation for  the received packets. 
            	**type**\:   :py:class:`CpwvcremotecontrolwordEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcremotecontrolwordEnum>`
            
            .. attribute:: cpwvcremotegroupid
            
            	Obtained from the Group ID field as received via the   maintenance protocol used for VC setup, zero if not used.   Value of 0xFFFF shall be used if the object is yet to be   defined by the VC maintenance protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcremoteifmtu
            
            	The remote interface MTU as (optionally) received from the  remote node via the maintenance protocol. Should be zero if  this parameter is not available or not used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcremoteifstring
            
            	Indicate the interface description string as received by  the maintenance protocol, MUST be NULL string if not   applicable or not known yet
            	**type**\:  str
            
            	**length:** 0..80
            
            .. attribute:: cpwvcrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwvcsetuppriority
            
            	This object define the relative set\-up priority of the VC    in a lowest\-to\-highest fashion, where 0 is the highest   priority. VCs with the same priority are treated with  equal priority. Dropped VC will be set 'dormant' (as  indicated in cpwVcOperStatus).  This value is significant if there are competing resources  between VCs and the implementation support this feature.  If not supported or not relevant, the value of zero MUST  be used
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcstoragetype
            
            	This variable indicates the storage type for this  object
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwvctimeelapsed
            
            	The number of seconds, including partial seconds,  that have elapsed since the beginning of the current  measurement period. If, for some reason, such as an  adjustment in the system's time\-of\-day clock, the  current interval exceeds the maximum value, the  agent will return the maximum value
            	**type**\:  int
            
            	**range:** 1..900
            
            .. attribute:: cpwvctype
            
            	This value indicate the service to be carried over  this VC.   Note\: the exact set of VC types is yet to be worked   out by the WG. 
            	**type**\:   :py:class:`CpwvctypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwvctypeEnum>`
            
            .. attribute:: cpwvcuptime
            
            	Number of consecutive ticks this VC has been 'up' in  both directions together (i.e. 'up' is observed in   cpwVcOperStatus.)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcvalidintervals
            
            	The number of previous 15\-minute intervals  for which data was collected.   An agent with PW capability must be capable of supporting at   least n intervals. The minimum value of n is 4, The default   of n is 32 and the maximum value of n is 96.  The value will be <n> unless the measurement was (re\-)   started within the last (<n>\*15) minutes, in which case the   value will be the number of complete 15 minute intervals for   which the agent has at least some data. In certain cases   (e.g., in the case where the agent is a proxy) it is   possible that some intervals are unavailable.  In this case,   this interval is the maximum interval number for which data   is available. 
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcadminstatus = None
                self.cpwvccontrolword = None
                self.cpwvccreatetime = None
                self.cpwvcdescr = None
                self.cpwvcholdingpriority = None
                self.cpwvcid = None
                self.cpwvcinboundmode = None
                self.cpwvcinboundoperstatus = None
                self.cpwvcinboundvclabel = None
                self.cpwvclocalgroupid = None
                self.cpwvclocalifmtu = None
                self.cpwvclocalifstring = None
                self.cpwvcname = None
                self.cpwvcoperstatus = None
                self.cpwvcoutboundoperstatus = None
                self.cpwvcoutboundvclabel = None
                self.cpwvcowner = None
                self.cpwvcpeeraddr = None
                self.cpwvcpeeraddrtype = None
                self.cpwvcpsntype = None
                self.cpwvcremotecontrolword = None
                self.cpwvcremotegroupid = None
                self.cpwvcremoteifmtu = None
                self.cpwvcremoteifstring = None
                self.cpwvcrowstatus = None
                self.cpwvcsetuppriority = None
                self.cpwvcstoragetype = None
                self.cpwvctimeelapsed = None
                self.cpwvctype = None
                self.cpwvcuptime = None
                self.cpwvcvalidintervals = None

            class CpwvcadminstatusEnum(Enum):
                """
                CpwvcadminstatusEnum

                The desired operational status of this VC.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = 1

                down = 2

                testing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                    return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcadminstatusEnum']


            class CpwvcinboundmodeEnum(Enum):
                """
                CpwvcinboundmodeEnum

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

                loose = 1

                strict = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                    return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcinboundmodeEnum']


            class CpwvcownerEnum(Enum):
                """
                CpwvcownerEnum

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

                manual = 1

                maintenanceProtocol = 2

                other = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                    return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcownerEnum']


            class CpwvcpsntypeEnum(Enum):
                """
                CpwvcpsntypeEnum

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

                mpls = 1

                l2tp = 2

                ip = 3

                mplsOverIp = 4

                gre = 5

                other = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                    return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcpsntypeEnum']


            class CpwvcremotecontrolwordEnum(Enum):
                """
                CpwvcremotecontrolwordEnum

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

                noControlWord = 1

                withControlWord = 2

                notYetKnown = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                    return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcremotecontrolwordEnum']


            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcTable/CISCO-IETF-PW-MIB:cpwVcEntry[CISCO-IETF-PW-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcadminstatus is not None:
                    return True

                if self.cpwvccontrolword is not None:
                    return True

                if self.cpwvccreatetime is not None:
                    return True

                if self.cpwvcdescr is not None:
                    return True

                if self.cpwvcholdingpriority is not None:
                    return True

                if self.cpwvcid is not None:
                    return True

                if self.cpwvcinboundmode is not None:
                    return True

                if self.cpwvcinboundoperstatus is not None:
                    return True

                if self.cpwvcinboundvclabel is not None:
                    return True

                if self.cpwvclocalgroupid is not None:
                    return True

                if self.cpwvclocalifmtu is not None:
                    return True

                if self.cpwvclocalifstring is not None:
                    return True

                if self.cpwvcname is not None:
                    return True

                if self.cpwvcoperstatus is not None:
                    return True

                if self.cpwvcoutboundoperstatus is not None:
                    return True

                if self.cpwvcoutboundvclabel is not None:
                    return True

                if self.cpwvcowner is not None:
                    return True

                if self.cpwvcpeeraddr is not None:
                    return True

                if self.cpwvcpeeraddrtype is not None:
                    return True

                if self.cpwvcpsntype is not None:
                    return True

                if self.cpwvcremotecontrolword is not None:
                    return True

                if self.cpwvcremotegroupid is not None:
                    return True

                if self.cpwvcremoteifmtu is not None:
                    return True

                if self.cpwvcremoteifstring is not None:
                    return True

                if self.cpwvcrowstatus is not None:
                    return True

                if self.cpwvcsetuppriority is not None:
                    return True

                if self.cpwvcstoragetype is not None:
                    return True

                if self.cpwvctimeelapsed is not None:
                    return True

                if self.cpwvctype is not None:
                    return True

                if self.cpwvcuptime is not None:
                    return True

                if self.cpwvcvalidintervals is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcentry is not None:
                for child_ref in self.cpwvcentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvctable']['meta_info']


    class Cpwvcperfcurrenttable(object):
        """
        This table provides per\-VC performance information for the  
        current interval.
        
        .. attribute:: cpwvcperfcurrententry
        
        	An entry in this table is created by the agent for  every VC
        	**type**\: list of    :py:class:`Cpwvcperfcurrententry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcperfcurrententry = YList()
            self.cpwvcperfcurrententry.parent = self
            self.cpwvcperfcurrententry.name = 'cpwvcperfcurrententry'


        class Cpwvcperfcurrententry(object):
            """
            An entry in this table is created by the agent for 
            every VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperfcurrentinhcbytes
            
            	High capacity counter for number of bytes received  by the VC (from the PSN) in the current 15 minute  interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentinhcpackets
            
            	High capacity counter for number of packets received  by the VC (from the PSN) in the current 15 minute  interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentouthcbytes
            
            	High capacity counter for number of bytes forwarded  by the VC (to the PSN) in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfcurrentouthcpackets
            
            	High capacity counter for number of packets forwarded  by the VC (to the PSN) in the current 15 minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcperfcurrentinhcbytes = None
                self.cpwvcperfcurrentinhcpackets = None
                self.cpwvcperfcurrentouthcbytes = None
                self.cpwvcperfcurrentouthcpackets = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfCurrentTable/CISCO-IETF-PW-MIB:cpwVcPerfCurrentEntry[CISCO-IETF-PW-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcperfcurrentinhcbytes is not None:
                    return True

                if self.cpwvcperfcurrentinhcpackets is not None:
                    return True

                if self.cpwvcperfcurrentouthcbytes is not None:
                    return True

                if self.cpwvcperfcurrentouthcpackets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcperfcurrententry is not None:
                for child_ref in self.cpwvcperfcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcperfcurrenttable']['meta_info']


    class Cpwvcperfintervaltable(object):
        """
        This table provides per\-VC performance information for  
        each interval.
        
        .. attribute:: cpwvcperfintervalentry
        
        	An entry in this table is created agent for every VC
        	**type**\: list of    :py:class:`Cpwvcperfintervalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcperfintervalentry = YList()
            self.cpwvcperfintervalentry.parent = self
            self.cpwvcperfintervalentry.name = 'cpwvcperfintervalentry'


        class Cpwvcperfintervalentry(object):
            """
            An entry in this table is created agent for every VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperfintervalnumber  <key>
            
            	A number N, between 1 and 96, which identifies the  interval for which the set of statistics is available.  The interval identified by 1 is the most recently  completed 15 minute interval, and the interval identified  by N is the interval immediately preceding the one  identified by N\-1.  The minimum range of N is 1 through 4. The default range  is 1 to 32. The maximum range of N is 1 through 96. 
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: cpwvcperfintervalinhcbytes
            
            	High capacity counter for number of bytes received by the   VC (from the PSN) in a particular 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalinhcpackets
            
            	High capacity counter for number of packets received by  the VC (from the PSN) in a particular 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalouthcbytes
            
            	High capacity counter for number of bytes forwarded by the   VC (to the PSN) in a particular 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervalouthcpackets
            
            	High capacity counter for number of packets forwarded by   the VC (to the PSN) in a particular 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperfintervaltimeelapsed
            
            	The duration of a particular interval in seconds.  Adjustments in the system's time\-of\-day clock, may  cause the interval to be greater or less than the  normal value. Therefore this actual interval value  is provided
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwvcperfintervalvaliddata
            
            	This variable indicates if the data for this interval  is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcperfintervalnumber = None
                self.cpwvcperfintervalinhcbytes = None
                self.cpwvcperfintervalinhcpackets = None
                self.cpwvcperfintervalouthcbytes = None
                self.cpwvcperfintervalouthcpackets = None
                self.cpwvcperfintervaltimeelapsed = None
                self.cpwvcperfintervalvaliddata = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwvcperfintervalnumber is None:
                    raise YPYModelError('Key property cpwvcperfintervalnumber is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfIntervalTable/CISCO-IETF-PW-MIB:cpwVcPerfIntervalEntry[CISCO-IETF-PW-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-MIB:cpwVcPerfIntervalNumber = ' + str(self.cpwvcperfintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcperfintervalnumber is not None:
                    return True

                if self.cpwvcperfintervalinhcbytes is not None:
                    return True

                if self.cpwvcperfintervalinhcpackets is not None:
                    return True

                if self.cpwvcperfintervalouthcbytes is not None:
                    return True

                if self.cpwvcperfintervalouthcpackets is not None:
                    return True

                if self.cpwvcperfintervaltimeelapsed is not None:
                    return True

                if self.cpwvcperfintervalvaliddata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcperfintervalentry is not None:
                for child_ref in self.cpwvcperfintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcperfintervaltable']['meta_info']


    class Cpwvcperftotaltable(object):
        """
        This table provides per\-VC Performance information from VC  
        start time.
        
        .. attribute:: cpwvcperftotalentry
        
        	An entry in this table is created agent for every VC
        	**type**\: list of    :py:class:`Cpwvcperftotalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcperftotalentry = YList()
            self.cpwvcperftotalentry.parent = self
            self.cpwvcperftotalentry.name = 'cpwvcperftotalentry'


        class Cpwvcperftotalentry(object):
            """
            An entry in this table is created agent for every VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcperftotaldiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at  which any one or more of this row Counter32 or  Counter64 suffered a discontinuity. If no such  discontinuities have occurred since the last re\-  initialization of the local management subsystem, then  this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcperftotalinhcbytes
            
            	High capacity counter for number of bytes received by the   VC (from the PSN)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalinhcpackets
            
            	High capacity counter for number of packets received by the   VC (from the PSN)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalouthcbytes
            
            	High capacity counter for number of bytes forwarded by the   VC (to the PSN)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcperftotalouthcpackets
            
            	High capacity counter for number of packets forwarded by   the VC (to the PSN)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcperftotaldiscontinuitytime = None
                self.cpwvcperftotalinhcbytes = None
                self.cpwvcperftotalinhcpackets = None
                self.cpwvcperftotalouthcbytes = None
                self.cpwvcperftotalouthcpackets = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfTotalTable/CISCO-IETF-PW-MIB:cpwVcPerfTotalEntry[CISCO-IETF-PW-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcperftotaldiscontinuitytime is not None:
                    return True

                if self.cpwvcperftotalinhcbytes is not None:
                    return True

                if self.cpwvcperftotalinhcpackets is not None:
                    return True

                if self.cpwvcperftotalouthcbytes is not None:
                    return True

                if self.cpwvcperftotalouthcpackets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPerfTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcperftotalentry is not None:
                for child_ref in self.cpwvcperftotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcperftotaltable']['meta_info']


    class Cpwvcidmappingtable(object):
        """
        This table provides reverse mapping of the existing VCs  
        based on vc type and VC ID ordering. This table is  
        typically useful for EMS ordered query of existing VCs.
        
        .. attribute:: cpwvcidmappingentry
        
        	An entry in this table is created by the agent for every   VC configured by the cpwVcTable
        	**type**\: list of    :py:class:`Cpwvcidmappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcidmappingentry = YList()
            self.cpwvcidmappingentry.parent = self
            self.cpwvcidmappingentry.name = 'cpwvcidmappingentry'


        class Cpwvcidmappingentry(object):
            """
            An entry in this table is created by the agent for every  
            VC configured by the cpwVcTable.
            
            .. attribute:: cpwvcidmappingvctype  <key>
            
            	The VC type (indicate the service) of this VC
            	**type**\:   :py:class:`CpwvctypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwvctypeEnum>`
            
            .. attribute:: cpwvcidmappingvcid  <key>
            
            	The VC ID of this VC. Zero if the VC is configured   manually
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcidmappingpeeraddrtype  <key>
            
            	IP address type of the peer node
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cpwvcidmappingpeeraddr  <key>
            
            	IP address type of the peer node
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcidmappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcidmappingvctype = None
                self.cpwvcidmappingvcid = None
                self.cpwvcidmappingpeeraddrtype = None
                self.cpwvcidmappingpeeraddr = None
                self.cpwvcidmappingvcindex = None

            @property
            def _common_path(self):
                if self.cpwvcidmappingvctype is None:
                    raise YPYModelError('Key property cpwvcidmappingvctype is None')
                if self.cpwvcidmappingvcid is None:
                    raise YPYModelError('Key property cpwvcidmappingvcid is None')
                if self.cpwvcidmappingpeeraddrtype is None:
                    raise YPYModelError('Key property cpwvcidmappingpeeraddrtype is None')
                if self.cpwvcidmappingpeeraddr is None:
                    raise YPYModelError('Key property cpwvcidmappingpeeraddr is None')
                if self.cpwvcidmappingvcindex is None:
                    raise YPYModelError('Key property cpwvcidmappingvcindex is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcIdMappingTable/CISCO-IETF-PW-MIB:cpwVcIdMappingEntry[CISCO-IETF-PW-MIB:cpwVcIdMappingVcType = ' + str(self.cpwvcidmappingvctype) + '][CISCO-IETF-PW-MIB:cpwVcIdMappingVcID = ' + str(self.cpwvcidmappingvcid) + '][CISCO-IETF-PW-MIB:cpwVcIdMappingPeerAddrType = ' + str(self.cpwvcidmappingpeeraddrtype) + '][CISCO-IETF-PW-MIB:cpwVcIdMappingPeerAddr = ' + str(self.cpwvcidmappingpeeraddr) + '][CISCO-IETF-PW-MIB:cpwVcIdMappingVcIndex = ' + str(self.cpwvcidmappingvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcidmappingvctype is not None:
                    return True

                if self.cpwvcidmappingvcid is not None:
                    return True

                if self.cpwvcidmappingpeeraddrtype is not None:
                    return True

                if self.cpwvcidmappingpeeraddr is not None:
                    return True

                if self.cpwvcidmappingvcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcIdMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcidmappingentry is not None:
                for child_ref in self.cpwvcidmappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcidmappingtable']['meta_info']


    class Cpwvcpeermappingtable(object):
        """
        This table provides reverse mapping of the existing VCs  
        based on vc type and VC ID ordering. This table is  
        typically useful for EMS ordered query of existing VCs.
        
        .. attribute:: cpwvcpeermappingentry
        
        	An entry in this table is created by the agent for every   VC configured in cpwVcTable
        	**type**\: list of    :py:class:`Cpwvcpeermappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MIB'
        _revision = '2004-03-17'

        def __init__(self):
            self.parent = None
            self.cpwvcpeermappingentry = YList()
            self.cpwvcpeermappingentry.parent = self
            self.cpwvcpeermappingentry.name = 'cpwvcpeermappingentry'


        class Cpwvcpeermappingentry(object):
            """
            An entry in this table is created by the agent for every  
            VC configured in cpwVcTable.
            
            .. attribute:: cpwvcpeermappingpeeraddrtype  <key>
            
            	IP address type of the peer node
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cpwvcpeermappingpeeraddr  <key>
            
            	IP address type of the peer node
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcpeermappingvctype  <key>
            
            	The VC type (indicate the service) of this VC
            	**type**\:   :py:class:`CpwvctypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.CpwvctypeEnum>`
            
            .. attribute:: cpwvcpeermappingvcid  <key>
            
            	The VC ID of this VC. Zero if the VC is configured   manually
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcpeermappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MIB'
            _revision = '2004-03-17'

            def __init__(self):
                self.parent = None
                self.cpwvcpeermappingpeeraddrtype = None
                self.cpwvcpeermappingpeeraddr = None
                self.cpwvcpeermappingvctype = None
                self.cpwvcpeermappingvcid = None
                self.cpwvcpeermappingvcindex = None

            @property
            def _common_path(self):
                if self.cpwvcpeermappingpeeraddrtype is None:
                    raise YPYModelError('Key property cpwvcpeermappingpeeraddrtype is None')
                if self.cpwvcpeermappingpeeraddr is None:
                    raise YPYModelError('Key property cpwvcpeermappingpeeraddr is None')
                if self.cpwvcpeermappingvctype is None:
                    raise YPYModelError('Key property cpwvcpeermappingvctype is None')
                if self.cpwvcpeermappingvcid is None:
                    raise YPYModelError('Key property cpwvcpeermappingvcid is None')
                if self.cpwvcpeermappingvcindex is None:
                    raise YPYModelError('Key property cpwvcpeermappingvcindex is None')

                return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPeerMappingTable/CISCO-IETF-PW-MIB:cpwVcPeerMappingEntry[CISCO-IETF-PW-MIB:cpwVcPeerMappingPeerAddrType = ' + str(self.cpwvcpeermappingpeeraddrtype) + '][CISCO-IETF-PW-MIB:cpwVcPeerMappingPeerAddr = ' + str(self.cpwvcpeermappingpeeraddr) + '][CISCO-IETF-PW-MIB:cpwVcPeerMappingVcType = ' + str(self.cpwvcpeermappingvctype) + '][CISCO-IETF-PW-MIB:cpwVcPeerMappingVcID = ' + str(self.cpwvcpeermappingvcid) + '][CISCO-IETF-PW-MIB:cpwVcPeerMappingVcIndex = ' + str(self.cpwvcpeermappingvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcpeermappingpeeraddrtype is not None:
                    return True

                if self.cpwvcpeermappingpeeraddr is not None:
                    return True

                if self.cpwvcpeermappingvctype is not None:
                    return True

                if self.cpwvcpeermappingvcid is not None:
                    return True

                if self.cpwvcpeermappingvcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
                return meta._meta_table['CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/CISCO-IETF-PW-MIB:cpwVcPeerMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcpeermappingentry is not None:
                for child_ref in self.cpwvcpeermappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
            return meta._meta_table['CiscoIetfPwMib.Cpwvcpeermappingtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpwvcidmappingtable is not None and self.cpwvcidmappingtable._has_data():
            return True

        if self.cpwvcobjects is not None and self.cpwvcobjects._has_data():
            return True

        if self.cpwvcpeermappingtable is not None and self.cpwvcpeermappingtable._has_data():
            return True

        if self.cpwvcperfcurrenttable is not None and self.cpwvcperfcurrenttable._has_data():
            return True

        if self.cpwvcperfintervaltable is not None and self.cpwvcperfintervaltable._has_data():
            return True

        if self.cpwvcperftotaltable is not None and self.cpwvcperftotaltable._has_data():
            return True

        if self.cpwvctable is not None and self.cpwvctable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MIB as meta
        return meta._meta_table['CiscoIetfPwMib']['meta_info']


