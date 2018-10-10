""" DOCS_QOS_MIB 

This is the management information for
Quality Of Service (QOS) for DOCSIS 1.1.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



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


class SchedulingType(Enum):
    """
    SchedulingType (Enum Class)

    The scheduling service provided by a CMTS for an

    upstream service flow. If the parameter is omitted

    from an upstream QOS Parameter Set, this object takes

    the value of bestEffort (2). This parameter must be

    reported as undefined (1) for downstream QOS Parameter

    Sets.

    .. data:: undefined = 1

    .. data:: bestEffort = 2

    .. data:: nonRealTimePollingService = 3

    .. data:: realTimePollingService = 4

    .. data:: unsolictedGrantServiceWithAD = 5

    .. data:: unsolictedGrantService = 6

    """

    undefined = Enum.YLeaf(1, "undefined")

    bestEffort = Enum.YLeaf(2, "bestEffort")

    nonRealTimePollingService = Enum.YLeaf(3, "nonRealTimePollingService")

    realTimePollingService = Enum.YLeaf(4, "realTimePollingService")

    unsolictedGrantServiceWithAD = Enum.YLeaf(5, "unsolictedGrantServiceWithAD")

    unsolictedGrantService = Enum.YLeaf(6, "unsolictedGrantService")



class DOCSQOSMIB(Entity):
    """
    
    
    .. attribute:: docsqospktclasstable
    
    	This table describes the packet classification configured on the CM or CMTS.   The model is that a packet either received as input from an interface or transmitted  for output on an interface may be compared  against an ordered list of rules pertaining to the packet contents. Each rule is a row of this table. A matching rule provides a service flow id to to which the packet is classified.  All rules need to match for a packet to match  a classifier.   The objects in this row correspond to a set of Classifier Encoding parameters in a DOCSIS MAC management message. The docsQosPktClassBitMap indicates which particular parameters were present in the classifier as signalled in the DOCSIS message. If the referenced parameter was not present in the signalled DOCSIS 1.1 Classifier, the corresponding object in this row reports a  value as specified in the DESCRIPTION section
    	**type**\:  :py:class:`DocsQosPktClassTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable>`
    
    .. attribute:: docsqosparamsettable
    
    	This table describes the set of DOCSIS 1.1 QOS  parameters defined in a managed device.  The ifIndex index specifies a DOCSIS MAC Domain. The docsQosServiceFlowId index specifies a particular Service Flow.  The docsQosParamSetType index indicates whether the active, admitted, or provisioned QOS Parameter  Set is being described by the row.  Only the QOS Parameter Sets of Docsis 1.1 service flows are represented in this table.  Docsis 1.0 QOS service profiles are not represented in this table.  Each row corresponds to a DOCSIS QOS Parameter Set as signaled via DOCSIS MAC management messages. Each object in the row corresponds to one or  part of one DOCSIS 1.1 Service Flow Encoding. The docsQosParamSetBitMap object in the row indicates which particular parameters were signalled in  the original registration or dynamic service request message that created the QOS Parameter Set.  In many cases, even if a QOS Parameter Set parameter was not signalled, the DOCSIS specification calls for a default value to be used. That default value is reported as the value of the corresponding object in this row.  Many objects are not applicable depending on the service flow direction or upstream scheduling type.  The object value reported in this case is specified in the DESCRIPTION clause
    	**type**\:  :py:class:`DocsQosParamSetTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosParamSetTable>`
    
    .. attribute:: docsqosserviceflowtable
    
    	This table describes the set of Docsis\-QOS  Service Flows in a managed device. 
    	**type**\:  :py:class:`DocsQosServiceFlowTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable>`
    
    .. attribute:: docsqosserviceflowstatstable
    
    	This table describes statistics associated with the   Service Flows in a managed device. 
    	**type**\:  :py:class:`DocsQosServiceFlowStatsTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowStatsTable>`
    
    .. attribute:: docsqosupstreamstatstable
    
    	This table describes statistics associated with   upstream service flows. All counted frames must  be received without an FCS error
    	**type**\:  :py:class:`DocsQosUpstreamStatsTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosUpstreamStatsTable>`
    
    .. attribute:: docsqosdynamicservicestatstable
    
    	This table describes statistics associated with the   Dynamic Service Flows in a managed device. 
    	**type**\:  :py:class:`DocsQosDynamicServiceStatsTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosDynamicServiceStatsTable>`
    
    .. attribute:: docsqosserviceflowlogtable
    
    	This table contains a log of the disconnected Service Flows in a managed device
    	**type**\:  :py:class:`DocsQosServiceFlowLogTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowLogTable>`
    
    .. attribute:: docsqosserviceclasstable
    
    	This table describes the set of Docsis\-QOS  Service Classes in a CMTS. 
    	**type**\:  :py:class:`DocsQosServiceClassTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceClassTable>`
    
    .. attribute:: docsqosserviceclasspolicytable
    
    	This table describes the set of Docsis\-QOS  Service Class Policies.    This table is an adjunct to the docsDevFilterPolicy table.  Entries in  docsDevFilterPolicy table can  point to  specific rows in this table.  This table permits mapping a packet to a service class name of an active service flow so long as  a classifier does not exist at a higher priority
    	**type**\:  :py:class:`DocsQosServiceClassPolicyTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceClassPolicyTable>`
    
    .. attribute:: docsqosphstable
    
    	This table describes set of payload header suppression entries
    	**type**\:  :py:class:`DocsQosPHSTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPHSTable>`
    
    .. attribute:: docsqoscmtsmactosrvflowtable
    
    	This table provide for referencing the service flows  associated with a particular cable modem. This allows  for indexing into other docsQos tables that are  indexed by docsQosServiceFlowId and ifIndex
    	**type**\:  :py:class:`DocsQosCmtsMacToSrvFlowTable <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable>`
    
    

    """

    _prefix = 'DOCS-QOS-MIB'
    _revision = '2001-11-09'

    def __init__(self):
        super(DOCSQOSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-QOS-MIB"
        self.yang_parent_name = "DOCS-QOS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsQosPktClassTable", ("docsqospktclasstable", DOCSQOSMIB.DocsQosPktClassTable)), ("docsQosParamSetTable", ("docsqosparamsettable", DOCSQOSMIB.DocsQosParamSetTable)), ("docsQosServiceFlowTable", ("docsqosserviceflowtable", DOCSQOSMIB.DocsQosServiceFlowTable)), ("docsQosServiceFlowStatsTable", ("docsqosserviceflowstatstable", DOCSQOSMIB.DocsQosServiceFlowStatsTable)), ("docsQosUpstreamStatsTable", ("docsqosupstreamstatstable", DOCSQOSMIB.DocsQosUpstreamStatsTable)), ("docsQosDynamicServiceStatsTable", ("docsqosdynamicservicestatstable", DOCSQOSMIB.DocsQosDynamicServiceStatsTable)), ("docsQosServiceFlowLogTable", ("docsqosserviceflowlogtable", DOCSQOSMIB.DocsQosServiceFlowLogTable)), ("docsQosServiceClassTable", ("docsqosserviceclasstable", DOCSQOSMIB.DocsQosServiceClassTable)), ("docsQosServiceClassPolicyTable", ("docsqosserviceclasspolicytable", DOCSQOSMIB.DocsQosServiceClassPolicyTable)), ("docsQosPHSTable", ("docsqosphstable", DOCSQOSMIB.DocsQosPHSTable)), ("docsQosCmtsMacToSrvFlowTable", ("docsqoscmtsmactosrvflowtable", DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable))])
        self._leafs = OrderedDict()

        self.docsqospktclasstable = DOCSQOSMIB.DocsQosPktClassTable()
        self.docsqospktclasstable.parent = self
        self._children_name_map["docsqospktclasstable"] = "docsQosPktClassTable"

        self.docsqosparamsettable = DOCSQOSMIB.DocsQosParamSetTable()
        self.docsqosparamsettable.parent = self
        self._children_name_map["docsqosparamsettable"] = "docsQosParamSetTable"

        self.docsqosserviceflowtable = DOCSQOSMIB.DocsQosServiceFlowTable()
        self.docsqosserviceflowtable.parent = self
        self._children_name_map["docsqosserviceflowtable"] = "docsQosServiceFlowTable"

        self.docsqosserviceflowstatstable = DOCSQOSMIB.DocsQosServiceFlowStatsTable()
        self.docsqosserviceflowstatstable.parent = self
        self._children_name_map["docsqosserviceflowstatstable"] = "docsQosServiceFlowStatsTable"

        self.docsqosupstreamstatstable = DOCSQOSMIB.DocsQosUpstreamStatsTable()
        self.docsqosupstreamstatstable.parent = self
        self._children_name_map["docsqosupstreamstatstable"] = "docsQosUpstreamStatsTable"

        self.docsqosdynamicservicestatstable = DOCSQOSMIB.DocsQosDynamicServiceStatsTable()
        self.docsqosdynamicservicestatstable.parent = self
        self._children_name_map["docsqosdynamicservicestatstable"] = "docsQosDynamicServiceStatsTable"

        self.docsqosserviceflowlogtable = DOCSQOSMIB.DocsQosServiceFlowLogTable()
        self.docsqosserviceflowlogtable.parent = self
        self._children_name_map["docsqosserviceflowlogtable"] = "docsQosServiceFlowLogTable"

        self.docsqosserviceclasstable = DOCSQOSMIB.DocsQosServiceClassTable()
        self.docsqosserviceclasstable.parent = self
        self._children_name_map["docsqosserviceclasstable"] = "docsQosServiceClassTable"

        self.docsqosserviceclasspolicytable = DOCSQOSMIB.DocsQosServiceClassPolicyTable()
        self.docsqosserviceclasspolicytable.parent = self
        self._children_name_map["docsqosserviceclasspolicytable"] = "docsQosServiceClassPolicyTable"

        self.docsqosphstable = DOCSQOSMIB.DocsQosPHSTable()
        self.docsqosphstable.parent = self
        self._children_name_map["docsqosphstable"] = "docsQosPHSTable"

        self.docsqoscmtsmactosrvflowtable = DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable()
        self.docsqoscmtsmactosrvflowtable.parent = self
        self._children_name_map["docsqoscmtsmactosrvflowtable"] = "docsQosCmtsMacToSrvFlowTable"
        self._segment_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSQOSMIB, [], name, value)


    class DocsQosPktClassTable(Entity):
        """
        This table describes the packet classification
        configured on the CM or CMTS.  
        The model is that a packet either received
        as input from an interface or transmitted 
        for output on an interface may be compared 
        against an ordered list of rules pertaining to
        the packet contents. Each rule is a row of this
        table. A matching rule provides a service flow
        id to to which the packet is classified. 
        All rules need to match for a packet to match 
        a classifier. 
        
        The objects in this row correspond to a set of
        Classifier Encoding parameters in a DOCSIS
        MAC management message. The docsQosPktClassBitMap
        indicates which particular parameters were present
        in the classifier as signalled in the DOCSIS message.
        If the referenced parameter was not present
        in the signalled DOCSIS 1.1 Classifier, the
        corresponding object in this row reports a 
        value as specified in the DESCRIPTION section.
        
        .. attribute:: docsqospktclassentry
        
        	An entry in this table provides a single packet classifier rule. The index ifIndex is an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsQosPktClassEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosPktClassTable, self).__init__()

            self.yang_name = "docsQosPktClassTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosPktClassEntry", ("docsqospktclassentry", DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry))])
            self._leafs = OrderedDict()

            self.docsqospktclassentry = YList(self)
            self._segment_path = lambda: "docsQosPktClassTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosPktClassTable, [], name, value)


        class DocsQosPktClassEntry(Entity):
            """
            An entry in this table provides a single packet
            classifier rule. The index ifIndex is an ifType
            of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            .. attribute:: docsqospktclassid  (key)
            
            	Index assigned to packet classifier entry by  the CMTS which is unique per service flow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: docsqospktclassdirection
            
            	Indicates the direction to which the classifier  is applied
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.IfDirection>`
            
            .. attribute:: docsqospktclasspriority
            
            	The value specifies the order of evaluation of the classifiers. The higher the value the higher the priority. The value of 0 is used as default in  provisioned service flows classifiers.  The default value of 64 is used for dynamic  service flow classifiers. If the referenced parameter is not present in a classifier, this object reports the default value as defined above
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsqospktclassiptoslow
            
            	The low value of a range of TOS byte values. If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqospktclassiptoshigh
            
            	The 8\-bit high value of a range of TOS byte values.  If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqospktclassiptosmask
            
            	The mask value is bitwise ANDed with TOS byte  in an IP packet and this value is used check  range checking of TosLow and TosHigh.  If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqospktclassipprotocol
            
            	This object indicates the value of the IP Protocol field required for IP packets to match this rule.   The value 256 matches traffic with any IP Protocol  value. The value 257 by convention matches both TCP and UDP.   If the referenced parameter is not present in a classifier, this object reports the value of 258
            	**type**\: int
            
            	**range:** 0..258
            
            .. attribute:: docsqospktclassipsourceaddr
            
            	This object is deprecated in favor of the object pair docsQosPktClassInetSourceAddrType and docsQosPktClassInetSourceAddr. Agents that choose to implement this object MUST report an address that matches docsQosPktClassInetSourceAddr object as long as docsQosPktClassInetSourceAddrType is ipv4(1). Otherwise, the value of this object shall be 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsqospktclassipsourcemask
            
            	This object is deprecated in favor of the object pair docsQosPktClassInetSourceMaskType and docsQosPktClassInetSourceMask. Agents that choose to implement this object MUST report an address that matches docsQosPktClassInetSourceMask object as long as docsQosPktClassInetSourceMaskType is ipv4(1). Otherwise, the value of this object shall be 255.255.255.255.  SNMP mangers should note that agent implementation of previous versions of this MIB report 0.0.0.0 as the value when the reference parameter is not present, rather than 255.255.255.255
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsqospktclassipdestaddr
            
            	This object is deprecated in favor of the object pair docsQosPktClassInetDestAddrType and docsQosPktClassInetDestAddr. Agents that choose to implement this object MUST report an address that matches docsQosPktClassInetDestAddr object as long as docsQosPktClassInetDestAddrType is ipv4(1). Otherwise, the value of this object shall be 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsqospktclassipdestmask
            
            	This object is deprecated in favor of the object pair docsQosPktClassInetDestMaskType and docsQosPktClassInetDestMask. Agents that choose to implement this object MUST report an address that matches docsQosPktClassInetDestMask object as long as docsQosPktClassInetDestMaskType is ipv4(1). Otherwise, the value of this object shall be 255.255.255.255.  SNMP mangers should note that agent implementation of previous versions of this MIB report 0.0.0.0 as the value when the reference parameter is not present, rather than 255.255.255.255
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsqospktclasssourceportstart
            
            	This object specifies the low end inclusive range of TCP/UDP source port numbers to which a packet is compared. This object is irrelevant for non\-TCP/UDP IP packets.  If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqospktclasssourceportend
            
            	This object specifies the high end inclusive range of TCP/UDP source port numbers to which a packet is compared. This object is irrelevant for non\-TCP/UDP IP packets.  If the referenced parameter is not present in a classifier, this object reports the value of  65535
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqospktclassdestportstart
            
            	This object specifies the low end inclusive range of TCP/UDP destination port numbers to which a packet is compared.  If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqospktclassdestportend
            
            	This object specifies the high end inclusive range of TCP/UDP destination port numbers to which a packet is compared.  If the referenced parameter is not present in a classifier, this object reports the value of  65535
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqospktclassdestmacaddr
            
            	An Ethernet packet matches an entry when its  destination MAC address bitwise ANDed with  docsQosPktClassDestMacMask equals the value of  docsQosPktClassDestMacAddr.   If the referenced parameter is not present in a classifier, this object reports the value of  '000000000000'H
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsqospktclassdestmacmask
            
            	An Ethernet packet matches an entry when its  destination MAC address bitwise ANDed with  docsQosPktClassDestMacMask equals the value of  docsQosPktClassDestMacAddr.  If the referenced parameter is not present in a classifier, this object reports the value of  '000000000000'H
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsqospktclasssourcemacaddr
            
            	An Ethernet packet matches this entry when its  source MAC address equals the value of  this object.  If the referenced parameter is not present in a classifier, this object reports the value of  'FFFFFFFFFFFF'H
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsqospktclassenetprotocoltype
            
            	This object indicates the format of the layer 3  protocol id in the Ethernet packet. A value of  none(0) means that the rule does not use the  layer 3 protocol type as a matching criteria.  A value of ethertype(1) means that the rule applies only to frames which contains an  EtherType value. Ethertype values are contained in packets using the Dec\-Intel\-Xerox (DIX) encapsulation or the RFC1042 Sub\-Network Access Protocol (SNAP) encapsulation formats.  A value of dsap(2) means that the rule applies only to frames using the IEEE802.3 encapsulation format with a Destination Service Access Point (DSAP) other  than 0xAA (which is reserved for SNAP).  A value of mac(3) means that the rule applies  only to MAC management messages for MAC management messages.  A value of all(4) means that the rule matches all Ethernet packets.   If the Ethernet frame contains an 802.1P/Q Tag  header (i.e. EtherType 0x8100), this object applies to the embedded EtherType field within  the 802.1P/Q header.  If the referenced parameter is not present in a classifier, this object reports the value of 0
            	**type**\:  :py:class:`DocsQosPktClassEnetProtocolType <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry.DocsQosPktClassEnetProtocolType>`
            
            .. attribute:: docsqospktclassenetprotocol
            
            	If docsQosEthPktClassProtocolType is none(0),  this object is ignored when considering whether  a packet matches the current rule.  If dosQosPktClassEnetProtocolType is ethertype(1), this object gives the 16\-bit value of the EtherType that the packet must match in order to match the rule.  If docsQosPktClassEnetProtocolType is dsap(2), the lower 8 bits of this object's value must match the DSAP byte of the packet in order to match the rule.  If docsQosPktClassEnetProtocolType is mac(3), the lower 8 bits of this object value represent a lower bound (inclusive) of MAC management message type codes matched, and the upper 8 bits of this object value represent the upper bound (inclusive) of matched MAC message type codes.  Certain message type codes are excluded from matching, as specified in the reference.  If the Ethernet frame contains an 802.1P/Q Tag header  (i.e. EtherType 0x8100), this object applies to the  embedded EtherType field within the 802.1P/Q header.  If the referenced parameter is not present in the classifier, the value of this object is reported as 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqospktclassuserpriapplies
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..1
            
            	**status**\: obsolete
            
            .. attribute:: docsqospktclassuserprilow
            
            	This object applies only to Ethernet frames  using the 802.1P/Q tag header (indicated with  EtherType 0x8100). Such frames include a 16\-bit  Tag that contains a 3 bit Priority field and a 12 bit VLAN number.  Tagged Ethernet packets must have a 3\-bit Priority field within the range of  docsQosPktClassPriLow and docsQosPktClassPriHigh in  order to match this rule.  If the referenced parameter is not present in the classifier, the value of this object is reported as 0
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docsqospktclassuserprihigh
            
            	This object applies only to Ethernet frames  using the 802.1P/Qtag header (indicated with  EtherType 0x8100). Such frames include a 16\-bit  Tag that contains a 3 bit Priority field and a 12 bit VLAN number.  Tagged Ethernet packets must have a 3\-bit Priority field within the range of  docsQosPktClassPriLow and  docsQosPktClassPriHigh in order to match this rule.  If the referenced parameter is not present in the classifier, the value of this object is reported  as 7
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docsqospktclassvlanid
            
            	This object applies only to Ethernet frames  using the 802.1P/Q tag header.  If this object's value is nonzero, tagged packets must have a VLAN Identifier that matches the value in order to match the rule.  Only the least significant 12 bits of this object's value are valid.   If the referenced parameter is not present in the classifier, the value of this object is reported  as 0
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: docsqospktclassstate
            
            	This object indicates whether or not the classifier is enabled to classify packets to a Service Flow.  If the referenced parameter is not present in the classifier, the value of this object is reported  as active(1)
            	**type**\:  :py:class:`DocsQosPktClassState <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry.DocsQosPktClassState>`
            
            .. attribute:: docsqospktclasspkts
            
            	This object counts the number of packets that have been classified using this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqospktclassbitmap
            
            	This object indicates which parameter encodings were actually present in the DOCSIS packet classifier encoding signaled in the DOCSIS message that created or modified the classifier. Note that Dynamic Service Change messages have replace semantics, so that all non\-default parameters must be present whether the classifier is being created or changed.  A bit of of this object is set to 1 if the parameter indicated by the comment was present in the classifier  encoding, and 0 otherwise.  Note that BITS are encoded most significant bit first, so that if e.g. bits 6 and 7 are set, this object is encoded as the octet string '030000'H
            	**type**\:  :py:class:`DocsQosPktClassBitMap <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry.DocsQosPktClassBitMap>`
            
            .. attribute:: docsqospktclassinetsourceaddrtype
            
            	The type of the internet address for docsQosPktClassInetSourceAddr. This type must be the same as the docsQosPktClassInetSourceMaskType.  If the referenced parameter is not present in a classifier, this object reports the value of ipv4(1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsqospktclassinetsourceaddr
            
            	This object specifies the value of the IP Source Address required for packets to match this rule. An IP packet matches the rule when the packet ip source address bitwise ANDed with the docsQosPktClassInetSourceMask value equals the docsQosPktClassInetSourceAddr value.  If the referenced parameter is not present in a classifier, this object reports the value of '00000000'H
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsqospktclassinetsourcemasktype
            
            	The type of the internet address for docsQosPktClassInetSourceMask. This type must be the same as the docsQosPktClassInetSourceAddrType.  If the referenced parameter is not present in a classifier, this object reports the value of ipv4(1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsqospktclassinetsourcemask
            
            	This object specifies which bits of a packet's IP Source Address that are compared to match this rule. An IP packet matches the rule when the packet source address bitwise ANDed with the docsQosPktClassInetSourceMask value equals the docsQosIpPktClassInetSourceAddr value.  If the referenced parameter is not present in a classifier, this object reports the value of 'FFFFFFFF'H
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsqospktclassinetdestaddrtype
            
            	The type of the internet address for docsQosPktClassInetDestAddr. This type must be the same as the docsQosPktClassInetDestMaskType.  If the referenced parameter is not present in a classifier, this object reports the value of ipv4(1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsqospktclassinetdestaddr
            
            	This object specifies the value of the IP Destination Address required for packets to match this rule. An IP packet matches the rule when the packet ip destination address bitwise ANDed with the docsQosPktClassInetDestMask value equals the docsQosPktClassInetDestAddr value.  If the referenced parameter is not present in a classifier, this object reports the value of '00000000'H
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsqospktclassinetdestmasktype
            
            	The type of the internet address for docsQosPktClassInetDestMask. This type must be the same as the docsQosPktClassInetDestAddrType.  If the referenced parameter is not present in a classifier, this object reports the value of ipv4(1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsqospktclassinetdestmask
            
            	This object specifies which bits of a packet's IP Destination Address that are compared to match this rule. An IP packet matches the rule when the packet destination address bitwise ANDed with the docsQosPktClassInetDestMask value equals the docsQosIpPktClassInetDestAddr value.  If the referenced parameter is not present in a classifier, this object reports the value of 'FFFFFFFF'H
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry, self).__init__()

                self.yang_name = "docsQosPktClassEntry"
                self.yang_parent_name = "docsQosPktClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid','docsqospktclassid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqospktclassid', (YLeaf(YType.int32, 'docsQosPktClassId'), ['int'])),
                    ('docsqospktclassdirection', (YLeaf(YType.enumeration, 'docsQosPktClassDirection'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'IfDirection', '')])),
                    ('docsqospktclasspriority', (YLeaf(YType.int32, 'docsQosPktClassPriority'), ['int'])),
                    ('docsqospktclassiptoslow', (YLeaf(YType.str, 'docsQosPktClassIpTosLow'), ['str'])),
                    ('docsqospktclassiptoshigh', (YLeaf(YType.str, 'docsQosPktClassIpTosHigh'), ['str'])),
                    ('docsqospktclassiptosmask', (YLeaf(YType.str, 'docsQosPktClassIpTosMask'), ['str'])),
                    ('docsqospktclassipprotocol', (YLeaf(YType.int32, 'docsQosPktClassIpProtocol'), ['int'])),
                    ('docsqospktclassipsourceaddr', (YLeaf(YType.str, 'docsQosPktClassIpSourceAddr'), ['str'])),
                    ('docsqospktclassipsourcemask', (YLeaf(YType.str, 'docsQosPktClassIpSourceMask'), ['str'])),
                    ('docsqospktclassipdestaddr', (YLeaf(YType.str, 'docsQosPktClassIpDestAddr'), ['str'])),
                    ('docsqospktclassipdestmask', (YLeaf(YType.str, 'docsQosPktClassIpDestMask'), ['str'])),
                    ('docsqospktclasssourceportstart', (YLeaf(YType.int32, 'docsQosPktClassSourcePortStart'), ['int'])),
                    ('docsqospktclasssourceportend', (YLeaf(YType.int32, 'docsQosPktClassSourcePortEnd'), ['int'])),
                    ('docsqospktclassdestportstart', (YLeaf(YType.int32, 'docsQosPktClassDestPortStart'), ['int'])),
                    ('docsqospktclassdestportend', (YLeaf(YType.int32, 'docsQosPktClassDestPortEnd'), ['int'])),
                    ('docsqospktclassdestmacaddr', (YLeaf(YType.str, 'docsQosPktClassDestMacAddr'), ['str'])),
                    ('docsqospktclassdestmacmask', (YLeaf(YType.str, 'docsQosPktClassDestMacMask'), ['str'])),
                    ('docsqospktclasssourcemacaddr', (YLeaf(YType.str, 'docsQosPktClassSourceMacAddr'), ['str'])),
                    ('docsqospktclassenetprotocoltype', (YLeaf(YType.enumeration, 'docsQosPktClassEnetProtocolType'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'DOCSQOSMIB', 'DocsQosPktClassTable.DocsQosPktClassEntry.DocsQosPktClassEnetProtocolType')])),
                    ('docsqospktclassenetprotocol', (YLeaf(YType.int32, 'docsQosPktClassEnetProtocol'), ['int'])),
                    ('docsqospktclassuserpriapplies', (YLeaf(YType.int32, 'docsQosPktClassUserPriApplies'), ['int'])),
                    ('docsqospktclassuserprilow', (YLeaf(YType.int32, 'docsQosPktClassUserPriLow'), ['int'])),
                    ('docsqospktclassuserprihigh', (YLeaf(YType.int32, 'docsQosPktClassUserPriHigh'), ['int'])),
                    ('docsqospktclassvlanid', (YLeaf(YType.int32, 'docsQosPktClassVlanId'), ['int'])),
                    ('docsqospktclassstate', (YLeaf(YType.enumeration, 'docsQosPktClassState'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'DOCSQOSMIB', 'DocsQosPktClassTable.DocsQosPktClassEntry.DocsQosPktClassState')])),
                    ('docsqospktclasspkts', (YLeaf(YType.uint32, 'docsQosPktClassPkts'), ['int'])),
                    ('docsqospktclassbitmap', (YLeaf(YType.bits, 'docsQosPktClassBitMap'), ['Bits'])),
                    ('docsqospktclassinetsourceaddrtype', (YLeaf(YType.enumeration, 'docsQosPktClassInetSourceAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsqospktclassinetsourceaddr', (YLeaf(YType.str, 'docsQosPktClassInetSourceAddr'), ['str'])),
                    ('docsqospktclassinetsourcemasktype', (YLeaf(YType.enumeration, 'docsQosPktClassInetSourceMaskType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsqospktclassinetsourcemask', (YLeaf(YType.str, 'docsQosPktClassInetSourceMask'), ['str'])),
                    ('docsqospktclassinetdestaddrtype', (YLeaf(YType.enumeration, 'docsQosPktClassInetDestAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsqospktclassinetdestaddr', (YLeaf(YType.str, 'docsQosPktClassInetDestAddr'), ['str'])),
                    ('docsqospktclassinetdestmasktype', (YLeaf(YType.enumeration, 'docsQosPktClassInetDestMaskType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsqospktclassinetdestmask', (YLeaf(YType.str, 'docsQosPktClassInetDestMask'), ['str'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqospktclassid = None
                self.docsqospktclassdirection = None
                self.docsqospktclasspriority = None
                self.docsqospktclassiptoslow = None
                self.docsqospktclassiptoshigh = None
                self.docsqospktclassiptosmask = None
                self.docsqospktclassipprotocol = None
                self.docsqospktclassipsourceaddr = None
                self.docsqospktclassipsourcemask = None
                self.docsqospktclassipdestaddr = None
                self.docsqospktclassipdestmask = None
                self.docsqospktclasssourceportstart = None
                self.docsqospktclasssourceportend = None
                self.docsqospktclassdestportstart = None
                self.docsqospktclassdestportend = None
                self.docsqospktclassdestmacaddr = None
                self.docsqospktclassdestmacmask = None
                self.docsqospktclasssourcemacaddr = None
                self.docsqospktclassenetprotocoltype = None
                self.docsqospktclassenetprotocol = None
                self.docsqospktclassuserpriapplies = None
                self.docsqospktclassuserprilow = None
                self.docsqospktclassuserprihigh = None
                self.docsqospktclassvlanid = None
                self.docsqospktclassstate = None
                self.docsqospktclasspkts = None
                self.docsqospktclassbitmap = Bits()
                self.docsqospktclassinetsourceaddrtype = None
                self.docsqospktclassinetsourceaddr = None
                self.docsqospktclassinetsourcemasktype = None
                self.docsqospktclassinetsourcemask = None
                self.docsqospktclassinetdestaddrtype = None
                self.docsqospktclassinetdestaddr = None
                self.docsqospktclassinetdestmasktype = None
                self.docsqospktclassinetdestmask = None
                self._segment_path = lambda: "docsQosPktClassEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']" + "[docsQosPktClassId='" + str(self.docsqospktclassid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosPktClassTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqospktclassid', u'docsqospktclassdirection', u'docsqospktclasspriority', u'docsqospktclassiptoslow', u'docsqospktclassiptoshigh', u'docsqospktclassiptosmask', u'docsqospktclassipprotocol', u'docsqospktclassipsourceaddr', u'docsqospktclassipsourcemask', u'docsqospktclassipdestaddr', u'docsqospktclassipdestmask', u'docsqospktclasssourceportstart', u'docsqospktclasssourceportend', u'docsqospktclassdestportstart', u'docsqospktclassdestportend', u'docsqospktclassdestmacaddr', u'docsqospktclassdestmacmask', u'docsqospktclasssourcemacaddr', u'docsqospktclassenetprotocoltype', u'docsqospktclassenetprotocol', u'docsqospktclassuserpriapplies', u'docsqospktclassuserprilow', u'docsqospktclassuserprihigh', u'docsqospktclassvlanid', u'docsqospktclassstate', u'docsqospktclasspkts', u'docsqospktclassbitmap', u'docsqospktclassinetsourceaddrtype', u'docsqospktclassinetsourceaddr', u'docsqospktclassinetsourcemasktype', u'docsqospktclassinetsourcemask', u'docsqospktclassinetdestaddrtype', u'docsqospktclassinetdestaddr', u'docsqospktclassinetdestmasktype', u'docsqospktclassinetdestmask'], name, value)

            class DocsQosPktClassEnetProtocolType(Enum):
                """
                DocsQosPktClassEnetProtocolType (Enum Class)

                This object indicates the format of the layer 3 

                protocol id in the Ethernet packet. A value of 

                none(0) means that the rule does not use the 

                layer 3 protocol type as a matching criteria.

                A value of ethertype(1) means that the rule

                applies only to frames which contains an 

                EtherType value. Ethertype values are contained

                in packets using the Dec\-Intel\-Xerox (DIX)

                encapsulation or the RFC1042 Sub\-Network Access

                Protocol (SNAP) encapsulation formats.

                A value of dsap(2) means that the rule applies

                only to frames using the IEEE802.3

                encapsulation format with a Destination Service

                Access Point (DSAP) other 

                than 0xAA (which is reserved for SNAP).

                A value of mac(3) means that the rule applies 

                only to MAC management messages for MAC management

                messages.

                A value of all(4) means that the rule matches

                all Ethernet packets. 

                If the Ethernet frame contains an 802.1P/Q Tag 

                header (i.e. EtherType 0x8100), this object

                applies to the embedded EtherType field within 

                the 802.1P/Q header.

                If the referenced parameter is not present

                in a classifier, this object reports the value of 0.

                .. data:: none = 0

                .. data:: ethertype = 1

                .. data:: dsap = 2

                .. data:: mac = 3

                .. data:: all = 4

                """

                none = Enum.YLeaf(0, "none")

                ethertype = Enum.YLeaf(1, "ethertype")

                dsap = Enum.YLeaf(2, "dsap")

                mac = Enum.YLeaf(3, "mac")

                all = Enum.YLeaf(4, "all")


            class DocsQosPktClassState(Enum):
                """
                DocsQosPktClassState (Enum Class)

                This object indicates whether or not the classifier

                is enabled to classify packets to a Service Flow.

                If the referenced parameter is not present in the

                classifier, the value of this object is reported 

                as active(1).

                .. data:: active = 1

                .. data:: inactive = 2

                """

                active = Enum.YLeaf(1, "active")

                inactive = Enum.YLeaf(2, "inactive")



    class DocsQosParamSetTable(Entity):
        """
        This table describes the set of DOCSIS 1.1 QOS 
        parameters defined in a managed device.
        
        The ifIndex index specifies a DOCSIS MAC Domain.
        The docsQosServiceFlowId index specifies a particular
        Service Flow. 
        The docsQosParamSetType index indicates whether
        the active, admitted, or provisioned QOS Parameter 
        Set is being described by the row.
        
        Only the QOS Parameter Sets of Docsis 1.1 service
        flows are represented in this table.  Docsis 1.0
        QOS service profiles are not represented in this
        table.
        
        Each row corresponds to a DOCSIS QOS Parameter Set
        as signaled via DOCSIS MAC management messages.
        Each object in the row corresponds to one or 
        part of one DOCSIS 1.1 Service Flow Encoding.
        The docsQosParamSetBitMap object in the row indicates
        which particular parameters were signalled in 
        the original registration or dynamic service
        request message that created the QOS Parameter Set.
        
        In many cases, even if a QOS Parameter Set parameter
        was not signalled, the DOCSIS specification calls
        for a default value to be used. That default value
        is reported as the value of the corresponding object
        in this row.
        
        Many objects are not applicable depending on
        the service flow direction or upstream scheduling
        type.  The object value reported in this case
        is specified in the DESCRIPTION clause.
        
        .. attribute:: docsqosparamsetentry
        
        	A unique set of QOS parameters
        	**type**\: list of  		 :py:class:`DocsQosParamSetEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosParamSetTable, self).__init__()

            self.yang_name = "docsQosParamSetTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosParamSetEntry", ("docsqosparamsetentry", DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry))])
            self._leafs = OrderedDict()

            self.docsqosparamsetentry = YList(self)
            self._segment_path = lambda: "docsQosParamSetTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosParamSetTable, [], name, value)


        class DocsQosParamSetEntry(Entity):
            """
            A unique set of QOS parameters.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            .. attribute:: docsqosparamsettype  (key)
            
            	Defines the type of the QOS parameter set defined by this row. active(1) indicates the Active QOS parameter set, describing the service currently being provided by the Docsis MAC domain to the  service flow. admitted(2) indicates the Admitted QOS Parameter Set, describing services reserved by by the Docsis MAC domain for use by the service flow. provisioned (3) describes the QOS Parameter Set defined in the DOCSIS CM Configuration file for the service flow
            	**type**\:  :py:class:`DocsQosParamSetType <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry.DocsQosParamSetType>`
            
            .. attribute:: docsqosparamsetserviceclassname
            
            	Refers to the Service Class Name that the  parameter set values were derived.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default  value of this object is a zero length string
            	**type**\: str
            
            .. attribute:: docsqosparamsetpriority
            
            	The relative priority of a service flow. Higher numbers indicate higher priority. This priority should only be used to differentiate service flow with identical parameter sets.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default  value of this object is 0.  If the parameter is not applicable, the reported value is 0
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docsqosparamsetmaxtrafficrate
            
            	Maximum sustained traffic rate allowed for this  service flow in bits/sec. Must count all MAC frame  data PDU from the bytes following the MAC header HCS to the end of the CRC. The number of bytes  forwarded is limited during any time interval. The value 0 means no maximum traffic rate is  enforced. This object applies to both upstream and downstream service flows.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default value of this object is 0. If the parameter is not applicable, it is reported as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosparamsetmaxtrafficburst
            
            	Specifies the token bucket size in bytes for this parameter set. The value is calculated  from the byte following the MAC header HCS to  the end of the CRC. This object is applied in  conjunction with docsQosParamSetMaxTrafficRate to  calculate maximum sustained traffic rate.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default value of this object for scheduling types bestEffort (2), nonRealTimePollingService(3), and realTimePollingService(4) is 1522.   If this parameter is not applicable, it is reported as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosparamsetminreservedrate
            
            	Specifies the guaranteed minimum rate in bits/sec for this parameter set. The value is  calculated from the byte following the MAC  header HCS to the end of the CRC. The default value of 0 has the meaning that no bandwidth  is reserved. If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default value of this object is 0. If the parameter is not applicable, it is reported as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosparamsetminreservedpkt
            
            	Specifies an assumed minimum packet size in  bytes for which the docsQosParamSetMinReservedRate  will be provided. The value is calculated from the byte following the MAC header HCS to the  end of the CRC.       If the referenced parameter is omitted from a DOCSIS QOS parameter set, the default value is CMTS implementation dependent. In this case, the CMTS reports the default value it is using and the CM reports a value of 0. If the referenced parameter is not applicable to the direction or scheduling type of the service flow, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosparamsetactivetimeout
            
            	Specifies the maximum duration in seconds that  resources remain unused on an active service flow before CMTS signals that both active and admitted parameters set are null. The default value of 0 signifies an infinite amount of time.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default value of this object is 0
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: docsqosparamsetadmittedtimeout
            
            	Specifies the maximum duration in seconds that  resources remain in admitted state before  resources must be released. The value of 0 signifies an infinite amount  of time.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the  default value of this object is 200
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: docsqosparamsetmaxconcatburst
            
            	Specifies the maximum concatenated burst in bytes which an upstream  service flow is allowed.  The value is calculated from the FC byte of the Concatenation MAC Header to the last CRC byte in  of the last concatenated MAC frame, inclusive. The value of 0 specifies no maximum burst.  If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set, the default value of this object is 0. If the parameter is not applicable, this object's value is reported as 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosparamsetschedulingtype
            
            	Specifies the upstream scheduling service used for  upstream service flow.   If the referenced parameter is not present in the corresponding DOCSIS QOS Parameter Set of an upstream service flow, the default value of this object is bestEffort(2). For QOS parameter sets of downstream service flows, this object's value is reported as undefined(1)
            	**type**\:  :py:class:`SchedulingType <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.SchedulingType>`
            
            .. attribute:: docsqosparamsetnompollinterval
            
            	Specifies the nominal interval in microseconds  between successive unicast request opportunities on an upstream service flow.  This object applies only to upstream service flows with schedulingType of value nonRealTimePollingService(3), realTimePollingService(4), and unsolictedGrantServiceWithAD(5).  The parameter is mandatory for realTimePollingService(4).  If the parameter is omitted with nonRealTimePollingService(3), the CMTS uses an implementation dependent value.  If the parameter is omitted with unsolictedGrantServiceWithAD(5), the CMTS uses as a default value the value of the Nominal Grant Interval parameter.  In all cases, the CMTS reports the value it is using when the parameter is applicable.  The CM reports the  signaled parameter value if it was signaled,  and 0 otherwise.  If the referenced parameter is not applicable to the direction or scheduling type of the corresponding DOCSIS QOS Parameter Set, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosparamsettolpolljitter
            
            	Specifies the maximum amount of time in microseconds that the unicast request interval may be delayed from the nominal periodic schedule on an upstream service flow.  This parameter is applicable only to upstream service flows with a Schedulingtype of realTimePollingService(4) or unsolictedGrantServiceWithAD(5).  If the referenced parameter is applicable but not present in the corresponding DOCSIS QOS Parameter Set, the CMTS uses an implementation dependent  value and reports the value it is using. The CM reports a value of 0 in this case.  If the parameter is not applicable to the direction or upstream scheduling type of the service flow, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosparamsetunsolicitgrantsize
            
            	Specifies the unsolicited grant size in bytes.  The grant size includes the entire MAC frame  data PDU from the Frame Control byte to end of the MAC frame.  The referenced parameter is applicable only  for upstream flows with a SchedulingType of of unsolicitedGrantServicewithAD(5) or unsolicitedGrantService(6), and is mandatory when applicable. Both CMTS and CM report the signaled value of the parameter in this case.                  If the referenced parameter is not applicable to the direction or scheduling type of the corresponding DOCSIS QOS Parameter Set, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosparamsetnomgrantinterval
            
            	Specifies the nominal interval in microseconds  between successive data grant opportunities  on an upstream service flow.  The referenced parameter is applicable only  for upstream flows with a SchedulingType of of unsolicitedGrantServicewithAD(5) or unsolicitedGrantService(6), and is mandatory when applicable. Both CMTS and CM report the signaled value of the parameter in this case.  If the referenced parameter is not applicable to the direction or scheduling type of the corresponding DOCSIS QOS Parameter Set, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosparamsettolgrantjitter
            
            	Specifies the maximum amount of time in microseconds that the transmission opportunities may be delayed from the nominal periodic schedule.   The referenced parameter is applicable only  for upstream flows with a SchedulingType of of unsolicitedGrantServicewithAD(5) or unsolicitedGrantService(6), and is mandatory when applicable. Both CMTS and CM report the signaled value of the parameter in this case.  If the referenced parameter is not applicable to the direction or scheduling type of the corresponding DOCSIS QOS Parameter Set, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosparamsetgrantsperinterval
            
            	Specifies the number of data grants per Nominal  Grant Interval  (docsQosParamSetNomGrantInterval).  The referenced parameter is applicable only  for upstream flows with a SchedulingType of of unsolicitedGrantServicewithAD(5) or unsolicitedGrantService(6), and is mandatory when applicable. Both CMTS and CM report the signaled value of the parameter in this case.  If the referenced parameter is not applicable to the direction or scheduling type of the corresponding DOCSIS QOS Parameter Set, both CMTS and CM report this object's value as 0
            	**type**\: int
            
            	**range:** 0..127
            
            .. attribute:: docsqosparamsettosandmask
            
            	Specifies the AND mask for IP TOS byte for overwriting IP packets TOS value.  The IP packets TOS byte is  bitwise ANDed with docsQosParamSetTosAndMask and  result is bitwise ORed with docsQosParamSetTosORMask and result is written to IP packet TOS byte.  A value of 'FF'H for docsQosParamSetTosAndMask and a value of '00'H for docsQosParamSetTosOrMask means  that IP Packet TOS byte is not overwritten.  Even though the this object is only enforced by the Cable Modem Termination System (CMTS), Cable Modems must report the value as signaled in the referenced parameter.  This combination is reported if the referenced parameter is not present in a QOS Parameter Set
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqosparamsettosormask
            
            	Specifies the OR mask for IP TOS byte. See the description of docsQosParamSetTosAndMask for further details
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqosparamsetmaxlatency
            
            	Specifies the maximum latency between the reception of a packet by the CMTS on its NSI  and the forwarding of the packet to the RF interface. A value of 0 signifies no maximum latency enforced. This object only applies to downstream service flows.  If the referenced parameter is not present in the corresponding downstream DOCSIS QOS Parameter Set,  the default value is 0. This parameter is not applicable to upstream DOCSIS QOS Parameter Sets, and its value is reported as 0 in this case
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosparamsetrequestpolicyoct
            
            	Specifies which transmit interval opportunities  the CM omits for upstream transmission requests and  packet transmissions. This object takes its default value for downstream service flows.  Unless otherwise indicated, a bit value of 1 means that a CM must \*not\* use that opportunity for  upstream transmission.  Calling bit 0 the least significant bit of the  least significant (4th) octet, and increasing bit number with significance, the bit definitions are as defined below\:  broadcastReqOpp(0)\:      all CMs broadcast request opportunities  priorityReqMulticastReq(1)\:      priority request multicast request opportunities  reqDataForReq(2)\:      request/data opportunities for requests  reqDataForData(3)\:      request/data opportunities for data  piggybackReqWithData(4)\:      piggyback requests with data  concatenateData(5)\:      concatenate data  fragmentData(6)\:      fragment data  suppresspayloadheaders(7)\:       suppress payload headers  dropPktsExceedUGSize(8)\:      A value of 1 mean that service flow must drop      packet that do not fit in the Unsolicited       Grant size   If the referenced parameter is not present in  a QOS Parameter Set, the value of this object is reported as '00000000'H
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: docsqosparamsetbitmap
            
            	This object indicates the set of QOS Parameter Set parameters actually signaled in the  DOCSIS registration or dynamic service request message that created or modified the QOS Parameter Set.  A bit is set to 1 when the parameter described by the indicated reference section is present in the original request.    Note that when Service Class names are expanded, the registration or dynamic response message may contain parameters as expanded by the CMTS based on a stored service class. These expanded parameters are \*not\* indicated by a 1 bit in this object.  Note that even though some QOS Parameter Set  parameters may not be signalled in a message (so that the paramater's bit in this object is 0) the DOCSIS specification calls for default values to be used. These default values are reported as the corresponding object's value in the row.   Note that BITS objects are encoded most significant bit first. For example, if bits 1 and 16 are set, the value of this object  is the octet string '400080'H
            	**type**\:  :py:class:`DocsQosParamSetBitMap <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry.DocsQosParamSetBitMap>`
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry, self).__init__()

                self.yang_name = "docsQosParamSetEntry"
                self.yang_parent_name = "docsQosParamSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid','docsqosparamsettype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqosparamsettype', (YLeaf(YType.enumeration, 'docsQosParamSetType'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'DOCSQOSMIB', 'DocsQosParamSetTable.DocsQosParamSetEntry.DocsQosParamSetType')])),
                    ('docsqosparamsetserviceclassname', (YLeaf(YType.str, 'docsQosParamSetServiceClassName'), ['str'])),
                    ('docsqosparamsetpriority', (YLeaf(YType.int32, 'docsQosParamSetPriority'), ['int'])),
                    ('docsqosparamsetmaxtrafficrate', (YLeaf(YType.uint32, 'docsQosParamSetMaxTrafficRate'), ['int'])),
                    ('docsqosparamsetmaxtrafficburst', (YLeaf(YType.uint32, 'docsQosParamSetMaxTrafficBurst'), ['int'])),
                    ('docsqosparamsetminreservedrate', (YLeaf(YType.uint32, 'docsQosParamSetMinReservedRate'), ['int'])),
                    ('docsqosparamsetminreservedpkt', (YLeaf(YType.int32, 'docsQosParamSetMinReservedPkt'), ['int'])),
                    ('docsqosparamsetactivetimeout', (YLeaf(YType.int32, 'docsQosParamSetActiveTimeout'), ['int'])),
                    ('docsqosparamsetadmittedtimeout', (YLeaf(YType.int32, 'docsQosParamSetAdmittedTimeout'), ['int'])),
                    ('docsqosparamsetmaxconcatburst', (YLeaf(YType.int32, 'docsQosParamSetMaxConcatBurst'), ['int'])),
                    ('docsqosparamsetschedulingtype', (YLeaf(YType.enumeration, 'docsQosParamSetSchedulingType'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'SchedulingType', '')])),
                    ('docsqosparamsetnompollinterval', (YLeaf(YType.uint32, 'docsQosParamSetNomPollInterval'), ['int'])),
                    ('docsqosparamsettolpolljitter', (YLeaf(YType.uint32, 'docsQosParamSetTolPollJitter'), ['int'])),
                    ('docsqosparamsetunsolicitgrantsize', (YLeaf(YType.int32, 'docsQosParamSetUnsolicitGrantSize'), ['int'])),
                    ('docsqosparamsetnomgrantinterval', (YLeaf(YType.uint32, 'docsQosParamSetNomGrantInterval'), ['int'])),
                    ('docsqosparamsettolgrantjitter', (YLeaf(YType.uint32, 'docsQosParamSetTolGrantJitter'), ['int'])),
                    ('docsqosparamsetgrantsperinterval', (YLeaf(YType.int32, 'docsQosParamSetGrantsPerInterval'), ['int'])),
                    ('docsqosparamsettosandmask', (YLeaf(YType.str, 'docsQosParamSetTosAndMask'), ['str'])),
                    ('docsqosparamsettosormask', (YLeaf(YType.str, 'docsQosParamSetTosOrMask'), ['str'])),
                    ('docsqosparamsetmaxlatency', (YLeaf(YType.uint32, 'docsQosParamSetMaxLatency'), ['int'])),
                    ('docsqosparamsetrequestpolicyoct', (YLeaf(YType.str, 'docsQosParamSetRequestPolicyOct'), ['str'])),
                    ('docsqosparamsetbitmap', (YLeaf(YType.bits, 'docsQosParamSetBitMap'), ['Bits'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqosparamsettype = None
                self.docsqosparamsetserviceclassname = None
                self.docsqosparamsetpriority = None
                self.docsqosparamsetmaxtrafficrate = None
                self.docsqosparamsetmaxtrafficburst = None
                self.docsqosparamsetminreservedrate = None
                self.docsqosparamsetminreservedpkt = None
                self.docsqosparamsetactivetimeout = None
                self.docsqosparamsetadmittedtimeout = None
                self.docsqosparamsetmaxconcatburst = None
                self.docsqosparamsetschedulingtype = None
                self.docsqosparamsetnompollinterval = None
                self.docsqosparamsettolpolljitter = None
                self.docsqosparamsetunsolicitgrantsize = None
                self.docsqosparamsetnomgrantinterval = None
                self.docsqosparamsettolgrantjitter = None
                self.docsqosparamsetgrantsperinterval = None
                self.docsqosparamsettosandmask = None
                self.docsqosparamsettosormask = None
                self.docsqosparamsetmaxlatency = None
                self.docsqosparamsetrequestpolicyoct = None
                self.docsqosparamsetbitmap = Bits()
                self._segment_path = lambda: "docsQosParamSetEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']" + "[docsQosParamSetType='" + str(self.docsqosparamsettype) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosParamSetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosParamSetTable.DocsQosParamSetEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqosparamsettype', u'docsqosparamsetserviceclassname', u'docsqosparamsetpriority', u'docsqosparamsetmaxtrafficrate', u'docsqosparamsetmaxtrafficburst', u'docsqosparamsetminreservedrate', u'docsqosparamsetminreservedpkt', u'docsqosparamsetactivetimeout', u'docsqosparamsetadmittedtimeout', u'docsqosparamsetmaxconcatburst', u'docsqosparamsetschedulingtype', u'docsqosparamsetnompollinterval', u'docsqosparamsettolpolljitter', u'docsqosparamsetunsolicitgrantsize', u'docsqosparamsetnomgrantinterval', u'docsqosparamsettolgrantjitter', u'docsqosparamsetgrantsperinterval', u'docsqosparamsettosandmask', u'docsqosparamsettosormask', u'docsqosparamsetmaxlatency', u'docsqosparamsetrequestpolicyoct', u'docsqosparamsetbitmap'], name, value)

            class DocsQosParamSetType(Enum):
                """
                DocsQosParamSetType (Enum Class)

                Defines the type of the QOS parameter set defined

                by this row. active(1) indicates the Active QOS

                parameter set, describing the service currently

                being provided by the Docsis MAC domain to the 

                service flow. admitted(2) indicates the Admitted

                QOS Parameter Set, describing services reserved by

                by the Docsis MAC domain for use by the service flow.

                provisioned (3) describes the QOS Parameter Set

                defined in the DOCSIS CM Configuration file for

                the service flow.

                .. data:: active = 1

                .. data:: admitted = 2

                .. data:: provisioned = 3

                """

                active = Enum.YLeaf(1, "active")

                admitted = Enum.YLeaf(2, "admitted")

                provisioned = Enum.YLeaf(3, "provisioned")



    class DocsQosServiceFlowTable(Entity):
        """
        This table describes the set of Docsis\-QOS 
        Service Flows in a managed device. 
        
        .. attribute:: docsqosserviceflowentry
        
        	Describes a service flow. An entry in the table exists for each  Service Flow ID. The ifIndex is an   ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsQosServiceFlowEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosServiceFlowTable, self).__init__()

            self.yang_name = "docsQosServiceFlowTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosServiceFlowEntry", ("docsqosserviceflowentry", DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry))])
            self._leafs = OrderedDict()

            self.docsqosserviceflowentry = YList(self)
            self._segment_path = lambda: "docsQosServiceFlowTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowTable, [], name, value)


        class DocsQosServiceFlowEntry(Entity):
            """
            Describes a service flow.
            An entry in the table exists for each 
            Service Flow ID. The ifIndex is an  
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	An index assigned to a service flow by CMTS
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsqosserviceflowprovisionedparamsetindex
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowadmittedparamsetindex
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowactiveparamsetindex
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowsid
            
            	Service Identifier (SID) assigned to an  admitted or active service flow. This object reports a value of 0 if a Service Id is not  associated with the service flow. Only active  or admitted upstream service flows will have a Service Id (SID)
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsqosserviceflowdirection
            
            	The direction of the service flow
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.IfDirection>`
            
            .. attribute:: docsqosserviceflowprimary
            
            	Object reflects whether service flow is the primary  or a secondary service flow.  A primary service flow is the default service flow for otherwise unclassified traffic and all MAC  messages
            	**type**\: bool
            
            .. attribute:: docsqosserviceflowactivetimeout
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowadmittedtimeout
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowschedulingtype
            
            	This object is obsolete
            	**type**\:  :py:class:`SchedulingType <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.SchedulingType>`
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowrequestpolicy
            
            	This object is obsolete
            	**type**\: str
            
            	**length:** 4
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowtosandmask
            
            	This object is obsolete
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceflowtosormask
            
            	This object is obsolete
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry, self).__init__()

                self.yang_name = "docsQosServiceFlowEntry"
                self.yang_parent_name = "docsQosServiceFlowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.uint32, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqosserviceflowprovisionedparamsetindex', (YLeaf(YType.uint32, 'docsQosServiceFlowProvisionedParamSetIndex'), ['int'])),
                    ('docsqosserviceflowadmittedparamsetindex', (YLeaf(YType.uint32, 'docsQosServiceFlowAdmittedParamSetIndex'), ['int'])),
                    ('docsqosserviceflowactiveparamsetindex', (YLeaf(YType.uint32, 'docsQosServiceFlowActiveParamSetIndex'), ['int'])),
                    ('docsqosserviceflowsid', (YLeaf(YType.uint32, 'docsQosServiceFlowSID'), ['int'])),
                    ('docsqosserviceflowdirection', (YLeaf(YType.enumeration, 'docsQosServiceFlowDirection'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'IfDirection', '')])),
                    ('docsqosserviceflowprimary', (YLeaf(YType.boolean, 'docsQosServiceFlowPrimary'), ['bool'])),
                    ('docsqosserviceflowactivetimeout', (YLeaf(YType.int32, 'docsQosServiceFlowActiveTimeout'), ['int'])),
                    ('docsqosserviceflowadmittedtimeout', (YLeaf(YType.int32, 'docsQosServiceFlowAdmittedTimeout'), ['int'])),
                    ('docsqosserviceflowschedulingtype', (YLeaf(YType.enumeration, 'docsQosServiceFlowSchedulingType'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'SchedulingType', '')])),
                    ('docsqosserviceflowrequestpolicy', (YLeaf(YType.str, 'docsQosServiceFlowRequestPolicy'), ['str'])),
                    ('docsqosserviceflowtosandmask', (YLeaf(YType.str, 'docsQosServiceFlowTosAndMask'), ['str'])),
                    ('docsqosserviceflowtosormask', (YLeaf(YType.str, 'docsQosServiceFlowTosOrMask'), ['str'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqosserviceflowprovisionedparamsetindex = None
                self.docsqosserviceflowadmittedparamsetindex = None
                self.docsqosserviceflowactiveparamsetindex = None
                self.docsqosserviceflowsid = None
                self.docsqosserviceflowdirection = None
                self.docsqosserviceflowprimary = None
                self.docsqosserviceflowactivetimeout = None
                self.docsqosserviceflowadmittedtimeout = None
                self.docsqosserviceflowschedulingtype = None
                self.docsqosserviceflowrequestpolicy = None
                self.docsqosserviceflowtosandmask = None
                self.docsqosserviceflowtosormask = None
                self._segment_path = lambda: "docsQosServiceFlowEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosServiceFlowTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqosserviceflowprovisionedparamsetindex', u'docsqosserviceflowadmittedparamsetindex', u'docsqosserviceflowactiveparamsetindex', u'docsqosserviceflowsid', u'docsqosserviceflowdirection', u'docsqosserviceflowprimary', u'docsqosserviceflowactivetimeout', u'docsqosserviceflowadmittedtimeout', u'docsqosserviceflowschedulingtype', u'docsqosserviceflowrequestpolicy', u'docsqosserviceflowtosandmask', u'docsqosserviceflowtosormask'], name, value)


    class DocsQosServiceFlowStatsTable(Entity):
        """
        This table describes statistics associated with the  
        Service Flows in a managed device. 
        
        .. attribute:: docsqosserviceflowstatsentry
        
        	Describes a set of service flow statistics. An entry in the table exists for each  Service Flow ID. The ifIndex is an   ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsQosServiceFlowStatsEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowStatsTable.DocsQosServiceFlowStatsEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosServiceFlowStatsTable, self).__init__()

            self.yang_name = "docsQosServiceFlowStatsTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosServiceFlowStatsEntry", ("docsqosserviceflowstatsentry", DOCSQOSMIB.DocsQosServiceFlowStatsTable.DocsQosServiceFlowStatsEntry))])
            self._leafs = OrderedDict()

            self.docsqosserviceflowstatsentry = YList(self)
            self._segment_path = lambda: "docsQosServiceFlowStatsTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowStatsTable, [], name, value)


        class DocsQosServiceFlowStatsEntry(Entity):
            """
            Describes a set of service flow statistics.
            An entry in the table exists for each 
            Service Flow ID. The ifIndex is an  
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            .. attribute:: docsqosserviceflowpkts
            
            	The number of Packet Data PDUs classified to this service flow. This object does not count MAC\-specific management messages. CMs not classifying downstream packets may report this object's value as 0. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowoctets
            
            	The number of octets transmitted on the Docsis RF network from the byte after the MAC header HCS to the end of the CRC for all packets counted in the docsQosServiceFlowPkts object for this row. Note that this counts the octets after payload header suppression has been applied. CMs not classifying to a downstream service flow may report this object's value as 0 for that flow. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowtimecreated
            
            	The value of sysUpTime when the service flow  was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowtimeactive
            
            	The total time that service flow has been active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: docsqosserviceflowphsunknowns
            
            	The number of packets received on the service flow with an unknown payload header suppression index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowpoliceddroppkts
            
            	The number of packets dropped due to policing of  the service flow, especially to limit the maximum  rate of the flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowpoliceddelaypkts
            
            	The number of packet delayed due to policing of  the service flow, especially to limit the maximum rate of the flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosServiceFlowStatsTable.DocsQosServiceFlowStatsEntry, self).__init__()

                self.yang_name = "docsQosServiceFlowStatsEntry"
                self.yang_parent_name = "docsQosServiceFlowStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqosserviceflowpkts', (YLeaf(YType.uint32, 'docsQosServiceFlowPkts'), ['int'])),
                    ('docsqosserviceflowoctets', (YLeaf(YType.uint32, 'docsQosServiceFlowOctets'), ['int'])),
                    ('docsqosserviceflowtimecreated', (YLeaf(YType.uint32, 'docsQosServiceFlowTimeCreated'), ['int'])),
                    ('docsqosserviceflowtimeactive', (YLeaf(YType.uint32, 'docsQosServiceFlowTimeActive'), ['int'])),
                    ('docsqosserviceflowphsunknowns', (YLeaf(YType.uint32, 'docsQosServiceFlowPHSUnknowns'), ['int'])),
                    ('docsqosserviceflowpoliceddroppkts', (YLeaf(YType.uint32, 'docsQosServiceFlowPolicedDropPkts'), ['int'])),
                    ('docsqosserviceflowpoliceddelaypkts', (YLeaf(YType.uint32, 'docsQosServiceFlowPolicedDelayPkts'), ['int'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqosserviceflowpkts = None
                self.docsqosserviceflowoctets = None
                self.docsqosserviceflowtimecreated = None
                self.docsqosserviceflowtimeactive = None
                self.docsqosserviceflowphsunknowns = None
                self.docsqosserviceflowpoliceddroppkts = None
                self.docsqosserviceflowpoliceddelaypkts = None
                self._segment_path = lambda: "docsQosServiceFlowStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosServiceFlowStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowStatsTable.DocsQosServiceFlowStatsEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqosserviceflowpkts', u'docsqosserviceflowoctets', u'docsqosserviceflowtimecreated', u'docsqosserviceflowtimeactive', u'docsqosserviceflowphsunknowns', u'docsqosserviceflowpoliceddroppkts', u'docsqosserviceflowpoliceddelaypkts'], name, value)


    class DocsQosUpstreamStatsTable(Entity):
        """
        This table describes statistics associated with  
        upstream service flows. All counted frames must 
        be received without an FCS error.
        
        .. attribute:: docsqosupstreamstatsentry
        
        	Describes a set of upstream service flow statistics. An entry in the table exists for each  upstream Service Flow in a managed device.  The ifIndex is an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsQosUpstreamStatsEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosUpstreamStatsTable.DocsQosUpstreamStatsEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosUpstreamStatsTable, self).__init__()

            self.yang_name = "docsQosUpstreamStatsTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosUpstreamStatsEntry", ("docsqosupstreamstatsentry", DOCSQOSMIB.DocsQosUpstreamStatsTable.DocsQosUpstreamStatsEntry))])
            self._leafs = OrderedDict()

            self.docsqosupstreamstatsentry = YList(self)
            self._segment_path = lambda: "docsQosUpstreamStatsTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosUpstreamStatsTable, [], name, value)


        class DocsQosUpstreamStatsEntry(Entity):
            """
            Describes a set of upstream service flow statistics.
            An entry in the table exists for each 
            upstream Service Flow in a managed device. 
            The ifIndex is an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqossid  (key)
            
            	Identifies a service id for an admitted or active  upstream service flow
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsqosupstreamfragments
            
            	The number of fragmentation headers received on an upstream  service flow, regardless of whether the fragment was correctly reassembled into a  valid packet. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosupstreamfragdiscards
            
            	The number of upstream fragments discarded and not  assembled into a valid upstream packet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosupstreamconcatbursts
            
            	The number of concatenation headers received on an  upstream service flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosUpstreamStatsTable.DocsQosUpstreamStatsEntry, self).__init__()

                self.yang_name = "docsQosUpstreamStatsEntry"
                self.yang_parent_name = "docsQosUpstreamStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqossid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqossid', (YLeaf(YType.int32, 'docsQosSID'), ['int'])),
                    ('docsqosupstreamfragments', (YLeaf(YType.uint32, 'docsQosUpstreamFragments'), ['int'])),
                    ('docsqosupstreamfragdiscards', (YLeaf(YType.uint32, 'docsQosUpstreamFragDiscards'), ['int'])),
                    ('docsqosupstreamconcatbursts', (YLeaf(YType.uint32, 'docsQosUpstreamConcatBursts'), ['int'])),
                ])
                self.ifindex = None
                self.docsqossid = None
                self.docsqosupstreamfragments = None
                self.docsqosupstreamfragdiscards = None
                self.docsqosupstreamconcatbursts = None
                self._segment_path = lambda: "docsQosUpstreamStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosSID='" + str(self.docsqossid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosUpstreamStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosUpstreamStatsTable.DocsQosUpstreamStatsEntry, [u'ifindex', u'docsqossid', u'docsqosupstreamfragments', u'docsqosupstreamfragdiscards', u'docsqosupstreamconcatbursts'], name, value)


    class DocsQosDynamicServiceStatsTable(Entity):
        """
        This table describes statistics associated with the  
        Dynamic Service Flows in a managed device. 
        
        .. attribute:: docsqosdynamicservicestatsentry
        
        	Describes a set of dynamic service flow statistics. Two entries exist for each Docsis mac layer  interface for the upstream and downstream direction. On the CMTS, the downstream direction row indicates messages transmitted or transactions originated by the CMTS. The upstream direction row indicates messages received or transaction originated by the CM. On the CM, the downstream direction row  indicates messages received or transactions originated by the CMTS. The upstream direction  row indicates messages transmitted by the CM or transactions originated by the CM. The ifIndex is an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsQosDynamicServiceStatsEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosDynamicServiceStatsTable.DocsQosDynamicServiceStatsEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosDynamicServiceStatsTable, self).__init__()

            self.yang_name = "docsQosDynamicServiceStatsTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosDynamicServiceStatsEntry", ("docsqosdynamicservicestatsentry", DOCSQOSMIB.DocsQosDynamicServiceStatsTable.DocsQosDynamicServiceStatsEntry))])
            self._leafs = OrderedDict()

            self.docsqosdynamicservicestatsentry = YList(self)
            self._segment_path = lambda: "docsQosDynamicServiceStatsTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosDynamicServiceStatsTable, [], name, value)


        class DocsQosDynamicServiceStatsEntry(Entity):
            """
            Describes a set of dynamic service flow statistics.
            Two entries exist for each Docsis mac layer 
            interface for the upstream and downstream direction.
            On the CMTS, the downstream direction row indicates
            messages transmitted or transactions originated
            by the CMTS. The upstream direction row indicates
            messages received or transaction originated by the
            CM. On the CM, the downstream direction row 
            indicates messages received or transactions
            originated by the CMTS. The upstream direction 
            row indicates messages transmitted by the CM or
            transactions originated by the CM.
            The ifIndex is an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosifdirection  (key)
            
            	The direction of interface
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.IfDirection>`
            
            .. attribute:: docsqosdsareqs
            
            	The number of Dynamic Service Addition Requests, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdsarsps
            
            	The number of Dynamic Service Addition Responses, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdsaacks
            
            	The number of Dynamic Service Addition Acknowledgements, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdscreqs
            
            	The number of Dynamic Service Change Requests, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdscrsps
            
            	The number of Dynamic Service Change Responses, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdscacks
            
            	The number of Dynamic Service Change Acknowledgements, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdsdreqs
            
            	The number of Dynamic Service Delete Requests, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdsdrsps
            
            	The number of Dynamic Service Delete Responses, including retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicadds
            
            	The number of successful Dynamic Service Addition transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicaddfails
            
            	The number of failed Dynamic Service Addition transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicchanges
            
            	The number of successful Dynamic Service Change transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicchangefails
            
            	The number of failed Dynamic Service Change transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicdeletes
            
            	The number of successful Dynamic Service Delete transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdynamicdeletefails
            
            	The number of failed Dynamic Service Delete transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccreqs
            
            	The number of Dynamic Channel Change Request messages traversing an interface. This count is nonzero only on downstream direction rows. This count should include number of retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccrsps
            
            	The number of Dynamic Channel Change Response messages traversing an interface. This count is nonzero only on upstream direction rows. This count should include number of retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccacks
            
            	The number of Dynamic Channel Change Acknowledgement messages traversing an interface. This count is nonzero only on downstream direction rows. This count should include number of retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccs
            
            	The number of successful Dynamic Channel Change transactions. This count is nonzero only on downstream direction rows
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccfails
            
            	The number of failed Dynamic Channel Change transactions. This count is nonzero only on downstream direction rows
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccrspdeparts
            
            	The number of Dynamic Channel Change Response (depart) messages traversing an interface. This count is only counted  on upstream direction rows
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosdccrsparrives
            
            	The number of Dynamic Channel Change Response (arrive) messages traversing an interface. This count is only counted on upstream direction rows. This count should include number of retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosDynamicServiceStatsTable.DocsQosDynamicServiceStatsEntry, self).__init__()

                self.yang_name = "docsQosDynamicServiceStatsEntry"
                self.yang_parent_name = "docsQosDynamicServiceStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosifdirection']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosifdirection', (YLeaf(YType.enumeration, 'docsQosIfDirection'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'IfDirection', '')])),
                    ('docsqosdsareqs', (YLeaf(YType.uint32, 'docsQosDSAReqs'), ['int'])),
                    ('docsqosdsarsps', (YLeaf(YType.uint32, 'docsQosDSARsps'), ['int'])),
                    ('docsqosdsaacks', (YLeaf(YType.uint32, 'docsQosDSAAcks'), ['int'])),
                    ('docsqosdscreqs', (YLeaf(YType.uint32, 'docsQosDSCReqs'), ['int'])),
                    ('docsqosdscrsps', (YLeaf(YType.uint32, 'docsQosDSCRsps'), ['int'])),
                    ('docsqosdscacks', (YLeaf(YType.uint32, 'docsQosDSCAcks'), ['int'])),
                    ('docsqosdsdreqs', (YLeaf(YType.uint32, 'docsQosDSDReqs'), ['int'])),
                    ('docsqosdsdrsps', (YLeaf(YType.uint32, 'docsQosDSDRsps'), ['int'])),
                    ('docsqosdynamicadds', (YLeaf(YType.uint32, 'docsQosDynamicAdds'), ['int'])),
                    ('docsqosdynamicaddfails', (YLeaf(YType.uint32, 'docsQosDynamicAddFails'), ['int'])),
                    ('docsqosdynamicchanges', (YLeaf(YType.uint32, 'docsQosDynamicChanges'), ['int'])),
                    ('docsqosdynamicchangefails', (YLeaf(YType.uint32, 'docsQosDynamicChangeFails'), ['int'])),
                    ('docsqosdynamicdeletes', (YLeaf(YType.uint32, 'docsQosDynamicDeletes'), ['int'])),
                    ('docsqosdynamicdeletefails', (YLeaf(YType.uint32, 'docsQosDynamicDeleteFails'), ['int'])),
                    ('docsqosdccreqs', (YLeaf(YType.uint32, 'docsQosDCCReqs'), ['int'])),
                    ('docsqosdccrsps', (YLeaf(YType.uint32, 'docsQosDCCRsps'), ['int'])),
                    ('docsqosdccacks', (YLeaf(YType.uint32, 'docsQosDCCAcks'), ['int'])),
                    ('docsqosdccs', (YLeaf(YType.uint32, 'docsQosDCCs'), ['int'])),
                    ('docsqosdccfails', (YLeaf(YType.uint32, 'docsQosDCCFails'), ['int'])),
                    ('docsqosdccrspdeparts', (YLeaf(YType.uint32, 'docsQosDCCRspDeparts'), ['int'])),
                    ('docsqosdccrsparrives', (YLeaf(YType.uint32, 'docsQosDCCRspArrives'), ['int'])),
                ])
                self.ifindex = None
                self.docsqosifdirection = None
                self.docsqosdsareqs = None
                self.docsqosdsarsps = None
                self.docsqosdsaacks = None
                self.docsqosdscreqs = None
                self.docsqosdscrsps = None
                self.docsqosdscacks = None
                self.docsqosdsdreqs = None
                self.docsqosdsdrsps = None
                self.docsqosdynamicadds = None
                self.docsqosdynamicaddfails = None
                self.docsqosdynamicchanges = None
                self.docsqosdynamicchangefails = None
                self.docsqosdynamicdeletes = None
                self.docsqosdynamicdeletefails = None
                self.docsqosdccreqs = None
                self.docsqosdccrsps = None
                self.docsqosdccacks = None
                self.docsqosdccs = None
                self.docsqosdccfails = None
                self.docsqosdccrspdeparts = None
                self.docsqosdccrsparrives = None
                self._segment_path = lambda: "docsQosDynamicServiceStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosIfDirection='" + str(self.docsqosifdirection) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosDynamicServiceStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosDynamicServiceStatsTable.DocsQosDynamicServiceStatsEntry, [u'ifindex', u'docsqosifdirection', u'docsqosdsareqs', u'docsqosdsarsps', u'docsqosdsaacks', u'docsqosdscreqs', u'docsqosdscrsps', u'docsqosdscacks', u'docsqosdsdreqs', u'docsqosdsdrsps', u'docsqosdynamicadds', u'docsqosdynamicaddfails', u'docsqosdynamicchanges', u'docsqosdynamicchangefails', u'docsqosdynamicdeletes', u'docsqosdynamicdeletefails', u'docsqosdccreqs', u'docsqosdccrsps', u'docsqosdccacks', u'docsqosdccs', u'docsqosdccfails', u'docsqosdccrspdeparts', u'docsqosdccrsparrives'], name, value)


    class DocsQosServiceFlowLogTable(Entity):
        """
        This table contains a log of the disconnected
        Service Flows in a managed device.
        
        .. attribute:: docsqosserviceflowlogentry
        
        	The information regarding a single disconnected  service flow
        	**type**\: list of  		 :py:class:`DocsQosServiceFlowLogEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosServiceFlowLogTable, self).__init__()

            self.yang_name = "docsQosServiceFlowLogTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosServiceFlowLogEntry", ("docsqosserviceflowlogentry", DOCSQOSMIB.DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry))])
            self._leafs = OrderedDict()

            self.docsqosserviceflowlogentry = YList(self)
            self._segment_path = lambda: "docsQosServiceFlowLogTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowLogTable, [], name, value)


        class DocsQosServiceFlowLogEntry(Entity):
            """
            The information regarding a single disconnected 
            service flow.
            
            .. attribute:: docsqosserviceflowlogindex  (key)
            
            	Unique index for a logged service flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogifindex
            
            	The ifIndex of ifType docsCableMaclayer(127)  on the CMTS where the service flow was present
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsqosserviceflowlogsfid
            
            	The index assigned to the service flow by the CMTS
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsqosserviceflowlogcmmac
            
            	The MAC address for the cable modem associated with  the service flow
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsqosserviceflowlogpkts
            
            	The number of packets counted on this service flow  after payload header suppression
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogoctets
            
            	The number of octets counted on this service flow  after payload header suppression
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogtimedeleted
            
            	The value of sysUpTime when the service flow  was deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogtimecreated
            
            	The value of sysUpTime when the service flow  was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogtimeactive
            
            	The total time that service flow was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: docsqosserviceflowlogdirection
            
            	The value of docsQosServiceFlowDirection  for the service flow
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.IfDirection>`
            
            .. attribute:: docsqosserviceflowlogprimary
            
            	The value of docsQosServiceFlowPrimary for the  service flow
            	**type**\: bool
            
            .. attribute:: docsqosserviceflowlogserviceclassname
            
            	The value of docsQosParamSetServiceClassName for the provisioned QOS Parameter Set of the  service flow
            	**type**\: str
            
            .. attribute:: docsqosserviceflowlogpoliceddroppkts
            
            	The final value of docsQosServiceFlowPolicedDropPkts for the service flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogpoliceddelaypkts
            
            	The final value of docsQosServiceFlowPolicedDelayPkts for the service flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceflowlogcontrol
            
            	Setting this object to the value destroy(6) removes this entry from the table.  Reading this object return the value active(1)
            	**type**\:  :py:class:`DocsQosServiceFlowLogControl <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry.DocsQosServiceFlowLogControl>`
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry, self).__init__()

                self.yang_name = "docsQosServiceFlowLogEntry"
                self.yang_parent_name = "docsQosServiceFlowLogTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsqosserviceflowlogindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsqosserviceflowlogindex', (YLeaf(YType.uint32, 'docsQosServiceFlowLogIndex'), ['int'])),
                    ('docsqosserviceflowlogifindex', (YLeaf(YType.int32, 'docsQosServiceFlowLogIfIndex'), ['int'])),
                    ('docsqosserviceflowlogsfid', (YLeaf(YType.uint32, 'docsQosServiceFlowLogSFID'), ['int'])),
                    ('docsqosserviceflowlogcmmac', (YLeaf(YType.str, 'docsQosServiceFlowLogCmMac'), ['str'])),
                    ('docsqosserviceflowlogpkts', (YLeaf(YType.uint32, 'docsQosServiceFlowLogPkts'), ['int'])),
                    ('docsqosserviceflowlogoctets', (YLeaf(YType.uint32, 'docsQosServiceFlowLogOctets'), ['int'])),
                    ('docsqosserviceflowlogtimedeleted', (YLeaf(YType.uint32, 'docsQosServiceFlowLogTimeDeleted'), ['int'])),
                    ('docsqosserviceflowlogtimecreated', (YLeaf(YType.uint32, 'docsQosServiceFlowLogTimeCreated'), ['int'])),
                    ('docsqosserviceflowlogtimeactive', (YLeaf(YType.uint32, 'docsQosServiceFlowLogTimeActive'), ['int'])),
                    ('docsqosserviceflowlogdirection', (YLeaf(YType.enumeration, 'docsQosServiceFlowLogDirection'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'IfDirection', '')])),
                    ('docsqosserviceflowlogprimary', (YLeaf(YType.boolean, 'docsQosServiceFlowLogPrimary'), ['bool'])),
                    ('docsqosserviceflowlogserviceclassname', (YLeaf(YType.str, 'docsQosServiceFlowLogServiceClassName'), ['str'])),
                    ('docsqosserviceflowlogpoliceddroppkts', (YLeaf(YType.uint32, 'docsQosServiceFlowLogPolicedDropPkts'), ['int'])),
                    ('docsqosserviceflowlogpoliceddelaypkts', (YLeaf(YType.uint32, 'docsQosServiceFlowLogPolicedDelayPkts'), ['int'])),
                    ('docsqosserviceflowlogcontrol', (YLeaf(YType.enumeration, 'docsQosServiceFlowLogControl'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'DOCSQOSMIB', 'DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry.DocsQosServiceFlowLogControl')])),
                ])
                self.docsqosserviceflowlogindex = None
                self.docsqosserviceflowlogifindex = None
                self.docsqosserviceflowlogsfid = None
                self.docsqosserviceflowlogcmmac = None
                self.docsqosserviceflowlogpkts = None
                self.docsqosserviceflowlogoctets = None
                self.docsqosserviceflowlogtimedeleted = None
                self.docsqosserviceflowlogtimecreated = None
                self.docsqosserviceflowlogtimeactive = None
                self.docsqosserviceflowlogdirection = None
                self.docsqosserviceflowlogprimary = None
                self.docsqosserviceflowlogserviceclassname = None
                self.docsqosserviceflowlogpoliceddroppkts = None
                self.docsqosserviceflowlogpoliceddelaypkts = None
                self.docsqosserviceflowlogcontrol = None
                self._segment_path = lambda: "docsQosServiceFlowLogEntry" + "[docsQosServiceFlowLogIndex='" + str(self.docsqosserviceflowlogindex) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosServiceFlowLogTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosServiceFlowLogTable.DocsQosServiceFlowLogEntry, [u'docsqosserviceflowlogindex', u'docsqosserviceflowlogifindex', u'docsqosserviceflowlogsfid', u'docsqosserviceflowlogcmmac', u'docsqosserviceflowlogpkts', u'docsqosserviceflowlogoctets', u'docsqosserviceflowlogtimedeleted', u'docsqosserviceflowlogtimecreated', u'docsqosserviceflowlogtimeactive', u'docsqosserviceflowlogdirection', u'docsqosserviceflowlogprimary', u'docsqosserviceflowlogserviceclassname', u'docsqosserviceflowlogpoliceddroppkts', u'docsqosserviceflowlogpoliceddelaypkts', u'docsqosserviceflowlogcontrol'], name, value)

            class DocsQosServiceFlowLogControl(Enum):
                """
                DocsQosServiceFlowLogControl (Enum Class)

                Setting this object to the value destroy(6) removes

                this entry from the table. 

                Reading this object return the value active(1).

                .. data:: active = 1

                .. data:: destroy = 6

                """

                active = Enum.YLeaf(1, "active")

                destroy = Enum.YLeaf(6, "destroy")



    class DocsQosServiceClassTable(Entity):
        """
        This table describes the set of Docsis\-QOS 
        Service Classes in a CMTS. 
        
        .. attribute:: docsqosserviceclassentry
        
        	A provisioned service class on a CMTS.  Each entry defines a template for certain  DOCSIS QOS Parameter Set values. When a CM  creates or modifies an Admitted QOS Parameter Set for a Service Flow, it may reference a Service Class Name instead of providing explicit QOS Parameter Set values. In this case, the CMTS populates the QOS Parameter Set with the applicable  corresponding values from the named Service Class. Subsequent changes to a Service Class row do \*not\*  affect the QOS Parameter Set values of any service flows already admitted.  A service class template applies to only a single direction, as indicated in the  docsQosServiceClassDirection object
        	**type**\: list of  		 :py:class:`DocsQosServiceClassEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceClassTable.DocsQosServiceClassEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosServiceClassTable, self).__init__()

            self.yang_name = "docsQosServiceClassTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosServiceClassEntry", ("docsqosserviceclassentry", DOCSQOSMIB.DocsQosServiceClassTable.DocsQosServiceClassEntry))])
            self._leafs = OrderedDict()

            self.docsqosserviceclassentry = YList(self)
            self._segment_path = lambda: "docsQosServiceClassTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosServiceClassTable, [], name, value)


        class DocsQosServiceClassEntry(Entity):
            """
            A provisioned service class on a CMTS. 
            Each entry defines a template for certain 
            DOCSIS QOS Parameter Set values. When a CM 
            creates or modifies an Admitted QOS Parameter Set for a
            Service Flow, it may reference a Service Class
            Name instead of providing explicit QOS Parameter
            Set values. In this case, the CMTS populates
            the QOS Parameter Set with the applicable 
            corresponding values from the named Service Class.
            Subsequent changes to a Service Class row do \*not\* 
            affect the QOS Parameter Set values of any service flows
            already admitted.
            
            A service class template applies to only
            a single direction, as indicated in the 
            docsQosServiceClassDirection object.
            
            .. attribute:: docsqosserviceclassname  (key)
            
            	Service Class Name. DOCSIS specifies that the maximum size is 15 printable ASCII characters with  a terminating zero. The terminating zero is not represented in this DisplayString syntax object
            	**type**\: str
            
            	**length:** 1..15
            
            .. attribute:: docsqosserviceclassparamsetindex
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsqosserviceclassstatus
            
            	Used to create or delete rows in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsqosserviceclasspriority
            
            	Template for docsQosParamSetPriority
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docsqosserviceclassmaxtrafficrate
            
            	Template for docsQosParamSetMaxTrafficRate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceclassmaxtrafficburst
            
            	Template for docsQosParamSetMaxTrafficBurst
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceclassminreservedrate
            
            	Template for docsQosParamSEtMinReservedRate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsqosserviceclassminreservedpkt
            
            	Template for docsQosParamSetMinReservedPkt
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosserviceclassmaxconcatburst
            
            	Template for docsQosParamSetMaxConcatBurst
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosserviceclassnompollinterval
            
            	Template for docsQosParamSetNomPollInterval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosserviceclasstolpolljitter
            
            	Template for docsQosParamSetTolPollJitter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosserviceclassunsolicitgrantsize
            
            	Template for docsQosParamSetUnsolicitGrantSize
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsqosserviceclassnomgrantinterval
            
            	Template for docsQosParamSetNomGrantInterval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosserviceclasstolgrantjitter
            
            	Template for docsQosParamSetTolGrantJitter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosserviceclassgrantsperinterval
            
            	Template for docsQosParamSetGrantsPerInterval
            	**type**\: int
            
            	**range:** 0..127
            
            .. attribute:: docsqosserviceclassmaxlatency
            
            	Template for docsQosParamSetClassMaxLatency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: docsqosserviceclassactivetimeout
            
            	Template for docsQosParamSetActiveTimeout
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: docsqosserviceclassadmittedtimeout
            
            	Template for docsQosParamSetAdmittedTimeout
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: docsqosserviceclassschedulingtype
            
            	Template for docsQosParamSetSchedulingType
            	**type**\:  :py:class:`SchedulingType <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.SchedulingType>`
            
            .. attribute:: docsqosserviceclassrequestpolicy
            
            	Template for docsQosParamSetRequestPolicyOct
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: docsqosserviceclasstosandmask
            
            	Template for docsQosParamSetTosAndMask
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqosserviceclasstosormask
            
            	Template for docsQosParamSetTosOrMask
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docsqosserviceclassdirection
            
            	Specifies whether the service class template applies to upstream or downstream service flows
            	**type**\:  :py:class:`IfDirection <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.IfDirection>`
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosServiceClassTable.DocsQosServiceClassEntry, self).__init__()

                self.yang_name = "docsQosServiceClassEntry"
                self.yang_parent_name = "docsQosServiceClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsqosserviceclassname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsqosserviceclassname', (YLeaf(YType.str, 'docsQosServiceClassName'), ['str'])),
                    ('docsqosserviceclassparamsetindex', (YLeaf(YType.uint32, 'docsQosServiceClassParamSetIndex'), ['int'])),
                    ('docsqosserviceclassstatus', (YLeaf(YType.enumeration, 'docsQosServiceClassStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsqosserviceclasspriority', (YLeaf(YType.int32, 'docsQosServiceClassPriority'), ['int'])),
                    ('docsqosserviceclassmaxtrafficrate', (YLeaf(YType.uint32, 'docsQosServiceClassMaxTrafficRate'), ['int'])),
                    ('docsqosserviceclassmaxtrafficburst', (YLeaf(YType.uint32, 'docsQosServiceClassMaxTrafficBurst'), ['int'])),
                    ('docsqosserviceclassminreservedrate', (YLeaf(YType.uint32, 'docsQosServiceClassMinReservedRate'), ['int'])),
                    ('docsqosserviceclassminreservedpkt', (YLeaf(YType.int32, 'docsQosServiceClassMinReservedPkt'), ['int'])),
                    ('docsqosserviceclassmaxconcatburst', (YLeaf(YType.int32, 'docsQosServiceClassMaxConcatBurst'), ['int'])),
                    ('docsqosserviceclassnompollinterval', (YLeaf(YType.uint32, 'docsQosServiceClassNomPollInterval'), ['int'])),
                    ('docsqosserviceclasstolpolljitter', (YLeaf(YType.uint32, 'docsQosServiceClassTolPollJitter'), ['int'])),
                    ('docsqosserviceclassunsolicitgrantsize', (YLeaf(YType.int32, 'docsQosServiceClassUnsolicitGrantSize'), ['int'])),
                    ('docsqosserviceclassnomgrantinterval', (YLeaf(YType.uint32, 'docsQosServiceClassNomGrantInterval'), ['int'])),
                    ('docsqosserviceclasstolgrantjitter', (YLeaf(YType.uint32, 'docsQosServiceClassTolGrantJitter'), ['int'])),
                    ('docsqosserviceclassgrantsperinterval', (YLeaf(YType.int32, 'docsQosServiceClassGrantsPerInterval'), ['int'])),
                    ('docsqosserviceclassmaxlatency', (YLeaf(YType.uint32, 'docsQosServiceClassMaxLatency'), ['int'])),
                    ('docsqosserviceclassactivetimeout', (YLeaf(YType.int32, 'docsQosServiceClassActiveTimeout'), ['int'])),
                    ('docsqosserviceclassadmittedtimeout', (YLeaf(YType.int32, 'docsQosServiceClassAdmittedTimeout'), ['int'])),
                    ('docsqosserviceclassschedulingtype', (YLeaf(YType.enumeration, 'docsQosServiceClassSchedulingType'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'SchedulingType', '')])),
                    ('docsqosserviceclassrequestpolicy', (YLeaf(YType.str, 'docsQosServiceClassRequestPolicy'), ['str'])),
                    ('docsqosserviceclasstosandmask', (YLeaf(YType.str, 'docsQosServiceClassTosAndMask'), ['str'])),
                    ('docsqosserviceclasstosormask', (YLeaf(YType.str, 'docsQosServiceClassTosOrMask'), ['str'])),
                    ('docsqosserviceclassdirection', (YLeaf(YType.enumeration, 'docsQosServiceClassDirection'), [('ydk.models.cisco_ios_xe.DOCS_QOS_MIB', 'IfDirection', '')])),
                ])
                self.docsqosserviceclassname = None
                self.docsqosserviceclassparamsetindex = None
                self.docsqosserviceclassstatus = None
                self.docsqosserviceclasspriority = None
                self.docsqosserviceclassmaxtrafficrate = None
                self.docsqosserviceclassmaxtrafficburst = None
                self.docsqosserviceclassminreservedrate = None
                self.docsqosserviceclassminreservedpkt = None
                self.docsqosserviceclassmaxconcatburst = None
                self.docsqosserviceclassnompollinterval = None
                self.docsqosserviceclasstolpolljitter = None
                self.docsqosserviceclassunsolicitgrantsize = None
                self.docsqosserviceclassnomgrantinterval = None
                self.docsqosserviceclasstolgrantjitter = None
                self.docsqosserviceclassgrantsperinterval = None
                self.docsqosserviceclassmaxlatency = None
                self.docsqosserviceclassactivetimeout = None
                self.docsqosserviceclassadmittedtimeout = None
                self.docsqosserviceclassschedulingtype = None
                self.docsqosserviceclassrequestpolicy = None
                self.docsqosserviceclasstosandmask = None
                self.docsqosserviceclasstosormask = None
                self.docsqosserviceclassdirection = None
                self._segment_path = lambda: "docsQosServiceClassEntry" + "[docsQosServiceClassName='" + str(self.docsqosserviceclassname) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosServiceClassTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosServiceClassTable.DocsQosServiceClassEntry, [u'docsqosserviceclassname', u'docsqosserviceclassparamsetindex', u'docsqosserviceclassstatus', u'docsqosserviceclasspriority', u'docsqosserviceclassmaxtrafficrate', u'docsqosserviceclassmaxtrafficburst', u'docsqosserviceclassminreservedrate', u'docsqosserviceclassminreservedpkt', u'docsqosserviceclassmaxconcatburst', u'docsqosserviceclassnompollinterval', u'docsqosserviceclasstolpolljitter', u'docsqosserviceclassunsolicitgrantsize', u'docsqosserviceclassnomgrantinterval', u'docsqosserviceclasstolgrantjitter', u'docsqosserviceclassgrantsperinterval', u'docsqosserviceclassmaxlatency', u'docsqosserviceclassactivetimeout', u'docsqosserviceclassadmittedtimeout', u'docsqosserviceclassschedulingtype', u'docsqosserviceclassrequestpolicy', u'docsqosserviceclasstosandmask', u'docsqosserviceclasstosormask', u'docsqosserviceclassdirection'], name, value)


    class DocsQosServiceClassPolicyTable(Entity):
        """
        This table describes the set of Docsis\-QOS 
        Service Class Policies.  
        
        This table is an adjunct to the
        docsDevFilterPolicy table.  Entries in 
        docsDevFilterPolicy table can  point to 
        specific rows in this table.
        
        This table permits mapping a packet to a service
        class name of an active service flow so long as 
        a classifier does not exist at a higher
        priority.
        
        .. attribute:: docsqosserviceclasspolicyentry
        
        	A service class name policy entry
        	**type**\: list of  		 :py:class:`DocsQosServiceClassPolicyEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceClassPolicyTable.DocsQosServiceClassPolicyEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosServiceClassPolicyTable, self).__init__()

            self.yang_name = "docsQosServiceClassPolicyTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosServiceClassPolicyEntry", ("docsqosserviceclasspolicyentry", DOCSQOSMIB.DocsQosServiceClassPolicyTable.DocsQosServiceClassPolicyEntry))])
            self._leafs = OrderedDict()

            self.docsqosserviceclasspolicyentry = YList(self)
            self._segment_path = lambda: "docsQosServiceClassPolicyTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosServiceClassPolicyTable, [], name, value)


        class DocsQosServiceClassPolicyEntry(Entity):
            """
            A service class name policy entry.
            
            .. attribute:: docsqosserviceclasspolicyindex  (key)
            
            	Index value to uniquely identify an entry in this table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsqosserviceclasspolicyname
            
            	Service Class Name to identify the name of the  service class flow to which the packet should be directed
            	**type**\: str
            
            .. attribute:: docsqosserviceclasspolicyrulepriority
            
            	Service Class Policy rule priority for the entry
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsqosserviceclasspolicystatus
            
            	Used to create or delete rows in this table. This object should not be deleted if it is reference by an entry in docsDevFilterPolicy. The reference should be deleted first
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosServiceClassPolicyTable.DocsQosServiceClassPolicyEntry, self).__init__()

                self.yang_name = "docsQosServiceClassPolicyEntry"
                self.yang_parent_name = "docsQosServiceClassPolicyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsqosserviceclasspolicyindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsqosserviceclasspolicyindex', (YLeaf(YType.int32, 'docsQosServiceClassPolicyIndex'), ['int'])),
                    ('docsqosserviceclasspolicyname', (YLeaf(YType.str, 'docsQosServiceClassPolicyName'), ['str'])),
                    ('docsqosserviceclasspolicyrulepriority', (YLeaf(YType.int32, 'docsQosServiceClassPolicyRulePriority'), ['int'])),
                    ('docsqosserviceclasspolicystatus', (YLeaf(YType.enumeration, 'docsQosServiceClassPolicyStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docsqosserviceclasspolicyindex = None
                self.docsqosserviceclasspolicyname = None
                self.docsqosserviceclasspolicyrulepriority = None
                self.docsqosserviceclasspolicystatus = None
                self._segment_path = lambda: "docsQosServiceClassPolicyEntry" + "[docsQosServiceClassPolicyIndex='" + str(self.docsqosserviceclasspolicyindex) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosServiceClassPolicyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosServiceClassPolicyTable.DocsQosServiceClassPolicyEntry, [u'docsqosserviceclasspolicyindex', u'docsqosserviceclasspolicyname', u'docsqosserviceclasspolicyrulepriority', u'docsqosserviceclasspolicystatus'], name, value)


    class DocsQosPHSTable(Entity):
        """
        This table describes set of payload header
        suppression entries.
        
        .. attribute:: docsqosphsentry
        
        	A payload header suppression entry.  The ifIndex is an ifType of docsCableMaclayer(127). The index docsQosServiceFlowId selects one service flow from the cable MAC layer interface. The docsQosPktClassId index matches an index of the docsQosPktClassTable
        	**type**\: list of  		 :py:class:`DocsQosPHSEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPHSTable.DocsQosPHSEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosPHSTable, self).__init__()

            self.yang_name = "docsQosPHSTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosPHSEntry", ("docsqosphsentry", DOCSQOSMIB.DocsQosPHSTable.DocsQosPHSEntry))])
            self._leafs = OrderedDict()

            self.docsqosphsentry = YList(self)
            self._segment_path = lambda: "docsQosPHSTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosPHSTable, [], name, value)


        class DocsQosPHSEntry(Entity):
            """
            A payload header suppression entry. 
            The ifIndex is an ifType of docsCableMaclayer(127).
            The index docsQosServiceFlowId selects one
            service flow from the cable MAC layer interface.
            The docsQosPktClassId index matches an
            index of the docsQosPktClassTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            .. attribute:: docsqospktclassid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`docsqospktclassid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry>`
            
            .. attribute:: docsqosphsfield
            
            	Payload header suppression field defines the  bytes of the header which must be  suppressed/restored by the sending/receiving  device.  The number of octets in this object should be the same as the value of docsQosPHSSize
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsqosphsmask
            
            	Payload header suppression mask defines the  bit mask which used in combination with the docsQosPHSField defines which bytes in header must be suppressed/restored by the sending or receiving device.  Each bit of this bit mask corresponds to a byte in the docsQosPHSField, with the least  significant  bit corresponding to first byte of the docsQosPHSField.  Each bit of the bit mask specifies whether of not the corresponding byte should be suppressed in the packet. A bit value of '1' indicates that the byte should be suppressed by the sending  device and restored by the receiving device.  A bit value of '0' indicates that  the byte should not be suppressed by the sending device or restored by the receiving device.  If the bit mask does not contain a bit for each byte in the docsQosPHSField then the bit mask is extended with bit values of '1' to be the necessary length
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: docsqosphssize
            
            	Payload header suppression size specifies the  number of bytes in the header to be suppressed and restored.  The value of this object must match the number of bytes in the docsQosPHSField
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsqosphsverify
            
            	Payload header suppression verification value of 'true' the sender must verify docsQosPHSField  is the same as what is contained in the packet to be suppressed
            	**type**\: bool
            
            .. attribute:: docsqosphsclassifierindex
            
            	This object is obsolete
            	**type**\: int
            
            	**range:** 1..65535
            
            	**status**\: obsolete
            
            .. attribute:: docsqosphsindex
            
            	Payload header suppression index uniquely  references the PHS rule for a given service flow
            	**type**\: int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosPHSTable.DocsQosPHSEntry, self).__init__()

                self.yang_name = "docsQosPHSEntry"
                self.yang_parent_name = "docsQosPHSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid','docsqospktclassid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqospktclassid', (YLeaf(YType.str, 'docsQosPktClassId'), ['int'])),
                    ('docsqosphsfield', (YLeaf(YType.str, 'docsQosPHSField'), ['str'])),
                    ('docsqosphsmask', (YLeaf(YType.str, 'docsQosPHSMask'), ['str'])),
                    ('docsqosphssize', (YLeaf(YType.int32, 'docsQosPHSSize'), ['int'])),
                    ('docsqosphsverify', (YLeaf(YType.boolean, 'docsQosPHSVerify'), ['bool'])),
                    ('docsqosphsclassifierindex', (YLeaf(YType.int32, 'docsQosPHSClassifierIndex'), ['int'])),
                    ('docsqosphsindex', (YLeaf(YType.int32, 'docsQosPHSIndex'), ['int'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqospktclassid = None
                self.docsqosphsfield = None
                self.docsqosphsmask = None
                self.docsqosphssize = None
                self.docsqosphsverify = None
                self.docsqosphsclassifierindex = None
                self.docsqosphsindex = None
                self._segment_path = lambda: "docsQosPHSEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']" + "[docsQosPktClassId='" + str(self.docsqospktclassid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosPHSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosPHSTable.DocsQosPHSEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqospktclassid', u'docsqosphsfield', u'docsqosphsmask', u'docsqosphssize', u'docsqosphsverify', u'docsqosphsclassifierindex', u'docsqosphsindex'], name, value)


    class DocsQosCmtsMacToSrvFlowTable(Entity):
        """
        This table provide for referencing the service flows 
        associated with a particular cable modem. This allows 
        for indexing into other docsQos tables that are 
        indexed by docsQosServiceFlowId and ifIndex.
        
        .. attribute:: docsqoscmtsmactosrvflowentry
        
        	An entry is created by CMTS for each service flow  connected to this CMTS
        	**type**\: list of  		 :py:class:`DocsQosCmtsMacToSrvFlowEntry <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable.DocsQosCmtsMacToSrvFlowEntry>`
        
        

        """

        _prefix = 'DOCS-QOS-MIB'
        _revision = '2001-11-09'

        def __init__(self):
            super(DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable, self).__init__()

            self.yang_name = "docsQosCmtsMacToSrvFlowTable"
            self.yang_parent_name = "DOCS-QOS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsQosCmtsMacToSrvFlowEntry", ("docsqoscmtsmactosrvflowentry", DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable.DocsQosCmtsMacToSrvFlowEntry))])
            self._leafs = OrderedDict()

            self.docsqoscmtsmactosrvflowentry = YList(self)
            self._segment_path = lambda: "docsQosCmtsMacToSrvFlowTable"
            self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable, [], name, value)


        class DocsQosCmtsMacToSrvFlowEntry(Entity):
            """
            An entry is created by CMTS for each service flow 
            connected to this CMTS.
            
            .. attribute:: docsqoscmtscmmac  (key)
            
            	The MAC address for the referenced CM
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsqoscmtsserviceflowid  (key)
            
            	An index assigned to a service flow by CMTS
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsqoscmtsifindex
            
            	The ifIndex of ifType docsCableMacLayter(127)  on the CMTS that is connected to the Cable Modem
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'DOCS-QOS-MIB'
            _revision = '2001-11-09'

            def __init__(self):
                super(DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable.DocsQosCmtsMacToSrvFlowEntry, self).__init__()

                self.yang_name = "docsQosCmtsMacToSrvFlowEntry"
                self.yang_parent_name = "docsQosCmtsMacToSrvFlowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsqoscmtscmmac','docsqoscmtsserviceflowid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsqoscmtscmmac', (YLeaf(YType.str, 'docsQosCmtsCmMac'), ['str'])),
                    ('docsqoscmtsserviceflowid', (YLeaf(YType.uint32, 'docsQosCmtsServiceFlowId'), ['int'])),
                    ('docsqoscmtsifindex', (YLeaf(YType.int32, 'docsQosCmtsIfIndex'), ['int'])),
                ])
                self.docsqoscmtscmmac = None
                self.docsqoscmtsserviceflowid = None
                self.docsqoscmtsifindex = None
                self._segment_path = lambda: "docsQosCmtsMacToSrvFlowEntry" + "[docsQosCmtsCmMac='" + str(self.docsqoscmtscmmac) + "']" + "[docsQosCmtsServiceFlowId='" + str(self.docsqoscmtsserviceflowid) + "']"
                self._absolute_path = lambda: "DOCS-QOS-MIB:DOCS-QOS-MIB/docsQosCmtsMacToSrvFlowTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSQOSMIB.DocsQosCmtsMacToSrvFlowTable.DocsQosCmtsMacToSrvFlowEntry, [u'docsqoscmtscmmac', u'docsqoscmtsserviceflowid', u'docsqoscmtsifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = DOCSQOSMIB()
        return self._top_entity

