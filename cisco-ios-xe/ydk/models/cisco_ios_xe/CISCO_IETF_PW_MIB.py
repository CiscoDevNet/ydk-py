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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfPwMib(Entity):
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
        super(CiscoIetfPwMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-MIB"

        self.cpwvcidmappingtable = CiscoIetfPwMib.Cpwvcidmappingtable()
        self.cpwvcidmappingtable.parent = self
        self._children_name_map["cpwvcidmappingtable"] = "cpwVcIdMappingTable"
        self._children_yang_names.add("cpwVcIdMappingTable")

        self.cpwvcobjects = CiscoIetfPwMib.Cpwvcobjects()
        self.cpwvcobjects.parent = self
        self._children_name_map["cpwvcobjects"] = "cpwVcObjects"
        self._children_yang_names.add("cpwVcObjects")

        self.cpwvcpeermappingtable = CiscoIetfPwMib.Cpwvcpeermappingtable()
        self.cpwvcpeermappingtable.parent = self
        self._children_name_map["cpwvcpeermappingtable"] = "cpwVcPeerMappingTable"
        self._children_yang_names.add("cpwVcPeerMappingTable")

        self.cpwvcperfcurrenttable = CiscoIetfPwMib.Cpwvcperfcurrenttable()
        self.cpwvcperfcurrenttable.parent = self
        self._children_name_map["cpwvcperfcurrenttable"] = "cpwVcPerfCurrentTable"
        self._children_yang_names.add("cpwVcPerfCurrentTable")

        self.cpwvcperfintervaltable = CiscoIetfPwMib.Cpwvcperfintervaltable()
        self.cpwvcperfintervaltable.parent = self
        self._children_name_map["cpwvcperfintervaltable"] = "cpwVcPerfIntervalTable"
        self._children_yang_names.add("cpwVcPerfIntervalTable")

        self.cpwvcperftotaltable = CiscoIetfPwMib.Cpwvcperftotaltable()
        self.cpwvcperftotaltable.parent = self
        self._children_name_map["cpwvcperftotaltable"] = "cpwVcPerfTotalTable"
        self._children_yang_names.add("cpwVcPerfTotalTable")

        self.cpwvctable = CiscoIetfPwMib.Cpwvctable()
        self.cpwvctable.parent = self
        self._children_name_map["cpwvctable"] = "cpwVcTable"
        self._children_yang_names.add("cpwVcTable")


    class Cpwvcobjects(Entity):
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
            super(CiscoIetfPwMib.Cpwvcobjects, self).__init__()

            self.yang_name = "cpwVcObjects"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcindexnext = YLeaf(YType.uint32, "cpwVcIndexNext")

            self.cpwvcnotifrate = YLeaf(YType.uint32, "cpwVcNotifRate")

            self.cpwvcperftotalerrorpackets = YLeaf(YType.uint64, "cpwVcPerfTotalErrorPackets")

            self.cpwvcupdownnotifenable = YLeaf(YType.boolean, "cpwVcUpDownNotifEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpwvcindexnext",
                            "cpwvcnotifrate",
                            "cpwvcperftotalerrorpackets",
                            "cpwvcupdownnotifenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfPwMib.Cpwvcobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cpwvcindexnext.is_set or
                self.cpwvcnotifrate.is_set or
                self.cpwvcperftotalerrorpackets.is_set or
                self.cpwvcupdownnotifenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpwvcindexnext.yfilter != YFilter.not_set or
                self.cpwvcnotifrate.yfilter != YFilter.not_set or
                self.cpwvcperftotalerrorpackets.yfilter != YFilter.not_set or
                self.cpwvcupdownnotifenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpwvcindexnext.is_set or self.cpwvcindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcindexnext.get_name_leafdata())
            if (self.cpwvcnotifrate.is_set or self.cpwvcnotifrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcnotifrate.get_name_leafdata())
            if (self.cpwvcperftotalerrorpackets.is_set or self.cpwvcperftotalerrorpackets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcperftotalerrorpackets.get_name_leafdata())
            if (self.cpwvcupdownnotifenable.is_set or self.cpwvcupdownnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcupdownnotifenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcIndexNext" or name == "cpwVcNotifRate" or name == "cpwVcPerfTotalErrorPackets" or name == "cpwVcUpDownNotifEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpwVcIndexNext"):
                self.cpwvcindexnext = value
                self.cpwvcindexnext.value_namespace = name_space
                self.cpwvcindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "cpwVcNotifRate"):
                self.cpwvcnotifrate = value
                self.cpwvcnotifrate.value_namespace = name_space
                self.cpwvcnotifrate.value_namespace_prefix = name_space_prefix
            if(value_path == "cpwVcPerfTotalErrorPackets"):
                self.cpwvcperftotalerrorpackets = value
                self.cpwvcperftotalerrorpackets.value_namespace = name_space
                self.cpwvcperftotalerrorpackets.value_namespace_prefix = name_space_prefix
            if(value_path == "cpwVcUpDownNotifEnable"):
                self.cpwvcupdownnotifenable = value
                self.cpwvcupdownnotifenable.value_namespace = name_space
                self.cpwvcupdownnotifenable.value_namespace_prefix = name_space_prefix


    class Cpwvctable(Entity):
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
            super(CiscoIetfPwMib.Cpwvctable, self).__init__()

            self.yang_name = "cpwVcTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcentry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvctable, self).__setattr__(name, value)


        class Cpwvcentry(Entity):
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
            	**type**\:   :py:class:`Cpwvcadminstatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.Cpwvcadminstatus>`
            
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
            	**type**\:   :py:class:`Cpwvcinboundmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.Cpwvcinboundmode>`
            
            .. attribute:: cpwvcinboundoperstatus
            
            	Indicates the actual operational status of this VC in the   inbound direction.   \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                     passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:   :py:class:`Cpwoperstatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwoperstatus>`
            
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
            	**type**\:   :py:class:`Cpwoperstatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwoperstatus>`
            
            .. attribute:: cpwvcoutboundoperstatus
            
            	Indicates the actual operational status of this VC in the   outbound direction  \- down\:           if PW signaling has not yet finished, or                    indications available at the service                     level indicate that the VC is not                    passing packets.  \- testing\:        if AdminStatus at the VC level is set to                     test.  \- dormant\:        The VC is not available because of the                    required resources are occupied VC with                     higher priority VCs .  \- notPresent\:     Some component is missing to accomplish                     the set up of the VC.  \- lowerLayerDown\: The underlying PSN is not in OperStatus                     'up'.  
            	**type**\:   :py:class:`Cpwoperstatus <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwoperstatus>`
            
            .. attribute:: cpwvcoutboundvclabel
            
            	The VC label used in the outbound direction (i.e. toward   the PSN). It may be set up manually if owner is 'manual' or   automatically otherwise. Examples\: For MPLS PSN, it   represents the 20 bits of VC tag, for L2TP it represent the  32 bits Session ID.  If the label is not yet known (signaling in process), the   object should return a value of 0xFFFF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcowner
            
            	Set by the operator to indicate the protocol responsible   for establishing this VC. Value 'manual' is used in all  cases where no maintenance protocol (PW signaling) is used   to set\-up the VC, i.e. require configuration of entries in  the VC tables including VC labels, etc. The value   'maintenanceProtocol' is used in case of standard  signaling of the VC for the specific PSN, for example LDP  for MPLS PSN as specified in <draft\- draft\-martini\-  l2circuit\-trans\-mpls> or L2TP control protocol.   Value 'other' is used for other types of signaling
            	**type**\:   :py:class:`Cpwvcowner <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.Cpwvcowner>`
            
            .. attribute:: cpwvcpeeraddr
            
            	This object contains the value of of the peer node address  of the PW/PE maintenance protocol entity. This object   should contain a value of 0 if not relevant (manual   configuration of the VC)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcpeeraddrtype
            
            	Denotes the address type of the peer node maintenance  protocol (signaling) address if PW maintenance protocol is  used for the VC creation. It should be set to   'unknown' if PE/PW maintenance protocol is not used,   i.e. cpwVcOwner is set to 'manual'. 
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cpwvcpsntype
            
            	Set by the operator to indicate the PSN type on which this   VC will be carried. Based on this object, the relevant PSN   table entries are created in the in the PSN specific MIB   modules. For example, if mpls(1) is defined, the agent   create an entry in cpwVcMplsTable, which further define the   MPLS PSN configuration.  Note\: the exact set of PSN types is yet to be worked   out by the WG. 
            	**type**\:   :py:class:`Cpwvcpsntype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.Cpwvcpsntype>`
            
            .. attribute:: cpwvcremotecontrolword
            
            	If maintenance protocol is used for VC establishment, this   parameter indicates the received status of the control word   usage, i.e. if packets will be received with control word  or not. The value of 'notYetKnown' is used while the  maintenance protocol has not yet received the indication   from the remote node.  In manual configuration of the VC this parameters indicate   to the local node what is the expected encapsulation for  the received packets. 
            	**type**\:   :py:class:`Cpwvcremotecontrolword <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry.Cpwvcremotecontrolword>`
            
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwvcsetuppriority
            
            	This object define the relative set\-up priority of the VC    in a lowest\-to\-highest fashion, where 0 is the highest   priority. VCs with the same priority are treated with  equal priority. Dropped VC will be set 'dormant' (as  indicated in cpwVcOperStatus).  This value is significant if there are competing resources  between VCs and the implementation support this feature.  If not supported or not relevant, the value of zero MUST  be used
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcstoragetype
            
            	This variable indicates the storage type for this  object
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwvctimeelapsed
            
            	The number of seconds, including partial seconds,  that have elapsed since the beginning of the current  measurement period. If, for some reason, such as an  adjustment in the system's time\-of\-day clock, the  current interval exceeds the maximum value, the  agent will return the maximum value
            	**type**\:  int
            
            	**range:** 1..900
            
            .. attribute:: cpwvctype
            
            	This value indicate the service to be carried over  this VC.   Note\: the exact set of VC types is yet to be worked   out by the WG. 
            	**type**\:   :py:class:`Cpwvctype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwvctype>`
            
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
                super(CiscoIetfPwMib.Cpwvctable.Cpwvcentry, self).__init__()

                self.yang_name = "cpwVcEntry"
                self.yang_parent_name = "cpwVcTable"

                self.cpwvcindex = YLeaf(YType.uint32, "cpwVcIndex")

                self.cpwvcadminstatus = YLeaf(YType.enumeration, "cpwVcAdminStatus")

                self.cpwvccontrolword = YLeaf(YType.boolean, "cpwVcControlWord")

                self.cpwvccreatetime = YLeaf(YType.uint32, "cpwVcCreateTime")

                self.cpwvcdescr = YLeaf(YType.str, "cpwVcDescr")

                self.cpwvcholdingpriority = YLeaf(YType.int32, "cpwVcHoldingPriority")

                self.cpwvcid = YLeaf(YType.uint32, "cpwVcID")

                self.cpwvcinboundmode = YLeaf(YType.enumeration, "cpwVcInboundMode")

                self.cpwvcinboundoperstatus = YLeaf(YType.enumeration, "cpwVcInboundOperStatus")

                self.cpwvcinboundvclabel = YLeaf(YType.uint32, "cpwVcInboundVcLabel")

                self.cpwvclocalgroupid = YLeaf(YType.uint32, "cpwVcLocalGroupID")

                self.cpwvclocalifmtu = YLeaf(YType.uint32, "cpwVcLocalIfMtu")

                self.cpwvclocalifstring = YLeaf(YType.boolean, "cpwVcLocalIfString")

                self.cpwvcname = YLeaf(YType.str, "cpwVcName")

                self.cpwvcoperstatus = YLeaf(YType.enumeration, "cpwVcOperStatus")

                self.cpwvcoutboundoperstatus = YLeaf(YType.enumeration, "cpwVcOutboundOperStatus")

                self.cpwvcoutboundvclabel = YLeaf(YType.uint32, "cpwVcOutboundVcLabel")

                self.cpwvcowner = YLeaf(YType.enumeration, "cpwVcOwner")

                self.cpwvcpeeraddr = YLeaf(YType.str, "cpwVcPeerAddr")

                self.cpwvcpeeraddrtype = YLeaf(YType.enumeration, "cpwVcPeerAddrType")

                self.cpwvcpsntype = YLeaf(YType.enumeration, "cpwVcPsnType")

                self.cpwvcremotecontrolword = YLeaf(YType.enumeration, "cpwVcRemoteControlWord")

                self.cpwvcremotegroupid = YLeaf(YType.uint32, "cpwVcRemoteGroupID")

                self.cpwvcremoteifmtu = YLeaf(YType.uint32, "cpwVcRemoteIfMtu")

                self.cpwvcremoteifstring = YLeaf(YType.str, "cpwVcRemoteIfString")

                self.cpwvcrowstatus = YLeaf(YType.enumeration, "cpwVcRowStatus")

                self.cpwvcsetuppriority = YLeaf(YType.int32, "cpwVcSetUpPriority")

                self.cpwvcstoragetype = YLeaf(YType.enumeration, "cpwVcStorageType")

                self.cpwvctimeelapsed = YLeaf(YType.int32, "cpwVcTimeElapsed")

                self.cpwvctype = YLeaf(YType.enumeration, "cpwVcType")

                self.cpwvcuptime = YLeaf(YType.uint32, "cpwVcUpTime")

                self.cpwvcvalidintervals = YLeaf(YType.int32, "cpwVcValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwvcadminstatus",
                                "cpwvccontrolword",
                                "cpwvccreatetime",
                                "cpwvcdescr",
                                "cpwvcholdingpriority",
                                "cpwvcid",
                                "cpwvcinboundmode",
                                "cpwvcinboundoperstatus",
                                "cpwvcinboundvclabel",
                                "cpwvclocalgroupid",
                                "cpwvclocalifmtu",
                                "cpwvclocalifstring",
                                "cpwvcname",
                                "cpwvcoperstatus",
                                "cpwvcoutboundoperstatus",
                                "cpwvcoutboundvclabel",
                                "cpwvcowner",
                                "cpwvcpeeraddr",
                                "cpwvcpeeraddrtype",
                                "cpwvcpsntype",
                                "cpwvcremotecontrolword",
                                "cpwvcremotegroupid",
                                "cpwvcremoteifmtu",
                                "cpwvcremoteifstring",
                                "cpwvcrowstatus",
                                "cpwvcsetuppriority",
                                "cpwvcstoragetype",
                                "cpwvctimeelapsed",
                                "cpwvctype",
                                "cpwvcuptime",
                                "cpwvcvalidintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvctable.Cpwvcentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvctable.Cpwvcentry, self).__setattr__(name, value)

            class Cpwvcadminstatus(Enum):
                """
                Cpwvcadminstatus

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
                Cpwvcinboundmode

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
                Cpwvcowner

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
                Cpwvcpsntype

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
                Cpwvcremotecontrolword

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


            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcadminstatus.is_set or
                    self.cpwvccontrolword.is_set or
                    self.cpwvccreatetime.is_set or
                    self.cpwvcdescr.is_set or
                    self.cpwvcholdingpriority.is_set or
                    self.cpwvcid.is_set or
                    self.cpwvcinboundmode.is_set or
                    self.cpwvcinboundoperstatus.is_set or
                    self.cpwvcinboundvclabel.is_set or
                    self.cpwvclocalgroupid.is_set or
                    self.cpwvclocalifmtu.is_set or
                    self.cpwvclocalifstring.is_set or
                    self.cpwvcname.is_set or
                    self.cpwvcoperstatus.is_set or
                    self.cpwvcoutboundoperstatus.is_set or
                    self.cpwvcoutboundvclabel.is_set or
                    self.cpwvcowner.is_set or
                    self.cpwvcpeeraddr.is_set or
                    self.cpwvcpeeraddrtype.is_set or
                    self.cpwvcpsntype.is_set or
                    self.cpwvcremotecontrolword.is_set or
                    self.cpwvcremotegroupid.is_set or
                    self.cpwvcremoteifmtu.is_set or
                    self.cpwvcremoteifstring.is_set or
                    self.cpwvcrowstatus.is_set or
                    self.cpwvcsetuppriority.is_set or
                    self.cpwvcstoragetype.is_set or
                    self.cpwvctimeelapsed.is_set or
                    self.cpwvctype.is_set or
                    self.cpwvcuptime.is_set or
                    self.cpwvcvalidintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcadminstatus.yfilter != YFilter.not_set or
                    self.cpwvccontrolword.yfilter != YFilter.not_set or
                    self.cpwvccreatetime.yfilter != YFilter.not_set or
                    self.cpwvcdescr.yfilter != YFilter.not_set or
                    self.cpwvcholdingpriority.yfilter != YFilter.not_set or
                    self.cpwvcid.yfilter != YFilter.not_set or
                    self.cpwvcinboundmode.yfilter != YFilter.not_set or
                    self.cpwvcinboundoperstatus.yfilter != YFilter.not_set or
                    self.cpwvcinboundvclabel.yfilter != YFilter.not_set or
                    self.cpwvclocalgroupid.yfilter != YFilter.not_set or
                    self.cpwvclocalifmtu.yfilter != YFilter.not_set or
                    self.cpwvclocalifstring.yfilter != YFilter.not_set or
                    self.cpwvcname.yfilter != YFilter.not_set or
                    self.cpwvcoperstatus.yfilter != YFilter.not_set or
                    self.cpwvcoutboundoperstatus.yfilter != YFilter.not_set or
                    self.cpwvcoutboundvclabel.yfilter != YFilter.not_set or
                    self.cpwvcowner.yfilter != YFilter.not_set or
                    self.cpwvcpeeraddr.yfilter != YFilter.not_set or
                    self.cpwvcpeeraddrtype.yfilter != YFilter.not_set or
                    self.cpwvcpsntype.yfilter != YFilter.not_set or
                    self.cpwvcremotecontrolword.yfilter != YFilter.not_set or
                    self.cpwvcremotegroupid.yfilter != YFilter.not_set or
                    self.cpwvcremoteifmtu.yfilter != YFilter.not_set or
                    self.cpwvcremoteifstring.yfilter != YFilter.not_set or
                    self.cpwvcrowstatus.yfilter != YFilter.not_set or
                    self.cpwvcsetuppriority.yfilter != YFilter.not_set or
                    self.cpwvcstoragetype.yfilter != YFilter.not_set or
                    self.cpwvctimeelapsed.yfilter != YFilter.not_set or
                    self.cpwvctype.yfilter != YFilter.not_set or
                    self.cpwvcuptime.yfilter != YFilter.not_set or
                    self.cpwvcvalidintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcadminstatus.is_set or self.cpwvcadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcadminstatus.get_name_leafdata())
                if (self.cpwvccontrolword.is_set or self.cpwvccontrolword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvccontrolword.get_name_leafdata())
                if (self.cpwvccreatetime.is_set or self.cpwvccreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvccreatetime.get_name_leafdata())
                if (self.cpwvcdescr.is_set or self.cpwvcdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcdescr.get_name_leafdata())
                if (self.cpwvcholdingpriority.is_set or self.cpwvcholdingpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcholdingpriority.get_name_leafdata())
                if (self.cpwvcid.is_set or self.cpwvcid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcid.get_name_leafdata())
                if (self.cpwvcinboundmode.is_set or self.cpwvcinboundmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcinboundmode.get_name_leafdata())
                if (self.cpwvcinboundoperstatus.is_set or self.cpwvcinboundoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcinboundoperstatus.get_name_leafdata())
                if (self.cpwvcinboundvclabel.is_set or self.cpwvcinboundvclabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcinboundvclabel.get_name_leafdata())
                if (self.cpwvclocalgroupid.is_set or self.cpwvclocalgroupid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvclocalgroupid.get_name_leafdata())
                if (self.cpwvclocalifmtu.is_set or self.cpwvclocalifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvclocalifmtu.get_name_leafdata())
                if (self.cpwvclocalifstring.is_set or self.cpwvclocalifstring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvclocalifstring.get_name_leafdata())
                if (self.cpwvcname.is_set or self.cpwvcname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcname.get_name_leafdata())
                if (self.cpwvcoperstatus.is_set or self.cpwvcoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcoperstatus.get_name_leafdata())
                if (self.cpwvcoutboundoperstatus.is_set or self.cpwvcoutboundoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcoutboundoperstatus.get_name_leafdata())
                if (self.cpwvcoutboundvclabel.is_set or self.cpwvcoutboundvclabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcoutboundvclabel.get_name_leafdata())
                if (self.cpwvcowner.is_set or self.cpwvcowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcowner.get_name_leafdata())
                if (self.cpwvcpeeraddr.is_set or self.cpwvcpeeraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeeraddr.get_name_leafdata())
                if (self.cpwvcpeeraddrtype.is_set or self.cpwvcpeeraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeeraddrtype.get_name_leafdata())
                if (self.cpwvcpsntype.is_set or self.cpwvcpsntype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpsntype.get_name_leafdata())
                if (self.cpwvcremotecontrolword.is_set or self.cpwvcremotecontrolword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcremotecontrolword.get_name_leafdata())
                if (self.cpwvcremotegroupid.is_set or self.cpwvcremotegroupid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcremotegroupid.get_name_leafdata())
                if (self.cpwvcremoteifmtu.is_set or self.cpwvcremoteifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcremoteifmtu.get_name_leafdata())
                if (self.cpwvcremoteifstring.is_set or self.cpwvcremoteifstring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcremoteifstring.get_name_leafdata())
                if (self.cpwvcrowstatus.is_set or self.cpwvcrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcrowstatus.get_name_leafdata())
                if (self.cpwvcsetuppriority.is_set or self.cpwvcsetuppriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcsetuppriority.get_name_leafdata())
                if (self.cpwvcstoragetype.is_set or self.cpwvcstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcstoragetype.get_name_leafdata())
                if (self.cpwvctimeelapsed.is_set or self.cpwvctimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvctimeelapsed.get_name_leafdata())
                if (self.cpwvctype.is_set or self.cpwvctype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvctype.get_name_leafdata())
                if (self.cpwvcuptime.is_set or self.cpwvcuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcuptime.get_name_leafdata())
                if (self.cpwvcvalidintervals.is_set or self.cpwvcvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcvalidintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcAdminStatus" or name == "cpwVcControlWord" or name == "cpwVcCreateTime" or name == "cpwVcDescr" or name == "cpwVcHoldingPriority" or name == "cpwVcID" or name == "cpwVcInboundMode" or name == "cpwVcInboundOperStatus" or name == "cpwVcInboundVcLabel" or name == "cpwVcLocalGroupID" or name == "cpwVcLocalIfMtu" or name == "cpwVcLocalIfString" or name == "cpwVcName" or name == "cpwVcOperStatus" or name == "cpwVcOutboundOperStatus" or name == "cpwVcOutboundVcLabel" or name == "cpwVcOwner" or name == "cpwVcPeerAddr" or name == "cpwVcPeerAddrType" or name == "cpwVcPsnType" or name == "cpwVcRemoteControlWord" or name == "cpwVcRemoteGroupID" or name == "cpwVcRemoteIfMtu" or name == "cpwVcRemoteIfString" or name == "cpwVcRowStatus" or name == "cpwVcSetUpPriority" or name == "cpwVcStorageType" or name == "cpwVcTimeElapsed" or name == "cpwVcType" or name == "cpwVcUpTime" or name == "cpwVcValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcAdminStatus"):
                    self.cpwvcadminstatus = value
                    self.cpwvcadminstatus.value_namespace = name_space
                    self.cpwvcadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcControlWord"):
                    self.cpwvccontrolword = value
                    self.cpwvccontrolword.value_namespace = name_space
                    self.cpwvccontrolword.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcCreateTime"):
                    self.cpwvccreatetime = value
                    self.cpwvccreatetime.value_namespace = name_space
                    self.cpwvccreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcDescr"):
                    self.cpwvcdescr = value
                    self.cpwvcdescr.value_namespace = name_space
                    self.cpwvcdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcHoldingPriority"):
                    self.cpwvcholdingpriority = value
                    self.cpwvcholdingpriority.value_namespace = name_space
                    self.cpwvcholdingpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcID"):
                    self.cpwvcid = value
                    self.cpwvcid.value_namespace = name_space
                    self.cpwvcid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcInboundMode"):
                    self.cpwvcinboundmode = value
                    self.cpwvcinboundmode.value_namespace = name_space
                    self.cpwvcinboundmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcInboundOperStatus"):
                    self.cpwvcinboundoperstatus = value
                    self.cpwvcinboundoperstatus.value_namespace = name_space
                    self.cpwvcinboundoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcInboundVcLabel"):
                    self.cpwvcinboundvclabel = value
                    self.cpwvcinboundvclabel.value_namespace = name_space
                    self.cpwvcinboundvclabel.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcLocalGroupID"):
                    self.cpwvclocalgroupid = value
                    self.cpwvclocalgroupid.value_namespace = name_space
                    self.cpwvclocalgroupid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcLocalIfMtu"):
                    self.cpwvclocalifmtu = value
                    self.cpwvclocalifmtu.value_namespace = name_space
                    self.cpwvclocalifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcLocalIfString"):
                    self.cpwvclocalifstring = value
                    self.cpwvclocalifstring.value_namespace = name_space
                    self.cpwvclocalifstring.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcName"):
                    self.cpwvcname = value
                    self.cpwvcname.value_namespace = name_space
                    self.cpwvcname.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcOperStatus"):
                    self.cpwvcoperstatus = value
                    self.cpwvcoperstatus.value_namespace = name_space
                    self.cpwvcoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcOutboundOperStatus"):
                    self.cpwvcoutboundoperstatus = value
                    self.cpwvcoutboundoperstatus.value_namespace = name_space
                    self.cpwvcoutboundoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcOutboundVcLabel"):
                    self.cpwvcoutboundvclabel = value
                    self.cpwvcoutboundvclabel.value_namespace = name_space
                    self.cpwvcoutboundvclabel.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcOwner"):
                    self.cpwvcowner = value
                    self.cpwvcowner.value_namespace = name_space
                    self.cpwvcowner.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerAddr"):
                    self.cpwvcpeeraddr = value
                    self.cpwvcpeeraddr.value_namespace = name_space
                    self.cpwvcpeeraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerAddrType"):
                    self.cpwvcpeeraddrtype = value
                    self.cpwvcpeeraddrtype.value_namespace = name_space
                    self.cpwvcpeeraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPsnType"):
                    self.cpwvcpsntype = value
                    self.cpwvcpsntype.value_namespace = name_space
                    self.cpwvcpsntype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcRemoteControlWord"):
                    self.cpwvcremotecontrolword = value
                    self.cpwvcremotecontrolword.value_namespace = name_space
                    self.cpwvcremotecontrolword.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcRemoteGroupID"):
                    self.cpwvcremotegroupid = value
                    self.cpwvcremotegroupid.value_namespace = name_space
                    self.cpwvcremotegroupid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcRemoteIfMtu"):
                    self.cpwvcremoteifmtu = value
                    self.cpwvcremoteifmtu.value_namespace = name_space
                    self.cpwvcremoteifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcRemoteIfString"):
                    self.cpwvcremoteifstring = value
                    self.cpwvcremoteifstring.value_namespace = name_space
                    self.cpwvcremoteifstring.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcRowStatus"):
                    self.cpwvcrowstatus = value
                    self.cpwvcrowstatus.value_namespace = name_space
                    self.cpwvcrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcSetUpPriority"):
                    self.cpwvcsetuppriority = value
                    self.cpwvcsetuppriority.value_namespace = name_space
                    self.cpwvcsetuppriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcStorageType"):
                    self.cpwvcstoragetype = value
                    self.cpwvcstoragetype.value_namespace = name_space
                    self.cpwvcstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcTimeElapsed"):
                    self.cpwvctimeelapsed = value
                    self.cpwvctimeelapsed.value_namespace = name_space
                    self.cpwvctimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcType"):
                    self.cpwvctype = value
                    self.cpwvctype.value_namespace = name_space
                    self.cpwvctype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcUpTime"):
                    self.cpwvcuptime = value
                    self.cpwvcuptime.value_namespace = name_space
                    self.cpwvcuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcValidIntervals"):
                    self.cpwvcvalidintervals = value
                    self.cpwvcvalidintervals.value_namespace = name_space
                    self.cpwvcvalidintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcEntry"):
                for c in self.cpwvcentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvctable.Cpwvcentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcperfcurrenttable(Entity):
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
            super(CiscoIetfPwMib.Cpwvcperfcurrenttable, self).__init__()

            self.yang_name = "cpwVcPerfCurrentTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcperfcurrententry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvcperfcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcperfcurrenttable, self).__setattr__(name, value)


        class Cpwvcperfcurrententry(Entity):
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
                super(CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry, self).__init__()

                self.yang_name = "cpwVcPerfCurrentEntry"
                self.yang_parent_name = "cpwVcPerfCurrentTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcperfcurrentinhcbytes = YLeaf(YType.uint64, "cpwVcPerfCurrentInHCBytes")

                self.cpwvcperfcurrentinhcpackets = YLeaf(YType.uint64, "cpwVcPerfCurrentInHCPackets")

                self.cpwvcperfcurrentouthcbytes = YLeaf(YType.uint64, "cpwVcPerfCurrentOutHCBytes")

                self.cpwvcperfcurrentouthcpackets = YLeaf(YType.uint64, "cpwVcPerfCurrentOutHCPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwvcperfcurrentinhcbytes",
                                "cpwvcperfcurrentinhcpackets",
                                "cpwvcperfcurrentouthcbytes",
                                "cpwvcperfcurrentouthcpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcperfcurrentinhcbytes.is_set or
                    self.cpwvcperfcurrentinhcpackets.is_set or
                    self.cpwvcperfcurrentouthcbytes.is_set or
                    self.cpwvcperfcurrentouthcpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcperfcurrentinhcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperfcurrentinhcpackets.yfilter != YFilter.not_set or
                    self.cpwvcperfcurrentouthcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperfcurrentouthcpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcPerfCurrentEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcperfcurrentinhcbytes.is_set or self.cpwvcperfcurrentinhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfcurrentinhcbytes.get_name_leafdata())
                if (self.cpwvcperfcurrentinhcpackets.is_set or self.cpwvcperfcurrentinhcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfcurrentinhcpackets.get_name_leafdata())
                if (self.cpwvcperfcurrentouthcbytes.is_set or self.cpwvcperfcurrentouthcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfcurrentouthcbytes.get_name_leafdata())
                if (self.cpwvcperfcurrentouthcpackets.is_set or self.cpwvcperfcurrentouthcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfcurrentouthcpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcPerfCurrentInHCBytes" or name == "cpwVcPerfCurrentInHCPackets" or name == "cpwVcPerfCurrentOutHCBytes" or name == "cpwVcPerfCurrentOutHCPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfCurrentInHCBytes"):
                    self.cpwvcperfcurrentinhcbytes = value
                    self.cpwvcperfcurrentinhcbytes.value_namespace = name_space
                    self.cpwvcperfcurrentinhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfCurrentInHCPackets"):
                    self.cpwvcperfcurrentinhcpackets = value
                    self.cpwvcperfcurrentinhcpackets.value_namespace = name_space
                    self.cpwvcperfcurrentinhcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfCurrentOutHCBytes"):
                    self.cpwvcperfcurrentouthcbytes = value
                    self.cpwvcperfcurrentouthcbytes.value_namespace = name_space
                    self.cpwvcperfcurrentouthcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfCurrentOutHCPackets"):
                    self.cpwvcperfcurrentouthcpackets = value
                    self.cpwvcperfcurrentouthcpackets.value_namespace = name_space
                    self.cpwvcperfcurrentouthcpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcperfcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcperfcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcPerfCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcPerfCurrentEntry"):
                for c in self.cpwvcperfcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcperfcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcPerfCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcperfintervaltable(Entity):
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
            super(CiscoIetfPwMib.Cpwvcperfintervaltable, self).__init__()

            self.yang_name = "cpwVcPerfIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcperfintervalentry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvcperfintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcperfintervaltable, self).__setattr__(name, value)


        class Cpwvcperfintervalentry(Entity):
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
                super(CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry, self).__init__()

                self.yang_name = "cpwVcPerfIntervalEntry"
                self.yang_parent_name = "cpwVcPerfIntervalTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcperfintervalnumber = YLeaf(YType.int32, "cpwVcPerfIntervalNumber")

                self.cpwvcperfintervalinhcbytes = YLeaf(YType.uint64, "cpwVcPerfIntervalInHCBytes")

                self.cpwvcperfintervalinhcpackets = YLeaf(YType.uint64, "cpwVcPerfIntervalInHCPackets")

                self.cpwvcperfintervalouthcbytes = YLeaf(YType.uint64, "cpwVcPerfIntervalOutHCBytes")

                self.cpwvcperfintervalouthcpackets = YLeaf(YType.uint64, "cpwVcPerfIntervalOutHCPackets")

                self.cpwvcperfintervaltimeelapsed = YLeaf(YType.int32, "cpwVcPerfIntervalTimeElapsed")

                self.cpwvcperfintervalvaliddata = YLeaf(YType.boolean, "cpwVcPerfIntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwvcperfintervalnumber",
                                "cpwvcperfintervalinhcbytes",
                                "cpwvcperfintervalinhcpackets",
                                "cpwvcperfintervalouthcbytes",
                                "cpwvcperfintervalouthcpackets",
                                "cpwvcperfintervaltimeelapsed",
                                "cpwvcperfintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcperfintervalnumber.is_set or
                    self.cpwvcperfintervalinhcbytes.is_set or
                    self.cpwvcperfintervalinhcpackets.is_set or
                    self.cpwvcperfintervalouthcbytes.is_set or
                    self.cpwvcperfintervalouthcpackets.is_set or
                    self.cpwvcperfintervaltimeelapsed.is_set or
                    self.cpwvcperfintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalnumber.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalinhcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalinhcpackets.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalouthcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalouthcpackets.yfilter != YFilter.not_set or
                    self.cpwvcperfintervaltimeelapsed.yfilter != YFilter.not_set or
                    self.cpwvcperfintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcPerfIntervalEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwVcPerfIntervalNumber='" + self.cpwvcperfintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcperfintervalnumber.is_set or self.cpwvcperfintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalnumber.get_name_leafdata())
                if (self.cpwvcperfintervalinhcbytes.is_set or self.cpwvcperfintervalinhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalinhcbytes.get_name_leafdata())
                if (self.cpwvcperfintervalinhcpackets.is_set or self.cpwvcperfintervalinhcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalinhcpackets.get_name_leafdata())
                if (self.cpwvcperfintervalouthcbytes.is_set or self.cpwvcperfintervalouthcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalouthcbytes.get_name_leafdata())
                if (self.cpwvcperfintervalouthcpackets.is_set or self.cpwvcperfintervalouthcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalouthcpackets.get_name_leafdata())
                if (self.cpwvcperfintervaltimeelapsed.is_set or self.cpwvcperfintervaltimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervaltimeelapsed.get_name_leafdata())
                if (self.cpwvcperfintervalvaliddata.is_set or self.cpwvcperfintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperfintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcPerfIntervalNumber" or name == "cpwVcPerfIntervalInHCBytes" or name == "cpwVcPerfIntervalInHCPackets" or name == "cpwVcPerfIntervalOutHCBytes" or name == "cpwVcPerfIntervalOutHCPackets" or name == "cpwVcPerfIntervalTimeElapsed" or name == "cpwVcPerfIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalNumber"):
                    self.cpwvcperfintervalnumber = value
                    self.cpwvcperfintervalnumber.value_namespace = name_space
                    self.cpwvcperfintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalInHCBytes"):
                    self.cpwvcperfintervalinhcbytes = value
                    self.cpwvcperfintervalinhcbytes.value_namespace = name_space
                    self.cpwvcperfintervalinhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalInHCPackets"):
                    self.cpwvcperfintervalinhcpackets = value
                    self.cpwvcperfintervalinhcpackets.value_namespace = name_space
                    self.cpwvcperfintervalinhcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalOutHCBytes"):
                    self.cpwvcperfintervalouthcbytes = value
                    self.cpwvcperfintervalouthcbytes.value_namespace = name_space
                    self.cpwvcperfintervalouthcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalOutHCPackets"):
                    self.cpwvcperfintervalouthcpackets = value
                    self.cpwvcperfintervalouthcpackets.value_namespace = name_space
                    self.cpwvcperfintervalouthcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalTimeElapsed"):
                    self.cpwvcperfintervaltimeelapsed = value
                    self.cpwvcperfintervaltimeelapsed.value_namespace = name_space
                    self.cpwvcperfintervaltimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfIntervalValidData"):
                    self.cpwvcperfintervalvaliddata = value
                    self.cpwvcperfintervalvaliddata.value_namespace = name_space
                    self.cpwvcperfintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcperfintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcperfintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcPerfIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcPerfIntervalEntry"):
                for c in self.cpwvcperfintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcperfintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcPerfIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcperftotaltable(Entity):
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
            super(CiscoIetfPwMib.Cpwvcperftotaltable, self).__init__()

            self.yang_name = "cpwVcPerfTotalTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcperftotalentry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvcperftotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcperftotaltable, self).__setattr__(name, value)


        class Cpwvcperftotalentry(Entity):
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
                super(CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry, self).__init__()

                self.yang_name = "cpwVcPerfTotalEntry"
                self.yang_parent_name = "cpwVcPerfTotalTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcperftotaldiscontinuitytime = YLeaf(YType.uint32, "cpwVcPerfTotalDiscontinuityTime")

                self.cpwvcperftotalinhcbytes = YLeaf(YType.uint64, "cpwVcPerfTotalInHCBytes")

                self.cpwvcperftotalinhcpackets = YLeaf(YType.uint64, "cpwVcPerfTotalInHCPackets")

                self.cpwvcperftotalouthcbytes = YLeaf(YType.uint64, "cpwVcPerfTotalOutHCBytes")

                self.cpwvcperftotalouthcpackets = YLeaf(YType.uint64, "cpwVcPerfTotalOutHCPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwvcperftotaldiscontinuitytime",
                                "cpwvcperftotalinhcbytes",
                                "cpwvcperftotalinhcpackets",
                                "cpwvcperftotalouthcbytes",
                                "cpwvcperftotalouthcpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcperftotaldiscontinuitytime.is_set or
                    self.cpwvcperftotalinhcbytes.is_set or
                    self.cpwvcperftotalinhcpackets.is_set or
                    self.cpwvcperftotalouthcbytes.is_set or
                    self.cpwvcperftotalouthcpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcperftotaldiscontinuitytime.yfilter != YFilter.not_set or
                    self.cpwvcperftotalinhcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperftotalinhcpackets.yfilter != YFilter.not_set or
                    self.cpwvcperftotalouthcbytes.yfilter != YFilter.not_set or
                    self.cpwvcperftotalouthcpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcPerfTotalEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPerfTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcperftotaldiscontinuitytime.is_set or self.cpwvcperftotaldiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperftotaldiscontinuitytime.get_name_leafdata())
                if (self.cpwvcperftotalinhcbytes.is_set or self.cpwvcperftotalinhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperftotalinhcbytes.get_name_leafdata())
                if (self.cpwvcperftotalinhcpackets.is_set or self.cpwvcperftotalinhcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperftotalinhcpackets.get_name_leafdata())
                if (self.cpwvcperftotalouthcbytes.is_set or self.cpwvcperftotalouthcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperftotalouthcbytes.get_name_leafdata())
                if (self.cpwvcperftotalouthcpackets.is_set or self.cpwvcperftotalouthcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcperftotalouthcpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcPerfTotalDiscontinuityTime" or name == "cpwVcPerfTotalInHCBytes" or name == "cpwVcPerfTotalInHCPackets" or name == "cpwVcPerfTotalOutHCBytes" or name == "cpwVcPerfTotalOutHCPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfTotalDiscontinuityTime"):
                    self.cpwvcperftotaldiscontinuitytime = value
                    self.cpwvcperftotaldiscontinuitytime.value_namespace = name_space
                    self.cpwvcperftotaldiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfTotalInHCBytes"):
                    self.cpwvcperftotalinhcbytes = value
                    self.cpwvcperftotalinhcbytes.value_namespace = name_space
                    self.cpwvcperftotalinhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfTotalInHCPackets"):
                    self.cpwvcperftotalinhcpackets = value
                    self.cpwvcperftotalinhcpackets.value_namespace = name_space
                    self.cpwvcperftotalinhcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfTotalOutHCBytes"):
                    self.cpwvcperftotalouthcbytes = value
                    self.cpwvcperftotalouthcbytes.value_namespace = name_space
                    self.cpwvcperftotalouthcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPerfTotalOutHCPackets"):
                    self.cpwvcperftotalouthcpackets = value
                    self.cpwvcperftotalouthcpackets.value_namespace = name_space
                    self.cpwvcperftotalouthcpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcperftotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcperftotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcPerfTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcPerfTotalEntry"):
                for c in self.cpwvcperftotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcperftotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcPerfTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcidmappingtable(Entity):
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
            super(CiscoIetfPwMib.Cpwvcidmappingtable, self).__init__()

            self.yang_name = "cpwVcIdMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcidmappingentry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvcidmappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcidmappingtable, self).__setattr__(name, value)


        class Cpwvcidmappingentry(Entity):
            """
            An entry in this table is created by the agent for every  
            VC configured by the cpwVcTable.
            
            .. attribute:: cpwvcidmappingvctype  <key>
            
            	The VC type (indicate the service) of this VC
            	**type**\:   :py:class:`Cpwvctype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwvctype>`
            
            .. attribute:: cpwvcidmappingvcid  <key>
            
            	The VC ID of this VC. Zero if the VC is configured   manually
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcidmappingpeeraddrtype  <key>
            
            	IP address type of the peer node
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
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
                super(CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry, self).__init__()

                self.yang_name = "cpwVcIdMappingEntry"
                self.yang_parent_name = "cpwVcIdMappingTable"

                self.cpwvcidmappingvctype = YLeaf(YType.enumeration, "cpwVcIdMappingVcType")

                self.cpwvcidmappingvcid = YLeaf(YType.uint32, "cpwVcIdMappingVcID")

                self.cpwvcidmappingpeeraddrtype = YLeaf(YType.enumeration, "cpwVcIdMappingPeerAddrType")

                self.cpwvcidmappingpeeraddr = YLeaf(YType.str, "cpwVcIdMappingPeerAddr")

                self.cpwvcidmappingvcindex = YLeaf(YType.uint32, "cpwVcIdMappingVcIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcidmappingvctype",
                                "cpwvcidmappingvcid",
                                "cpwvcidmappingpeeraddrtype",
                                "cpwvcidmappingpeeraddr",
                                "cpwvcidmappingvcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcidmappingvctype.is_set or
                    self.cpwvcidmappingvcid.is_set or
                    self.cpwvcidmappingpeeraddrtype.is_set or
                    self.cpwvcidmappingpeeraddr.is_set or
                    self.cpwvcidmappingvcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcidmappingvctype.yfilter != YFilter.not_set or
                    self.cpwvcidmappingvcid.yfilter != YFilter.not_set or
                    self.cpwvcidmappingpeeraddrtype.yfilter != YFilter.not_set or
                    self.cpwvcidmappingpeeraddr.yfilter != YFilter.not_set or
                    self.cpwvcidmappingvcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcIdMappingEntry" + "[cpwVcIdMappingVcType='" + self.cpwvcidmappingvctype.get() + "']" + "[cpwVcIdMappingVcID='" + self.cpwvcidmappingvcid.get() + "']" + "[cpwVcIdMappingPeerAddrType='" + self.cpwvcidmappingpeeraddrtype.get() + "']" + "[cpwVcIdMappingPeerAddr='" + self.cpwvcidmappingpeeraddr.get() + "']" + "[cpwVcIdMappingVcIndex='" + self.cpwvcidmappingvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcIdMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcidmappingvctype.is_set or self.cpwvcidmappingvctype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcidmappingvctype.get_name_leafdata())
                if (self.cpwvcidmappingvcid.is_set or self.cpwvcidmappingvcid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcidmappingvcid.get_name_leafdata())
                if (self.cpwvcidmappingpeeraddrtype.is_set or self.cpwvcidmappingpeeraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcidmappingpeeraddrtype.get_name_leafdata())
                if (self.cpwvcidmappingpeeraddr.is_set or self.cpwvcidmappingpeeraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcidmappingpeeraddr.get_name_leafdata())
                if (self.cpwvcidmappingvcindex.is_set or self.cpwvcidmappingvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcidmappingvcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIdMappingVcType" or name == "cpwVcIdMappingVcID" or name == "cpwVcIdMappingPeerAddrType" or name == "cpwVcIdMappingPeerAddr" or name == "cpwVcIdMappingVcIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIdMappingVcType"):
                    self.cpwvcidmappingvctype = value
                    self.cpwvcidmappingvctype.value_namespace = name_space
                    self.cpwvcidmappingvctype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcIdMappingVcID"):
                    self.cpwvcidmappingvcid = value
                    self.cpwvcidmappingvcid.value_namespace = name_space
                    self.cpwvcidmappingvcid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcIdMappingPeerAddrType"):
                    self.cpwvcidmappingpeeraddrtype = value
                    self.cpwvcidmappingpeeraddrtype.value_namespace = name_space
                    self.cpwvcidmappingpeeraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcIdMappingPeerAddr"):
                    self.cpwvcidmappingpeeraddr = value
                    self.cpwvcidmappingpeeraddr.value_namespace = name_space
                    self.cpwvcidmappingpeeraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcIdMappingVcIndex"):
                    self.cpwvcidmappingvcindex = value
                    self.cpwvcidmappingvcindex.value_namespace = name_space
                    self.cpwvcidmappingvcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcidmappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcidmappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcIdMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcIdMappingEntry"):
                for c in self.cpwvcidmappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcidmappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcIdMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcpeermappingtable(Entity):
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
            super(CiscoIetfPwMib.Cpwvcpeermappingtable, self).__init__()

            self.yang_name = "cpwVcPeerMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MIB"

            self.cpwvcpeermappingentry = YList(self)

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
                        super(CiscoIetfPwMib.Cpwvcpeermappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMib.Cpwvcpeermappingtable, self).__setattr__(name, value)


        class Cpwvcpeermappingentry(Entity):
            """
            An entry in this table is created by the agent for every  
            VC configured in cpwVcTable.
            
            .. attribute:: cpwvcpeermappingpeeraddrtype  <key>
            
            	IP address type of the peer node
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cpwvcpeermappingpeeraddr  <key>
            
            	IP address type of the peer node
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cpwvcpeermappingvctype  <key>
            
            	The VC type (indicate the service) of this VC
            	**type**\:   :py:class:`Cpwvctype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB.Cpwvctype>`
            
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
                super(CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry, self).__init__()

                self.yang_name = "cpwVcPeerMappingEntry"
                self.yang_parent_name = "cpwVcPeerMappingTable"

                self.cpwvcpeermappingpeeraddrtype = YLeaf(YType.enumeration, "cpwVcPeerMappingPeerAddrType")

                self.cpwvcpeermappingpeeraddr = YLeaf(YType.str, "cpwVcPeerMappingPeerAddr")

                self.cpwvcpeermappingvctype = YLeaf(YType.enumeration, "cpwVcPeerMappingVcType")

                self.cpwvcpeermappingvcid = YLeaf(YType.uint32, "cpwVcPeerMappingVcID")

                self.cpwvcpeermappingvcindex = YLeaf(YType.uint32, "cpwVcPeerMappingVcIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcpeermappingpeeraddrtype",
                                "cpwvcpeermappingpeeraddr",
                                "cpwvcpeermappingvctype",
                                "cpwvcpeermappingvcid",
                                "cpwvcpeermappingvcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcpeermappingpeeraddrtype.is_set or
                    self.cpwvcpeermappingpeeraddr.is_set or
                    self.cpwvcpeermappingvctype.is_set or
                    self.cpwvcpeermappingvcid.is_set or
                    self.cpwvcpeermappingvcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcpeermappingpeeraddrtype.yfilter != YFilter.not_set or
                    self.cpwvcpeermappingpeeraddr.yfilter != YFilter.not_set or
                    self.cpwvcpeermappingvctype.yfilter != YFilter.not_set or
                    self.cpwvcpeermappingvcid.yfilter != YFilter.not_set or
                    self.cpwvcpeermappingvcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcPeerMappingEntry" + "[cpwVcPeerMappingPeerAddrType='" + self.cpwvcpeermappingpeeraddrtype.get() + "']" + "[cpwVcPeerMappingPeerAddr='" + self.cpwvcpeermappingpeeraddr.get() + "']" + "[cpwVcPeerMappingVcType='" + self.cpwvcpeermappingvctype.get() + "']" + "[cpwVcPeerMappingVcID='" + self.cpwvcpeermappingvcid.get() + "']" + "[cpwVcPeerMappingVcIndex='" + self.cpwvcpeermappingvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/cpwVcPeerMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcpeermappingpeeraddrtype.is_set or self.cpwvcpeermappingpeeraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeermappingpeeraddrtype.get_name_leafdata())
                if (self.cpwvcpeermappingpeeraddr.is_set or self.cpwvcpeermappingpeeraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeermappingpeeraddr.get_name_leafdata())
                if (self.cpwvcpeermappingvctype.is_set or self.cpwvcpeermappingvctype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeermappingvctype.get_name_leafdata())
                if (self.cpwvcpeermappingvcid.is_set or self.cpwvcpeermappingvcid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeermappingvcid.get_name_leafdata())
                if (self.cpwvcpeermappingvcindex.is_set or self.cpwvcpeermappingvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcpeermappingvcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcPeerMappingPeerAddrType" or name == "cpwVcPeerMappingPeerAddr" or name == "cpwVcPeerMappingVcType" or name == "cpwVcPeerMappingVcID" or name == "cpwVcPeerMappingVcIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcPeerMappingPeerAddrType"):
                    self.cpwvcpeermappingpeeraddrtype = value
                    self.cpwvcpeermappingpeeraddrtype.value_namespace = name_space
                    self.cpwvcpeermappingpeeraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerMappingPeerAddr"):
                    self.cpwvcpeermappingpeeraddr = value
                    self.cpwvcpeermappingpeeraddr.value_namespace = name_space
                    self.cpwvcpeermappingpeeraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerMappingVcType"):
                    self.cpwvcpeermappingvctype = value
                    self.cpwvcpeermappingvctype.value_namespace = name_space
                    self.cpwvcpeermappingvctype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerMappingVcID"):
                    self.cpwvcpeermappingvcid = value
                    self.cpwvcpeermappingvcid.value_namespace = name_space
                    self.cpwvcpeermappingvcid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcPeerMappingVcIndex"):
                    self.cpwvcpeermappingvcindex = value
                    self.cpwvcpeermappingvcindex.value_namespace = name_space
                    self.cpwvcpeermappingvcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcpeermappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcpeermappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcPeerMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcPeerMappingEntry"):
                for c in self.cpwvcpeermappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcpeermappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcPeerMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cpwvcidmappingtable is not None and self.cpwvcidmappingtable.has_data()) or
            (self.cpwvcobjects is not None and self.cpwvcobjects.has_data()) or
            (self.cpwvcpeermappingtable is not None and self.cpwvcpeermappingtable.has_data()) or
            (self.cpwvcperfcurrenttable is not None and self.cpwvcperfcurrenttable.has_data()) or
            (self.cpwvcperfintervaltable is not None and self.cpwvcperfintervaltable.has_data()) or
            (self.cpwvcperftotaltable is not None and self.cpwvcperftotaltable.has_data()) or
            (self.cpwvctable is not None and self.cpwvctable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpwvcidmappingtable is not None and self.cpwvcidmappingtable.has_operation()) or
            (self.cpwvcobjects is not None and self.cpwvcobjects.has_operation()) or
            (self.cpwvcpeermappingtable is not None and self.cpwvcpeermappingtable.has_operation()) or
            (self.cpwvcperfcurrenttable is not None and self.cpwvcperfcurrenttable.has_operation()) or
            (self.cpwvcperfintervaltable is not None and self.cpwvcperfintervaltable.has_operation()) or
            (self.cpwvcperftotaltable is not None and self.cpwvcperftotaltable.has_operation()) or
            (self.cpwvctable is not None and self.cpwvctable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-PW-MIB:CISCO-IETF-PW-MIB" + path_buffer

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

        if (child_yang_name == "cpwVcIdMappingTable"):
            if (self.cpwvcidmappingtable is None):
                self.cpwvcidmappingtable = CiscoIetfPwMib.Cpwvcidmappingtable()
                self.cpwvcidmappingtable.parent = self
                self._children_name_map["cpwvcidmappingtable"] = "cpwVcIdMappingTable"
            return self.cpwvcidmappingtable

        if (child_yang_name == "cpwVcObjects"):
            if (self.cpwvcobjects is None):
                self.cpwvcobjects = CiscoIetfPwMib.Cpwvcobjects()
                self.cpwvcobjects.parent = self
                self._children_name_map["cpwvcobjects"] = "cpwVcObjects"
            return self.cpwvcobjects

        if (child_yang_name == "cpwVcPeerMappingTable"):
            if (self.cpwvcpeermappingtable is None):
                self.cpwvcpeermappingtable = CiscoIetfPwMib.Cpwvcpeermappingtable()
                self.cpwvcpeermappingtable.parent = self
                self._children_name_map["cpwvcpeermappingtable"] = "cpwVcPeerMappingTable"
            return self.cpwvcpeermappingtable

        if (child_yang_name == "cpwVcPerfCurrentTable"):
            if (self.cpwvcperfcurrenttable is None):
                self.cpwvcperfcurrenttable = CiscoIetfPwMib.Cpwvcperfcurrenttable()
                self.cpwvcperfcurrenttable.parent = self
                self._children_name_map["cpwvcperfcurrenttable"] = "cpwVcPerfCurrentTable"
            return self.cpwvcperfcurrenttable

        if (child_yang_name == "cpwVcPerfIntervalTable"):
            if (self.cpwvcperfintervaltable is None):
                self.cpwvcperfintervaltable = CiscoIetfPwMib.Cpwvcperfintervaltable()
                self.cpwvcperfintervaltable.parent = self
                self._children_name_map["cpwvcperfintervaltable"] = "cpwVcPerfIntervalTable"
            return self.cpwvcperfintervaltable

        if (child_yang_name == "cpwVcPerfTotalTable"):
            if (self.cpwvcperftotaltable is None):
                self.cpwvcperftotaltable = CiscoIetfPwMib.Cpwvcperftotaltable()
                self.cpwvcperftotaltable.parent = self
                self._children_name_map["cpwvcperftotaltable"] = "cpwVcPerfTotalTable"
            return self.cpwvcperftotaltable

        if (child_yang_name == "cpwVcTable"):
            if (self.cpwvctable is None):
                self.cpwvctable = CiscoIetfPwMib.Cpwvctable()
                self.cpwvctable.parent = self
                self._children_name_map["cpwvctable"] = "cpwVcTable"
            return self.cpwvctable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpwVcIdMappingTable" or name == "cpwVcObjects" or name == "cpwVcPeerMappingTable" or name == "cpwVcPerfCurrentTable" or name == "cpwVcPerfIntervalTable" or name == "cpwVcPerfTotalTable" or name == "cpwVcTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfPwMib()
        return self._top_entity

