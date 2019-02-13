""" CISCO_IETF_PW_MPLS_MIB 

This MIB complements the CISCO\-IETF\-PW\-MIB for PW operation 
over MPLS. 

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIETFPWMPLSMIB(Entity):
    """
    
    
    .. attribute:: cpwvcmplsobjects
    
    	
    	**type**\:  :py:class:`CpwVcMplsObjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsObjects>`
    
    	**config**\: False
    
    .. attribute:: cpwvcmplstable
    
    	This table specifies information for VC to be carried over   MPLS PSN
    	**type**\:  :py:class:`CpwVcMplsTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcmplsoutboundtable
    
    	This table associates VCs using MPLS PSN with the outbound  MPLS tunnels (i.e. toward the PSN) or the physical   interface in case of VC only
    	**type**\:  :py:class:`CpwVcMplsOutboundTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcmplsinboundtable
    
    	This table associates VCs using MPLS PSN with the inbound  MPLS tunnels (i.e. for packets coming from the PSN),   if such association is desired (mainly for security   reasons)
    	**type**\:  :py:class:`CpwVcMplsInboundTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcmplsnontemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in non\-  TE applications
    	**type**\:  :py:class:`CpwVcMplsNonTeMappingTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcmplstemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in   MPLS\-TE applications
    	**type**\:  :py:class:`CpwVcMplsTeMappingTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IETF-PW-MPLS-MIB'
    _revision = '2003-02-26'

    def __init__(self):
        super(CISCOIETFPWMPLSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-MPLS-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpwVcMplsObjects", ("cpwvcmplsobjects", CISCOIETFPWMPLSMIB.CpwVcMplsObjects)), ("cpwVcMplsTable", ("cpwvcmplstable", CISCOIETFPWMPLSMIB.CpwVcMplsTable)), ("cpwVcMplsOutboundTable", ("cpwvcmplsoutboundtable", CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable)), ("cpwVcMplsInboundTable", ("cpwvcmplsinboundtable", CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable)), ("cpwVcMplsNonTeMappingTable", ("cpwvcmplsnontemappingtable", CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable)), ("cpwVcMplsTeMappingTable", ("cpwvcmplstemappingtable", CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable))])
        self._leafs = OrderedDict()

        self.cpwvcmplsobjects = CISCOIETFPWMPLSMIB.CpwVcMplsObjects()
        self.cpwvcmplsobjects.parent = self
        self._children_name_map["cpwvcmplsobjects"] = "cpwVcMplsObjects"

        self.cpwvcmplstable = CISCOIETFPWMPLSMIB.CpwVcMplsTable()
        self.cpwvcmplstable.parent = self
        self._children_name_map["cpwvcmplstable"] = "cpwVcMplsTable"

        self.cpwvcmplsoutboundtable = CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable()
        self.cpwvcmplsoutboundtable.parent = self
        self._children_name_map["cpwvcmplsoutboundtable"] = "cpwVcMplsOutboundTable"

        self.cpwvcmplsinboundtable = CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable()
        self.cpwvcmplsinboundtable.parent = self
        self._children_name_map["cpwvcmplsinboundtable"] = "cpwVcMplsInboundTable"

        self.cpwvcmplsnontemappingtable = CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable()
        self.cpwvcmplsnontemappingtable.parent = self
        self._children_name_map["cpwvcmplsnontemappingtable"] = "cpwVcMplsNonTeMappingTable"

        self.cpwvcmplstemappingtable = CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable()
        self.cpwvcmplstemappingtable.parent = self
        self._children_name_map["cpwvcmplstemappingtable"] = "cpwVcMplsTeMappingTable"
        self._segment_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIETFPWMPLSMIB, [], name, value)


    class CpwVcMplsObjects(Entity):
        """
        
        
        .. attribute:: cpwvcmplsoutboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsOutboundIndex when creating  entries in the cpwVcMplsOutboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsOutboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cpwvcmplsinboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsInboundIndex when creating  entries in the cpwVcMplsInboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsInboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsObjects, self).__init__()

            self.yang_name = "cpwVcMplsObjects"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpwvcmplsoutboundindexnext', (YLeaf(YType.uint32, 'cpwVcMplsOutboundIndexNext'), ['int'])),
                ('cpwvcmplsinboundindexnext', (YLeaf(YType.uint32, 'cpwVcMplsInboundIndexNext'), ['int'])),
            ])
            self.cpwvcmplsoutboundindexnext = None
            self.cpwvcmplsinboundindexnext = None
            self._segment_path = lambda: "cpwVcMplsObjects"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsObjects, ['cpwvcmplsoutboundindexnext', 'cpwvcmplsinboundindexnext'], name, value)



    class CpwVcMplsTable(Entity):
        """
        This table specifies information for VC to be carried over  
        MPLS PSN.
        
        .. attribute:: cpwvcmplsentry
        
        	A row in this table represents parameters specific to MPLS   PSN for a pseudo wire connection (VC). The row is created   automatically by the local agent if the cpwVcPsnType is   MPLS. It is indexed by cpwVcIndex, which uniquely   identifying a singular connection. 
        	**type**\: list of  		 :py:class:`CpwVcMplsEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsTable, self).__init__()

            self.yang_name = "cpwVcMplsTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcMplsEntry", ("cpwvcmplsentry", CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsTable, [], name, value)


        class CpwVcMplsEntry(Entity):
            """
            A row in this table represents parameters specific to MPLS  
            PSN for a pseudo wire connection (VC). The row is created  
            automatically by the local agent if the cpwVcPsnType is  
            MPLS. It is indexed by cpwVcIndex, which uniquely  
            identifying a singular connection. 
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsmplstype
            
            	Set by the operator to indicate the outer tunnel types, if  exists. mplsTe is used if the outer tunnel was set\-up by   MPLS\-TE, and mplsNonTe is used the outer tunnel was set up  by LDP or manually. Combination of mplsTe and mplsNonTe   may exist in case of outer tunnel protection.  vcOnly is used if there is no outer tunnel label. vcOnly   cannot be combined with mplsNonTe or mplsTe
            	**type**\:  :py:class:`CpwVcMplsMplsType <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsMplsType>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsexpbitsmode
            
            	Set by the operator to indicate the way the VC shim label  EXP bits are to be determined. The value of outerTunnel(1)  is used where there is an outer tunnel \- cpwVcMplsMplsType   is mplsTe or mplsNonTe. Note that in this case there is no  need to mark the VC label with the EXP bits since the VC   label is not visible to the intermediate nodes.  If there is no outer tunnel, specifiedValue(2) indicate   that the value is specified by cpwVcMplsExpBits, and   serviceDependant(3) indicate that the EXP bits are setup   based on a rule specified in the emulated service specific   tables, for example when the EXP bits are a function of   802.1p marking for Ethernet emulated service
            	**type**\:  :py:class:`CpwVcMplsExpBitsMode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsexpbits
            
            	Set by the operator to indicate the MPLS EXP bits to be   used on the VC shim label if cpwVcMplsExpBitsMode is    specifiedValue(2), zero otherwise
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsttl
            
            	Set by the operator to indicate the VC TTL bits to be used  on the VC shim label
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cpwvcmplslocalldpid
            
            	The local LDP identifier of the LDP entity creating  this VC in the local node. As the VC labels are always  set from the per platform label space, the last two octets   in the LDP ID MUST be always both zeros
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cpwvcmplslocalldpentityid
            
            	The local LDP Entity index of the LDP entity to be used   for this VC on the local node. Should be set to all zeros   if not used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplspeerldpid
            
            	The peer LDP identifier as identified from the LDP   session. Should be zero if not relevant or not known yet
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry, self).__init__()

                self.yang_name = "cpwVcMplsEntry"
                self.yang_parent_name = "cpwVcMplsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcmplsmplstype', (YLeaf(YType.bits, 'cpwVcMplsMplsType'), ['Bits'])),
                    ('cpwvcmplsexpbitsmode', (YLeaf(YType.enumeration, 'cpwVcMplsExpBitsMode'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB', 'CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode')])),
                    ('cpwvcmplsexpbits', (YLeaf(YType.uint32, 'cpwVcMplsExpBits'), ['int'])),
                    ('cpwvcmplsttl', (YLeaf(YType.uint32, 'cpwVcMplsTtl'), ['int'])),
                    ('cpwvcmplslocalldpid', (YLeaf(YType.str, 'cpwVcMplsLocalLdpID'), ['str'])),
                    ('cpwvcmplslocalldpentityid', (YLeaf(YType.uint32, 'cpwVcMplsLocalLdpEntityID'), ['int'])),
                    ('cpwvcmplspeerldpid', (YLeaf(YType.str, 'cpwVcMplsPeerLdpID'), ['str'])),
                    ('cpwvcmplsstoragetype', (YLeaf(YType.enumeration, 'cpwVcMplsStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cpwvcindex = None
                self.cpwvcmplsmplstype = Bits()
                self.cpwvcmplsexpbitsmode = None
                self.cpwvcmplsexpbits = None
                self.cpwvcmplsttl = None
                self.cpwvcmplslocalldpid = None
                self.cpwvcmplslocalldpentityid = None
                self.cpwvcmplspeerldpid = None
                self.cpwvcmplsstoragetype = None
                self._segment_path = lambda: "cpwVcMplsEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry, ['cpwvcindex', 'cpwvcmplsmplstype', 'cpwvcmplsexpbitsmode', 'cpwvcmplsexpbits', 'cpwvcmplsttl', 'cpwvcmplslocalldpid', 'cpwvcmplslocalldpentityid', 'cpwvcmplspeerldpid', 'cpwvcmplsstoragetype'], name, value)

            class CpwVcMplsExpBitsMode(Enum):
                """
                CpwVcMplsExpBitsMode (Enum Class)

                Set by the operator to indicate the way the VC shim label 

                EXP bits are to be determined. The value of outerTunnel(1) 

                is used where there is an outer tunnel \- cpwVcMplsMplsType  

                is mplsTe or mplsNonTe. Note that in this case there is no 

                need to mark the VC label with the EXP bits since the VC  

                label is not visible to the intermediate nodes. 

                If there is no outer tunnel, specifiedValue(2) indicate  

                that the value is specified by cpwVcMplsExpBits, and  

                serviceDependant(3) indicate that the EXP bits are setup  

                based on a rule specified in the emulated service specific  

                tables, for example when the EXP bits are a function of  

                802.1p marking for Ethernet emulated service.

                .. data:: outerTunnel = 1

                .. data:: specifiedValue = 2

                .. data:: serviceDependant = 3

                """

                outerTunnel = Enum.YLeaf(1, "outerTunnel")

                specifiedValue = Enum.YLeaf(2, "specifiedValue")

                serviceDependant = Enum.YLeaf(3, "serviceDependant")





    class CpwVcMplsOutboundTable(Entity):
        """
        This table associates VCs using MPLS PSN with the outbound 
        MPLS tunnels (i.e. toward the PSN) or the physical  
        interface in case of VC only.
        
        .. attribute:: cpwvcmplsoutboundentry
        
        	A row in this table represents a link between PW VC (that  require MPLS tunnels) and MPLS tunnel toward the PSN.  In the case of VC only, it associate the VC with the   interface that shall carry the VC.  This table is indexed by the pwVcIndex and an additional  index enabling multiple rows for the same VC index.   At least one entry is created in this table by the operator   for each PW VC that requires MPLS PSN. Note that the first  entry for each VC can be indexed by cpwVcMplsOutboundIndex   equal zero without a need for retrieval of   cpwVcMplsOutboundIndexNext.   This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of   a TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.  In case of Non\-TE MPLS (an outer tunnel label assigned by   LDP or manually) the table points to the XC entry in the   LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>.  In case of VC only (no outer tunnel) the ifIndex of the  port to carry the VC is configured.    Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of  		 :py:class:`CpwVcMplsOutboundEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable, self).__init__()

            self.yang_name = "cpwVcMplsOutboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcMplsOutboundEntry", ("cpwvcmplsoutboundentry", CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsoutboundentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsOutboundTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable, [], name, value)


        class CpwVcMplsOutboundEntry(Entity):
            """
            A row in this table represents a link between PW VC (that 
            require MPLS tunnels) and MPLS tunnel toward the PSN. 
            In the case of VC only, it associate the VC with the  
            interface that shall carry the VC. 
            This table is indexed by the pwVcIndex and an additional 
            index enabling multiple rows for the same VC index. 
            
            At least one entry is created in this table by the operator  
            for each PW VC that requires MPLS PSN. Note that the first 
            entry for each VC can be indexed by cpwVcMplsOutboundIndex  
            equal zero without a need for retrieval of  
            cpwVcMplsOutboundIndexNext. 
            
            This table points to the appropriate MPLS MIB. In the case  
            of MPLS\-TE, the 4 variables relevant to the indexing of  
            a TE MPLS tunnel are set as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-te\-mib>. 
            In case of Non\-TE MPLS (an outer tunnel label assigned by  
            LDP or manually) the table points to the XC entry in the  
            LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>. 
            In case of VC only (no outer tunnel) the ifIndex of the 
            port to carry the VC is configured.  
            
            Each VC may have multiple rows in this tables if protection  
            is available at the outer tunnel level, each row may be of 
            different type except for VC only, on which only rows with 
            ifIndex of the port are allowed. 
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundindex  (key)
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved   using cpwVcMplsOutboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundlsrxcindex
            
            	This object will be set by the operator. If the outer  label is defined in the MPL\-LSR\-MIB, i.e. set by LDP  or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundifindex
            
            	In case of VC only (no outer tunnel), this object holds  the ifIndex of the outbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsoutboundstoragetype
            
            	This variable indicates the storage type for this object
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry, self).__init__()

                self.yang_name = "cpwVcMplsOutboundEntry"
                self.yang_parent_name = "cpwVcMplsOutboundTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcmplsoutboundindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcmplsoutboundindex', (YLeaf(YType.uint32, 'cpwVcMplsOutboundIndex'), ['int'])),
                    ('cpwvcmplsoutboundlsrxcindex', (YLeaf(YType.uint32, 'cpwVcMplsOutboundLsrXcIndex'), ['int'])),
                    ('cpwvcmplsoutboundtunnelindex', (YLeaf(YType.uint32, 'cpwVcMplsOutboundTunnelIndex'), ['int'])),
                    ('cpwvcmplsoutboundtunnelinstance', (YLeaf(YType.uint32, 'cpwVcMplsOutboundTunnelInstance'), ['int'])),
                    ('cpwvcmplsoutboundtunnellcllsr', (YLeaf(YType.str, 'cpwVcMplsOutboundTunnelLclLSR'), ['str'])),
                    ('cpwvcmplsoutboundtunnelpeerlsr', (YLeaf(YType.str, 'cpwVcMplsOutboundTunnelPeerLSR'), ['str'])),
                    ('cpwvcmplsoutboundifindex', (YLeaf(YType.int32, 'cpwVcMplsOutboundIfIndex'), ['int'])),
                    ('cpwvcmplsoutboundrowstatus', (YLeaf(YType.enumeration, 'cpwVcMplsOutboundRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cpwvcmplsoutboundstoragetype', (YLeaf(YType.enumeration, 'cpwVcMplsOutboundStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cpwvcindex = None
                self.cpwvcmplsoutboundindex = None
                self.cpwvcmplsoutboundlsrxcindex = None
                self.cpwvcmplsoutboundtunnelindex = None
                self.cpwvcmplsoutboundtunnelinstance = None
                self.cpwvcmplsoutboundtunnellcllsr = None
                self.cpwvcmplsoutboundtunnelpeerlsr = None
                self.cpwvcmplsoutboundifindex = None
                self.cpwvcmplsoutboundrowstatus = None
                self.cpwvcmplsoutboundstoragetype = None
                self._segment_path = lambda: "cpwVcMplsOutboundEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwVcMplsOutboundIndex='" + str(self.cpwvcmplsoutboundindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsOutboundTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry, ['cpwvcindex', 'cpwvcmplsoutboundindex', 'cpwvcmplsoutboundlsrxcindex', 'cpwvcmplsoutboundtunnelindex', 'cpwvcmplsoutboundtunnelinstance', 'cpwvcmplsoutboundtunnellcllsr', 'cpwvcmplsoutboundtunnelpeerlsr', 'cpwvcmplsoutboundifindex', 'cpwvcmplsoutboundrowstatus', 'cpwvcmplsoutboundstoragetype'], name, value)




    class CpwVcMplsInboundTable(Entity):
        """
        This table associates VCs using MPLS PSN with the inbound 
        MPLS tunnels (i.e. for packets coming from the PSN),  
        if such association is desired (mainly for security  
        reasons).
        
        .. attribute:: cpwvcmplsinboundentry
        
        	A row in this table represents a link between PW VCs (that  require MPLS tunnels) and MPLS tunnel for packets arriving  from the PSN.  This table is indexed by the set of indexes used to  identify the VC \- cpwVcIndex and an additional  index enabling multiple rows for the same VC index.   Note that the first entry for each VC can be indexed by   cpwVcMplsOutboundIndex equal zero without a need for   retrieval of cpwVcMplsInboundIndexNext.   An entry is created in this table either automatically by   the local agent or created manually by the operator in   cases that strict mode is required.   Note that the control messages contain VC ID and VC type,   which together with the remote IP address identify the  cpwVcIndex in the local node.  This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of a  TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.   In case of non\-TE MPLS tunnel (an outer tunnel label   assigned by LDP or manually) the table points to the XC   entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\-  ietf\-mpls\-lsr\-mib>.   Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of  		 :py:class:`CpwVcMplsInboundEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable, self).__init__()

            self.yang_name = "cpwVcMplsInboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcMplsInboundEntry", ("cpwvcmplsinboundentry", CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsinboundentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsInboundTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable, [], name, value)


        class CpwVcMplsInboundEntry(Entity):
            """
            A row in this table represents a link between PW VCs (that 
            require MPLS tunnels) and MPLS tunnel for packets arriving 
            from the PSN. 
            This table is indexed by the set of indexes used to 
            identify the VC \- cpwVcIndex and an additional 
            index enabling multiple rows for the same VC index. 
            
            Note that the first entry for each VC can be indexed by  
            cpwVcMplsOutboundIndex equal zero without a need for  
            retrieval of cpwVcMplsInboundIndexNext. 
            
            An entry is created in this table either automatically by  
            the local agent or created manually by the operator in  
            cases that strict mode is required. 
            
            Note that the control messages contain VC ID and VC type,  
            which together with the remote IP address identify the 
            cpwVcIndex in the local node. 
            This table points to the appropriate MPLS MIB. In the case  
            of MPLS\-TE, the 4 variables relevant to the indexing of a 
            TE MPLS tunnel are set as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-te\-mib>. 
            
            In case of non\-TE MPLS tunnel (an outer tunnel label  
            assigned by LDP or manually) the table points to the XC  
            entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-lsr\-mib>. 
            
            Each VC may have multiple rows in this tables if protection  
            is available at the outer tunnel level, each row may be of 
            different type except for VC only, on which only rows with 
            ifIndex of the port are allowed. 
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundindex  (key)
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved  using cpwVcMplsInboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundlsrxcindex
            
            	If the outer label is defined in the MPL\-LSR\-MIB, i.e. set   by LDP or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundifindex
            
            	In case of VC only (no outer tunnel), this object holds the  ifIndex of the inbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsinboundstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry, self).__init__()

                self.yang_name = "cpwVcMplsInboundEntry"
                self.yang_parent_name = "cpwVcMplsInboundTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcmplsinboundindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcmplsinboundindex', (YLeaf(YType.uint32, 'cpwVcMplsInboundIndex'), ['int'])),
                    ('cpwvcmplsinboundlsrxcindex', (YLeaf(YType.uint32, 'cpwVcMplsInboundLsrXcIndex'), ['int'])),
                    ('cpwvcmplsinboundtunnelindex', (YLeaf(YType.uint32, 'cpwVcMplsInboundTunnelIndex'), ['int'])),
                    ('cpwvcmplsinboundtunnelinstance', (YLeaf(YType.uint32, 'cpwVcMplsInboundTunnelInstance'), ['int'])),
                    ('cpwvcmplsinboundtunnellcllsr', (YLeaf(YType.str, 'cpwVcMplsInboundTunnelLclLSR'), ['str'])),
                    ('cpwvcmplsinboundtunnelpeerlsr', (YLeaf(YType.str, 'cpwVcMplsInboundTunnelPeerLSR'), ['str'])),
                    ('cpwvcmplsinboundifindex', (YLeaf(YType.int32, 'cpwVcMplsInboundIfIndex'), ['int'])),
                    ('cpwvcmplsinboundrowstatus', (YLeaf(YType.enumeration, 'cpwVcMplsInboundRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cpwvcmplsinboundstoragetype', (YLeaf(YType.enumeration, 'cpwVcMplsInboundStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cpwvcindex = None
                self.cpwvcmplsinboundindex = None
                self.cpwvcmplsinboundlsrxcindex = None
                self.cpwvcmplsinboundtunnelindex = None
                self.cpwvcmplsinboundtunnelinstance = None
                self.cpwvcmplsinboundtunnellcllsr = None
                self.cpwvcmplsinboundtunnelpeerlsr = None
                self.cpwvcmplsinboundifindex = None
                self.cpwvcmplsinboundrowstatus = None
                self.cpwvcmplsinboundstoragetype = None
                self._segment_path = lambda: "cpwVcMplsInboundEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwVcMplsInboundIndex='" + str(self.cpwvcmplsinboundindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsInboundTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry, ['cpwvcindex', 'cpwvcmplsinboundindex', 'cpwvcmplsinboundlsrxcindex', 'cpwvcmplsinboundtunnelindex', 'cpwvcmplsinboundtunnelinstance', 'cpwvcmplsinboundtunnellcllsr', 'cpwvcmplsinboundtunnelpeerlsr', 'cpwvcmplsinboundifindex', 'cpwvcmplsinboundrowstatus', 'cpwvcmplsinboundstoragetype'], name, value)




    class CpwVcMplsNonTeMappingTable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in non\- 
        TE applications.
        
        .. attribute:: cpwvcmplsnontemappingentry
        
        	A row in this table represents the association  between the PW VC and it's non TE MPLS outer Tunnel  it's physical interface if there is no outer tunnel   (VC only).   An application can use this table to quickly retrieve the   PW carried over specific non\-TE MPLS outer tunnel or   physical interface.   The table in indexed by the XC index for MPLS Non\-TE   tunnel, or ifIndex of the port in VC only case, the   direction of the VC in the specific entry and the VCIndex.   The same table is used in both inbound and outbound  directions, but in a different row for each direction. If   the inbound association is not known, no rows should exist   for it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of  		 :py:class:`CpwVcMplsNonTeMappingEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable, self).__init__()

            self.yang_name = "cpwVcMplsNonTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcMplsNonTeMappingEntry", ("cpwvcmplsnontemappingentry", CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsnontemappingentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsNonTeMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable, [], name, value)


        class CpwVcMplsNonTeMappingEntry(Entity):
            """
            A row in this table represents the association 
            between the PW VC and it's non TE MPLS outer Tunnel 
            it's physical interface if there is no outer tunnel  
            (VC only). 
            
            An application can use this table to quickly retrieve the  
            PW carried over specific non\-TE MPLS outer tunnel or  
            physical interface. 
            
            The table in indexed by the XC index for MPLS Non\-TE  
            tunnel, or ifIndex of the port in VC only case, the  
            direction of the VC in the specific entry and the VCIndex. 
            
            The same table is used in both inbound and outbound 
            directions, but in a different row for each direction. If  
            the inbound association is not known, no rows should exist  
            for it. 
            
            Rows are created by the local agent when all the  
            association data is available for display.
            
            .. attribute:: cpwvcmplsnontemappingtunneldirection  (key)
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:  :py:class:`CpwVcMplsNonTeMappingTunnelDirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsnontemappingxctunnelindex  (key)
            
            	Index for the conceptual XC row identifying Tunnel to VC   mappings when the outer tunnel is created by the MPLS\-LSR\-  MIB, Zero otherwise
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsnontemappingifindex  (key)
            
            	Identify the port on which the VC is carried for VC only   case
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwvcmplsnontemappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry, self).__init__()

                self.yang_name = "cpwVcMplsNonTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsNonTeMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcmplsnontemappingtunneldirection','cpwvcmplsnontemappingxctunnelindex','cpwvcmplsnontemappingifindex','cpwvcmplsnontemappingvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcmplsnontemappingtunneldirection', (YLeaf(YType.enumeration, 'cpwVcMplsNonTeMappingTunnelDirection'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB', 'CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection')])),
                    ('cpwvcmplsnontemappingxctunnelindex', (YLeaf(YType.uint32, 'cpwVcMplsNonTeMappingXcTunnelIndex'), ['int'])),
                    ('cpwvcmplsnontemappingifindex', (YLeaf(YType.int32, 'cpwVcMplsNonTeMappingIfIndex'), ['int'])),
                    ('cpwvcmplsnontemappingvcindex', (YLeaf(YType.uint32, 'cpwVcMplsNonTeMappingVcIndex'), ['int'])),
                ])
                self.cpwvcmplsnontemappingtunneldirection = None
                self.cpwvcmplsnontemappingxctunnelindex = None
                self.cpwvcmplsnontemappingifindex = None
                self.cpwvcmplsnontemappingvcindex = None
                self._segment_path = lambda: "cpwVcMplsNonTeMappingEntry" + "[cpwVcMplsNonTeMappingTunnelDirection='" + str(self.cpwvcmplsnontemappingtunneldirection) + "']" + "[cpwVcMplsNonTeMappingXcTunnelIndex='" + str(self.cpwvcmplsnontemappingxctunnelindex) + "']" + "[cpwVcMplsNonTeMappingIfIndex='" + str(self.cpwvcmplsnontemappingifindex) + "']" + "[cpwVcMplsNonTeMappingVcIndex='" + str(self.cpwvcmplsnontemappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsNonTeMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry, ['cpwvcmplsnontemappingtunneldirection', 'cpwvcmplsnontemappingxctunnelindex', 'cpwvcmplsnontemappingifindex', 'cpwvcmplsnontemappingvcindex'], name, value)

            class CpwVcMplsNonTeMappingTunnelDirection(Enum):
                """
                CpwVcMplsNonTeMappingTunnelDirection (Enum Class)

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = Enum.YLeaf(1, "outbound")

                inbound = Enum.YLeaf(2, "inbound")





    class CpwVcMplsTeMappingTable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in  
        MPLS\-TE applications.
        
        .. attribute:: cpwvcmplstemappingentry
        
        	A row in this table represents the association  between a PW VC and it's MPLS\-TE outer Tunnel.   An application can use this table to quickly retrieve the   PW carried over specific TE MPLS outer tunnel.   The table in indexed by the 4 indexes of a TE tunnel,  the direction of the VC specific entry and the VcIndex.   The same table is used in both inbound and outbound  directions, a different row for each direction. If the   inbound association is not known, no rows should exist for   it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of  		 :py:class:`CpwVcMplsTeMappingEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable, self).__init__()

            self.yang_name = "cpwVcMplsTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcMplsTeMappingEntry", ("cpwvcmplstemappingentry", CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry))])
            self._leafs = OrderedDict()

            self.cpwvcmplstemappingentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsTeMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable, [], name, value)


        class CpwVcMplsTeMappingEntry(Entity):
            """
            A row in this table represents the association 
            between a PW VC and it's MPLS\-TE outer Tunnel. 
            
            An application can use this table to quickly retrieve the  
            PW carried over specific TE MPLS outer tunnel. 
            
            The table in indexed by the 4 indexes of a TE tunnel, 
            the direction of the VC specific entry and the VcIndex. 
            
            The same table is used in both inbound and outbound 
            directions, a different row for each direction. If the  
            inbound association is not known, no rows should exist for  
            it. 
            
            Rows are created by the local agent when all the  
            association data is available for display.
            
            .. attribute:: cpwvcmplstemappingtunneldirection  (key)
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:  :py:class:`CpwVcMplsTeMappingTunnelDirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection>`
            
            	**config**\: False
            
            .. attribute:: cpwvcmplstemappingtunnelindex  (key)
            
            	Primary index for the conceptual row identifying the   MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cpwvcmplstemappingtunnelinstance  (key)
            
            	Identifies an instance of the MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwvcmplstemappingtunnelpeerlsrid  (key)
            
            	Identifies an Peer LSR when the outer tunnel is MPLS\-TE   based
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplstemappingtunnellocallsrid  (key)
            
            	Identifies the local LSR
            	**type**\: str
            
            	**length:** 4
            
            	**config**\: False
            
            .. attribute:: cpwvcmplstemappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry, self).__init__()

                self.yang_name = "cpwVcMplsTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsTeMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcmplstemappingtunneldirection','cpwvcmplstemappingtunnelindex','cpwvcmplstemappingtunnelinstance','cpwvcmplstemappingtunnelpeerlsrid','cpwvcmplstemappingtunnellocallsrid','cpwvcmplstemappingvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcmplstemappingtunneldirection', (YLeaf(YType.enumeration, 'cpwVcMplsTeMappingTunnelDirection'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB', 'CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection')])),
                    ('cpwvcmplstemappingtunnelindex', (YLeaf(YType.uint32, 'cpwVcMplsTeMappingTunnelIndex'), ['int'])),
                    ('cpwvcmplstemappingtunnelinstance', (YLeaf(YType.uint32, 'cpwVcMplsTeMappingTunnelInstance'), ['int'])),
                    ('cpwvcmplstemappingtunnelpeerlsrid', (YLeaf(YType.str, 'cpwVcMplsTeMappingTunnelPeerLsrID'), ['str'])),
                    ('cpwvcmplstemappingtunnellocallsrid', (YLeaf(YType.str, 'cpwVcMplsTeMappingTunnelLocalLsrID'), ['str'])),
                    ('cpwvcmplstemappingvcindex', (YLeaf(YType.uint32, 'cpwVcMplsTeMappingVcIndex'), ['int'])),
                ])
                self.cpwvcmplstemappingtunneldirection = None
                self.cpwvcmplstemappingtunnelindex = None
                self.cpwvcmplstemappingtunnelinstance = None
                self.cpwvcmplstemappingtunnelpeerlsrid = None
                self.cpwvcmplstemappingtunnellocallsrid = None
                self.cpwvcmplstemappingvcindex = None
                self._segment_path = lambda: "cpwVcMplsTeMappingEntry" + "[cpwVcMplsTeMappingTunnelDirection='" + str(self.cpwvcmplstemappingtunneldirection) + "']" + "[cpwVcMplsTeMappingTunnelIndex='" + str(self.cpwvcmplstemappingtunnelindex) + "']" + "[cpwVcMplsTeMappingTunnelInstance='" + str(self.cpwvcmplstemappingtunnelinstance) + "']" + "[cpwVcMplsTeMappingTunnelPeerLsrID='" + str(self.cpwvcmplstemappingtunnelpeerlsrid) + "']" + "[cpwVcMplsTeMappingTunnelLocalLsrID='" + str(self.cpwvcmplstemappingtunnellocallsrid) + "']" + "[cpwVcMplsTeMappingVcIndex='" + str(self.cpwvcmplstemappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsTeMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry, ['cpwvcmplstemappingtunneldirection', 'cpwvcmplstemappingtunnelindex', 'cpwvcmplstemappingtunnelinstance', 'cpwvcmplstemappingtunnelpeerlsrid', 'cpwvcmplstemappingtunnellocallsrid', 'cpwvcmplstemappingvcindex'], name, value)

            class CpwVcMplsTeMappingTunnelDirection(Enum):
                """
                CpwVcMplsTeMappingTunnelDirection (Enum Class)

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = Enum.YLeaf(1, "outbound")

                inbound = Enum.YLeaf(2, "inbound")




    def clone_ptr(self):
        self._top_entity = CISCOIETFPWMPLSMIB()
        return self._top_entity



