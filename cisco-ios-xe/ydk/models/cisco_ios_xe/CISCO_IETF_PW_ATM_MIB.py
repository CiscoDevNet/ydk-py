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
    	**type**\:  :py:class:`Cpwvcatmtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.Cpwvcatmtable>`
    
    

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
        self._child_container_classes = OrderedDict([("cpwVcAtmTable", ("cpwvcatmtable", CISCOIETFPWATMMIB.Cpwvcatmtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpwvcatmtable = CISCOIETFPWATMMIB.Cpwvcatmtable()
        self.cpwvcatmtable.parent = self
        self._children_name_map["cpwvcatmtable"] = "cpwVcAtmTable"
        self._children_yang_names.add("cpwVcAtmTable")
        self._segment_path = lambda: "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB"


    class Cpwvcatmtable(Entity):
        """
        This table specifies the information for an ATM interface, VC,
        VP to be carried over PSN.
        
        .. attribute:: cpwvcatmentry
        
        	A row in this table represents an ATM interface, VC, VP that needs to be adapted and carried over PSN. This table is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB
        	**type**\: list of  		 :py:class:`Cpwvcatmentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.Cpwvcatmtable.Cpwvcatmentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-ATM-MIB'
        _revision = '2005-04-19'

        def __init__(self):
            super(CISCOIETFPWATMMIB.Cpwvcatmtable, self).__init__()

            self.yang_name = "cpwVcAtmTable"
            self.yang_parent_name = "CISCO-IETF-PW-ATM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cpwVcAtmEntry", ("cpwvcatmentry", CISCOIETFPWATMMIB.Cpwvcatmtable.Cpwvcatmentry))])
            self._leafs = OrderedDict()

            self.cpwvcatmentry = YList(self)
            self._segment_path = lambda: "cpwVcAtmTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-ATM-MIB:CISCO-IETF-PW-ATM-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWATMMIB.Cpwvcatmtable, [], name, value)


        class Cpwvcatmentry(Entity):
            """
            A row in this table represents an ATM interface, VC, VP
            that needs to be adapted and carried over PSN. This table
            is indexed by CpwVcIndex in CISCO\-IETF\-PW\-MIB.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwatmif
            
            	The ATM Interface that receives cells from the ATM network
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpwatmvpi
            
            	VPI value of this ATM VC
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cpwatmvci
            
            	VCI value of this ATM VC
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwatmclpqosmapping
            
            	This Object indicates whether the CLP bits are considered when determining the value placed in the Quality of Service fields (e.g. EXP fields of the MPLS Label Stack) of the encapsulating protocol
            	**type**\: bool
            
            .. attribute:: cpwatmrowstatus
            
            	This Object is used to create, modify or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cpwatmoamcellsupported
            
            	This Object indicates whether OAM Cells are transported on this VC
            	**type**\: bool
            
            .. attribute:: cpwatmqosscalingfactor
            
            	This Object represents the scaling factor (% value) to be applied to ATM QoS rates when calculating QoS rates for the PSN domain . For example, in the cell transport mode the bandwidth needed in the PSN domain will be higher (since PSN Transport header, PW header, and optional control word have to transmitted with every cell), whereas in the AAL5 mode the bandwidth needed in PSN domain will be less since cell headers will be removed after reassembly
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmcellpacking
            
            	This object is used to identify if the VC is configured to do Cell Packing
            	**type**\: bool
            
            .. attribute:: cpwatmmncp
            
            	This object indicates the maximum number of cells that get packed in one packet
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmpeermncp
            
            	This Object represents the maximum number of cell that can be packed in one packet for peer interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmencap
            
            	This object indicates if the packet going on the pseudowire is mpls or l2tpv3 encapsulated
            	**type**\:  :py:class:`Cpwatmencap <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB.CISCOIETFPWATMMIB.Cpwvcatmtable.Cpwvcatmentry.Cpwatmencap>`
            
            .. attribute:: cpwatmmcpttimeout
            
            	This Object represents which MCPT timeout value
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwatmcellsreceived
            
            	This object can be used to obtain the information on the number of cells that were received and sent to the PSN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellssent
            
            	This object can be used to obtain the information on the number of cells that were received from the PSN and sent over the ATM network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellsrejected
            
            	This Object indicates the number of cells that were rejected by this VC because of policing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmcellstagged
            
            	This Object indicates the number of cells that were Tagged
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmhccellsreceived
            
            	High Capacity counter for the number of cells that were received by this VC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellsrejected
            
            	High Capacity counter for the number of cells that were rejected by this VC because of policing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmhccellstagged
            
            	High Capacity counter for the number of cells that were tagged
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpwatmavgcellspacked
            
            	It indicates the Average number of cells that were received in one packet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktsreceived
            
            	This object can be used to obtain the information on the number of packets that were received and sent to the PSN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktssent
            
            	This object indicates the number of packets that were sent to the atm network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwatmpktsrejected
            
            	This object indicates the number of packets that were rejected because of Policing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-ATM-MIB'
            _revision = '2005-04-19'

            def __init__(self):
                super(CISCOIETFPWATMMIB.Cpwvcatmtable.Cpwvcatmentry, self).__init__()

                self.yang_name = "cpwVcAtmEntry"
                self.yang_parent_name = "cpwVcAtmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', YLeaf(YType.str, 'cpwVcIndex')),
                    ('cpwatmif', YLeaf(YType.int32, 'cpwAtmIf')),
                    ('cpwatmvpi', YLeaf(YType.int32, 'cpwAtmVpi')),
                    ('cpwatmvci', YLeaf(YType.int32, 'cpwAtmVci')),
                    ('cpwatmclpqosmapping', YLeaf(YType.boolean, 'cpwAtmClpQosMapping')),
                    ('cpwatmrowstatus', YLeaf(YType.enumeration, 'cpwAtmRowStatus')),
                    ('cpwatmoamcellsupported', YLeaf(YType.boolean, 'cpwAtmOamCellSupported')),
                    ('cpwatmqosscalingfactor', YLeaf(YType.int32, 'cpwAtmQosScalingFactor')),
                    ('cpwatmcellpacking', YLeaf(YType.boolean, 'cpwAtmCellPacking')),
                    ('cpwatmmncp', YLeaf(YType.int32, 'cpwAtmMncp')),
                    ('cpwatmpeermncp', YLeaf(YType.int32, 'cpwAtmPeerMncp')),
                    ('cpwatmencap', YLeaf(YType.enumeration, 'cpwAtmEncap')),
                    ('cpwatmmcpttimeout', YLeaf(YType.int32, 'cpwAtmMcptTimeout')),
                    ('cpwatmcellsreceived', YLeaf(YType.uint32, 'cpwAtmCellsReceived')),
                    ('cpwatmcellssent', YLeaf(YType.uint32, 'cpwAtmCellsSent')),
                    ('cpwatmcellsrejected', YLeaf(YType.uint32, 'cpwAtmCellsRejected')),
                    ('cpwatmcellstagged', YLeaf(YType.uint32, 'cpwAtmCellsTagged')),
                    ('cpwatmhccellsreceived', YLeaf(YType.uint64, 'cpwAtmHCCellsReceived')),
                    ('cpwatmhccellsrejected', YLeaf(YType.uint64, 'cpwAtmHCCellsRejected')),
                    ('cpwatmhccellstagged', YLeaf(YType.uint64, 'cpwAtmHCCellsTagged')),
                    ('cpwatmavgcellspacked', YLeaf(YType.uint32, 'cpwAtmAvgCellsPacked')),
                    ('cpwatmpktsreceived', YLeaf(YType.uint32, 'cpwAtmPktsReceived')),
                    ('cpwatmpktssent', YLeaf(YType.uint32, 'cpwAtmPktsSent')),
                    ('cpwatmpktsrejected', YLeaf(YType.uint32, 'cpwAtmPktsRejected')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWATMMIB.Cpwvcatmtable.Cpwvcatmentry, ['cpwvcindex', 'cpwatmif', 'cpwatmvpi', 'cpwatmvci', 'cpwatmclpqosmapping', 'cpwatmrowstatus', 'cpwatmoamcellsupported', 'cpwatmqosscalingfactor', 'cpwatmcellpacking', 'cpwatmmncp', 'cpwatmpeermncp', 'cpwatmencap', 'cpwatmmcpttimeout', 'cpwatmcellsreceived', 'cpwatmcellssent', 'cpwatmcellsrejected', 'cpwatmcellstagged', 'cpwatmhccellsreceived', 'cpwatmhccellsrejected', 'cpwatmhccellstagged', 'cpwatmavgcellspacked', 'cpwatmpktsreceived', 'cpwatmpktssent', 'cpwatmpktsrejected'], name, value)

            class Cpwatmencap(Enum):
                """
                Cpwatmencap (Enum Class)

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

