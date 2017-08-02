""" CISCO_IETF_PW_MPLS_MIB 

This MIB complements the CISCO\-IETF\-PW\-MIB for PW operation 
over MPLS. 

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfPwMplsMib(Entity):
    """
    
    
    .. attribute:: cpwvcmplsinboundtable
    
    	This table associates VCs using MPLS PSN with the inbound  MPLS tunnels (i.e. for packets coming from the PSN),   if such association is desired (mainly for security   reasons)
    	**type**\:   :py:class:`Cpwvcmplsinboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsinboundtable>`
    
    .. attribute:: cpwvcmplsnontemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in non\-  TE applications
    	**type**\:   :py:class:`Cpwvcmplsnontemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable>`
    
    .. attribute:: cpwvcmplsobjects
    
    	
    	**type**\:   :py:class:`Cpwvcmplsobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsobjects>`
    
    .. attribute:: cpwvcmplsoutboundtable
    
    	This table associates VCs using MPLS PSN with the outbound  MPLS tunnels (i.e. toward the PSN) or the physical   interface in case of VC only
    	**type**\:   :py:class:`Cpwvcmplsoutboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable>`
    
    .. attribute:: cpwvcmplstable
    
    	This table specifies information for VC to be carried over   MPLS PSN
    	**type**\:   :py:class:`Cpwvcmplstable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable>`
    
    .. attribute:: cpwvcmplstemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in   MPLS\-TE applications
    	**type**\:   :py:class:`Cpwvcmplstemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-MPLS-MIB'
    _revision = '2003-02-26'

    def __init__(self):
        super(CiscoIetfPwMplsMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-MPLS-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

        self.cpwvcmplsinboundtable = CiscoIetfPwMplsMib.Cpwvcmplsinboundtable()
        self.cpwvcmplsinboundtable.parent = self
        self._children_name_map["cpwvcmplsinboundtable"] = "cpwVcMplsInboundTable"
        self._children_yang_names.add("cpwVcMplsInboundTable")

        self.cpwvcmplsnontemappingtable = CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable()
        self.cpwvcmplsnontemappingtable.parent = self
        self._children_name_map["cpwvcmplsnontemappingtable"] = "cpwVcMplsNonTeMappingTable"
        self._children_yang_names.add("cpwVcMplsNonTeMappingTable")

        self.cpwvcmplsobjects = CiscoIetfPwMplsMib.Cpwvcmplsobjects()
        self.cpwvcmplsobjects.parent = self
        self._children_name_map["cpwvcmplsobjects"] = "cpwVcMplsObjects"
        self._children_yang_names.add("cpwVcMplsObjects")

        self.cpwvcmplsoutboundtable = CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable()
        self.cpwvcmplsoutboundtable.parent = self
        self._children_name_map["cpwvcmplsoutboundtable"] = "cpwVcMplsOutboundTable"
        self._children_yang_names.add("cpwVcMplsOutboundTable")

        self.cpwvcmplstable = CiscoIetfPwMplsMib.Cpwvcmplstable()
        self.cpwvcmplstable.parent = self
        self._children_name_map["cpwvcmplstable"] = "cpwVcMplsTable"
        self._children_yang_names.add("cpwVcMplsTable")

        self.cpwvcmplstemappingtable = CiscoIetfPwMplsMib.Cpwvcmplstemappingtable()
        self.cpwvcmplstemappingtable.parent = self
        self._children_name_map["cpwvcmplstemappingtable"] = "cpwVcMplsTeMappingTable"
        self._children_yang_names.add("cpwVcMplsTeMappingTable")


    class Cpwvcmplsobjects(Entity):
        """
        
        
        .. attribute:: cpwvcmplsinboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsInboundIndex when creating  entries in the cpwVcMplsInboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsInboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcmplsoutboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsOutboundIndex when creating  entries in the cpwVcMplsOutboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsOutboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplsobjects, self).__init__()

            self.yang_name = "cpwVcMplsObjects"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplsinboundindexnext = YLeaf(YType.uint32, "cpwVcMplsInboundIndexNext")

            self.cpwvcmplsoutboundindexnext = YLeaf(YType.uint32, "cpwVcMplsOutboundIndexNext")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpwvcmplsinboundindexnext",
                            "cpwvcmplsoutboundindexnext") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfPwMplsMib.Cpwvcmplsobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplsobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cpwvcmplsinboundindexnext.is_set or
                self.cpwvcmplsoutboundindexnext.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpwvcmplsinboundindexnext.yfilter != YFilter.not_set or
                self.cpwvcmplsoutboundindexnext.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpwvcmplsinboundindexnext.is_set or self.cpwvcmplsinboundindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcmplsinboundindexnext.get_name_leafdata())
            if (self.cpwvcmplsoutboundindexnext.is_set or self.cpwvcmplsoutboundindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwvcmplsoutboundindexnext.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsInboundIndexNext" or name == "cpwVcMplsOutboundIndexNext"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpwVcMplsInboundIndexNext"):
                self.cpwvcmplsinboundindexnext = value
                self.cpwvcmplsinboundindexnext.value_namespace = name_space
                self.cpwvcmplsinboundindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "cpwVcMplsOutboundIndexNext"):
                self.cpwvcmplsoutboundindexnext = value
                self.cpwvcmplsoutboundindexnext.value_namespace = name_space
                self.cpwvcmplsoutboundindexnext.value_namespace_prefix = name_space_prefix


    class Cpwvcmplstable(Entity):
        """
        This table specifies information for VC to be carried over  
        MPLS PSN.
        
        .. attribute:: cpwvcmplsentry
        
        	A row in this table represents parameters specific to MPLS   PSN for a pseudo wire connection (VC). The row is created   automatically by the local agent if the cpwVcPsnType is   MPLS. It is indexed by cpwVcIndex, which uniquely   identifying a singular connection. 
        	**type**\: list of    :py:class:`Cpwvcmplsentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplstable, self).__init__()

            self.yang_name = "cpwVcMplsTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplsentry = YList(self)

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
                        super(CiscoIetfPwMplsMib.Cpwvcmplstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplstable, self).__setattr__(name, value)


        class Cpwvcmplsentry(Entity):
            """
            A row in this table represents parameters specific to MPLS  
            PSN for a pseudo wire connection (VC). The row is created  
            automatically by the local agent if the cpwVcPsnType is  
            MPLS. It is indexed by cpwVcIndex, which uniquely  
            identifying a singular connection. 
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsexpbits
            
            	Set by the operator to indicate the MPLS EXP bits to be   used on the VC shim label if cpwVcMplsExpBitsMode is    specifiedValue(2), zero otherwise
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcmplsexpbitsmode
            
            	Set by the operator to indicate the way the VC shim label  EXP bits are to be determined. The value of outerTunnel(1)  is used where there is an outer tunnel \- cpwVcMplsMplsType   is mplsTe or mplsNonTe. Note that in this case there is no  need to mark the VC label with the EXP bits since the VC   label is not visible to the intermediate nodes.  If there is no outer tunnel, specifiedValue(2) indicate   that the value is specified by cpwVcMplsExpBits, and   serviceDependant(3) indicate that the EXP bits are setup   based on a rule specified in the emulated service specific   tables, for example when the EXP bits are a function of   802.1p marking for Ethernet emulated service
            	**type**\:   :py:class:`Cpwvcmplsexpbitsmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsexpbitsmode>`
            
            .. attribute:: cpwvcmplslocalldpentityid
            
            	The local LDP Entity index of the LDP entity to be used   for this VC on the local node. Should be set to all zeros   if not used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplslocalldpid
            
            	The local LDP identifier of the LDP entity creating  this VC in the local node. As the VC labels are always  set from the per platform label space, the last two octets   in the LDP ID MUST be always both zeros
            	**type**\:  str
            
            .. attribute:: cpwvcmplsmplstype
            
            	Set by the operator to indicate the outer tunnel types, if  exists. mplsTe is used if the outer tunnel was set\-up by   MPLS\-TE, and mplsNonTe is used the outer tunnel was set up  by LDP or manually. Combination of mplsTe and mplsNonTe   may exist in case of outer tunnel protection.  vcOnly is used if there is no outer tunnel label. vcOnly   cannot be combined with mplsNonTe or mplsTe
            	**type**\:   :py:class:`Cpwvcmplsmplstype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsmplstype>`
            
            .. attribute:: cpwvcmplspeerldpid
            
            	The peer LDP identifier as identified from the LDP   session. Should be zero if not relevant or not known yet
            	**type**\:  str
            
            .. attribute:: cpwvcmplsstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwvcmplsttl
            
            	Set by the operator to indicate the VC TTL bits to be used  on the VC shim label
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry, self).__init__()

                self.yang_name = "cpwVcMplsEntry"
                self.yang_parent_name = "cpwVcMplsTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcmplsexpbits = YLeaf(YType.uint32, "cpwVcMplsExpBits")

                self.cpwvcmplsexpbitsmode = YLeaf(YType.enumeration, "cpwVcMplsExpBitsMode")

                self.cpwvcmplslocalldpentityid = YLeaf(YType.uint32, "cpwVcMplsLocalLdpEntityID")

                self.cpwvcmplslocalldpid = YLeaf(YType.str, "cpwVcMplsLocalLdpID")

                self.cpwvcmplsmplstype = YLeaf(YType.bits, "cpwVcMplsMplsType")

                self.cpwvcmplspeerldpid = YLeaf(YType.str, "cpwVcMplsPeerLdpID")

                self.cpwvcmplsstoragetype = YLeaf(YType.enumeration, "cpwVcMplsStorageType")

                self.cpwvcmplsttl = YLeaf(YType.uint32, "cpwVcMplsTtl")

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
                                "cpwvcmplsexpbits",
                                "cpwvcmplsexpbitsmode",
                                "cpwvcmplslocalldpentityid",
                                "cpwvcmplslocalldpid",
                                "cpwvcmplsmplstype",
                                "cpwvcmplspeerldpid",
                                "cpwvcmplsstoragetype",
                                "cpwvcmplsttl") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry, self).__setattr__(name, value)

            class Cpwvcmplsexpbitsmode(Enum):
                """
                Cpwvcmplsexpbitsmode

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


            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcmplsexpbits.is_set or
                    self.cpwvcmplsexpbitsmode.is_set or
                    self.cpwvcmplslocalldpentityid.is_set or
                    self.cpwvcmplslocalldpid.is_set or
                    self.cpwvcmplsmplstype.is_set or
                    self.cpwvcmplspeerldpid.is_set or
                    self.cpwvcmplsstoragetype.is_set or
                    self.cpwvcmplsttl.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsexpbits.yfilter != YFilter.not_set or
                    self.cpwvcmplsexpbitsmode.yfilter != YFilter.not_set or
                    self.cpwvcmplslocalldpentityid.yfilter != YFilter.not_set or
                    self.cpwvcmplslocalldpid.yfilter != YFilter.not_set or
                    self.cpwvcmplsmplstype.yfilter != YFilter.not_set or
                    self.cpwvcmplspeerldpid.yfilter != YFilter.not_set or
                    self.cpwvcmplsstoragetype.yfilter != YFilter.not_set or
                    self.cpwvcmplsttl.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcMplsEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcmplsexpbits.is_set or self.cpwvcmplsexpbits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsexpbits.get_name_leafdata())
                if (self.cpwvcmplsexpbitsmode.is_set or self.cpwvcmplsexpbitsmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsexpbitsmode.get_name_leafdata())
                if (self.cpwvcmplslocalldpentityid.is_set or self.cpwvcmplslocalldpentityid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplslocalldpentityid.get_name_leafdata())
                if (self.cpwvcmplslocalldpid.is_set or self.cpwvcmplslocalldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplslocalldpid.get_name_leafdata())
                if (self.cpwvcmplsmplstype.is_set or self.cpwvcmplsmplstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsmplstype.get_name_leafdata())
                if (self.cpwvcmplspeerldpid.is_set or self.cpwvcmplspeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplspeerldpid.get_name_leafdata())
                if (self.cpwvcmplsstoragetype.is_set or self.cpwvcmplsstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsstoragetype.get_name_leafdata())
                if (self.cpwvcmplsttl.is_set or self.cpwvcmplsttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsttl.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcMplsExpBits" or name == "cpwVcMplsExpBitsMode" or name == "cpwVcMplsLocalLdpEntityID" or name == "cpwVcMplsLocalLdpID" or name == "cpwVcMplsMplsType" or name == "cpwVcMplsPeerLdpID" or name == "cpwVcMplsStorageType" or name == "cpwVcMplsTtl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsExpBits"):
                    self.cpwvcmplsexpbits = value
                    self.cpwvcmplsexpbits.value_namespace = name_space
                    self.cpwvcmplsexpbits.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsExpBitsMode"):
                    self.cpwvcmplsexpbitsmode = value
                    self.cpwvcmplsexpbitsmode.value_namespace = name_space
                    self.cpwvcmplsexpbitsmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsLocalLdpEntityID"):
                    self.cpwvcmplslocalldpentityid = value
                    self.cpwvcmplslocalldpentityid.value_namespace = name_space
                    self.cpwvcmplslocalldpentityid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsLocalLdpID"):
                    self.cpwvcmplslocalldpid = value
                    self.cpwvcmplslocalldpid.value_namespace = name_space
                    self.cpwvcmplslocalldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsMplsType"):
                    self.cpwvcmplsmplstype[value] = True
                if(value_path == "cpwVcMplsPeerLdpID"):
                    self.cpwvcmplspeerldpid = value
                    self.cpwvcmplspeerldpid.value_namespace = name_space
                    self.cpwvcmplspeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsStorageType"):
                    self.cpwvcmplsstoragetype = value
                    self.cpwvcmplsstoragetype.value_namespace = name_space
                    self.cpwvcmplsstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTtl"):
                    self.cpwvcmplsttl = value
                    self.cpwvcmplsttl.value_namespace = name_space
                    self.cpwvcmplsttl.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcmplsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcmplsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcMplsEntry"):
                for c in self.cpwvcmplsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcmplsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcmplsoutboundtable(Entity):
        """
        This table associates VCs using MPLS PSN with the outbound 
        MPLS tunnels (i.e. toward the PSN) or the physical  
        interface in case of VC only.
        
        .. attribute:: cpwvcmplsoutboundentry
        
        	A row in this table represents a link between PW VC (that  require MPLS tunnels) and MPLS tunnel toward the PSN.  In the case of VC only, it associate the VC with the   interface that shall carry the VC.  This table is indexed by the pwVcIndex and an additional  index enabling multiple rows for the same VC index.   At least one entry is created in this table by the operator   for each PW VC that requires MPLS PSN. Note that the first  entry for each VC can be indexed by cpwVcMplsOutboundIndex   equal zero without a need for retrieval of   cpwVcMplsOutboundIndexNext.   This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of   a TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.  In case of Non\-TE MPLS (an outer tunnel label assigned by   LDP or manually) the table points to the XC entry in the   LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>.  In case of VC only (no outer tunnel) the ifIndex of the  port to carry the VC is configured.    Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of    :py:class:`Cpwvcmplsoutboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable, self).__init__()

            self.yang_name = "cpwVcMplsOutboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplsoutboundentry = YList(self)

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
                        super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable, self).__setattr__(name, value)


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
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsoutboundindex  <key>
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved   using cpwVcMplsOutboundIndexNext. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundifindex
            
            	In case of VC only (no outer tunnel), this object holds  the ifIndex of the outbound port, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsoutboundlsrxcindex
            
            	This object will be set by the operator. If the outer  label is defined in the MPL\-LSR\-MIB, i.e. set by LDP  or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwvcmplsoutboundstoragetype
            
            	This variable indicates the storage type for this object
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwvcmplsoutboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsoutboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsoutboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry, self).__init__()

                self.yang_name = "cpwVcMplsOutboundEntry"
                self.yang_parent_name = "cpwVcMplsOutboundTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcmplsoutboundindex = YLeaf(YType.uint32, "cpwVcMplsOutboundIndex")

                self.cpwvcmplsoutboundifindex = YLeaf(YType.int32, "cpwVcMplsOutboundIfIndex")

                self.cpwvcmplsoutboundlsrxcindex = YLeaf(YType.uint32, "cpwVcMplsOutboundLsrXcIndex")

                self.cpwvcmplsoutboundrowstatus = YLeaf(YType.enumeration, "cpwVcMplsOutboundRowStatus")

                self.cpwvcmplsoutboundstoragetype = YLeaf(YType.enumeration, "cpwVcMplsOutboundStorageType")

                self.cpwvcmplsoutboundtunnelindex = YLeaf(YType.uint32, "cpwVcMplsOutboundTunnelIndex")

                self.cpwvcmplsoutboundtunnelinstance = YLeaf(YType.uint32, "cpwVcMplsOutboundTunnelInstance")

                self.cpwvcmplsoutboundtunnellcllsr = YLeaf(YType.str, "cpwVcMplsOutboundTunnelLclLSR")

                self.cpwvcmplsoutboundtunnelpeerlsr = YLeaf(YType.str, "cpwVcMplsOutboundTunnelPeerLSR")

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
                                "cpwvcmplsoutboundindex",
                                "cpwvcmplsoutboundifindex",
                                "cpwvcmplsoutboundlsrxcindex",
                                "cpwvcmplsoutboundrowstatus",
                                "cpwvcmplsoutboundstoragetype",
                                "cpwvcmplsoutboundtunnelindex",
                                "cpwvcmplsoutboundtunnelinstance",
                                "cpwvcmplsoutboundtunnellcllsr",
                                "cpwvcmplsoutboundtunnelpeerlsr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcmplsoutboundindex.is_set or
                    self.cpwvcmplsoutboundifindex.is_set or
                    self.cpwvcmplsoutboundlsrxcindex.is_set or
                    self.cpwvcmplsoutboundrowstatus.is_set or
                    self.cpwvcmplsoutboundstoragetype.is_set or
                    self.cpwvcmplsoutboundtunnelindex.is_set or
                    self.cpwvcmplsoutboundtunnelinstance.is_set or
                    self.cpwvcmplsoutboundtunnellcllsr.is_set or
                    self.cpwvcmplsoutboundtunnelpeerlsr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundifindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundlsrxcindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundrowstatus.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundstoragetype.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundtunnelindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundtunnelinstance.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundtunnellcllsr.yfilter != YFilter.not_set or
                    self.cpwvcmplsoutboundtunnelpeerlsr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcMplsOutboundEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwVcMplsOutboundIndex='" + self.cpwvcmplsoutboundindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsOutboundTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcmplsoutboundindex.is_set or self.cpwvcmplsoutboundindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundindex.get_name_leafdata())
                if (self.cpwvcmplsoutboundifindex.is_set or self.cpwvcmplsoutboundifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundifindex.get_name_leafdata())
                if (self.cpwvcmplsoutboundlsrxcindex.is_set or self.cpwvcmplsoutboundlsrxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundlsrxcindex.get_name_leafdata())
                if (self.cpwvcmplsoutboundrowstatus.is_set or self.cpwvcmplsoutboundrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundrowstatus.get_name_leafdata())
                if (self.cpwvcmplsoutboundstoragetype.is_set or self.cpwvcmplsoutboundstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundstoragetype.get_name_leafdata())
                if (self.cpwvcmplsoutboundtunnelindex.is_set or self.cpwvcmplsoutboundtunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundtunnelindex.get_name_leafdata())
                if (self.cpwvcmplsoutboundtunnelinstance.is_set or self.cpwvcmplsoutboundtunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundtunnelinstance.get_name_leafdata())
                if (self.cpwvcmplsoutboundtunnellcllsr.is_set or self.cpwvcmplsoutboundtunnellcllsr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundtunnellcllsr.get_name_leafdata())
                if (self.cpwvcmplsoutboundtunnelpeerlsr.is_set or self.cpwvcmplsoutboundtunnelpeerlsr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsoutboundtunnelpeerlsr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcMplsOutboundIndex" or name == "cpwVcMplsOutboundIfIndex" or name == "cpwVcMplsOutboundLsrXcIndex" or name == "cpwVcMplsOutboundRowStatus" or name == "cpwVcMplsOutboundStorageType" or name == "cpwVcMplsOutboundTunnelIndex" or name == "cpwVcMplsOutboundTunnelInstance" or name == "cpwVcMplsOutboundTunnelLclLSR" or name == "cpwVcMplsOutboundTunnelPeerLSR"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundIndex"):
                    self.cpwvcmplsoutboundindex = value
                    self.cpwvcmplsoutboundindex.value_namespace = name_space
                    self.cpwvcmplsoutboundindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundIfIndex"):
                    self.cpwvcmplsoutboundifindex = value
                    self.cpwvcmplsoutboundifindex.value_namespace = name_space
                    self.cpwvcmplsoutboundifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundLsrXcIndex"):
                    self.cpwvcmplsoutboundlsrxcindex = value
                    self.cpwvcmplsoutboundlsrxcindex.value_namespace = name_space
                    self.cpwvcmplsoutboundlsrxcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundRowStatus"):
                    self.cpwvcmplsoutboundrowstatus = value
                    self.cpwvcmplsoutboundrowstatus.value_namespace = name_space
                    self.cpwvcmplsoutboundrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundStorageType"):
                    self.cpwvcmplsoutboundstoragetype = value
                    self.cpwvcmplsoutboundstoragetype.value_namespace = name_space
                    self.cpwvcmplsoutboundstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundTunnelIndex"):
                    self.cpwvcmplsoutboundtunnelindex = value
                    self.cpwvcmplsoutboundtunnelindex.value_namespace = name_space
                    self.cpwvcmplsoutboundtunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundTunnelInstance"):
                    self.cpwvcmplsoutboundtunnelinstance = value
                    self.cpwvcmplsoutboundtunnelinstance.value_namespace = name_space
                    self.cpwvcmplsoutboundtunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundTunnelLclLSR"):
                    self.cpwvcmplsoutboundtunnellcllsr = value
                    self.cpwvcmplsoutboundtunnellcllsr.value_namespace = name_space
                    self.cpwvcmplsoutboundtunnellcllsr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsOutboundTunnelPeerLSR"):
                    self.cpwvcmplsoutboundtunnelpeerlsr = value
                    self.cpwvcmplsoutboundtunnelpeerlsr.value_namespace = name_space
                    self.cpwvcmplsoutboundtunnelpeerlsr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcmplsoutboundentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcmplsoutboundentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsOutboundTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcMplsOutboundEntry"):
                for c in self.cpwvcmplsoutboundentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcmplsoutboundentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsOutboundEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcmplsinboundtable(Entity):
        """
        This table associates VCs using MPLS PSN with the inbound 
        MPLS tunnels (i.e. for packets coming from the PSN),  
        if such association is desired (mainly for security  
        reasons).
        
        .. attribute:: cpwvcmplsinboundentry
        
        	A row in this table represents a link between PW VCs (that  require MPLS tunnels) and MPLS tunnel for packets arriving  from the PSN.  This table is indexed by the set of indexes used to  identify the VC \- cpwVcIndex and an additional  index enabling multiple rows for the same VC index.   Note that the first entry for each VC can be indexed by   cpwVcMplsOutboundIndex equal zero without a need for   retrieval of cpwVcMplsInboundIndexNext.   An entry is created in this table either automatically by   the local agent or created manually by the operator in   cases that strict mode is required.   Note that the control messages contain VC ID and VC type,   which together with the remote IP address identify the  cpwVcIndex in the local node.  This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of a  TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.   In case of non\-TE MPLS tunnel (an outer tunnel label   assigned by LDP or manually) the table points to the XC   entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\-  ietf\-mpls\-lsr\-mib>.   Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of    :py:class:`Cpwvcmplsinboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable, self).__init__()

            self.yang_name = "cpwVcMplsInboundTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplsinboundentry = YList(self)

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
                        super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable, self).__setattr__(name, value)


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
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsinboundindex  <key>
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved  using cpwVcMplsInboundIndexNext. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundifindex
            
            	In case of VC only (no outer tunnel), this object holds the  ifIndex of the inbound port, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsinboundlsrxcindex
            
            	If the outer label is defined in the MPL\-LSR\-MIB, i.e. set   by LDP or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwvcmplsinboundstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwvcmplsinboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsinboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsinboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry, self).__init__()

                self.yang_name = "cpwVcMplsInboundEntry"
                self.yang_parent_name = "cpwVcMplsInboundTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcmplsinboundindex = YLeaf(YType.uint32, "cpwVcMplsInboundIndex")

                self.cpwvcmplsinboundifindex = YLeaf(YType.int32, "cpwVcMplsInboundIfIndex")

                self.cpwvcmplsinboundlsrxcindex = YLeaf(YType.uint32, "cpwVcMplsInboundLsrXcIndex")

                self.cpwvcmplsinboundrowstatus = YLeaf(YType.enumeration, "cpwVcMplsInboundRowStatus")

                self.cpwvcmplsinboundstoragetype = YLeaf(YType.enumeration, "cpwVcMplsInboundStorageType")

                self.cpwvcmplsinboundtunnelindex = YLeaf(YType.uint32, "cpwVcMplsInboundTunnelIndex")

                self.cpwvcmplsinboundtunnelinstance = YLeaf(YType.uint32, "cpwVcMplsInboundTunnelInstance")

                self.cpwvcmplsinboundtunnellcllsr = YLeaf(YType.str, "cpwVcMplsInboundTunnelLclLSR")

                self.cpwvcmplsinboundtunnelpeerlsr = YLeaf(YType.str, "cpwVcMplsInboundTunnelPeerLSR")

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
                                "cpwvcmplsinboundindex",
                                "cpwvcmplsinboundifindex",
                                "cpwvcmplsinboundlsrxcindex",
                                "cpwvcmplsinboundrowstatus",
                                "cpwvcmplsinboundstoragetype",
                                "cpwvcmplsinboundtunnelindex",
                                "cpwvcmplsinboundtunnelinstance",
                                "cpwvcmplsinboundtunnellcllsr",
                                "cpwvcmplsinboundtunnelpeerlsr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcmplsinboundindex.is_set or
                    self.cpwvcmplsinboundifindex.is_set or
                    self.cpwvcmplsinboundlsrxcindex.is_set or
                    self.cpwvcmplsinboundrowstatus.is_set or
                    self.cpwvcmplsinboundstoragetype.is_set or
                    self.cpwvcmplsinboundtunnelindex.is_set or
                    self.cpwvcmplsinboundtunnelinstance.is_set or
                    self.cpwvcmplsinboundtunnellcllsr.is_set or
                    self.cpwvcmplsinboundtunnelpeerlsr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundifindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundlsrxcindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundrowstatus.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundstoragetype.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundtunnelindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundtunnelinstance.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundtunnellcllsr.yfilter != YFilter.not_set or
                    self.cpwvcmplsinboundtunnelpeerlsr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcMplsInboundEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwVcMplsInboundIndex='" + self.cpwvcmplsinboundindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsInboundTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcmplsinboundindex.is_set or self.cpwvcmplsinboundindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundindex.get_name_leafdata())
                if (self.cpwvcmplsinboundifindex.is_set or self.cpwvcmplsinboundifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundifindex.get_name_leafdata())
                if (self.cpwvcmplsinboundlsrxcindex.is_set or self.cpwvcmplsinboundlsrxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundlsrxcindex.get_name_leafdata())
                if (self.cpwvcmplsinboundrowstatus.is_set or self.cpwvcmplsinboundrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundrowstatus.get_name_leafdata())
                if (self.cpwvcmplsinboundstoragetype.is_set or self.cpwvcmplsinboundstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundstoragetype.get_name_leafdata())
                if (self.cpwvcmplsinboundtunnelindex.is_set or self.cpwvcmplsinboundtunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundtunnelindex.get_name_leafdata())
                if (self.cpwvcmplsinboundtunnelinstance.is_set or self.cpwvcmplsinboundtunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundtunnelinstance.get_name_leafdata())
                if (self.cpwvcmplsinboundtunnellcllsr.is_set or self.cpwvcmplsinboundtunnellcllsr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundtunnellcllsr.get_name_leafdata())
                if (self.cpwvcmplsinboundtunnelpeerlsr.is_set or self.cpwvcmplsinboundtunnelpeerlsr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsinboundtunnelpeerlsr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcMplsInboundIndex" or name == "cpwVcMplsInboundIfIndex" or name == "cpwVcMplsInboundLsrXcIndex" or name == "cpwVcMplsInboundRowStatus" or name == "cpwVcMplsInboundStorageType" or name == "cpwVcMplsInboundTunnelIndex" or name == "cpwVcMplsInboundTunnelInstance" or name == "cpwVcMplsInboundTunnelLclLSR" or name == "cpwVcMplsInboundTunnelPeerLSR"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundIndex"):
                    self.cpwvcmplsinboundindex = value
                    self.cpwvcmplsinboundindex.value_namespace = name_space
                    self.cpwvcmplsinboundindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundIfIndex"):
                    self.cpwvcmplsinboundifindex = value
                    self.cpwvcmplsinboundifindex.value_namespace = name_space
                    self.cpwvcmplsinboundifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundLsrXcIndex"):
                    self.cpwvcmplsinboundlsrxcindex = value
                    self.cpwvcmplsinboundlsrxcindex.value_namespace = name_space
                    self.cpwvcmplsinboundlsrxcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundRowStatus"):
                    self.cpwvcmplsinboundrowstatus = value
                    self.cpwvcmplsinboundrowstatus.value_namespace = name_space
                    self.cpwvcmplsinboundrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundStorageType"):
                    self.cpwvcmplsinboundstoragetype = value
                    self.cpwvcmplsinboundstoragetype.value_namespace = name_space
                    self.cpwvcmplsinboundstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundTunnelIndex"):
                    self.cpwvcmplsinboundtunnelindex = value
                    self.cpwvcmplsinboundtunnelindex.value_namespace = name_space
                    self.cpwvcmplsinboundtunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundTunnelInstance"):
                    self.cpwvcmplsinboundtunnelinstance = value
                    self.cpwvcmplsinboundtunnelinstance.value_namespace = name_space
                    self.cpwvcmplsinboundtunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundTunnelLclLSR"):
                    self.cpwvcmplsinboundtunnellcllsr = value
                    self.cpwvcmplsinboundtunnellcllsr.value_namespace = name_space
                    self.cpwvcmplsinboundtunnellcllsr.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsInboundTunnelPeerLSR"):
                    self.cpwvcmplsinboundtunnelpeerlsr = value
                    self.cpwvcmplsinboundtunnelpeerlsr.value_namespace = name_space
                    self.cpwvcmplsinboundtunnelpeerlsr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcmplsinboundentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcmplsinboundentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsInboundTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcMplsInboundEntry"):
                for c in self.cpwvcmplsinboundentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcmplsinboundentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsInboundEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcmplsnontemappingtable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in non\- 
        TE applications.
        
        .. attribute:: cpwvcmplsnontemappingentry
        
        	A row in this table represents the association  between the PW VC and it's non TE MPLS outer Tunnel  it's physical interface if there is no outer tunnel   (VC only).   An application can use this table to quickly retrieve the   PW carried over specific non\-TE MPLS outer tunnel or   physical interface.   The table in indexed by the XC index for MPLS Non\-TE   tunnel, or ifIndex of the port in VC only case, the   direction of the VC in the specific entry and the VCIndex.   The same table is used in both inbound and outbound  directions, but in a different row for each direction. If   the inbound association is not known, no rows should exist   for it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of    :py:class:`Cpwvcmplsnontemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable, self).__init__()

            self.yang_name = "cpwVcMplsNonTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplsnontemappingentry = YList(self)

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
                        super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable, self).__setattr__(name, value)


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
            
            .. attribute:: cpwvcmplsnontemappingtunneldirection  <key>
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:   :py:class:`Cpwvcmplsnontemappingtunneldirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.Cpwvcmplsnontemappingtunneldirection>`
            
            .. attribute:: cpwvcmplsnontemappingxctunnelindex  <key>
            
            	Index for the conceptual XC row identifying Tunnel to VC   mappings when the outer tunnel is created by the MPLS\-LSR\-  MIB, Zero otherwise
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsnontemappingifindex  <key>
            
            	Identify the port on which the VC is carried for VC only   case
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsnontemappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry, self).__init__()

                self.yang_name = "cpwVcMplsNonTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsNonTeMappingTable"

                self.cpwvcmplsnontemappingtunneldirection = YLeaf(YType.enumeration, "cpwVcMplsNonTeMappingTunnelDirection")

                self.cpwvcmplsnontemappingxctunnelindex = YLeaf(YType.uint32, "cpwVcMplsNonTeMappingXcTunnelIndex")

                self.cpwvcmplsnontemappingifindex = YLeaf(YType.int32, "cpwVcMplsNonTeMappingIfIndex")

                self.cpwvcmplsnontemappingvcindex = YLeaf(YType.uint32, "cpwVcMplsNonTeMappingVcIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcmplsnontemappingtunneldirection",
                                "cpwvcmplsnontemappingxctunnelindex",
                                "cpwvcmplsnontemappingifindex",
                                "cpwvcmplsnontemappingvcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry, self).__setattr__(name, value)

            class Cpwvcmplsnontemappingtunneldirection(Enum):
                """
                Cpwvcmplsnontemappingtunneldirection

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = Enum.YLeaf(1, "outbound")

                inbound = Enum.YLeaf(2, "inbound")


            def has_data(self):
                return (
                    self.cpwvcmplsnontemappingtunneldirection.is_set or
                    self.cpwvcmplsnontemappingxctunnelindex.is_set or
                    self.cpwvcmplsnontemappingifindex.is_set or
                    self.cpwvcmplsnontemappingvcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcmplsnontemappingtunneldirection.yfilter != YFilter.not_set or
                    self.cpwvcmplsnontemappingxctunnelindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsnontemappingifindex.yfilter != YFilter.not_set or
                    self.cpwvcmplsnontemappingvcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcMplsNonTeMappingEntry" + "[cpwVcMplsNonTeMappingTunnelDirection='" + self.cpwvcmplsnontemappingtunneldirection.get() + "']" + "[cpwVcMplsNonTeMappingXcTunnelIndex='" + self.cpwvcmplsnontemappingxctunnelindex.get() + "']" + "[cpwVcMplsNonTeMappingIfIndex='" + self.cpwvcmplsnontemappingifindex.get() + "']" + "[cpwVcMplsNonTeMappingVcIndex='" + self.cpwvcmplsnontemappingvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsNonTeMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcmplsnontemappingtunneldirection.is_set or self.cpwvcmplsnontemappingtunneldirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsnontemappingtunneldirection.get_name_leafdata())
                if (self.cpwvcmplsnontemappingxctunnelindex.is_set or self.cpwvcmplsnontemappingxctunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsnontemappingxctunnelindex.get_name_leafdata())
                if (self.cpwvcmplsnontemappingifindex.is_set or self.cpwvcmplsnontemappingifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsnontemappingifindex.get_name_leafdata())
                if (self.cpwvcmplsnontemappingvcindex.is_set or self.cpwvcmplsnontemappingvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplsnontemappingvcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcMplsNonTeMappingTunnelDirection" or name == "cpwVcMplsNonTeMappingXcTunnelIndex" or name == "cpwVcMplsNonTeMappingIfIndex" or name == "cpwVcMplsNonTeMappingVcIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcMplsNonTeMappingTunnelDirection"):
                    self.cpwvcmplsnontemappingtunneldirection = value
                    self.cpwvcmplsnontemappingtunneldirection.value_namespace = name_space
                    self.cpwvcmplsnontemappingtunneldirection.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsNonTeMappingXcTunnelIndex"):
                    self.cpwvcmplsnontemappingxctunnelindex = value
                    self.cpwvcmplsnontemappingxctunnelindex.value_namespace = name_space
                    self.cpwvcmplsnontemappingxctunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsNonTeMappingIfIndex"):
                    self.cpwvcmplsnontemappingifindex = value
                    self.cpwvcmplsnontemappingifindex.value_namespace = name_space
                    self.cpwvcmplsnontemappingifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsNonTeMappingVcIndex"):
                    self.cpwvcmplsnontemappingvcindex = value
                    self.cpwvcmplsnontemappingvcindex.value_namespace = name_space
                    self.cpwvcmplsnontemappingvcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcmplsnontemappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcmplsnontemappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsNonTeMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcMplsNonTeMappingEntry"):
                for c in self.cpwvcmplsnontemappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcmplsnontemappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsNonTeMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcmplstemappingtable(Entity):
        """
        This table maps an inbound/outbound Tunnel to a VC in  
        MPLS\-TE applications.
        
        .. attribute:: cpwvcmplstemappingentry
        
        	A row in this table represents the association  between a PW VC and it's MPLS\-TE outer Tunnel.   An application can use this table to quickly retrieve the   PW carried over specific TE MPLS outer tunnel.   The table in indexed by the 4 indexes of a TE tunnel,  the direction of the VC specific entry and the VcIndex.   The same table is used in both inbound and outbound  directions, a different row for each direction. If the   inbound association is not known, no rows should exist for   it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of    :py:class:`Cpwvcmplstemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable, self).__init__()

            self.yang_name = "cpwVcMplsTeMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-MPLS-MIB"

            self.cpwvcmplstemappingentry = YList(self)

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
                        super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable, self).__setattr__(name, value)


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
            
            .. attribute:: cpwvcmplstemappingtunneldirection  <key>
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:   :py:class:`Cpwvcmplstemappingtunneldirection <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.Cpwvcmplstemappingtunneldirection>`
            
            .. attribute:: cpwvcmplstemappingtunnelindex  <key>
            
            	Primary index for the conceptual row identifying the   MPLS\-TE tunnel
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplstemappingtunnelinstance  <key>
            
            	Identifies an instance of the MPLS\-TE tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplstemappingtunnelpeerlsrid  <key>
            
            	Identifies an Peer LSR when the outer tunnel is MPLS\-TE   based
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingtunnellocallsrid  <key>
            
            	Identifies the local LSR
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry, self).__init__()

                self.yang_name = "cpwVcMplsTeMappingEntry"
                self.yang_parent_name = "cpwVcMplsTeMappingTable"

                self.cpwvcmplstemappingtunneldirection = YLeaf(YType.enumeration, "cpwVcMplsTeMappingTunnelDirection")

                self.cpwvcmplstemappingtunnelindex = YLeaf(YType.uint32, "cpwVcMplsTeMappingTunnelIndex")

                self.cpwvcmplstemappingtunnelinstance = YLeaf(YType.uint32, "cpwVcMplsTeMappingTunnelInstance")

                self.cpwvcmplstemappingtunnelpeerlsrid = YLeaf(YType.str, "cpwVcMplsTeMappingTunnelPeerLsrID")

                self.cpwvcmplstemappingtunnellocallsrid = YLeaf(YType.str, "cpwVcMplsTeMappingTunnelLocalLsrID")

                self.cpwvcmplstemappingvcindex = YLeaf(YType.uint32, "cpwVcMplsTeMappingVcIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcmplstemappingtunneldirection",
                                "cpwvcmplstemappingtunnelindex",
                                "cpwvcmplstemappingtunnelinstance",
                                "cpwvcmplstemappingtunnelpeerlsrid",
                                "cpwvcmplstemappingtunnellocallsrid",
                                "cpwvcmplstemappingvcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry, self).__setattr__(name, value)

            class Cpwvcmplstemappingtunneldirection(Enum):
                """
                Cpwvcmplstemappingtunneldirection

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = Enum.YLeaf(1, "outbound")

                inbound = Enum.YLeaf(2, "inbound")


            def has_data(self):
                return (
                    self.cpwvcmplstemappingtunneldirection.is_set or
                    self.cpwvcmplstemappingtunnelindex.is_set or
                    self.cpwvcmplstemappingtunnelinstance.is_set or
                    self.cpwvcmplstemappingtunnelpeerlsrid.is_set or
                    self.cpwvcmplstemappingtunnellocallsrid.is_set or
                    self.cpwvcmplstemappingvcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingtunneldirection.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingtunnelindex.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingtunnelinstance.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingtunnelpeerlsrid.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingtunnellocallsrid.yfilter != YFilter.not_set or
                    self.cpwvcmplstemappingvcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcMplsTeMappingEntry" + "[cpwVcMplsTeMappingTunnelDirection='" + self.cpwvcmplstemappingtunneldirection.get() + "']" + "[cpwVcMplsTeMappingTunnelIndex='" + self.cpwvcmplstemappingtunnelindex.get() + "']" + "[cpwVcMplsTeMappingTunnelInstance='" + self.cpwvcmplstemappingtunnelinstance.get() + "']" + "[cpwVcMplsTeMappingTunnelPeerLsrID='" + self.cpwvcmplstemappingtunnelpeerlsrid.get() + "']" + "[cpwVcMplsTeMappingTunnelLocalLsrID='" + self.cpwvcmplstemappingtunnellocallsrid.get() + "']" + "[cpwVcMplsTeMappingVcIndex='" + self.cpwvcmplstemappingvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/cpwVcMplsTeMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcmplstemappingtunneldirection.is_set or self.cpwvcmplstemappingtunneldirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingtunneldirection.get_name_leafdata())
                if (self.cpwvcmplstemappingtunnelindex.is_set or self.cpwvcmplstemappingtunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingtunnelindex.get_name_leafdata())
                if (self.cpwvcmplstemappingtunnelinstance.is_set or self.cpwvcmplstemappingtunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingtunnelinstance.get_name_leafdata())
                if (self.cpwvcmplstemappingtunnelpeerlsrid.is_set or self.cpwvcmplstemappingtunnelpeerlsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingtunnelpeerlsrid.get_name_leafdata())
                if (self.cpwvcmplstemappingtunnellocallsrid.is_set or self.cpwvcmplstemappingtunnellocallsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingtunnellocallsrid.get_name_leafdata())
                if (self.cpwvcmplstemappingvcindex.is_set or self.cpwvcmplstemappingvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcmplstemappingvcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcMplsTeMappingTunnelDirection" or name == "cpwVcMplsTeMappingTunnelIndex" or name == "cpwVcMplsTeMappingTunnelInstance" or name == "cpwVcMplsTeMappingTunnelPeerLsrID" or name == "cpwVcMplsTeMappingTunnelLocalLsrID" or name == "cpwVcMplsTeMappingVcIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcMplsTeMappingTunnelDirection"):
                    self.cpwvcmplstemappingtunneldirection = value
                    self.cpwvcmplstemappingtunneldirection.value_namespace = name_space
                    self.cpwvcmplstemappingtunneldirection.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTeMappingTunnelIndex"):
                    self.cpwvcmplstemappingtunnelindex = value
                    self.cpwvcmplstemappingtunnelindex.value_namespace = name_space
                    self.cpwvcmplstemappingtunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTeMappingTunnelInstance"):
                    self.cpwvcmplstemappingtunnelinstance = value
                    self.cpwvcmplstemappingtunnelinstance.value_namespace = name_space
                    self.cpwvcmplstemappingtunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTeMappingTunnelPeerLsrID"):
                    self.cpwvcmplstemappingtunnelpeerlsrid = value
                    self.cpwvcmplstemappingtunnelpeerlsrid.value_namespace = name_space
                    self.cpwvcmplstemappingtunnelpeerlsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTeMappingTunnelLocalLsrID"):
                    self.cpwvcmplstemappingtunnellocallsrid = value
                    self.cpwvcmplstemappingtunnellocallsrid.value_namespace = name_space
                    self.cpwvcmplstemappingtunnellocallsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcMplsTeMappingVcIndex"):
                    self.cpwvcmplstemappingvcindex = value
                    self.cpwvcmplstemappingvcindex.value_namespace = name_space
                    self.cpwvcmplstemappingvcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcmplstemappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcmplstemappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcMplsTeMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcMplsTeMappingEntry"):
                for c in self.cpwvcmplstemappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcmplstemappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcMplsTeMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cpwvcmplsinboundtable is not None and self.cpwvcmplsinboundtable.has_data()) or
            (self.cpwvcmplsnontemappingtable is not None and self.cpwvcmplsnontemappingtable.has_data()) or
            (self.cpwvcmplsobjects is not None and self.cpwvcmplsobjects.has_data()) or
            (self.cpwvcmplsoutboundtable is not None and self.cpwvcmplsoutboundtable.has_data()) or
            (self.cpwvcmplstable is not None and self.cpwvcmplstable.has_data()) or
            (self.cpwvcmplstemappingtable is not None and self.cpwvcmplstemappingtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpwvcmplsinboundtable is not None and self.cpwvcmplsinboundtable.has_operation()) or
            (self.cpwvcmplsnontemappingtable is not None and self.cpwvcmplsnontemappingtable.has_operation()) or
            (self.cpwvcmplsobjects is not None and self.cpwvcmplsobjects.has_operation()) or
            (self.cpwvcmplsoutboundtable is not None and self.cpwvcmplsoutboundtable.has_operation()) or
            (self.cpwvcmplstable is not None and self.cpwvcmplstable.has_operation()) or
            (self.cpwvcmplstemappingtable is not None and self.cpwvcmplstemappingtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB" + path_buffer

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

        if (child_yang_name == "cpwVcMplsInboundTable"):
            if (self.cpwvcmplsinboundtable is None):
                self.cpwvcmplsinboundtable = CiscoIetfPwMplsMib.Cpwvcmplsinboundtable()
                self.cpwvcmplsinboundtable.parent = self
                self._children_name_map["cpwvcmplsinboundtable"] = "cpwVcMplsInboundTable"
            return self.cpwvcmplsinboundtable

        if (child_yang_name == "cpwVcMplsNonTeMappingTable"):
            if (self.cpwvcmplsnontemappingtable is None):
                self.cpwvcmplsnontemappingtable = CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable()
                self.cpwvcmplsnontemappingtable.parent = self
                self._children_name_map["cpwvcmplsnontemappingtable"] = "cpwVcMplsNonTeMappingTable"
            return self.cpwvcmplsnontemappingtable

        if (child_yang_name == "cpwVcMplsObjects"):
            if (self.cpwvcmplsobjects is None):
                self.cpwvcmplsobjects = CiscoIetfPwMplsMib.Cpwvcmplsobjects()
                self.cpwvcmplsobjects.parent = self
                self._children_name_map["cpwvcmplsobjects"] = "cpwVcMplsObjects"
            return self.cpwvcmplsobjects

        if (child_yang_name == "cpwVcMplsOutboundTable"):
            if (self.cpwvcmplsoutboundtable is None):
                self.cpwvcmplsoutboundtable = CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable()
                self.cpwvcmplsoutboundtable.parent = self
                self._children_name_map["cpwvcmplsoutboundtable"] = "cpwVcMplsOutboundTable"
            return self.cpwvcmplsoutboundtable

        if (child_yang_name == "cpwVcMplsTable"):
            if (self.cpwvcmplstable is None):
                self.cpwvcmplstable = CiscoIetfPwMplsMib.Cpwvcmplstable()
                self.cpwvcmplstable.parent = self
                self._children_name_map["cpwvcmplstable"] = "cpwVcMplsTable"
            return self.cpwvcmplstable

        if (child_yang_name == "cpwVcMplsTeMappingTable"):
            if (self.cpwvcmplstemappingtable is None):
                self.cpwvcmplstemappingtable = CiscoIetfPwMplsMib.Cpwvcmplstemappingtable()
                self.cpwvcmplstemappingtable.parent = self
                self._children_name_map["cpwvcmplstemappingtable"] = "cpwVcMplsTeMappingTable"
            return self.cpwvcmplstemappingtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpwVcMplsInboundTable" or name == "cpwVcMplsNonTeMappingTable" or name == "cpwVcMplsObjects" or name == "cpwVcMplsOutboundTable" or name == "cpwVcMplsTable" or name == "cpwVcMplsTeMappingTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfPwMplsMib()
        return self._top_entity

