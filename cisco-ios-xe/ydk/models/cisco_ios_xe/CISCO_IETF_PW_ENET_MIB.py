""" CISCO_IETF_PW_ENET_MIB 

This MIB describes a model for managing Ethernet  
point\-to\-point pseudo wire services over a Packet  
Switched Network (PSN).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIETFPWENETMIB(Entity):
    """
    
    
    .. attribute:: cpwvcenettable
    
    	This table contains the index to the Ethernet tables   associated with this ETH VC, the VLAN configuration and   VLAN mode
    	**type**\:  :py:class:`CpwVcEnetTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcenetmplsprimappingtable
    
    	This table may be used for MPLS PSNs if there is a need   to hold multiple VC, each with different COS, for the same  user service (port + PW VLAN). Such a need may arise if the  MPLS network is capable of L\-LSP or E\-LSP without multiple  COS capabilities.  Each row is indexed by the cpwVcIndex   and indicate the PRI bits on the packet recieved from the   user port (or VPLS virtual port) that are  classified to this VC. Note that the EXP bit value of the VC  is configured in the CISCO\-IETF\-PW\-MPLS\-MIB
    	**type**\:  :py:class:`CpwVcEnetMplsPriMappingTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cpwvcenetstatstable
    
    	This table contains statistical counters specific for   Ethernet PW
    	**type**\:  :py:class:`CpwVcEnetStatsTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetStatsTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IETF-PW-ENET-MIB'
    _revision = '2002-09-22'

    def __init__(self):
        super(CISCOIETFPWENETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-ENET-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpwVcEnetTable", ("cpwvcenettable", CISCOIETFPWENETMIB.CpwVcEnetTable)), ("cpwVcEnetMplsPriMappingTable", ("cpwvcenetmplsprimappingtable", CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable)), ("cpwVcEnetStatsTable", ("cpwvcenetstatstable", CISCOIETFPWENETMIB.CpwVcEnetStatsTable))])
        self._leafs = OrderedDict()

        self.cpwvcenettable = CISCOIETFPWENETMIB.CpwVcEnetTable()
        self.cpwvcenettable.parent = self
        self._children_name_map["cpwvcenettable"] = "cpwVcEnetTable"

        self.cpwvcenetmplsprimappingtable = CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable()
        self.cpwvcenetmplsprimappingtable.parent = self
        self._children_name_map["cpwvcenetmplsprimappingtable"] = "cpwVcEnetMplsPriMappingTable"

        self.cpwvcenetstatstable = CISCOIETFPWENETMIB.CpwVcEnetStatsTable()
        self.cpwvcenetstatstable.parent = self
        self._children_name_map["cpwvcenetstatstable"] = "cpwVcEnetStatsTable"
        self._segment_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIETFPWENETMIB, [], name, value)


    class CpwVcEnetTable(Entity):
        """
        This table contains the index to the Ethernet tables  
        associated with this ETH VC, the VLAN configuration and  
        VLAN mode.
        
        .. attribute:: cpwvcenetentry
        
        	This table is indexed by the same index that was created   for the associated entry in the PW VC Table in the  CISCO\-IETF\-PW\-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan  are used as indexes to allow multiple VLANs to exist on  the same PW.   An entry is created in this table by the agent for every   entry in the cpwVc table with a VcType of 'ethernetVLAN',  'ethernet' or 'ethernetVPLS'. Additional rows may be   created by the operator or the agent if multiple entries  are required for the same VC.   This table provides Ethernet port mapping and VLAN   configuration for each Ethernet VC
        	**type**\: list of  		 :py:class:`CpwVcEnetEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetTable.CpwVcEnetEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CISCOIETFPWENETMIB.CpwVcEnetTable, self).__init__()

            self.yang_name = "cpwVcEnetTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcEnetEntry", ("cpwvcenetentry", CISCOIETFPWENETMIB.CpwVcEnetTable.CpwVcEnetEntry))])
            self._leafs = OrderedDict()

            self.cpwvcenetentry = YList(self)
            self._segment_path = lambda: "cpwVcEnetTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetTable, [], name, value)


        class CpwVcEnetEntry(Entity):
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
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetpwvlan  (key)
            
            	This Object defines the VLAN on the VC. The value of 4097  is used if the object is not applicable, for example when  mapping all packets from an Ethernet port to this VC.  The value of 4096 is used to indicate untagged frames (at   least from the PW point of view), for example if   cpwVcEnetVlanMode is equal 'removeVLAN' or when   cpwVcEnetVlanMode equal 'noChange' and cpwVcEnetPortVlan  is equal 4096
            	**type**\: int
            
            	**range:** 0..4097
            
            	**config**\: False
            
            .. attribute:: cpwvcenetvlanmode
            
            	Indicate the mode of VLAN handling between the port   associated to the VC and the VC encapsulation itself.   \- 'other' indicate operation that is not defined by    this MIB.   \- 'portBased' indicates that the forwarder will forward    packets between the port and the PW independent of their    structure.   \- 'noChange' indicates that the VC contains the original     user VLAN, as specified in cpwVcEnetPortVlan.   \- 'changeVlan' indicates that the VLAN field on the VC     may be different than the VLAN field on the user's     port.   \- 'removeVlan' indicates that the encapsulation on the     VC does not include the original VLAN field. Note     that PRI bits transparency is lost in this case.   \- 'addVlan' indicate that a VLAN field will be added    on the PSN bound direction. cpwVcEnetPwVlan indicate    the value that will be added.    \- 'removeVlan', 'addVlan' and 'changeVlan' implementation    is not required. 
            	**type**\:  :py:class:`CpwVcEnetVlanMode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetTable.CpwVcEnetEntry.CpwVcEnetVlanMode>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetportvlan
            
            	This object define the VLAN value on the physical port (or   VPLS virtual port) if a change is required to the VLAN value  between the VC and the physical/virtual port.   The value of this object can be ignored if the whole traffic   from the port is forwarded to one VC independent of the   tagging on the port, but it is RECOMENDED that the value in  this case will be '4097' indicating not relevant.   It MUST be equal to cpwVcEnetPwVlan if 'noChange' mode  is used.   The value 4096 indicate that no VLAN (i.e. untagged   frames) on the port are associated to this VC. This   allows the same behaviors as assigning 'Default VLAN'   to un\-tagged frames. 
            	**type**\: int
            
            	**range:** 0..4097
            
            	**config**\: False
            
            .. attribute:: cpwvcenetvcifindex
            
            	It is sometimes convenient to model the VC PW as a   virtual interface in the ifTable. In these cases this   object hold the value of the ifIndex in the ifTable   representing this VC PW. A value of zero indicate no such   association or association is not yet known
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwvcenetportifindex
            
            	This object is used to specify the ifIndex of the ETHERNET  port associated with this VC for point\-to\-point Ethernet   service, or the ifIndex of the virtual interface of the VPLS   instance associated with the PW if the service is VPLS. Two   rows in this table can point to the same ifIndex only if\:   1) It is required to support multiple COS on a MPLS PSN      for the same service (i.e.\: a combination of ports and      VLANs) by the use of multiple VC, each with a different     COS.   2) There is no overlap of VLAN values specified in      cpwVcEnetPortVlan that are associated with this port.   A value of zero indicate that association to an ifIndex is  not yet known
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpwvcenetrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetstoragetype
            
            	Indicates the storage type of this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CISCOIETFPWENETMIB.CpwVcEnetTable.CpwVcEnetEntry, self).__init__()

                self.yang_name = "cpwVcEnetEntry"
                self.yang_parent_name = "cpwVcEnetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwvcenetpwvlan']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcenetpwvlan', (YLeaf(YType.int32, 'cpwVcEnetPwVlan'), ['int'])),
                    ('cpwvcenetvlanmode', (YLeaf(YType.enumeration, 'cpwVcEnetVlanMode'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CISCOIETFPWENETMIB', 'CpwVcEnetTable.CpwVcEnetEntry.CpwVcEnetVlanMode')])),
                    ('cpwvcenetportvlan', (YLeaf(YType.int32, 'cpwVcEnetPortVlan'), ['int'])),
                    ('cpwvcenetvcifindex', (YLeaf(YType.int32, 'cpwVcEnetVcIfIndex'), ['int'])),
                    ('cpwvcenetportifindex', (YLeaf(YType.int32, 'cpwVcEnetPortIfIndex'), ['int'])),
                    ('cpwvcenetrowstatus', (YLeaf(YType.enumeration, 'cpwVcEnetRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cpwvcenetstoragetype', (YLeaf(YType.enumeration, 'cpwVcEnetStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cpwvcindex = None
                self.cpwvcenetpwvlan = None
                self.cpwvcenetvlanmode = None
                self.cpwvcenetportvlan = None
                self.cpwvcenetvcifindex = None
                self.cpwvcenetportifindex = None
                self.cpwvcenetrowstatus = None
                self.cpwvcenetstoragetype = None
                self._segment_path = lambda: "cpwVcEnetEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwVcEnetPwVlan='" + str(self.cpwvcenetpwvlan) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetTable.CpwVcEnetEntry, ['cpwvcindex', 'cpwvcenetpwvlan', 'cpwvcenetvlanmode', 'cpwvcenetportvlan', 'cpwvcenetvcifindex', 'cpwvcenetportifindex', 'cpwvcenetrowstatus', 'cpwvcenetstoragetype'], name, value)

            class CpwVcEnetVlanMode(Enum):
                """
                CpwVcEnetVlanMode (Enum Class)

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





    class CpwVcEnetMplsPriMappingTable(Entity):
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
        	**type**\: list of  		 :py:class:`CpwVcEnetMplsPriMappingTableEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable.CpwVcEnetMplsPriMappingTableEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable, self).__init__()

            self.yang_name = "cpwVcEnetMplsPriMappingTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcEnetMplsPriMappingTableEntry", ("cpwvcenetmplsprimappingtableentry", CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable.CpwVcEnetMplsPriMappingTableEntry))])
            self._leafs = OrderedDict()

            self.cpwvcenetmplsprimappingtableentry = YList(self)
            self._segment_path = lambda: "cpwVcEnetMplsPriMappingTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable, [], name, value)


        class CpwVcEnetMplsPriMappingTableEntry(Entity):
            """
            Each entry is created if special classification based on  
            the PRI bits is required for this VC.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetmplsprimapping
            
            	This object defines the groups of user PRI mapped into  this VC. Each bit set indicates that this user priority   is assigned to this VC.   The value 'untagged' is used to indicate that untagged   frames are also associated to this VC.   This object allow the use of different PSN COS based on   user marking of PRI bits in MPLS PSN with L\-LSP or   E\-LSP without multiple COS support. In all other cases,   the default value MUST be used.   It is REQUIRED that there is no overlap on this object   between rows serving the same service (port+ PW VLAN).   In case of missing BIT configuration between rows to   the same service, incoming packets with PRI marking not   configured should be handled by the VC with the lowest   COS. 
            	**type**\:  :py:class:`CpwVcEnetMplsPriMapping <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable.CpwVcEnetMplsPriMappingTableEntry.CpwVcEnetMplsPriMapping>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetmplsprimappingrowstatus
            
            	Enable creating, deleting and modifying this row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetmplsprimappingstoragetype
            
            	Indicates the storage type of this row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable.CpwVcEnetMplsPriMappingTableEntry, self).__init__()

                self.yang_name = "cpwVcEnetMplsPriMappingTableEntry"
                self.yang_parent_name = "cpwVcEnetMplsPriMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcenetmplsprimapping', (YLeaf(YType.bits, 'cpwVcEnetMplsPriMapping'), ['Bits'])),
                    ('cpwvcenetmplsprimappingrowstatus', (YLeaf(YType.enumeration, 'cpwVcEnetMplsPriMappingRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cpwvcenetmplsprimappingstoragetype', (YLeaf(YType.enumeration, 'cpwVcEnetMplsPriMappingStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cpwvcindex = None
                self.cpwvcenetmplsprimapping = Bits()
                self.cpwvcenetmplsprimappingrowstatus = None
                self.cpwvcenetmplsprimappingstoragetype = None
                self._segment_path = lambda: "cpwVcEnetMplsPriMappingTableEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetMplsPriMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetMplsPriMappingTable.CpwVcEnetMplsPriMappingTableEntry, ['cpwvcindex', 'cpwvcenetmplsprimapping', 'cpwvcenetmplsprimappingrowstatus', 'cpwvcenetmplsprimappingstoragetype'], name, value)




    class CpwVcEnetStatsTable(Entity):
        """
        This table contains statistical counters specific for  
        Ethernet PW.
        
        .. attribute:: cpwvcenetstatsentry
        
        	Each entry represents the statistics gathered for the   VC carrying the Ethernet packets since this VC was   first created in the cpwVcEnetTable
        	**type**\: list of  		 :py:class:`CpwVcEnetStatsEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB.CISCOIETFPWENETMIB.CpwVcEnetStatsTable.CpwVcEnetStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IETF-PW-ENET-MIB'
        _revision = '2002-09-22'

        def __init__(self):
            super(CISCOIETFPWENETMIB.CpwVcEnetStatsTable, self).__init__()

            self.yang_name = "cpwVcEnetStatsTable"
            self.yang_parent_name = "CISCO-IETF-PW-ENET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwVcEnetStatsEntry", ("cpwvcenetstatsentry", CISCOIETFPWENETMIB.CpwVcEnetStatsTable.CpwVcEnetStatsEntry))])
            self._leafs = OrderedDict()

            self.cpwvcenetstatsentry = YList(self)
            self._segment_path = lambda: "cpwVcEnetStatsTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetStatsTable, [], name, value)


        class CpwVcEnetStatsEntry(Entity):
            """
            Each entry represents the statistics gathered for the  
            VC carrying the Ethernet packets since this VC was  
            first created in the cpwVcEnetTable.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            	**config**\: False
            
            .. attribute:: cpwvcenetstatsillegalvlan
            
            	The number of packets received (from the PSN) on this VC with   an illegal VLAN field, missing VLAN field that was expected, or   A VLAN field when it was not expected. This counter is not   relevant if the VC type is 'ethernet' (i.e. raw mode), and   should be set to 0 by the agent to indicate this
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cpwvcenetstatsillegallength
            
            	The number of packets that were received with an illegal   Ethernet packet length on this VC. An illegal length is defined  as being greater than the value in the advertised maximum MTU   supported, or shorter than the allowed Ethernet packet size
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IETF-PW-ENET-MIB'
            _revision = '2002-09-22'

            def __init__(self):
                super(CISCOIETFPWENETMIB.CpwVcEnetStatsTable.CpwVcEnetStatsEntry, self).__init__()

                self.yang_name = "cpwVcEnetStatsEntry"
                self.yang_parent_name = "cpwVcEnetStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwvcenetstatsillegalvlan', (YLeaf(YType.uint64, 'cpwVcEnetStatsIllegalVlan'), ['int'])),
                    ('cpwvcenetstatsillegallength', (YLeaf(YType.uint64, 'cpwVcEnetStatsIllegalLength'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwvcenetstatsillegalvlan = None
                self.cpwvcenetstatsillegallength = None
                self._segment_path = lambda: "cpwVcEnetStatsEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-ENET-MIB:CISCO-IETF-PW-ENET-MIB/cpwVcEnetStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWENETMIB.CpwVcEnetStatsTable.CpwVcEnetStatsEntry, ['cpwvcindex', 'cpwvcenetstatsillegalvlan', 'cpwvcenetstatsillegallength'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOIETFPWENETMIB()
        return self._top_entity



