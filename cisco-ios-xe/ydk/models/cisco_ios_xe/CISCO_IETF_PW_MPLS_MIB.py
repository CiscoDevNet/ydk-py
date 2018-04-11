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
    
    	
    	**type**\:  :py:class:`Cpwvcmplsobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsobjects>`
    
    .. attribute:: cpwvcmplstable
    
    	This table specifies information for VC to be carried over   MPLS PSN
    	**type**\:  :py:class:`Cpwvcmplstable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstable>`
    
    .. attribute:: cpwvcmplsoutboundtable
    
    	This table associates VCs using MPLS PSN with the outbound  MPLS tunnels (i.e. toward the PSN) or the physical   interface in case of VC only
    	**type**\:  :py:class:`Cpwvcmplsoutboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable>`
    
    .. attribute:: cpwvcmplsinboundtable
    
    	This table associates VCs using MPLS PSN with the inbound  MPLS tunnels (i.e. for packets coming from the PSN),   if such association is desired (mainly for security   reasons)
    	**type**\:  :py:class:`Cpwvcmplsinboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable>`
    
    .. attribute:: cpwvcmplsnontemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in non\-  TE applications
    	**type**\:  :py:class:`Cpwvcmplsnontemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable>`
    
    .. attribute:: cpwvcmplstemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in   MPLS\-TE applications
    	**type**\:  :py:class:`Cpwvcmplstemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable>`
    
    

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
        self._child_container_classes = OrderedDict([("cpwVcMplsObjects", ("cpwvcmplsobjects", CISCOIETFPWMPLSMIB.Cpwvcmplsobjects)), ("cpwVcMplsTable", ("cpwvcmplstable", CISCOIETFPWMPLSMIB.Cpwvcmplstable)), ("cpwVcMplsOutboundTable", ("cpwvcmplsoutboundtable", CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable)), ("cpwVcMplsInboundTable", ("cpwvcmplsinboundtable", CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable)), ("cpwVcMplsNonTeMappingTable", ("cpwvcmplsnontemappingtable", CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable)), ("cpwVcMplsTeMappingTable", ("cpwvcmplstemappingtable", CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpwvcmplsobjects = CISCOIETFPWMPLSMIB.Cpwvcmplsobjects()
        self.cpwvcmplsobjects.parent = self
        self._children_name_map["cpwvcmplsobjects"] = "cpwVcMplsObjects"
        self._children_yang_names.add("cpwVcMplsObjects")

        self.cpwvcmplstable = CISCOIETFPWMPLSMIB.Cpwvcmplstable()
        self.cpwvcmplstable.parent = self
        self._children_name_map["cpwvcmplstable"] = "cpwVcMplsTable"
        self._children_yang_names.add("cpwVcMplsTable")

        self.cpwvcmplsoutboundtable = CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable()
        self.cpwvcmplsoutboundtable.parent = self
        self._children_name_map["cpwvcmplsoutboundtable"] = "cpwVcMplsOutboundTable"
        self._children_yang_names.add("cpwVcMplsOutboundTable")

        self.cpwvcmplsinboundtable = CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable()
        self.cpwvcmplsinboundtable.parent = self
        self._children_name_map["cpwvcmplsinboundtable"] = "cpwVcMplsInboundTable"
        self._children_yang_names.add("cpwVcMplsInboundTable")

        self.cpwvcmplsnontemappingtable = CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable()
        self.cpwvcmplsnontemappingtable.parent = self
        self._children_name_map["cpwvcmplsnontemappingtable"] = "cpwVcMplsNonTeMappingTable"
        self._children_yang_names.add("cpwVcMplsNonTeMappingTable")

        self.cpwvcmplstemappingtable = CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable()
        self.cpwvcmplstemappingtable.parent = self
        self._children_name_map["cpwvcmplstemappingtable"] = "cpwVcMplsTeMappingTable"
        self._children_yang_names.add("cpwVcMplsTeMappingTable")
        self._segment_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB"


    class Cpwvcmplsobjects(Entity):
        """
        
        
        .. attribute:: cpwvcmplsoutboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsOutboundIndex when creating  entries in the cpwVcMplsOutboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsOutboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcmplsinboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsInboundIndex when creating  entries in the cpwVcMplsInboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsInboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplsobjects, self).__init__()

            self.yang_name = "cpwVcMplsObjects"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpwvcmplsoutboundindexnext', YLeaf(YType.uint32, 'cpwVcMplsOutboundIndexNext')),
                ('cpwvcmplsinboundindexnext', YLeaf(YType.uint32, 'cpwVcMplsInboundIndexNext')),
            ])
            self.cpwvcmplsoutboundindexnext = None
            self.cpwvcmplsinboundindexnext = None
            self._segment_path = lambda: "cpwVcMplsObjects"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsobjects, ['cpwvcmplsoutboundindexnext', 'cpwvcmplsinboundindexnext'], name, value)


    class Cpwvcmplstable(Entity):
        """
        This table specifies information for VC to be carried over  
        MPLS PSN.
        
        .. attribute:: cpwvcmplsentry
        
        	A row in this table represents parameters specific to MPLS   PSN for a pseudo wire connection (VC). The row is created   automatically by the local agent if the cpwVcPsnType is   MPLS. It is indexed by cpwVcIndex, which uniquely   identifying a singular connection. 
        	**type**\: list of  		 :py:class:`Cpwvcmplsentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplstable, self).__init__()

            self.yang_name = "cpwVcMplsTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcMplsEntry", ("cpwvcmplsentry", CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplstable, [], name, value)


        class Cpwvcmplsentry(Entity):
            """
            A row in this table represents parameters specific to MPLS  
            PSN for a pseudo wire connection (VC). The row is created  
            automatically by the local agent if the cpwVcPsnType is  
            MPLS. It is indexed by cpwVcIndex, which uniquely  
            identifying a singular connection. 
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsmplstype
            
            	Set by the operator to indicate the outer tunnel types, if  exists. mplsTe is used if the outer tunnel was set\-up by   MPLS\-TE, and mplsNonTe is used the outer tunnel was set up  by LDP or manually. Combination of mplsTe and mplsNonTe   may exist in case of outer tunnel protection.  vcOnly is used if there is no outer tunnel label. vcOnly   cannot be combined with mplsNonTe or mplsTe
            	**type**\:  :py:class:`Cpwvcmplsmplstype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsmplstype>`
            
            .. attribute:: cpwvcmplsexpbitsmode
            
            	Set by the operator to indicate the way the VC shim label  EXP bits are to be determined. The value of outerTunnel(1)  is used where there is an outer tunnel \- cpwVcMplsMplsType   is mplsTe or mplsNonTe. Note that in this case there is no  need to mark the VC label with the EXP bits since the VC   label is not visible to the intermediate nodes.  If there is no outer tunnel, specifiedValue(2) indicate   that the value is specified by cpwVcMplsExpBits, and   serviceDependant(3) indicate that the EXP bits are setup   based on a rule specified in the emulated service specific   tables, for example when the EXP bits are a function of   802.1p marking for Ethernet emulated service
            	**type**\:  :py:class:`Cpwvcmplsexpbitsmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsexpbitsmode>`
            
            .. attribute:: cpwvcmplsexpbits
            
            	Set by the operator to indicate the MPLS EXP bits to be   used on the VC shim label if cpwVcMplsExpBitsMode is    specifiedValue(2), zero otherwise
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcmplsttl
            
            	Set by the operator to indicate the VC TTL bits to be used  on the VC shim label
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cpwvcmplslocalldpid
            
            	The local LDP identifier of the LDP entity creating  this VC in the local node. As the VC labels are always  set from the per platform label space, the last two octets   in the LDP ID MUST be always both zeros
            	**type**\: str
            
            .. attribute:: cpwvcmplslocalldpentityid
            
            	The local LDP Entity index of the LDP entity to be used   for this VC on the local node. Should be set to all zeros   if not used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplspeerldpid
            
            	The peer LDP identifier as identified from the LDP   session. Should be zero if not relevant or not known yet
            	**type**\: str
            
            .. attribute:: cpwvcmplsstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry, self).__init__()

                self.yang_name = "cpwVcMplsEntry"
                self.yang_parent_name = "cpwVcMplsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcmplsmplstype', YLeaf(YType.bits, 'cpwVcMplsMplsType')),
                    ('cpwvcmplsexpbitsmode', YLeaf(YType.enumeration, 'cpwVcMplsExpBitsMode')),
                    ('cpwvcmplsexpbits', YLeaf(YType.uint32, 'cpwVcMplsExpBits')),
                    ('cpwvcmplsttl', YLeaf(YType.uint32, 'cpwVcMplsTtl')),
                    ('cpwvcmplslocalldpid', YLeaf(YType.str, 'cpwVcMplsLocalLdpID')),
                    ('cpwvcmplslocalldpentityid', YLeaf(YType.uint32, 'cpwVcMplsLocalLdpEntityID')),
                    ('cpwvcmplspeerldpid', YLeaf(YType.str, 'cpwVcMplsPeerLdpID')),
                    ('cpwvcmplsstoragetype', YLeaf(YType.enumeration, 'cpwVcMplsStorageType')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplstable.Cpwvcmplsentry, ['cpwvcindex', 'cpwvcmplsmplstype', 'cpwvcmplsexpbitsmode', 'cpwvcmplsexpbits', 'cpwvcmplsttl', 'cpwvcmplslocalldpid', 'cpwvcmplslocalldpentityid', 'cpwvcmplspeerldpid', 'cpwvcmplsstoragetype'], name, value)

            class Cpwvcmplsexpbitsmode(Enum):
                """
                Cpwvcmplsexpbitsmode (Enum Class)

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



    class Cpwvcmplsoutboundtable(Entity):
        """
        This table associates VCs using MPLS PSN with the outbound 
        MPLS tunnels (i.e. toward the PSN) or the physical  
        interface in case of VC only.
        
        .. attribute:: cpwvcmplsoutboundentry
        
        	A row in this table represents a link between PW VC (that  require MPLS tunnels) and MPLS tunnel toward the PSN.  In the case of VC only, it associate the VC with the   interface that shall carry the VC.  This table is indexed by the pwVcIndex and an additional  index enabling multiple rows for the same VC index.   At least one entry is created in this table by the operator   for each PW VC that requires MPLS PSN. Note that the first  entry for each VC can be indexed by cpwVcMplsOutboundIndex   equal zero without a need for retrieval of   cpwVcMplsOutboundIndexNext.   This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of   a TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.  In case of Non\-TE MPLS (an outer tunnel label assigned by   LDP or manually) the table points to the XC entry in the   LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>.  In case of VC only (no outer tunnel) the ifIndex of the  port to carry the VC is configured.    Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of  		 :py:class:`Cpwvcmplsoutboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable, self).__init__()

            self.yang_name = "cpwVcMplsOutboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcMplsOutboundEntry", ("cpwvcmplsoutboundentry", CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsoutboundentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsOutboundTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable, [], name, value)


        class Cpwvcmplsoutboundentry(Entity):
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
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsoutboundindex  (key)
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved   using cpwVcMplsOutboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundlsrxcindex
            
            	This object will be set by the operator. If the outer  label is defined in the MPL\-LSR\-MIB, i.e. set by LDP  or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsoutboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsoutboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsoutboundifindex
            
            	In case of VC only (no outer tunnel), this object holds  the ifIndex of the outbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsoutboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cpwvcmplsoutboundstoragetype
            
            	This variable indicates the storage type for this object
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry, self).__init__()

                self.yang_name = "cpwVcMplsOutboundEntry"
                self.yang_parent_name = "cpwVcMplsOutboundTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcmplsoutboundindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcmplsoutboundindex', YLeaf(YType.uint32, 'cpwVcMplsOutboundIndex')),
                    ('cpwvcmplsoutboundlsrxcindex', YLeaf(YType.uint32, 'cpwVcMplsOutboundLsrXcIndex')),
                    ('cpwvcmplsoutboundtunnelindex', YLeaf(YType.uint32, 'cpwVcMplsOutboundTunnelIndex')),
                    ('cpwvcmplsoutboundtunnelinstance', YLeaf(YType.uint32, 'cpwVcMplsOutboundTunnelInstance')),
                    ('cpwvcmplsoutboundtunnellcllsr', YLeaf(YType.str, 'cpwVcMplsOutboundTunnelLclLSR')),
                    ('cpwvcmplsoutboundtunnelpeerlsr', YLeaf(YType.str, 'cpwVcMplsOutboundTunnelPeerLSR')),
                    ('cpwvcmplsoutboundifindex', YLeaf(YType.int32, 'cpwVcMplsOutboundIfIndex')),
                    ('cpwvcmplsoutboundrowstatus', YLeaf(YType.enumeration, 'cpwVcMplsOutboundRowStatus')),
                    ('cpwvcmplsoutboundstoragetype', YLeaf(YType.enumeration, 'cpwVcMplsOutboundStorageType')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry, ['cpwvcindex', 'cpwvcmplsoutboundindex', 'cpwvcmplsoutboundlsrxcindex', 'cpwvcmplsoutboundtunnelindex', 'cpwvcmplsoutboundtunnelinstance', 'cpwvcmplsoutboundtunnellcllsr', 'cpwvcmplsoutboundtunnelpeerlsr', 'cpwvcmplsoutboundifindex', 'cpwvcmplsoutboundrowstatus', 'cpwvcmplsoutboundstoragetype'], name, value)


    class Cpwvcmplsinboundtable(Entity):
        """
        This table associates VCs using MPLS PSN with the inbound 
        MPLS tunnels (i.e. for packets coming from the PSN),  
        if such association is desired (mainly for security  
        reasons).
        
        .. attribute:: cpwvcmplsinboundentry
        
        	A row in this table represents a link between PW VCs (that  require MPLS tunnels) and MPLS tunnel for packets arriving  from the PSN.  This table is indexed by the set of indexes used to  identify the VC \- cpwVcIndex and an additional  index enabling multiple rows for the same VC index.   Note that the first entry for each VC can be indexed by   cpwVcMplsOutboundIndex equal zero without a need for   retrieval of cpwVcMplsInboundIndexNext.   An entry is created in this table either automatically by   the local agent or created manually by the operator in   cases that strict mode is required.   Note that the control messages contain VC ID and VC type,   which together with the remote IP address identify the  cpwVcIndex in the local node.  This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of a  TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.   In case of non\-TE MPLS tunnel (an outer tunnel label   assigned by LDP or manually) the table points to the XC   entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\-  ietf\-mpls\-lsr\-mib>.   Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of  		 :py:class:`Cpwvcmplsinboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable, self).__init__()

            self.yang_name = "cpwVcMplsInboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcMplsInboundEntry", ("cpwvcmplsinboundentry", CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsinboundentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsInboundTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable, [], name, value)


        class Cpwvcmplsinboundentry(Entity):
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
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsinboundindex  (key)
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved  using cpwVcMplsInboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundlsrxcindex
            
            	If the outer label is defined in the MPL\-LSR\-MIB, i.e. set   by LDP or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsinboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsinboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsinboundifindex
            
            	In case of VC only (no outer tunnel), this object holds the  ifIndex of the inbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsinboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cpwvcmplsinboundstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry, self).__init__()

                self.yang_name = "cpwVcMplsInboundEntry"
                self.yang_parent_name = "cpwVcMplsInboundTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcmplsinboundindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwvcmplsinboundindex', YLeaf(YType.uint32, 'cpwVcMplsInboundIndex')),
                    ('cpwvcmplsinboundlsrxcindex', YLeaf(YType.uint32, 'cpwVcMplsInboundLsrXcIndex')),
                    ('cpwvcmplsinboundtunnelindex', YLeaf(YType.uint32, 'cpwVcMplsInboundTunnelIndex')),
                    ('cpwvcmplsinboundtunnelinstance', YLeaf(YType.uint32, 'cpwVcMplsInboundTunnelInstance')),
                    ('cpwvcmplsinboundtunnellcllsr', YLeaf(YType.str, 'cpwVcMplsInboundTunnelLclLSR')),
                    ('cpwvcmplsinboundtunnelpeerlsr', YLeaf(YType.str, 'cpwVcMplsInboundTunnelPeerLSR')),
                    ('cpwvcmplsinboundifindex', YLeaf(YType.int32, 'cpwVcMplsInboundIfIndex')),
                    ('cpwvcmplsinboundrowstatus', YLeaf(YType.enumeration, 'cpwVcMplsInboundRowStatus')),
                    ('cpwvcmplsinboundstoragetype', YLeaf(YType.enumeration, 'cpwVcMplsInboundStorageType')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry, ['cpwvcindex', 'cpwvcmplsinboundindex', 'cpwvcmplsinboundlsrxcindex', 'cpwvcmplsinboundtunnelindex', 'cpwvcmplsinboundtunnelinstance', 'cpwvcmplsinboundtunnellcllsr', 'cpwvcmplsinboundtunnelpeerlsr', 'cpwvcmplsinboundifindex', 'cpwvcmplsinboundrowstatus', 'cpwvcmplsinboundstoragetype'], name, value)


    class Cpwvcmplsnontemappingtable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in non\- 
        TE applications.
        
        .. attribute:: cpwvcmplsnontemappingentry
        
        	A row in this table represents the association  between the PW VC and it's non TE MPLS outer Tunnel  it's physical interface if there is no outer tunnel   (VC only).   An application can use this table to quickly retrieve the   PW carried over specific non\-TE MPLS outer tunnel or   physical interface.   The table in indexed by the XC index for MPLS Non\-TE   tunnel, or ifIndex of the port in VC only case, the   direction of the VC in the specific entry and the VCIndex.   The same table is used in both inbound and outbound  directions, but in a different row for each direction. If   the inbound association is not known, no rows should exist   for it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of  		 :py:class:`Cpwvcmplsnontemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable, self).__init__()

            self.yang_name = "cpwVcMplsNonTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcMplsNonTeMappingEntry", ("cpwvcmplsnontemappingentry", CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry))])
            self._leafs = OrderedDict()

            self.cpwvcmplsnontemappingentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsNonTeMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable, [], name, value)


        class Cpwvcmplsnontemappingentry(Entity):
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
            	**type**\:  :py:class:`Cpwvcmplsnontemappingtunneldirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.Cpwvcmplsnontemappingtunneldirection>`
            
            .. attribute:: cpwvcmplsnontemappingxctunnelindex  (key)
            
            	Index for the conceptual XC row identifying Tunnel to VC   mappings when the outer tunnel is created by the MPLS\-LSR\-  MIB, Zero otherwise
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsnontemappingifindex  (key)
            
            	Identify the port on which the VC is carried for VC only   case
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsnontemappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry, self).__init__()

                self.yang_name = "cpwVcMplsNonTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsNonTeMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcmplsnontemappingtunneldirection','cpwvcmplsnontemappingxctunnelindex','cpwvcmplsnontemappingifindex','cpwvcmplsnontemappingvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcmplsnontemappingtunneldirection', YLeaf(YType.enumeration, 'cpwVcMplsNonTeMappingTunnelDirection')),
                    ('cpwvcmplsnontemappingxctunnelindex', YLeaf(YType.uint32, 'cpwVcMplsNonTeMappingXcTunnelIndex')),
                    ('cpwvcmplsnontemappingifindex', YLeaf(YType.int32, 'cpwVcMplsNonTeMappingIfIndex')),
                    ('cpwvcmplsnontemappingvcindex', YLeaf(YType.uint32, 'cpwVcMplsNonTeMappingVcIndex')),
                ])
                self.cpwvcmplsnontemappingtunneldirection = None
                self.cpwvcmplsnontemappingxctunnelindex = None
                self.cpwvcmplsnontemappingifindex = None
                self.cpwvcmplsnontemappingvcindex = None
                self._segment_path = lambda: "cpwVcMplsNonTeMappingEntry" + "[cpwVcMplsNonTeMappingTunnelDirection='" + str(self.cpwvcmplsnontemappingtunneldirection) + "']" + "[cpwVcMplsNonTeMappingXcTunnelIndex='" + str(self.cpwvcmplsnontemappingxctunnelindex) + "']" + "[cpwVcMplsNonTeMappingIfIndex='" + str(self.cpwvcmplsnontemappingifindex) + "']" + "[cpwVcMplsNonTeMappingVcIndex='" + str(self.cpwvcmplsnontemappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsNonTeMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry, ['cpwvcmplsnontemappingtunneldirection', 'cpwvcmplsnontemappingxctunnelindex', 'cpwvcmplsnontemappingifindex', 'cpwvcmplsnontemappingvcindex'], name, value)

            class Cpwvcmplsnontemappingtunneldirection(Enum):
                """
                Cpwvcmplsnontemappingtunneldirection (Enum Class)

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = Enum.YLeaf(1, "outbound")

                inbound = Enum.YLeaf(2, "inbound")



    class Cpwvcmplstemappingtable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in  
        MPLS\-TE applications.
        
        .. attribute:: cpwvcmplstemappingentry
        
        	A row in this table represents the association  between a PW VC and it's MPLS\-TE outer Tunnel.   An application can use this table to quickly retrieve the   PW carried over specific TE MPLS outer tunnel.   The table in indexed by the 4 indexes of a TE tunnel,  the direction of the VC specific entry and the VcIndex.   The same table is used in both inbound and outbound  directions, a different row for each direction. If the   inbound association is not known, no rows should exist for   it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of  		 :py:class:`Cpwvcmplstemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable, self).__init__()

            self.yang_name = "cpwVcMplsTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcMplsTeMappingEntry", ("cpwvcmplstemappingentry", CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry))])
            self._leafs = OrderedDict()

            self.cpwvcmplstemappingentry = YList(self)
            self._segment_path = lambda: "cpwVcMplsTeMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable, [], name, value)


        class Cpwvcmplstemappingentry(Entity):
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
            	**type**\:  :py:class:`Cpwvcmplstemappingtunneldirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.Cpwvcmplstemappingtunneldirection>`
            
            .. attribute:: cpwvcmplstemappingtunnelindex  (key)
            
            	Primary index for the conceptual row identifying the   MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplstemappingtunnelinstance  (key)
            
            	Identifies an instance of the MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplstemappingtunnelpeerlsrid  (key)
            
            	Identifies an Peer LSR when the outer tunnel is MPLS\-TE   based
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingtunnellocallsrid  (key)
            
            	Identifies the local LSR
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingvcindex  (key)
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry, self).__init__()

                self.yang_name = "cpwVcMplsTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsTeMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcmplstemappingtunneldirection','cpwvcmplstemappingtunnelindex','cpwvcmplstemappingtunnelinstance','cpwvcmplstemappingtunnelpeerlsrid','cpwvcmplstemappingtunnellocallsrid','cpwvcmplstemappingvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcmplstemappingtunneldirection', YLeaf(YType.enumeration, 'cpwVcMplsTeMappingTunnelDirection')),
                    ('cpwvcmplstemappingtunnelindex', YLeaf(YType.uint32, 'cpwVcMplsTeMappingTunnelIndex')),
                    ('cpwvcmplstemappingtunnelinstance', YLeaf(YType.uint32, 'cpwVcMplsTeMappingTunnelInstance')),
                    ('cpwvcmplstemappingtunnelpeerlsrid', YLeaf(YType.str, 'cpwVcMplsTeMappingTunnelPeerLsrID')),
                    ('cpwvcmplstemappingtunnellocallsrid', YLeaf(YType.str, 'cpwVcMplsTeMappingTunnelLocalLsrID')),
                    ('cpwvcmplstemappingvcindex', YLeaf(YType.uint32, 'cpwVcMplsTeMappingVcIndex')),
                ])
                self.cpwvcmplstemappingtunneldirection = None
                self.cpwvcmplstemappingtunnelindex = None
                self.cpwvcmplstemappingtunnelinstance = None
                self.cpwvcmplstemappingtunnelpeerlsrid = None
                self.cpwvcmplstemappingtunnellocallsrid = None
                self.cpwvcmplstemappingvcindex = None
                self._segment_path = lambda: "cpwVcMplsTeMappingEntry" + "[cpwVcMplsTeMappingTunnelDirection='" + str(self.cpwvcmplstemappingtunneldirection) + "']" + "[cpwVcMplsTeMappingTunnelIndex='" + str(self.cpwvcmplstemappingtunnelindex) + "']" + "[cpwVcMplsTeMappingTunnelInstance='" + str(self.cpwvcmplstemappingtunnelinstance) + "']" + "[cpwVcMplsTeMappingTunnelPeerLsrID='" + str(self.cpwvcmplstemappingtunnelpeerlsrid) + "']" + "[cpwVcMplsTeMappingTunnelLocalLsrID='" + str(self.cpwvcmplstemappingtunnellocallsrid) + "']" + "[cpwVcMplsTeMappingVcIndex='" + str(self.cpwvcmplstemappingvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsTeMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWMPLSMIB.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry, ['cpwvcmplstemappingtunneldirection', 'cpwvcmplstemappingtunnelindex', 'cpwvcmplstemappingtunnelinstance', 'cpwvcmplstemappingtunnelpeerlsrid', 'cpwvcmplstemappingtunnellocallsrid', 'cpwvcmplstemappingvcindex'], name, value)

            class Cpwvcmplstemappingtunneldirection(Enum):
                """
                Cpwvcmplstemappingtunneldirection (Enum Class)

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

