""" CISCO_STP_EXTENSIONS_MIB 

The MIB module for managing Cisco extensions to
the 802.1D Spanning Tree Protocol (STP).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoStpExtensionsMib(Entity):
    """
    
    
    .. attribute:: stpxbackbonefastobjects
    
    	
    	**type**\:   :py:class:`Stpxbackbonefastobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxbackbonefastobjects>`
    
    .. attribute:: stpxbpduskewingobjects
    
    	
    	**type**\:   :py:class:`Stpxbpduskewingobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxbpduskewingobjects>`
    
    .. attribute:: stpxbpduskewingtable
    
    	A table containing a list of the bridge ports for  which a particular Spanning Tree instance has been  detected to have BPDU skewing occurred since the  object value of stpxBpduSkewingDetectionEnable was last changed to true(1).  The agent creates a new entry in this table whenever a port in a particular Spanning Tree instance is  detected to be BPDU skewed since the object value of  stpxBpduSkewingDetectionEnable object is changed to  true(1). The agent deletes all the entries in this  table when the object value of  stpxBpduSkewingDetectionEnable is changed to false(2) or the object value of stpxSpanningTreeType is  changed
    	**type**\:   :py:class:`Stpxbpduskewingtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxbpduskewingtable>`
    
    .. attribute:: stpxfaststartobjects
    
    	
    	**type**\:   :py:class:`Stpxfaststartobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartobjects>`
    
    .. attribute:: stpxfaststartopermodetable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance
    	**type**\:   :py:class:`Stpxfaststartopermodetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartopermodetable>`
    
    .. attribute:: stpxfaststartporttable
    
    	A table containing a list of the bridge ports for which Spanning Tree Port Fast Start can be configured
    	**type**\:   :py:class:`Stpxfaststartporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartporttable>`
    
    .. attribute:: stpxinconsistencytable
    
    	A table containing a list of the ports for which a particular VLAN's Spanning Tree has been found to have an inconsistency.  Two types of inconsistency are discovered\: 1) an inconsistency where two different port types have been plugged together; and 2) an inconsistency where different switches have different PVIDs for the same link
    	**type**\:   :py:class:`Stpxinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxinconsistencytable>`
    
    .. attribute:: stpxloopguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree LoopGuard capability can be configured
    	**type**\:   :py:class:`Stpxloopguardconfigtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopguardconfigtable>`
    
    .. attribute:: stpxloopguardobjects
    
    	
    	**type**\:   :py:class:`Stpxloopguardobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopguardobjects>`
    
    .. attribute:: stpxloopinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found to have a loop\-inconsistency. The agent creates a new entry in this table whenever it detects a new loop\-inconsistency, and deletes entries when/soon after the inconsistency is no longer present
    	**type**\:   :py:class:`Stpxloopinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopinconsistencytable>`
    
    .. attribute:: stpxmistpinstancetable
    
    	This table contains one entry for each instance of MISTP and  it contains stpxMISTPInstanceNumber entries, numbered from 1 to stpxMISTPInstanceNumber.  This table is only instantiated when the value of  stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3)
    	**type**\:   :py:class:`Stpxmistpinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmistpinstancetable>`
    
    .. attribute:: stpxmistpobjects
    
    	
    	**type**\:   :py:class:`Stpxmistpobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmistpobjects>`
    
    .. attribute:: stpxmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer with one entry for each MST instance numbered from 0 to stpxMSTMaxInstanceNumber.   This table is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2).  This table is deprecated and replaced by  stpxSMSTInstanceEditTable
    	**type**\:   :py:class:`Stpxmstinstanceedittable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstinstanceedittable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstinstancetable
    
    	This table contains MST instance information with one entry for an MST instance within the range of  0 to the object value of stpxMSTMaxInstanceNumber.   This table is deprecated and replaced by  stpxSMSTInstanceTable
    	**type**\:   :py:class:`Stpxmstinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstinstancetable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstobjects
    
    	
    	**type**\:   :py:class:`Stpxmstobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstobjects>`
    
    .. attribute:: stpxmstportroletable
    
    	A table containing a list of the bridge ports for a  particular MST instance.  This table is only instantiated  when the stpxSpanningTreeType is mst(4).   This table is deprecated and replaced with  stpxRSTPPortRoleTable
    	**type**\:   :py:class:`Stpxmstportroletable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstportroletable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system
    	**type**\:   :py:class:`Stpxmstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstporttable>`
    
    	**status**\: deprecated
    
    .. attribute:: stpxpvstvlantable
    
    	A list of Virtual LAN entries containing information for Spanning Tree PVST+ protocol.  An entry will exist for each VLAN existing on  the device
    	**type**\:   :py:class:`Stpxpvstvlantable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxpvstvlantable>`
    
    .. attribute:: stpxrootguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree RootGuard capability can be configured
    	**type**\:   :py:class:`Stpxrootguardconfigtable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrootguardconfigtable>`
    
    .. attribute:: stpxrootinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found  to have an root\-inconsistency. The agent creates a new  entry in this table whenever it detects a new  root\-inconsistency, and deletes entries  when/soon after the inconsistency is no longer present
    	**type**\:   :py:class:`Stpxrootinconsistencytable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrootinconsistencytable>`
    
    .. attribute:: stpxrpvstporttable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance. This table is only instantiated when the object value of stpxSpanningTreeType is rapidPvstPlus(5)
    	**type**\:   :py:class:`Stpxrpvstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrpvstporttable>`
    
    .. attribute:: stpxrstpobjects
    
    	
    	**type**\:   :py:class:`Stpxrstpobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpobjects>`
    
    .. attribute:: stpxrstpportroletable
    
    	A table containing a list of the bridge ports for a  particular Spanning Tree instance.  This table is  only instantiated when the stpxSpanningTreeType is mst(4)  or rapidPvstPlus(5)
    	**type**\:   :py:class:`Stpxrstpportroletable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpportroletable>`
    
    .. attribute:: stpxrstpporttable
    
    	A table containing port information for the RSTP  Protocol on all the bridge ports existing in the  system
    	**type**\:   :py:class:`Stpxrstpporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpporttable>`
    
    .. attribute:: stpxsmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer.   This table is only instantiated when the object value of  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2)
    	**type**\:   :py:class:`Stpxsmstinstanceedittable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstinstanceedittable>`
    
    .. attribute:: stpxsmstinstancetable
    
    	This table contains MST instance information for IEEE MST
    	**type**\:   :py:class:`Stpxsmstinstancetable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstinstancetable>`
    
    .. attribute:: stpxsmstobjects
    
    	
    	**type**\:   :py:class:`Stpxsmstobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstobjects>`
    
    .. attribute:: stpxsmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system.  This table is only instantiated when the object  value of stpxSpanningTreeType is mst(4)
    	**type**\:   :py:class:`Stpxsmstporttable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstporttable>`
    
    .. attribute:: stpxspanningtreeobjects
    
    	
    	**type**\:   :py:class:`Stpxspanningtreeobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxspanningtreeobjects>`
    
    .. attribute:: stpxuplinkfastobjects
    
    	
    	**type**\:   :py:class:`Stpxuplinkfastobjects <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxuplinkfastobjects>`
    
    

    """

    _prefix = 'CISCO-STP-EXTENSIONS-MIB'
    _revision = '2013-03-07'

    def __init__(self):
        super(CiscoStpExtensionsMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-STP-EXTENSIONS-MIB"
        self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

        self.stpxbackbonefastobjects = CiscoStpExtensionsMib.Stpxbackbonefastobjects()
        self.stpxbackbonefastobjects.parent = self
        self._children_name_map["stpxbackbonefastobjects"] = "stpxBackboneFastObjects"
        self._children_yang_names.add("stpxBackboneFastObjects")

        self.stpxbpduskewingobjects = CiscoStpExtensionsMib.Stpxbpduskewingobjects()
        self.stpxbpduskewingobjects.parent = self
        self._children_name_map["stpxbpduskewingobjects"] = "stpxBpduSkewingObjects"
        self._children_yang_names.add("stpxBpduSkewingObjects")

        self.stpxbpduskewingtable = CiscoStpExtensionsMib.Stpxbpduskewingtable()
        self.stpxbpduskewingtable.parent = self
        self._children_name_map["stpxbpduskewingtable"] = "stpxBpduSkewingTable"
        self._children_yang_names.add("stpxBpduSkewingTable")

        self.stpxfaststartobjects = CiscoStpExtensionsMib.Stpxfaststartobjects()
        self.stpxfaststartobjects.parent = self
        self._children_name_map["stpxfaststartobjects"] = "stpxFastStartObjects"
        self._children_yang_names.add("stpxFastStartObjects")

        self.stpxfaststartopermodetable = CiscoStpExtensionsMib.Stpxfaststartopermodetable()
        self.stpxfaststartopermodetable.parent = self
        self._children_name_map["stpxfaststartopermodetable"] = "stpxFastStartOperModeTable"
        self._children_yang_names.add("stpxFastStartOperModeTable")

        self.stpxfaststartporttable = CiscoStpExtensionsMib.Stpxfaststartporttable()
        self.stpxfaststartporttable.parent = self
        self._children_name_map["stpxfaststartporttable"] = "stpxFastStartPortTable"
        self._children_yang_names.add("stpxFastStartPortTable")

        self.stpxinconsistencytable = CiscoStpExtensionsMib.Stpxinconsistencytable()
        self.stpxinconsistencytable.parent = self
        self._children_name_map["stpxinconsistencytable"] = "stpxInconsistencyTable"
        self._children_yang_names.add("stpxInconsistencyTable")

        self.stpxloopguardconfigtable = CiscoStpExtensionsMib.Stpxloopguardconfigtable()
        self.stpxloopguardconfigtable.parent = self
        self._children_name_map["stpxloopguardconfigtable"] = "stpxLoopGuardConfigTable"
        self._children_yang_names.add("stpxLoopGuardConfigTable")

        self.stpxloopguardobjects = CiscoStpExtensionsMib.Stpxloopguardobjects()
        self.stpxloopguardobjects.parent = self
        self._children_name_map["stpxloopguardobjects"] = "stpxLoopGuardObjects"
        self._children_yang_names.add("stpxLoopGuardObjects")

        self.stpxloopinconsistencytable = CiscoStpExtensionsMib.Stpxloopinconsistencytable()
        self.stpxloopinconsistencytable.parent = self
        self._children_name_map["stpxloopinconsistencytable"] = "stpxLoopInconsistencyTable"
        self._children_yang_names.add("stpxLoopInconsistencyTable")

        self.stpxmistpinstancetable = CiscoStpExtensionsMib.Stpxmistpinstancetable()
        self.stpxmistpinstancetable.parent = self
        self._children_name_map["stpxmistpinstancetable"] = "stpxMISTPInstanceTable"
        self._children_yang_names.add("stpxMISTPInstanceTable")

        self.stpxmistpobjects = CiscoStpExtensionsMib.Stpxmistpobjects()
        self.stpxmistpobjects.parent = self
        self._children_name_map["stpxmistpobjects"] = "stpxMISTPObjects"
        self._children_yang_names.add("stpxMISTPObjects")

        self.stpxmstinstanceedittable = CiscoStpExtensionsMib.Stpxmstinstanceedittable()
        self.stpxmstinstanceedittable.parent = self
        self._children_name_map["stpxmstinstanceedittable"] = "stpxMSTInstanceEditTable"
        self._children_yang_names.add("stpxMSTInstanceEditTable")

        self.stpxmstinstancetable = CiscoStpExtensionsMib.Stpxmstinstancetable()
        self.stpxmstinstancetable.parent = self
        self._children_name_map["stpxmstinstancetable"] = "stpxMSTInstanceTable"
        self._children_yang_names.add("stpxMSTInstanceTable")

        self.stpxmstobjects = CiscoStpExtensionsMib.Stpxmstobjects()
        self.stpxmstobjects.parent = self
        self._children_name_map["stpxmstobjects"] = "stpxMSTObjects"
        self._children_yang_names.add("stpxMSTObjects")

        self.stpxmstportroletable = CiscoStpExtensionsMib.Stpxmstportroletable()
        self.stpxmstportroletable.parent = self
        self._children_name_map["stpxmstportroletable"] = "stpxMSTPortRoleTable"
        self._children_yang_names.add("stpxMSTPortRoleTable")

        self.stpxmstporttable = CiscoStpExtensionsMib.Stpxmstporttable()
        self.stpxmstporttable.parent = self
        self._children_name_map["stpxmstporttable"] = "stpxMSTPortTable"
        self._children_yang_names.add("stpxMSTPortTable")

        self.stpxpvstvlantable = CiscoStpExtensionsMib.Stpxpvstvlantable()
        self.stpxpvstvlantable.parent = self
        self._children_name_map["stpxpvstvlantable"] = "stpxPVSTVlanTable"
        self._children_yang_names.add("stpxPVSTVlanTable")

        self.stpxrootguardconfigtable = CiscoStpExtensionsMib.Stpxrootguardconfigtable()
        self.stpxrootguardconfigtable.parent = self
        self._children_name_map["stpxrootguardconfigtable"] = "stpxRootGuardConfigTable"
        self._children_yang_names.add("stpxRootGuardConfigTable")

        self.stpxrootinconsistencytable = CiscoStpExtensionsMib.Stpxrootinconsistencytable()
        self.stpxrootinconsistencytable.parent = self
        self._children_name_map["stpxrootinconsistencytable"] = "stpxRootInconsistencyTable"
        self._children_yang_names.add("stpxRootInconsistencyTable")

        self.stpxrpvstporttable = CiscoStpExtensionsMib.Stpxrpvstporttable()
        self.stpxrpvstporttable.parent = self
        self._children_name_map["stpxrpvstporttable"] = "stpxRPVSTPortTable"
        self._children_yang_names.add("stpxRPVSTPortTable")

        self.stpxrstpobjects = CiscoStpExtensionsMib.Stpxrstpobjects()
        self.stpxrstpobjects.parent = self
        self._children_name_map["stpxrstpobjects"] = "stpxRSTPObjects"
        self._children_yang_names.add("stpxRSTPObjects")

        self.stpxrstpportroletable = CiscoStpExtensionsMib.Stpxrstpportroletable()
        self.stpxrstpportroletable.parent = self
        self._children_name_map["stpxrstpportroletable"] = "stpxRSTPPortRoleTable"
        self._children_yang_names.add("stpxRSTPPortRoleTable")

        self.stpxrstpporttable = CiscoStpExtensionsMib.Stpxrstpporttable()
        self.stpxrstpporttable.parent = self
        self._children_name_map["stpxrstpporttable"] = "stpxRSTPPortTable"
        self._children_yang_names.add("stpxRSTPPortTable")

        self.stpxsmstinstanceedittable = CiscoStpExtensionsMib.Stpxsmstinstanceedittable()
        self.stpxsmstinstanceedittable.parent = self
        self._children_name_map["stpxsmstinstanceedittable"] = "stpxSMSTInstanceEditTable"
        self._children_yang_names.add("stpxSMSTInstanceEditTable")

        self.stpxsmstinstancetable = CiscoStpExtensionsMib.Stpxsmstinstancetable()
        self.stpxsmstinstancetable.parent = self
        self._children_name_map["stpxsmstinstancetable"] = "stpxSMSTInstanceTable"
        self._children_yang_names.add("stpxSMSTInstanceTable")

        self.stpxsmstobjects = CiscoStpExtensionsMib.Stpxsmstobjects()
        self.stpxsmstobjects.parent = self
        self._children_name_map["stpxsmstobjects"] = "stpxSMSTObjects"
        self._children_yang_names.add("stpxSMSTObjects")

        self.stpxsmstporttable = CiscoStpExtensionsMib.Stpxsmstporttable()
        self.stpxsmstporttable.parent = self
        self._children_name_map["stpxsmstporttable"] = "stpxSMSTPortTable"
        self._children_yang_names.add("stpxSMSTPortTable")

        self.stpxspanningtreeobjects = CiscoStpExtensionsMib.Stpxspanningtreeobjects()
        self.stpxspanningtreeobjects.parent = self
        self._children_name_map["stpxspanningtreeobjects"] = "stpxSpanningTreeObjects"
        self._children_yang_names.add("stpxSpanningTreeObjects")

        self.stpxuplinkfastobjects = CiscoStpExtensionsMib.Stpxuplinkfastobjects()
        self.stpxuplinkfastobjects.parent = self
        self._children_name_map["stpxuplinkfastobjects"] = "stpxUplinkFastObjects"
        self._children_yang_names.add("stpxUplinkFastObjects")


    class Stpxuplinkfastobjects(Entity):
        """
        
        
        .. attribute:: stpxuplinkfastenabled
        
        	An indication of whether the UplinkFast capability is administratively enabled on the device.  If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is  mst(4), then this object is not instantiated
        	**type**\:  bool
        
        .. attribute:: stpxuplinkfastoperenabled
        
        	An indication of whether the UplinkFast capability is  operationally enabled on the device
        	**type**\:  bool
        
        .. attribute:: stpxuplinkfasttransitions
        
        	The cumulative number of UplinkFast transitions (from the STP 'Blocking' state directly to the STP 'Forwarding' state).  All transitions are included in this counter, irrespective of the instance of the Spanning Tree  Protocol on which they occur.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: transitions
        
        .. attribute:: stpxuplinkstationlearningframes
        
        	The cumulative number of station\-learning frames generated due to UplinkFast transitions.  All generated station\-learning frames are included in this counter, irrespective of the instance of the Spanning Tree Protocol on which the UplinkFast transition occurred.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: frames
        
        .. attribute:: stpxuplinkstationlearninggenrate
        
        	The maximum number of station\-learning frames that this device will generate in each 100 milli\-second period after a UplinkFast transition.  By configuring this object, the network administrator can limit the rate at which station\-learning frames are generated.    If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is mst(4), then this object is not instantiated
        	**type**\:  int
        
        	**range:** 0..32000
        
        	**units**\: frames
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxuplinkfastobjects, self).__init__()

            self.yang_name = "stpxUplinkFastObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxuplinkfastenabled = YLeaf(YType.boolean, "stpxUplinkFastEnabled")

            self.stpxuplinkfastoperenabled = YLeaf(YType.boolean, "stpxUplinkFastOperEnabled")

            self.stpxuplinkfasttransitions = YLeaf(YType.uint32, "stpxUplinkFastTransitions")

            self.stpxuplinkstationlearningframes = YLeaf(YType.uint32, "stpxUplinkStationLearningFrames")

            self.stpxuplinkstationlearninggenrate = YLeaf(YType.int32, "stpxUplinkStationLearningGenRate")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxuplinkfastenabled",
                            "stpxuplinkfastoperenabled",
                            "stpxuplinkfasttransitions",
                            "stpxuplinkstationlearningframes",
                            "stpxuplinkstationlearninggenrate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxuplinkfastobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxuplinkfastobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.stpxuplinkfastenabled.is_set or
                self.stpxuplinkfastoperenabled.is_set or
                self.stpxuplinkfasttransitions.is_set or
                self.stpxuplinkstationlearningframes.is_set or
                self.stpxuplinkstationlearninggenrate.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxuplinkfastenabled.yfilter != YFilter.not_set or
                self.stpxuplinkfastoperenabled.yfilter != YFilter.not_set or
                self.stpxuplinkfasttransitions.yfilter != YFilter.not_set or
                self.stpxuplinkstationlearningframes.yfilter != YFilter.not_set or
                self.stpxuplinkstationlearninggenrate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxUplinkFastObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxuplinkfastenabled.is_set or self.stpxuplinkfastenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxuplinkfastenabled.get_name_leafdata())
            if (self.stpxuplinkfastoperenabled.is_set or self.stpxuplinkfastoperenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxuplinkfastoperenabled.get_name_leafdata())
            if (self.stpxuplinkfasttransitions.is_set or self.stpxuplinkfasttransitions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxuplinkfasttransitions.get_name_leafdata())
            if (self.stpxuplinkstationlearningframes.is_set or self.stpxuplinkstationlearningframes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxuplinkstationlearningframes.get_name_leafdata())
            if (self.stpxuplinkstationlearninggenrate.is_set or self.stpxuplinkstationlearninggenrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxuplinkstationlearninggenrate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxUplinkFastEnabled" or name == "stpxUplinkFastOperEnabled" or name == "stpxUplinkFastTransitions" or name == "stpxUplinkStationLearningFrames" or name == "stpxUplinkStationLearningGenRate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxUplinkFastEnabled"):
                self.stpxuplinkfastenabled = value
                self.stpxuplinkfastenabled.value_namespace = name_space
                self.stpxuplinkfastenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxUplinkFastOperEnabled"):
                self.stpxuplinkfastoperenabled = value
                self.stpxuplinkfastoperenabled.value_namespace = name_space
                self.stpxuplinkfastoperenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxUplinkFastTransitions"):
                self.stpxuplinkfasttransitions = value
                self.stpxuplinkfasttransitions.value_namespace = name_space
                self.stpxuplinkfasttransitions.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxUplinkStationLearningFrames"):
                self.stpxuplinkstationlearningframes = value
                self.stpxuplinkstationlearningframes.value_namespace = name_space
                self.stpxuplinkstationlearningframes.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxUplinkStationLearningGenRate"):
                self.stpxuplinkstationlearninggenrate = value
                self.stpxuplinkstationlearninggenrate.value_namespace = name_space
                self.stpxuplinkstationlearninggenrate.value_namespace_prefix = name_space_prefix


    class Stpxbackbonefastobjects(Entity):
        """
        
        
        .. attribute:: stpxbackbonefastenabled
        
        	An indication of whether the BackboneFast capability is administratively enabled on the device
        	**type**\:  bool
        
        .. attribute:: stpxbackbonefastininferiorbpdus
        
        	The number of inferior BPDUs received by the switch  since the stpxBackboneFastOperEnabled has become true(1). If the value of  stpxBackboneFastOperEnabled is false(2), then this  mib object will have a value of 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastinrlqrequestpdus
        
        	The number of Root Link Query request PDUs received by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastinrlqresponsepdus
        
        	The number of Root Link Query response PDUs received by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoperenabled
        
        	An indication of whether the BackboneFast capability is operationally enabled on the device
        	**type**\:  bool
        
        .. attribute:: stpxbackbonefastoutrlqrequestpdus
        
        	The number of Root Link Query request PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoutrlqresponsepdus
        
        	The number of Root Link Query response PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxbackbonefastobjects, self).__init__()

            self.yang_name = "stpxBackboneFastObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxbackbonefastenabled = YLeaf(YType.boolean, "stpxBackboneFastEnabled")

            self.stpxbackbonefastininferiorbpdus = YLeaf(YType.uint32, "stpxBackboneFastInInferiorBPDUs")

            self.stpxbackbonefastinrlqrequestpdus = YLeaf(YType.uint32, "stpxBackboneFastInRLQRequestPDUs")

            self.stpxbackbonefastinrlqresponsepdus = YLeaf(YType.uint32, "stpxBackboneFastInRLQResponsePDUs")

            self.stpxbackbonefastoperenabled = YLeaf(YType.boolean, "stpxBackboneFastOperEnabled")

            self.stpxbackbonefastoutrlqrequestpdus = YLeaf(YType.uint32, "stpxBackboneFastOutRLQRequestPDUs")

            self.stpxbackbonefastoutrlqresponsepdus = YLeaf(YType.uint32, "stpxBackboneFastOutRLQResponsePDUs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxbackbonefastenabled",
                            "stpxbackbonefastininferiorbpdus",
                            "stpxbackbonefastinrlqrequestpdus",
                            "stpxbackbonefastinrlqresponsepdus",
                            "stpxbackbonefastoperenabled",
                            "stpxbackbonefastoutrlqrequestpdus",
                            "stpxbackbonefastoutrlqresponsepdus") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxbackbonefastobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxbackbonefastobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.stpxbackbonefastenabled.is_set or
                self.stpxbackbonefastininferiorbpdus.is_set or
                self.stpxbackbonefastinrlqrequestpdus.is_set or
                self.stpxbackbonefastinrlqresponsepdus.is_set or
                self.stpxbackbonefastoperenabled.is_set or
                self.stpxbackbonefastoutrlqrequestpdus.is_set or
                self.stpxbackbonefastoutrlqresponsepdus.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxbackbonefastenabled.yfilter != YFilter.not_set or
                self.stpxbackbonefastininferiorbpdus.yfilter != YFilter.not_set or
                self.stpxbackbonefastinrlqrequestpdus.yfilter != YFilter.not_set or
                self.stpxbackbonefastinrlqresponsepdus.yfilter != YFilter.not_set or
                self.stpxbackbonefastoperenabled.yfilter != YFilter.not_set or
                self.stpxbackbonefastoutrlqrequestpdus.yfilter != YFilter.not_set or
                self.stpxbackbonefastoutrlqresponsepdus.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxBackboneFastObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxbackbonefastenabled.is_set or self.stpxbackbonefastenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastenabled.get_name_leafdata())
            if (self.stpxbackbonefastininferiorbpdus.is_set or self.stpxbackbonefastininferiorbpdus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastininferiorbpdus.get_name_leafdata())
            if (self.stpxbackbonefastinrlqrequestpdus.is_set or self.stpxbackbonefastinrlqrequestpdus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastinrlqrequestpdus.get_name_leafdata())
            if (self.stpxbackbonefastinrlqresponsepdus.is_set or self.stpxbackbonefastinrlqresponsepdus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastinrlqresponsepdus.get_name_leafdata())
            if (self.stpxbackbonefastoperenabled.is_set or self.stpxbackbonefastoperenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastoperenabled.get_name_leafdata())
            if (self.stpxbackbonefastoutrlqrequestpdus.is_set or self.stpxbackbonefastoutrlqrequestpdus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastoutrlqrequestpdus.get_name_leafdata())
            if (self.stpxbackbonefastoutrlqresponsepdus.is_set or self.stpxbackbonefastoutrlqresponsepdus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbackbonefastoutrlqresponsepdus.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxBackboneFastEnabled" or name == "stpxBackboneFastInInferiorBPDUs" or name == "stpxBackboneFastInRLQRequestPDUs" or name == "stpxBackboneFastInRLQResponsePDUs" or name == "stpxBackboneFastOperEnabled" or name == "stpxBackboneFastOutRLQRequestPDUs" or name == "stpxBackboneFastOutRLQResponsePDUs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxBackboneFastEnabled"):
                self.stpxbackbonefastenabled = value
                self.stpxbackbonefastenabled.value_namespace = name_space
                self.stpxbackbonefastenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastInInferiorBPDUs"):
                self.stpxbackbonefastininferiorbpdus = value
                self.stpxbackbonefastininferiorbpdus.value_namespace = name_space
                self.stpxbackbonefastininferiorbpdus.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastInRLQRequestPDUs"):
                self.stpxbackbonefastinrlqrequestpdus = value
                self.stpxbackbonefastinrlqrequestpdus.value_namespace = name_space
                self.stpxbackbonefastinrlqrequestpdus.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastInRLQResponsePDUs"):
                self.stpxbackbonefastinrlqresponsepdus = value
                self.stpxbackbonefastinrlqresponsepdus.value_namespace = name_space
                self.stpxbackbonefastinrlqresponsepdus.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastOperEnabled"):
                self.stpxbackbonefastoperenabled = value
                self.stpxbackbonefastoperenabled.value_namespace = name_space
                self.stpxbackbonefastoperenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastOutRLQRequestPDUs"):
                self.stpxbackbonefastoutrlqrequestpdus = value
                self.stpxbackbonefastoutrlqrequestpdus.value_namespace = name_space
                self.stpxbackbonefastoutrlqrequestpdus.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxBackboneFastOutRLQResponsePDUs"):
                self.stpxbackbonefastoutrlqresponsepdus = value
                self.stpxbackbonefastoutrlqresponsepdus.value_namespace = name_space
                self.stpxbackbonefastoutrlqresponsepdus.value_namespace_prefix = name_space_prefix


    class Stpxspanningtreeobjects(Entity):
        """
        
        
        .. attribute:: stpxextendedsysidadminenabled
        
        	Indicates whether Extended System ID feature  is administratively enabled on the device or not
        	**type**\:  bool
        
        .. attribute:: stpxextendedsysidoperenabled
        
        	Indicates whether Extended System ID feature  is operationaly enabled on the device or not.  If the value of this object is true(1), then the accepted values for dot1dStpPriority in BRIDGE\-MIB should be multiples of 4096 plus bridge instance ID, such as VlanIndex. Changing this object value might cause the values of dot1dBaseBridgeAddress and dot1dStpPriority in BRIDGE\-MIB to be changed also
        	**type**\:  bool
        
        .. attribute:: stpxnotificationenable
        
        	Indicates whether a specified notification is enabled or not. If a bit corresponding to a notification is set to 1, then  the specified notification can be generated.  newRoot \-\- the newRoot notification as defined in BRIDGE\-MIB.  topologyChange \-\- the topologyChange notification as                   defined in BRIDGE\-MIB.  inconsistency \-\- the stpxInconsistencyUpdate notification.  rootInconsistency \-\- the stpxRootInconsistencyUpdate                       notification.  loopInconsistency \-\- the stpxLoopInconsistencyUpdate                       notification
        	**type**\:   :py:class:`Stpxnotificationenable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxspanningtreeobjects.Stpxnotificationenable>`
        
        .. attribute:: stpxspanningtreepathcostmode
        
        	Indicates the administrative  spanning tree path cost mode  configured on device
        	**type**\:   :py:class:`Stpxspanningtreepathcostmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxspanningtreeobjects.Stpxspanningtreepathcostmode>`
        
        .. attribute:: stpxspanningtreepathcostopermode
        
        	Indicate the operational spanning tree path cost mode on device. This mode applies to all instances of the Spanning Tree protocol running on the device.   When the value of this MIB object gets changed, the path cost of all ports will be reassigned to the default path cost values based on the new spanning tree path cost mode and the ports' speed.  When the value of this MIB object is long(2), the stpxLongStpPortPathCost MIB object must be used in order to retrieve/configure the spanning tree port path cost as a 32 bits value. The set operation on dot1dStpPortPathCost in BRIDGE\-MIB will be rejected. While retrieving the value of dot1dStpPortPathCost, the maximum value of 65535 will be returned if the value of stpxLongStpPortPathCost for the same instance exceeds 65535.  When the value of this MIB object is short(1), the dot1dStpPortPathCost in BRIDGE\-MIB must be used
        	**type**\:   :py:class:`Stpxspanningtreepathcostopermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxspanningtreeobjects.Stpxspanningtreepathcostopermode>`
        
        .. attribute:: stpxspanningtreetype
        
        	The actual mode of spanning tree protocol runs on the  device. It can be one of the following\:  pvstPlus \-\- PVST+ (Per VLAN Spanning Tree+ Protocol).  mistp \-\- MISTP (Multi Instance Spanning Tree Protocol).  mistpPvstPlus \-\-  MISTP with the tunneling scheme                      enabled for PVST+.  mst \-\- IEEE 802.1s Multiple Spanning Tree (MST)        with IEEE 802.1w Rapid Spanning Tree Protocol        (RSTP).  rapidPvstPlus \-\- IEEE 802.1w Rapid Spanning Tree          Protocol (RSTP) for all vlans in PVST+.  When the value of this MIB object gets changed, the  network connectivity would be affected and the  connectivity to this device would also be lost  temporarily
        	**type**\:   :py:class:`Stpxspanningtreetype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxspanningtreeobjects.Stpxspanningtreetype>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxspanningtreeobjects, self).__init__()

            self.yang_name = "stpxSpanningTreeObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxextendedsysidadminenabled = YLeaf(YType.boolean, "stpxExtendedSysIDAdminEnabled")

            self.stpxextendedsysidoperenabled = YLeaf(YType.boolean, "stpxExtendedSysIDOperEnabled")

            self.stpxnotificationenable = YLeaf(YType.bits, "stpxNotificationEnable")

            self.stpxspanningtreepathcostmode = YLeaf(YType.enumeration, "stpxSpanningTreePathCostMode")

            self.stpxspanningtreepathcostopermode = YLeaf(YType.enumeration, "stpxSpanningTreePathCostOperMode")

            self.stpxspanningtreetype = YLeaf(YType.enumeration, "stpxSpanningTreeType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxextendedsysidadminenabled",
                            "stpxextendedsysidoperenabled",
                            "stpxnotificationenable",
                            "stpxspanningtreepathcostmode",
                            "stpxspanningtreepathcostopermode",
                            "stpxspanningtreetype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxspanningtreeobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxspanningtreeobjects, self).__setattr__(name, value)

        class Stpxspanningtreepathcostmode(Enum):
            """
            Stpxspanningtreepathcostmode

            Indicates the administrative  spanning tree path cost mode 

            configured on device.

            .. data:: short = 1

            .. data:: long = 2

            """

            short = Enum.YLeaf(1, "short")

            long = Enum.YLeaf(2, "long")


        class Stpxspanningtreepathcostopermode(Enum):
            """
            Stpxspanningtreepathcostopermode

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
            Stpxspanningtreetype

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


        def has_data(self):
            return (
                self.stpxextendedsysidadminenabled.is_set or
                self.stpxextendedsysidoperenabled.is_set or
                self.stpxnotificationenable.is_set or
                self.stpxspanningtreepathcostmode.is_set or
                self.stpxspanningtreepathcostopermode.is_set or
                self.stpxspanningtreetype.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxextendedsysidadminenabled.yfilter != YFilter.not_set or
                self.stpxextendedsysidoperenabled.yfilter != YFilter.not_set or
                self.stpxnotificationenable.yfilter != YFilter.not_set or
                self.stpxspanningtreepathcostmode.yfilter != YFilter.not_set or
                self.stpxspanningtreepathcostopermode.yfilter != YFilter.not_set or
                self.stpxspanningtreetype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxSpanningTreeObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxextendedsysidadminenabled.is_set or self.stpxextendedsysidadminenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxextendedsysidadminenabled.get_name_leafdata())
            if (self.stpxextendedsysidoperenabled.is_set or self.stpxextendedsysidoperenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxextendedsysidoperenabled.get_name_leafdata())
            if (self.stpxnotificationenable.is_set or self.stpxnotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxnotificationenable.get_name_leafdata())
            if (self.stpxspanningtreepathcostmode.is_set or self.stpxspanningtreepathcostmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxspanningtreepathcostmode.get_name_leafdata())
            if (self.stpxspanningtreepathcostopermode.is_set or self.stpxspanningtreepathcostopermode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxspanningtreepathcostopermode.get_name_leafdata())
            if (self.stpxspanningtreetype.is_set or self.stpxspanningtreetype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxspanningtreetype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxExtendedSysIDAdminEnabled" or name == "stpxExtendedSysIDOperEnabled" or name == "stpxNotificationEnable" or name == "stpxSpanningTreePathCostMode" or name == "stpxSpanningTreePathCostOperMode" or name == "stpxSpanningTreeType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxExtendedSysIDAdminEnabled"):
                self.stpxextendedsysidadminenabled = value
                self.stpxextendedsysidadminenabled.value_namespace = name_space
                self.stpxextendedsysidadminenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxExtendedSysIDOperEnabled"):
                self.stpxextendedsysidoperenabled = value
                self.stpxextendedsysidoperenabled.value_namespace = name_space
                self.stpxextendedsysidoperenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxNotificationEnable"):
                self.stpxnotificationenable[value] = True
            if(value_path == "stpxSpanningTreePathCostMode"):
                self.stpxspanningtreepathcostmode = value
                self.stpxspanningtreepathcostmode.value_namespace = name_space
                self.stpxspanningtreepathcostmode.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSpanningTreePathCostOperMode"):
                self.stpxspanningtreepathcostopermode = value
                self.stpxspanningtreepathcostopermode.value_namespace = name_space
                self.stpxspanningtreepathcostopermode.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSpanningTreeType"):
                self.stpxspanningtreetype = value
                self.stpxspanningtreetype.value_namespace = name_space
                self.stpxspanningtreetype.value_namespace_prefix = name_space_prefix


    class Stpxmistpobjects(Entity):
        """
        
        
        .. attribute:: stpxmistpinstancenumber
        
        	The number of MISTP instances, that are supported by the device  when the value of stpxSpanningTreeType is either mistp(2) or mistpPvstPlus(3)
        	**type**\:  int
        
        	**range:** 1..256
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmistpobjects, self).__init__()

            self.yang_name = "stpxMISTPObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmistpinstancenumber = YLeaf(YType.int32, "stpxMISTPInstanceNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxmistpinstancenumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxmistpobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmistpobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.stpxmistpinstancenumber.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxmistpinstancenumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMISTPObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxmistpinstancenumber.is_set or self.stpxmistpinstancenumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmistpinstancenumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMISTPInstanceNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxMISTPInstanceNumber"):
                self.stpxmistpinstancenumber = value
                self.stpxmistpinstancenumber.value_namespace = name_space
                self.stpxmistpinstancenumber.value_namespace_prefix = name_space_prefix


    class Stpxloopguardobjects(Entity):
        """
        
        
        .. attribute:: stpxloopguardglobaldefaultmode
        
        	Indicates the global default config mode of LoopGuard  feature on the device
        	**type**\:   :py:class:`Stpxloopguardglobaldefaultmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopguardobjects.Stpxloopguardglobaldefaultmode>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxloopguardobjects, self).__init__()

            self.yang_name = "stpxLoopGuardObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxloopguardglobaldefaultmode = YLeaf(YType.enumeration, "stpxLoopGuardGlobalDefaultMode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxloopguardglobaldefaultmode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxloopguardobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxloopguardobjects, self).__setattr__(name, value)

        class Stpxloopguardglobaldefaultmode(Enum):
            """
            Stpxloopguardglobaldefaultmode

            Indicates the global default config mode of LoopGuard 

            feature on the device.

            .. data:: enable = 1

            .. data:: disable = 2

            """

            enable = Enum.YLeaf(1, "enable")

            disable = Enum.YLeaf(2, "disable")


        def has_data(self):
            return self.stpxloopguardglobaldefaultmode.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxloopguardglobaldefaultmode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxLoopGuardObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxloopguardglobaldefaultmode.is_set or self.stpxloopguardglobaldefaultmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxloopguardglobaldefaultmode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxLoopGuardGlobalDefaultMode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxLoopGuardGlobalDefaultMode"):
                self.stpxloopguardglobaldefaultmode = value
                self.stpxloopguardglobaldefaultmode.value_namespace = name_space
                self.stpxloopguardglobaldefaultmode.value_namespace_prefix = name_space_prefix


    class Stpxfaststartobjects(Entity):
        """
        
        
        .. attribute:: stpxfaststartbpdufilterenable
        
        	Indicates the global default mode of the Bpdu  Filter feature on the device.  On platforms that does not support per port  Bpdu Filter configuration as indicated by the object stpxFastStartPortBpduFilterMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then no BPDUs will be  transmitted on this port
        	**type**\:  bool
        
        .. attribute:: stpxfaststartbpduguardenable
        
        	Indicates the global default mode of the Bpdu Guard feature on the device.  On platforms that does not support per port  Bpdu Guard configuration as indicated by the object stpxFastStartPortBpduGuardMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then that port will be  immediately disabled when the system receives a BPDU from that port
        	**type**\:  bool
        
        .. attribute:: stpxfaststartglobaldefaultmode
        
        	Indicates the global default mode of the Fast  Start feature on the device
        	**type**\:   :py:class:`Stpxfaststartglobaldefaultmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartobjects.Stpxfaststartglobaldefaultmode>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxfaststartobjects, self).__init__()

            self.yang_name = "stpxFastStartObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxfaststartbpdufilterenable = YLeaf(YType.boolean, "stpxFastStartBpduFilterEnable")

            self.stpxfaststartbpduguardenable = YLeaf(YType.boolean, "stpxFastStartBpduGuardEnable")

            self.stpxfaststartglobaldefaultmode = YLeaf(YType.enumeration, "stpxFastStartGlobalDefaultMode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxfaststartbpdufilterenable",
                            "stpxfaststartbpduguardenable",
                            "stpxfaststartglobaldefaultmode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxfaststartobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxfaststartobjects, self).__setattr__(name, value)

        class Stpxfaststartglobaldefaultmode(Enum):
            """
            Stpxfaststartglobaldefaultmode

            Indicates the global default mode of the Fast 

            Start feature on the device.

            .. data:: enable = 1

            .. data:: disable = 2

            """

            enable = Enum.YLeaf(1, "enable")

            disable = Enum.YLeaf(2, "disable")


        def has_data(self):
            return (
                self.stpxfaststartbpdufilterenable.is_set or
                self.stpxfaststartbpduguardenable.is_set or
                self.stpxfaststartglobaldefaultmode.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxfaststartbpdufilterenable.yfilter != YFilter.not_set or
                self.stpxfaststartbpduguardenable.yfilter != YFilter.not_set or
                self.stpxfaststartglobaldefaultmode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxFastStartObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxfaststartbpdufilterenable.is_set or self.stpxfaststartbpdufilterenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxfaststartbpdufilterenable.get_name_leafdata())
            if (self.stpxfaststartbpduguardenable.is_set or self.stpxfaststartbpduguardenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxfaststartbpduguardenable.get_name_leafdata())
            if (self.stpxfaststartglobaldefaultmode.is_set or self.stpxfaststartglobaldefaultmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxfaststartglobaldefaultmode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxFastStartBpduFilterEnable" or name == "stpxFastStartBpduGuardEnable" or name == "stpxFastStartGlobalDefaultMode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxFastStartBpduFilterEnable"):
                self.stpxfaststartbpdufilterenable = value
                self.stpxfaststartbpdufilterenable.value_namespace = name_space
                self.stpxfaststartbpdufilterenable.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxFastStartBpduGuardEnable"):
                self.stpxfaststartbpduguardenable = value
                self.stpxfaststartbpduguardenable.value_namespace = name_space
                self.stpxfaststartbpduguardenable.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxFastStartGlobalDefaultMode"):
                self.stpxfaststartglobaldefaultmode = value
                self.stpxfaststartglobaldefaultmode.value_namespace = name_space
                self.stpxfaststartglobaldefaultmode.value_namespace_prefix = name_space_prefix


    class Stpxbpduskewingobjects(Entity):
        """
        
        
        .. attribute:: stpxbpduskewingdetectionenable
        
        	Indicates whether BPDU skewing detection feature is enabled or not on the system. If this object has the value of true(1), then the system will detect whether BPDUs received by any port on any Spanning  Tree instance are processed at an interval longer than the object value of dot1dStpHelloTime in the BIRDGE\-MIB of the Spanning Tree instance
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxbpduskewingobjects, self).__init__()

            self.yang_name = "stpxBpduSkewingObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxbpduskewingdetectionenable = YLeaf(YType.boolean, "stpxBpduSkewingDetectionEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxbpduskewingdetectionenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxbpduskewingobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxbpduskewingobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.stpxbpduskewingdetectionenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxbpduskewingdetectionenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxBpduSkewingObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxbpduskewingdetectionenable.is_set or self.stpxbpduskewingdetectionenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxbpduskewingdetectionenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxBpduSkewingDetectionEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxBpduSkewingDetectionEnable"):
                self.stpxbpduskewingdetectionenable = value
                self.stpxbpduskewingdetectionenable.value_namespace = name_space
                self.stpxbpduskewingdetectionenable.value_namespace_prefix = name_space_prefix


    class Stpxmstobjects(Entity):
        """
        
        
        .. attribute:: stpxmstmaxhopcount
        
        	The maximum number of hops for the MST region.   This object will take on value of 40 if the object value of stpxSMSTMaxHopCount is greater than 40.  This object is deprecated and replaced by stpxSMSTMaxHopCount
        	**type**\:  int
        
        	**range:** 1..40
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstmaxinstancenumber
        
        	The maximum MST (Multiple Spanning Tree) instance id,  that can be supported by the device for Cisco proprietary implementation of the MST Protocol.  This object is deprecated and replaced by  stpxSMSTMaxInstanceID
        	**type**\:  int
        
        	**range:** 1..256
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstregioneditbufferoperation
        
        	Indicates the operation that is performed on the Region  Config Edit Buffer.  other \-\-   none of the following operations.    acquire \-\- acquire the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value of            released(1). After the successful operation of             this action, the stpxMSTRegionEditBufferStatus            will be changed to acquiredBySnmp(2).               releaseWithForce \-\- release the Edit Buffer acquired by            non\-SNMP users with force and discard the changes            in the Edit Buffer. This operation can only be             performed when the object             stpxMSTRegionEditBufferStatus has the value of             acquiredByNonSnmp(2).  commit \-\-  commit the changes in the Edit Buffer            and release the Edit Buffer. The successful             operation of this action will make the changes            in the Edit Buffer effective on the device.            This operation can only be performed when the             object stpxMSTRegionEditBufferStatus has the             value of acquiredBySnmp(3).   rollBack \-\- discard the changes in the Edit Buffer            and release the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value             of acquiredBySnmp(3).  This object always returns other(1) when it is read
        	**type**\:   :py:class:`Stpxmstregioneditbufferoperation <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstobjects.Stpxmstregioneditbufferoperation>`
        
        .. attribute:: stpxmstregioneditbufferstatus
        
        	Indicates the current ownership status of the unique  Region Config Edit Buffer.   released \-\- the Edit Buffer can be acquired by any of              the SNMP management stations.   acquiredBySnmp \-\- the Edit Buffer is acquired by             any of the SNMP management stations.   acquiredByNonSnmp \-\- the Edit Buffer is acquired by the              non\-SNMP users managing the device
        	**type**\:   :py:class:`Stpxmstregioneditbufferstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstobjects.Stpxmstregioneditbufferstatus>`
        
        .. attribute:: stpxmstregioneditname
        
        	The MST region name in the Edit Buffer.   This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\:  str
        
        	**length:** 0..32
        
        .. attribute:: stpxmstregioneditrevision
        
        	The MST region version in the Edit Buffer. This object is only instantiated when the stpxMSTRegionEditBufferStatus  has the value of acquiredBySnmp(2).  This object is deprecated and replaced by stpxSMSTRegionEditRevision
        	**type**\:  int
        
        	**range:** 1..65535
        
        	**status**\: deprecated
        
        .. attribute:: stpxmstregionname
        
        	The operational MST region name
        	**type**\:  str
        
        	**length:** 0..32
        
        .. attribute:: stpxmstregionrevision
        
        	The operational MST region version.  This object is deprecated and replaced by  stpxSMSTRegionRevision
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmstobjects, self).__init__()

            self.yang_name = "stpxMSTObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmstmaxhopcount = YLeaf(YType.int32, "stpxMSTMaxHopCount")

            self.stpxmstmaxinstancenumber = YLeaf(YType.int32, "stpxMSTMaxInstanceNumber")

            self.stpxmstregioneditbufferoperation = YLeaf(YType.enumeration, "stpxMSTRegionEditBufferOperation")

            self.stpxmstregioneditbufferstatus = YLeaf(YType.enumeration, "stpxMSTRegionEditBufferStatus")

            self.stpxmstregioneditname = YLeaf(YType.str, "stpxMSTRegionEditName")

            self.stpxmstregioneditrevision = YLeaf(YType.int32, "stpxMSTRegionEditRevision")

            self.stpxmstregionname = YLeaf(YType.str, "stpxMSTRegionName")

            self.stpxmstregionrevision = YLeaf(YType.int32, "stpxMSTRegionRevision")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxmstmaxhopcount",
                            "stpxmstmaxinstancenumber",
                            "stpxmstregioneditbufferoperation",
                            "stpxmstregioneditbufferstatus",
                            "stpxmstregioneditname",
                            "stpxmstregioneditrevision",
                            "stpxmstregionname",
                            "stpxmstregionrevision") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxmstobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmstobjects, self).__setattr__(name, value)

        class Stpxmstregioneditbufferoperation(Enum):
            """
            Stpxmstregioneditbufferoperation

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
            Stpxmstregioneditbufferstatus

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


        def has_data(self):
            return (
                self.stpxmstmaxhopcount.is_set or
                self.stpxmstmaxinstancenumber.is_set or
                self.stpxmstregioneditbufferoperation.is_set or
                self.stpxmstregioneditbufferstatus.is_set or
                self.stpxmstregioneditname.is_set or
                self.stpxmstregioneditrevision.is_set or
                self.stpxmstregionname.is_set or
                self.stpxmstregionrevision.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxmstmaxhopcount.yfilter != YFilter.not_set or
                self.stpxmstmaxinstancenumber.yfilter != YFilter.not_set or
                self.stpxmstregioneditbufferoperation.yfilter != YFilter.not_set or
                self.stpxmstregioneditbufferstatus.yfilter != YFilter.not_set or
                self.stpxmstregioneditname.yfilter != YFilter.not_set or
                self.stpxmstregioneditrevision.yfilter != YFilter.not_set or
                self.stpxmstregionname.yfilter != YFilter.not_set or
                self.stpxmstregionrevision.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMSTObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxmstmaxhopcount.is_set or self.stpxmstmaxhopcount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstmaxhopcount.get_name_leafdata())
            if (self.stpxmstmaxinstancenumber.is_set or self.stpxmstmaxinstancenumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstmaxinstancenumber.get_name_leafdata())
            if (self.stpxmstregioneditbufferoperation.is_set or self.stpxmstregioneditbufferoperation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregioneditbufferoperation.get_name_leafdata())
            if (self.stpxmstregioneditbufferstatus.is_set or self.stpxmstregioneditbufferstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregioneditbufferstatus.get_name_leafdata())
            if (self.stpxmstregioneditname.is_set or self.stpxmstregioneditname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregioneditname.get_name_leafdata())
            if (self.stpxmstregioneditrevision.is_set or self.stpxmstregioneditrevision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregioneditrevision.get_name_leafdata())
            if (self.stpxmstregionname.is_set or self.stpxmstregionname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregionname.get_name_leafdata())
            if (self.stpxmstregionrevision.is_set or self.stpxmstregionrevision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxmstregionrevision.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMSTMaxHopCount" or name == "stpxMSTMaxInstanceNumber" or name == "stpxMSTRegionEditBufferOperation" or name == "stpxMSTRegionEditBufferStatus" or name == "stpxMSTRegionEditName" or name == "stpxMSTRegionEditRevision" or name == "stpxMSTRegionName" or name == "stpxMSTRegionRevision"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxMSTMaxHopCount"):
                self.stpxmstmaxhopcount = value
                self.stpxmstmaxhopcount.value_namespace = name_space
                self.stpxmstmaxhopcount.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTMaxInstanceNumber"):
                self.stpxmstmaxinstancenumber = value
                self.stpxmstmaxinstancenumber.value_namespace = name_space
                self.stpxmstmaxinstancenumber.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionEditBufferOperation"):
                self.stpxmstregioneditbufferoperation = value
                self.stpxmstregioneditbufferoperation.value_namespace = name_space
                self.stpxmstregioneditbufferoperation.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionEditBufferStatus"):
                self.stpxmstregioneditbufferstatus = value
                self.stpxmstregioneditbufferstatus.value_namespace = name_space
                self.stpxmstregioneditbufferstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionEditName"):
                self.stpxmstregioneditname = value
                self.stpxmstregioneditname.value_namespace = name_space
                self.stpxmstregioneditname.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionEditRevision"):
                self.stpxmstregioneditrevision = value
                self.stpxmstregioneditrevision.value_namespace = name_space
                self.stpxmstregioneditrevision.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionName"):
                self.stpxmstregionname = value
                self.stpxmstregionname.value_namespace = name_space
                self.stpxmstregionname.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxMSTRegionRevision"):
                self.stpxmstregionrevision = value
                self.stpxmstregionrevision.value_namespace = name_space
                self.stpxmstregionrevision.value_namespace_prefix = name_space_prefix


    class Stpxrstpobjects(Entity):
        """
        
        
        .. attribute:: stpxrstptransmitholdcount
        
        	The Transmit Hold Count
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrstpobjects, self).__init__()

            self.yang_name = "stpxRSTPObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrstptransmitholdcount = YLeaf(YType.uint32, "stpxRSTPTransmitHoldCount")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxrstptransmitholdcount") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxrstpobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrstpobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.stpxrstptransmitholdcount.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxrstptransmitholdcount.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRSTPObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxrstptransmitholdcount.is_set or self.stpxrstptransmitholdcount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxrstptransmitholdcount.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRSTPTransmitHoldCount"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxRSTPTransmitHoldCount"):
                self.stpxrstptransmitholdcount = value
                self.stpxrstptransmitholdcount.value_namespace = name_space
                self.stpxrstptransmitholdcount.value_namespace_prefix = name_space_prefix


    class Stpxsmstobjects(Entity):
        """
        
        
        .. attribute:: stpxsmstconfigdigest
        
        	The IEEE MST region configuration digest
        	**type**\:  str
        
        .. attribute:: stpxsmstconfigprestandarddigest
        
        	The pre\-standard MST region configuration digest
        	**type**\:  str
        
        .. attribute:: stpxsmstmaxhopcount
        
        	The maximum number of hops for the IEEE MST region
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxinstanceid
        
        	The maximum MST instance ID that can be supported  by the device for IEEE MST
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxinstances
        
        	The maximum number of MST instances that can be  supported by the device for IEEE MST
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregioneditrevision
        
        	The MST region version in the Edit Buffer for IEEE  MST.  This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregionrevision
        
        	The operational region version for IEEE MST
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxsmstobjects, self).__init__()

            self.yang_name = "stpxSMSTObjects"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxsmstconfigdigest = YLeaf(YType.str, "stpxSMSTConfigDigest")

            self.stpxsmstconfigprestandarddigest = YLeaf(YType.str, "stpxSMSTConfigPreStandardDigest")

            self.stpxsmstmaxhopcount = YLeaf(YType.uint32, "stpxSMSTMaxHopCount")

            self.stpxsmstmaxinstanceid = YLeaf(YType.uint32, "stpxSMSTMaxInstanceID")

            self.stpxsmstmaxinstances = YLeaf(YType.uint32, "stpxSMSTMaxInstances")

            self.stpxsmstregioneditrevision = YLeaf(YType.uint32, "stpxSMSTRegionEditRevision")

            self.stpxsmstregionrevision = YLeaf(YType.uint32, "stpxSMSTRegionRevision")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stpxsmstconfigdigest",
                            "stpxsmstconfigprestandarddigest",
                            "stpxsmstmaxhopcount",
                            "stpxsmstmaxinstanceid",
                            "stpxsmstmaxinstances",
                            "stpxsmstregioneditrevision",
                            "stpxsmstregionrevision") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoStpExtensionsMib.Stpxsmstobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxsmstobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.stpxsmstconfigdigest.is_set or
                self.stpxsmstconfigprestandarddigest.is_set or
                self.stpxsmstmaxhopcount.is_set or
                self.stpxsmstmaxinstanceid.is_set or
                self.stpxsmstmaxinstances.is_set or
                self.stpxsmstregioneditrevision.is_set or
                self.stpxsmstregionrevision.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.stpxsmstconfigdigest.yfilter != YFilter.not_set or
                self.stpxsmstconfigprestandarddigest.yfilter != YFilter.not_set or
                self.stpxsmstmaxhopcount.yfilter != YFilter.not_set or
                self.stpxsmstmaxinstanceid.yfilter != YFilter.not_set or
                self.stpxsmstmaxinstances.yfilter != YFilter.not_set or
                self.stpxsmstregioneditrevision.yfilter != YFilter.not_set or
                self.stpxsmstregionrevision.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxSMSTObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.stpxsmstconfigdigest.is_set or self.stpxsmstconfigdigest.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstconfigdigest.get_name_leafdata())
            if (self.stpxsmstconfigprestandarddigest.is_set or self.stpxsmstconfigprestandarddigest.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstconfigprestandarddigest.get_name_leafdata())
            if (self.stpxsmstmaxhopcount.is_set or self.stpxsmstmaxhopcount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstmaxhopcount.get_name_leafdata())
            if (self.stpxsmstmaxinstanceid.is_set or self.stpxsmstmaxinstanceid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstmaxinstanceid.get_name_leafdata())
            if (self.stpxsmstmaxinstances.is_set or self.stpxsmstmaxinstances.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstmaxinstances.get_name_leafdata())
            if (self.stpxsmstregioneditrevision.is_set or self.stpxsmstregioneditrevision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstregioneditrevision.get_name_leafdata())
            if (self.stpxsmstregionrevision.is_set or self.stpxsmstregionrevision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stpxsmstregionrevision.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxSMSTConfigDigest" or name == "stpxSMSTConfigPreStandardDigest" or name == "stpxSMSTMaxHopCount" or name == "stpxSMSTMaxInstanceID" or name == "stpxSMSTMaxInstances" or name == "stpxSMSTRegionEditRevision" or name == "stpxSMSTRegionRevision"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stpxSMSTConfigDigest"):
                self.stpxsmstconfigdigest = value
                self.stpxsmstconfigdigest.value_namespace = name_space
                self.stpxsmstconfigdigest.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTConfigPreStandardDigest"):
                self.stpxsmstconfigprestandarddigest = value
                self.stpxsmstconfigprestandarddigest.value_namespace = name_space
                self.stpxsmstconfigprestandarddigest.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTMaxHopCount"):
                self.stpxsmstmaxhopcount = value
                self.stpxsmstmaxhopcount.value_namespace = name_space
                self.stpxsmstmaxhopcount.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTMaxInstanceID"):
                self.stpxsmstmaxinstanceid = value
                self.stpxsmstmaxinstanceid.value_namespace = name_space
                self.stpxsmstmaxinstanceid.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTMaxInstances"):
                self.stpxsmstmaxinstances = value
                self.stpxsmstmaxinstances.value_namespace = name_space
                self.stpxsmstmaxinstances.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTRegionEditRevision"):
                self.stpxsmstregioneditrevision = value
                self.stpxsmstregioneditrevision.value_namespace = name_space
                self.stpxsmstregioneditrevision.value_namespace_prefix = name_space_prefix
            if(value_path == "stpxSMSTRegionRevision"):
                self.stpxsmstregionrevision = value
                self.stpxsmstregionrevision.value_namespace = name_space
                self.stpxsmstregionrevision.value_namespace_prefix = name_space_prefix


    class Stpxpvstvlantable(Entity):
        """
        A list of Virtual LAN entries containing
        information for Spanning Tree PVST+ protocol. 
        An entry will exist for each VLAN existing on 
        the device.
        
        .. attribute:: stpxpvstvlanentry
        
        	An entry containing Spanning Tree PVST+ Protocol  information for a particular Virtual LAN
        	**type**\: list of    :py:class:`Stpxpvstvlanentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxpvstvlantable, self).__init__()

            self.yang_name = "stpxPVSTVlanTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxpvstvlanentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxpvstvlantable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxpvstvlantable, self).__setattr__(name, value)


        class Stpxpvstvlanentry(Entity):
            """
            An entry containing Spanning Tree PVST+ Protocol 
            information for a particular Virtual LAN.
            
            .. attribute:: stpxpvstvlanindex  <key>
            
            	An index value that uniquely identifies the Virtual LAN associated with this information
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxpvstvlanenable
            
            	Indicates whether Spanning Tree PVST+   Protocol is enabled for this Virtual LAN. If  Spanning Tree PVST+ Protocol is not supported  on this VLAN, then notApplicable(3) will be  returned while retrieving the object value for  this VLAN.  If the device only supports a single global Spanning Tree PVST+ Protocol enable/disable  for all the existing VLANs, then the object  value assigned to this VLAN will be applied to the object values of all the instances in this table which do not have the value of notApplicable(3).  If the value of stpxSpanningTreeType is neither  pvstPlus(1) nor rapidPvstPlus(5), then the value  of stpxPVSTVlanEnable for this VLAN can not be  changed
            	**type**\:   :py:class:`Stpxpvstvlanenable <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry.Stpxpvstvlanenable>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry, self).__init__()

                self.yang_name = "stpxPVSTVlanEntry"
                self.yang_parent_name = "stpxPVSTVlanTable"

                self.stpxpvstvlanindex = YLeaf(YType.int32, "stpxPVSTVlanIndex")

                self.stpxpvstvlanenable = YLeaf(YType.enumeration, "stpxPVSTVlanEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxpvstvlanindex",
                                "stpxpvstvlanenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry, self).__setattr__(name, value)

            class Stpxpvstvlanenable(Enum):
                """
                Stpxpvstvlanenable

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


            def has_data(self):
                return (
                    self.stpxpvstvlanindex.is_set or
                    self.stpxpvstvlanenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxpvstvlanindex.yfilter != YFilter.not_set or
                    self.stpxpvstvlanenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxPVSTVlanEntry" + "[stpxPVSTVlanIndex='" + self.stpxpvstvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxPVSTVlanTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxpvstvlanindex.is_set or self.stpxpvstvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpvstvlanindex.get_name_leafdata())
                if (self.stpxpvstvlanenable.is_set or self.stpxpvstvlanenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpvstvlanenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxPVSTVlanIndex" or name == "stpxPVSTVlanEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxPVSTVlanIndex"):
                    self.stpxpvstvlanindex = value
                    self.stpxpvstvlanindex.value_namespace = name_space
                    self.stpxpvstvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPVSTVlanEnable"):
                    self.stpxpvstvlanenable = value
                    self.stpxpvstvlanenable.value_namespace = name_space
                    self.stpxpvstvlanenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxpvstvlanentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxpvstvlanentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxPVSTVlanTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxPVSTVlanEntry"):
                for c in self.stpxpvstvlanentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxpvstvlanentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxPVSTVlanEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Stpxinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxinconsistencytable, self).__init__()

            self.yang_name = "stpxInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxinconsistencyentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxinconsistencytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxinconsistencytable, self).__setattr__(name, value)


        class Stpxinconsistencyentry(Entity):
            """
            A VLAN on a particular port for which a Spanning Tree
            inconsistency is currently in effect.
            
            .. attribute:: stpxvlanindex  <key>
            
            	The VLAN id of the VLAN
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxinconsistentstate
            
            	The types of inconsistency which have been discovered on this port for this VLAN's Spanning Tree.  When this object exists, the value of the corresponding instance of the Bridge MIB's dot1dStpPortState object will be 'broken(6)'
            	**type**\:   :py:class:`Stpxinconsistentstate <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry.Stpxinconsistentstate>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry, self).__init__()

                self.yang_name = "stpxInconsistencyEntry"
                self.yang_parent_name = "stpxInconsistencyTable"

                self.stpxvlanindex = YLeaf(YType.int32, "stpxVlanIndex")

                self.stpxportindex = YLeaf(YType.int32, "stpxPortIndex")

                self.stpxinconsistentstate = YLeaf(YType.bits, "stpxInconsistentState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxvlanindex",
                                "stpxportindex",
                                "stpxinconsistentstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxvlanindex.is_set or
                    self.stpxportindex.is_set or
                    self.stpxinconsistentstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxvlanindex.yfilter != YFilter.not_set or
                    self.stpxportindex.yfilter != YFilter.not_set or
                    self.stpxinconsistentstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxInconsistencyEntry" + "[stpxVlanIndex='" + self.stpxvlanindex.get() + "']" + "[stpxPortIndex='" + self.stpxportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxInconsistencyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxvlanindex.is_set or self.stpxvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxvlanindex.get_name_leafdata())
                if (self.stpxportindex.is_set or self.stpxportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxportindex.get_name_leafdata())
                if (self.stpxinconsistentstate.is_set or self.stpxinconsistentstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxinconsistentstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxVlanIndex" or name == "stpxPortIndex" or name == "stpxInconsistentState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxVlanIndex"):
                    self.stpxvlanindex = value
                    self.stpxvlanindex.value_namespace = name_space
                    self.stpxvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPortIndex"):
                    self.stpxportindex = value
                    self.stpxportindex.value_namespace = name_space
                    self.stpxportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxInconsistentState"):
                    self.stpxinconsistentstate[value] = True

        def has_data(self):
            for c in self.stpxinconsistencyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxinconsistencyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxInconsistencyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxInconsistencyEntry"):
                for c in self.stpxinconsistencyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxinconsistencyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxInconsistencyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxrootguardconfigtable(Entity):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree RootGuard capability can be configured.
        
        .. attribute:: stpxrootguardconfigentry
        
        	A bridge port for which Spanning Tree RootGuard capability can be configured
        	**type**\: list of    :py:class:`Stpxrootguardconfigentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrootguardconfigtable, self).__init__()

            self.yang_name = "stpxRootGuardConfigTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrootguardconfigentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxrootguardconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrootguardconfigtable, self).__setattr__(name, value)


        class Stpxrootguardconfigentry(Entity):
            """
            A bridge port for which Spanning Tree RootGuard
            capability can be configured.
            
            .. attribute:: stpxrootguardconfigportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootguardconfigenabled
            
            	An indication of whether the RootGuard capability is  enabled on this port or not. This configuration will be applied to all Spanning Tree instances in which this port  exists
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry, self).__init__()

                self.yang_name = "stpxRootGuardConfigEntry"
                self.yang_parent_name = "stpxRootGuardConfigTable"

                self.stpxrootguardconfigportindex = YLeaf(YType.int32, "stpxRootGuardConfigPortIndex")

                self.stpxrootguardconfigenabled = YLeaf(YType.boolean, "stpxRootGuardConfigEnabled")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxrootguardconfigportindex",
                                "stpxrootguardconfigenabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxrootguardconfigportindex.is_set or
                    self.stpxrootguardconfigenabled.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxrootguardconfigportindex.yfilter != YFilter.not_set or
                    self.stpxrootguardconfigenabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxRootGuardConfigEntry" + "[stpxRootGuardConfigPortIndex='" + self.stpxrootguardconfigportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRootGuardConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxrootguardconfigportindex.is_set or self.stpxrootguardconfigportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrootguardconfigportindex.get_name_leafdata())
                if (self.stpxrootguardconfigenabled.is_set or self.stpxrootguardconfigenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrootguardconfigenabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxRootGuardConfigPortIndex" or name == "stpxRootGuardConfigEnabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxRootGuardConfigPortIndex"):
                    self.stpxrootguardconfigportindex = value
                    self.stpxrootguardconfigportindex.value_namespace = name_space
                    self.stpxrootguardconfigportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRootGuardConfigEnabled"):
                    self.stpxrootguardconfigenabled = value
                    self.stpxrootguardconfigenabled.value_namespace = name_space
                    self.stpxrootguardconfigenabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxrootguardconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxrootguardconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRootGuardConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxRootGuardConfigEntry"):
                for c in self.stpxrootguardconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxrootguardconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRootGuardConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Stpxrootinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrootinconsistencytable, self).__init__()

            self.yang_name = "stpxRootInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrootinconsistencyentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxrootinconsistencytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrootinconsistencytable, self).__setattr__(name, value)


        class Stpxrootinconsistencyentry(Entity):
            """
            A Spanning Tree instance on a particular port for 
            which a Spanning Tree root\-inconsistency is currently 
            in effect.
            
            .. attribute:: stpxrootinconsistencyindex  <key>
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: stpxrootinconsistencyportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in root\-inconsistent  state or not
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry, self).__init__()

                self.yang_name = "stpxRootInconsistencyEntry"
                self.yang_parent_name = "stpxRootInconsistencyTable"

                self.stpxrootinconsistencyindex = YLeaf(YType.int32, "stpxRootInconsistencyIndex")

                self.stpxrootinconsistencyportindex = YLeaf(YType.int32, "stpxRootInconsistencyPortIndex")

                self.stpxrootinconsistencystate = YLeaf(YType.boolean, "stpxRootInconsistencyState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxrootinconsistencyindex",
                                "stpxrootinconsistencyportindex",
                                "stpxrootinconsistencystate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxrootinconsistencyindex.is_set or
                    self.stpxrootinconsistencyportindex.is_set or
                    self.stpxrootinconsistencystate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxrootinconsistencyindex.yfilter != YFilter.not_set or
                    self.stpxrootinconsistencyportindex.yfilter != YFilter.not_set or
                    self.stpxrootinconsistencystate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxRootInconsistencyEntry" + "[stpxRootInconsistencyIndex='" + self.stpxrootinconsistencyindex.get() + "']" + "[stpxRootInconsistencyPortIndex='" + self.stpxrootinconsistencyportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRootInconsistencyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxrootinconsistencyindex.is_set or self.stpxrootinconsistencyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrootinconsistencyindex.get_name_leafdata())
                if (self.stpxrootinconsistencyportindex.is_set or self.stpxrootinconsistencyportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrootinconsistencyportindex.get_name_leafdata())
                if (self.stpxrootinconsistencystate.is_set or self.stpxrootinconsistencystate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrootinconsistencystate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxRootInconsistencyIndex" or name == "stpxRootInconsistencyPortIndex" or name == "stpxRootInconsistencyState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxRootInconsistencyIndex"):
                    self.stpxrootinconsistencyindex = value
                    self.stpxrootinconsistencyindex.value_namespace = name_space
                    self.stpxrootinconsistencyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRootInconsistencyPortIndex"):
                    self.stpxrootinconsistencyportindex = value
                    self.stpxrootinconsistencyportindex.value_namespace = name_space
                    self.stpxrootinconsistencyportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRootInconsistencyState"):
                    self.stpxrootinconsistencystate = value
                    self.stpxrootinconsistencystate.value_namespace = name_space
                    self.stpxrootinconsistencystate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxrootinconsistencyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxrootinconsistencyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRootInconsistencyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxRootInconsistencyEntry"):
                for c in self.stpxrootinconsistencyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxrootinconsistencyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRootInconsistencyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxmistpinstancetable(Entity):
        """
        This table contains one entry for each instance of MISTP and 
        it contains stpxMISTPInstanceNumber entries, numbered from 1
        to stpxMISTPInstanceNumber.
        
        This table is only instantiated when the value of 
        stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3).
        
        .. attribute:: stpxmistpinstanceentry
        
        	A conceptual row containing the status of the MISTP  instance
        	**type**\: list of    :py:class:`Stpxmistpinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmistpinstancetable, self).__init__()

            self.yang_name = "stpxMISTPInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmistpinstanceentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxmistpinstancetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmistpinstancetable, self).__setattr__(name, value)


        class Stpxmistpinstanceentry(Entity):
            """
            A conceptual row containing the status of the MISTP 
            instance.
            
            .. attribute:: stpxmistpinstanceindex  <key>
            
            	An arbitrary integer within the range from 1 to the value of stpxMISTPInstanceNumber that uniquely identifies an instance
            	**type**\:  int
            
            	**range:** 1..256
            
            .. attribute:: stpxmistpinstanceenable
            
            	This object indicates whether the MISTP protocol is currently enabled on the MISTP instance.  If this object is set to    'true'    \- the MISTP protocol will run on this instance.                   'false'   \- the MISTP protocol will stop running on this                 instance
            	**type**\:  bool
            
            .. attribute:: stpxmistpinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\:  str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry, self).__init__()

                self.yang_name = "stpxMISTPInstanceEntry"
                self.yang_parent_name = "stpxMISTPInstanceTable"

                self.stpxmistpinstanceindex = YLeaf(YType.int32, "stpxMISTPInstanceIndex")

                self.stpxmistpinstanceenable = YLeaf(YType.boolean, "stpxMISTPInstanceEnable")

                self.stpxmistpinstancevlansmapped = YLeaf(YType.str, "stpxMISTPInstanceVlansMapped")

                self.stpxmistpinstancevlansmapped2k = YLeaf(YType.str, "stpxMISTPInstanceVlansMapped2k")

                self.stpxmistpinstancevlansmapped3k = YLeaf(YType.str, "stpxMISTPInstanceVlansMapped3k")

                self.stpxmistpinstancevlansmapped4k = YLeaf(YType.str, "stpxMISTPInstanceVlansMapped4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxmistpinstanceindex",
                                "stpxmistpinstanceenable",
                                "stpxmistpinstancevlansmapped",
                                "stpxmistpinstancevlansmapped2k",
                                "stpxmistpinstancevlansmapped3k",
                                "stpxmistpinstancevlansmapped4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxmistpinstanceindex.is_set or
                    self.stpxmistpinstanceenable.is_set or
                    self.stpxmistpinstancevlansmapped.is_set or
                    self.stpxmistpinstancevlansmapped2k.is_set or
                    self.stpxmistpinstancevlansmapped3k.is_set or
                    self.stpxmistpinstancevlansmapped4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxmistpinstanceindex.yfilter != YFilter.not_set or
                    self.stpxmistpinstanceenable.yfilter != YFilter.not_set or
                    self.stpxmistpinstancevlansmapped.yfilter != YFilter.not_set or
                    self.stpxmistpinstancevlansmapped2k.yfilter != YFilter.not_set or
                    self.stpxmistpinstancevlansmapped3k.yfilter != YFilter.not_set or
                    self.stpxmistpinstancevlansmapped4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxMISTPInstanceEntry" + "[stpxMISTPInstanceIndex='" + self.stpxmistpinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMISTPInstanceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxmistpinstanceindex.is_set or self.stpxmistpinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstanceindex.get_name_leafdata())
                if (self.stpxmistpinstanceenable.is_set or self.stpxmistpinstanceenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstanceenable.get_name_leafdata())
                if (self.stpxmistpinstancevlansmapped.is_set or self.stpxmistpinstancevlansmapped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstancevlansmapped.get_name_leafdata())
                if (self.stpxmistpinstancevlansmapped2k.is_set or self.stpxmistpinstancevlansmapped2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstancevlansmapped2k.get_name_leafdata())
                if (self.stpxmistpinstancevlansmapped3k.is_set or self.stpxmistpinstancevlansmapped3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstancevlansmapped3k.get_name_leafdata())
                if (self.stpxmistpinstancevlansmapped4k.is_set or self.stpxmistpinstancevlansmapped4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmistpinstancevlansmapped4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxMISTPInstanceIndex" or name == "stpxMISTPInstanceEnable" or name == "stpxMISTPInstanceVlansMapped" or name == "stpxMISTPInstanceVlansMapped2k" or name == "stpxMISTPInstanceVlansMapped3k" or name == "stpxMISTPInstanceVlansMapped4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxMISTPInstanceIndex"):
                    self.stpxmistpinstanceindex = value
                    self.stpxmistpinstanceindex.value_namespace = name_space
                    self.stpxmistpinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMISTPInstanceEnable"):
                    self.stpxmistpinstanceenable = value
                    self.stpxmistpinstanceenable.value_namespace = name_space
                    self.stpxmistpinstanceenable.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMISTPInstanceVlansMapped"):
                    self.stpxmistpinstancevlansmapped = value
                    self.stpxmistpinstancevlansmapped.value_namespace = name_space
                    self.stpxmistpinstancevlansmapped.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMISTPInstanceVlansMapped2k"):
                    self.stpxmistpinstancevlansmapped2k = value
                    self.stpxmistpinstancevlansmapped2k.value_namespace = name_space
                    self.stpxmistpinstancevlansmapped2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMISTPInstanceVlansMapped3k"):
                    self.stpxmistpinstancevlansmapped3k = value
                    self.stpxmistpinstancevlansmapped3k.value_namespace = name_space
                    self.stpxmistpinstancevlansmapped3k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMISTPInstanceVlansMapped4k"):
                    self.stpxmistpinstancevlansmapped4k = value
                    self.stpxmistpinstancevlansmapped4k.value_namespace = name_space
                    self.stpxmistpinstancevlansmapped4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxmistpinstanceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxmistpinstanceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMISTPInstanceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxMISTPInstanceEntry"):
                for c in self.stpxmistpinstanceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxmistpinstanceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMISTPInstanceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxloopguardconfigtable(Entity):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree LoopGuard capability can be configured.
        
        .. attribute:: stpxloopguardconfigentry
        
        	A bridge port for which Spanning Tree LoopGuard  capability can be configured
        	**type**\: list of    :py:class:`Stpxloopguardconfigentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxloopguardconfigtable, self).__init__()

            self.yang_name = "stpxLoopGuardConfigTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxloopguardconfigentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxloopguardconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxloopguardconfigtable, self).__setattr__(name, value)


        class Stpxloopguardconfigentry(Entity):
            """
            A bridge port for which Spanning Tree LoopGuard 
            capability can be configured.
            
            .. attribute:: stpxloopguardconfigportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopguardconfigenabled
            
            	An indication of whether the LoopGuard capability is  enabled on this port or not. This configuration will be applied to all the Spanning Tree instances in which this  port exists.  In order to support additional Loop Guard config mode (default) as defined in stpxLoopGuardConfigMode other  than enable (true(1)) or disable (false(2)) as defined  in this object, stpxLoopGuardConfigMode object needs to  be used.  When the stpxLoopGuardConfigMode object has the value of enable(1), the value of stpxLoopGuardConfigEnabled for  the same instance will be true(1). When the  stpxLoopGuardConfigMode object has the value of disable(2),  the value of stpxLoopGuardConfigEnabled for the same  instance will be false(2). When the stpxLoopGuardConfigMode  object has the value of default(3), the value of  stpxLoopGuardConfigEnabled for the same instance will  depend on the object value of  stpxLoopGuardGlobalDefaultMode
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxloopguardconfigmode
            
            	Indicates the mode of Loop Guard Feature on this  port. This configuration will be applied to all  the Spanning Tree instances in which this port  exists.  enable \-\- the Loop Guard feature is enabled on this            port.   disable \-\- the Loop Guard feature is disabled on this            port.    default \-\- whether the Loop Guard feature is enabled            or not on this port depends on the object             value of stpxLoopGuardGlobalDefaultMode
            	**type**\:   :py:class:`Stpxloopguardconfigmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry.Stpxloopguardconfigmode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry, self).__init__()

                self.yang_name = "stpxLoopGuardConfigEntry"
                self.yang_parent_name = "stpxLoopGuardConfigTable"

                self.stpxloopguardconfigportindex = YLeaf(YType.int32, "stpxLoopGuardConfigPortIndex")

                self.stpxloopguardconfigenabled = YLeaf(YType.boolean, "stpxLoopGuardConfigEnabled")

                self.stpxloopguardconfigmode = YLeaf(YType.enumeration, "stpxLoopGuardConfigMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxloopguardconfigportindex",
                                "stpxloopguardconfigenabled",
                                "stpxloopguardconfigmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry, self).__setattr__(name, value)

            class Stpxloopguardconfigmode(Enum):
                """
                Stpxloopguardconfigmode

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


            def has_data(self):
                return (
                    self.stpxloopguardconfigportindex.is_set or
                    self.stpxloopguardconfigenabled.is_set or
                    self.stpxloopguardconfigmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxloopguardconfigportindex.yfilter != YFilter.not_set or
                    self.stpxloopguardconfigenabled.yfilter != YFilter.not_set or
                    self.stpxloopguardconfigmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxLoopGuardConfigEntry" + "[stpxLoopGuardConfigPortIndex='" + self.stpxloopguardconfigportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxLoopGuardConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxloopguardconfigportindex.is_set or self.stpxloopguardconfigportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopguardconfigportindex.get_name_leafdata())
                if (self.stpxloopguardconfigenabled.is_set or self.stpxloopguardconfigenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopguardconfigenabled.get_name_leafdata())
                if (self.stpxloopguardconfigmode.is_set or self.stpxloopguardconfigmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopguardconfigmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxLoopGuardConfigPortIndex" or name == "stpxLoopGuardConfigEnabled" or name == "stpxLoopGuardConfigMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxLoopGuardConfigPortIndex"):
                    self.stpxloopguardconfigportindex = value
                    self.stpxloopguardconfigportindex.value_namespace = name_space
                    self.stpxloopguardconfigportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxLoopGuardConfigEnabled"):
                    self.stpxloopguardconfigenabled = value
                    self.stpxloopguardconfigenabled.value_namespace = name_space
                    self.stpxloopguardconfigenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxLoopGuardConfigMode"):
                    self.stpxloopguardconfigmode = value
                    self.stpxloopguardconfigmode.value_namespace = name_space
                    self.stpxloopguardconfigmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxloopguardconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxloopguardconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxLoopGuardConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxLoopGuardConfigEntry"):
                for c in self.stpxloopguardconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxloopguardconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxLoopGuardConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Stpxloopinconsistencyentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxloopinconsistencytable, self).__init__()

            self.yang_name = "stpxLoopInconsistencyTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxloopinconsistencyentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxloopinconsistencytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxloopinconsistencytable, self).__setattr__(name, value)


        class Stpxloopinconsistencyentry(Entity):
            """
            A Spanning Tree instance on a particular port for
            which a Spanning Tree loop\-inconsistency is currently
            in effect.
            
            .. attribute:: stpxloopinconsistencyindex  <key>
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: stpxloopinconsistencyportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in loop\-inconsistent  state or not
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry, self).__init__()

                self.yang_name = "stpxLoopInconsistencyEntry"
                self.yang_parent_name = "stpxLoopInconsistencyTable"

                self.stpxloopinconsistencyindex = YLeaf(YType.int32, "stpxLoopInconsistencyIndex")

                self.stpxloopinconsistencyportindex = YLeaf(YType.int32, "stpxLoopInconsistencyPortIndex")

                self.stpxloopinconsistencystate = YLeaf(YType.boolean, "stpxLoopInconsistencyState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxloopinconsistencyindex",
                                "stpxloopinconsistencyportindex",
                                "stpxloopinconsistencystate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxloopinconsistencyindex.is_set or
                    self.stpxloopinconsistencyportindex.is_set or
                    self.stpxloopinconsistencystate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxloopinconsistencyindex.yfilter != YFilter.not_set or
                    self.stpxloopinconsistencyportindex.yfilter != YFilter.not_set or
                    self.stpxloopinconsistencystate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxLoopInconsistencyEntry" + "[stpxLoopInconsistencyIndex='" + self.stpxloopinconsistencyindex.get() + "']" + "[stpxLoopInconsistencyPortIndex='" + self.stpxloopinconsistencyportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxLoopInconsistencyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxloopinconsistencyindex.is_set or self.stpxloopinconsistencyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopinconsistencyindex.get_name_leafdata())
                if (self.stpxloopinconsistencyportindex.is_set or self.stpxloopinconsistencyportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopinconsistencyportindex.get_name_leafdata())
                if (self.stpxloopinconsistencystate.is_set or self.stpxloopinconsistencystate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxloopinconsistencystate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxLoopInconsistencyIndex" or name == "stpxLoopInconsistencyPortIndex" or name == "stpxLoopInconsistencyState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxLoopInconsistencyIndex"):
                    self.stpxloopinconsistencyindex = value
                    self.stpxloopinconsistencyindex.value_namespace = name_space
                    self.stpxloopinconsistencyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxLoopInconsistencyPortIndex"):
                    self.stpxloopinconsistencyportindex = value
                    self.stpxloopinconsistencyportindex.value_namespace = name_space
                    self.stpxloopinconsistencyportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxLoopInconsistencyState"):
                    self.stpxloopinconsistencystate = value
                    self.stpxloopinconsistencystate.value_namespace = name_space
                    self.stpxloopinconsistencystate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxloopinconsistencyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxloopinconsistencyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxLoopInconsistencyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxLoopInconsistencyEntry"):
                for c in self.stpxloopinconsistencyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxloopinconsistencyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxLoopInconsistencyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxfaststartporttable(Entity):
        """
        A table containing a list of the bridge ports for
        which Spanning Tree Port Fast Start can be
        configured.
        
        .. attribute:: stpxfaststartportentry
        
        	A bridge port for which Spanning Tree Port Fast Start can be configured
        	**type**\: list of    :py:class:`Stpxfaststartportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxfaststartporttable, self).__init__()

            self.yang_name = "stpxFastStartPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxfaststartportentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxfaststartporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxfaststartporttable, self).__setattr__(name, value)


        class Stpxfaststartportentry(Entity):
            """
            A bridge port for which Spanning Tree Port Fast
            Start can be configured.
            
            .. attribute:: stpxfaststartportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartportbpdufiltermode
            
            	Indicates the mode of Bpdu Filter Feature on the port. The system will not transmit BPDUs on a port  with Bpdu Filter feature enabled.  enable \-\- the Bpdu Filter feature is enabled on this            port.   disable \-\- the Bpdu Filter feature is disabled on this            port.  default \-\- whether the Bpdu Filter feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduFilterEnable. If            the value of stpxFastStartBpduFilterEnable            is true(1) and Fast Start feature is also            enabled operationally on this port, then            no BPDUs will be transmitted on this port
            	**type**\:   :py:class:`Stpxfaststartportbpdufiltermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportbpdufiltermode>`
            
            .. attribute:: stpxfaststartportbpduguardmode
            
            	Indicates the mode of Bpdu Guard Feature on the port. A port with Bpdu Guard enabled is  immediately disabled when the system  receives a BPDU from that port.   enable \-\- the Bpdu Guard feature is enabled on this           port.   disable \-\- the Bpdu Guard feature is disabled on this           port.  default \-\- whether the Bpdu Guard feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduGuardEnable. If             the value of stpxFastStartBpduGuardEnable            is true(1) and Fast Start feature is also             enabled operationally on this port, then            this port is immediately disabled when             the system receives a BPDU from this port
            	**type**\:   :py:class:`Stpxfaststartportbpduguardmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportbpduguardmode>`
            
            .. attribute:: stpxfaststartportenable
            
            	Indicates whether the port is operating in spantree fast start mode.  A port with fast start enabled is immediately put in spanning tree forwarding state when that port is detected by the Spanning Tree, rather  than starting in blocking state which is the normal  operation.  In order to support additional Fast Start enable mode (enableForTrunk and default) as defined in stpxFastStartPortMode other than enable (true(1)) or disable (false(2)) as defined in this object, stpxFastStartPortMode object needs to be used.  When the stpxFastStartPortMode has the value of enable(1) or enableForTrunk(3), the value of stpxFastStartPortEnable for the same instance will be true(1). When the stpxFastStartPortMode has the value of disable(2), the value of  stpxFastStartPortEnable for the same instance will be  false(2). When the stpxFastStartPortMode has the value  of default(4), the value of stpxFastStartPortEnable for  the same instance depends on the object value of  stpxFastStartGlobalDefaultMode
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxfaststartportmode
            
            	Indicates the mode of Fast Start Feature on the  port. A port with fast start enabled is immediately  put in spanning tree forwarding state when the port is detected by the Spanning Tree, rather than  starting in blocking state which is the normal  operation.  enable \-\- the fast start feature is enabled on this            port but will only take effect when the            object value of its            vlanTrunkPortDynamicStatus as specified            in CISCO\-VTP\-MIB is notTrunking(2).  disable \-\- the fast start feature is disabled on this            port.    enableForTrunk \-\- the fast start feature is enabled            on this port and will take effect            regardless of the object value of            its vlanTrunkPortDynamicStatus.  default \-\- whether the fast start feature is enabled            or not on this port depends on the object             value of stpxFastStartGlobalDefaultMode.  network \-\- the fast start network mode is enabled on             this port
            	**type**\:   :py:class:`Stpxfaststartportmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.Stpxfaststartportmode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry, self).__init__()

                self.yang_name = "stpxFastStartPortEntry"
                self.yang_parent_name = "stpxFastStartPortTable"

                self.stpxfaststartportindex = YLeaf(YType.int32, "stpxFastStartPortIndex")

                self.stpxfaststartportbpdufiltermode = YLeaf(YType.enumeration, "stpxFastStartPortBpduFilterMode")

                self.stpxfaststartportbpduguardmode = YLeaf(YType.enumeration, "stpxFastStartPortBpduGuardMode")

                self.stpxfaststartportenable = YLeaf(YType.boolean, "stpxFastStartPortEnable")

                self.stpxfaststartportmode = YLeaf(YType.enumeration, "stpxFastStartPortMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxfaststartportindex",
                                "stpxfaststartportbpdufiltermode",
                                "stpxfaststartportbpduguardmode",
                                "stpxfaststartportenable",
                                "stpxfaststartportmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry, self).__setattr__(name, value)

            class Stpxfaststartportbpdufiltermode(Enum):
                """
                Stpxfaststartportbpdufiltermode

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
                Stpxfaststartportbpduguardmode

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
                Stpxfaststartportmode

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


            def has_data(self):
                return (
                    self.stpxfaststartportindex.is_set or
                    self.stpxfaststartportbpdufiltermode.is_set or
                    self.stpxfaststartportbpduguardmode.is_set or
                    self.stpxfaststartportenable.is_set or
                    self.stpxfaststartportmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxfaststartportindex.yfilter != YFilter.not_set or
                    self.stpxfaststartportbpdufiltermode.yfilter != YFilter.not_set or
                    self.stpxfaststartportbpduguardmode.yfilter != YFilter.not_set or
                    self.stpxfaststartportenable.yfilter != YFilter.not_set or
                    self.stpxfaststartportmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxFastStartPortEntry" + "[stpxFastStartPortIndex='" + self.stpxfaststartportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxFastStartPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxfaststartportindex.is_set or self.stpxfaststartportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartportindex.get_name_leafdata())
                if (self.stpxfaststartportbpdufiltermode.is_set or self.stpxfaststartportbpdufiltermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartportbpdufiltermode.get_name_leafdata())
                if (self.stpxfaststartportbpduguardmode.is_set or self.stpxfaststartportbpduguardmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartportbpduguardmode.get_name_leafdata())
                if (self.stpxfaststartportenable.is_set or self.stpxfaststartportenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartportenable.get_name_leafdata())
                if (self.stpxfaststartportmode.is_set or self.stpxfaststartportmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartportmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxFastStartPortIndex" or name == "stpxFastStartPortBpduFilterMode" or name == "stpxFastStartPortBpduGuardMode" or name == "stpxFastStartPortEnable" or name == "stpxFastStartPortMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxFastStartPortIndex"):
                    self.stpxfaststartportindex = value
                    self.stpxfaststartportindex.value_namespace = name_space
                    self.stpxfaststartportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartPortBpduFilterMode"):
                    self.stpxfaststartportbpdufiltermode = value
                    self.stpxfaststartportbpdufiltermode.value_namespace = name_space
                    self.stpxfaststartportbpdufiltermode.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartPortBpduGuardMode"):
                    self.stpxfaststartportbpduguardmode = value
                    self.stpxfaststartportbpduguardmode.value_namespace = name_space
                    self.stpxfaststartportbpduguardmode.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartPortEnable"):
                    self.stpxfaststartportenable = value
                    self.stpxfaststartportenable.value_namespace = name_space
                    self.stpxfaststartportenable.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartPortMode"):
                    self.stpxfaststartportmode = value
                    self.stpxfaststartportmode.value_namespace = name_space
                    self.stpxfaststartportmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxfaststartportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxfaststartportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxFastStartPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxFastStartPortEntry"):
                for c in self.stpxfaststartportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxfaststartportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxFastStartPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxfaststartopermodetable(Entity):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        
        .. attribute:: stpxfaststartopermodeentry
        
        	An entry with port fast start oper mode  information on a bridge port for a particular  Spanning Tree Instance
        	**type**\: list of    :py:class:`Stpxfaststartopermodeentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxfaststartopermodetable, self).__init__()

            self.yang_name = "stpxFastStartOperModeTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxfaststartopermodeentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxfaststartopermodetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxfaststartopermodetable, self).__setattr__(name, value)


        class Stpxfaststartopermodeentry(Entity):
            """
            An entry with port fast start oper mode 
            information on a bridge port for a particular 
            Spanning Tree Instance.
            
            .. attribute:: stpxfaststartopermodeinstindex  <key>
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: stpxfaststartopermodeportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartopermode
            
            	Indicates the fast start operational status of the  port on a particular Spanning Tree Instance
            	**type**\:   :py:class:`Stpxfaststartopermode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry.Stpxfaststartopermode>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry, self).__init__()

                self.yang_name = "stpxFastStartOperModeEntry"
                self.yang_parent_name = "stpxFastStartOperModeTable"

                self.stpxfaststartopermodeinstindex = YLeaf(YType.int32, "stpxFastStartOperModeInstIndex")

                self.stpxfaststartopermodeportindex = YLeaf(YType.int32, "stpxFastStartOperModePortIndex")

                self.stpxfaststartopermode = YLeaf(YType.enumeration, "stpxFastStartOperMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxfaststartopermodeinstindex",
                                "stpxfaststartopermodeportindex",
                                "stpxfaststartopermode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry, self).__setattr__(name, value)

            class Stpxfaststartopermode(Enum):
                """
                Stpxfaststartopermode

                Indicates the fast start operational status of the 

                port on a particular Spanning Tree Instance.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            def has_data(self):
                return (
                    self.stpxfaststartopermodeinstindex.is_set or
                    self.stpxfaststartopermodeportindex.is_set or
                    self.stpxfaststartopermode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxfaststartopermodeinstindex.yfilter != YFilter.not_set or
                    self.stpxfaststartopermodeportindex.yfilter != YFilter.not_set or
                    self.stpxfaststartopermode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxFastStartOperModeEntry" + "[stpxFastStartOperModeInstIndex='" + self.stpxfaststartopermodeinstindex.get() + "']" + "[stpxFastStartOperModePortIndex='" + self.stpxfaststartopermodeportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxFastStartOperModeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxfaststartopermodeinstindex.is_set or self.stpxfaststartopermodeinstindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartopermodeinstindex.get_name_leafdata())
                if (self.stpxfaststartopermodeportindex.is_set or self.stpxfaststartopermodeportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartopermodeportindex.get_name_leafdata())
                if (self.stpxfaststartopermode.is_set or self.stpxfaststartopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxfaststartopermode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxFastStartOperModeInstIndex" or name == "stpxFastStartOperModePortIndex" or name == "stpxFastStartOperMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxFastStartOperModeInstIndex"):
                    self.stpxfaststartopermodeinstindex = value
                    self.stpxfaststartopermodeinstindex.value_namespace = name_space
                    self.stpxfaststartopermodeinstindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartOperModePortIndex"):
                    self.stpxfaststartopermodeportindex = value
                    self.stpxfaststartopermodeportindex.value_namespace = name_space
                    self.stpxfaststartopermodeportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxFastStartOperMode"):
                    self.stpxfaststartopermode = value
                    self.stpxfaststartopermode.value_namespace = name_space
                    self.stpxfaststartopermode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxfaststartopermodeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxfaststartopermodeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxFastStartOperModeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxFastStartOperModeEntry"):
                for c in self.stpxfaststartopermodeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxfaststartopermodeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxFastStartOperModeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Stpxbpduskewingentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxbpduskewingtable, self).__init__()

            self.yang_name = "stpxBpduSkewingTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxbpduskewingentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxbpduskewingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxbpduskewingtable, self).__setattr__(name, value)


        class Stpxbpduskewingentry(Entity):
            """
            A Spanning Tree instance on a particular port for
            which BPDU skewing has been detected.
            
            .. attribute:: stpxbpduskewinginstanceindex  <key>
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType  is pvstPlus(1)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: stpxbpduskewingportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxbpduskewinglastskewduration
            
            	Indicates the skew duration in milliseconds of the last BPDU skewing detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: stpxbpduskewingworstskewduration
            
            	Indicates the skew duration in milliseconds of the worst BPDU skewing detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: stpxbpduskewingworstskewtime
            
            	Indicates the value of sysUpTime when the worst BPDU skewing was detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry, self).__init__()

                self.yang_name = "stpxBpduSkewingEntry"
                self.yang_parent_name = "stpxBpduSkewingTable"

                self.stpxbpduskewinginstanceindex = YLeaf(YType.int32, "stpxBpduSkewingInstanceIndex")

                self.stpxbpduskewingportindex = YLeaf(YType.int32, "stpxBpduSkewingPortIndex")

                self.stpxbpduskewinglastskewduration = YLeaf(YType.uint32, "stpxBpduSkewingLastSkewDuration")

                self.stpxbpduskewingworstskewduration = YLeaf(YType.uint32, "stpxBpduSkewingWorstSkewDuration")

                self.stpxbpduskewingworstskewtime = YLeaf(YType.uint32, "stpxBpduSkewingWorstSkewTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxbpduskewinginstanceindex",
                                "stpxbpduskewingportindex",
                                "stpxbpduskewinglastskewduration",
                                "stpxbpduskewingworstskewduration",
                                "stpxbpduskewingworstskewtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxbpduskewinginstanceindex.is_set or
                    self.stpxbpduskewingportindex.is_set or
                    self.stpxbpduskewinglastskewduration.is_set or
                    self.stpxbpduskewingworstskewduration.is_set or
                    self.stpxbpduskewingworstskewtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxbpduskewinginstanceindex.yfilter != YFilter.not_set or
                    self.stpxbpduskewingportindex.yfilter != YFilter.not_set or
                    self.stpxbpduskewinglastskewduration.yfilter != YFilter.not_set or
                    self.stpxbpduskewingworstskewduration.yfilter != YFilter.not_set or
                    self.stpxbpduskewingworstskewtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxBpduSkewingEntry" + "[stpxBpduSkewingInstanceIndex='" + self.stpxbpduskewinginstanceindex.get() + "']" + "[stpxBpduSkewingPortIndex='" + self.stpxbpduskewingportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxBpduSkewingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxbpduskewinginstanceindex.is_set or self.stpxbpduskewinginstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxbpduskewinginstanceindex.get_name_leafdata())
                if (self.stpxbpduskewingportindex.is_set or self.stpxbpduskewingportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxbpduskewingportindex.get_name_leafdata())
                if (self.stpxbpduskewinglastskewduration.is_set or self.stpxbpduskewinglastskewduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxbpduskewinglastskewduration.get_name_leafdata())
                if (self.stpxbpduskewingworstskewduration.is_set or self.stpxbpduskewingworstskewduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxbpduskewingworstskewduration.get_name_leafdata())
                if (self.stpxbpduskewingworstskewtime.is_set or self.stpxbpduskewingworstskewtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxbpduskewingworstskewtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxBpduSkewingInstanceIndex" or name == "stpxBpduSkewingPortIndex" or name == "stpxBpduSkewingLastSkewDuration" or name == "stpxBpduSkewingWorstSkewDuration" or name == "stpxBpduSkewingWorstSkewTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxBpduSkewingInstanceIndex"):
                    self.stpxbpduskewinginstanceindex = value
                    self.stpxbpduskewinginstanceindex.value_namespace = name_space
                    self.stpxbpduskewinginstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxBpduSkewingPortIndex"):
                    self.stpxbpduskewingportindex = value
                    self.stpxbpduskewingportindex.value_namespace = name_space
                    self.stpxbpduskewingportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxBpduSkewingLastSkewDuration"):
                    self.stpxbpduskewinglastskewduration = value
                    self.stpxbpduskewinglastskewduration.value_namespace = name_space
                    self.stpxbpduskewinglastskewduration.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxBpduSkewingWorstSkewDuration"):
                    self.stpxbpduskewingworstskewduration = value
                    self.stpxbpduskewingworstskewduration.value_namespace = name_space
                    self.stpxbpduskewingworstskewduration.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxBpduSkewingWorstSkewTime"):
                    self.stpxbpduskewingworstskewtime = value
                    self.stpxbpduskewingworstskewtime.value_namespace = name_space
                    self.stpxbpduskewingworstskewtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxbpduskewingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxbpduskewingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxBpduSkewingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxBpduSkewingEntry"):
                for c in self.stpxbpduskewingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxbpduskewingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxBpduSkewingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxmstinstancetable(Entity):
        """
        This table contains MST instance information with
        one entry for an MST instance within the range of 
        0 to the object value of stpxMSTMaxInstanceNumber. 
        
        This table is deprecated and replaced by 
        stpxSMSTInstanceTable.
        
        .. attribute:: stpxmstinstanceentry
        
        	A conceptual row containing the MST instance  information
        	**type**\: list of    :py:class:`Stpxmstinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmstinstancetable, self).__init__()

            self.yang_name = "stpxMSTInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmstinstanceentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxmstinstancetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmstinstancetable, self).__setattr__(name, value)


        class Stpxmstinstanceentry(Entity):
            """
            A conceptual row containing the MST instance 
            information.
            
            .. attribute:: stpxmstinstanceindex  <key>
            
            	An integer that uniquely identifies an MST instance  within the range of 0 to the object value of stpxMSTMaxInstanceNumber.  This object is deprecated and replaced by  stpxSMSTInstanceIndex
            	**type**\:  int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance.  This object will take on value of 40 if the object value of stpxSMSTInstanceRemainingHopCount is greater than 40.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTInstanceRemainingHopCount
            	**type**\:  int
            
            	**range:** 0..40
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped3k4k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by stpxSMSTInstanceVlansMapped3k4k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry, self).__init__()

                self.yang_name = "stpxMSTInstanceEntry"
                self.yang_parent_name = "stpxMSTInstanceTable"

                self.stpxmstinstanceindex = YLeaf(YType.int32, "stpxMSTInstanceIndex")

                self.stpxmstinstanceremaininghopcount = YLeaf(YType.int32, "stpxMSTInstanceRemainingHopCount")

                self.stpxmstinstancevlansmapped = YLeaf(YType.str, "stpxMSTInstanceVlansMapped")

                self.stpxmstinstancevlansmapped2k = YLeaf(YType.str, "stpxMSTInstanceVlansMapped2k")

                self.stpxmstinstancevlansmapped3k = YLeaf(YType.str, "stpxMSTInstanceVlansMapped3k")

                self.stpxmstinstancevlansmapped4k = YLeaf(YType.str, "stpxMSTInstanceVlansMapped4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxmstinstanceindex",
                                "stpxmstinstanceremaininghopcount",
                                "stpxmstinstancevlansmapped",
                                "stpxmstinstancevlansmapped2k",
                                "stpxmstinstancevlansmapped3k",
                                "stpxmstinstancevlansmapped4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxmstinstanceindex.is_set or
                    self.stpxmstinstanceremaininghopcount.is_set or
                    self.stpxmstinstancevlansmapped.is_set or
                    self.stpxmstinstancevlansmapped2k.is_set or
                    self.stpxmstinstancevlansmapped3k.is_set or
                    self.stpxmstinstancevlansmapped4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxmstinstanceindex.yfilter != YFilter.not_set or
                    self.stpxmstinstanceremaininghopcount.yfilter != YFilter.not_set or
                    self.stpxmstinstancevlansmapped.yfilter != YFilter.not_set or
                    self.stpxmstinstancevlansmapped2k.yfilter != YFilter.not_set or
                    self.stpxmstinstancevlansmapped3k.yfilter != YFilter.not_set or
                    self.stpxmstinstancevlansmapped4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxMSTInstanceEntry" + "[stpxMSTInstanceIndex='" + self.stpxmstinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTInstanceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxmstinstanceindex.is_set or self.stpxmstinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceindex.get_name_leafdata())
                if (self.stpxmstinstanceremaininghopcount.is_set or self.stpxmstinstanceremaininghopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceremaininghopcount.get_name_leafdata())
                if (self.stpxmstinstancevlansmapped.is_set or self.stpxmstinstancevlansmapped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstancevlansmapped.get_name_leafdata())
                if (self.stpxmstinstancevlansmapped2k.is_set or self.stpxmstinstancevlansmapped2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstancevlansmapped2k.get_name_leafdata())
                if (self.stpxmstinstancevlansmapped3k.is_set or self.stpxmstinstancevlansmapped3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstancevlansmapped3k.get_name_leafdata())
                if (self.stpxmstinstancevlansmapped4k.is_set or self.stpxmstinstancevlansmapped4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstancevlansmapped4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxMSTInstanceIndex" or name == "stpxMSTInstanceRemainingHopCount" or name == "stpxMSTInstanceVlansMapped" or name == "stpxMSTInstanceVlansMapped2k" or name == "stpxMSTInstanceVlansMapped3k" or name == "stpxMSTInstanceVlansMapped4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxMSTInstanceIndex"):
                    self.stpxmstinstanceindex = value
                    self.stpxmstinstanceindex.value_namespace = name_space
                    self.stpxmstinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceRemainingHopCount"):
                    self.stpxmstinstanceremaininghopcount = value
                    self.stpxmstinstanceremaininghopcount.value_namespace = name_space
                    self.stpxmstinstanceremaininghopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceVlansMapped"):
                    self.stpxmstinstancevlansmapped = value
                    self.stpxmstinstancevlansmapped.value_namespace = name_space
                    self.stpxmstinstancevlansmapped.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceVlansMapped2k"):
                    self.stpxmstinstancevlansmapped2k = value
                    self.stpxmstinstancevlansmapped2k.value_namespace = name_space
                    self.stpxmstinstancevlansmapped2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceVlansMapped3k"):
                    self.stpxmstinstancevlansmapped3k = value
                    self.stpxmstinstancevlansmapped3k.value_namespace = name_space
                    self.stpxmstinstancevlansmapped3k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceVlansMapped4k"):
                    self.stpxmstinstancevlansmapped4k = value
                    self.stpxmstinstancevlansmapped4k.value_namespace = name_space
                    self.stpxmstinstancevlansmapped4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxmstinstanceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxmstinstanceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMSTInstanceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxMSTInstanceEntry"):
                for c in self.stpxmstinstanceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxmstinstanceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMSTInstanceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Stpxmstinstanceeditentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmstinstanceedittable, self).__init__()

            self.yang_name = "stpxMSTInstanceEditTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmstinstanceeditentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxmstinstanceedittable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmstinstanceedittable, self).__setattr__(name, value)


        class Stpxmstinstanceeditentry(Entity):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            .. attribute:: stpxmstinstanceeditindex  <key>
            
            	An integer that uniquely identifies an MST instance  from 0 to the object value of stpxMSTMaxInstanceNumber.  The instances of this table entry with  stpxMSTInstanceEditIndex of zero can not be  modified.  This object is deprecated and replaced by  stpxSMSTInstanceEditIndex
            	**type**\:  int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap3k4k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstinstanceeditvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by stpxSMSTInstanceEditVlansMap3k4k
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry, self).__init__()

                self.yang_name = "stpxMSTInstanceEditEntry"
                self.yang_parent_name = "stpxMSTInstanceEditTable"

                self.stpxmstinstanceeditindex = YLeaf(YType.int32, "stpxMSTInstanceEditIndex")

                self.stpxmstinstanceeditvlansmap = YLeaf(YType.str, "stpxMSTInstanceEditVlansMap")

                self.stpxmstinstanceeditvlansmap2k = YLeaf(YType.str, "stpxMSTInstanceEditVlansMap2k")

                self.stpxmstinstanceeditvlansmap3k = YLeaf(YType.str, "stpxMSTInstanceEditVlansMap3k")

                self.stpxmstinstanceeditvlansmap4k = YLeaf(YType.str, "stpxMSTInstanceEditVlansMap4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxmstinstanceeditindex",
                                "stpxmstinstanceeditvlansmap",
                                "stpxmstinstanceeditvlansmap2k",
                                "stpxmstinstanceeditvlansmap3k",
                                "stpxmstinstanceeditvlansmap4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxmstinstanceeditindex.is_set or
                    self.stpxmstinstanceeditvlansmap.is_set or
                    self.stpxmstinstanceeditvlansmap2k.is_set or
                    self.stpxmstinstanceeditvlansmap3k.is_set or
                    self.stpxmstinstanceeditvlansmap4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxmstinstanceeditindex.yfilter != YFilter.not_set or
                    self.stpxmstinstanceeditvlansmap.yfilter != YFilter.not_set or
                    self.stpxmstinstanceeditvlansmap2k.yfilter != YFilter.not_set or
                    self.stpxmstinstanceeditvlansmap3k.yfilter != YFilter.not_set or
                    self.stpxmstinstanceeditvlansmap4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxMSTInstanceEditEntry" + "[stpxMSTInstanceEditIndex='" + self.stpxmstinstanceeditindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTInstanceEditTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxmstinstanceeditindex.is_set or self.stpxmstinstanceeditindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceeditindex.get_name_leafdata())
                if (self.stpxmstinstanceeditvlansmap.is_set or self.stpxmstinstanceeditvlansmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceeditvlansmap.get_name_leafdata())
                if (self.stpxmstinstanceeditvlansmap2k.is_set or self.stpxmstinstanceeditvlansmap2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceeditvlansmap2k.get_name_leafdata())
                if (self.stpxmstinstanceeditvlansmap3k.is_set or self.stpxmstinstanceeditvlansmap3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceeditvlansmap3k.get_name_leafdata())
                if (self.stpxmstinstanceeditvlansmap4k.is_set or self.stpxmstinstanceeditvlansmap4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstinstanceeditvlansmap4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxMSTInstanceEditIndex" or name == "stpxMSTInstanceEditVlansMap" or name == "stpxMSTInstanceEditVlansMap2k" or name == "stpxMSTInstanceEditVlansMap3k" or name == "stpxMSTInstanceEditVlansMap4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxMSTInstanceEditIndex"):
                    self.stpxmstinstanceeditindex = value
                    self.stpxmstinstanceeditindex.value_namespace = name_space
                    self.stpxmstinstanceeditindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceEditVlansMap"):
                    self.stpxmstinstanceeditvlansmap = value
                    self.stpxmstinstanceeditvlansmap.value_namespace = name_space
                    self.stpxmstinstanceeditvlansmap.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceEditVlansMap2k"):
                    self.stpxmstinstanceeditvlansmap2k = value
                    self.stpxmstinstanceeditvlansmap2k.value_namespace = name_space
                    self.stpxmstinstanceeditvlansmap2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceEditVlansMap3k"):
                    self.stpxmstinstanceeditvlansmap3k = value
                    self.stpxmstinstanceeditvlansmap3k.value_namespace = name_space
                    self.stpxmstinstanceeditvlansmap3k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTInstanceEditVlansMap4k"):
                    self.stpxmstinstanceeditvlansmap4k = value
                    self.stpxmstinstanceeditvlansmap4k.value_namespace = name_space
                    self.stpxmstinstanceeditvlansmap4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxmstinstanceeditentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxmstinstanceeditentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMSTInstanceEditTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxMSTInstanceEditEntry"):
                for c in self.stpxmstinstanceeditentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxmstinstanceeditentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMSTInstanceEditEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxmstporttable(Entity):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        .. attribute:: stpxmstportentry
        
        	An entry with port information for the MST Protocol on a bridge port
        	**type**\: list of    :py:class:`Stpxmstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmstporttable, self).__init__()

            self.yang_name = "stpxMSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmstportentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxmstporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmstporttable, self).__setattr__(name, value)


        class Stpxmstportentry(Entity):
            """
            An entry with port information for the MST Protocol
            on a bridge port.
            
            .. attribute:: stpxmstportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the MST protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5). stpxMSTPortAdminLinkType is deprecated and replaced  with stpxRSTPPortAdminLinkType
            	**type**\:   :py:class:`Stpxmstportadminlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.Stpxmstportadminlinktype>`
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportoperlinktype
            
            	Indicates the operational link type of a bridge port for the MST protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  stpxMSTPortOperLinkType  is deprecated and replaced with stpxRSTPPortOperLinkType
            	**type**\:   :py:class:`Stpxmstportoperlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.Stpxmstportoperlinktype>`
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to this  object has no effect. Setting false(2) to this object has  no effect. This object always returns false(2) when read. stpxMSTPortProtocolMigration is deprecated and  replaced with stpxRSTPPortProtocolMigration
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTPortStatus
            	**type**\:   :py:class:`Stpxmstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.Stpxmstportstatus>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry, self).__init__()

                self.yang_name = "stpxMSTPortEntry"
                self.yang_parent_name = "stpxMSTPortTable"

                self.stpxmstportindex = YLeaf(YType.int32, "stpxMSTPortIndex")

                self.stpxmstportadminlinktype = YLeaf(YType.enumeration, "stpxMSTPortAdminLinkType")

                self.stpxmstportoperlinktype = YLeaf(YType.enumeration, "stpxMSTPortOperLinkType")

                self.stpxmstportprotocolmigration = YLeaf(YType.boolean, "stpxMSTPortProtocolMigration")

                self.stpxmstportstatus = YLeaf(YType.bits, "stpxMSTPortStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxmstportindex",
                                "stpxmstportadminlinktype",
                                "stpxmstportoperlinktype",
                                "stpxmstportprotocolmigration",
                                "stpxmstportstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry, self).__setattr__(name, value)

            class Stpxmstportadminlinktype(Enum):
                """
                Stpxmstportadminlinktype

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
                Stpxmstportoperlinktype

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


            def has_data(self):
                return (
                    self.stpxmstportindex.is_set or
                    self.stpxmstportadminlinktype.is_set or
                    self.stpxmstportoperlinktype.is_set or
                    self.stpxmstportprotocolmigration.is_set or
                    self.stpxmstportstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxmstportindex.yfilter != YFilter.not_set or
                    self.stpxmstportadminlinktype.yfilter != YFilter.not_set or
                    self.stpxmstportoperlinktype.yfilter != YFilter.not_set or
                    self.stpxmstportprotocolmigration.yfilter != YFilter.not_set or
                    self.stpxmstportstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxMSTPortEntry" + "[stpxMSTPortIndex='" + self.stpxmstportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxmstportindex.is_set or self.stpxmstportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportindex.get_name_leafdata())
                if (self.stpxmstportadminlinktype.is_set or self.stpxmstportadminlinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportadminlinktype.get_name_leafdata())
                if (self.stpxmstportoperlinktype.is_set or self.stpxmstportoperlinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportoperlinktype.get_name_leafdata())
                if (self.stpxmstportprotocolmigration.is_set or self.stpxmstportprotocolmigration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportprotocolmigration.get_name_leafdata())
                if (self.stpxmstportstatus.is_set or self.stpxmstportstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxMSTPortIndex" or name == "stpxMSTPortAdminLinkType" or name == "stpxMSTPortOperLinkType" or name == "stpxMSTPortProtocolMigration" or name == "stpxMSTPortStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxMSTPortIndex"):
                    self.stpxmstportindex = value
                    self.stpxmstportindex.value_namespace = name_space
                    self.stpxmstportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortAdminLinkType"):
                    self.stpxmstportadminlinktype = value
                    self.stpxmstportadminlinktype.value_namespace = name_space
                    self.stpxmstportadminlinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortOperLinkType"):
                    self.stpxmstportoperlinktype = value
                    self.stpxmstportoperlinktype.value_namespace = name_space
                    self.stpxmstportoperlinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortProtocolMigration"):
                    self.stpxmstportprotocolmigration = value
                    self.stpxmstportprotocolmigration.value_namespace = name_space
                    self.stpxmstportprotocolmigration.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortStatus"):
                    self.stpxmstportstatus[value] = True

        def has_data(self):
            for c in self.stpxmstportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxmstportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMSTPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxMSTPortEntry"):
                for c in self.stpxmstportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxmstportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMSTPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxmstportroletable(Entity):
        """
        A table containing a list of the bridge ports for a 
        particular MST instance.  This table is only instantiated 
        when the stpxSpanningTreeType is mst(4). 
        
        This table is deprecated and replaced with 
        stpxRSTPPortRoleTable.
        
        .. attribute:: stpxmstportroleentry
        
        	An entry containing the port role information for the MST protocol on a port for a particular MST instance existing on the system
        	**type**\: list of    :py:class:`Stpxmstportroleentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxmstportroletable, self).__init__()

            self.yang_name = "stpxMSTPortRoleTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxmstportroleentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxmstportroletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxmstportroletable, self).__setattr__(name, value)


        class Stpxmstportroleentry(Entity):
            """
            An entry containing the port role information for the MST
            protocol on a port for a particular MST instance existing
            on the system.
            
            .. attribute:: stpxmstportroleinstanceindex  <key>
            
            	The MST instance id within the range of 0 to stpxMSTMaxInstanceNumber
            	**type**\:  int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportroleportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: stpxmstportrolevalue
            
            	Indicates the port role on a particular MST instance for the MST protocol.   disabled \-\-  this port has no role on this MST instance.   root \-\- this port has the role of root port on this MST             instance.   designated \-\- this port has the role of designated              port on this MST instance.  alternate \-\- this port has the role of alternate port             on this MST instance.  backUp \-\- this port has the role of backup port on this               MST instance.  boundary \-\- this port has the role of boundary port on              this MST instance.  master \-\- this port has the role of master port on           this MST instance
            	**type**\:   :py:class:`Stpxmstportrolevalue <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry.Stpxmstportrolevalue>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry, self).__init__()

                self.yang_name = "stpxMSTPortRoleEntry"
                self.yang_parent_name = "stpxMSTPortRoleTable"

                self.stpxmstportroleinstanceindex = YLeaf(YType.int32, "stpxMSTPortRoleInstanceIndex")

                self.stpxmstportroleportindex = YLeaf(YType.int32, "stpxMSTPortRolePortIndex")

                self.stpxmstportrolevalue = YLeaf(YType.enumeration, "stpxMSTPortRoleValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxmstportroleinstanceindex",
                                "stpxmstportroleportindex",
                                "stpxmstportrolevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry, self).__setattr__(name, value)

            class Stpxmstportrolevalue(Enum):
                """
                Stpxmstportrolevalue

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


            def has_data(self):
                return (
                    self.stpxmstportroleinstanceindex.is_set or
                    self.stpxmstportroleportindex.is_set or
                    self.stpxmstportrolevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxmstportroleinstanceindex.yfilter != YFilter.not_set or
                    self.stpxmstportroleportindex.yfilter != YFilter.not_set or
                    self.stpxmstportrolevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxMSTPortRoleEntry" + "[stpxMSTPortRoleInstanceIndex='" + self.stpxmstportroleinstanceindex.get() + "']" + "[stpxMSTPortRolePortIndex='" + self.stpxmstportroleportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxMSTPortRoleTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxmstportroleinstanceindex.is_set or self.stpxmstportroleinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportroleinstanceindex.get_name_leafdata())
                if (self.stpxmstportroleportindex.is_set or self.stpxmstportroleportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportroleportindex.get_name_leafdata())
                if (self.stpxmstportrolevalue.is_set or self.stpxmstportrolevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxmstportrolevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxMSTPortRoleInstanceIndex" or name == "stpxMSTPortRolePortIndex" or name == "stpxMSTPortRoleValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxMSTPortRoleInstanceIndex"):
                    self.stpxmstportroleinstanceindex = value
                    self.stpxmstportroleinstanceindex.value_namespace = name_space
                    self.stpxmstportroleinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortRolePortIndex"):
                    self.stpxmstportroleportindex = value
                    self.stpxmstportroleportindex.value_namespace = name_space
                    self.stpxmstportroleportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxMSTPortRoleValue"):
                    self.stpxmstportrolevalue = value
                    self.stpxmstportrolevalue.value_namespace = name_space
                    self.stpxmstportrolevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxmstportroleentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxmstportroleentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxMSTPortRoleTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxMSTPortRoleEntry"):
                for c in self.stpxmstportroleentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxmstportroleentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxMSTPortRoleEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxrstpporttable(Entity):
        """
        A table containing port information for the RSTP 
        Protocol on all the bridge ports existing in the 
        system.
        
        .. attribute:: stpxrstpportentry
        
        	An entry with port information for the RSTP Protocol on a bridge port
        	**type**\: list of    :py:class:`Stpxrstpportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrstpporttable, self).__init__()

            self.yang_name = "stpxRSTPPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrstpportentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxrstpporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrstpporttable, self).__setattr__(name, value)


        class Stpxrstpportentry(Entity):
            """
            An entry with port information for the RSTP Protocol
            on a bridge port.
            
            .. attribute:: stpxrstpportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the RSTP protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\:   :py:class:`Stpxrstpportadminlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.Stpxrstpportadminlinktype>`
            
            .. attribute:: stpxrstpportoperlinktype
            
            	Indicates the operational link type of a bridge port for the RSTP protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\:   :py:class:`Stpxrstpportoperlinktype <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.Stpxrstpportoperlinktype>`
            
            .. attribute:: stpxrstpportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to  this object has no effect. Setting false(2) to this  object has no effect. This object always returns  false(2) when read
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry, self).__init__()

                self.yang_name = "stpxRSTPPortEntry"
                self.yang_parent_name = "stpxRSTPPortTable"

                self.stpxrstpportindex = YLeaf(YType.int32, "stpxRSTPPortIndex")

                self.stpxrstpportadminlinktype = YLeaf(YType.enumeration, "stpxRSTPPortAdminLinkType")

                self.stpxrstpportoperlinktype = YLeaf(YType.enumeration, "stpxRSTPPortOperLinkType")

                self.stpxrstpportprotocolmigration = YLeaf(YType.boolean, "stpxRSTPPortProtocolMigration")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxrstpportindex",
                                "stpxrstpportadminlinktype",
                                "stpxrstpportoperlinktype",
                                "stpxrstpportprotocolmigration") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry, self).__setattr__(name, value)

            class Stpxrstpportadminlinktype(Enum):
                """
                Stpxrstpportadminlinktype

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
                Stpxrstpportoperlinktype

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


            def has_data(self):
                return (
                    self.stpxrstpportindex.is_set or
                    self.stpxrstpportadminlinktype.is_set or
                    self.stpxrstpportoperlinktype.is_set or
                    self.stpxrstpportprotocolmigration.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxrstpportindex.yfilter != YFilter.not_set or
                    self.stpxrstpportadminlinktype.yfilter != YFilter.not_set or
                    self.stpxrstpportoperlinktype.yfilter != YFilter.not_set or
                    self.stpxrstpportprotocolmigration.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxRSTPPortEntry" + "[stpxRSTPPortIndex='" + self.stpxrstpportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRSTPPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxrstpportindex.is_set or self.stpxrstpportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportindex.get_name_leafdata())
                if (self.stpxrstpportadminlinktype.is_set or self.stpxrstpportadminlinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportadminlinktype.get_name_leafdata())
                if (self.stpxrstpportoperlinktype.is_set or self.stpxrstpportoperlinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportoperlinktype.get_name_leafdata())
                if (self.stpxrstpportprotocolmigration.is_set or self.stpxrstpportprotocolmigration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportprotocolmigration.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxRSTPPortIndex" or name == "stpxRSTPPortAdminLinkType" or name == "stpxRSTPPortOperLinkType" or name == "stpxRSTPPortProtocolMigration"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxRSTPPortIndex"):
                    self.stpxrstpportindex = value
                    self.stpxrstpportindex.value_namespace = name_space
                    self.stpxrstpportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRSTPPortAdminLinkType"):
                    self.stpxrstpportadminlinktype = value
                    self.stpxrstpportadminlinktype.value_namespace = name_space
                    self.stpxrstpportadminlinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRSTPPortOperLinkType"):
                    self.stpxrstpportoperlinktype = value
                    self.stpxrstpportoperlinktype.value_namespace = name_space
                    self.stpxrstpportoperlinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRSTPPortProtocolMigration"):
                    self.stpxrstpportprotocolmigration = value
                    self.stpxrstpportprotocolmigration.value_namespace = name_space
                    self.stpxrstpportprotocolmigration.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxrstpportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxrstpportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRSTPPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxRSTPPortEntry"):
                for c in self.stpxrstpportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxrstpportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRSTPPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxrstpportroletable(Entity):
        """
        A table containing a list of the bridge ports for a 
        particular Spanning Tree instance.  This table is 
        only instantiated when the stpxSpanningTreeType is mst(4) 
        or rapidPvstPlus(5).
        
        .. attribute:: stpxrstpportroleentry
        
        	An entry containing the port role information for the RSTP protocol on a port for a particular Spanning Tree instance
        	**type**\: list of    :py:class:`Stpxrstpportroleentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrstpportroletable, self).__init__()

            self.yang_name = "stpxRSTPPortRoleTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrstpportroleentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxrstpportroletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrstpportroletable, self).__setattr__(name, value)


        class Stpxrstpportroleentry(Entity):
            """
            An entry containing the port role information for the RSTP
            protocol on a port for a particular Spanning Tree instance.
            
            .. attribute:: stpxrstpportroleinstanceindex  <key>
            
            	The Spanning Tree instance id, it can either be a  VLAN number if the stpxSpanningTreeType is rapidPvstPlus(5)  or an MST instance id if the stpxSpanningTreeType is mst(4)
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrstpportroleportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportrolevalue
            
            	Indicates the port role on a particular Spanning Tree  instance for the RSTP protocol.   disabled \-\-  this port has no role in this Spanning             Tree instance.   root \-\- this port has the role of root port in this             Spanning Tree instance.   designated \-\- this port has the role of designated              port in this Spanning Tree instance.  alternate \-\- this port has the role of alternate port             in this Spanning Tree instance.  backUp \-\- this port has the role of backup port in this               Spanning Tree instance.  boundary \-\- this port has the role of boundary port in              this Spanning Tree instance.  master \-\- this port has the role of master port in             this Spanning Tree instance.  This object could have a value of 'boundary' or 'master' only when the object value of stpxSpanningTreeType is mst(4)
            	**type**\:   :py:class:`Stpxrstpportrolevalue <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry.Stpxrstpportrolevalue>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry, self).__init__()

                self.yang_name = "stpxRSTPPortRoleEntry"
                self.yang_parent_name = "stpxRSTPPortRoleTable"

                self.stpxrstpportroleinstanceindex = YLeaf(YType.int32, "stpxRSTPPortRoleInstanceIndex")

                self.stpxrstpportroleportindex = YLeaf(YType.int32, "stpxRSTPPortRolePortIndex")

                self.stpxrstpportrolevalue = YLeaf(YType.enumeration, "stpxRSTPPortRoleValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxrstpportroleinstanceindex",
                                "stpxrstpportroleportindex",
                                "stpxrstpportrolevalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry, self).__setattr__(name, value)

            class Stpxrstpportrolevalue(Enum):
                """
                Stpxrstpportrolevalue

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


            def has_data(self):
                return (
                    self.stpxrstpportroleinstanceindex.is_set or
                    self.stpxrstpportroleportindex.is_set or
                    self.stpxrstpportrolevalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxrstpportroleinstanceindex.yfilter != YFilter.not_set or
                    self.stpxrstpportroleportindex.yfilter != YFilter.not_set or
                    self.stpxrstpportrolevalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxRSTPPortRoleEntry" + "[stpxRSTPPortRoleInstanceIndex='" + self.stpxrstpportroleinstanceindex.get() + "']" + "[stpxRSTPPortRolePortIndex='" + self.stpxrstpportroleportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRSTPPortRoleTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxrstpportroleinstanceindex.is_set or self.stpxrstpportroleinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportroleinstanceindex.get_name_leafdata())
                if (self.stpxrstpportroleportindex.is_set or self.stpxrstpportroleportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportroleportindex.get_name_leafdata())
                if (self.stpxrstpportrolevalue.is_set or self.stpxrstpportrolevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrstpportrolevalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxRSTPPortRoleInstanceIndex" or name == "stpxRSTPPortRolePortIndex" or name == "stpxRSTPPortRoleValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxRSTPPortRoleInstanceIndex"):
                    self.stpxrstpportroleinstanceindex = value
                    self.stpxrstpportroleinstanceindex.value_namespace = name_space
                    self.stpxrstpportroleinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRSTPPortRolePortIndex"):
                    self.stpxrstpportroleportindex = value
                    self.stpxrstpportroleportindex.value_namespace = name_space
                    self.stpxrstpportroleportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRSTPPortRoleValue"):
                    self.stpxrstpportrolevalue = value
                    self.stpxrstpportrolevalue.value_namespace = name_space
                    self.stpxrstpportrolevalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxrstpportroleentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxrstpportroleentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRSTPPortRoleTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxRSTPPortRoleEntry"):
                for c in self.stpxrstpportroleentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxrstpportroleentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRSTPPortRoleEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxrpvstporttable(Entity):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        This table is only instantiated when the object value
        of stpxSpanningTreeType is rapidPvstPlus(5).
        
        .. attribute:: stpxrpvstportentry
        
        	An entry with port status information on a  bridge port for a particular Spanning Tree  Instance
        	**type**\: list of    :py:class:`Stpxrpvstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxrpvstporttable, self).__init__()

            self.yang_name = "stpxRPVSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxrpvstportentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxrpvstporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxrpvstporttable, self).__setattr__(name, value)


        class Stpxrpvstportentry(Entity):
            """
            An entry with port status information on a 
            bridge port for a particular Spanning Tree 
            Instance.
            
            .. attribute:: stpxrpvstportvlanindex  <key>
            
            	The VLAN id of the VLAN
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrpvstportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrpvstportstatus
            
            	Indicates the operational status of the port for the  Rapid PVST+ protocol.  edge \-\- this port is an edge port for the RST region.  unused1 \-\- unused bit 1.  unused2 \-\- unused bit 2.  stp \-\- this port is connected to a Single Spanning        Tree/PVST+ bridge.  dispute \-\- this port, as a designated port, received an        inferior BPDU with a designated role and the        learning bit being set
            	**type**\:   :py:class:`Stpxrpvstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry.Stpxrpvstportstatus>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry, self).__init__()

                self.yang_name = "stpxRPVSTPortEntry"
                self.yang_parent_name = "stpxRPVSTPortTable"

                self.stpxrpvstportvlanindex = YLeaf(YType.int32, "stpxRPVSTPortVlanIndex")

                self.stpxrpvstportindex = YLeaf(YType.int32, "stpxRPVSTPortIndex")

                self.stpxrpvstportstatus = YLeaf(YType.bits, "stpxRPVSTPortStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxrpvstportvlanindex",
                                "stpxrpvstportindex",
                                "stpxrpvstportstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxrpvstportvlanindex.is_set or
                    self.stpxrpvstportindex.is_set or
                    self.stpxrpvstportstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxrpvstportvlanindex.yfilter != YFilter.not_set or
                    self.stpxrpvstportindex.yfilter != YFilter.not_set or
                    self.stpxrpvstportstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxRPVSTPortEntry" + "[stpxRPVSTPortVlanIndex='" + self.stpxrpvstportvlanindex.get() + "']" + "[stpxRPVSTPortIndex='" + self.stpxrpvstportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxRPVSTPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxrpvstportvlanindex.is_set or self.stpxrpvstportvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrpvstportvlanindex.get_name_leafdata())
                if (self.stpxrpvstportindex.is_set or self.stpxrpvstportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrpvstportindex.get_name_leafdata())
                if (self.stpxrpvstportstatus.is_set or self.stpxrpvstportstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxrpvstportstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxRPVSTPortVlanIndex" or name == "stpxRPVSTPortIndex" or name == "stpxRPVSTPortStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxRPVSTPortVlanIndex"):
                    self.stpxrpvstportvlanindex = value
                    self.stpxrpvstportvlanindex.value_namespace = name_space
                    self.stpxrpvstportvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRPVSTPortIndex"):
                    self.stpxrpvstportindex = value
                    self.stpxrpvstportindex.value_namespace = name_space
                    self.stpxrpvstportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxRPVSTPortStatus"):
                    self.stpxrpvstportstatus[value] = True

        def has_data(self):
            for c in self.stpxrpvstportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxrpvstportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxRPVSTPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxRPVSTPortEntry"):
                for c in self.stpxrpvstportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxrpvstportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxRPVSTPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxsmstinstancetable(Entity):
        """
        This table contains MST instance information
        for IEEE MST.
        
        .. attribute:: stpxsmstinstanceentry
        
        	A conceptual row containing the MST instance  information for IEEE MST
        	**type**\: list of    :py:class:`Stpxsmstinstanceentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxsmstinstancetable, self).__init__()

            self.yang_name = "stpxSMSTInstanceTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxsmstinstanceentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxsmstinstancetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxsmstinstancetable, self).__setattr__(name, value)


        class Stpxsmstinstanceentry(Entity):
            """
            A conceptual row containing the MST instance 
            information for IEEE MST.
            
            .. attribute:: stpxsmstinstanceindex  <key>
            
            	The MST instance ID, the value of which is in the range  from 0 to stpxSMSTMaxInstanceID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstancecistintrootcost
            
            	Indicates the CIST Internal Root Path Cost, i.e., the path cost to the CIST Regional Root as specified by the corresponding stpxSMSTInstanceCISTRegionalRoot for the  MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstancecistregionalroot
            
            	Indicates the Bridge Identifier (refer to BridgeId  defined in BRIDGE\-MIB) of CIST (Common and Internal  Spanning Tree) Regional Root for the MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: stpxsmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance. If this object value is not applicable on an MST instance, then the value retrieved for this object for that MST instance will be \-1.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4)
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: stpxsmstinstancevlansmapped1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstancevlansmapped3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry, self).__init__()

                self.yang_name = "stpxSMSTInstanceEntry"
                self.yang_parent_name = "stpxSMSTInstanceTable"

                self.stpxsmstinstanceindex = YLeaf(YType.uint32, "stpxSMSTInstanceIndex")

                self.stpxsmstinstancecistintrootcost = YLeaf(YType.uint32, "stpxSMSTInstanceCISTIntRootCost")

                self.stpxsmstinstancecistregionalroot = YLeaf(YType.str, "stpxSMSTInstanceCISTRegionalRoot")

                self.stpxsmstinstanceremaininghopcount = YLeaf(YType.int32, "stpxSMSTInstanceRemainingHopCount")

                self.stpxsmstinstancevlansmapped1k2k = YLeaf(YType.str, "stpxSMSTInstanceVlansMapped1k2k")

                self.stpxsmstinstancevlansmapped3k4k = YLeaf(YType.str, "stpxSMSTInstanceVlansMapped3k4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxsmstinstanceindex",
                                "stpxsmstinstancecistintrootcost",
                                "stpxsmstinstancecistregionalroot",
                                "stpxsmstinstanceremaininghopcount",
                                "stpxsmstinstancevlansmapped1k2k",
                                "stpxsmstinstancevlansmapped3k4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxsmstinstanceindex.is_set or
                    self.stpxsmstinstancecistintrootcost.is_set or
                    self.stpxsmstinstancecistregionalroot.is_set or
                    self.stpxsmstinstanceremaininghopcount.is_set or
                    self.stpxsmstinstancevlansmapped1k2k.is_set or
                    self.stpxsmstinstancevlansmapped3k4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceindex.yfilter != YFilter.not_set or
                    self.stpxsmstinstancecistintrootcost.yfilter != YFilter.not_set or
                    self.stpxsmstinstancecistregionalroot.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceremaininghopcount.yfilter != YFilter.not_set or
                    self.stpxsmstinstancevlansmapped1k2k.yfilter != YFilter.not_set or
                    self.stpxsmstinstancevlansmapped3k4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxSMSTInstanceEntry" + "[stpxSMSTInstanceIndex='" + self.stpxsmstinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTInstanceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxsmstinstanceindex.is_set or self.stpxsmstinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceindex.get_name_leafdata())
                if (self.stpxsmstinstancecistintrootcost.is_set or self.stpxsmstinstancecistintrootcost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstancecistintrootcost.get_name_leafdata())
                if (self.stpxsmstinstancecistregionalroot.is_set or self.stpxsmstinstancecistregionalroot.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstancecistregionalroot.get_name_leafdata())
                if (self.stpxsmstinstanceremaininghopcount.is_set or self.stpxsmstinstanceremaininghopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceremaininghopcount.get_name_leafdata())
                if (self.stpxsmstinstancevlansmapped1k2k.is_set or self.stpxsmstinstancevlansmapped1k2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstancevlansmapped1k2k.get_name_leafdata())
                if (self.stpxsmstinstancevlansmapped3k4k.is_set or self.stpxsmstinstancevlansmapped3k4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstancevlansmapped3k4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxSMSTInstanceIndex" or name == "stpxSMSTInstanceCISTIntRootCost" or name == "stpxSMSTInstanceCISTRegionalRoot" or name == "stpxSMSTInstanceRemainingHopCount" or name == "stpxSMSTInstanceVlansMapped1k2k" or name == "stpxSMSTInstanceVlansMapped3k4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxSMSTInstanceIndex"):
                    self.stpxsmstinstanceindex = value
                    self.stpxsmstinstanceindex.value_namespace = name_space
                    self.stpxsmstinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceCISTIntRootCost"):
                    self.stpxsmstinstancecistintrootcost = value
                    self.stpxsmstinstancecistintrootcost.value_namespace = name_space
                    self.stpxsmstinstancecistintrootcost.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceCISTRegionalRoot"):
                    self.stpxsmstinstancecistregionalroot = value
                    self.stpxsmstinstancecistregionalroot.value_namespace = name_space
                    self.stpxsmstinstancecistregionalroot.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceRemainingHopCount"):
                    self.stpxsmstinstanceremaininghopcount = value
                    self.stpxsmstinstanceremaininghopcount.value_namespace = name_space
                    self.stpxsmstinstanceremaininghopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceVlansMapped1k2k"):
                    self.stpxsmstinstancevlansmapped1k2k = value
                    self.stpxsmstinstancevlansmapped1k2k.value_namespace = name_space
                    self.stpxsmstinstancevlansmapped1k2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceVlansMapped3k4k"):
                    self.stpxsmstinstancevlansmapped3k4k = value
                    self.stpxsmstinstancevlansmapped3k4k.value_namespace = name_space
                    self.stpxsmstinstancevlansmapped3k4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxsmstinstanceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxsmstinstanceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxSMSTInstanceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxSMSTInstanceEntry"):
                for c in self.stpxsmstinstanceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxsmstinstanceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxSMSTInstanceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxsmstinstanceedittable(Entity):
        """
        This table contains MST instance information in the 
        Edit Buffer. 
        
        This table is only instantiated when the object value
        of  stpxMSTRegionEditBufferStatus has the value of
        acquiredBySnmp(2).
        
        .. attribute:: stpxsmstinstanceeditentry
        
        	A conceptual row containing MST instance information  in the Edit Buffer.  The total number of entries in this table has to be  less than or equal to the object value of stpxSMSTMaxInstances
        	**type**\: list of    :py:class:`Stpxsmstinstanceeditentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable, self).__init__()

            self.yang_name = "stpxSMSTInstanceEditTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxsmstinstanceeditentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable, self).__setattr__(name, value)


        class Stpxsmstinstanceeditentry(Entity):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            The total number of entries in this table has to be 
            less than or equal to the object value of stpxSMSTMaxInstances.
            
            .. attribute:: stpxsmstinstanceeditindex  <key>
            
            	The MST instance ID, the value of which is in the range from 0 to stpxSMSTMaxInstanceID.   The instances of this table entry with  stpxSMSTInstanceEditIndex of zero is automatically created by the device and can not modified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstanceeditrowstatus
            
            	This object controls the creation and deletion of a row  in stpxSMSTInstanceEditTable.  When creating an entry in this table, 'createAndGo' method is used and the value of this object is set to 'active'. Deactivation of an 'active' entry is not allowed.  When  deleting an entry in this table, 'destroy' method is used.  Once a row becomes active, value in any other column  within such a row may be modified. When a row is active,  setting the instance of stpxSMSTInstanceEditVlansMap1k2k stpxSMSTInstanceEditVlansMap3k4k for the same MST instance both to the value of zero length can not be allowed
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: stpxsmstinstanceeditvlansmap1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  SMST instance 0 by the device. If the bit corresponding  to a VLAN is changed from '0' to '1', then that VLAN will  be automatically removed from the MST instance this VLAN was  previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: stpxsmstinstanceeditvlansmap3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1' to '0', then that VLAN will be automatically mapped to SMST instance 0 by the device. If the bit corresponding to a VLAN is changed from '0' to '1', then that VLAN will be automatically removed from the MST instance this VLAN was previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry, self).__init__()

                self.yang_name = "stpxSMSTInstanceEditEntry"
                self.yang_parent_name = "stpxSMSTInstanceEditTable"

                self.stpxsmstinstanceeditindex = YLeaf(YType.uint32, "stpxSMSTInstanceEditIndex")

                self.stpxsmstinstanceeditrowstatus = YLeaf(YType.enumeration, "stpxSMSTInstanceEditRowStatus")

                self.stpxsmstinstanceeditvlansmap1k2k = YLeaf(YType.str, "stpxSMSTInstanceEditVlansMap1k2k")

                self.stpxsmstinstanceeditvlansmap3k4k = YLeaf(YType.str, "stpxSMSTInstanceEditVlansMap3k4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxsmstinstanceeditindex",
                                "stpxsmstinstanceeditrowstatus",
                                "stpxsmstinstanceeditvlansmap1k2k",
                                "stpxsmstinstanceeditvlansmap3k4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.stpxsmstinstanceeditindex.is_set or
                    self.stpxsmstinstanceeditrowstatus.is_set or
                    self.stpxsmstinstanceeditvlansmap1k2k.is_set or
                    self.stpxsmstinstanceeditvlansmap3k4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceeditindex.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceeditrowstatus.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceeditvlansmap1k2k.yfilter != YFilter.not_set or
                    self.stpxsmstinstanceeditvlansmap3k4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxSMSTInstanceEditEntry" + "[stpxSMSTInstanceEditIndex='" + self.stpxsmstinstanceeditindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTInstanceEditTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxsmstinstanceeditindex.is_set or self.stpxsmstinstanceeditindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceeditindex.get_name_leafdata())
                if (self.stpxsmstinstanceeditrowstatus.is_set or self.stpxsmstinstanceeditrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceeditrowstatus.get_name_leafdata())
                if (self.stpxsmstinstanceeditvlansmap1k2k.is_set or self.stpxsmstinstanceeditvlansmap1k2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceeditvlansmap1k2k.get_name_leafdata())
                if (self.stpxsmstinstanceeditvlansmap3k4k.is_set or self.stpxsmstinstanceeditvlansmap3k4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstinstanceeditvlansmap3k4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxSMSTInstanceEditIndex" or name == "stpxSMSTInstanceEditRowStatus" or name == "stpxSMSTInstanceEditVlansMap1k2k" or name == "stpxSMSTInstanceEditVlansMap3k4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxSMSTInstanceEditIndex"):
                    self.stpxsmstinstanceeditindex = value
                    self.stpxsmstinstanceeditindex.value_namespace = name_space
                    self.stpxsmstinstanceeditindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceEditRowStatus"):
                    self.stpxsmstinstanceeditrowstatus = value
                    self.stpxsmstinstanceeditrowstatus.value_namespace = name_space
                    self.stpxsmstinstanceeditrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceEditVlansMap1k2k"):
                    self.stpxsmstinstanceeditvlansmap1k2k = value
                    self.stpxsmstinstanceeditvlansmap1k2k.value_namespace = name_space
                    self.stpxsmstinstanceeditvlansmap1k2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTInstanceEditVlansMap3k4k"):
                    self.stpxsmstinstanceeditvlansmap3k4k = value
                    self.stpxsmstinstanceeditvlansmap3k4k.value_namespace = name_space
                    self.stpxsmstinstanceeditvlansmap3k4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stpxsmstinstanceeditentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxsmstinstanceeditentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxSMSTInstanceEditTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxSMSTInstanceEditEntry"):
                for c in self.stpxsmstinstanceeditentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxsmstinstanceeditentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxSMSTInstanceEditEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Stpxsmstporttable(Entity):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        This table is only instantiated when the object 
        value of stpxSpanningTreeType is mst(4)
        
        .. attribute:: stpxsmstportentry
        
        	An entry with port information for the MST protocol on a bridge port
        	**type**\: list of    :py:class:`Stpxsmstportentry <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry>`
        
        

        """

        _prefix = 'CISCO-STP-EXTENSIONS-MIB'
        _revision = '2013-03-07'

        def __init__(self):
            super(CiscoStpExtensionsMib.Stpxsmstporttable, self).__init__()

            self.yang_name = "stpxSMSTPortTable"
            self.yang_parent_name = "CISCO-STP-EXTENSIONS-MIB"

            self.stpxsmstportentry = YList(self)

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
                        super(CiscoStpExtensionsMib.Stpxsmstporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoStpExtensionsMib.Stpxsmstporttable, self).__setattr__(name, value)


        class Stpxsmstportentry(Entity):
            """
            An entry with port information for the MST protocol
            on a bridge port.
            
            .. attribute:: stpxsmstportindex  <key>
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: stpxsmstportadminhellotime
            
            	The adminitratively configured hello time in hundredth  of seconds on a port for IEEE MST. The granularity  of this timer is 1 second. An agent may return a badValue  error if a set is attempted to a value which is not a  whole number of seconds. This object value of zero means the hello time is not specifically configured on  this port and object value of stpxSMSTPortConfigedHelloTime retrieved for this port will take on the value of  dot1dStpBridgeHelloTime defined in BRIDGE\-MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportadminmstmode
            
            	The desired MST mode of this port.  preStandard \-\- this port is administratively configured to     transmit pre\-standard, i.e. pre IEEE MST, BPDUs.  auto \-\- the BPDU transmission mode of this port is based      on automatic detection of neighbor ports
            	**type**\:   :py:class:`Stpxsmstportadminmstmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportadminmstmode>`
            
            .. attribute:: stpxsmstportconfigedhellotime
            
            	Indicates the effective configuration of the hello time on  a port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportoperhellotime
            
            	The operational hello time in hundredth of seconds on a  port for IEEE MST. If this object value is not applicable on a port, then the value retrieved on that port will be \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            	**units**\: hundredth of seconds
            
            .. attribute:: stpxsmstportopermstmode
            
            	Indicates the current operational MST mode of this port.  unknown \-\- the operational mode is currently unknown.  preStandard \-\- this port is currently operating in      pre\-standard MSTP BPDU transmission mode.  standard \-\- this port is currently operating in IEEE MST      BPDU transmission mode
            	**type**\:   :py:class:`Stpxsmstportopermstmode <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportopermstmode>`
            
            .. attribute:: stpxsmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.  dispute \-\- this port, as a designated port, received an         inferior BPDU with a designated role and the         learning bit being set.  rstp \-\- this port is connected to a RSTP bridge or an          MST bridge in a different MST region
            	**type**\:   :py:class:`Stpxsmstportstatus <ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB.CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportstatus>`
            
            

            """

            _prefix = 'CISCO-STP-EXTENSIONS-MIB'
            _revision = '2013-03-07'

            def __init__(self):
                super(CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry, self).__init__()

                self.yang_name = "stpxSMSTPortEntry"
                self.yang_parent_name = "stpxSMSTPortTable"

                self.stpxsmstportindex = YLeaf(YType.int32, "stpxSMSTPortIndex")

                self.stpxsmstportadminhellotime = YLeaf(YType.uint32, "stpxSMSTPortAdminHelloTime")

                self.stpxsmstportadminmstmode = YLeaf(YType.enumeration, "stpxSMSTPortAdminMSTMode")

                self.stpxsmstportconfigedhellotime = YLeaf(YType.uint32, "stpxSMSTPortConfigedHelloTime")

                self.stpxsmstportoperhellotime = YLeaf(YType.int32, "stpxSMSTPortOperHelloTime")

                self.stpxsmstportopermstmode = YLeaf(YType.enumeration, "stpxSMSTPortOperMSTMode")

                self.stpxsmstportstatus = YLeaf(YType.bits, "stpxSMSTPortStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("stpxsmstportindex",
                                "stpxsmstportadminhellotime",
                                "stpxsmstportadminmstmode",
                                "stpxsmstportconfigedhellotime",
                                "stpxsmstportoperhellotime",
                                "stpxsmstportopermstmode",
                                "stpxsmstportstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry, self).__setattr__(name, value)

            class Stpxsmstportadminmstmode(Enum):
                """
                Stpxsmstportadminmstmode

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
                Stpxsmstportopermstmode

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


            def has_data(self):
                return (
                    self.stpxsmstportindex.is_set or
                    self.stpxsmstportadminhellotime.is_set or
                    self.stpxsmstportadminmstmode.is_set or
                    self.stpxsmstportconfigedhellotime.is_set or
                    self.stpxsmstportoperhellotime.is_set or
                    self.stpxsmstportopermstmode.is_set or
                    self.stpxsmstportstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.stpxsmstportindex.yfilter != YFilter.not_set or
                    self.stpxsmstportadminhellotime.yfilter != YFilter.not_set or
                    self.stpxsmstportadminmstmode.yfilter != YFilter.not_set or
                    self.stpxsmstportconfigedhellotime.yfilter != YFilter.not_set or
                    self.stpxsmstportoperhellotime.yfilter != YFilter.not_set or
                    self.stpxsmstportopermstmode.yfilter != YFilter.not_set or
                    self.stpxsmstportstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stpxSMSTPortEntry" + "[stpxSMSTPortIndex='" + self.stpxsmstportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/stpxSMSTPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.stpxsmstportindex.is_set or self.stpxsmstportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportindex.get_name_leafdata())
                if (self.stpxsmstportadminhellotime.is_set or self.stpxsmstportadminhellotime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportadminhellotime.get_name_leafdata())
                if (self.stpxsmstportadminmstmode.is_set or self.stpxsmstportadminmstmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportadminmstmode.get_name_leafdata())
                if (self.stpxsmstportconfigedhellotime.is_set or self.stpxsmstportconfigedhellotime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportconfigedhellotime.get_name_leafdata())
                if (self.stpxsmstportoperhellotime.is_set or self.stpxsmstportoperhellotime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportoperhellotime.get_name_leafdata())
                if (self.stpxsmstportopermstmode.is_set or self.stpxsmstportopermstmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportopermstmode.get_name_leafdata())
                if (self.stpxsmstportstatus.is_set or self.stpxsmstportstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxsmstportstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "stpxSMSTPortIndex" or name == "stpxSMSTPortAdminHelloTime" or name == "stpxSMSTPortAdminMSTMode" or name == "stpxSMSTPortConfigedHelloTime" or name == "stpxSMSTPortOperHelloTime" or name == "stpxSMSTPortOperMSTMode" or name == "stpxSMSTPortStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "stpxSMSTPortIndex"):
                    self.stpxsmstportindex = value
                    self.stpxsmstportindex.value_namespace = name_space
                    self.stpxsmstportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortAdminHelloTime"):
                    self.stpxsmstportadminhellotime = value
                    self.stpxsmstportadminhellotime.value_namespace = name_space
                    self.stpxsmstportadminhellotime.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortAdminMSTMode"):
                    self.stpxsmstportadminmstmode = value
                    self.stpxsmstportadminmstmode.value_namespace = name_space
                    self.stpxsmstportadminmstmode.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortConfigedHelloTime"):
                    self.stpxsmstportconfigedhellotime = value
                    self.stpxsmstportconfigedhellotime.value_namespace = name_space
                    self.stpxsmstportconfigedhellotime.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortOperHelloTime"):
                    self.stpxsmstportoperhellotime = value
                    self.stpxsmstportoperhellotime.value_namespace = name_space
                    self.stpxsmstportoperhellotime.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortOperMSTMode"):
                    self.stpxsmstportopermstmode = value
                    self.stpxsmstportopermstmode.value_namespace = name_space
                    self.stpxsmstportopermstmode.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxSMSTPortStatus"):
                    self.stpxsmstportstatus[value] = True

        def has_data(self):
            for c in self.stpxsmstportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stpxsmstportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stpxSMSTPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stpxSMSTPortEntry"):
                for c in self.stpxsmstportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stpxsmstportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stpxSMSTPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.stpxbackbonefastobjects is not None and self.stpxbackbonefastobjects.has_data()) or
            (self.stpxbpduskewingobjects is not None and self.stpxbpduskewingobjects.has_data()) or
            (self.stpxbpduskewingtable is not None and self.stpxbpduskewingtable.has_data()) or
            (self.stpxfaststartobjects is not None and self.stpxfaststartobjects.has_data()) or
            (self.stpxfaststartopermodetable is not None and self.stpxfaststartopermodetable.has_data()) or
            (self.stpxfaststartporttable is not None and self.stpxfaststartporttable.has_data()) or
            (self.stpxinconsistencytable is not None and self.stpxinconsistencytable.has_data()) or
            (self.stpxloopguardconfigtable is not None and self.stpxloopguardconfigtable.has_data()) or
            (self.stpxloopguardobjects is not None and self.stpxloopguardobjects.has_data()) or
            (self.stpxloopinconsistencytable is not None and self.stpxloopinconsistencytable.has_data()) or
            (self.stpxmistpinstancetable is not None and self.stpxmistpinstancetable.has_data()) or
            (self.stpxmistpobjects is not None and self.stpxmistpobjects.has_data()) or
            (self.stpxmstinstanceedittable is not None and self.stpxmstinstanceedittable.has_data()) or
            (self.stpxmstinstancetable is not None and self.stpxmstinstancetable.has_data()) or
            (self.stpxmstobjects is not None and self.stpxmstobjects.has_data()) or
            (self.stpxmstportroletable is not None and self.stpxmstportroletable.has_data()) or
            (self.stpxmstporttable is not None and self.stpxmstporttable.has_data()) or
            (self.stpxpvstvlantable is not None and self.stpxpvstvlantable.has_data()) or
            (self.stpxrootguardconfigtable is not None and self.stpxrootguardconfigtable.has_data()) or
            (self.stpxrootinconsistencytable is not None and self.stpxrootinconsistencytable.has_data()) or
            (self.stpxrpvstporttable is not None and self.stpxrpvstporttable.has_data()) or
            (self.stpxrstpobjects is not None and self.stpxrstpobjects.has_data()) or
            (self.stpxrstpportroletable is not None and self.stpxrstpportroletable.has_data()) or
            (self.stpxrstpporttable is not None and self.stpxrstpporttable.has_data()) or
            (self.stpxsmstinstanceedittable is not None and self.stpxsmstinstanceedittable.has_data()) or
            (self.stpxsmstinstancetable is not None and self.stpxsmstinstancetable.has_data()) or
            (self.stpxsmstobjects is not None and self.stpxsmstobjects.has_data()) or
            (self.stpxsmstporttable is not None and self.stpxsmstporttable.has_data()) or
            (self.stpxspanningtreeobjects is not None and self.stpxspanningtreeobjects.has_data()) or
            (self.stpxuplinkfastobjects is not None and self.stpxuplinkfastobjects.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.stpxbackbonefastobjects is not None and self.stpxbackbonefastobjects.has_operation()) or
            (self.stpxbpduskewingobjects is not None and self.stpxbpduskewingobjects.has_operation()) or
            (self.stpxbpduskewingtable is not None and self.stpxbpduskewingtable.has_operation()) or
            (self.stpxfaststartobjects is not None and self.stpxfaststartobjects.has_operation()) or
            (self.stpxfaststartopermodetable is not None and self.stpxfaststartopermodetable.has_operation()) or
            (self.stpxfaststartporttable is not None and self.stpxfaststartporttable.has_operation()) or
            (self.stpxinconsistencytable is not None and self.stpxinconsistencytable.has_operation()) or
            (self.stpxloopguardconfigtable is not None and self.stpxloopguardconfigtable.has_operation()) or
            (self.stpxloopguardobjects is not None and self.stpxloopguardobjects.has_operation()) or
            (self.stpxloopinconsistencytable is not None and self.stpxloopinconsistencytable.has_operation()) or
            (self.stpxmistpinstancetable is not None and self.stpxmistpinstancetable.has_operation()) or
            (self.stpxmistpobjects is not None and self.stpxmistpobjects.has_operation()) or
            (self.stpxmstinstanceedittable is not None and self.stpxmstinstanceedittable.has_operation()) or
            (self.stpxmstinstancetable is not None and self.stpxmstinstancetable.has_operation()) or
            (self.stpxmstobjects is not None and self.stpxmstobjects.has_operation()) or
            (self.stpxmstportroletable is not None and self.stpxmstportroletable.has_operation()) or
            (self.stpxmstporttable is not None and self.stpxmstporttable.has_operation()) or
            (self.stpxpvstvlantable is not None and self.stpxpvstvlantable.has_operation()) or
            (self.stpxrootguardconfigtable is not None and self.stpxrootguardconfigtable.has_operation()) or
            (self.stpxrootinconsistencytable is not None and self.stpxrootinconsistencytable.has_operation()) or
            (self.stpxrpvstporttable is not None and self.stpxrpvstporttable.has_operation()) or
            (self.stpxrstpobjects is not None and self.stpxrstpobjects.has_operation()) or
            (self.stpxrstpportroletable is not None and self.stpxrstpportroletable.has_operation()) or
            (self.stpxrstpporttable is not None and self.stpxrstpporttable.has_operation()) or
            (self.stpxsmstinstanceedittable is not None and self.stpxsmstinstanceedittable.has_operation()) or
            (self.stpxsmstinstancetable is not None and self.stpxsmstinstancetable.has_operation()) or
            (self.stpxsmstobjects is not None and self.stpxsmstobjects.has_operation()) or
            (self.stpxsmstporttable is not None and self.stpxsmstporttable.has_operation()) or
            (self.stpxspanningtreeobjects is not None and self.stpxspanningtreeobjects.has_operation()) or
            (self.stpxuplinkfastobjects is not None and self.stpxuplinkfastobjects.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB" + path_buffer

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

        if (child_yang_name == "stpxBackboneFastObjects"):
            if (self.stpxbackbonefastobjects is None):
                self.stpxbackbonefastobjects = CiscoStpExtensionsMib.Stpxbackbonefastobjects()
                self.stpxbackbonefastobjects.parent = self
                self._children_name_map["stpxbackbonefastobjects"] = "stpxBackboneFastObjects"
            return self.stpxbackbonefastobjects

        if (child_yang_name == "stpxBpduSkewingObjects"):
            if (self.stpxbpduskewingobjects is None):
                self.stpxbpduskewingobjects = CiscoStpExtensionsMib.Stpxbpduskewingobjects()
                self.stpxbpduskewingobjects.parent = self
                self._children_name_map["stpxbpduskewingobjects"] = "stpxBpduSkewingObjects"
            return self.stpxbpduskewingobjects

        if (child_yang_name == "stpxBpduSkewingTable"):
            if (self.stpxbpduskewingtable is None):
                self.stpxbpduskewingtable = CiscoStpExtensionsMib.Stpxbpduskewingtable()
                self.stpxbpduskewingtable.parent = self
                self._children_name_map["stpxbpduskewingtable"] = "stpxBpduSkewingTable"
            return self.stpxbpduskewingtable

        if (child_yang_name == "stpxFastStartObjects"):
            if (self.stpxfaststartobjects is None):
                self.stpxfaststartobjects = CiscoStpExtensionsMib.Stpxfaststartobjects()
                self.stpxfaststartobjects.parent = self
                self._children_name_map["stpxfaststartobjects"] = "stpxFastStartObjects"
            return self.stpxfaststartobjects

        if (child_yang_name == "stpxFastStartOperModeTable"):
            if (self.stpxfaststartopermodetable is None):
                self.stpxfaststartopermodetable = CiscoStpExtensionsMib.Stpxfaststartopermodetable()
                self.stpxfaststartopermodetable.parent = self
                self._children_name_map["stpxfaststartopermodetable"] = "stpxFastStartOperModeTable"
            return self.stpxfaststartopermodetable

        if (child_yang_name == "stpxFastStartPortTable"):
            if (self.stpxfaststartporttable is None):
                self.stpxfaststartporttable = CiscoStpExtensionsMib.Stpxfaststartporttable()
                self.stpxfaststartporttable.parent = self
                self._children_name_map["stpxfaststartporttable"] = "stpxFastStartPortTable"
            return self.stpxfaststartporttable

        if (child_yang_name == "stpxInconsistencyTable"):
            if (self.stpxinconsistencytable is None):
                self.stpxinconsistencytable = CiscoStpExtensionsMib.Stpxinconsistencytable()
                self.stpxinconsistencytable.parent = self
                self._children_name_map["stpxinconsistencytable"] = "stpxInconsistencyTable"
            return self.stpxinconsistencytable

        if (child_yang_name == "stpxLoopGuardConfigTable"):
            if (self.stpxloopguardconfigtable is None):
                self.stpxloopguardconfigtable = CiscoStpExtensionsMib.Stpxloopguardconfigtable()
                self.stpxloopguardconfigtable.parent = self
                self._children_name_map["stpxloopguardconfigtable"] = "stpxLoopGuardConfigTable"
            return self.stpxloopguardconfigtable

        if (child_yang_name == "stpxLoopGuardObjects"):
            if (self.stpxloopguardobjects is None):
                self.stpxloopguardobjects = CiscoStpExtensionsMib.Stpxloopguardobjects()
                self.stpxloopguardobjects.parent = self
                self._children_name_map["stpxloopguardobjects"] = "stpxLoopGuardObjects"
            return self.stpxloopguardobjects

        if (child_yang_name == "stpxLoopInconsistencyTable"):
            if (self.stpxloopinconsistencytable is None):
                self.stpxloopinconsistencytable = CiscoStpExtensionsMib.Stpxloopinconsistencytable()
                self.stpxloopinconsistencytable.parent = self
                self._children_name_map["stpxloopinconsistencytable"] = "stpxLoopInconsistencyTable"
            return self.stpxloopinconsistencytable

        if (child_yang_name == "stpxMISTPInstanceTable"):
            if (self.stpxmistpinstancetable is None):
                self.stpxmistpinstancetable = CiscoStpExtensionsMib.Stpxmistpinstancetable()
                self.stpxmistpinstancetable.parent = self
                self._children_name_map["stpxmistpinstancetable"] = "stpxMISTPInstanceTable"
            return self.stpxmistpinstancetable

        if (child_yang_name == "stpxMISTPObjects"):
            if (self.stpxmistpobjects is None):
                self.stpxmistpobjects = CiscoStpExtensionsMib.Stpxmistpobjects()
                self.stpxmistpobjects.parent = self
                self._children_name_map["stpxmistpobjects"] = "stpxMISTPObjects"
            return self.stpxmistpobjects

        if (child_yang_name == "stpxMSTInstanceEditTable"):
            if (self.stpxmstinstanceedittable is None):
                self.stpxmstinstanceedittable = CiscoStpExtensionsMib.Stpxmstinstanceedittable()
                self.stpxmstinstanceedittable.parent = self
                self._children_name_map["stpxmstinstanceedittable"] = "stpxMSTInstanceEditTable"
            return self.stpxmstinstanceedittable

        if (child_yang_name == "stpxMSTInstanceTable"):
            if (self.stpxmstinstancetable is None):
                self.stpxmstinstancetable = CiscoStpExtensionsMib.Stpxmstinstancetable()
                self.stpxmstinstancetable.parent = self
                self._children_name_map["stpxmstinstancetable"] = "stpxMSTInstanceTable"
            return self.stpxmstinstancetable

        if (child_yang_name == "stpxMSTObjects"):
            if (self.stpxmstobjects is None):
                self.stpxmstobjects = CiscoStpExtensionsMib.Stpxmstobjects()
                self.stpxmstobjects.parent = self
                self._children_name_map["stpxmstobjects"] = "stpxMSTObjects"
            return self.stpxmstobjects

        if (child_yang_name == "stpxMSTPortRoleTable"):
            if (self.stpxmstportroletable is None):
                self.stpxmstportroletable = CiscoStpExtensionsMib.Stpxmstportroletable()
                self.stpxmstportroletable.parent = self
                self._children_name_map["stpxmstportroletable"] = "stpxMSTPortRoleTable"
            return self.stpxmstportroletable

        if (child_yang_name == "stpxMSTPortTable"):
            if (self.stpxmstporttable is None):
                self.stpxmstporttable = CiscoStpExtensionsMib.Stpxmstporttable()
                self.stpxmstporttable.parent = self
                self._children_name_map["stpxmstporttable"] = "stpxMSTPortTable"
            return self.stpxmstporttable

        if (child_yang_name == "stpxPVSTVlanTable"):
            if (self.stpxpvstvlantable is None):
                self.stpxpvstvlantable = CiscoStpExtensionsMib.Stpxpvstvlantable()
                self.stpxpvstvlantable.parent = self
                self._children_name_map["stpxpvstvlantable"] = "stpxPVSTVlanTable"
            return self.stpxpvstvlantable

        if (child_yang_name == "stpxRootGuardConfigTable"):
            if (self.stpxrootguardconfigtable is None):
                self.stpxrootguardconfigtable = CiscoStpExtensionsMib.Stpxrootguardconfigtable()
                self.stpxrootguardconfigtable.parent = self
                self._children_name_map["stpxrootguardconfigtable"] = "stpxRootGuardConfigTable"
            return self.stpxrootguardconfigtable

        if (child_yang_name == "stpxRootInconsistencyTable"):
            if (self.stpxrootinconsistencytable is None):
                self.stpxrootinconsistencytable = CiscoStpExtensionsMib.Stpxrootinconsistencytable()
                self.stpxrootinconsistencytable.parent = self
                self._children_name_map["stpxrootinconsistencytable"] = "stpxRootInconsistencyTable"
            return self.stpxrootinconsistencytable

        if (child_yang_name == "stpxRPVSTPortTable"):
            if (self.stpxrpvstporttable is None):
                self.stpxrpvstporttable = CiscoStpExtensionsMib.Stpxrpvstporttable()
                self.stpxrpvstporttable.parent = self
                self._children_name_map["stpxrpvstporttable"] = "stpxRPVSTPortTable"
            return self.stpxrpvstporttable

        if (child_yang_name == "stpxRSTPObjects"):
            if (self.stpxrstpobjects is None):
                self.stpxrstpobjects = CiscoStpExtensionsMib.Stpxrstpobjects()
                self.stpxrstpobjects.parent = self
                self._children_name_map["stpxrstpobjects"] = "stpxRSTPObjects"
            return self.stpxrstpobjects

        if (child_yang_name == "stpxRSTPPortRoleTable"):
            if (self.stpxrstpportroletable is None):
                self.stpxrstpportroletable = CiscoStpExtensionsMib.Stpxrstpportroletable()
                self.stpxrstpportroletable.parent = self
                self._children_name_map["stpxrstpportroletable"] = "stpxRSTPPortRoleTable"
            return self.stpxrstpportroletable

        if (child_yang_name == "stpxRSTPPortTable"):
            if (self.stpxrstpporttable is None):
                self.stpxrstpporttable = CiscoStpExtensionsMib.Stpxrstpporttable()
                self.stpxrstpporttable.parent = self
                self._children_name_map["stpxrstpporttable"] = "stpxRSTPPortTable"
            return self.stpxrstpporttable

        if (child_yang_name == "stpxSMSTInstanceEditTable"):
            if (self.stpxsmstinstanceedittable is None):
                self.stpxsmstinstanceedittable = CiscoStpExtensionsMib.Stpxsmstinstanceedittable()
                self.stpxsmstinstanceedittable.parent = self
                self._children_name_map["stpxsmstinstanceedittable"] = "stpxSMSTInstanceEditTable"
            return self.stpxsmstinstanceedittable

        if (child_yang_name == "stpxSMSTInstanceTable"):
            if (self.stpxsmstinstancetable is None):
                self.stpxsmstinstancetable = CiscoStpExtensionsMib.Stpxsmstinstancetable()
                self.stpxsmstinstancetable.parent = self
                self._children_name_map["stpxsmstinstancetable"] = "stpxSMSTInstanceTable"
            return self.stpxsmstinstancetable

        if (child_yang_name == "stpxSMSTObjects"):
            if (self.stpxsmstobjects is None):
                self.stpxsmstobjects = CiscoStpExtensionsMib.Stpxsmstobjects()
                self.stpxsmstobjects.parent = self
                self._children_name_map["stpxsmstobjects"] = "stpxSMSTObjects"
            return self.stpxsmstobjects

        if (child_yang_name == "stpxSMSTPortTable"):
            if (self.stpxsmstporttable is None):
                self.stpxsmstporttable = CiscoStpExtensionsMib.Stpxsmstporttable()
                self.stpxsmstporttable.parent = self
                self._children_name_map["stpxsmstporttable"] = "stpxSMSTPortTable"
            return self.stpxsmstporttable

        if (child_yang_name == "stpxSpanningTreeObjects"):
            if (self.stpxspanningtreeobjects is None):
                self.stpxspanningtreeobjects = CiscoStpExtensionsMib.Stpxspanningtreeobjects()
                self.stpxspanningtreeobjects.parent = self
                self._children_name_map["stpxspanningtreeobjects"] = "stpxSpanningTreeObjects"
            return self.stpxspanningtreeobjects

        if (child_yang_name == "stpxUplinkFastObjects"):
            if (self.stpxuplinkfastobjects is None):
                self.stpxuplinkfastobjects = CiscoStpExtensionsMib.Stpxuplinkfastobjects()
                self.stpxuplinkfastobjects.parent = self
                self._children_name_map["stpxuplinkfastobjects"] = "stpxUplinkFastObjects"
            return self.stpxuplinkfastobjects

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "stpxBackboneFastObjects" or name == "stpxBpduSkewingObjects" or name == "stpxBpduSkewingTable" or name == "stpxFastStartObjects" or name == "stpxFastStartOperModeTable" or name == "stpxFastStartPortTable" or name == "stpxInconsistencyTable" or name == "stpxLoopGuardConfigTable" or name == "stpxLoopGuardObjects" or name == "stpxLoopInconsistencyTable" or name == "stpxMISTPInstanceTable" or name == "stpxMISTPObjects" or name == "stpxMSTInstanceEditTable" or name == "stpxMSTInstanceTable" or name == "stpxMSTObjects" or name == "stpxMSTPortRoleTable" or name == "stpxMSTPortTable" or name == "stpxPVSTVlanTable" or name == "stpxRootGuardConfigTable" or name == "stpxRootInconsistencyTable" or name == "stpxRPVSTPortTable" or name == "stpxRSTPObjects" or name == "stpxRSTPPortRoleTable" or name == "stpxRSTPPortTable" or name == "stpxSMSTInstanceEditTable" or name == "stpxSMSTInstanceTable" or name == "stpxSMSTObjects" or name == "stpxSMSTPortTable" or name == "stpxSpanningTreeObjects" or name == "stpxUplinkFastObjects"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoStpExtensionsMib()
        return self._top_entity

