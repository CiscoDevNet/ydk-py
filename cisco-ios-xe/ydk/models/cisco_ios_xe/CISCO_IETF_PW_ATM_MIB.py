""" CISCO_IETF_PW_ATM_MIB 

This MIB contains managed object definitions for Pseudo Wire
emulation of ATM over Packet Switched Networks(PSN).

This MIB reports to the PW\-MIB. The PW\-MIB contains
structures and MIB associations generic to Pseudo\-Wire
Virtual Circuit (VC) emulation. VC\-specific MIBs (such as
this) contain config and stats for specific VC types.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIETFPWATMMIB(Entity):
    """
    
    
    .. attribute:: cpwvcatmtable
    
    	This table specifies the information for an ATM interface, VC, VP to be carried over PSN
    	**type**\:  :py:class:`CpwVcAtmTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.CpwVcAtmTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IETF-PW-ATM-MIB'
    _revision = '2005-04-19'

    def __init__(self):
        super(CISCOIETFPWATMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-ATM-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-ATM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpwVcAtmTable", ("cpwvcatmtable", CISCOIETFPWATMMIB.CpwVcAtmTable))])
        self._leafs = OrderedDict()

        self.cpwvcatmtable = CISCOIETFPWATMMIB.CpwVcAtmTable()
        self.cpwvcatmtable.parent = self
        self._children_name_map["cpwvcatmtable"] = "cpwVcAtmTable"
        self._segment_path = lambda: "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIETFPWATMMIB, [], name, value)


    class CpwVcAtmTable(Entity):
        """
        This table specifies the information for an ATM interface, VC,
        VP to be carried over PSN.
        
        .. attribute:: cpwvcatmentry
        
        	A row in this table represents an ATM interface, VC, VP that needs to be adapted and carried over PSN. This table is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB
        	**type**\: list of  		 :py:class:`CpwVcAtmEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.CpwVcAtmTable.CpwVcAtmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-ATM-MIB'
        _revision = '2005-04-19'

        def __init__(self):
            super(CISCOIETFPWATMMIB.CpwVcAtmTable, self).__init__()

            self.yang_name = "cpwVcAtmTable"
            self.yang_parent_name = "CISCO-IETF-PW-ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcAtmEntry", ("cpwvcatmentry", CISCOIETFPWATMMIB.CpwVcAtmTable.CpwVcAtmEntry))])
            self._leafs = OrderedDict()

            self.cpwvcatmentry = YList(self)
            self._segment_path = lambda: "cpwVcAtmTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWATMMIB.CpwVcAtmTable, [], name, value)


        class CpwVcAtmEntry(Entity):
            """
            A row in this table represents an ATM interface, VC, VP
            that needs to be adapted and carried over PSN. This table
            is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwatmif
            
            	The ATM Interface that receives cells from the ATM network
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwatmvpi
            
            	VPI value of this ATM VC
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: cpwatmvci
            
            	VCI value of this ATM VC
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cpwatmclpqosmapping
            
            	This Object indicates whether the CLP bits are considered when determining the value placed in the Quality of Service fields (e.g. EXP fields of the MPLS Label Stack) of the encapsulating protocol
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cpwatmrowstatus
            
            	This Object is used to create, modify or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cpwatmoamcellsupported
            
            	This Object indicates whether OAM Cells are transported on this VC
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cpwatmqosscalingfactor
            
            	This Object represents the scaling factor (% value) to be applied to ATM QoS rates when calculating QoS rates for the PSN domain . For example, in the cell transport mode the bandwidth needed in the PSN domain will be higher (since PSN Transport header, PW header, and optional control word have to transmitted with every cell), whereas in the AAL5 mode the bandwidth needed in PSN domain will be less since cell headers will be removed after reassembly
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwatmcellpacking
            
            	This object is used to identify if the VC is configured to do Cell Packing
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cpwatmmncp
            
            	This object indicates the maximum number of cells that get packed in one packet
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwatmpeermncp
            
            	This Object represents the maximum number of cell that can be packed in one packet for peer interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwatmencap
            
            	This object indicates if the packet going on the pseudowire is mpls or l2tpv3 encapsulated
            	**type**\:  :py:class:`CpwAtmEncap <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.CpwVcAtmTable.CpwVcAtmEntry.CpwAtmEncap>`
            
            	**config**\: False
            
            .. attribute:: cpwatmmcpttimeout
            
            	This Object represents which MCPT timeout value
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwatmcellsreceived
            
            	This object can be used to obtain the information on the number of cells that were received and sent to the PSN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmcellssent
            
            	This object can be used to obtain the information on the number of cells that were received from the PSN and sent over the ATM network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmcellsrejected
            
            	This Object indicates the number of cells that were rejected by this VC because of policing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmcellstagged
            
            	This Object indicates the number of cells that were Tagged
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmhccellsreceived
            
            	High Capacity counter for the number of cells that were received by this VC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cpwatmhccellsrejected
            
            	High Capacity counter for the number of cells that were rejected by this VC because of policing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cpwatmhccellstagged
            
            	High Capacity counter for the number of cells that were tagged
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cpwatmavgcellspacked
            
            	It indicates the Average number of cells that were received in one packet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmpktsreceived
            
            	This object can be used to obtain the information on the number of packets that were received and sent to the PSN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmpktssent
            
            	This object indicates the number of packets that were sent to the atm network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpwatmpktsrejected
            
            	This object indicates the number of packets that were rejected because of Policing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-ATM-MIB'
            _revision = '2005-04-19'

            def __init__(self):
                super(CISCOIETFPWATMMIB.CpwVcAtmTable.CpwVcAtmEntry, self).__init__()

                self.yang_name = "cpwVcAtmEntry"
                self.yang_parent_name = "cpwVcAtmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwatmif', (YLeaf(YType.int32, 'cpwAtmIf'), ['int'])),
                    ('cpwatmvpi', (YLeaf(YType.int32, 'cpwAtmVpi'), ['int'])),
                    ('cpwatmvci', (YLeaf(YType.int32, 'cpwAtmVci'), ['int'])),
                    ('cpwatmclpqosmapping', (YLeaf(YType.boolean, 'cpwAtmClpQosMapping'), ['bool'])),
                    ('cpwatmrowstatus', (YLeaf(YType.enumeration, 'cpwAtmRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cpwatmoamcellsupported', (YLeaf(YType.boolean, 'cpwAtmOamCellSupported'), ['bool'])),
                    ('cpwatmqosscalingfactor', (YLeaf(YType.int32, 'cpwAtmQosScalingFactor'), ['int'])),
                    ('cpwatmcellpacking', (YLeaf(YType.boolean, 'cpwAtmCellPacking'), ['bool'])),
                    ('cpwatmmncp', (YLeaf(YType.int32, 'cpwAtmMncp'), ['int'])),
                    ('cpwatmpeermncp', (YLeaf(YType.int32, 'cpwAtmPeerMncp'), ['int'])),
                    ('cpwatmencap', (YLeaf(YType.enumeration, 'cpwAtmEncap'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB', 'CISCOIETFPWATMMIB', 'CpwVcAtmTable.CpwVcAtmEntry.CpwAtmEncap')])),
                    ('cpwatmmcpttimeout', (YLeaf(YType.int32, 'cpwAtmMcptTimeout'), ['int'])),
                    ('cpwatmcellsreceived', (YLeaf(YType.uint32, 'cpwAtmCellsReceived'), ['int'])),
                    ('cpwatmcellssent', (YLeaf(YType.uint32, 'cpwAtmCellsSent'), ['int'])),
                    ('cpwatmcellsrejected', (YLeaf(YType.uint32, 'cpwAtmCellsRejected'), ['int'])),
                    ('cpwatmcellstagged', (YLeaf(YType.uint32, 'cpwAtmCellsTagged'), ['int'])),
                    ('cpwatmhccellsreceived', (YLeaf(YType.uint64, 'cpwAtmHCCellsReceived'), ['int'])),
                    ('cpwatmhccellsrejected', (YLeaf(YType.uint64, 'cpwAtmHCCellsRejected'), ['int'])),
                    ('cpwatmhccellstagged', (YLeaf(YType.uint64, 'cpwAtmHCCellsTagged'), ['int'])),
                    ('cpwatmavgcellspacked', (YLeaf(YType.uint32, 'cpwAtmAvgCellsPacked'), ['int'])),
                    ('cpwatmpktsreceived', (YLeaf(YType.uint32, 'cpwAtmPktsReceived'), ['int'])),
                    ('cpwatmpktssent', (YLeaf(YType.uint32, 'cpwAtmPktsSent'), ['int'])),
                    ('cpwatmpktsrejected', (YLeaf(YType.uint32, 'cpwAtmPktsRejected'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwatmif = None
                self.cpwatmvpi = None
                self.cpwatmvci = None
                self.cpwatmclpqosmapping = None
                self.cpwatmrowstatus = None
                self.cpwatmoamcellsupported = None
                self.cpwatmqosscalingfactor = None
                self.cpwatmcellpacking = None
                self.cpwatmmncp = None
                self.cpwatmpeermncp = None
                self.cpwatmencap = None
                self.cpwatmmcpttimeout = None
                self.cpwatmcellsreceived = None
                self.cpwatmcellssent = None
                self.cpwatmcellsrejected = None
                self.cpwatmcellstagged = None
                self.cpwatmhccellsreceived = None
                self.cpwatmhccellsrejected = None
                self.cpwatmhccellstagged = None
                self.cpwatmavgcellspacked = None
                self.cpwatmpktsreceived = None
                self.cpwatmpktssent = None
                self.cpwatmpktsrejected = None
                self._segment_path = lambda: "cpwVcAtmEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/cpwVcAtmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWATMMIB.CpwVcAtmTable.CpwVcAtmEntry, ['cpwvcindex', 'cpwatmif', 'cpwatmvpi', 'cpwatmvci', 'cpwatmclpqosmapping', 'cpwatmrowstatus', 'cpwatmoamcellsupported', 'cpwatmqosscalingfactor', 'cpwatmcellpacking', 'cpwatmmncp', 'cpwatmpeermncp', 'cpwatmencap', 'cpwatmmcpttimeout', 'cpwatmcellsreceived', 'cpwatmcellssent', 'cpwatmcellsrejected', 'cpwatmcellstagged', 'cpwatmhccellsreceived', 'cpwatmhccellsrejected', 'cpwatmhccellstagged', 'cpwatmavgcellspacked', 'cpwatmpktsreceived', 'cpwatmpktssent', 'cpwatmpktsrejected'], name, value)

            class CpwAtmEncap(Enum):
                """
                CpwAtmEncap (Enum Class)

                This object indicates if the packet going on the pseudowire

                is mpls or l2tpv3 encapsulated.

                .. data:: mpls = 1

                .. data:: l2tpv3 = 2

                .. data:: unknown = 3

                """

                mpls = Enum.YLeaf(1, "mpls")

                l2tpv3 = Enum.YLeaf(2, "l2tpv3")

                unknown = Enum.YLeaf(3, "unknown")




    def clone_ptr(self):
        self._top_entity = CISCOIETFPWATMMIB()
        return self._top_entity



