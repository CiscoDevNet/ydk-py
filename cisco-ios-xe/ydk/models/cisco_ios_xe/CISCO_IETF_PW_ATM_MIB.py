""" CISCO_IETF_PW_ATM_MIB 

This MIB contains managed object definitions for Pseudo Wire
emulation of ATM over Packet Switched Networks(PSN).

This MIB reports to the PW\-MIB. The PW\-MIB contains
structures and MIB associations generic to Pseudo\-Wire
Virtual Circuit (VC) emulation. VC\-specific MIBs (such as
this) contain config and stats for specific VC types.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfPwAtmMib(Entity):
    """
    
    
    .. attribute:: cpwvcatmtable
    
    	This table specifies the information for an ATM interface, VC, VP to be carried over PSN
    	**type**\:   :py:class:`Cpwvcatmtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-ATM-MIB'
    _revision = '2005-04-19'

    def __init__(self):
        super(CiscoIetfPwAtmMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-ATM-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-ATM-MIB"

        self.cpwvcatmtable = CiscoIetfPwAtmMib.Cpwvcatmtable()
        self.cpwvcatmtable.parent = self
        self._children_name_map["cpwvcatmtable"] = "cpwVcAtmTable"
        self._children_yang_names.add("cpwVcAtmTable")


    class Cpwvcatmtable(Entity):
        """
        This table specifies the information for an ATM interface, VC,
        VP to be carried over PSN.
        
        .. attribute:: cpwvcatmentry
        
        	A row in this table represents an ATM interface, VC, VP that needs to be adapted and carried over PSN. This table is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB
        	**type**\: list of    :py:class:`Cpwvcatmentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ATM-MIB'
        _revision = '2005-04-19'

        def __init__(self):
            super(CiscoIetfPwAtmMib.Cpwvcatmtable, self).__init__()

            self.yang_name = "cpwVcAtmTable"
            self.yang_parent_name = "CISCO-IETF-PW-ATM-MIB"

            self.cpwvcatmentry = YList(self)

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
                        super(CiscoIetfPwAtmMib.Cpwvcatmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwAtmMib.Cpwvcatmtable, self).__setattr__(name, value)


        class Cpwvcatmentry(Entity):
            """
            A row in this table represents an ATM interface, VC, VP
            that needs to be adapted and carried over PSN. This table
            is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwatmavgcellspacked
            
            	It indicates the Average number of cells that were received in one packet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellpacking
            
            	This object is used to identify if the VC is configured to do Cell Packing
            	**type**\:  bool
            
            .. attribute:: cpwatmcellsreceived
            
            	This object can be used to obtain the information on the number of cells that were received and sent to the PSN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellsrejected
            
            	This Object indicates the number of cells that were rejected by this VC because of policing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellssent
            
            	This object can be used to obtain the information on the number of cells that were received from the PSN and sent over the ATM network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellstagged
            
            	This Object indicates the number of cells that were Tagged
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmclpqosmapping
            
            	This Object indicates whether the CLP bits are considered when determining the value placed in the Quality of Service fields (e.g. EXP fields of the MPLS Label Stack) of the encapsulating protocol
            	**type**\:  bool
            
            .. attribute:: cpwatmencap
            
            	This object indicates if the packet going on the pseudowire is mpls or l2tpv3 encapsulated
            	**type**\:   :py:class:`Cpwatmencap <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry.Cpwatmencap>`
            
            .. attribute:: cpwatmhccellsreceived
            
            	High Capacity counter for the number of cells that were received by this VC
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellsrejected
            
            	High Capacity counter for the number of cells that were rejected by this VC because of policing
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellstagged
            
            	High Capacity counter for the number of cells that were tagged
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmif
            
            	The ATM Interface that receives cells from the ATM network
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpwatmmcpttimeout
            
            	This Object represents which MCPT timeout value
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmmncp
            
            	This object indicates the maximum number of cells that get packed in one packet
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmoamcellsupported
            
            	This Object indicates whether OAM Cells are transported on this VC
            	**type**\:  bool
            
            .. attribute:: cpwatmpeermncp
            
            	This Object represents the maximum number of cell that can be packed in one packet for peer interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmpktsreceived
            
            	This object can be used to obtain the information on the number of packets that were received and sent to the PSN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktsrejected
            
            	This object indicates the number of packets that were rejected because of Policing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktssent
            
            	This object indicates the number of packets that were sent to the atm network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmqosscalingfactor
            
            	This Object represents the scaling factor (% value) to be applied to ATM QoS rates when calculating QoS rates for the PSN domain . For example, in the cell transport mode the bandwidth needed in the PSN domain will be higher (since PSN Transport header, PW header, and optional control word have to transmitted with every cell), whereas in the AAL5 mode the bandwidth needed in PSN domain will be less since cell headers will be removed after reassembly
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmrowstatus
            
            	This Object is used to create, modify or delete a row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwatmvci
            
            	VCI value of this ATM VC
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwatmvpi
            
            	VPI value of this ATM VC
            	**type**\:  int
            
            	**range:** 0..4095
            
            

            """

            _prefix = 'CISCO-IETF-PW-ATM-MIB'
            _revision = '2005-04-19'

            def __init__(self):
                super(CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry, self).__init__()

                self.yang_name = "cpwVcAtmEntry"
                self.yang_parent_name = "cpwVcAtmTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwatmavgcellspacked = YLeaf(YType.uint32, "cpwAtmAvgCellsPacked")

                self.cpwatmcellpacking = YLeaf(YType.boolean, "cpwAtmCellPacking")

                self.cpwatmcellsreceived = YLeaf(YType.uint32, "cpwAtmCellsReceived")

                self.cpwatmcellsrejected = YLeaf(YType.uint32, "cpwAtmCellsRejected")

                self.cpwatmcellssent = YLeaf(YType.uint32, "cpwAtmCellsSent")

                self.cpwatmcellstagged = YLeaf(YType.uint32, "cpwAtmCellsTagged")

                self.cpwatmclpqosmapping = YLeaf(YType.boolean, "cpwAtmClpQosMapping")

                self.cpwatmencap = YLeaf(YType.enumeration, "cpwAtmEncap")

                self.cpwatmhccellsreceived = YLeaf(YType.uint64, "cpwAtmHCCellsReceived")

                self.cpwatmhccellsrejected = YLeaf(YType.uint64, "cpwAtmHCCellsRejected")

                self.cpwatmhccellstagged = YLeaf(YType.uint64, "cpwAtmHCCellsTagged")

                self.cpwatmif = YLeaf(YType.int32, "cpwAtmIf")

                self.cpwatmmcpttimeout = YLeaf(YType.int32, "cpwAtmMcptTimeout")

                self.cpwatmmncp = YLeaf(YType.int32, "cpwAtmMncp")

                self.cpwatmoamcellsupported = YLeaf(YType.boolean, "cpwAtmOamCellSupported")

                self.cpwatmpeermncp = YLeaf(YType.int32, "cpwAtmPeerMncp")

                self.cpwatmpktsreceived = YLeaf(YType.uint32, "cpwAtmPktsReceived")

                self.cpwatmpktsrejected = YLeaf(YType.uint32, "cpwAtmPktsRejected")

                self.cpwatmpktssent = YLeaf(YType.uint32, "cpwAtmPktsSent")

                self.cpwatmqosscalingfactor = YLeaf(YType.int32, "cpwAtmQosScalingFactor")

                self.cpwatmrowstatus = YLeaf(YType.enumeration, "cpwAtmRowStatus")

                self.cpwatmvci = YLeaf(YType.int32, "cpwAtmVci")

                self.cpwatmvpi = YLeaf(YType.int32, "cpwAtmVpi")

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
                                "cpwatmavgcellspacked",
                                "cpwatmcellpacking",
                                "cpwatmcellsreceived",
                                "cpwatmcellsrejected",
                                "cpwatmcellssent",
                                "cpwatmcellstagged",
                                "cpwatmclpqosmapping",
                                "cpwatmencap",
                                "cpwatmhccellsreceived",
                                "cpwatmhccellsrejected",
                                "cpwatmhccellstagged",
                                "cpwatmif",
                                "cpwatmmcpttimeout",
                                "cpwatmmncp",
                                "cpwatmoamcellsupported",
                                "cpwatmpeermncp",
                                "cpwatmpktsreceived",
                                "cpwatmpktsrejected",
                                "cpwatmpktssent",
                                "cpwatmqosscalingfactor",
                                "cpwatmrowstatus",
                                "cpwatmvci",
                                "cpwatmvpi") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry, self).__setattr__(name, value)

            class Cpwatmencap(Enum):
                """
                Cpwatmencap

                This object indicates if the packet going on the pseudowire

                is mpls or l2tpv3 encapsulated.

                .. data:: mpls = 1

                .. data:: l2tpv3 = 2

                .. data:: unknown = 3

                """

                mpls = Enum.YLeaf(1, "mpls")

                l2tpv3 = Enum.YLeaf(2, "l2tpv3")

                unknown = Enum.YLeaf(3, "unknown")


            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwatmavgcellspacked.is_set or
                    self.cpwatmcellpacking.is_set or
                    self.cpwatmcellsreceived.is_set or
                    self.cpwatmcellsrejected.is_set or
                    self.cpwatmcellssent.is_set or
                    self.cpwatmcellstagged.is_set or
                    self.cpwatmclpqosmapping.is_set or
                    self.cpwatmencap.is_set or
                    self.cpwatmhccellsreceived.is_set or
                    self.cpwatmhccellsrejected.is_set or
                    self.cpwatmhccellstagged.is_set or
                    self.cpwatmif.is_set or
                    self.cpwatmmcpttimeout.is_set or
                    self.cpwatmmncp.is_set or
                    self.cpwatmoamcellsupported.is_set or
                    self.cpwatmpeermncp.is_set or
                    self.cpwatmpktsreceived.is_set or
                    self.cpwatmpktsrejected.is_set or
                    self.cpwatmpktssent.is_set or
                    self.cpwatmqosscalingfactor.is_set or
                    self.cpwatmrowstatus.is_set or
                    self.cpwatmvci.is_set or
                    self.cpwatmvpi.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwatmavgcellspacked.yfilter != YFilter.not_set or
                    self.cpwatmcellpacking.yfilter != YFilter.not_set or
                    self.cpwatmcellsreceived.yfilter != YFilter.not_set or
                    self.cpwatmcellsrejected.yfilter != YFilter.not_set or
                    self.cpwatmcellssent.yfilter != YFilter.not_set or
                    self.cpwatmcellstagged.yfilter != YFilter.not_set or
                    self.cpwatmclpqosmapping.yfilter != YFilter.not_set or
                    self.cpwatmencap.yfilter != YFilter.not_set or
                    self.cpwatmhccellsreceived.yfilter != YFilter.not_set or
                    self.cpwatmhccellsrejected.yfilter != YFilter.not_set or
                    self.cpwatmhccellstagged.yfilter != YFilter.not_set or
                    self.cpwatmif.yfilter != YFilter.not_set or
                    self.cpwatmmcpttimeout.yfilter != YFilter.not_set or
                    self.cpwatmmncp.yfilter != YFilter.not_set or
                    self.cpwatmoamcellsupported.yfilter != YFilter.not_set or
                    self.cpwatmpeermncp.yfilter != YFilter.not_set or
                    self.cpwatmpktsreceived.yfilter != YFilter.not_set or
                    self.cpwatmpktsrejected.yfilter != YFilter.not_set or
                    self.cpwatmpktssent.yfilter != YFilter.not_set or
                    self.cpwatmqosscalingfactor.yfilter != YFilter.not_set or
                    self.cpwatmrowstatus.yfilter != YFilter.not_set or
                    self.cpwatmvci.yfilter != YFilter.not_set or
                    self.cpwatmvpi.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwVcAtmEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/cpwVcAtmTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwatmavgcellspacked.is_set or self.cpwatmavgcellspacked.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmavgcellspacked.get_name_leafdata())
                if (self.cpwatmcellpacking.is_set or self.cpwatmcellpacking.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmcellpacking.get_name_leafdata())
                if (self.cpwatmcellsreceived.is_set or self.cpwatmcellsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmcellsreceived.get_name_leafdata())
                if (self.cpwatmcellsrejected.is_set or self.cpwatmcellsrejected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmcellsrejected.get_name_leafdata())
                if (self.cpwatmcellssent.is_set or self.cpwatmcellssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmcellssent.get_name_leafdata())
                if (self.cpwatmcellstagged.is_set or self.cpwatmcellstagged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmcellstagged.get_name_leafdata())
                if (self.cpwatmclpqosmapping.is_set or self.cpwatmclpqosmapping.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmclpqosmapping.get_name_leafdata())
                if (self.cpwatmencap.is_set or self.cpwatmencap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmencap.get_name_leafdata())
                if (self.cpwatmhccellsreceived.is_set or self.cpwatmhccellsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmhccellsreceived.get_name_leafdata())
                if (self.cpwatmhccellsrejected.is_set or self.cpwatmhccellsrejected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmhccellsrejected.get_name_leafdata())
                if (self.cpwatmhccellstagged.is_set or self.cpwatmhccellstagged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmhccellstagged.get_name_leafdata())
                if (self.cpwatmif.is_set or self.cpwatmif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmif.get_name_leafdata())
                if (self.cpwatmmcpttimeout.is_set or self.cpwatmmcpttimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmmcpttimeout.get_name_leafdata())
                if (self.cpwatmmncp.is_set or self.cpwatmmncp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmmncp.get_name_leafdata())
                if (self.cpwatmoamcellsupported.is_set or self.cpwatmoamcellsupported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmoamcellsupported.get_name_leafdata())
                if (self.cpwatmpeermncp.is_set or self.cpwatmpeermncp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmpeermncp.get_name_leafdata())
                if (self.cpwatmpktsreceived.is_set or self.cpwatmpktsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmpktsreceived.get_name_leafdata())
                if (self.cpwatmpktsrejected.is_set or self.cpwatmpktsrejected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmpktsrejected.get_name_leafdata())
                if (self.cpwatmpktssent.is_set or self.cpwatmpktssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmpktssent.get_name_leafdata())
                if (self.cpwatmqosscalingfactor.is_set or self.cpwatmqosscalingfactor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmqosscalingfactor.get_name_leafdata())
                if (self.cpwatmrowstatus.is_set or self.cpwatmrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmrowstatus.get_name_leafdata())
                if (self.cpwatmvci.is_set or self.cpwatmvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmvci.get_name_leafdata())
                if (self.cpwatmvpi.is_set or self.cpwatmvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwatmvpi.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwAtmAvgCellsPacked" or name == "cpwAtmCellPacking" or name == "cpwAtmCellsReceived" or name == "cpwAtmCellsRejected" or name == "cpwAtmCellsSent" or name == "cpwAtmCellsTagged" or name == "cpwAtmClpQosMapping" or name == "cpwAtmEncap" or name == "cpwAtmHCCellsReceived" or name == "cpwAtmHCCellsRejected" or name == "cpwAtmHCCellsTagged" or name == "cpwAtmIf" or name == "cpwAtmMcptTimeout" or name == "cpwAtmMncp" or name == "cpwAtmOamCellSupported" or name == "cpwAtmPeerMncp" or name == "cpwAtmPktsReceived" or name == "cpwAtmPktsRejected" or name == "cpwAtmPktsSent" or name == "cpwAtmQosScalingFactor" or name == "cpwAtmRowStatus" or name == "cpwAtmVci" or name == "cpwAtmVpi"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmAvgCellsPacked"):
                    self.cpwatmavgcellspacked = value
                    self.cpwatmavgcellspacked.value_namespace = name_space
                    self.cpwatmavgcellspacked.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmCellPacking"):
                    self.cpwatmcellpacking = value
                    self.cpwatmcellpacking.value_namespace = name_space
                    self.cpwatmcellpacking.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmCellsReceived"):
                    self.cpwatmcellsreceived = value
                    self.cpwatmcellsreceived.value_namespace = name_space
                    self.cpwatmcellsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmCellsRejected"):
                    self.cpwatmcellsrejected = value
                    self.cpwatmcellsrejected.value_namespace = name_space
                    self.cpwatmcellsrejected.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmCellsSent"):
                    self.cpwatmcellssent = value
                    self.cpwatmcellssent.value_namespace = name_space
                    self.cpwatmcellssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmCellsTagged"):
                    self.cpwatmcellstagged = value
                    self.cpwatmcellstagged.value_namespace = name_space
                    self.cpwatmcellstagged.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmClpQosMapping"):
                    self.cpwatmclpqosmapping = value
                    self.cpwatmclpqosmapping.value_namespace = name_space
                    self.cpwatmclpqosmapping.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmEncap"):
                    self.cpwatmencap = value
                    self.cpwatmencap.value_namespace = name_space
                    self.cpwatmencap.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmHCCellsReceived"):
                    self.cpwatmhccellsreceived = value
                    self.cpwatmhccellsreceived.value_namespace = name_space
                    self.cpwatmhccellsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmHCCellsRejected"):
                    self.cpwatmhccellsrejected = value
                    self.cpwatmhccellsrejected.value_namespace = name_space
                    self.cpwatmhccellsrejected.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmHCCellsTagged"):
                    self.cpwatmhccellstagged = value
                    self.cpwatmhccellstagged.value_namespace = name_space
                    self.cpwatmhccellstagged.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmIf"):
                    self.cpwatmif = value
                    self.cpwatmif.value_namespace = name_space
                    self.cpwatmif.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmMcptTimeout"):
                    self.cpwatmmcpttimeout = value
                    self.cpwatmmcpttimeout.value_namespace = name_space
                    self.cpwatmmcpttimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmMncp"):
                    self.cpwatmmncp = value
                    self.cpwatmmncp.value_namespace = name_space
                    self.cpwatmmncp.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmOamCellSupported"):
                    self.cpwatmoamcellsupported = value
                    self.cpwatmoamcellsupported.value_namespace = name_space
                    self.cpwatmoamcellsupported.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmPeerMncp"):
                    self.cpwatmpeermncp = value
                    self.cpwatmpeermncp.value_namespace = name_space
                    self.cpwatmpeermncp.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmPktsReceived"):
                    self.cpwatmpktsreceived = value
                    self.cpwatmpktsreceived.value_namespace = name_space
                    self.cpwatmpktsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmPktsRejected"):
                    self.cpwatmpktsrejected = value
                    self.cpwatmpktsrejected.value_namespace = name_space
                    self.cpwatmpktsrejected.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmPktsSent"):
                    self.cpwatmpktssent = value
                    self.cpwatmpktssent.value_namespace = name_space
                    self.cpwatmpktssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmQosScalingFactor"):
                    self.cpwatmqosscalingfactor = value
                    self.cpwatmqosscalingfactor.value_namespace = name_space
                    self.cpwatmqosscalingfactor.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmRowStatus"):
                    self.cpwatmrowstatus = value
                    self.cpwatmrowstatus.value_namespace = name_space
                    self.cpwatmrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmVci"):
                    self.cpwatmvci = value
                    self.cpwatmvci.value_namespace = name_space
                    self.cpwatmvci.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwAtmVpi"):
                    self.cpwatmvpi = value
                    self.cpwatmvpi.value_namespace = name_space
                    self.cpwatmvpi.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwvcatmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwvcatmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwVcAtmTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwVcAtmEntry"):
                for c in self.cpwvcatmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwvcatmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwVcAtmEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.cpwvcatmtable is not None and self.cpwvcatmtable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpwvcatmtable is not None and self.cpwvcatmtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB" + path_buffer

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

        if (child_yang_name == "cpwVcAtmTable"):
            if (self.cpwvcatmtable is None):
                self.cpwvcatmtable = CiscoIetfPwAtmMib.Cpwvcatmtable()
                self.cpwvcatmtable.parent = self
                self._children_name_map["cpwvcatmtable"] = "cpwVcAtmTable"
            return self.cpwvcatmtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpwVcAtmTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfPwAtmMib()
        return self._top_entity

