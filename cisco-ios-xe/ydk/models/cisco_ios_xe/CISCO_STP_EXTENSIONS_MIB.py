""" CISCO_STP_EXTENSIONS_MIB 

The MIB module for managing Cisco extensions to
the 802.1D Spanning Tree Protocol (STP).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOSTPEXTENSIONSMIB(Entity):
    """
    
    
    .. attribute:: stpxuplinkfastobjects
    
    	
    	**type**\:  :py:class:`Stpxuplinkfastobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxuplinkfastobjects>`
    
    .. attribute:: stpxbackbonefastobjects
    
    	
    	**type**\:  :py:class:`Stpxbackbonefastobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxbackbonefastobjects>`
    
    .. attribute:: stpxspanningtreeobjects
    
    	
    	**type**\:  :py:class:`Stpxspanningtreeobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects>`
    
    .. attribute:: stpxmistpobjects
    
    	
    	**type**\:  :py:class:`Stpxmistpobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmistpobjects>`
    
    .. attribute:: stpxloopguardobjects
    
    	
    	**type**\:  :py:class:`Stpxloopguardobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects>`
    
    .. attribute:: stpxfaststartobjects
    
    	
    	**type**\:  :py:class:`Stpxfaststartobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects>`
    
    .. attribute:: stpxbpduskewingobjects
    
    	
    	**type**\:  :py:class:`Stpxbpduskewingobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxbpduskewingobjects>`
    
    .. attribute:: stpxmstobjects
    
    	
    	**type**\:  :py:class:`Stpxmstobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstobjects>`
    
    .. attribute:: stpxrstpobjects
    
    	
    	**type**\:  :py:class:`Stpxrstpobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpobjects>`
    
    .. attribute:: stpxsmstobjects
    
    	
    	**type**\:  :py:class:`Stpxsmstobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstobjects>`
    
    .. attribute:: stpxpvstvlantable
    
    	A list of Virtual LAN entries containing information for Spanning Tree PVST+ protocol.  An entry will exist for each VLAN existing on  the device
    	**type**\:  :py:class:`Stpxpvstvlantable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable>`
    
    .. attribute:: stpxinconsistencytable
    
    	A table containing a list of the ports for which a particular VLAN's Spanning Tree has been found to have an inconsistency.  Two types of inconsistency are discovered\: 1) an inconsistency where two different port types have been plugged together; and 2) an inconsistency where different switches have different PVIDs for the same link
    	**type**\:  :py:class:`Stpxinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable>`
    
    .. attribute:: stpxrootguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree RootGuard capability can be configured
    	**type**\:  :py:class:`Stpxrootguardconfigtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable>`
    
    .. attribute:: stpxrootinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found  to have an root\-inconsistency. The agent creates a new  entry in this table whenever it detects a new  root\-inconsistency, and deletes entries  when/soon after the inconsistency is no longer present
    	**type**\:  :py:class:`Stpxrootinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable>`
    
    .. attribute:: stpxmistpinstancetable
    
    	This table contains one entry for each instance of MISTP and  it contains stpxMISTPInstanceNumber entries, numbered from 1 to stpxMISTPInstanceNumber.  This table is only instantiated when the value of  stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3)
    	**type**\:  :py:class:`Stpxmistpinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable>`
    
    .. attribute:: stpxloopguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree LoopGuard capability can be configured
    	**type**\:  :py:class:`Stpxloopguardconfigtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable>`
    
    .. attribute:: stpxloopinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found to have a loop\-inconsistency. The agent creates a new entry in this table whenever it detects a new loop\-inconsistency, and deletes entries when/soon after the inconsistency is no longer present
    	**type**\:  :py:class:`Stpxloopinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable>`
    
    .. attribute:: stpxfaststartporttable
    
    	A table containing a list of the bridge ports for which Spanning Tree Port Fast Start can be configured
    	**type**\:  :py:class:`Stpxfaststartporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable>`
    
    .. attribute:: stpxfaststartopermodetable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance
    	**type**\:  :py:class:`Stpxfaststartopermodetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable>`
    
    .. attribute:: stpxbpduskewingtable
    
    	A table containing a list of the bridge ports for  which a particular Spanning Tree instance has been  detected to have BPDU skewing occurred since the  object value of stpxBpduSkewingDetectionEnable was last changed to true(1).  The agent creates a new entry in this table whenever a port in a particular Spanning Tree instance is  detected to be BPDU skewed since the object value of  stpxBpduSkewingDetectionEnable object is changed to  true(1). The agent deletes all the entries in this  table when the object value of  stpxBpduSkewingDetectionEnable is changed to false(2) or the object value of stpxSpanningTreeType is  changed
    	**type**\:  :py:class:`Stpxbpduskewingtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable>`
    
    .. attribute:: stpxmstinstancetable
    
    	This table contains MST instance information with one entry for an MST instance within the range of  0 to the object value of stpxMSTMaxInstanceNumber.   This table is deprecated and replaced by  stpxSMSTInstanceTable
    	**type**\:  :py:class:`Stpxmstinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer with one entry for each MST instance numbered from 0 to stpxMSTMaxInstanceNumber.   This table is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2).  This table is deprecated and replaced by  stpxSMSTInstanceEditTable
    	**type**\:  :py:class:`Stpxmstinstanceedittable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system
    	**type**\:  :py:class:`Stpxmstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstporttable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstportroletable
    
    	A table containing a list of the bridge ports for a  particular MST instance.  This table is only instantiated  when the stpxSpanningTreeType is mst(4).   This table is deprecated and replaced with  stpxRSTPPortRoleTable
    	**type**\:  :py:class:`Stpxmstportroletable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstportroletable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxrstpporttable
    
    	A table containing port information for the RSTP  Protocol on all the bridge ports existing in the  system
    	**type**\:  :py:class:`Stpxrstpporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpporttable>`
    
    .. attribute:: stpxrstpportroletable
    
    	A table containing a list of the bridge ports for a  particular Spanning Tree instance.  This table is  only instantiated when the stpxSpanningTreeType is mst(4)  or rapidPvstPlus(5)
    	**type**\:  :py:class:`Stpxrstpportroletable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable>`
    
    .. attribute:: stpxrpvstporttable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance. This table is only instantiated when the object value of stpxSpanningTreeType is rapidPvstPlus(5)
    	**type**\:  :py:class:`Stpxrpvstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable>`
    
    .. attribute:: stpxsmstinstancetable
    
    	This table contains MST instance information for IEEE MST
    	**type**\:  :py:class:`Stpxsmstinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable>`
    
    .. attribute:: stpxsmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer.   This table is only instantiated when the object value of  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2)
    	**type**\:  :py:class:`Stpxsmstinstanceedittable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable>`
    
    .. attribute:: stpxsmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system.  This table is only instantiated when the object  value of stpxSpanningTreeType is mst(4)
    	**type**\:  :py:class:`Stpxsmstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstporttable>`
    
    

    """

    _prefix = 'CISCO-STP-EXTENSIONS-MIB'
    _revision = '2013-03-07'

    def __init__(self):
        super(CISCOSTPEXTENSIONSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-STP-EXTENSIONS-MIB"
        self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("stpxUplinkFastObjects", ("stpxuplinkfastobjects", CISCOSTPEXTENSIONSMIB.Stpxuplinkfastobjects)), ("stpxBackboneFastObjects", ("stpxbackbonefastobjects", CISCOSTPEXTENSIONSMIB.Stpxbackbonefastobjects)), ("stpxSpanningTreeObjects", ("stpxspanningtreeobjects", CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects)), ("stpxMISTPObjects", ("stpxmistpobjects", CISCOSTPEXTENSIONSMIB.Stpxmistpobjects)), ("stpxLoopGuardObjects", ("stpxloopguardobjects", CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects)), ("stpxFastStartObjects", ("stpxfaststartobjects", CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects)), ("stpxBpduSkewingObjects", ("stpxbpduskewingobjects", CISCOSTPEXTENSIONSMIB.Stpxbpduskewingobjects)), ("stpxMSTObjects", ("stpxmstobjects", CISCOSTPEXTENSIONSMIB.Stpxmstobjects)), ("stpxRSTPObjects", ("stpxrstpobjects", CISCOSTPEXTENSIONSMIB.Stpxrstpobjects)), ("stpxSMSTObjects", ("stpxsmstobjects", CISCOSTPEXTENSIONSMIB.Stpxsmstobjects)), ("stpxPVSTVlanTable", ("stpxpvstvlantable", CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable)), ("stpxInconsistencyTable", ("stpxinconsistencytable", CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable)), ("stpxRootGuardConfigTable", ("stpxrootguardconfigtable", CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable)), ("stpxRootInconsistencyTable", ("stpxrootinconsistencytable", CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable)), ("stpxMISTPInstanceTable", ("stpxmistpinstancetable", CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable)), ("stpxLoopGuardConfigTable", ("stpxloopguardconfigtable", CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable)), ("stpxLoopInconsistencyTable", ("stpxloopinconsistencytable", CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable)), ("stpxFastStartPortTable", ("stpxfaststartporttable", CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable)), ("stpxFastStartOperModeTable", ("stpxfaststartopermodetable", CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable)), ("stpxBpduSkewingTable", ("stpxbpduskewingtable", CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable)), ("stpxMSTInstanceTable", ("stpxmstinstancetable", CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable)), ("stpxMSTInstanceEditTable", ("stpxmstinstanceedittable", CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable)), ("stpxMSTPortTable", ("stpxmstporttable", CISCOSTPEXTENSIONSMIB.Stpxmstporttable)), ("stpxMSTPortRoleTable", ("stpxmstportroletable", CISCOSTPEXTENSIONSMIB.Stpxmstportroletable)), ("stpxRSTPPortTable", ("stpxrstpporttable", CISCOSTPEXTENSIONSMIB.Stpxrstpporttable)), ("stpxRSTPPortRoleTable", ("stpxrstpportroletable", CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable)), ("stpxRPVSTPortTable", ("stpxrpvstporttable", CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable)), ("stpxSMSTInstanceTable", ("stpxsmstinstancetable", CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable)), ("stpxSMSTInstanceEditTable", ("stpxsmstinstanceedittable", CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable)), ("stpxSMSTPortTable", ("stpxsmstporttable", CISCOSTPEXTENSIONSMIB.Stpxsmstporttable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.stpxuplinkfastobjects = CISCOSTPEXTENSIONSMIB.Stpxuplinkfastobjects()
        self.stpxuplinkfastobjects.parent = self
        self._children_name_map["stpxuplinkfastobjects"] = "stpxUplinkFastObjects"
        self._children_yang_names.add("stpxUplinkFastObjects")

        self.stpxbackbonefastobjects = CISCOSTPEXTENSIONSMIB.Stpxbackbonefastobjects()
        self.stpxbackbonefastobjects.parent = self
        self._children_name_map["stpxbackbonefastobjects"] = "stpxBackboneFastObjects"
        self._children_yang_names.add("stpxBackboneFastObjects")

        self.stpxspanningtreeobjects = CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects()
        self.stpxspanningtreeobjects.parent = self
        self._children_name_map["stpxspanningtreeobjects"] = "stpxSpanningTreeObjects"
        self._children_yang_names.add("stpxSpanningTreeObjects")

        self.stpxmistpobjects = CISCOSTPEXTENSIONSMIB.Stpxmistpobjects()
        self.stpxmistpobjects.parent = self
        self._children_name_map["stpxmistpobjects"] = "stpxMISTPObjects"
        self._children_yang_names.add("stpxMISTPObjects")

        self.stpxloopguardobjects = CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects()
        self.stpxloopguardobjects.parent = self
        self._children_name_map["stpxloopguardobjects"] = "stpxLoopGuardObjects"
        self._children_yang_names.add("stpxLoopGuardObjects")

        self.stpxfaststartobjects = CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects()
        self.stpxfaststartobjects.parent = self
        self._children_name_map["stpxfaststartobjects"] = "stpxFastStartObjects"
        self._children_yang_names.add("stpxFastStartObjects")

        self.stpxbpduskewingobjects = CISCOSTPEXTENSIONSMIB.Stpxbpduskewingobjects()
        self.stpxbpduskewingobjects.parent = self
        self._children_name_map["stpxbpduskewingobjects"] = "stpxBpduSkewingObjects"
        self._children_yang_names.add("stpxBpduSkewingObjects")

        self.stpxmstobjects = CISCOSTPEXTENSIONSMIB.Stpxmstobjects()
        self.stpxmstobjects.parent = self
        self._children_name_map["stpxmstobjects"] = "stpxMSTObjects"
        self._children_yang_names.add("stpxMSTObjects")

        self.stpxrstpobjects = CISCOSTPEXTENSIONSMIB.Stpxrstpobjects()
        self.stpxrstpobjects.parent = self
        self._children_name_map["stpxrstpobjects"] = "stpxRSTPObjects"
        self._children_yang_names.add("stpxRSTPObjects")

        self.stpxsmstobjects = CISCOSTPEXTENSIONSMIB.Stpxsmstobjects()
        self.stpxsmstobjects.parent = self
        self._children_name_map["stpxsmstobjects"] = "stpxSMSTObjects"
        self._children_yang_names.add("stpxSMSTObjects")

        self.stpxpvstvlantable = CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable()
        self.stpxpvstvlantable.parent = self
        self._children_name_map["stpxpvstvlantable"] = "stpxPVSTVlanTable"
        self._children_yang_names.add("stpxPVSTVlanTable")

        self.stpxinconsistencytable = CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable()
        self.stpxinconsistencytable.parent = self
        self._children_name_map["stpxinconsistencytable"] = "stpxInconsistencyTable"
        self._children_yang_names.add("stpxInconsistencyTable")

        self.stpxrootguardconfigtable = CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable()
        self.stpxrootguardconfigtable.parent = self
        self._children_name_map["stpxrootguardconfigtable"] = "stpxRootGuardConfigTable"
        self._children_yang_names.add("stpxRootGuardConfigTable")

        self.stpxrootinconsistencytable = CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable()
        self.stpxrootinconsistencytable.parent = self
        self._children_name_map["stpxrootinconsistencytable"] = "stpxRootInconsistencyTable"
        self._children_yang_names.add("stpxRootInconsistencyTable")

        self.stpxmistpinstancetable = CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable()
        self.stpxmistpinstancetable.parent = self
        self._children_name_map["stpxmistpinstancetable"] = "stpxMISTPInstanceTable"
        self._children_yang_names.add("stpxMISTPInstanceTable")

        self.stpxloopguardconfigtable = CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable()
        self.stpxloopguardconfigtable.parent = self
        self._children_name_map["stpxloopguardconfigtable"] = "stpxLoopGuardConfigTable"
        self._children_yang_names.add("stpxLoopGuardConfigTable")

        self.stpxloopinconsistencytable = CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable()
        self.stpxloopinconsistencytable.parent = self
        self._children_name_map["stpxloopinconsistencytable"] = "stpxLoopInconsistencyTable"
        self._children_yang_names.add("stpxLoopInconsistencyTable")

        self.stpxfaststartporttable = CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable()
        self.stpxfaststartporttable.parent = self
        self._children_name_map["stpxfaststartporttable"] = "stpxFastStartPortTable"
        self._children_yang_names.add("stpxFastStartPortTable")

        self.stpxfaststartopermodetable = CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable()
        self.stpxfaststartopermodetable.parent = self
        self._children_name_map["stpxfaststartopermodetable"] = "stpxFastStartOperModeTable"
        self._children_yang_names.add("stpxFastStartOperModeTable")

        self.stpxbpduskewingtable = CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable()
        self.stpxbpduskewingtable.parent = self
        self._children_name_map["stpxbpduskewingtable"] = "stpxBpduSkewingTable"
        self._children_yang_names.add("stpxBpduSkewingTable")

        self.stpxmstinstancetable = CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable()
        self.stpxmstinstancetable.parent = self
        self._children_name_map["stpxmstinstancetable"] = "stpxMSTInstanceTable"
        self._children_yang_names.add("stpxMSTInstanceTable")

        self.stpxmstinstanceedittable = CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable()
        self.stpxmstinstanceedittable.parent = self
        self._children_name_map["stpxmstinstanceedittable"] = "stpxMSTInstanceEditTable"
        self._children_yang_names.add("stpxMSTInstanceEditTable")

        self.stpxmstporttable = CISCOSTPEXTENSIONSMIB.Stpxmstporttable()
        self.stpxmstporttable.parent = self
        self._children_name_map["stpxmstporttable"] = "stpxMSTPortTable"
        self._children_yang_names.add("stpxMSTPortTable")

        self.stpxmstportroletable = CISCOSTPEXTENSIONSMIB.Stpxmstportroletable()
        self.stpxmstportroletable.parent = self
        self._children_name_map["stpxmstportroletable"] = "stpxMSTPortRoleTable"
        self._children_yang_names.add("stpxMSTPortRoleTable")

        self.stpxrstpporttable = CISCOSTPEXTENSIONSMIB.Stpxrstpporttable()
        self.stpxrstpporttable.parent = self
        self._children_name_map["stpxrstpporttable"] = "stpxRSTPPortTable"
        self._children_yang_names.add("stpxRSTPPortTable")

        self.stpxrstpportroletable = CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable()
        self.stpxrstpportroletable.parent = self
        self._children_name_map["stpxrstpportroletable"] = "stpxRSTPPortRoleTable"
        self._children_yang_names.add("stpxRSTPPortRoleTable")

        self.stpxrpvstporttable = CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable()
        self.stpxrpvstporttable.parent = self
        self._children_name_map["stpxrpvstporttable"] = "stpxRPVSTPortTable"
        self._children_yang_names.add("stpxRPVSTPortTable")

        self.stpxsmstinstancetable = CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable()
        self.stpxsmstinstancetable.parent = self
        self._children_name_map["stpxsmstinstancetable"] = "stpxSMSTInstanceTable"
        self._children_yang_names.add("stpxSMSTInstanceTable")

        self.stpxsmstinstanceedittable = CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable()
        self.stpxsmstinstanceedittable.parent = self
        self._children_name_map["stpxsmstinstanceedittable"] = "stpxSMSTInstanceEditTable"
        self._children_yang_names.add("stpxSMSTInstanceEditTable")

        self.stpxsmstporttable = CISCOSTPEXTENSIONSMIB.Stpxsmstporttable()
        self.stpxsmstporttable.parent = self
        self._children_name_map["stpxsmstporttable"] = "stpxSMSTPortTable"
        self._children_yang_names.add("stpxSMSTPortTable")
        self._segment_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB"


    class Stpxuplinkfastobjects(Entity):
        """
        
        
        .. attribute:: stpxuplinkfastenabled
        
        	An indication of whether the UplinkFast capability is administratively enabled on the device.  If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is  mst(4), then this object is not instantiated
        	**type**\: bool
        
        .. attribute:: stpxuplinkfasttransitions
        
        	The cumulative number of UplinkFast transitions (from the STP 'Blocking' state directly to the STP 'Forwarding' state).  All transitions are included in this counter, irrespective of the instance of the Spanning Tree  Protocol on which they occur.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: transitions
        
        .. attribute:: stpxuplinkstationlearninggenrate
        
        	The maximum number of station\-learning frames that this device will generate in each 100 milli\-second period after a UplinkFast transition.  By configuring this object, the network administrator can limit the rate at which station\-learning frames are generated.    If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is mst(4), then this object is not instantiated
        	**type**\: int
        
        	**range:** 0..32000
        
        	**units**\: frames
        
        .. attribute:: stpxuplinkstationlearningframes
        
        	The cumulative number of station\-learning frames generated due to UplinkFast transitions.  All generated station\-learning frames are included in this counter, irrespective of the instance of the Spanning Tree Protocol on which the UplinkFast transition occurred.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: frames
        
        .. attribute:: stpxuplinkfastoperenabled
        
        	An indication of whether the UplinkFast capability is  operationally enabled on the device
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxuplinkfastobjects, self).__init__()

            self.yang_name = "stpxUplinkFastObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxuplinkfastenabled', YLeaf(YType.boolean, 'stpxUplinkFastEnabled')),
                ('stpxuplinkfasttransitions', YLeaf(YType.uint32, 'stpxUplinkFastTransitions')),
                ('stpxuplinkstationlearninggenrate', YLeaf(YType.int32, 'stpxUplinkStationLearningGenRate')),
                ('stpxuplinkstationlearningframes', YLeaf(YType.uint32, 'stpxUplinkStationLearningFrames')),
                ('stpxuplinkfastoperenabled', YLeaf(YType.boolean, 'stpxUplinkFastOperEnabled')),
            ])
            self.stpxuplinkfastenabled = None
            self.stpxuplinkfasttransitions = None
            self.stpxuplinkstationlearninggenrate = None
            self.stpxuplinkstationlearningframes = None
            self.stpxuplinkfastoperenabled = None
            self._segment_path = lambda: "stpxUplinkFastObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxuplinkfastobjects, ['stpxuplinkfastenabled', 'stpxuplinkfasttransitions', 'stpxuplinkstationlearninggenrate', 'stpxuplinkstationlearningframes', 'stpxuplinkfastoperenabled'], name, value)


    class Stpxbackbonefastobjects(Entity):
        """
        
        
        .. attribute:: stpxbackbonefastenabled
        
        	An indication of whether the BackboneFast capability is administratively enabled on the device
        	**type**\: bool
        
        .. attribute:: stpxbackbonefastininferiorbpdus
        
        	The number of inferior BPDUs received by the switch  since the stpxBackboneFastOperEnabled has become true(1). If the value of  stpxBackboneFastOperEnabled is false(2), then this  mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastinrlqrequestpdus
        
        	The number of Root Link Query request PDUs received by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastinrlqresponsepdus
        
        	The number of Root Link Query response PDUs received by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoutrlqrequestpdus
        
        	The number of Root Link Query request PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoutrlqresponsepdus
        
        	The number of Root Link Query response PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoperenabled
        
        	An indication of whether the BackboneFast capability is operationally enabled on the device
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxbackbonefastobjects, self).__init__()

            self.yang_name = "stpxBackboneFastObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxbackbonefastenabled', YLeaf(YType.boolean, 'stpxBackboneFastEnabled')),
                ('stpxbackbonefastininferiorbpdus', YLeaf(YType.uint32, 'stpxBackboneFastInInferiorBPDUs')),
                ('stpxbackbonefastinrlqrequestpdus', YLeaf(YType.uint32, 'stpxBackboneFastInRLQRequestPDUs')),
                ('stpxbackbonefastinrlqresponsepdus', YLeaf(YType.uint32, 'stpxBackboneFastInRLQResponsePDUs')),
                ('stpxbackbonefastoutrlqrequestpdus', YLeaf(YType.uint32, 'stpxBackboneFastOutRLQRequestPDUs')),
                ('stpxbackbonefastoutrlqresponsepdus', YLeaf(YType.uint32, 'stpxBackboneFastOutRLQResponsePDUs')),
                ('stpxbackbonefastoperenabled', YLeaf(YType.boolean, 'stpxBackboneFastOperEnabled')),
            ])
            self.stpxbackbonefastenabled = None
            self.stpxbackbonefastininferiorbpdus = None
            self.stpxbackbonefastinrlqrequestpdus = None
            self.stpxbackbonefastinrlqresponsepdus = None
            self.stpxbackbonefastoutrlqrequestpdus = None
            self.stpxbackbonefastoutrlqresponsepdus = None
            self.stpxbackbonefastoperenabled = None
            self._segment_path = lambda: "stpxBackboneFastObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxbackbonefastobjects, ['stpxbackbonefastenabled', 'stpxbackbonefastininferiorbpdus', 'stpxbackbonefastinrlqrequestpdus', 'stpxbackbonefastinrlqresponsepdus', 'stpxbackbonefastoutrlqrequestpdus', 'stpxbackbonefastoutrlqresponsepdus', 'stpxbackbonefastoperenabled'], name, value)


    class Stpxspanningtreeobjects(Entity):
        """
        
        
        .. attribute:: stpxspanningtreetype
        
        	The actual mode of spanning tree protocol runs on the  device. It can be one of the following\:  pvstPlus \-\- PVST+ (Per VLAN Spanning Tree+ Protocol).  mistp \-\- MISTP (Multi Instance Spanning Tree Protocol).  mistpPvstPlus \-\-  MISTP with the tunneling scheme                      enabled for PVST+.  mst \-\- IEEE 802.1s Multiple Spanning Tree (MST)        with IEEE 802.1w Rapid Spanning Tree Protocol        (RSTP).  rapidPvstPlus \-\- IEEE 802.1w Rapid Spanning Tree          Protocol (RSTP) for all vlans in PVST+.  When the value of this MIB object gets changed, the  network connectivity would be affected and the  connectivity to this device would also be lost  temporarily
        	**type**\:  :py:class:`Stpxspanningtreetype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects.Stpxspanningtreetype>`
        
        .. attribute:: stpxspanningtreepathcostmode
        
        	Indicates the administrative  spanning tree path cost mode  configured on device
        	**type**\:  :py:class:`Stpxspanningtreepathcostmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects.Stpxspanningtreepathcostmode>`
        
        .. attribute:: stpxextendedsysidadminenabled
        
        	Indicates whether Extended System ID feature  is administratively enabled on the device or not
        	**type**\: bool
        
        .. attribute:: stpxextendedsysidoperenabled
        
        	Indicates whether Extended System ID feature  is operationaly enabled on the device or not.  If the value of this object is true(1), then the accepted values for dot1dStpPriority in BRIDGE\-MIB should be multiples of 4096 plus bridge instance ID, such as VlanIndex. Changing this object value might cause the values of dot1dBaseBridgeAddress and dot1dStpPriority in BRIDGE\-MIB to be changed also
        	**type**\: bool
        
        .. attribute:: stpxnotificationenable
        
        	Indicates whether a specified notification is enabled or not. If a bit corresponding to a notification is set to 1, then  the specified notification can be generated.  newRoot \-\- the newRoot notification as defined in BRIDGE\-MIB.  topologyChange \-\- the topologyChange notification as                   defined in BRIDGE\-MIB.  inconsistency \-\- the stpxInconsistencyUpdate notification.  rootInconsistency \-\- the stpxRootInconsistencyUpdate                       notification.  loopInconsistency \-\- the stpxLoopInconsistencyUpdate                       notification
        	**type**\:  :py:class:`Stpxnotificationenable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects.Stpxnotificationenable>`
        
        .. attribute:: stpxspanningtreepathcostopermode
        
        	Indicate the operational spanning tree path cost mode on device. This mode applies to all instances of the Spanning Tree protocol running on the device.   When the value of this MIB object gets changed, the path cost of all ports will be reassigned to the default path cost values based on the new spanning tree path cost mode and the ports' speed.  When the value of this MIB object is long(2), the stpxLongStpPortPathCost MIB object must be used in order to retrieve/configure the spanning tree port path cost as a 32 bits value. The set operation on dot1dStpPortPathCost in BRIDGE\-MIB will be rejected. While retrieving the value of dot1dStpPortPathCost, the maximum value of 65535 will be returned if the value of stpxLongStpPortPathCost for the same instance exceeds 65535.  When the value of this MIB object is short(1), the dot1dStpPortPathCost in BRIDGE\-MIB must be used
        	**type**\:  :py:class:`Stpxspanningtreepathcostopermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects.Stpxspanningtreepathcostopermode>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects, self).__init__()

            self.yang_name = "stpxSpanningTreeObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxspanningtreetype', YLeaf(YType.enumeration, 'stpxSpanningTreeType')),
                ('stpxspanningtreepathcostmode', YLeaf(YType.enumeration, 'stpxSpanningTreePathCostMode')),
                ('stpxextendedsysidadminenabled', YLeaf(YType.boolean, 'stpxExtendedSysIDAdminEnabled')),
                ('stpxextendedsysidoperenabled', YLeaf(YType.boolean, 'stpxExtendedSysIDOperEnabled')),
                ('stpxnotificationenable', YLeaf(YType.bits, 'stpxNotificationEnable')),
                ('stpxspanningtreepathcostopermode', YLeaf(YType.enumeration, 'stpxSpanningTreePathCostOperMode')),
            ])
            self.stpxspanningtreetype = None
            self.stpxspanningtreepathcostmode = None
            self.stpxextendedsysidadminenabled = None
            self.stpxextendedsysidoperenabled = None
            self.stpxnotificationenable = Bits()
            self.stpxspanningtreepathcostopermode = None
            self._segment_path = lambda: "stpxSpanningTreeObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxspanningtreeobjects, ['stpxspanningtreetype', 'stpxspanningtreepathcostmode', 'stpxextendedsysidadminenabled', 'stpxextendedsysidoperenabled', 'stpxnotificationenable', 'stpxspanningtreepathcostopermode'], name, value)

        class Stpxspanningtreepathcostmode(Enum):
            """
            Stpxspanningtreepathcostmode (Enum Class)

            Indicates the administrative  spanning tree path cost mode 

            configured on device.

            .. data:: short = 1

            .. data:: long = 2

            """

            short = Enum.YLeaf(1, "short")

            long = Enum.YLeaf(2, "long")


        class Stpxspanningtreepathcostopermode(Enum):
            """
            Stpxspanningtreepathcostopermode (Enum Class)

            Indicate the operational spanning tree path cost mode

            on device. This mode applies to all instances of the Spanning

            Tree protocol running on the device. 

            When the value of this MIB object gets changed, the path cost

            of all ports will be reassigned to the default path cost

            values based on the new spanning tree path cost mode and the

            ports' speed.

            When the value of this MIB object is long(2),

            the stpxLongStpPortPathCost MIB object must be used in order

            to retrieve/configure the spanning tree port path cost as a

            32 bits value. The set operation on dot1dStpPortPathCost in

            BRIDGE\-MIB will be rejected. While retrieving the value of

            dot1dStpPortPathCost, the maximum value of 65535 will be

            returned if the value of stpxLongStpPortPathCost for the same

            instance exceeds 65535.

            When the value of this MIB object is short(1),

            the dot1dStpPortPathCost in BRIDGE\-MIB must be used.

            .. data:: short = 1

            .. data:: long = 2

            """

            short = Enum.YLeaf(1, "short")

            long = Enum.YLeaf(2, "long")


        class Stpxspanningtreetype(Enum):
            """
            Stpxspanningtreetype (Enum Class)

            The actual mode of spanning tree protocol runs

            on the  device. It can be one of the following\:

            pvstPlus \-\- PVST+ (Per VLAN Spanning Tree+ Protocol).

            mistp \-\- MISTP (Multi Instance Spanning Tree Protocol).

            mistpPvstPlus \-\-  MISTP with the tunneling scheme

                                 enabled for PVST+.

            mst \-\- IEEE 802.1s Multiple Spanning Tree (MST)

                   with IEEE 802.1w Rapid Spanning Tree Protocol

                   (RSTP).

            rapidPvstPlus \-\- IEEE 802.1w Rapid Spanning Tree 

                    Protocol (RSTP) for all vlans in PVST+.

            When the value of this MIB object gets changed, the 

            network connectivity would be affected and the 

            connectivity to this device would also be lost 

            temporarily.

            .. data:: pvstPlus = 1

            .. data:: mistp = 2

            .. data:: mistpPvstPlus = 3

            .. data:: mst = 4

            .. data:: rapidPvstPlus = 5

            """

            pvstPlus = Enum.YLeaf(1, "pvstPlus")

            mistp = Enum.YLeaf(2, "mistp")

            mistpPvstPlus = Enum.YLeaf(3, "mistpPvstPlus")

            mst = Enum.YLeaf(4, "mst")

            rapidPvstPlus = Enum.YLeaf(5, "rapidPvstPlus")



    class Stpxmistpobjects(Entity):
        """
        
        
        .. attribute:: stpxmistpinstancenumber
        
        	The number of MISTP instances, that are supported by the device  when the value of stpxSpanningTreeType is either mistp(2) or mistpPvstPlus(3)
        	**type**\: int
        
        	**range:** 1..256
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmistpobjects, self).__init__()

            self.yang_name = "stpxMISTPObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxmistpinstancenumber', YLeaf(YType.int32, 'stpxMISTPInstanceNumber')),
            ])
            self.stpxmistpinstancenumber = None
            self._segment_path = lambda: "stpxMISTPObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmistpobjects, ['stpxmistpinstancenumber'], name, value)


    class Stpxloopguardobjects(Entity):
        """
        
        
        .. attribute:: stpxloopguardglobaldefaultmode
        
        	Indicates the global default config mode of LoopGuard  feature on the device
        	**type**\:  :py:class:`Stpxloopguardglobaldefaultmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects.Stpxloopguardglobaldefaultmode>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects, self).__init__()

            self.yang_name = "stpxLoopGuardObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxloopguardglobaldefaultmode', YLeaf(YType.enumeration, 'stpxLoopGuardGlobalDefaultMode')),
            ])
            self.stpxloopguardglobaldefaultmode = None
            self._segment_path = lambda: "stpxLoopGuardObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxloopguardobjects, ['stpxloopguardglobaldefaultmode'], name, value)

        class Stpxloopguardglobaldefaultmode(Enum):
            """
            Stpxloopguardglobaldefaultmode (Enum Class)

            Indicates the global default config mode of LoopGuard 

            feature on the device.

            .. data:: enable = 1

            .. data:: disable = 2

            """

            enable = Enum.YLeaf(1, "enable")

            disable = Enum.YLeaf(2, "disable")



    class Stpxfaststartobjects(Entity):
        """
        
        
        .. attribute:: stpxfaststartbpduguardenable
        
        	Indicates the global default mode of the Bpdu Guard feature on the device.  On platforms that does not support per port  Bpdu Guard configuration as indicated by the object stpxFastStartPortBpduGuardMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then that port will be  immediately disabled when the system receives a BPDU from that port
        	**type**\: bool
        
        .. attribute:: stpxfaststartbpdufilterenable
        
        	Indicates the global default mode of the Bpdu  Filter feature on the device.  On platforms that does not support per port  Bpdu Filter configuration as indicated by the object stpxFastStartPortBpduFilterMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then no BPDUs will be  transmitted on this port
        	**type**\: bool
        
        .. attribute:: stpxfaststartglobaldefaultmode
        
        	Indicates the global default mode of the Fast  Start feature on the device
        	**type**\:  :py:class:`Stpxfaststartglobaldefaultmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects.Stpxfaststartglobaldefaultmode>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects, self).__init__()

            self.yang_name = "stpxFastStartObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxfaststartbpduguardenable', YLeaf(YType.boolean, 'stpxFastStartBpduGuardEnable')),
                ('stpxfaststartbpdufilterenable', YLeaf(YType.boolean, 'stpxFastStartBpduFilterEnable')),
                ('stpxfaststartglobaldefaultmode', YLeaf(YType.enumeration, 'stpxFastStartGlobalDefaultMode')),
            ])
            self.stpxfaststartbpduguardenable = None
            self.stpxfaststartbpdufilterenable = None
            self.stpxfaststartglobaldefaultmode = None
            self._segment_path = lambda: "stpxFastStartObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxfaststartobjects, ['stpxfaststartbpduguardenable', 'stpxfaststartbpdufilterenable', 'stpxfaststartglobaldefaultmode'], name, value)

        class Stpxfaststartglobaldefaultmode(Enum):
            """
            Stpxfaststartglobaldefaultmode (Enum Class)

            Indicates the global default mode of the Fast 

            Start feature on the device.

            .. data:: enable = 1

            .. data:: disable = 2

            """

            enable = Enum.YLeaf(1, "enable")

            disable = Enum.YLeaf(2, "disable")



    class Stpxbpduskewingobjects(Entity):
        """
        
        
        .. attribute:: stpxbpduskewingdetectionenable
        
        	Indicates whether BPDU skewing detection feature is enabled or not on the system. If this object has the value of true(1), then the system will detect whether BPDUs received by any port on any Spanning  Tree instance are processed at an interval longer than the object value of dot1dStpHelloTime in the BIRDGE\-MIB of the Spanning Tree instance
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingobjects, self).__init__()

            self.yang_name = "stpxBpduSkewingObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxbpduskewingdetectionenable', YLeaf(YType.boolean, 'stpxBpduSkewingDetectionEnable')),
            ])
            self.stpxbpduskewingdetectionenable = None
            self._segment_path = lambda: "stpxBpduSkewingObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingobjects, ['stpxbpduskewingdetectionenable'], name, value)


    class Stpxmstobjects(Entity):
        """
        
        
        .. attribute:: stpxmstmaxinstancenumber
        
        	The maximum MST (Multiple Spanning Tree) instance id,  that can be supported by the device for Cisco proprietary implementation of the MST Protocol.  This object is deprecated and replaced by  stpxSMSTMaxInstanceID
        	**type**\: int
        
        	**range:** 1..256
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstregionname
        
        	The operational MST region name
        	**type**\: str
        
        	**length:** 0..32
        
        .. attribute:: stpxmstregionrevision
        
        	The operational MST region version.  This object is deprecated and replaced by  stpxSMSTRegionRevision
        	**type**\: int
        
        	**range:** 0..65535
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstregioneditbufferstatus
        
        	Indicates the current ownership status of the unique  Region Config Edit Buffer.   released \-\- the Edit Buffer can be acquired by any of              the SNMP management stations.   acquiredBySnmp \-\- the Edit Buffer is acquired by             any of the SNMP management stations.   acquiredByNonSnmp \-\- the Edit Buffer is acquired by the              non\-SNMP users managing the device
        	**type**\:  :py:class:`Stpxmstregioneditbufferstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstobjects.Stpxmstregioneditbufferstatus>`
        
        .. attribute:: stpxmstregioneditbufferoperation
        
        	Indicates the operation that is performed on the Region  Config Edit Buffer.  other \-\-   none of the following operations.    acquire \-\- acquire the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value of            released(1). After the successful operation of             this action, the stpxMSTRegionEditBufferStatus            will be changed to acquiredBySnmp(2).               releaseWithForce \-\- release the Edit Buffer acquired by            non\-SNMP users with force and discard the changes            in the Edit Buffer. This operation can only be             performed when the object             stpxMSTRegionEditBufferStatus has the value of             acquiredByNonSnmp(2).  commit \-\-  commit the changes in the Edit Buffer            and release the Edit Buffer. The successful             operation of this action will make the changes            in the Edit Buffer effective on the device.            This operation can only be performed when the             object stpxMSTRegionEditBufferStatus has the             value of acquiredBySnmp(3).   rollBack \-\- discard the changes in the Edit Buffer            and release the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value             of acquiredBySnmp(3).  This object always returns other(1) when it is read
        	**type**\:  :py:class:`Stpxmstregioneditbufferoperation <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstobjects.Stpxmstregioneditbufferoperation>`
        
        .. attribute:: stpxmstregioneditname
        
        	The MST region name in the Edit Buffer.   This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\: str
        
        	**length:** 0..32
        
        .. attribute:: stpxmstregioneditrevision
        
        	The MST region version in the Edit Buffer. This object is only instantiated when the stpxMSTRegionEditBufferStatus  has the value of acquiredBySnmp(2).  This object is deprecated and replaced by stpxSMSTRegionEditRevision
        	**type**\: int
        
        	**range:** 1..65535
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstmaxhopcount
        
        	The maximum number of hops for the MST region.   This object will take on value of 40 if the object value of stpxSMSTMaxHopCount is greater than 40.  This object is deprecated and replaced by stpxSMSTMaxHopCount
        	**type**\: int
        
        	**range:** 1..40
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmstobjects, self).__init__()

            self.yang_name = "stpxMSTObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxmstmaxinstancenumber', YLeaf(YType.int32, 'stpxMSTMaxInstanceNumber')),
                ('stpxmstregionname', YLeaf(YType.str, 'stpxMSTRegionName')),
                ('stpxmstregionrevision', YLeaf(YType.int32, 'stpxMSTRegionRevision')),
                ('stpxmstregioneditbufferstatus', YLeaf(YType.enumeration, 'stpxMSTRegionEditBufferStatus')),
                ('stpxmstregioneditbufferoperation', YLeaf(YType.enumeration, 'stpxMSTRegionEditBufferOperation')),
                ('stpxmstregioneditname', YLeaf(YType.str, 'stpxMSTRegionEditName')),
                ('stpxmstregioneditrevision', YLeaf(YType.int32, 'stpxMSTRegionEditRevision')),
                ('stpxmstmaxhopcount', YLeaf(YType.int32, 'stpxMSTMaxHopCount')),
            ])
            self.stpxmstmaxinstancenumber = None
            self.stpxmstregionname = None
            self.stpxmstregionrevision = None
            self.stpxmstregioneditbufferstatus = None
            self.stpxmstregioneditbufferoperation = None
            self.stpxmstregioneditname = None
            self.stpxmstregioneditrevision = None
            self.stpxmstmaxhopcount = None
            self._segment_path = lambda: "stpxMSTObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstobjects, ['stpxmstmaxinstancenumber', 'stpxmstregionname', 'stpxmstregionrevision', 'stpxmstregioneditbufferstatus', 'stpxmstregioneditbufferoperation', 'stpxmstregioneditname', 'stpxmstregioneditrevision', 'stpxmstmaxhopcount'], name, value)

        class Stpxmstregioneditbufferoperation(Enum):
            """
            Stpxmstregioneditbufferoperation (Enum Class)

            Indicates the operation that is performed on the Region 

            Config Edit Buffer.

            other \-\-   none of the following operations.  

            acquire \-\- acquire the Edit Buffer. This operation can 

                       only be performed when the object 

                       stpxMSTRegionEditBufferStatus has the value of

                       released(1). After the successful operation of 

                       this action, the stpxMSTRegionEditBufferStatus

                       will be changed to acquiredBySnmp(2). 

            releaseWithForce \-\- release the Edit Buffer acquired by

                       non\-SNMP users with force and discard the changes

                       in the Edit Buffer. This operation can only be 

                       performed when the object 

                       stpxMSTRegionEditBufferStatus has the value of 

                       acquiredByNonSnmp(2).

            commit \-\-  commit the changes in the Edit Buffer

                       and release the Edit Buffer. The successful 

                       operation of this action will make the changes

                       in the Edit Buffer effective on the device.

                       This operation can only be performed when the 

                       object stpxMSTRegionEditBufferStatus has the 

                       value of acquiredBySnmp(3).

            rollBack \-\- discard the changes in the Edit Buffer

                       and release the Edit Buffer. This operation can 

                       only be performed when the object 

                       stpxMSTRegionEditBufferStatus has the value 

                       of acquiredBySnmp(3).

            This object always returns other(1) when it is read.

            .. data:: other = 1

            .. data:: acquire = 2

            .. data:: releaseWithForce = 3

            .. data:: commit = 4

            .. data:: rollBack = 5

            """

            other = Enum.YLeaf(1, "other")

            acquire = Enum.YLeaf(2, "acquire")

            releaseWithForce = Enum.YLeaf(3, "releaseWithForce")

            commit = Enum.YLeaf(4, "commit")

            rollBack = Enum.YLeaf(5, "rollBack")


        class Stpxmstregioneditbufferstatus(Enum):
            """
            Stpxmstregioneditbufferstatus (Enum Class)

            Indicates the current ownership status of the unique 

            Region Config Edit Buffer. 

            released \-\- the Edit Buffer can be acquired by any of 

                        the SNMP management stations. 

            acquiredBySnmp \-\- the Edit Buffer is acquired by

                        any of the SNMP management stations. 

            acquiredByNonSnmp \-\- the Edit Buffer is acquired by the 

                        non\-SNMP users managing the device.

            .. data:: released = 1

            .. data:: acquiredBySnmp = 2

            .. data:: acquiredByNonSnmp = 3

            """

            released = Enum.YLeaf(1, "released")

            acquiredBySnmp = Enum.YLeaf(2, "acquiredBySnmp")

            acquiredByNonSnmp = Enum.YLeaf(3, "acquiredByNonSnmp")



    class Stpxrstpobjects(Entity):
        """
        
        
        .. attribute:: stpxrstptransmitholdcount
        
        	The Transmit Hold Count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrstpobjects, self).__init__()

            self.yang_name = "stpxRSTPObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxrstptransmitholdcount', YLeaf(YType.uint32, 'stpxRSTPTransmitHoldCount')),
            ])
            self.stpxrstptransmitholdcount = None
            self._segment_path = lambda: "stpxRSTPObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrstpobjects, ['stpxrstptransmitholdcount'], name, value)


    class Stpxsmstobjects(Entity):
        """
        
        
        .. attribute:: stpxsmstmaxinstances
        
        	The maximum number of MST instances that can be  supported by the device for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxinstanceid
        
        	The maximum MST instance ID that can be supported  by the device for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregionrevision
        
        	The operational region version for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregioneditrevision
        
        	The MST region version in the Edit Buffer for IEEE  MST.  This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxhopcount
        
        	The maximum number of hops for the IEEE MST region
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstconfigdigest
        
        	The IEEE MST region configuration digest
        	**type**\: str
        
        .. attribute:: stpxsmstconfigprestandarddigest
        
        	The pre\-standard MST region configuration digest
        	**type**\: str
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxsmstobjects, self).__init__()

            self.yang_name = "stpxSMSTObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stpxsmstmaxinstances', YLeaf(YType.uint32, 'stpxSMSTMaxInstances')),
                ('stpxsmstmaxinstanceid', YLeaf(YType.uint32, 'stpxSMSTMaxInstanceID')),
                ('stpxsmstregionrevision', YLeaf(YType.uint32, 'stpxSMSTRegionRevision')),
                ('stpxsmstregioneditrevision', YLeaf(YType.uint32, 'stpxSMSTRegionEditRevision')),
                ('stpxsmstmaxhopcount', YLeaf(YType.uint32, 'stpxSMSTMaxHopCount')),
                ('stpxsmstconfigdigest', YLeaf(YType.str, 'stpxSMSTConfigDigest')),
                ('stpxsmstconfigprestandarddigest', YLeaf(YType.str, 'stpxSMSTConfigPreStandardDigest')),
            ])
            self.stpxsmstmaxinstances = None
            self.stpxsmstmaxinstanceid = None
            self.stpxsmstregionrevision = None
            self.stpxsmstregioneditrevision = None
            self.stpxsmstmaxhopcount = None
            self.stpxsmstconfigdigest = None
            self.stpxsmstconfigprestandarddigest = None
            self._segment_path = lambda: "stpxSMSTObjects"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstobjects, ['stpxsmstmaxinstances', 'stpxsmstmaxinstanceid', 'stpxsmstregionrevision', 'stpxsmstregioneditrevision', 'stpxsmstmaxhopcount', 'stpxsmstconfigdigest', 'stpxsmstconfigprestandarddigest'], name, value)


    class Stpxpvstvlantable(Entity):
        """
        A list of Virtual LAN entries containing
        information for Spanning Tree PVST+ protocol. 
        An entry will exist for each VLAN existing on 
        the device.
        
        .. attribute:: stpxpvstvlanentry
        
        	An entry containing Spanning Tree PVST+ Protocol  information for a particular Virtual LAN
        	**type**\: list of  		 :py:class:`Stpxpvstvlanentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable.Stpxpvstvlanentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable, self).__init__()

            self.yang_name = "stpxPVSTVlanTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxPVSTVlanEntry", ("stpxpvstvlanentry", CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable.Stpxpvstvlanentry))])
            self._leafs = OrderedDict()

            self.stpxpvstvlanentry = YList(self)
            self._segment_path = lambda: "stpxPVSTVlanTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable, [], name, value)


        class Stpxpvstvlanentry(Entity):
            """
            An entry containing Spanning Tree PVST+ Protocol 
            information for a particular Virtual LAN.
            
            .. attribute:: stpxpvstvlanindex  (key)
            
            	An index value that uniquely identifies the Virtual LAN associated with this information
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxpvstvlanenable
            
            	Indicates whether Spanning Tree PVST+   Protocol is enabled for this Virtual LAN. If  Spanning Tree PVST+ Protocol is not supported  on this VLAN, then notApplicable(3) will be  returned while retrieving the object value for  this VLAN.  If the device only supports a single global Spanning Tree PVST+ Protocol enable/disable  for all the existing VLANs, then the object  value assigned to this VLAN will be applied to the object values of all the instances in this table which do not have the value of notApplicable(3).  If the value of stpxSpanningTreeType is neither  pvstPlus(1) nor rapidPvstPlus(5), then the value  of stpxPVSTVlanEnable for this VLAN can not be  changed
            	**type**\:  :py:class:`Stpxpvstvlanenable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable.Stpxpvstvlanentry.Stpxpvstvlanenable>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable.Stpxpvstvlanentry, self).__init__()

                self.yang_name = "stpxPVSTVlanEntry"
                self.yang_parent_name = "stpxPVSTVlanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxpvstvlanindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxpvstvlanindex', YLeaf(YType.int32, 'stpxPVSTVlanIndex')),
                    ('stpxpvstvlanenable', YLeaf(YType.enumeration, 'stpxPVSTVlanEnable')),
                ])
                self.stpxpvstvlanindex = None
                self.stpxpvstvlanenable = None
                self._segment_path = lambda: "stpxPVSTVlanEntry" + "[stpxPVSTVlanIndex='" + str(self.stpxpvstvlanindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxPVSTVlanTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxpvstvlantable.Stpxpvstvlanentry, ['stpxpvstvlanindex', 'stpxpvstvlanenable'], name, value)

            class Stpxpvstvlanenable(Enum):
                """
                Stpxpvstvlanenable (Enum Class)

                Indicates whether Spanning Tree PVST+  

                Protocol is enabled for this Virtual LAN. If 

                Spanning Tree PVST+ Protocol is not supported 

                on this VLAN, then notApplicable(3) will be 

                returned while retrieving the object value for 

                this VLAN.

                If the device only supports a single global

                Spanning Tree PVST+ Protocol enable/disable 

                for all the existing VLANs, then the object 

                value assigned to this VLAN will be applied

                to the object values of all the instances

                in this table which do not have the value

                of notApplicable(3).

                If the value of stpxSpanningTreeType is neither 

                pvstPlus(1) nor rapidPvstPlus(5), then the value 

                of stpxPVSTVlanEnable for this VLAN can not be 

                changed.

                .. data:: enabled = 1

                .. data:: disabled = 2

                .. data:: notApplicable = 3

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")

                notApplicable = Enum.YLeaf(3, "notApplicable")



    class Stpxinconsistencytable(Entity):
        """
        A table containing a list of the ports for which
        a particular VLAN's Spanning Tree has been found to
        have an inconsistency.  Two types of inconsistency
        are discovered\: 1) an inconsistency where two different
        port types have been plugged together; and 2) an
        inconsistency where different switches have different
        PVIDs for the same link.
        
        .. attribute:: stpxinconsistencyentry
        
        	A VLAN on a particular port for which a Spanning Tree inconsistency is currently in effect
        	**type**\: list of  		 :py:class:`Stpxinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable.Stpxinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable, self).__init__()

            self.yang_name = "stpxInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxInconsistencyEntry", ("stpxinconsistencyentry", CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable.Stpxinconsistencyentry))])
            self._leafs = OrderedDict()

            self.stpxinconsistencyentry = YList(self)
            self._segment_path = lambda: "stpxInconsistencyTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable, [], name, value)


        class Stpxinconsistencyentry(Entity):
            """
            A VLAN on a particular port for which a Spanning Tree
            inconsistency is currently in effect.
            
            .. attribute:: stpxvlanindex  (key)
            
            	The VLAN id of the VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxinconsistentstate
            
            	The types of inconsistency which have been discovered on this port for this VLAN's Spanning Tree.  When this object exists, the value of the corresponding instance of the Bridge MIB's dot1dStpPortState object will be 'broken(6)'
            	**type**\:  :py:class:`Stpxinconsistentstate <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable.Stpxinconsistencyentry.Stpxinconsistentstate>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable.Stpxinconsistencyentry, self).__init__()

                self.yang_name = "stpxInconsistencyEntry"
                self.yang_parent_name = "stpxInconsistencyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxvlanindex','stpxportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxvlanindex', YLeaf(YType.int32, 'stpxVlanIndex')),
                    ('stpxportindex', YLeaf(YType.int32, 'stpxPortIndex')),
                    ('stpxinconsistentstate', YLeaf(YType.bits, 'stpxInconsistentState')),
                ])
                self.stpxvlanindex = None
                self.stpxportindex = None
                self.stpxinconsistentstate = Bits()
                self._segment_path = lambda: "stpxInconsistencyEntry" + "[stpxVlanIndex='" + str(self.stpxvlanindex) + "']" + "[stpxPortIndex='" + str(self.stpxportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxInconsistencyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxinconsistencytable.Stpxinconsistencyentry, ['stpxvlanindex', 'stpxportindex', 'stpxinconsistentstate'], name, value)


    class Stpxrootguardconfigtable(Entity):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree RootGuard capability can be configured.
        
        .. attribute:: stpxrootguardconfigentry
        
        	A bridge port for which Spanning Tree RootGuard capability can be configured
        	**type**\: list of  		 :py:class:`Stpxrootguardconfigentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable.Stpxrootguardconfigentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable, self).__init__()

            self.yang_name = "stpxRootGuardConfigTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxRootGuardConfigEntry", ("stpxrootguardconfigentry", CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable.Stpxrootguardconfigentry))])
            self._leafs = OrderedDict()

            self.stpxrootguardconfigentry = YList(self)
            self._segment_path = lambda: "stpxRootGuardConfigTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable, [], name, value)


        class Stpxrootguardconfigentry(Entity):
            """
            A bridge port for which Spanning Tree RootGuard
            capability can be configured.
            
            .. attribute:: stpxrootguardconfigportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootguardconfigenabled
            
            	An indication of whether the RootGuard capability is  enabled on this port or not. This configuration will be applied to all Spanning Tree instances in which this port  exists
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable.Stpxrootguardconfigentry, self).__init__()

                self.yang_name = "stpxRootGuardConfigEntry"
                self.yang_parent_name = "stpxRootGuardConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxrootguardconfigportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxrootguardconfigportindex', YLeaf(YType.int32, 'stpxRootGuardConfigPortIndex')),
                    ('stpxrootguardconfigenabled', YLeaf(YType.boolean, 'stpxRootGuardConfigEnabled')),
                ])
                self.stpxrootguardconfigportindex = None
                self.stpxrootguardconfigenabled = None
                self._segment_path = lambda: "stpxRootGuardConfigEntry" + "[stpxRootGuardConfigPortIndex='" + str(self.stpxrootguardconfigportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRootGuardConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrootguardconfigtable.Stpxrootguardconfigentry, ['stpxrootguardconfigportindex', 'stpxrootguardconfigenabled'], name, value)


    class Stpxrootinconsistencytable(Entity):
        """
        A table containing a list of the bridge ports for which
        a particular Spanning Tree instance has been found 
        to have an root\-inconsistency. The agent creates a new 
        entry in this table whenever it detects a new 
        root\-inconsistency, and deletes entries 
        when/soon after the inconsistency is no longer present.
        
        .. attribute:: stpxrootinconsistencyentry
        
        	A Spanning Tree instance on a particular port for  which a Spanning Tree root\-inconsistency is currently  in effect
        	**type**\: list of  		 :py:class:`Stpxrootinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable.Stpxrootinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable, self).__init__()

            self.yang_name = "stpxRootInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxRootInconsistencyEntry", ("stpxrootinconsistencyentry", CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable.Stpxrootinconsistencyentry))])
            self._leafs = OrderedDict()

            self.stpxrootinconsistencyentry = YList(self)
            self._segment_path = lambda: "stpxRootInconsistencyTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable, [], name, value)


        class Stpxrootinconsistencyentry(Entity):
            """
            A Spanning Tree instance on a particular port for 
            which a Spanning Tree root\-inconsistency is currently 
            in effect.
            
            .. attribute:: stpxrootinconsistencyindex  (key)
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxrootinconsistencyportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in root\-inconsistent  state or not
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable.Stpxrootinconsistencyentry, self).__init__()

                self.yang_name = "stpxRootInconsistencyEntry"
                self.yang_parent_name = "stpxRootInconsistencyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxrootinconsistencyindex','stpxrootinconsistencyportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxrootinconsistencyindex', YLeaf(YType.int32, 'stpxRootInconsistencyIndex')),
                    ('stpxrootinconsistencyportindex', YLeaf(YType.int32, 'stpxRootInconsistencyPortIndex')),
                    ('stpxrootinconsistencystate', YLeaf(YType.boolean, 'stpxRootInconsistencyState')),
                ])
                self.stpxrootinconsistencyindex = None
                self.stpxrootinconsistencyportindex = None
                self.stpxrootinconsistencystate = None
                self._segment_path = lambda: "stpxRootInconsistencyEntry" + "[stpxRootInconsistencyIndex='" + str(self.stpxrootinconsistencyindex) + "']" + "[stpxRootInconsistencyPortIndex='" + str(self.stpxrootinconsistencyportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRootInconsistencyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrootinconsistencytable.Stpxrootinconsistencyentry, ['stpxrootinconsistencyindex', 'stpxrootinconsistencyportindex', 'stpxrootinconsistencystate'], name, value)


    class Stpxmistpinstancetable(Entity):
        """
        This table contains one entry for each instance of MISTP and 
        it contains stpxMISTPInstanceNumber entries, numbered from 1
        to stpxMISTPInstanceNumber.
        
        This table is only instantiated when the value of 
        stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3).
        
        .. attribute:: stpxmistpinstanceentry
        
        	A conceptual row containing the status of the MISTP  instance
        	**type**\: list of  		 :py:class:`Stpxmistpinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable.Stpxmistpinstanceentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable, self).__init__()

            self.yang_name = "stpxMISTPInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxMISTPInstanceEntry", ("stpxmistpinstanceentry", CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable.Stpxmistpinstanceentry))])
            self._leafs = OrderedDict()

            self.stpxmistpinstanceentry = YList(self)
            self._segment_path = lambda: "stpxMISTPInstanceTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable, [], name, value)


        class Stpxmistpinstanceentry(Entity):
            """
            A conceptual row containing the status of the MISTP 
            instance.
            
            .. attribute:: stpxmistpinstanceindex  (key)
            
            	An arbitrary integer within the range from 1 to the value of stpxMISTPInstanceNumber that uniquely identifies an instance
            	**type**\: int
            
            	**range:** 1..256
            
            .. attribute:: stpxmistpinstanceenable
            
            	This object indicates whether the MISTP protocol is currently enabled on the MISTP instance.  If this object is set to    'true'    \- the MISTP protocol will run on this instance.                   'false'   \- the MISTP protocol will stop running on this                 instance
            	**type**\: bool
            
            .. attribute:: stpxmistpinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable.Stpxmistpinstanceentry, self).__init__()

                self.yang_name = "stpxMISTPInstanceEntry"
                self.yang_parent_name = "stpxMISTPInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxmistpinstanceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxmistpinstanceindex', YLeaf(YType.int32, 'stpxMISTPInstanceIndex')),
                    ('stpxmistpinstanceenable', YLeaf(YType.boolean, 'stpxMISTPInstanceEnable')),
                    ('stpxmistpinstancevlansmapped', YLeaf(YType.str, 'stpxMISTPInstanceVlansMapped')),
                    ('stpxmistpinstancevlansmapped2k', YLeaf(YType.str, 'stpxMISTPInstanceVlansMapped2k')),
                    ('stpxmistpinstancevlansmapped3k', YLeaf(YType.str, 'stpxMISTPInstanceVlansMapped3k')),
                    ('stpxmistpinstancevlansmapped4k', YLeaf(YType.str, 'stpxMISTPInstanceVlansMapped4k')),
                ])
                self.stpxmistpinstanceindex = None
                self.stpxmistpinstanceenable = None
                self.stpxmistpinstancevlansmapped = None
                self.stpxmistpinstancevlansmapped2k = None
                self.stpxmistpinstancevlansmapped3k = None
                self.stpxmistpinstancevlansmapped4k = None
                self._segment_path = lambda: "stpxMISTPInstanceEntry" + "[stpxMISTPInstanceIndex='" + str(self.stpxmistpinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMISTPInstanceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmistpinstancetable.Stpxmistpinstanceentry, ['stpxmistpinstanceindex', 'stpxmistpinstanceenable', 'stpxmistpinstancevlansmapped', 'stpxmistpinstancevlansmapped2k', 'stpxmistpinstancevlansmapped3k', 'stpxmistpinstancevlansmapped4k'], name, value)


    class Stpxloopguardconfigtable(Entity):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree LoopGuard capability can be configured.
        
        .. attribute:: stpxloopguardconfigentry
        
        	A bridge port for which Spanning Tree LoopGuard  capability can be configured
        	**type**\: list of  		 :py:class:`Stpxloopguardconfigentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable.Stpxloopguardconfigentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable, self).__init__()

            self.yang_name = "stpxLoopGuardConfigTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxLoopGuardConfigEntry", ("stpxloopguardconfigentry", CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable.Stpxloopguardconfigentry))])
            self._leafs = OrderedDict()

            self.stpxloopguardconfigentry = YList(self)
            self._segment_path = lambda: "stpxLoopGuardConfigTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable, [], name, value)


        class Stpxloopguardconfigentry(Entity):
            """
            A bridge port for which Spanning Tree LoopGuard 
            capability can be configured.
            
            .. attribute:: stpxloopguardconfigportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopguardconfigenabled
            
            	An indication of whether the LoopGuard capability is  enabled on this port or not. This configuration will be applied to all the Spanning Tree instances in which this  port exists.  In order to support additional Loop Guard config mode (default) as defined in stpxLoopGuardConfigMode other  than enable (true(1)) or disable (false(2)) as defined  in this object, stpxLoopGuardConfigMode object needs to  be used.  When the stpxLoopGuardConfigMode object has the value of enable(1), the value of stpxLoopGuardConfigEnabled for  the same instance will be true(1). When the  stpxLoopGuardConfigMode object has the value of disable(2),  the value of stpxLoopGuardConfigEnabled for the same  instance will be false(2). When the stpxLoopGuardConfigMode  object has the value of default(3), the value of  stpxLoopGuardConfigEnabled for the same instance will  depend on the object value of  stpxLoopGuardGlobalDefaultMode
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxloopguardconfigmode
            
            	Indicates the mode of Loop Guard Feature on this  port. This configuration will be applied to all  the Spanning Tree instances in which this port  exists.  enable \-\- the Loop Guard feature is enabled on this            port.   disable \-\- the Loop Guard feature is disabled on this            port.    default \-\- whether the Loop Guard feature is enabled            or not on this port depends on the object             value of stpxLoopGuardGlobalDefaultMode
            	**type**\:  :py:class:`Stpxloopguardconfigmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable.Stpxloopguardconfigentry.Stpxloopguardconfigmode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable.Stpxloopguardconfigentry, self).__init__()

                self.yang_name = "stpxLoopGuardConfigEntry"
                self.yang_parent_name = "stpxLoopGuardConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxloopguardconfigportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxloopguardconfigportindex', YLeaf(YType.int32, 'stpxLoopGuardConfigPortIndex')),
                    ('stpxloopguardconfigenabled', YLeaf(YType.boolean, 'stpxLoopGuardConfigEnabled')),
                    ('stpxloopguardconfigmode', YLeaf(YType.enumeration, 'stpxLoopGuardConfigMode')),
                ])
                self.stpxloopguardconfigportindex = None
                self.stpxloopguardconfigenabled = None
                self.stpxloopguardconfigmode = None
                self._segment_path = lambda: "stpxLoopGuardConfigEntry" + "[stpxLoopGuardConfigPortIndex='" + str(self.stpxloopguardconfigportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxLoopGuardConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxloopguardconfigtable.Stpxloopguardconfigentry, ['stpxloopguardconfigportindex', 'stpxloopguardconfigenabled', 'stpxloopguardconfigmode'], name, value)

            class Stpxloopguardconfigmode(Enum):
                """
                Stpxloopguardconfigmode (Enum Class)

                Indicates the mode of Loop Guard Feature on this 

                port. This configuration will be applied to all 

                the Spanning Tree instances in which this port 

                exists.

                enable \-\- the Loop Guard feature is enabled on this 

                          port. 

                disable \-\- the Loop Guard feature is disabled on this 

                          port.  

                default \-\- whether the Loop Guard feature is enabled

                           or not on this port depends on the object 

                           value of stpxLoopGuardGlobalDefaultMode.

                .. data:: enable = 1

                .. data:: disable = 2

                .. data:: default = 3

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")

                default = Enum.YLeaf(3, "default")



    class Stpxloopinconsistencytable(Entity):
        """
        A table containing a list of the bridge ports for which
        a particular Spanning Tree instance has been found
        to have a loop\-inconsistency. The agent creates a new
        entry in this table whenever it detects a new
        loop\-inconsistency, and deletes entries
        when/soon after the inconsistency is no longer present.
        
        .. attribute:: stpxloopinconsistencyentry
        
        	A Spanning Tree instance on a particular port for which a Spanning Tree loop\-inconsistency is currently in effect
        	**type**\: list of  		 :py:class:`Stpxloopinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable.Stpxloopinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable, self).__init__()

            self.yang_name = "stpxLoopInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxLoopInconsistencyEntry", ("stpxloopinconsistencyentry", CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable.Stpxloopinconsistencyentry))])
            self._leafs = OrderedDict()

            self.stpxloopinconsistencyentry = YList(self)
            self._segment_path = lambda: "stpxLoopInconsistencyTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable, [], name, value)


        class Stpxloopinconsistencyentry(Entity):
            """
            A Spanning Tree instance on a particular port for
            which a Spanning Tree loop\-inconsistency is currently
            in effect.
            
            .. attribute:: stpxloopinconsistencyindex  (key)
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxloopinconsistencyportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in loop\-inconsistent  state or not
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable.Stpxloopinconsistencyentry, self).__init__()

                self.yang_name = "stpxLoopInconsistencyEntry"
                self.yang_parent_name = "stpxLoopInconsistencyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxloopinconsistencyindex','stpxloopinconsistencyportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxloopinconsistencyindex', YLeaf(YType.int32, 'stpxLoopInconsistencyIndex')),
                    ('stpxloopinconsistencyportindex', YLeaf(YType.int32, 'stpxLoopInconsistencyPortIndex')),
                    ('stpxloopinconsistencystate', YLeaf(YType.boolean, 'stpxLoopInconsistencyState')),
                ])
                self.stpxloopinconsistencyindex = None
                self.stpxloopinconsistencyportindex = None
                self.stpxloopinconsistencystate = None
                self._segment_path = lambda: "stpxLoopInconsistencyEntry" + "[stpxLoopInconsistencyIndex='" + str(self.stpxloopinconsistencyindex) + "']" + "[stpxLoopInconsistencyPortIndex='" + str(self.stpxloopinconsistencyportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxLoopInconsistencyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxloopinconsistencytable.Stpxloopinconsistencyentry, ['stpxloopinconsistencyindex', 'stpxloopinconsistencyportindex', 'stpxloopinconsistencystate'], name, value)


    class Stpxfaststartporttable(Entity):
        """
        A table containing a list of the bridge ports for
        which Spanning Tree Port Fast Start can be
        configured.
        
        .. attribute:: stpxfaststartportentry
        
        	A bridge port for which Spanning Tree Port Fast Start can be configured
        	**type**\: list of  		 :py:class:`Stpxfaststartportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable, self).__init__()

            self.yang_name = "stpxFastStartPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxFastStartPortEntry", ("stpxfaststartportentry", CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry))])
            self._leafs = OrderedDict()

            self.stpxfaststartportentry = YList(self)
            self._segment_path = lambda: "stpxFastStartPortTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable, [], name, value)


        class Stpxfaststartportentry(Entity):
            """
            A bridge port for which Spanning Tree Port Fast
            Start can be configured.
            
            .. attribute:: stpxfaststartportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartportenable
            
            	Indicates whether the port is operating in spantree fast start mode.  A port with fast start enabled is immediately put in spanning tree forwarding state when that port is detected by the Spanning Tree, rather  than starting in blocking state which is the normal  operation.  In order to support additional Fast Start enable mode (enableForTrunk and default) as defined in stpxFastStartPortMode other than enable (true(1)) or disable (false(2)) as defined in this object, stpxFastStartPortMode object needs to be used.  When the stpxFastStartPortMode has the value of enable(1) or enableForTrunk(3), the value of stpxFastStartPortEnable for the same instance will be true(1). When the stpxFastStartPortMode has the value of disable(2), the value of  stpxFastStartPortEnable for the same instance will be  false(2). When the stpxFastStartPortMode has the value  of default(4), the value of stpxFastStartPortEnable for  the same instance depends on the object value of  stpxFastStartGlobalDefaultMode
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxfaststartportmode
            
            	Indicates the mode of Fast Start Feature on the  port. A port with fast start enabled is immediately  put in spanning tree forwarding state when the port is detected by the Spanning Tree, rather than  starting in blocking state which is the normal  operation.  enable \-\- the fast start feature is enabled on this            port but will only take effect when the            object value of its            vlanTrunkPortDynamicStatus as specified            in CISCO\-VTP\-MIB is notTrunking(2).  disable \-\- the fast start feature is disabled on this            port.    enableForTrunk \-\- the fast start feature is enabled            on this port and will take effect            regardless of the object value of            its vlanTrunkPortDynamicStatus.  default \-\- whether the fast start feature is enabled            or not on this port depends on the object             value of stpxFastStartGlobalDefaultMode.  network \-\- the fast start network mode is enabled on             this port
            	**type**\:  :py:class:`Stpxfaststartportmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportmode>`
            
            .. attribute:: stpxfaststartportbpduguardmode
            
            	Indicates the mode of Bpdu Guard Feature on the port. A port with Bpdu Guard enabled is  immediately disabled when the system  receives a BPDU from that port.   enable \-\- the Bpdu Guard feature is enabled on this           port.   disable \-\- the Bpdu Guard feature is disabled on this           port.  default \-\- whether the Bpdu Guard feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduGuardEnable. If             the value of stpxFastStartBpduGuardEnable            is true(1) and Fast Start feature is also             enabled operationally on this port, then            this port is immediately disabled when             the system receives a BPDU from this port
            	**type**\:  :py:class:`Stpxfaststartportbpduguardmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportbpduguardmode>`
            
            .. attribute:: stpxfaststartportbpdufiltermode
            
            	Indicates the mode of Bpdu Filter Feature on the port. The system will not transmit BPDUs on a port  with Bpdu Filter feature enabled.  enable \-\- the Bpdu Filter feature is enabled on this            port.   disable \-\- the Bpdu Filter feature is disabled on this            port.  default \-\- whether the Bpdu Filter feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduFilterEnable. If            the value of stpxFastStartBpduFilterEnable            is true(1) and Fast Start feature is also            enabled operationally on this port, then            no BPDUs will be transmitted on this port
            	**type**\:  :py:class:`Stpxfaststartportbpdufiltermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportbpdufiltermode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry, self).__init__()

                self.yang_name = "stpxFastStartPortEntry"
                self.yang_parent_name = "stpxFastStartPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxfaststartportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxfaststartportindex', YLeaf(YType.int32, 'stpxFastStartPortIndex')),
                    ('stpxfaststartportenable', YLeaf(YType.boolean, 'stpxFastStartPortEnable')),
                    ('stpxfaststartportmode', YLeaf(YType.enumeration, 'stpxFastStartPortMode')),
                    ('stpxfaststartportbpduguardmode', YLeaf(YType.enumeration, 'stpxFastStartPortBpduGuardMode')),
                    ('stpxfaststartportbpdufiltermode', YLeaf(YType.enumeration, 'stpxFastStartPortBpduFilterMode')),
                ])
                self.stpxfaststartportindex = None
                self.stpxfaststartportenable = None
                self.stpxfaststartportmode = None
                self.stpxfaststartportbpduguardmode = None
                self.stpxfaststartportbpdufiltermode = None
                self._segment_path = lambda: "stpxFastStartPortEntry" + "[stpxFastStartPortIndex='" + str(self.stpxfaststartportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxFastStartPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxfaststartporttable.Stpxfaststartportentry, ['stpxfaststartportindex', 'stpxfaststartportenable', 'stpxfaststartportmode', 'stpxfaststartportbpduguardmode', 'stpxfaststartportbpdufiltermode'], name, value)

            class Stpxfaststartportbpdufiltermode(Enum):
                """
                Stpxfaststartportbpdufiltermode (Enum Class)

                Indicates the mode of Bpdu Filter Feature on the

                port. The system will not transmit BPDUs on a port 

                with Bpdu Filter feature enabled.

                enable \-\- the Bpdu Filter feature is enabled on this 

                          port. 

                disable \-\- the Bpdu Filter feature is disabled on this

                           port.

                default \-\- whether the Bpdu Filter feature is enabled

                           or not on this port depends on the object

                           value of stpxFastStartBpduFilterEnable. If

                           the value of stpxFastStartBpduFilterEnable

                           is true(1) and Fast Start feature is also

                           enabled operationally on this port, then

                           no BPDUs will be transmitted on this port.

                .. data:: enable = 1

                .. data:: disable = 2

                .. data:: default = 3

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")

                default = Enum.YLeaf(3, "default")


            class Stpxfaststartportbpduguardmode(Enum):
                """
                Stpxfaststartportbpduguardmode (Enum Class)

                Indicates the mode of Bpdu Guard Feature on the

                port. A port with Bpdu Guard enabled is 

                immediately disabled when the system 

                receives a BPDU from that port. 

                enable \-\- the Bpdu Guard feature is enabled on this

                          port. 

                disable \-\- the Bpdu Guard feature is disabled on this

                          port.

                default \-\- whether the Bpdu Guard feature is enabled

                           or not on this port depends on the object

                           value of stpxFastStartBpduGuardEnable. If 

                           the value of stpxFastStartBpduGuardEnable

                           is true(1) and Fast Start feature is also 

                           enabled operationally on this port, then

                           this port is immediately disabled when 

                           the system receives a BPDU from this port.

                .. data:: enable = 1

                .. data:: disable = 2

                .. data:: default = 3

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")

                default = Enum.YLeaf(3, "default")


            class Stpxfaststartportmode(Enum):
                """
                Stpxfaststartportmode (Enum Class)

                Indicates the mode of Fast Start Feature on the 

                port. A port with fast start enabled is immediately 

                put in spanning tree forwarding state when the port

                is detected by the Spanning Tree, rather than 

                starting in blocking state which is the normal 

                operation.

                enable \-\- the fast start feature is enabled on this 

                          port but will only take effect when the 

                          object value of its 

                          vlanTrunkPortDynamicStatus as specified 

                          in CISCO\-VTP\-MIB is notTrunking(2).

                disable \-\- the fast start feature is disabled on this 

                          port.  

                enableForTrunk \-\- the fast start feature is enabled 

                          on this port and will take effect 

                          regardless of the object value of 

                          its vlanTrunkPortDynamicStatus.

                default \-\- whether the fast start feature is enabled

                           or not on this port depends on the object 

                           value of stpxFastStartGlobalDefaultMode.

                network \-\- the fast start network mode is enabled on 

                           this port.

                .. data:: enable = 1

                .. data:: disable = 2

                .. data:: enableForTrunk = 3

                .. data:: default = 4

                .. data:: network = 5

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")

                enableForTrunk = Enum.YLeaf(3, "enableForTrunk")

                default = Enum.YLeaf(4, "default")

                network = Enum.YLeaf(5, "network")



    class Stpxfaststartopermodetable(Entity):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        
        .. attribute:: stpxfaststartopermodeentry
        
        	An entry with port fast start oper mode  information on a bridge port for a particular  Spanning Tree Instance
        	**type**\: list of  		 :py:class:`Stpxfaststartopermodeentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable.Stpxfaststartopermodeentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable, self).__init__()

            self.yang_name = "stpxFastStartOperModeTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxFastStartOperModeEntry", ("stpxfaststartopermodeentry", CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable.Stpxfaststartopermodeentry))])
            self._leafs = OrderedDict()

            self.stpxfaststartopermodeentry = YList(self)
            self._segment_path = lambda: "stpxFastStartOperModeTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable, [], name, value)


        class Stpxfaststartopermodeentry(Entity):
            """
            An entry with port fast start oper mode 
            information on a bridge port for a particular 
            Spanning Tree Instance.
            
            .. attribute:: stpxfaststartopermodeinstindex  (key)
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxfaststartopermodeportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartopermode
            
            	Indicates the fast start operational status of the  port on a particular Spanning Tree Instance
            	**type**\:  :py:class:`Stpxfaststartopermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable.Stpxfaststartopermodeentry.Stpxfaststartopermode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable.Stpxfaststartopermodeentry, self).__init__()

                self.yang_name = "stpxFastStartOperModeEntry"
                self.yang_parent_name = "stpxFastStartOperModeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxfaststartopermodeinstindex','stpxfaststartopermodeportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxfaststartopermodeinstindex', YLeaf(YType.int32, 'stpxFastStartOperModeInstIndex')),
                    ('stpxfaststartopermodeportindex', YLeaf(YType.int32, 'stpxFastStartOperModePortIndex')),
                    ('stpxfaststartopermode', YLeaf(YType.enumeration, 'stpxFastStartOperMode')),
                ])
                self.stpxfaststartopermodeinstindex = None
                self.stpxfaststartopermodeportindex = None
                self.stpxfaststartopermode = None
                self._segment_path = lambda: "stpxFastStartOperModeEntry" + "[stpxFastStartOperModeInstIndex='" + str(self.stpxfaststartopermodeinstindex) + "']" + "[stpxFastStartOperModePortIndex='" + str(self.stpxfaststartopermodeportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxFastStartOperModeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxfaststartopermodetable.Stpxfaststartopermodeentry, ['stpxfaststartopermodeinstindex', 'stpxfaststartopermodeportindex', 'stpxfaststartopermode'], name, value)

            class Stpxfaststartopermode(Enum):
                """
                Stpxfaststartopermode (Enum Class)

                Indicates the fast start operational status of the 

                port on a particular Spanning Tree Instance.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")



    class Stpxbpduskewingtable(Entity):
        """
        A table containing a list of the bridge ports for 
        which a particular Spanning Tree instance has been 
        detected to have BPDU skewing occurred since the 
        object value of stpxBpduSkewingDetectionEnable was
        last changed to true(1).
        
        The agent creates a new entry in this table whenever
        a port in a particular Spanning Tree instance is 
        detected to be BPDU skewed since the object value of 
        stpxBpduSkewingDetectionEnable object is changed to 
        true(1). The agent deletes all the entries in this 
        table when the object value of 
        stpxBpduSkewingDetectionEnable is changed to false(2)
        or the object value of stpxSpanningTreeType is 
        changed.
        
        .. attribute:: stpxbpduskewingentry
        
        	A Spanning Tree instance on a particular port for which BPDU skewing has been detected
        	**type**\: list of  		 :py:class:`Stpxbpduskewingentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable.Stpxbpduskewingentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable, self).__init__()

            self.yang_name = "stpxBpduSkewingTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxBpduSkewingEntry", ("stpxbpduskewingentry", CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable.Stpxbpduskewingentry))])
            self._leafs = OrderedDict()

            self.stpxbpduskewingentry = YList(self)
            self._segment_path = lambda: "stpxBpduSkewingTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable, [], name, value)


        class Stpxbpduskewingentry(Entity):
            """
            A Spanning Tree instance on a particular port for
            which BPDU skewing has been detected.
            
            .. attribute:: stpxbpduskewinginstanceindex  (key)
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType  is pvstPlus(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxbpduskewingportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxbpduskewinglastskewduration
            
            	Indicates the skew duration in milliseconds of the last BPDU skewing detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: stpxbpduskewingworstskewduration
            
            	Indicates the skew duration in milliseconds of the worst BPDU skewing detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: stpxbpduskewingworstskewtime
            
            	Indicates the value of sysUpTime when the worst BPDU skewing was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable.Stpxbpduskewingentry, self).__init__()

                self.yang_name = "stpxBpduSkewingEntry"
                self.yang_parent_name = "stpxBpduSkewingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxbpduskewinginstanceindex','stpxbpduskewingportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxbpduskewinginstanceindex', YLeaf(YType.int32, 'stpxBpduSkewingInstanceIndex')),
                    ('stpxbpduskewingportindex', YLeaf(YType.int32, 'stpxBpduSkewingPortIndex')),
                    ('stpxbpduskewinglastskewduration', YLeaf(YType.uint32, 'stpxBpduSkewingLastSkewDuration')),
                    ('stpxbpduskewingworstskewduration', YLeaf(YType.uint32, 'stpxBpduSkewingWorstSkewDuration')),
                    ('stpxbpduskewingworstskewtime', YLeaf(YType.uint32, 'stpxBpduSkewingWorstSkewTime')),
                ])
                self.stpxbpduskewinginstanceindex = None
                self.stpxbpduskewingportindex = None
                self.stpxbpduskewinglastskewduration = None
                self.stpxbpduskewingworstskewduration = None
                self.stpxbpduskewingworstskewtime = None
                self._segment_path = lambda: "stpxBpduSkewingEntry" + "[stpxBpduSkewingInstanceIndex='" + str(self.stpxbpduskewinginstanceindex) + "']" + "[stpxBpduSkewingPortIndex='" + str(self.stpxbpduskewingportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxBpduSkewingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxbpduskewingtable.Stpxbpduskewingentry, ['stpxbpduskewinginstanceindex', 'stpxbpduskewingportindex', 'stpxbpduskewinglastskewduration', 'stpxbpduskewingworstskewduration', 'stpxbpduskewingworstskewtime'], name, value)


    class Stpxmstinstancetable(Entity):
        """
        This table contains MST instance information with
        one entry for an MST instance within the range of 
        0 to the object value of stpxMSTMaxInstanceNumber. 
        
        This table is deprecated and replaced by 
        stpxSMSTInstanceTable.
        
        .. attribute:: stpxmstinstanceentry
        
        	A conceptual row containing the MST instance  information
        	**type**\: list of  		 :py:class:`Stpxmstinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable.Stpxmstinstanceentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable, self).__init__()

            self.yang_name = "stpxMSTInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxMSTInstanceEntry", ("stpxmstinstanceentry", CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable.Stpxmstinstanceentry))])
            self._leafs = OrderedDict()

            self.stpxmstinstanceentry = YList(self)
            self._segment_path = lambda: "stpxMSTInstanceTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable, [], name, value)


        class Stpxmstinstanceentry(Entity):
            """
            A conceptual row containing the MST instance 
            information.
            
            .. attribute:: stpxmstinstanceindex  (key)
            
            	An integer that uniquely identifies an MST instance  within the range of 0 to the object value of stpxMSTMaxInstanceNumber.  This object is deprecated and replaced by  stpxSMSTInstanceIndex
            	**type**\: int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped3k4k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by stpxSMSTInstanceVlansMapped3k4k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance.  This object will take on value of 40 if the object value of stpxSMSTInstanceRemainingHopCount is greater than 40.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTInstanceRemainingHopCount
            	**type**\: int
            
            	**range:** 0..40
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable.Stpxmstinstanceentry, self).__init__()

                self.yang_name = "stpxMSTInstanceEntry"
                self.yang_parent_name = "stpxMSTInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxmstinstanceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxmstinstanceindex', YLeaf(YType.int32, 'stpxMSTInstanceIndex')),
                    ('stpxmstinstancevlansmapped', YLeaf(YType.str, 'stpxMSTInstanceVlansMapped')),
                    ('stpxmstinstancevlansmapped2k', YLeaf(YType.str, 'stpxMSTInstanceVlansMapped2k')),
                    ('stpxmstinstancevlansmapped3k', YLeaf(YType.str, 'stpxMSTInstanceVlansMapped3k')),
                    ('stpxmstinstancevlansmapped4k', YLeaf(YType.str, 'stpxMSTInstanceVlansMapped4k')),
                    ('stpxmstinstanceremaininghopcount', YLeaf(YType.int32, 'stpxMSTInstanceRemainingHopCount')),
                ])
                self.stpxmstinstanceindex = None
                self.stpxmstinstancevlansmapped = None
                self.stpxmstinstancevlansmapped2k = None
                self.stpxmstinstancevlansmapped3k = None
                self.stpxmstinstancevlansmapped4k = None
                self.stpxmstinstanceremaininghopcount = None
                self._segment_path = lambda: "stpxMSTInstanceEntry" + "[stpxMSTInstanceIndex='" + str(self.stpxmstinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTInstanceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstinstancetable.Stpxmstinstanceentry, ['stpxmstinstanceindex', 'stpxmstinstancevlansmapped', 'stpxmstinstancevlansmapped2k', 'stpxmstinstancevlansmapped3k', 'stpxmstinstancevlansmapped4k', 'stpxmstinstanceremaininghopcount'], name, value)


    class Stpxmstinstanceedittable(Entity):
        """
        This table contains MST instance information in the 
        Edit Buffer with one entry for each MST
        instance numbered from 0 to stpxMSTMaxInstanceNumber. 
        
        This table is only instantiated when the 
        stpxMSTRegionEditBufferStatus has the value of
        acquiredBySnmp(2).
        
        This table is deprecated and replaced by 
        stpxSMSTInstanceEditTable.
        
        .. attribute:: stpxmstinstanceeditentry
        
        	A conceptual row containing MST instance information  in the Edit Buffer
        	**type**\: list of  		 :py:class:`Stpxmstinstanceeditentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable.Stpxmstinstanceeditentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable, self).__init__()

            self.yang_name = "stpxMSTInstanceEditTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxMSTInstanceEditEntry", ("stpxmstinstanceeditentry", CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable.Stpxmstinstanceeditentry))])
            self._leafs = OrderedDict()

            self.stpxmstinstanceeditentry = YList(self)
            self._segment_path = lambda: "stpxMSTInstanceEditTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable, [], name, value)


        class Stpxmstinstanceeditentry(Entity):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            .. attribute:: stpxmstinstanceeditindex  (key)
            
            	An integer that uniquely identifies an MST instance  from 0 to the object value of stpxMSTMaxInstanceNumber.  The instances of this table entry with  stpxMSTInstanceEditIndex of zero can not be  modified.  This object is deprecated and replaced by  stpxSMSTInstanceEditIndex
            	**type**\: int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap3k4k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by stpxSMSTInstanceEditVlansMap3k4k
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable.Stpxmstinstanceeditentry, self).__init__()

                self.yang_name = "stpxMSTInstanceEditEntry"
                self.yang_parent_name = "stpxMSTInstanceEditTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxmstinstanceeditindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxmstinstanceeditindex', YLeaf(YType.int32, 'stpxMSTInstanceEditIndex')),
                    ('stpxmstinstanceeditvlansmap', YLeaf(YType.str, 'stpxMSTInstanceEditVlansMap')),
                    ('stpxmstinstanceeditvlansmap2k', YLeaf(YType.str, 'stpxMSTInstanceEditVlansMap2k')),
                    ('stpxmstinstanceeditvlansmap3k', YLeaf(YType.str, 'stpxMSTInstanceEditVlansMap3k')),
                    ('stpxmstinstanceeditvlansmap4k', YLeaf(YType.str, 'stpxMSTInstanceEditVlansMap4k')),
                ])
                self.stpxmstinstanceeditindex = None
                self.stpxmstinstanceeditvlansmap = None
                self.stpxmstinstanceeditvlansmap2k = None
                self.stpxmstinstanceeditvlansmap3k = None
                self.stpxmstinstanceeditvlansmap4k = None
                self._segment_path = lambda: "stpxMSTInstanceEditEntry" + "[stpxMSTInstanceEditIndex='" + str(self.stpxmstinstanceeditindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTInstanceEditTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstinstanceedittable.Stpxmstinstanceeditentry, ['stpxmstinstanceeditindex', 'stpxmstinstanceeditvlansmap', 'stpxmstinstanceeditvlansmap2k', 'stpxmstinstanceeditvlansmap3k', 'stpxmstinstanceeditvlansmap4k'], name, value)


    class Stpxmstporttable(Entity):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        .. attribute:: stpxmstportentry
        
        	An entry with port information for the MST Protocol on a bridge port
        	**type**\: list of  		 :py:class:`Stpxmstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmstporttable, self).__init__()

            self.yang_name = "stpxMSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxMSTPortEntry", ("stpxmstportentry", CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry))])
            self._leafs = OrderedDict()

            self.stpxmstportentry = YList(self)
            self._segment_path = lambda: "stpxMSTPortTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstporttable, [], name, value)


        class Stpxmstportentry(Entity):
            """
            An entry with port information for the MST Protocol
            on a bridge port.
            
            .. attribute:: stpxmstportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the MST protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5). stpxMSTPortAdminLinkType is deprecated and replaced  with stpxRSTPPortAdminLinkType
            	**type**\:  :py:class:`Stpxmstportadminlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry.Stpxmstportadminlinktype>`
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportoperlinktype
            
            	Indicates the operational link type of a bridge port for the MST protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  stpxMSTPortOperLinkType  is deprecated and replaced with stpxRSTPPortOperLinkType
            	**type**\:  :py:class:`Stpxmstportoperlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry.Stpxmstportoperlinktype>`
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to this  object has no effect. Setting false(2) to this object has  no effect. This object always returns false(2) when read. stpxMSTPortProtocolMigration is deprecated and  replaced with stpxRSTPPortProtocolMigration
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTPortStatus
            	**type**\:  :py:class:`Stpxmstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry.Stpxmstportstatus>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry, self).__init__()

                self.yang_name = "stpxMSTPortEntry"
                self.yang_parent_name = "stpxMSTPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxmstportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxmstportindex', YLeaf(YType.int32, 'stpxMSTPortIndex')),
                    ('stpxmstportadminlinktype', YLeaf(YType.enumeration, 'stpxMSTPortAdminLinkType')),
                    ('stpxmstportoperlinktype', YLeaf(YType.enumeration, 'stpxMSTPortOperLinkType')),
                    ('stpxmstportprotocolmigration', YLeaf(YType.boolean, 'stpxMSTPortProtocolMigration')),
                    ('stpxmstportstatus', YLeaf(YType.bits, 'stpxMSTPortStatus')),
                ])
                self.stpxmstportindex = None
                self.stpxmstportadminlinktype = None
                self.stpxmstportoperlinktype = None
                self.stpxmstportprotocolmigration = None
                self.stpxmstportstatus = Bits()
                self._segment_path = lambda: "stpxMSTPortEntry" + "[stpxMSTPortIndex='" + str(self.stpxmstportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstporttable.Stpxmstportentry, ['stpxmstportindex', 'stpxmstportadminlinktype', 'stpxmstportoperlinktype', 'stpxmstportprotocolmigration', 'stpxmstportstatus'], name, value)

            class Stpxmstportadminlinktype(Enum):
                """
                Stpxmstportadminlinktype (Enum Class)

                Indicates the administrative link type configuration of 

                a bridge port for the MST protocol. 

                pointToPoint \-\- the port is administratively configured to

                        be connected to a point\-to\-point link.

                shared \-\- the port is administratively configured to be

                        connected to a shared medium. 

                auto \-\- the administrative configuration of the port's 

                        link type depends on link duplex of the port.

                        If the port link is full\-duplex, the administrative 

                        link type configuration on this port will be taken 

                        as pointTopoint(1). If the port link is half\-duplex, 

                        the administrative link type configuration on this

                        port will be taken as shared(2).

                This configuration of this object only takes effect when the

                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).

                stpxMSTPortAdminLinkType is deprecated and replaced 

                with stpxRSTPPortAdminLinkType.

                .. data:: pointToPoint = 1

                .. data:: shared = 2

                .. data:: auto = 3

                """

                pointToPoint = Enum.YLeaf(1, "pointToPoint")

                shared = Enum.YLeaf(2, "shared")

                auto = Enum.YLeaf(3, "auto")


            class Stpxmstportoperlinktype(Enum):
                """
                Stpxmstportoperlinktype (Enum Class)

                Indicates the operational link type of a bridge port

                for the MST protocol.

                pointToPoint \-\- the port is operationally connected to

                        a point\-to\-point link.

                shared \-\- the port is operationally connected to 

                        a shared medium.

                other \-\- none of the above.

                This object is only instantiated when the object value of

                stpxSpanningTreeType is mst(4).  stpxMSTPortOperLinkType 

                is deprecated and replaced with stpxRSTPPortOperLinkType.

                .. data:: pointToPoint = 1

                .. data:: shared = 2

                .. data:: other = 3

                """

                pointToPoint = Enum.YLeaf(1, "pointToPoint")

                shared = Enum.YLeaf(2, "shared")

                other = Enum.YLeaf(3, "other")



    class Stpxmstportroletable(Entity):
        """
        A table containing a list of the bridge ports for a 
        particular MST instance.  This table is only instantiated 
        when the stpxSpanningTreeType is mst(4). 
        
        This table is deprecated and replaced with 
        stpxRSTPPortRoleTable.
        
        .. attribute:: stpxmstportroleentry
        
        	An entry containing the port role information for the MST protocol on a port for a particular MST instance existing on the system
        	**type**\: list of  		 :py:class:`Stpxmstportroleentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstportroletable.Stpxmstportroleentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxmstportroletable, self).__init__()

            self.yang_name = "stpxMSTPortRoleTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxMSTPortRoleEntry", ("stpxmstportroleentry", CISCOSTPEXTENSIONSMIB.Stpxmstportroletable.Stpxmstportroleentry))])
            self._leafs = OrderedDict()

            self.stpxmstportroleentry = YList(self)
            self._segment_path = lambda: "stpxMSTPortRoleTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstportroletable, [], name, value)


        class Stpxmstportroleentry(Entity):
            """
            An entry containing the port role information for the MST
            protocol on a port for a particular MST instance existing
            on the system.
            
            .. attribute:: stpxmstportroleinstanceindex  (key)
            
            	The MST instance id within the range of 0 to stpxMSTMaxInstanceNumber
            	**type**\: int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportroleportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportrolevalue
            
            	Indicates the port role on a particular MST instance for the MST protocol.   disabled \-\-  this port has no role on this MST instance.   root \-\- this port has the role of root port on this MST             instance.   designated \-\- this port has the role of designated              port on this MST instance.  alternate \-\- this port has the role of alternate port             on this MST instance.  backUp \-\- this port has the role of backup port on this               MST instance.  boundary \-\- this port has the role of boundary port on              this MST instance.  master \-\- this port has the role of master port on           this MST instance
            	**type**\:  :py:class:`Stpxmstportrolevalue <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxmstportroletable.Stpxmstportroleentry.Stpxmstportrolevalue>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxmstportroletable.Stpxmstportroleentry, self).__init__()

                self.yang_name = "stpxMSTPortRoleEntry"
                self.yang_parent_name = "stpxMSTPortRoleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxmstportroleinstanceindex','stpxmstportroleportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxmstportroleinstanceindex', YLeaf(YType.int32, 'stpxMSTPortRoleInstanceIndex')),
                    ('stpxmstportroleportindex', YLeaf(YType.int32, 'stpxMSTPortRolePortIndex')),
                    ('stpxmstportrolevalue', YLeaf(YType.enumeration, 'stpxMSTPortRoleValue')),
                ])
                self.stpxmstportroleinstanceindex = None
                self.stpxmstportroleportindex = None
                self.stpxmstportrolevalue = None
                self._segment_path = lambda: "stpxMSTPortRoleEntry" + "[stpxMSTPortRoleInstanceIndex='" + str(self.stpxmstportroleinstanceindex) + "']" + "[stpxMSTPortRolePortIndex='" + str(self.stpxmstportroleportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTPortRoleTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxmstportroletable.Stpxmstportroleentry, ['stpxmstportroleinstanceindex', 'stpxmstportroleportindex', 'stpxmstportrolevalue'], name, value)

            class Stpxmstportrolevalue(Enum):
                """
                Stpxmstportrolevalue (Enum Class)

                Indicates the port role on a particular MST instance

                for the MST protocol. 

                disabled \-\-  this port has no role on this MST instance. 

                root \-\- this port has the role of root port on this MST

                            instance. 

                designated \-\- this port has the role of designated 

                            port on this MST instance.

                alternate \-\- this port has the role of alternate port

                            on this MST instance.

                backUp \-\- this port has the role of backup port on this  

                            MST instance.

                boundary \-\- this port has the role of boundary port on 

                            this MST instance.

                master \-\- this port has the role of master port on

                          this MST instance.

                .. data:: disabled = 1

                .. data:: root = 2

                .. data:: designated = 3

                .. data:: alternate = 4

                .. data:: backUp = 5

                .. data:: boundary = 6

                .. data:: master = 7

                """

                disabled = Enum.YLeaf(1, "disabled")

                root = Enum.YLeaf(2, "root")

                designated = Enum.YLeaf(3, "designated")

                alternate = Enum.YLeaf(4, "alternate")

                backUp = Enum.YLeaf(5, "backUp")

                boundary = Enum.YLeaf(6, "boundary")

                master = Enum.YLeaf(7, "master")



    class Stpxrstpporttable(Entity):
        """
        A table containing port information for the RSTP 
        Protocol on all the bridge ports existing in the 
        system.
        
        .. attribute:: stpxrstpportentry
        
        	An entry with port information for the RSTP Protocol on a bridge port
        	**type**\: list of  		 :py:class:`Stpxrstpportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrstpporttable, self).__init__()

            self.yang_name = "stpxRSTPPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxRSTPPortEntry", ("stpxrstpportentry", CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry))])
            self._leafs = OrderedDict()

            self.stpxrstpportentry = YList(self)
            self._segment_path = lambda: "stpxRSTPPortTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrstpporttable, [], name, value)


        class Stpxrstpportentry(Entity):
            """
            An entry with port information for the RSTP Protocol
            on a bridge port.
            
            .. attribute:: stpxrstpportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the RSTP protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\:  :py:class:`Stpxrstpportadminlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry.Stpxrstpportadminlinktype>`
            
            .. attribute:: stpxrstpportoperlinktype
            
            	Indicates the operational link type of a bridge port for the RSTP protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\:  :py:class:`Stpxrstpportoperlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry.Stpxrstpportoperlinktype>`
            
            .. attribute:: stpxrstpportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to  this object has no effect. Setting false(2) to this  object has no effect. This object always returns  false(2) when read
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry, self).__init__()

                self.yang_name = "stpxRSTPPortEntry"
                self.yang_parent_name = "stpxRSTPPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxrstpportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxrstpportindex', YLeaf(YType.int32, 'stpxRSTPPortIndex')),
                    ('stpxrstpportadminlinktype', YLeaf(YType.enumeration, 'stpxRSTPPortAdminLinkType')),
                    ('stpxrstpportoperlinktype', YLeaf(YType.enumeration, 'stpxRSTPPortOperLinkType')),
                    ('stpxrstpportprotocolmigration', YLeaf(YType.boolean, 'stpxRSTPPortProtocolMigration')),
                ])
                self.stpxrstpportindex = None
                self.stpxrstpportadminlinktype = None
                self.stpxrstpportoperlinktype = None
                self.stpxrstpportprotocolmigration = None
                self._segment_path = lambda: "stpxRSTPPortEntry" + "[stpxRSTPPortIndex='" + str(self.stpxrstpportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRSTPPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrstpporttable.Stpxrstpportentry, ['stpxrstpportindex', 'stpxrstpportadminlinktype', 'stpxrstpportoperlinktype', 'stpxrstpportprotocolmigration'], name, value)

            class Stpxrstpportadminlinktype(Enum):
                """
                Stpxrstpportadminlinktype (Enum Class)

                Indicates the administrative link type configuration of 

                a bridge port for the RSTP protocol. 

                pointToPoint \-\- the port is administratively configured to

                        be connected to a point\-to\-point link.

                shared \-\- the port is administratively configured to be

                        connected to a shared medium. 

                auto \-\- the administrative configuration of the port's 

                        link type depends on link duplex of the port.

                        If the port link is full\-duplex, the administrative 

                        link type configuration on this port will be taken 

                        as pointTopoint(1). If the port link is half\-duplex, 

                        the administrative link type configuration on this

                        port will be taken as shared(2).

                This configuration of this object only takes effect when the

                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).

                .. data:: pointToPoint = 1

                .. data:: shared = 2

                .. data:: auto = 3

                """

                pointToPoint = Enum.YLeaf(1, "pointToPoint")

                shared = Enum.YLeaf(2, "shared")

                auto = Enum.YLeaf(3, "auto")


            class Stpxrstpportoperlinktype(Enum):
                """
                Stpxrstpportoperlinktype (Enum Class)

                Indicates the operational link type of a bridge port

                for the RSTP protocol.

                pointToPoint \-\- the port is operationally connected to

                        a point\-to\-point link.

                shared \-\- the port is operationally connected to 

                        a shared medium.

                other \-\- none of the above.

                This object is only instantiated when the object value of

                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).

                .. data:: pointToPoint = 1

                .. data:: shared = 2

                .. data:: other = 3

                """

                pointToPoint = Enum.YLeaf(1, "pointToPoint")

                shared = Enum.YLeaf(2, "shared")

                other = Enum.YLeaf(3, "other")



    class Stpxrstpportroletable(Entity):
        """
        A table containing a list of the bridge ports for a 
        particular Spanning Tree instance.  This table is 
        only instantiated when the stpxSpanningTreeType is mst(4) 
        or rapidPvstPlus(5).
        
        .. attribute:: stpxrstpportroleentry
        
        	An entry containing the port role information for the RSTP protocol on a port for a particular Spanning Tree instance
        	**type**\: list of  		 :py:class:`Stpxrstpportroleentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable.Stpxrstpportroleentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable, self).__init__()

            self.yang_name = "stpxRSTPPortRoleTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxRSTPPortRoleEntry", ("stpxrstpportroleentry", CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable.Stpxrstpportroleentry))])
            self._leafs = OrderedDict()

            self.stpxrstpportroleentry = YList(self)
            self._segment_path = lambda: "stpxRSTPPortRoleTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable, [], name, value)


        class Stpxrstpportroleentry(Entity):
            """
            An entry containing the port role information for the RSTP
            protocol on a port for a particular Spanning Tree instance.
            
            .. attribute:: stpxrstpportroleinstanceindex  (key)
            
            	The Spanning Tree instance id, it can either be a  VLAN number if the stpxSpanningTreeType is rapidPvstPlus(5)  or an MST instance id if the stpxSpanningTreeType is mst(4)
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrstpportroleportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportrolevalue
            
            	Indicates the port role on a particular Spanning Tree  instance for the RSTP protocol.   disabled \-\-  this port has no role in this Spanning             Tree instance.   root \-\- this port has the role of root port in this             Spanning Tree instance.   designated \-\- this port has the role of designated              port in this Spanning Tree instance.  alternate \-\- this port has the role of alternate port             in this Spanning Tree instance.  backUp \-\- this port has the role of backup port in this               Spanning Tree instance.  boundary \-\- this port has the role of boundary port in              this Spanning Tree instance.  master \-\- this port has the role of master port in             this Spanning Tree instance.  This object could have a value of 'boundary' or 'master' only when the object value of stpxSpanningTreeType is mst(4)
            	**type**\:  :py:class:`Stpxrstpportrolevalue <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable.Stpxrstpportroleentry.Stpxrstpportrolevalue>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable.Stpxrstpportroleentry, self).__init__()

                self.yang_name = "stpxRSTPPortRoleEntry"
                self.yang_parent_name = "stpxRSTPPortRoleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxrstpportroleinstanceindex','stpxrstpportroleportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxrstpportroleinstanceindex', YLeaf(YType.int32, 'stpxRSTPPortRoleInstanceIndex')),
                    ('stpxrstpportroleportindex', YLeaf(YType.int32, 'stpxRSTPPortRolePortIndex')),
                    ('stpxrstpportrolevalue', YLeaf(YType.enumeration, 'stpxRSTPPortRoleValue')),
                ])
                self.stpxrstpportroleinstanceindex = None
                self.stpxrstpportroleportindex = None
                self.stpxrstpportrolevalue = None
                self._segment_path = lambda: "stpxRSTPPortRoleEntry" + "[stpxRSTPPortRoleInstanceIndex='" + str(self.stpxrstpportroleinstanceindex) + "']" + "[stpxRSTPPortRolePortIndex='" + str(self.stpxrstpportroleportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRSTPPortRoleTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrstpportroletable.Stpxrstpportroleentry, ['stpxrstpportroleinstanceindex', 'stpxrstpportroleportindex', 'stpxrstpportrolevalue'], name, value)

            class Stpxrstpportrolevalue(Enum):
                """
                Stpxrstpportrolevalue (Enum Class)

                Indicates the port role on a particular Spanning Tree 

                instance for the RSTP protocol. 

                disabled \-\-  this port has no role in this Spanning

                            Tree instance. 

                root \-\- this port has the role of root port in this

                            Spanning Tree instance. 

                designated \-\- this port has the role of designated 

                            port in this Spanning Tree instance.

                alternate \-\- this port has the role of alternate port

                            in this Spanning Tree instance.

                backUp \-\- this port has the role of backup port in this  

                            Spanning Tree instance.

                boundary \-\- this port has the role of boundary port in 

                            this Spanning Tree instance.

                master \-\- this port has the role of master port in

                            this Spanning Tree instance.

                This object could have a value of 'boundary' or 'master'

                only when the object value of stpxSpanningTreeType is mst(4).

                .. data:: disabled = 1

                .. data:: root = 2

                .. data:: designated = 3

                .. data:: alternate = 4

                .. data:: backUp = 5

                .. data:: boundary = 6

                .. data:: master = 7

                """

                disabled = Enum.YLeaf(1, "disabled")

                root = Enum.YLeaf(2, "root")

                designated = Enum.YLeaf(3, "designated")

                alternate = Enum.YLeaf(4, "alternate")

                backUp = Enum.YLeaf(5, "backUp")

                boundary = Enum.YLeaf(6, "boundary")

                master = Enum.YLeaf(7, "master")



    class Stpxrpvstporttable(Entity):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        This table is only instantiated when the object value
        of stpxSpanningTreeType is rapidPvstPlus(5).
        
        .. attribute:: stpxrpvstportentry
        
        	An entry with port status information on a  bridge port for a particular Spanning Tree  Instance
        	**type**\: list of  		 :py:class:`Stpxrpvstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable.Stpxrpvstportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable, self).__init__()

            self.yang_name = "stpxRPVSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxRPVSTPortEntry", ("stpxrpvstportentry", CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable.Stpxrpvstportentry))])
            self._leafs = OrderedDict()

            self.stpxrpvstportentry = YList(self)
            self._segment_path = lambda: "stpxRPVSTPortTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable, [], name, value)


        class Stpxrpvstportentry(Entity):
            """
            An entry with port status information on a 
            bridge port for a particular Spanning Tree 
            Instance.
            
            .. attribute:: stpxrpvstportvlanindex  (key)
            
            	The VLAN id of the VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrpvstportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrpvstportstatus
            
            	Indicates the operational status of the port for the  Rapid PVST+ protocol.  edge \-\- this port is an edge port for the RST region.  unused1 \-\- unused bit 1.  unused2 \-\- unused bit 2.  stp \-\- this port is connected to a Single Spanning        Tree/PVST+ bridge.  dispute \-\- this port, as a designated port, received an        inferior BPDU with a designated role and the        learning bit being set
            	**type**\:  :py:class:`Stpxrpvstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable.Stpxrpvstportentry.Stpxrpvstportstatus>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable.Stpxrpvstportentry, self).__init__()

                self.yang_name = "stpxRPVSTPortEntry"
                self.yang_parent_name = "stpxRPVSTPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxrpvstportvlanindex','stpxrpvstportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxrpvstportvlanindex', YLeaf(YType.int32, 'stpxRPVSTPortVlanIndex')),
                    ('stpxrpvstportindex', YLeaf(YType.int32, 'stpxRPVSTPortIndex')),
                    ('stpxrpvstportstatus', YLeaf(YType.bits, 'stpxRPVSTPortStatus')),
                ])
                self.stpxrpvstportvlanindex = None
                self.stpxrpvstportindex = None
                self.stpxrpvstportstatus = Bits()
                self._segment_path = lambda: "stpxRPVSTPortEntry" + "[stpxRPVSTPortVlanIndex='" + str(self.stpxrpvstportvlanindex) + "']" + "[stpxRPVSTPortIndex='" + str(self.stpxrpvstportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRPVSTPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxrpvstporttable.Stpxrpvstportentry, ['stpxrpvstportvlanindex', 'stpxrpvstportindex', 'stpxrpvstportstatus'], name, value)


    class Stpxsmstinstancetable(Entity):
        """
        This table contains MST instance information
        for IEEE MST.
        
        .. attribute:: stpxsmstinstanceentry
        
        	A conceptual row containing the MST instance  information for IEEE MST
        	**type**\: list of  		 :py:class:`Stpxsmstinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable.Stpxsmstinstanceentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable, self).__init__()

            self.yang_name = "stpxSMSTInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxSMSTInstanceEntry", ("stpxsmstinstanceentry", CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable.Stpxsmstinstanceentry))])
            self._leafs = OrderedDict()

            self.stpxsmstinstanceentry = YList(self)
            self._segment_path = lambda: "stpxSMSTInstanceTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable, [], name, value)


        class Stpxsmstinstanceentry(Entity):
            """
            A conceptual row containing the MST instance 
            information for IEEE MST.
            
            .. attribute:: stpxsmstinstanceindex  (key)
            
            	The MST instance ID, the value of which is in the range  from 0 to stpxSMSTMaxInstanceID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstancevlansmapped1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstancevlansmapped3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance. If this object value is not applicable on an MST instance, then the value retrieved for this object for that MST instance will be \-1.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4)
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: stpxsmstinstancecistregionalroot
            
            	Indicates the Bridge Identifier (refer to BridgeId  defined in BRIDGE\-MIB) of CIST (Common and Internal  Spanning Tree) Regional Root for the MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\: str
            
            	**length:** 8
            
            .. attribute:: stpxsmstinstancecistintrootcost
            
            	Indicates the CIST Internal Root Path Cost, i.e., the path cost to the CIST Regional Root as specified by the corresponding stpxSMSTInstanceCISTRegionalRoot for the  MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable.Stpxsmstinstanceentry, self).__init__()

                self.yang_name = "stpxSMSTInstanceEntry"
                self.yang_parent_name = "stpxSMSTInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxsmstinstanceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxsmstinstanceindex', YLeaf(YType.uint32, 'stpxSMSTInstanceIndex')),
                    ('stpxsmstinstancevlansmapped1k2k', YLeaf(YType.str, 'stpxSMSTInstanceVlansMapped1k2k')),
                    ('stpxsmstinstancevlansmapped3k4k', YLeaf(YType.str, 'stpxSMSTInstanceVlansMapped3k4k')),
                    ('stpxsmstinstanceremaininghopcount', YLeaf(YType.int32, 'stpxSMSTInstanceRemainingHopCount')),
                    ('stpxsmstinstancecistregionalroot', YLeaf(YType.str, 'stpxSMSTInstanceCISTRegionalRoot')),
                    ('stpxsmstinstancecistintrootcost', YLeaf(YType.uint32, 'stpxSMSTInstanceCISTIntRootCost')),
                ])
                self.stpxsmstinstanceindex = None
                self.stpxsmstinstancevlansmapped1k2k = None
                self.stpxsmstinstancevlansmapped3k4k = None
                self.stpxsmstinstanceremaininghopcount = None
                self.stpxsmstinstancecistregionalroot = None
                self.stpxsmstinstancecistintrootcost = None
                self._segment_path = lambda: "stpxSMSTInstanceEntry" + "[stpxSMSTInstanceIndex='" + str(self.stpxsmstinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTInstanceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstinstancetable.Stpxsmstinstanceentry, ['stpxsmstinstanceindex', 'stpxsmstinstancevlansmapped1k2k', 'stpxsmstinstancevlansmapped3k4k', 'stpxsmstinstanceremaininghopcount', 'stpxsmstinstancecistregionalroot', 'stpxsmstinstancecistintrootcost'], name, value)


    class Stpxsmstinstanceedittable(Entity):
        """
        This table contains MST instance information in the 
        Edit Buffer. 
        
        This table is only instantiated when the object value
        of  stpxMSTRegionEditBufferStatus has the value of
        acquiredBySnmp(2).
        
        .. attribute:: stpxsmstinstanceeditentry
        
        	A conceptual row containing MST instance information  in the Edit Buffer.  The total number of entries in this table has to be  less than or equal to the object value of stpxSMSTMaxInstances
        	**type**\: list of  		 :py:class:`Stpxsmstinstanceeditentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable, self).__init__()

            self.yang_name = "stpxSMSTInstanceEditTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxSMSTInstanceEditEntry", ("stpxsmstinstanceeditentry", CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry))])
            self._leafs = OrderedDict()

            self.stpxsmstinstanceeditentry = YList(self)
            self._segment_path = lambda: "stpxSMSTInstanceEditTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable, [], name, value)


        class Stpxsmstinstanceeditentry(Entity):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            The total number of entries in this table has to be 
            less than or equal to the object value of stpxSMSTMaxInstances.
            
            .. attribute:: stpxsmstinstanceeditindex  (key)
            
            	The MST instance ID, the value of which is in the range from 0 to stpxSMSTMaxInstanceID.   The instances of this table entry with  stpxSMSTInstanceEditIndex of zero is automatically created by the device and can not modified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstanceeditvlansmap1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  SMST instance 0 by the device. If the bit corresponding  to a VLAN is changed from '0' to '1', then that VLAN will  be automatically removed from the MST instance this VLAN was  previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstanceeditvlansmap3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1' to '0', then that VLAN will be automatically mapped to SMST instance 0 by the device. If the bit corresponding to a VLAN is changed from '0' to '1', then that VLAN will be automatically removed from the MST instance this VLAN was previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstanceeditrowstatus
            
            	This object controls the creation and deletion of a row  in stpxSMSTInstanceEditTable.  When creating an entry in this table, 'createAndGo' method is used and the value of this object is set to 'active'. Deactivation of an 'active' entry is not allowed.  When  deleting an entry in this table, 'destroy' method is used.  Once a row becomes active, value in any other column  within such a row may be modified. When a row is active,  setting the instance of stpxSMSTInstanceEditVlansMap1k2k stpxSMSTInstanceEditVlansMap3k4k for the same MST instance both to the value of zero length can not be allowed
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry, self).__init__()

                self.yang_name = "stpxSMSTInstanceEditEntry"
                self.yang_parent_name = "stpxSMSTInstanceEditTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxsmstinstanceeditindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxsmstinstanceeditindex', YLeaf(YType.uint32, 'stpxSMSTInstanceEditIndex')),
                    ('stpxsmstinstanceeditvlansmap1k2k', YLeaf(YType.str, 'stpxSMSTInstanceEditVlansMap1k2k')),
                    ('stpxsmstinstanceeditvlansmap3k4k', YLeaf(YType.str, 'stpxSMSTInstanceEditVlansMap3k4k')),
                    ('stpxsmstinstanceeditrowstatus', YLeaf(YType.enumeration, 'stpxSMSTInstanceEditRowStatus')),
                ])
                self.stpxsmstinstanceeditindex = None
                self.stpxsmstinstanceeditvlansmap1k2k = None
                self.stpxsmstinstanceeditvlansmap3k4k = None
                self.stpxsmstinstanceeditrowstatus = None
                self._segment_path = lambda: "stpxSMSTInstanceEditEntry" + "[stpxSMSTInstanceEditIndex='" + str(self.stpxsmstinstanceeditindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTInstanceEditTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry, ['stpxsmstinstanceeditindex', 'stpxsmstinstanceeditvlansmap1k2k', 'stpxsmstinstanceeditvlansmap3k4k', 'stpxsmstinstanceeditrowstatus'], name, value)


    class Stpxsmstporttable(Entity):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        This table is only instantiated when the object 
        value of stpxSpanningTreeType is mst(4)
        
        .. attribute:: stpxsmstportentry
        
        	An entry with port information for the MST protocol on a bridge port
        	**type**\: list of  		 :py:class:`Stpxsmstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CISCOSTPEXTENSIONSMIB.Stpxsmstporttable, self).__init__()

            self.yang_name = "stpxSMSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stpxSMSTPortEntry", ("stpxsmstportentry", CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry))])
            self._leafs = OrderedDict()

            self.stpxsmstportentry = YList(self)
            self._segment_path = lambda: "stpxSMSTPortTable"
            self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstporttable, [], name, value)


        class Stpxsmstportentry(Entity):
            """
            An entry with port information for the MST protocol
            on a bridge port.
            
            .. attribute:: stpxsmstportindex  (key)
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxsmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.  dispute \-\- this port, as a designated port, received an         inferior BPDU with a designated role and the         learning bit being set.  rstp \-\- this port is connected to a RSTP bridge or an          MST bridge in a different MST region
            	**type**\:  :py:class:`Stpxsmstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportstatus>`
            
            .. attribute:: stpxsmstportadminhellotime
            
            	The adminitratively configured hello time in hundredth  of seconds on a port for IEEE MST. The granularity  of this timer is 1 second. An agent may return a badValue  error if a set is attempted to a value which is not a  whole number of seconds. This object value of zero means the hello time is not specifically configured on  this port and object value of stpxSMSTPortConfigedHelloTime retrieved for this port will take on the value of  dot1dStpBridgeHelloTime defined in BRIDGE\-MIB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportconfigedhellotime
            
            	Indicates the effective configuration of the hello time on  a port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportoperhellotime
            
            	The operational hello time in hundredth of seconds on a  port for IEEE MST. If this object value is not applicable on a port, then the value retrieved on that port will be \-1
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportadminmstmode
            
            	The desired MST mode of this port.  preStandard \-\- this port is administratively configured to     transmit pre\-standard, i.e. pre IEEE MST, BPDUs.  auto \-\- the BPDU transmission mode of this port is based      on automatic detection of neighbor ports
            	**type**\:  :py:class:`Stpxsmstportadminmstmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportadminmstmode>`
            
            .. attribute:: stpxsmstportopermstmode
            
            	Indicates the current operational MST mode of this port.  unknown \-\- the operational mode is currently unknown.  preStandard \-\- this port is currently operating in      pre\-standard MSTP BPDU transmission mode.  standard \-\- this port is currently operating in IEEE MST      BPDU transmission mode
            	**type**\:  :py:class:`Stpxsmstportopermstmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportopermstmode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry, self).__init__()

                self.yang_name = "stpxSMSTPortEntry"
                self.yang_parent_name = "stpxSMSTPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['stpxsmstportindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stpxsmstportindex', YLeaf(YType.int32, 'stpxSMSTPortIndex')),
                    ('stpxsmstportstatus', YLeaf(YType.bits, 'stpxSMSTPortStatus')),
                    ('stpxsmstportadminhellotime', YLeaf(YType.uint32, 'stpxSMSTPortAdminHelloTime')),
                    ('stpxsmstportconfigedhellotime', YLeaf(YType.uint32, 'stpxSMSTPortConfigedHelloTime')),
                    ('stpxsmstportoperhellotime', YLeaf(YType.int32, 'stpxSMSTPortOperHelloTime')),
                    ('stpxsmstportadminmstmode', YLeaf(YType.enumeration, 'stpxSMSTPortAdminMSTMode')),
                    ('stpxsmstportopermstmode', YLeaf(YType.enumeration, 'stpxSMSTPortOperMSTMode')),
                ])
                self.stpxsmstportindex = None
                self.stpxsmstportstatus = Bits()
                self.stpxsmstportadminhellotime = None
                self.stpxsmstportconfigedhellotime = None
                self.stpxsmstportoperhellotime = None
                self.stpxsmstportadminmstmode = None
                self.stpxsmstportopermstmode = None
                self._segment_path = lambda: "stpxSMSTPortEntry" + "[stpxSMSTPortIndex='" + str(self.stpxsmstportindex) + "']"
                self._absolute_path = lambda: "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSTPEXTENSIONSMIB.Stpxsmstporttable.Stpxsmstportentry, ['stpxsmstportindex', 'stpxsmstportstatus', 'stpxsmstportadminhellotime', 'stpxsmstportconfigedhellotime', 'stpxsmstportoperhellotime', 'stpxsmstportadminmstmode', 'stpxsmstportopermstmode'], name, value)

            class Stpxsmstportadminmstmode(Enum):
                """
                Stpxsmstportadminmstmode (Enum Class)

                The desired MST mode of this port.

                preStandard \-\- this port is administratively configured to

                    transmit pre\-standard, i.e. pre IEEE MST, BPDUs.

                auto \-\- the BPDU transmission mode of this port is based 

                    on automatic detection of neighbor ports.

                .. data:: preStandard = 1

                .. data:: auto = 2

                """

                preStandard = Enum.YLeaf(1, "preStandard")

                auto = Enum.YLeaf(2, "auto")


            class Stpxsmstportopermstmode(Enum):
                """
                Stpxsmstportopermstmode (Enum Class)

                Indicates the current operational MST mode of this port.

                unknown \-\- the operational mode is currently unknown.

                preStandard \-\- this port is currently operating in 

                    pre\-standard MSTP BPDU transmission mode.

                standard \-\- this port is currently operating in IEEE MST 

                    BPDU transmission mode.

                .. data:: unknown = 1

                .. data:: preStandard = 2

                .. data:: standard = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                preStandard = Enum.YLeaf(2, "preStandard")

                standard = Enum.YLeaf(3, "standard")


    def clone_ptr(self):
        self._top_entity = CISCOSTPEXTENSIONSMIB()
        return self._top_entity

