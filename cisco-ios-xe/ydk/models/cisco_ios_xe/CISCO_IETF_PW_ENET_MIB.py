""" CISCO_IETF_PW_ENET_MIB 

This MIB describes a model for managing Ethernet  
point\-to\-point pseudo wire services over a Packet  
Switched Network (PSN).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfPwEnetMib(Entity):
    """
    
    
    .. attribute:: cpwvcenetmplsprimappingtable
    
    	This table may be used for MPLS PSNs if there is a need   to hold multiple VC, each with different COS, for the same  user service (port + PW VLAN). Such a need may arise if the  MPLS network is capable of L\-LSP or E\-LSP without multiple  COS capabilities.  Each row is indexed by the cpwVcIndex   and indicate the PRI bits on the packet recieved from the   user port (or VPLS virtual port) that are  classified to this VC. Note that the EXP bit value of the VC  is configured in the CISCO\-IETF\-PW\-MPLS\-MIB
    	**type**\:   :py:class:`Cpwvcenetmplsprimappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable>`
    
    .. attribute:: cpwvcenetstatstable
    
    	This table contains statistical counters specific for   Ethernet PW
    	**type**\:   :py:class:`Cpwvcenetstatstable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetstatstable>`
    
    .. attribute:: cpwvcenettable
    
    	This table contains the index to the Ethernet tables   associated with this ETH VC, the VLAN configuration and   VLAN mode
    	**type**\:   :py:class:`Cpwvcenettable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-ENET-MIB'
    _revision = '2002-09-22'

    def __init__(self):
        super(CiscoIetfPwEnetMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-ENET-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"

        self.cpwvcenetmplsprimappingtable = CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable()
        self.cpwvcenetmplsprimappingtable.parent = self
        self._children_name_map["cpwvcenetmplsprimappingtable"] = "cpwVcEnetMplsPriMappingTable"
        self._children_yang_names.add("cpwVcEnetMplsPriMappingTable")

        self.cpwvcenetstatstable = CiscoIetfPwEnetMib.Cpwvcenetstatstable()
        self.cpwvcenetstatstable.parent = self
        self._children_name_map["cpwvcenetstatstable"] = "cpwVcEnetStatsTable"
        self._children_yang_names.add("cpwVcEnetStatsTable")

        self.cpwvcenettable = CiscoIetfPwEnetMib.Cpwvcenettable()
        self.cpwvcenettable.parent = self
        self._children_name_map["cpwvcenettable"] = "cpwVcEnetTable"
        self._children_yang_names.add("cpwVcEnetTable")


    class Cpwvcenettable(Entity):
        """
        This table contains the index to the Ethernet tables  
        associated with this ETH VC, the VLAN configuration and  
        VLAN mode.
        
        .. attribute:: cpwvcenetentry
        
        	This table is indexed by the same index that was created   for the associated entry in the PW VC Table in the  CISCO\-IETF\-PW\-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan  are used as indexes to allow multiple VLANs to exist on  the same PW.   An entry is created in this table by the agent for every   entry in the cpwVc table with a VcType of 'ethernetVLAN',  'ethernet' or 'ethernetVPLS'. Additional rows may be   created by the operator or the agent if multiple entries  are required for the same VC.   This table provides Ethernet port mapping and VLAN   configuration for each Ethernet VC
        	**type**\: list of    :py:class:`Cpwvcenetentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CiscoIetfPwEnetMib.Cpwvcenettable, self).__init__()

            self.yang_name = "cpwVcEnetTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"

            self.cpwvcenetentry = YList(self)

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
                        super(CiscoIetfPwEnetMib.Cpwvcenettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwEnetMib.Cpwvcenettable, self).__setattr__(name, value)


        class Cpwvcenetentry(Entity):
            """
            This table is indexed by the same index that was created  
            for the associated entry in the PW VC Table in the 
            CISCO\-IETF\-PW\-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan 
            are used as indexes to allow multiple VLANs to exist on 
            the same PW. 
            
            An entry is created in this table by the agent for every  
            entry in the cpwVc table with a VcType of 'ethernetVLAN', 
            'ethernet' or 'ethernetVPLS'. Additional rows may be  
            created by the operator or the agent if multiple entries 
            are required for the same VC. 
            
            This table provides Ethernet port mapping and VLAN  
            configuration for each Ethernet VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetpwvlan  <key>
            
            	This Object defines the VLAN on the VC. The value of 4097  is used if the object is not applicable, for example when  mapping all packets from an Ethernet port to this VC.  The value of 4096 is used to indicate untagged frames (at   least from the PW point of view), for example if   cpwVcEnetVlanMode is equal 'removeVLAN' or when   cpwVcEnetVlanMode equal 'noChange' and cpwVcEnetPortVlan  is equal 4096
            	**type**\:  int
            
            	**range:** 0..4097
            
            .. attribute:: cpwvcenetportifindex
            
            	This object is used to specify the ifIndex of the ETHERNET  port associated with this VC for point\-to\-point Ethernet   service, or the ifIndex of the virtual interface of the VPLS   instance associated with the PW if the service is VPLS. Two   rows in this table can point to the same ifIndex only if\:   1) It is required to support multiple COS on a MPLS PSN      for the same service (i.e.\: a combination of ports and      VLANs) by the use of multiple VC, each with a different     COS.   2) There is no overlap of VLAN values specified in      cpwVcEnetPortVlan that are associated with this port.   A value of zero indicate that association to an ifIndex is  not yet known
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcenetportvlan
            
            	This object define the VLAN value on the physical port (or   VPLS virtual port) if a change is required to the VLAN value  between the VC and the physical/virtual port.   The value of this object can be ignored if the whole traffic   from the port is forwarded to one VC independent of the   tagging on the port, but it is RECOMENDED that the value in  this case will be '4097' indicating not relevant.   It MUST be equal to cpwVcEnetPwVlan if 'noChange' mode  is used.   The value 4096 indicate that no VLAN (i.e. untagged   frames) on the port are associated to this VC. This   allows the same behaviors as assigning 'Default VLAN'   to un\-tagged frames. 
            	**type**\:  int
            
            	**range:** 0..4097
            
            .. attribute:: cpwvcenetrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwvcenetstoragetype
            
            	Indicates the storage type of this row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwvcenetvcifindex
            
            	It is sometimes convenient to model the VC PW as a   virtual interface in the ifTable. In these cases this   object hold the value of the ifIndex in the ifTable   representing this VC PW. A value of zero indicate no such   association or association is not yet known
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcenetvlanmode
            
            	Indicate the mode of VLAN handling between the port   associated to the VC and the VC encapsulation itself.   \- 'other' indicate operation that is not defined by    this MIB.   \- 'portBased' indicates that the forwarder will forward    packets between the port and the PW independent of their    structure.   \- 'noChange' indicates that the VC contains the original     user VLAN, as specified in cpwVcEnetPortVlan.   \- 'changeVlan' indicates that the VLAN field on the VC     may be different than the VLAN field on the user's     port.   \- 'removeVlan' indicates that the encapsulation on the     VC does not include the original VLAN field. Note     that PRI bits transparency is lost in this case.   \- 'addVlan' indicate that a VLAN field will be added    on the PSN bound direction. cpwVcEnetPwVlan indicate    the value that will be added.    \- 'removeVlan', 'addVlan' and 'changeVlan' implementation    is not required. 
            	**type**\:   :py:class:`Cpwvcenetvlanmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry.Cpwvcenetvlanmode>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry, self).__init__()

                self.yang_name = "cpwVcEnetEntry"
                self.yang_parent_name = "cpwVcEnetTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcenetpwvlan = YLeaf(YType.int32, "cpwVcEnetPwVlan")

                self.cpwvcenetportifindex = YLeaf(YType.int32, "cpwVcEnetPortIfIndex")

                self.cpwvcenetportvlan = YLeaf(YType.int32, "cpwVcEnetPortVlan")

                self.cpwvcenetrowstatus = YLeaf(YType.enumeration, "cpwVcEnetRowStatus")

                self.cpwvcenetstoragetype = YLeaf(YType.enumeration, "cpwVcEnetStorageType")

                self.cpwvcenetvcifindex = YLeaf(YType.int32, "cpwVcEnetVcIfIndex")

                self.cpwvcenetvlanmode = YLeaf(YType.enumeration, "cpwVcEnetVlanMode")

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
                                "cpwvcenetpwvlan",
                                "cpwvcenetportifindex",
                                "cpwvcenetportvlan",
                                "cpwvcenetrowstatus",
                                "cpwvcenetstoragetype",
                                "cpwvcenetvcifindex",
                                "cpwvcenetvlanmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry, self).__setattr__(name, value)

            class Cpwvcenetvlanmode(Enum):
                """
                Cpwvcenetvlanmode

                Indicate the mode of VLAN handling between the port  

                associated to the VC and the VC encapsulation itself. 

                \- 'other' indicate operation that is not defined by 

                  this MIB. 

                \- 'portBased' indicates that the forwarder will forward 

                  packets between the port and the PW independent of their 

                  structure. 

                \- 'noChange' indicates that the VC contains the original 

                   user VLAN, as specified in cpwVcEnetPortVlan. 

                \- 'changeVlan' indicates that the VLAN field on the VC  

                  may be different than the VLAN field on the user's  

                  port. 

                \- 'removeVlan' indicates that the encapsulation on the  

                  VC does not include the original VLAN field. Note  

                  that PRI bits transparency is lost in this case. 

                \- 'addVlan' indicate that a VLAN field will be added 

                  on the PSN bound direction. cpwVcEnetPwVlan indicate 

                  the value that will be added.  

                \- 'removeVlan', 'addVlan' and 'changeVlan' implementation 

                  is not required. 

                .. data:: other = 0

                .. data:: portBased = 1

                .. data:: noChange = 2

                .. data:: changeVlan = 3

                .. data:: addVlan = 4

                .. data:: removeVlan = 5

                """

                other = Enum.YLeaf(0, "other")

                portBased = Enum.YLeaf(1, "portBased")

                noChange = Enum.YLeaf(2, "noChange")

                changeVlan = Enum.YLeaf(3, "changeVlan")

                addVlan = Enum.YLeaf(4, "addVlan")

                removeVlan = Enum.YLeaf(5, "removeVlan")


            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcenetpwvlan.is_set or
                    self.cpwvcenetportifindex.is_set or
                    self.cpwvcenetportvlan.is_set or
                    self.cpwvcenetrowstatus.is_set or
                    self.cpwvcenetstoragetype.is_set or
                    self.cpwvcenetvcifindex.is_set or
                    self.cpwvcenetvlanmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcenetpwvlan.yfilter != YFilter.not_set or
                    self.cpwvcenetportifindex.yfilter != YFilter.not_set or
                    self.cpwvcenetportvlan.yfilter != YFilter.not_set or
                    self.cpwvcenetrowstatus.yfilter != YFilter.not_set or
                    self.cpwvcenetstoragetype.yfilter != YFilter.not_set or
                    self.cpwvcenetvcifindex.yfilter != YFilter.not_set or
                    self.cpwvcenetvlanmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcEnetEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwVcEnetPwVlan='" + self.cpwvcenetpwvlan.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcenetpwvlan.is_set or self.cpwvcenetpwvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetpwvlan.get_name_leafdata())
                if (self.cpwvcenetportifindex.is_set or self.cpwvcenetportifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetportifindex.get_name_leafdata())
                if (self.cpwvcenetportvlan.is_set or self.cpwvcenetportvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetportvlan.get_name_leafdata())
                if (self.cpwvcenetrowstatus.is_set or self.cpwvcenetrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetrowstatus.get_name_leafdata())
                if (self.cpwvcenetstoragetype.is_set or self.cpwvcenetstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetstoragetype.get_name_leafdata())
                if (self.cpwvcenetvcifindex.is_set or self.cpwvcenetvcifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetvcifindex.get_name_leafdata())
                if (self.cpwvcenetvlanmode.is_set or self.cpwvcenetvlanmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetvlanmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcEnetPwVlan" or name == "cpwVcEnetPortIfIndex" or name == "cpwVcEnetPortVlan" or name == "cpwVcEnetRowStatus" or name == "cpwVcEnetStorageType" or name == "cpwVcEnetVcIfIndex" or name == "cpwVcEnetVlanMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetPwVlan"):
                    self.cpwvcenetpwvlan = value
                    self.cpwvcenetpwvlan.value_namespace = name_space
                    self.cpwvcenetpwvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetPortIfIndex"):
                    self.cpwvcenetportifindex = value
                    self.cpwvcenetportifindex.value_namespace = name_space
                    self.cpwvcenetportifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetPortVlan"):
                    self.cpwvcenetportvlan = value
                    self.cpwvcenetportvlan.value_namespace = name_space
                    self.cpwvcenetportvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetRowStatus"):
                    self.cpwvcenetrowstatus = value
                    self.cpwvcenetrowstatus.value_namespace = name_space
                    self.cpwvcenetrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetStorageType"):
                    self.cpwvcenetstoragetype = value
                    self.cpwvcenetstoragetype.value_namespace = name_space
                    self.cpwvcenetstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetVcIfIndex"):
                    self.cpwvcenetvcifindex = value
                    self.cpwvcenetvcifindex.value_namespace = name_space
                    self.cpwvcenetvcifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetVlanMode"):
                    self.cpwvcenetvlanmode = value
                    self.cpwvcenetvlanmode.value_namespace = name_space
                    self.cpwvcenetvlanmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcenetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcenetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcEnetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcEnetEntry"):
                for c in self.cpwvcenetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcenetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcEnetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcenetmplsprimappingtable(Entity):
        """
        This table may be used for MPLS PSNs if there is a need  
        to hold multiple VC, each with different COS, for the same 
        user service (port + PW VLAN). Such a need may arise if the 
        MPLS network is capable of L\-LSP or E\-LSP without multiple 
        COS capabilities.  Each row is indexed by the cpwVcIndex  
        and indicate the PRI bits on the packet recieved from the  
        user port (or VPLS virtual port) that are 
        classified to this VC. Note that the EXP bit value of the VC 
        is configured in the CISCO\-IETF\-PW\-MPLS\-MIB.
        
        .. attribute:: cpwvcenetmplsprimappingtableentry
        
        	Each entry is created if special classification based on   the PRI bits is required for this VC
        	**type**\: list of    :py:class:`Cpwvcenetmplsprimappingtableentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable, self).__init__()

            self.yang_name = "cpwVcEnetMplsPriMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"

            self.cpwvcenetmplsprimappingtableentry = YList(self)

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
                        super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable, self).__setattr__(name, value)


        class Cpwvcenetmplsprimappingtableentry(Entity):
            """
            Each entry is created if special classification based on  
            the PRI bits is required for this VC.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetmplsprimapping
            
            	This object defines the groups of user PRI mapped into  this VC. Each bit set indicates that this user priority   is assigned to this VC.   The value 'untagged' is used to indicate that untagged   frames are also associated to this VC.   This object allow the use of different PSN COS based on   user marking of PRI bits in MPLS PSN with L\-LSP or   E\-LSP without multiple COS support. In all other cases,   the default value MUST be used.   It is REQUIRED that there is no overlap on this object   between rows serving the same service (port+ PW VLAN).   In case of missing BIT configuration between rows to   the same service, incoming packets with PRI marking not   configured should be handled by the VC with the lowest   COS. 
            	**type**\:   :py:class:`Cpwvcenetmplsprimapping <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry.Cpwvcenetmplsprimapping>`
            
            .. attribute:: cpwvcenetmplsprimappingrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwvcenetmplsprimappingstoragetype
            
            	Indicates the storage type of this row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry, self).__init__()

                self.yang_name = "cpwVcEnetMplsPriMappingTableEntry"
                self.yang_parent_name = "cpwVcEnetMplsPriMappingTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcenetmplsprimapping = YLeaf(YType.bits, "cpwVcEnetMplsPriMapping")

                self.cpwvcenetmplsprimappingrowstatus = YLeaf(YType.enumeration, "cpwVcEnetMplsPriMappingRowStatus")

                self.cpwvcenetmplsprimappingstoragetype = YLeaf(YType.enumeration, "cpwVcEnetMplsPriMappingStorageType")

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
                                "cpwvcenetmplsprimapping",
                                "cpwvcenetmplsprimappingrowstatus",
                                "cpwvcenetmplsprimappingstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcenetmplsprimapping.is_set or
                    self.cpwvcenetmplsprimappingrowstatus.is_set or
                    self.cpwvcenetmplsprimappingstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcenetmplsprimapping.yfilter != YFilter.not_set or
                    self.cpwvcenetmplsprimappingrowstatus.yfilter != YFilter.not_set or
                    self.cpwvcenetmplsprimappingstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcEnetMplsPriMappingTableEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetMplsPriMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcenetmplsprimapping.is_set or self.cpwvcenetmplsprimapping.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetmplsprimapping.get_name_leafdata())
                if (self.cpwvcenetmplsprimappingrowstatus.is_set or self.cpwvcenetmplsprimappingrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetmplsprimappingrowstatus.get_name_leafdata())
                if (self.cpwvcenetmplsprimappingstoragetype.is_set or self.cpwvcenetmplsprimappingstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetmplsprimappingstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcEnetMplsPriMapping" or name == "cpwVcEnetMplsPriMappingRowStatus" or name == "cpwVcEnetMplsPriMappingStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetMplsPriMapping"):
                    self.cpwvcenetmplsprimapping[value] = True
                if(value_path == "cpwVcEnetMplsPriMappingRowStatus"):
                    self.cpwvcenetmplsprimappingrowstatus = value
                    self.cpwvcenetmplsprimappingrowstatus.value_namespace = name_space
                    self.cpwvcenetmplsprimappingrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetMplsPriMappingStorageType"):
                    self.cpwvcenetmplsprimappingstoragetype = value
                    self.cpwvcenetmplsprimappingstoragetype.value_namespace = name_space
                    self.cpwvcenetmplsprimappingstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcenetmplsprimappingtableentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcenetmplsprimappingtableentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcEnetMplsPriMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcEnetMplsPriMappingTableEntry"):
                for c in self.cpwvcenetmplsprimappingtableentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcenetmplsprimappingtableentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcEnetMplsPriMappingTableEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwvcenetstatstable(Entity):
        """
        This table contains statistical counters specific for  
        Ethernet PW.
        
        .. attribute:: cpwvcenetstatsentry
        
        	Each entry represents the statistics gathered for the   VC carrying the Ethernet packets since this VC was   first created in the cpwVcEnetTable
        	**type**\: list of    :py:class:`Cpwvcenetstatsentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CiscoIetfPwEnetMib.Cpwvcenetstatstable, self).__init__()

            self.yang_name = "cpwVcEnetStatsTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"

            self.cpwvcenetstatsentry = YList(self)

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
                        super(CiscoIetfPwEnetMib.Cpwvcenetstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwEnetMib.Cpwvcenetstatstable, self).__setattr__(name, value)


        class Cpwvcenetstatsentry(Entity):
            """
            Each entry represents the statistics gathered for the  
            VC carrying the Ethernet packets since this VC was  
            first created in the cpwVcEnetTable.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcenetstatsillegallength
            
            	The number of packets that were received with an illegal   Ethernet packet length on this VC. An illegal length is defined  as being greater than the value in the advertised maximum MTU   supported, or shorter than the allowed Ethernet packet size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwvcenetstatsillegalvlan
            
            	The number of packets received (from the PSN) on this VC with   an illegal VLAN field, missing VLAN field that was expected, or   A VLAN field when it was not expected. This counter is not   relevant if the VC type is 'ethernet' (i.e. raw mode), and   should be set to 0 by the agent to indicate this
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry, self).__init__()

                self.yang_name = "cpwVcEnetStatsEntry"
                self.yang_parent_name = "cpwVcEnetStatsTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwvcenetstatsillegallength = YLeaf(YType.uint64, "cpwVcEnetStatsIllegalLength")

                self.cpwvcenetstatsillegalvlan = YLeaf(YType.uint64, "cpwVcEnetStatsIllegalVlan")

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
                                "cpwvcenetstatsillegallength",
                                "cpwvcenetstatsillegalvlan") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwvcenetstatsillegallength.is_set or
                    self.cpwvcenetstatsillegalvlan.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwvcenetstatsillegallength.yfilter != YFilter.not_set or
                    self.cpwvcenetstatsillegalvlan.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcEnetStatsEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwvcenetstatsillegallength.is_set or self.cpwvcenetstatsillegallength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetstatsillegallength.get_name_leafdata())
                if (self.cpwvcenetstatsillegalvlan.is_set or self.cpwvcenetstatsillegalvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcenetstatsillegalvlan.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwVcEnetStatsIllegalLength" or name == "cpwVcEnetStatsIllegalVlan"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetStatsIllegalLength"):
                    self.cpwvcenetstatsillegallength = value
                    self.cpwvcenetstatsillegallength.value_namespace = name_space
                    self.cpwvcenetstatsillegallength.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwVcEnetStatsIllegalVlan"):
                    self.cpwvcenetstatsillegalvlan = value
                    self.cpwvcenetstatsillegalvlan.value_namespace = name_space
                    self.cpwvcenetstatsillegalvlan.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcenetstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcenetstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcEnetStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcEnetStatsEntry"):
                for c in self.cpwvcenetstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcenetstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcEnetStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cpwvcenetmplsprimappingtable is not None and self.cpwvcenetmplsprimappingtable.has_data()) or
            (self.cpwvcenetstatstable is not None and self.cpwvcenetstatstable.has_data()) or
            (self.cpwvcenettable is not None and self.cpwvcenettable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpwvcenetmplsprimappingtable is not None and self.cpwvcenetmplsprimappingtable.has_operation()) or
            (self.cpwvcenetstatstable is not None and self.cpwvcenetstatstable.has_operation()) or
            (self.cpwvcenettable is not None and self.cpwvcenettable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB" + path_buffer

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

        if (child_yang_name == "cpwVcEnetMplsPriMappingTable"):
            if (self.cpwvcenetmplsprimappingtable is None):
                self.cpwvcenetmplsprimappingtable = CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable()
                self.cpwvcenetmplsprimappingtable.parent = self
                self._children_name_map["cpwvcenetmplsprimappingtable"] = "cpwVcEnetMplsPriMappingTable"
            return self.cpwvcenetmplsprimappingtable

        if (child_yang_name == "cpwVcEnetStatsTable"):
            if (self.cpwvcenetstatstable is None):
                self.cpwvcenetstatstable = CiscoIetfPwEnetMib.Cpwvcenetstatstable()
                self.cpwvcenetstatstable.parent = self
                self._children_name_map["cpwvcenetstatstable"] = "cpwVcEnetStatsTable"
            return self.cpwvcenetstatstable

        if (child_yang_name == "cpwVcEnetTable"):
            if (self.cpwvcenettable is None):
                self.cpwvcenettable = CiscoIetfPwEnetMib.Cpwvcenettable()
                self.cpwvcenettable.parent = self
                self._children_name_map["cpwvcenettable"] = "cpwVcEnetTable"
            return self.cpwvcenettable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpwVcEnetMplsPriMappingTable" or name == "cpwVcEnetStatsTable" or name == "cpwVcEnetTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfPwEnetMib()
        return self._top_entity

