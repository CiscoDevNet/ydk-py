""" CISCO_STP_EXTENSIONS_MIB 

The MIB module for managing Cisco extensions to
the 802.1D Spanning Tree Protocol (STP).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOSTPEXTENSIONSMIB(object):
    """
    
    
    .. attribute:: stpxbackbonefastobjects
    
    	
    	**type**\: :py:class:`StpxBackboneFastObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects>`
    
    .. attribute:: stpxbpduskewingobjects
    
    	
    	**type**\: :py:class:`StpxBpduSkewingObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects>`
    
    .. attribute:: stpxbpduskewingtable
    
    	A table containing a list of the bridge ports for  which a particular Spanning Tree instance has been  detected to have BPDU skewing occurred since the  object value of stpxBpduSkewingDetectionEnable was last changed to true(1).  The agent creates a new entry in this table whenever a port in a particular Spanning Tree instance is  detected to be BPDU skewed since the object value of  stpxBpduSkewingDetectionEnable object is changed to  true(1). The agent deletes all the entries in this  table when the object value of  stpxBpduSkewingDetectionEnable is changed to false(2) or the object value of stpxSpanningTreeType is  changed
    	**type**\: :py:class:`StpxBpduSkewingTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable>`
    
    .. attribute:: stpxfaststartobjects
    
    	
    	**type**\: :py:class:`StpxFastStartObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartObjects>`
    
    .. attribute:: stpxfaststartopermodetable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance
    	**type**\: :py:class:`StpxFastStartOperModeTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable>`
    
    .. attribute:: stpxfaststartporttable
    
    	A table containing a list of the bridge ports for which Spanning Tree Port Fast Start can be configured
    	**type**\: :py:class:`StpxFastStartPortTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable>`
    
    .. attribute:: stpxinconsistencytable
    
    	A table containing a list of the ports for which a particular VLAN's Spanning Tree has been found to have an inconsistency.  Two types of inconsistency are discovered\: 1) an inconsistency where two different port types have been plugged together; and 2) an inconsistency where different switches have different PVIDs for the same link
    	**type**\: :py:class:`StpxInconsistencyTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable>`
    
    .. attribute:: stpxloopguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree LoopGuard capability can be configured
    	**type**\: :py:class:`StpxLoopGuardConfigTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable>`
    
    .. attribute:: stpxloopguardobjects
    
    	
    	**type**\: :py:class:`StpxLoopGuardObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects>`
    
    .. attribute:: stpxloopinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found to have a loop\-inconsistency. The agent creates a new entry in this table whenever it detects a new loop\-inconsistency, and deletes entries when/soon after the inconsistency is no longer present
    	**type**\: :py:class:`StpxLoopInconsistencyTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable>`
    
    .. attribute:: stpxmistpinstancetable
    
    	This table contains one entry for each instance of MISTP and  it contains stpxMISTPInstanceNumber entries, numbered from 1 to stpxMISTPInstanceNumber.  This table is only instantiated when the value of  stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3)
    	**type**\: :py:class:`StpxMISTPInstanceTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable>`
    
    .. attribute:: stpxmistpobjects
    
    	
    	**type**\: :py:class:`StpxMISTPObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMISTPObjects>`
    
    .. attribute:: stpxmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer with one entry for each MST instance numbered from 0 to stpxMSTMaxInstanceNumber.   This table is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2).  This table is deprecated and replaced by  stpxSMSTInstanceEditTable
    	**type**\: :py:class:`StpxMSTInstanceEditTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable>`
    
    .. attribute:: stpxmstinstancetable
    
    	This table contains MST instance information with one entry for an MST instance within the range of  0 to the object value of stpxMSTMaxInstanceNumber.   This table is deprecated and replaced by  stpxSMSTInstanceTable
    	**type**\: :py:class:`StpxMSTInstanceTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable>`
    
    .. attribute:: stpxmstobjects
    
    	
    	**type**\: :py:class:`StpxMSTObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTObjects>`
    
    .. attribute:: stpxmstportroletable
    
    	A table containing a list of the bridge ports for a  particular MST instance.  This table is only instantiated  when the stpxSpanningTreeType is mst(4).   This table is deprecated and replaced with  stpxRSTPPortRoleTable
    	**type**\: :py:class:`StpxMSTPortRoleTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable>`
    
    .. attribute:: stpxmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system
    	**type**\: :py:class:`StpxMSTPortTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortTable>`
    
    .. attribute:: stpxpvstvlantable
    
    	A list of Virtual LAN entries containing information for Spanning Tree PVST+ protocol.  An entry will exist for each VLAN existing on  the device
    	**type**\: :py:class:`StpxPVSTVlanTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable>`
    
    .. attribute:: stpxrootguardconfigtable
    
    	A table containing a list of the bridge ports for which Spanning Tree RootGuard capability can be configured
    	**type**\: :py:class:`StpxRootGuardConfigTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable>`
    
    .. attribute:: stpxrootinconsistencytable
    
    	A table containing a list of the bridge ports for which a particular Spanning Tree instance has been found  to have an root\-inconsistency. The agent creates a new  entry in this table whenever it detects a new  root\-inconsistency, and deletes entries  when/soon after the inconsistency is no longer present
    	**type**\: :py:class:`StpxRootInconsistencyTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable>`
    
    .. attribute:: stpxrpvstporttable
    
    	A table containing a list of the bridge ports  for a particular Spanning Tree Instance. This table is only instantiated when the object value of stpxSpanningTreeType is rapidPvstPlus(5)
    	**type**\: :py:class:`StpxRPVSTPortTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable>`
    
    .. attribute:: stpxrstpobjects
    
    	
    	**type**\: :py:class:`StpxRSTPObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPObjects>`
    
    .. attribute:: stpxrstpportroletable
    
    	A table containing a list of the bridge ports for a  particular Spanning Tree instance.  This table is  only instantiated when the stpxSpanningTreeType is mst(4)  or rapidPvstPlus(5)
    	**type**\: :py:class:`StpxRSTPPortRoleTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable>`
    
    .. attribute:: stpxrstpporttable
    
    	A table containing port information for the RSTP  Protocol on all the bridge ports existing in the  system
    	**type**\: :py:class:`StpxRSTPPortTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable>`
    
    .. attribute:: stpxsmstinstanceedittable
    
    	This table contains MST instance information in the  Edit Buffer.   This table is only instantiated when the object value of  stpxMSTRegionEditBufferStatus has the value of acquiredBySnmp(2)
    	**type**\: :py:class:`StpxSMSTInstanceEditTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable>`
    
    .. attribute:: stpxsmstinstancetable
    
    	This table contains MST instance information for IEEE MST
    	**type**\: :py:class:`StpxSMSTInstanceTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable>`
    
    .. attribute:: stpxsmstobjects
    
    	
    	**type**\: :py:class:`StpxSMSTObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTObjects>`
    
    .. attribute:: stpxsmstporttable
    
    	A table containing port information for the MST  Protocol on all the bridge ports existing on the  system.  This table is only instantiated when the object  value of stpxSpanningTreeType is mst(4)
    	**type**\: :py:class:`StpxSMSTPortTable <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable>`
    
    .. attribute:: stpxspanningtreeobjects
    
    	
    	**type**\: :py:class:`StpxSpanningTreeObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects>`
    
    .. attribute:: stpxuplinkfastobjects
    
    	
    	**type**\: :py:class:`StpxUplinkFastObjects <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects>`
    
    

    """

    _prefix = 'cisco-stp'
    _revision = '2013-03-07'

    def __init__(self):
        self.stpxbackbonefastobjects = CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects()
        self.stpxbackbonefastobjects.parent = self
        self.stpxbpduskewingobjects = CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects()
        self.stpxbpduskewingobjects.parent = self
        self.stpxbpduskewingtable = CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable()
        self.stpxbpduskewingtable.parent = self
        self.stpxfaststartobjects = CISCOSTPEXTENSIONSMIB.StpxFastStartObjects()
        self.stpxfaststartobjects.parent = self
        self.stpxfaststartopermodetable = CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable()
        self.stpxfaststartopermodetable.parent = self
        self.stpxfaststartporttable = CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable()
        self.stpxfaststartporttable.parent = self
        self.stpxinconsistencytable = CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable()
        self.stpxinconsistencytable.parent = self
        self.stpxloopguardconfigtable = CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable()
        self.stpxloopguardconfigtable.parent = self
        self.stpxloopguardobjects = CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects()
        self.stpxloopguardobjects.parent = self
        self.stpxloopinconsistencytable = CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable()
        self.stpxloopinconsistencytable.parent = self
        self.stpxmistpinstancetable = CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable()
        self.stpxmistpinstancetable.parent = self
        self.stpxmistpobjects = CISCOSTPEXTENSIONSMIB.StpxMISTPObjects()
        self.stpxmistpobjects.parent = self
        self.stpxmstinstanceedittable = CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable()
        self.stpxmstinstanceedittable.parent = self
        self.stpxmstinstancetable = CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable()
        self.stpxmstinstancetable.parent = self
        self.stpxmstobjects = CISCOSTPEXTENSIONSMIB.StpxMSTObjects()
        self.stpxmstobjects.parent = self
        self.stpxmstportroletable = CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable()
        self.stpxmstportroletable.parent = self
        self.stpxmstporttable = CISCOSTPEXTENSIONSMIB.StpxMSTPortTable()
        self.stpxmstporttable.parent = self
        self.stpxpvstvlantable = CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable()
        self.stpxpvstvlantable.parent = self
        self.stpxrootguardconfigtable = CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable()
        self.stpxrootguardconfigtable.parent = self
        self.stpxrootinconsistencytable = CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable()
        self.stpxrootinconsistencytable.parent = self
        self.stpxrpvstporttable = CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable()
        self.stpxrpvstporttable.parent = self
        self.stpxrstpobjects = CISCOSTPEXTENSIONSMIB.StpxRSTPObjects()
        self.stpxrstpobjects.parent = self
        self.stpxrstpportroletable = CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable()
        self.stpxrstpportroletable.parent = self
        self.stpxrstpporttable = CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable()
        self.stpxrstpporttable.parent = self
        self.stpxsmstinstanceedittable = CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable()
        self.stpxsmstinstanceedittable.parent = self
        self.stpxsmstinstancetable = CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable()
        self.stpxsmstinstancetable.parent = self
        self.stpxsmstobjects = CISCOSTPEXTENSIONSMIB.StpxSMSTObjects()
        self.stpxsmstobjects.parent = self
        self.stpxsmstporttable = CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable()
        self.stpxsmstporttable.parent = self
        self.stpxspanningtreeobjects = CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects()
        self.stpxspanningtreeobjects.parent = self
        self.stpxuplinkfastobjects = CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects()
        self.stpxuplinkfastobjects.parent = self


    class StpxBackboneFastObjects(object):
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
        
        .. attribute:: stpxbackbonefastoperenabled
        
        	An indication of whether the BackboneFast capability is operationally enabled on the device
        	**type**\: bool
        
        .. attribute:: stpxbackbonefastoutrlqrequestpdus
        
        	The number of Root Link Query request PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxbackbonefastoutrlqresponsepdus
        
        	The number of Root Link Query response PDUs transmitted by the switch since the stpxBackboneFastOperEnabled has become true(1). If the value of stpxBackboneFastOperEnabled is false(2), then this mib object will have a value of 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxbackbonefastenabled = None
            self.stpxbackbonefastininferiorbpdus = None
            self.stpxbackbonefastinrlqrequestpdus = None
            self.stpxbackbonefastinrlqresponsepdus = None
            self.stpxbackbonefastoperenabled = None
            self.stpxbackbonefastoutrlqrequestpdus = None
            self.stpxbackbonefastoutrlqresponsepdus = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxBackboneFastObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxbackbonefastenabled is not None:
                return True

            if self.stpxbackbonefastininferiorbpdus is not None:
                return True

            if self.stpxbackbonefastinrlqrequestpdus is not None:
                return True

            if self.stpxbackbonefastinrlqresponsepdus is not None:
                return True

            if self.stpxbackbonefastoperenabled is not None:
                return True

            if self.stpxbackbonefastoutrlqrequestpdus is not None:
                return True

            if self.stpxbackbonefastoutrlqresponsepdus is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects']['meta_info']


    class StpxBpduSkewingObjects(object):
        """
        
        
        .. attribute:: stpxbpduskewingdetectionenable
        
        	Indicates whether BPDU skewing detection feature is enabled or not on the system. If this object has the value of true(1), then the system will detect whether BPDUs received by any port on any Spanning  Tree instance are processed at an interval longer than the object value of dot1dStpHelloTime in the BIRDGE\-MIB of the Spanning Tree instance
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxbpduskewingdetectionenable = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxbpduskewingdetectionenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects']['meta_info']


    class StpxBpduSkewingTable(object):
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
        	**type**\: list of :py:class:`StpxBpduSkewingEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxbpduskewingentry = YList()
            self.stpxbpduskewingentry.parent = self
            self.stpxbpduskewingentry.name = 'stpxbpduskewingentry'


        class StpxBpduSkewingEntry(object):
            """
            A Spanning Tree instance on a particular port for
            which BPDU skewing has been detected.
            
            .. attribute:: stpxbpduskewinginstanceindex
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType  is pvstPlus(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxbpduskewingportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxbpduskewinglastskewduration
            
            	Indicates the skew duration in milliseconds of the last BPDU skewing detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxbpduskewingworstskewduration
            
            	Indicates the skew duration in milliseconds of the worst BPDU skewing detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxbpduskewingworstskewtime
            
            	Indicates the value of sysUpTime when the worst BPDU skewing was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxbpduskewinginstanceindex = None
                self.stpxbpduskewingportindex = None
                self.stpxbpduskewinglastskewduration = None
                self.stpxbpduskewingworstskewduration = None
                self.stpxbpduskewingworstskewtime = None

            @property
            def _common_path(self):
                if self.stpxbpduskewinginstanceindex is None:
                    raise YPYDataValidationError('Key property stpxbpduskewinginstanceindex is None')
                if self.stpxbpduskewingportindex is None:
                    raise YPYDataValidationError('Key property stpxbpduskewingportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingTable/CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingEntry[CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingInstanceIndex = ' + str(self.stpxbpduskewinginstanceindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingPortIndex = ' + str(self.stpxbpduskewingportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxbpduskewinginstanceindex is not None:
                    return True

                if self.stpxbpduskewingportindex is not None:
                    return True

                if self.stpxbpduskewinglastskewduration is not None:
                    return True

                if self.stpxbpduskewingworstskewduration is not None:
                    return True

                if self.stpxbpduskewingworstskewtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxBpduSkewingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxbpduskewingentry is not None:
                for child_ref in self.stpxbpduskewingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable']['meta_info']


    class StpxFastStartObjects(object):
        """
        
        
        .. attribute:: stpxfaststartbpdufilterenable
        
        	Indicates the global default mode of the Bpdu  Filter feature on the device.  On platforms that does not support per port  Bpdu Filter configuration as indicated by the object stpxFastStartPortBpduFilterMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then no BPDUs will be  transmitted on this port
        	**type**\: bool
        
        .. attribute:: stpxfaststartbpduguardenable
        
        	Indicates the global default mode of the Bpdu Guard feature on the device.  On platforms that does not support per port  Bpdu Guard configuration as indicated by the object stpxFastStartPortBpduGuardMode, if  the value of this object is set to true(1),  and the Fast Start Feature is operationally  enabled on a port, then that port will be  immediately disabled when the system receives a BPDU from that port
        	**type**\: bool
        
        .. attribute:: stpxfaststartglobaldefaultmode
        
        	Indicates the global default mode of the Fast  Start feature on the device
        	**type**\: :py:class:`StpxFastStartGlobalDefaultMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartObjects.StpxFastStartGlobalDefaultMode_Enum>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxfaststartbpdufilterenable = None
            self.stpxfaststartbpduguardenable = None
            self.stpxfaststartglobaldefaultmode = None

        class StpxFastStartGlobalDefaultMode_Enum(Enum):
            """
            StpxFastStartGlobalDefaultMode_Enum

            Indicates the global default mode of the Fast 
            Start feature on the device.

            """

            ENABLE = 1

            DISABLE = 2


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartObjects.StpxFastStartGlobalDefaultMode_Enum']


        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxFastStartObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxfaststartbpdufilterenable is not None:
                return True

            if self.stpxfaststartbpduguardenable is not None:
                return True

            if self.stpxfaststartglobaldefaultmode is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartObjects']['meta_info']


    class StpxFastStartOperModeTable(object):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        
        .. attribute:: stpxfaststartopermodeentry
        
        	An entry with port fast start oper mode  information on a bridge port for a particular  Spanning Tree Instance
        	**type**\: list of :py:class:`StpxFastStartOperModeEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxfaststartopermodeentry = YList()
            self.stpxfaststartopermodeentry.parent = self
            self.stpxfaststartopermodeentry.name = 'stpxfaststartopermodeentry'


        class StpxFastStartOperModeEntry(object):
            """
            An entry with port fast start oper mode 
            information on a bridge port for a particular 
            Spanning Tree Instance.
            
            .. attribute:: stpxfaststartopermodeinstindex
            
            	The Spanning Tree instance id, such as the VLAN id  of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxfaststartopermodeportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartopermode
            
            	Indicates the fast start operational status of the  port on a particular Spanning Tree Instance
            	**type**\: :py:class:`StpxFastStartOperMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry.StpxFastStartOperMode_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxfaststartopermodeinstindex = None
                self.stpxfaststartopermodeportindex = None
                self.stpxfaststartopermode = None

            class StpxFastStartOperMode_Enum(Enum):
                """
                StpxFastStartOperMode_Enum

                Indicates the fast start operational status of the 
                port on a particular Spanning Tree Instance.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry.StpxFastStartOperMode_Enum']


            @property
            def _common_path(self):
                if self.stpxfaststartopermodeinstindex is None:
                    raise YPYDataValidationError('Key property stpxfaststartopermodeinstindex is None')
                if self.stpxfaststartopermodeportindex is None:
                    raise YPYDataValidationError('Key property stpxfaststartopermodeportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxFastStartOperModeTable/CISCO-STP-EXTENSIONS-MIB:stpxFastStartOperModeEntry[CISCO-STP-EXTENSIONS-MIB:stpxFastStartOperModeInstIndex = ' + str(self.stpxfaststartopermodeinstindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxFastStartOperModePortIndex = ' + str(self.stpxfaststartopermodeportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxfaststartopermodeinstindex is not None:
                    return True

                if self.stpxfaststartopermodeportindex is not None:
                    return True

                if self.stpxfaststartopermode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxFastStartOperModeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxfaststartopermodeentry is not None:
                for child_ref in self.stpxfaststartopermodeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable']['meta_info']


    class StpxFastStartPortTable(object):
        """
        A table containing a list of the bridge ports for
        which Spanning Tree Port Fast Start can be
        configured.
        
        .. attribute:: stpxfaststartportentry
        
        	A bridge port for which Spanning Tree Port Fast Start can be configured
        	**type**\: list of :py:class:`StpxFastStartPortEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxfaststartportentry = YList()
            self.stpxfaststartportentry.parent = self
            self.stpxfaststartportentry.name = 'stpxfaststartportentry'


        class StpxFastStartPortEntry(object):
            """
            A bridge port for which Spanning Tree Port Fast
            Start can be configured.
            
            .. attribute:: stpxfaststartportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxfaststartportbpdufiltermode
            
            	Indicates the mode of Bpdu Filter Feature on the port. The system will not transmit BPDUs on a port  with Bpdu Filter feature enabled.  enable \-\- the Bpdu Filter feature is enabled on this            port.   disable \-\- the Bpdu Filter feature is disabled on this            port.  default \-\- whether the Bpdu Filter feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduFilterEnable. If            the value of stpxFastStartBpduFilterEnable            is true(1) and Fast Start feature is also            enabled operationally on this port, then            no BPDUs will be transmitted on this port
            	**type**\: :py:class:`StpxFastStartPortBpduFilterMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduFilterMode_Enum>`
            
            .. attribute:: stpxfaststartportbpduguardmode
            
            	Indicates the mode of Bpdu Guard Feature on the port. A port with Bpdu Guard enabled is  immediately disabled when the system  receives a BPDU from that port.   enable \-\- the Bpdu Guard feature is enabled on this           port.   disable \-\- the Bpdu Guard feature is disabled on this           port.  default \-\- whether the Bpdu Guard feature is enabled            or not on this port depends on the object            value of stpxFastStartBpduGuardEnable. If             the value of stpxFastStartBpduGuardEnable            is true(1) and Fast Start feature is also             enabled operationally on this port, then            this port is immediately disabled when             the system receives a BPDU from this port
            	**type**\: :py:class:`StpxFastStartPortBpduGuardMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduGuardMode_Enum>`
            
            .. attribute:: stpxfaststartportenable
            
            	Indicates whether the port is operating in spantree fast start mode.  A port with fast start enabled is immediately put in spanning tree forwarding state when that port is detected by the Spanning Tree, rather  than starting in blocking state which is the normal  operation.  In order to support additional Fast Start enable mode (enableForTrunk and default) as defined in stpxFastStartPortMode other than enable (true(1)) or disable (false(2)) as defined in this object, stpxFastStartPortMode object needs to be used.  When the stpxFastStartPortMode has the value of enable(1) or enableForTrunk(3), the value of stpxFastStartPortEnable for the same instance will be true(1). When the stpxFastStartPortMode has the value of disable(2), the value of  stpxFastStartPortEnable for the same instance will be  false(2). When the stpxFastStartPortMode has the value  of default(4), the value of stpxFastStartPortEnable for  the same instance depends on the object value of  stpxFastStartGlobalDefaultMode
            	**type**\: bool
            
            .. attribute:: stpxfaststartportmode
            
            	Indicates the mode of Fast Start Feature on the  port. A port with fast start enabled is immediately  put in spanning tree forwarding state when the port is detected by the Spanning Tree, rather than  starting in blocking state which is the normal  operation.  enable \-\- the fast start feature is enabled on this            port but will only take effect when the            object value of its            vlanTrunkPortDynamicStatus as specified            in CISCO\-VTP\-MIB is notTrunking(2).  disable \-\- the fast start feature is disabled on this            port.    enableForTrunk \-\- the fast start feature is enabled            on this port and will take effect            regardless of the object value of            its vlanTrunkPortDynamicStatus.  default \-\- whether the fast start feature is enabled            or not on this port depends on the object             value of stpxFastStartGlobalDefaultMode.  network \-\- the fast start network mode is enabled on             this port
            	**type**\: :py:class:`StpxFastStartPortMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortMode_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxfaststartportindex = None
                self.stpxfaststartportbpdufiltermode = None
                self.stpxfaststartportbpduguardmode = None
                self.stpxfaststartportenable = None
                self.stpxfaststartportmode = None

            class StpxFastStartPortBpduFilterMode_Enum(Enum):
                """
                StpxFastStartPortBpduFilterMode_Enum

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

                """

                ENABLE = 1

                DISABLE = 2

                DEFAULT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduFilterMode_Enum']


            class StpxFastStartPortBpduGuardMode_Enum(Enum):
                """
                StpxFastStartPortBpduGuardMode_Enum

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

                """

                ENABLE = 1

                DISABLE = 2

                DEFAULT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduGuardMode_Enum']


            class StpxFastStartPortMode_Enum(Enum):
                """
                StpxFastStartPortMode_Enum

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

                """

                ENABLE = 1

                DISABLE = 2

                ENABLEFORTRUNK = 3

                DEFAULT = 4

                NETWORK = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortMode_Enum']


            @property
            def _common_path(self):
                if self.stpxfaststartportindex is None:
                    raise YPYDataValidationError('Key property stpxfaststartportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxFastStartPortTable/CISCO-STP-EXTENSIONS-MIB:stpxFastStartPortEntry[CISCO-STP-EXTENSIONS-MIB:stpxFastStartPortIndex = ' + str(self.stpxfaststartportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxfaststartportindex is not None:
                    return True

                if self.stpxfaststartportbpdufiltermode is not None:
                    return True

                if self.stpxfaststartportbpduguardmode is not None:
                    return True

                if self.stpxfaststartportenable is not None:
                    return True

                if self.stpxfaststartportmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxFastStartPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxfaststartportentry is not None:
                for child_ref in self.stpxfaststartportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable']['meta_info']


    class StpxInconsistencyTable(object):
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
        	**type**\: list of :py:class:`StpxInconsistencyEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxinconsistencyentry = YList()
            self.stpxinconsistencyentry.parent = self
            self.stpxinconsistencyentry.name = 'stpxinconsistencyentry'


        class StpxInconsistencyEntry(object):
            """
            A VLAN on a particular port for which a Spanning Tree
            inconsistency is currently in effect.
            
            .. attribute:: stpxportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxvlanindex
            
            	The VLAN id of the VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxinconsistentstate
            
            	The types of inconsistency which have been discovered on this port for this VLAN's Spanning Tree.  When this object exists, the value of the corresponding instance of the Bridge MIB's dot1dStpPortState object will be 'broken(6)'
            	**type**\: :py:class:`StpxInconsistentState_Bits <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry.StpxInconsistentState_Bits>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxportindex = None
                self.stpxvlanindex = None
                self.stpxinconsistentstate = CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry.StpxInconsistentState_Bits()

            class StpxInconsistentState_Bits(FixedBitsDict):
                """
                StpxInconsistentState_Bits

                The types of inconsistency which have been discovered on
                this port for this VLAN's Spanning Tree.
                
                When this object exists, the value of the corresponding
                instance of the Bridge MIB's dot1dStpPortState object will
                be 'broken(6)'.
                Keys are:- typeInconsistent , pvidInconsistent

                """

                def __init__(self):
                    self._dictionary = { 
                        'typeInconsistent':False,
                        'pvidInconsistent':False,
                    }
                    self._pos_map = { 
                        'typeInconsistent':0,
                        'pvidInconsistent':1,
                    }

            @property
            def _common_path(self):
                if self.stpxportindex is None:
                    raise YPYDataValidationError('Key property stpxportindex is None')
                if self.stpxvlanindex is None:
                    raise YPYDataValidationError('Key property stpxvlanindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxInconsistencyTable/CISCO-STP-EXTENSIONS-MIB:stpxInconsistencyEntry[CISCO-STP-EXTENSIONS-MIB:stpxPortIndex = ' + str(self.stpxportindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxVlanIndex = ' + str(self.stpxvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxportindex is not None:
                    return True

                if self.stpxvlanindex is not None:
                    return True

                if self.stpxinconsistentstate is not None:
                    if self.stpxinconsistentstate._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxInconsistencyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxinconsistencyentry is not None:
                for child_ref in self.stpxinconsistencyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable']['meta_info']


    class StpxLoopGuardConfigTable(object):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree LoopGuard capability can be configured.
        
        .. attribute:: stpxloopguardconfigentry
        
        	A bridge port for which Spanning Tree LoopGuard  capability can be configured
        	**type**\: list of :py:class:`StpxLoopGuardConfigEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxloopguardconfigentry = YList()
            self.stpxloopguardconfigentry.parent = self
            self.stpxloopguardconfigentry.name = 'stpxloopguardconfigentry'


        class StpxLoopGuardConfigEntry(object):
            """
            A bridge port for which Spanning Tree LoopGuard 
            capability can be configured.
            
            .. attribute:: stpxloopguardconfigportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopguardconfigenabled
            
            	An indication of whether the LoopGuard capability is  enabled on this port or not. This configuration will be applied to all the Spanning Tree instances in which this  port exists.  In order to support additional Loop Guard config mode (default) as defined in stpxLoopGuardConfigMode other  than enable (true(1)) or disable (false(2)) as defined  in this object, stpxLoopGuardConfigMode object needs to  be used.  When the stpxLoopGuardConfigMode object has the value of enable(1), the value of stpxLoopGuardConfigEnabled for  the same instance will be true(1). When the  stpxLoopGuardConfigMode object has the value of disable(2),  the value of stpxLoopGuardConfigEnabled for the same  instance will be false(2). When the stpxLoopGuardConfigMode  object has the value of default(3), the value of  stpxLoopGuardConfigEnabled for the same instance will  depend on the object value of  stpxLoopGuardGlobalDefaultMode
            	**type**\: bool
            
            .. attribute:: stpxloopguardconfigmode
            
            	Indicates the mode of Loop Guard Feature on this  port. This configuration will be applied to all  the Spanning Tree instances in which this port  exists.  enable \-\- the Loop Guard feature is enabled on this            port.   disable \-\- the Loop Guard feature is disabled on this            port.    default \-\- whether the Loop Guard feature is enabled            or not on this port depends on the object             value of stpxLoopGuardGlobalDefaultMode
            	**type**\: :py:class:`StpxLoopGuardConfigMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry.StpxLoopGuardConfigMode_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxloopguardconfigportindex = None
                self.stpxloopguardconfigenabled = None
                self.stpxloopguardconfigmode = None

            class StpxLoopGuardConfigMode_Enum(Enum):
                """
                StpxLoopGuardConfigMode_Enum

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

                """

                ENABLE = 1

                DISABLE = 2

                DEFAULT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry.StpxLoopGuardConfigMode_Enum']


            @property
            def _common_path(self):
                if self.stpxloopguardconfigportindex is None:
                    raise YPYDataValidationError('Key property stpxloopguardconfigportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxLoopGuardConfigTable/CISCO-STP-EXTENSIONS-MIB:stpxLoopGuardConfigEntry[CISCO-STP-EXTENSIONS-MIB:stpxLoopGuardConfigPortIndex = ' + str(self.stpxloopguardconfigportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxloopguardconfigportindex is not None:
                    return True

                if self.stpxloopguardconfigenabled is not None:
                    return True

                if self.stpxloopguardconfigmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxLoopGuardConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxloopguardconfigentry is not None:
                for child_ref in self.stpxloopguardconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable']['meta_info']


    class StpxLoopGuardObjects(object):
        """
        
        
        .. attribute:: stpxloopguardglobaldefaultmode
        
        	Indicates the global default config mode of LoopGuard  feature on the device
        	**type**\: :py:class:`StpxLoopGuardGlobalDefaultMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects.StpxLoopGuardGlobalDefaultMode_Enum>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxloopguardglobaldefaultmode = None

        class StpxLoopGuardGlobalDefaultMode_Enum(Enum):
            """
            StpxLoopGuardGlobalDefaultMode_Enum

            Indicates the global default config mode of LoopGuard 
            feature on the device.

            """

            ENABLE = 1

            DISABLE = 2


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects.StpxLoopGuardGlobalDefaultMode_Enum']


        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxLoopGuardObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxloopguardglobaldefaultmode is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects']['meta_info']


    class StpxLoopInconsistencyTable(object):
        """
        A table containing a list of the bridge ports for which
        a particular Spanning Tree instance has been found
        to have a loop\-inconsistency. The agent creates a new
        entry in this table whenever it detects a new
        loop\-inconsistency, and deletes entries
        when/soon after the inconsistency is no longer present.
        
        .. attribute:: stpxloopinconsistencyentry
        
        	A Spanning Tree instance on a particular port for which a Spanning Tree loop\-inconsistency is currently in effect
        	**type**\: list of :py:class:`StpxLoopInconsistencyEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxloopinconsistencyentry = YList()
            self.stpxloopinconsistencyentry.parent = self
            self.stpxloopinconsistencyentry.name = 'stpxloopinconsistencyentry'


        class StpxLoopInconsistencyEntry(object):
            """
            A Spanning Tree instance on a particular port for
            which a Spanning Tree loop\-inconsistency is currently
            in effect.
            
            .. attribute:: stpxloopinconsistencyindex
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxloopinconsistencyportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxloopinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in loop\-inconsistent  state or not
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxloopinconsistencyindex = None
                self.stpxloopinconsistencyportindex = None
                self.stpxloopinconsistencystate = None

            @property
            def _common_path(self):
                if self.stpxloopinconsistencyindex is None:
                    raise YPYDataValidationError('Key property stpxloopinconsistencyindex is None')
                if self.stpxloopinconsistencyportindex is None:
                    raise YPYDataValidationError('Key property stpxloopinconsistencyportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxLoopInconsistencyTable/CISCO-STP-EXTENSIONS-MIB:stpxLoopInconsistencyEntry[CISCO-STP-EXTENSIONS-MIB:stpxLoopInconsistencyIndex = ' + str(self.stpxloopinconsistencyindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxLoopInconsistencyPortIndex = ' + str(self.stpxloopinconsistencyportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxloopinconsistencyindex is not None:
                    return True

                if self.stpxloopinconsistencyportindex is not None:
                    return True

                if self.stpxloopinconsistencystate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxLoopInconsistencyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxloopinconsistencyentry is not None:
                for child_ref in self.stpxloopinconsistencyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable']['meta_info']


    class StpxMISTPInstanceTable(object):
        """
        This table contains one entry for each instance of MISTP and 
        it contains stpxMISTPInstanceNumber entries, numbered from 1
        to stpxMISTPInstanceNumber.
        
        This table is only instantiated when the value of 
        stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3).
        
        .. attribute:: stpxmistpinstanceentry
        
        	A conceptual row containing the status of the MISTP  instance
        	**type**\: list of :py:class:`StpxMISTPInstanceEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmistpinstanceentry = YList()
            self.stpxmistpinstanceentry.parent = self
            self.stpxmistpinstanceentry.name = 'stpxmistpinstanceentry'


        class StpxMISTPInstanceEntry(object):
            """
            A conceptual row containing the status of the MISTP 
            instance.
            
            .. attribute:: stpxmistpinstanceindex
            
            	An arbitrary integer within the range from 1 to the value of stpxMISTPInstanceNumber that uniquely identifies an instance
            	**type**\: int
            
            	**range:** 1..256
            
            .. attribute:: stpxmistpinstanceenable
            
            	This object indicates whether the MISTP protocol is currently enabled on the MISTP instance.  If this object is set to    'true'    \- the MISTP protocol will run on this instance.                   'false'   \- the MISTP protocol will stop running on this                 instance
            	**type**\: bool
            
            .. attribute:: stpxmistpinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmistpinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MISTP instance, then the bit corresponding to that VLAN is set to '1'.  This object is only instantiated on devices with  support for VlanIndex up to 4095
            	**type**\: str
            
            	**range:** 0..128
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxmistpinstanceindex = None
                self.stpxmistpinstanceenable = None
                self.stpxmistpinstancevlansmapped = None
                self.stpxmistpinstancevlansmapped2k = None
                self.stpxmistpinstancevlansmapped3k = None
                self.stpxmistpinstancevlansmapped4k = None

            @property
            def _common_path(self):
                if self.stpxmistpinstanceindex is None:
                    raise YPYDataValidationError('Key property stpxmistpinstanceindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMISTPInstanceTable/CISCO-STP-EXTENSIONS-MIB:stpxMISTPInstanceEntry[CISCO-STP-EXTENSIONS-MIB:stpxMISTPInstanceIndex = ' + str(self.stpxmistpinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxmistpinstanceindex is not None:
                    return True

                if self.stpxmistpinstanceenable is not None:
                    return True

                if self.stpxmistpinstancevlansmapped is not None:
                    return True

                if self.stpxmistpinstancevlansmapped2k is not None:
                    return True

                if self.stpxmistpinstancevlansmapped3k is not None:
                    return True

                if self.stpxmistpinstancevlansmapped4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMISTPInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmistpinstanceentry is not None:
                for child_ref in self.stpxmistpinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable']['meta_info']


    class StpxMISTPObjects(object):
        """
        
        
        .. attribute:: stpxmistpinstancenumber
        
        	The number of MISTP instances, that are supported by the device  when the value of stpxSpanningTreeType is either mistp(2) or mistpPvstPlus(3)
        	**type**\: int
        
        	**range:** 1..256
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmistpinstancenumber = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMISTPObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmistpinstancenumber is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPObjects']['meta_info']


    class StpxMSTInstanceEditTable(object):
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
        	**type**\: list of :py:class:`StpxMSTInstanceEditEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmstinstanceeditentry = YList()
            self.stpxmstinstanceeditentry.parent = self
            self.stpxmstinstanceeditentry.name = 'stpxmstinstanceeditentry'


        class StpxMSTInstanceEditEntry(object):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            .. attribute:: stpxmstinstanceeditindex
            
            	An integer that uniquely identifies an MST instance  from 0 to the object value of stpxMSTMaxInstanceNumber.  The instances of this table entry with  stpxMSTInstanceEditIndex of zero can not be  modified.  This object is deprecated and replaced by  stpxSMSTInstanceEditIndex
            	**type**\: int
            
            	**range:** 0..256
            
            .. attribute:: stpxmstinstanceeditvlansmap
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstanceeditvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap1k2k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstanceeditvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by  stpxSMSTInstanceEditVlansMap3k4k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstanceeditvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance in the range from 1 to stpxMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  MST instance 0 by the device.  This object is deprecated and replaced by stpxSMSTInstanceEditVlansMap3k4k
            	**type**\: str
            
            	**range:** 0..128
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxmstinstanceeditindex = None
                self.stpxmstinstanceeditvlansmap = None
                self.stpxmstinstanceeditvlansmap2k = None
                self.stpxmstinstanceeditvlansmap3k = None
                self.stpxmstinstanceeditvlansmap4k = None

            @property
            def _common_path(self):
                if self.stpxmstinstanceeditindex is None:
                    raise YPYDataValidationError('Key property stpxmstinstanceeditindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceEditTable/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceEditEntry[CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceEditIndex = ' + str(self.stpxmstinstanceeditindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxmstinstanceeditindex is not None:
                    return True

                if self.stpxmstinstanceeditvlansmap is not None:
                    return True

                if self.stpxmstinstanceeditvlansmap2k is not None:
                    return True

                if self.stpxmstinstanceeditvlansmap3k is not None:
                    return True

                if self.stpxmstinstanceeditvlansmap4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceEditTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmstinstanceeditentry is not None:
                for child_ref in self.stpxmstinstanceeditentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable']['meta_info']


    class StpxMSTInstanceTable(object):
        """
        This table contains MST instance information with
        one entry for an MST instance within the range of 
        0 to the object value of stpxMSTMaxInstanceNumber. 
        
        This table is deprecated and replaced by 
        stpxSMSTInstanceTable.
        
        .. attribute:: stpxmstinstanceentry
        
        	A conceptual row containing the MST instance  information
        	**type**\: list of :py:class:`StpxMSTInstanceEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmstinstanceentry = YList()
            self.stpxmstinstanceentry.parent = self
            self.stpxmstinstanceentry.name = 'stpxmstinstanceentry'


        class StpxMSTInstanceEntry(object):
            """
            A conceptual row containing the MST instance 
            information.
            
            .. attribute:: stpxmstinstanceindex
            
            	An integer that uniquely identifies an MST instance  within the range of 0 to the object value of stpxMSTMaxInstanceNumber.  This object is deprecated and replaced by  stpxSMSTInstanceIndex
            	**type**\: int
            
            	**range:** 0..256
            
            .. attribute:: stpxmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance.  This object will take on value of 40 if the object value of stpxSMSTInstanceRemainingHopCount is greater than 40.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTInstanceRemainingHopCount
            	**type**\: int
            
            	**range:** 0..40
            
            .. attribute:: stpxmstinstancevlansmapped
            
            	A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstancevlansmapped2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped1k2k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstancevlansmapped3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by  stpxSMSTInstanceVlansMapped3k4k
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxmstinstancevlansmapped4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to '1'.  This object is deprecated and replaced by stpxSMSTInstanceVlansMapped3k4k
            	**type**\: str
            
            	**range:** 0..128
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxmstinstanceindex = None
                self.stpxmstinstanceremaininghopcount = None
                self.stpxmstinstancevlansmapped = None
                self.stpxmstinstancevlansmapped2k = None
                self.stpxmstinstancevlansmapped3k = None
                self.stpxmstinstancevlansmapped4k = None

            @property
            def _common_path(self):
                if self.stpxmstinstanceindex is None:
                    raise YPYDataValidationError('Key property stpxmstinstanceindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceTable/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceEntry[CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceIndex = ' + str(self.stpxmstinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxmstinstanceindex is not None:
                    return True

                if self.stpxmstinstanceremaininghopcount is not None:
                    return True

                if self.stpxmstinstancevlansmapped is not None:
                    return True

                if self.stpxmstinstancevlansmapped2k is not None:
                    return True

                if self.stpxmstinstancevlansmapped3k is not None:
                    return True

                if self.stpxmstinstancevlansmapped4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmstinstanceentry is not None:
                for child_ref in self.stpxmstinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable']['meta_info']


    class StpxMSTObjects(object):
        """
        
        
        .. attribute:: stpxmstmaxhopcount
        
        	The maximum number of hops for the MST region.   This object will take on value of 40 if the object value of stpxSMSTMaxHopCount is greater than 40.  This object is deprecated and replaced by stpxSMSTMaxHopCount
        	**type**\: int
        
        	**range:** 1..40
        
        .. attribute:: stpxmstmaxinstancenumber
        
        	The maximum MST (Multiple Spanning Tree) instance id,  that can be supported by the device for Cisco proprietary implementation of the MST Protocol.  This object is deprecated and replaced by  stpxSMSTMaxInstanceID
        	**type**\: int
        
        	**range:** 1..256
        
        .. attribute:: stpxmstregioneditbufferoperation
        
        	Indicates the operation that is performed on the Region  Config Edit Buffer.  other \-\-   none of the following operations.    acquire \-\- acquire the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value of            released(1). After the successful operation of             this action, the stpxMSTRegionEditBufferStatus            will be changed to acquiredBySnmp(2).               releaseWithForce \-\- release the Edit Buffer acquired by            non\-SNMP users with force and discard the changes            in the Edit Buffer. This operation can only be             performed when the object             stpxMSTRegionEditBufferStatus has the value of             acquiredByNonSnmp(2).  commit \-\-  commit the changes in the Edit Buffer            and release the Edit Buffer. The successful             operation of this action will make the changes            in the Edit Buffer effective on the device.            This operation can only be performed when the             object stpxMSTRegionEditBufferStatus has the             value of acquiredBySnmp(3).   rollBack \-\- discard the changes in the Edit Buffer            and release the Edit Buffer. This operation can             only be performed when the object             stpxMSTRegionEditBufferStatus has the value             of acquiredBySnmp(3).  This object always returns other(1) when it is read
        	**type**\: :py:class:`StpxMSTRegionEditBufferOperation_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferOperation_Enum>`
        
        .. attribute:: stpxmstregioneditbufferstatus
        
        	Indicates the current ownership status of the unique  Region Config Edit Buffer.   released \-\- the Edit Buffer can be acquired by any of              the SNMP management stations.   acquiredBySnmp \-\- the Edit Buffer is acquired by             any of the SNMP management stations.   acquiredByNonSnmp \-\- the Edit Buffer is acquired by the              non\-SNMP users managing the device
        	**type**\: :py:class:`StpxMSTRegionEditBufferStatus_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferStatus_Enum>`
        
        .. attribute:: stpxmstregioneditname
        
        	The MST region name in the Edit Buffer.   This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\: str
        
        	**range:** 0..32
        
        .. attribute:: stpxmstregioneditrevision
        
        	The MST region version in the Edit Buffer. This object is only instantiated when the stpxMSTRegionEditBufferStatus  has the value of acquiredBySnmp(2).  This object is deprecated and replaced by stpxSMSTRegionEditRevision
        	**type**\: int
        
        	**range:** 1..65535
        
        .. attribute:: stpxmstregionname
        
        	The operational MST region name
        	**type**\: str
        
        	**range:** 0..32
        
        .. attribute:: stpxmstregionrevision
        
        	The operational MST region version.  This object is deprecated and replaced by  stpxSMSTRegionRevision
        	**type**\: int
        
        	**range:** 1..65535
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmstmaxhopcount = None
            self.stpxmstmaxinstancenumber = None
            self.stpxmstregioneditbufferoperation = None
            self.stpxmstregioneditbufferstatus = None
            self.stpxmstregioneditname = None
            self.stpxmstregioneditrevision = None
            self.stpxmstregionname = None
            self.stpxmstregionrevision = None

        class StpxMSTRegionEditBufferOperation_Enum(Enum):
            """
            StpxMSTRegionEditBufferOperation_Enum

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

            """

            OTHER = 1

            ACQUIRE = 2

            RELEASEWITHFORCE = 3

            COMMIT = 4

            ROLLBACK = 5


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferOperation_Enum']


        class StpxMSTRegionEditBufferStatus_Enum(Enum):
            """
            StpxMSTRegionEditBufferStatus_Enum

            Indicates the current ownership status of the unique 
            Region Config Edit Buffer. 
            
            released \-\- the Edit Buffer can be acquired by any of 
                        the SNMP management stations. 
            
            acquiredBySnmp \-\- the Edit Buffer is acquired by
                        any of the SNMP management stations. 
            
            acquiredByNonSnmp \-\- the Edit Buffer is acquired by the 
                        non\-SNMP users managing the device.

            """

            RELEASED = 1

            ACQUIREDBYSNMP = 2

            ACQUIREDBYNONSNMP = 3


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferStatus_Enum']


        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmstmaxhopcount is not None:
                return True

            if self.stpxmstmaxinstancenumber is not None:
                return True

            if self.stpxmstregioneditbufferoperation is not None:
                return True

            if self.stpxmstregioneditbufferstatus is not None:
                return True

            if self.stpxmstregioneditname is not None:
                return True

            if self.stpxmstregioneditrevision is not None:
                return True

            if self.stpxmstregionname is not None:
                return True

            if self.stpxmstregionrevision is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTObjects']['meta_info']


    class StpxMSTPortRoleTable(object):
        """
        A table containing a list of the bridge ports for a 
        particular MST instance.  This table is only instantiated 
        when the stpxSpanningTreeType is mst(4). 
        
        This table is deprecated and replaced with 
        stpxRSTPPortRoleTable.
        
        .. attribute:: stpxmstportroleentry
        
        	An entry containing the port role information for the MST protocol on a port for a particular MST instance existing on the system
        	**type**\: list of :py:class:`StpxMSTPortRoleEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmstportroleentry = YList()
            self.stpxmstportroleentry.parent = self
            self.stpxmstportroleentry.name = 'stpxmstportroleentry'


        class StpxMSTPortRoleEntry(object):
            """
            An entry containing the port role information for the MST
            protocol on a port for a particular MST instance existing
            on the system.
            
            .. attribute:: stpxmstportroleinstanceindex
            
            	The MST instance id within the range of 0 to stpxMSTMaxInstanceNumber
            	**type**\: int
            
            	**range:** 0..256
            
            .. attribute:: stpxmstportroleportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxmstportrolevalue
            
            	Indicates the port role on a particular MST instance for the MST protocol.   disabled \-\-  this port has no role on this MST instance.   root \-\- this port has the role of root port on this MST             instance.   designated \-\- this port has the role of designated              port on this MST instance.  alternate \-\- this port has the role of alternate port             on this MST instance.  backUp \-\- this port has the role of backup port on this               MST instance.  boundary \-\- this port has the role of boundary port on              this MST instance.  master \-\- this port has the role of master port on           this MST instance
            	**type**\: :py:class:`StpxMSTPortRoleValue_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry.StpxMSTPortRoleValue_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxmstportroleinstanceindex = None
                self.stpxmstportroleportindex = None
                self.stpxmstportrolevalue = None

            class StpxMSTPortRoleValue_Enum(Enum):
                """
                StpxMSTPortRoleValue_Enum

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

                """

                DISABLED = 1

                ROOT = 2

                DESIGNATED = 3

                ALTERNATE = 4

                BACKUP = 5

                BOUNDARY = 6

                MASTER = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry.StpxMSTPortRoleValue_Enum']


            @property
            def _common_path(self):
                if self.stpxmstportroleinstanceindex is None:
                    raise YPYDataValidationError('Key property stpxmstportroleinstanceindex is None')
                if self.stpxmstportroleportindex is None:
                    raise YPYDataValidationError('Key property stpxmstportroleportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortRoleTable/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortRoleEntry[CISCO-STP-EXTENSIONS-MIB:stpxMSTPortRoleInstanceIndex = ' + str(self.stpxmstportroleinstanceindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxMSTPortRolePortIndex = ' + str(self.stpxmstportroleportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxmstportroleinstanceindex is not None:
                    return True

                if self.stpxmstportroleportindex is not None:
                    return True

                if self.stpxmstportrolevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortRoleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmstportroleentry is not None:
                for child_ref in self.stpxmstportroleentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable']['meta_info']


    class StpxMSTPortTable(object):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        .. attribute:: stpxmstportentry
        
        	An entry with port information for the MST Protocol on a bridge port
        	**type**\: list of :py:class:`StpxMSTPortEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxmstportentry = YList()
            self.stpxmstportentry.parent = self
            self.stpxmstportentry.name = 'stpxmstportentry'


        class StpxMSTPortEntry(object):
            """
            An entry with port information for the MST Protocol
            on a bridge port.
            
            .. attribute:: stpxmstportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxmstportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the MST protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5). stpxMSTPortAdminLinkType is deprecated and replaced  with stpxRSTPPortAdminLinkType
            	**type**\: :py:class:`StpxMSTPortAdminLinkType_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortAdminLinkType_Enum>`
            
            .. attribute:: stpxmstportoperlinktype
            
            	Indicates the operational link type of a bridge port for the MST protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  stpxMSTPortOperLinkType  is deprecated and replaced with stpxRSTPPortOperLinkType
            	**type**\: :py:class:`StpxMSTPortOperLinkType_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortOperLinkType_Enum>`
            
            .. attribute:: stpxmstportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to this  object has no effect. Setting false(2) to this object has  no effect. This object always returns false(2) when read. stpxMSTPortProtocolMigration is deprecated and  replaced with stpxRSTPPortProtocolMigration
            	**type**\: bool
            
            .. attribute:: stpxmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4).  This object is deprecated and replaced by  stpxSMSTPortStatus
            	**type**\: :py:class:`StpxMSTPortStatus_Bits <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortStatus_Bits>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxmstportindex = None
                self.stpxmstportadminlinktype = None
                self.stpxmstportoperlinktype = None
                self.stpxmstportprotocolmigration = None
                self.stpxmstportstatus = CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortStatus_Bits()

            class StpxMSTPortAdminLinkType_Enum(Enum):
                """
                StpxMSTPortAdminLinkType_Enum

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

                """

                POINTTOPOINT = 1

                SHARED = 2

                AUTO = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortAdminLinkType_Enum']


            class StpxMSTPortOperLinkType_Enum(Enum):
                """
                StpxMSTPortOperLinkType_Enum

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

                """

                POINTTOPOINT = 1

                SHARED = 2

                OTHER = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortOperLinkType_Enum']


            class StpxMSTPortStatus_Bits(FixedBitsDict):
                """
                StpxMSTPortStatus_Bits

                Indicates the operational status of the port for the 
                MST protocol. 
                
                edge \-\- this port is an edge port for the MST region.
                
                boundary \-\- this port is a boundary port for the 
                        MST region.
                
                pvst \-\-  this port is connected to a PVST/PVST+ bridge.   
                
                stp \-\- this port is connected to a Single Spanning
                        Tree bridge. 
                
                This object is only instantiated when the object value
                of stpxSpanningTreeType is mst(4).
                
                This object is deprecated and replaced by 
                stpxSMSTPortStatus.
                Keys are:- boundary , edge , stp , pvst

                """

                def __init__(self):
                    self._dictionary = { 
                        'boundary':False,
                        'edge':False,
                        'stp':False,
                        'pvst':False,
                    }
                    self._pos_map = { 
                        'boundary':1,
                        'edge':0,
                        'stp':3,
                        'pvst':2,
                    }

            @property
            def _common_path(self):
                if self.stpxmstportindex is None:
                    raise YPYDataValidationError('Key property stpxmstportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortTable/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortEntry[CISCO-STP-EXTENSIONS-MIB:stpxMSTPortIndex = ' + str(self.stpxmstportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxmstportindex is not None:
                    return True

                if self.stpxmstportadminlinktype is not None:
                    return True

                if self.stpxmstportoperlinktype is not None:
                    return True

                if self.stpxmstportprotocolmigration is not None:
                    return True

                if self.stpxmstportstatus is not None:
                    if self.stpxmstportstatus._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxMSTPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxmstportentry is not None:
                for child_ref in self.stpxmstportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable']['meta_info']


    class StpxPVSTVlanTable(object):
        """
        A list of Virtual LAN entries containing
        information for Spanning Tree PVST+ protocol. 
        An entry will exist for each VLAN existing on 
        the device.
        
        .. attribute:: stpxpvstvlanentry
        
        	An entry containing Spanning Tree PVST+ Protocol  information for a particular Virtual LAN
        	**type**\: list of :py:class:`StpxPVSTVlanEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxpvstvlanentry = YList()
            self.stpxpvstvlanentry.parent = self
            self.stpxpvstvlanentry.name = 'stpxpvstvlanentry'


        class StpxPVSTVlanEntry(object):
            """
            An entry containing Spanning Tree PVST+ Protocol 
            information for a particular Virtual LAN.
            
            .. attribute:: stpxpvstvlanindex
            
            	An index value that uniquely identifies the Virtual LAN associated with this information
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxpvstvlanenable
            
            	Indicates whether Spanning Tree PVST+   Protocol is enabled for this Virtual LAN. If  Spanning Tree PVST+ Protocol is not supported  on this VLAN, then notApplicable(3) will be  returned while retrieving the object value for  this VLAN.  If the device only supports a single global Spanning Tree PVST+ Protocol enable/disable  for all the existing VLANs, then the object  value assigned to this VLAN will be applied to the object values of all the instances in this table which do not have the value of notApplicable(3).  If the value of stpxSpanningTreeType is neither  pvstPlus(1) nor rapidPvstPlus(5), then the value  of stpxPVSTVlanEnable for this VLAN can not be  changed
            	**type**\: :py:class:`StpxPVSTVlanEnable_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry.StpxPVSTVlanEnable_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxpvstvlanindex = None
                self.stpxpvstvlanenable = None

            class StpxPVSTVlanEnable_Enum(Enum):
                """
                StpxPVSTVlanEnable_Enum

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

                """

                ENABLED = 1

                DISABLED = 2

                NOTAPPLICABLE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry.StpxPVSTVlanEnable_Enum']


            @property
            def _common_path(self):
                if self.stpxpvstvlanindex is None:
                    raise YPYDataValidationError('Key property stpxpvstvlanindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxPVSTVlanTable/CISCO-STP-EXTENSIONS-MIB:stpxPVSTVlanEntry[CISCO-STP-EXTENSIONS-MIB:stpxPVSTVlanIndex = ' + str(self.stpxpvstvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxpvstvlanindex is not None:
                    return True

                if self.stpxpvstvlanenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxPVSTVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxpvstvlanentry is not None:
                for child_ref in self.stpxpvstvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable']['meta_info']


    class StpxRPVSTPortTable(object):
        """
        A table containing a list of the bridge ports 
        for a particular Spanning Tree Instance.
        This table is only instantiated when the object value
        of stpxSpanningTreeType is rapidPvstPlus(5).
        
        .. attribute:: stpxrpvstportentry
        
        	An entry with port status information on a  bridge port for a particular Spanning Tree  Instance
        	**type**\: list of :py:class:`StpxRPVSTPortEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrpvstportentry = YList()
            self.stpxrpvstportentry.parent = self
            self.stpxrpvstportentry.name = 'stpxrpvstportentry'


        class StpxRPVSTPortEntry(object):
            """
            An entry with port status information on a 
            bridge port for a particular Spanning Tree 
            Instance.
            
            .. attribute:: stpxrpvstportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrpvstportvlanindex
            
            	The VLAN id of the VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrpvstportstatus
            
            	Indicates the operational status of the port for the  Rapid PVST+ protocol.  edge \-\- this port is an edge port for the RST region.  unused1 \-\- unused bit 1.  unused2 \-\- unused bit 2.  stp \-\- this port is connected to a Single Spanning        Tree/PVST+ bridge.  dispute \-\- this port, as a designated port, received an        inferior BPDU with a designated role and the        learning bit being set
            	**type**\: :py:class:`StpxRPVSTPortStatus_Bits <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry.StpxRPVSTPortStatus_Bits>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxrpvstportindex = None
                self.stpxrpvstportvlanindex = None
                self.stpxrpvstportstatus = CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry.StpxRPVSTPortStatus_Bits()

            class StpxRPVSTPortStatus_Bits(FixedBitsDict):
                """
                StpxRPVSTPortStatus_Bits

                Indicates the operational status of the port for the 
                Rapid PVST+ protocol.
                
                edge \-\- this port is an edge port for the RST region.
                
                unused1 \-\- unused bit 1.
                
                unused2 \-\- unused bit 2.
                
                stp \-\- this port is connected to a Single Spanning
                       Tree/PVST+ bridge.
                
                dispute \-\- this port, as a designated port, received an
                       inferior BPDU with a designated role and the
                       learning bit being set.
                Keys are:- stp , edge , unused1 , dispute , unused2

                """

                def __init__(self):
                    self._dictionary = { 
                        'stp':False,
                        'edge':False,
                        'unused1':False,
                        'dispute':False,
                        'unused2':False,
                    }
                    self._pos_map = { 
                        'stp':3,
                        'edge':0,
                        'unused1':1,
                        'dispute':4,
                        'unused2':2,
                    }

            @property
            def _common_path(self):
                if self.stpxrpvstportindex is None:
                    raise YPYDataValidationError('Key property stpxrpvstportindex is None')
                if self.stpxrpvstportvlanindex is None:
                    raise YPYDataValidationError('Key property stpxrpvstportvlanindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRPVSTPortTable/CISCO-STP-EXTENSIONS-MIB:stpxRPVSTPortEntry[CISCO-STP-EXTENSIONS-MIB:stpxRPVSTPortIndex = ' + str(self.stpxrpvstportindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxRPVSTPortVlanIndex = ' + str(self.stpxrpvstportvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxrpvstportindex is not None:
                    return True

                if self.stpxrpvstportvlanindex is not None:
                    return True

                if self.stpxrpvstportstatus is not None:
                    if self.stpxrpvstportstatus._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRPVSTPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrpvstportentry is not None:
                for child_ref in self.stpxrpvstportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable']['meta_info']


    class StpxRSTPObjects(object):
        """
        
        
        .. attribute:: stpxrstptransmitholdcount
        
        	The Transmit Hold Count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrstptransmitholdcount = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRSTPObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrstptransmitholdcount is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPObjects']['meta_info']


    class StpxRSTPPortRoleTable(object):
        """
        A table containing a list of the bridge ports for a 
        particular Spanning Tree instance.  This table is 
        only instantiated when the stpxSpanningTreeType is mst(4) 
        or rapidPvstPlus(5).
        
        .. attribute:: stpxrstpportroleentry
        
        	An entry containing the port role information for the RSTP protocol on a port for a particular Spanning Tree instance
        	**type**\: list of :py:class:`StpxRSTPPortRoleEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrstpportroleentry = YList()
            self.stpxrstpportroleentry.parent = self
            self.stpxrstpportroleentry.name = 'stpxrstpportroleentry'


        class StpxRSTPPortRoleEntry(object):
            """
            An entry containing the port role information for the RSTP
            protocol on a port for a particular Spanning Tree instance.
            
            .. attribute:: stpxrstpportroleinstanceindex
            
            	The Spanning Tree instance id, it can either be a  VLAN number if the stpxSpanningTreeType is rapidPvstPlus(5)  or an MST instance id if the stpxSpanningTreeType is mst(4)
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxrstpportroleportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportrolevalue
            
            	Indicates the port role on a particular Spanning Tree  instance for the RSTP protocol.   disabled \-\-  this port has no role in this Spanning             Tree instance.   root \-\- this port has the role of root port in this             Spanning Tree instance.   designated \-\- this port has the role of designated              port in this Spanning Tree instance.  alternate \-\- this port has the role of alternate port             in this Spanning Tree instance.  backUp \-\- this port has the role of backup port in this               Spanning Tree instance.  boundary \-\- this port has the role of boundary port in              this Spanning Tree instance.  master \-\- this port has the role of master port in             this Spanning Tree instance.  This object could have a value of 'boundary' or 'master' only when the object value of stpxSpanningTreeType is mst(4)
            	**type**\: :py:class:`StpxRSTPPortRoleValue_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry.StpxRSTPPortRoleValue_Enum>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxrstpportroleinstanceindex = None
                self.stpxrstpportroleportindex = None
                self.stpxrstpportrolevalue = None

            class StpxRSTPPortRoleValue_Enum(Enum):
                """
                StpxRSTPPortRoleValue_Enum

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

                """

                DISABLED = 1

                ROOT = 2

                DESIGNATED = 3

                ALTERNATE = 4

                BACKUP = 5

                BOUNDARY = 6

                MASTER = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry.StpxRSTPPortRoleValue_Enum']


            @property
            def _common_path(self):
                if self.stpxrstpportroleinstanceindex is None:
                    raise YPYDataValidationError('Key property stpxrstpportroleinstanceindex is None')
                if self.stpxrstpportroleportindex is None:
                    raise YPYDataValidationError('Key property stpxrstpportroleportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortRoleTable/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortRoleEntry[CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortRoleInstanceIndex = ' + str(self.stpxrstpportroleinstanceindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortRolePortIndex = ' + str(self.stpxrstpportroleportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxrstpportroleinstanceindex is not None:
                    return True

                if self.stpxrstpportroleportindex is not None:
                    return True

                if self.stpxrstpportrolevalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortRoleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrstpportroleentry is not None:
                for child_ref in self.stpxrstpportroleentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable']['meta_info']


    class StpxRSTPPortTable(object):
        """
        A table containing port information for the RSTP 
        Protocol on all the bridge ports existing in the 
        system.
        
        .. attribute:: stpxrstpportentry
        
        	An entry with port information for the RSTP Protocol on a bridge port
        	**type**\: list of :py:class:`StpxRSTPPortEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrstpportentry = YList()
            self.stpxrstpportentry.parent = self
            self.stpxrstpportentry.name = 'stpxrstpportentry'


        class StpxRSTPPortEntry(object):
            """
            An entry with port information for the RSTP Protocol
            on a bridge port.
            
            .. attribute:: stpxrstpportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrstpportadminlinktype
            
            	Indicates the administrative link type configuration of  a bridge port for the RSTP protocol.   pointToPoint \-\- the port is administratively configured to         be connected to a point\-to\-point link.  shared \-\- the port is administratively configured to be         connected to a shared medium.   auto \-\- the administrative configuration of the port's          link type depends on link duplex of the port.         If the port link is full\-duplex, the administrative          link type configuration on this port will be taken          as pointTopoint(1). If the port link is half\-duplex,          the administrative link type configuration on this         port will be taken as shared(2).  This configuration of this object only takes effect when the stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\: :py:class:`StpxRSTPPortAdminLinkType_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortAdminLinkType_Enum>`
            
            .. attribute:: stpxrstpportoperlinktype
            
            	Indicates the operational link type of a bridge port for the RSTP protocol.  pointToPoint \-\- the port is operationally connected to         a point\-to\-point link.  shared \-\- the port is operationally connected to          a shared medium.  other \-\- none of the above.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) or rapidPvstPlus(5)
            	**type**\: :py:class:`StpxRSTPPortOperLinkType_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortOperLinkType_Enum>`
            
            .. attribute:: stpxrstpportprotocolmigration
            
            	The protocol migration control on this port. When the  object value of  stpxSpanningTreeType is mst(4) or  rapidPvstPlus(5), setting true(1) to this object forces  the device to try using version 2 BPDUs on this port.  When the object value of stpxSpanningTreeType is neither  mst(4) nor rapidPvstPlus(5), setting true(1) to  this object has no effect. Setting false(2) to this  object has no effect. This object always returns  false(2) when read
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxrstpportindex = None
                self.stpxrstpportadminlinktype = None
                self.stpxrstpportoperlinktype = None
                self.stpxrstpportprotocolmigration = None

            class StpxRSTPPortAdminLinkType_Enum(Enum):
                """
                StpxRSTPPortAdminLinkType_Enum

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

                """

                POINTTOPOINT = 1

                SHARED = 2

                AUTO = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortAdminLinkType_Enum']


            class StpxRSTPPortOperLinkType_Enum(Enum):
                """
                StpxRSTPPortOperLinkType_Enum

                Indicates the operational link type of a bridge port
                for the RSTP protocol.
                
                pointToPoint \-\- the port is operationally connected to
                        a point\-to\-point link.
                
                shared \-\- the port is operationally connected to 
                        a shared medium.
                
                other \-\- none of the above.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).

                """

                POINTTOPOINT = 1

                SHARED = 2

                OTHER = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortOperLinkType_Enum']


            @property
            def _common_path(self):
                if self.stpxrstpportindex is None:
                    raise YPYDataValidationError('Key property stpxrstpportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortTable/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortEntry[CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortIndex = ' + str(self.stpxrstpportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxrstpportindex is not None:
                    return True

                if self.stpxrstpportadminlinktype is not None:
                    return True

                if self.stpxrstpportoperlinktype is not None:
                    return True

                if self.stpxrstpportprotocolmigration is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRSTPPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrstpportentry is not None:
                for child_ref in self.stpxrstpportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable']['meta_info']


    class StpxRootGuardConfigTable(object):
        """
        A table containing a list of the bridge ports for which
        Spanning Tree RootGuard capability can be configured.
        
        .. attribute:: stpxrootguardconfigentry
        
        	A bridge port for which Spanning Tree RootGuard capability can be configured
        	**type**\: list of :py:class:`StpxRootGuardConfigEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrootguardconfigentry = YList()
            self.stpxrootguardconfigentry.parent = self
            self.stpxrootguardconfigentry.name = 'stpxrootguardconfigentry'


        class StpxRootGuardConfigEntry(object):
            """
            A bridge port for which Spanning Tree RootGuard
            capability can be configured.
            
            .. attribute:: stpxrootguardconfigportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootguardconfigenabled
            
            	An indication of whether the RootGuard capability is  enabled on this port or not. This configuration will be applied to all Spanning Tree instances in which this port  exists
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxrootguardconfigportindex = None
                self.stpxrootguardconfigenabled = None

            @property
            def _common_path(self):
                if self.stpxrootguardconfigportindex is None:
                    raise YPYDataValidationError('Key property stpxrootguardconfigportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRootGuardConfigTable/CISCO-STP-EXTENSIONS-MIB:stpxRootGuardConfigEntry[CISCO-STP-EXTENSIONS-MIB:stpxRootGuardConfigPortIndex = ' + str(self.stpxrootguardconfigportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxrootguardconfigportindex is not None:
                    return True

                if self.stpxrootguardconfigenabled is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRootGuardConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrootguardconfigentry is not None:
                for child_ref in self.stpxrootguardconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable']['meta_info']


    class StpxRootInconsistencyTable(object):
        """
        A table containing a list of the bridge ports for which
        a particular Spanning Tree instance has been found 
        to have an root\-inconsistency. The agent creates a new 
        entry in this table whenever it detects a new 
        root\-inconsistency, and deletes entries 
        when/soon after the inconsistency is no longer present.
        
        .. attribute:: stpxrootinconsistencyentry
        
        	A Spanning Tree instance on a particular port for  which a Spanning Tree root\-inconsistency is currently  in effect
        	**type**\: list of :py:class:`StpxRootInconsistencyEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxrootinconsistencyentry = YList()
            self.stpxrootinconsistencyentry.parent = self
            self.stpxrootinconsistencyentry.name = 'stpxrootinconsistencyentry'


        class StpxRootInconsistencyEntry(object):
            """
            A Spanning Tree instance on a particular port for 
            which a Spanning Tree root\-inconsistency is currently 
            in effect.
            
            .. attribute:: stpxrootinconsistencyindex
            
            	The Spanning Tree instance id, such as the VLAN id of the VLAN if the object value of stpxSpanningTreeType is pvstPlus(1) or rapidPvstPlus(5)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: stpxrootinconsistencyportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxrootinconsistencystate
            
            	Indicates whether the port on a particular Spanning  Tree instance is currently in root\-inconsistent  state or not
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxrootinconsistencyindex = None
                self.stpxrootinconsistencyportindex = None
                self.stpxrootinconsistencystate = None

            @property
            def _common_path(self):
                if self.stpxrootinconsistencyindex is None:
                    raise YPYDataValidationError('Key property stpxrootinconsistencyindex is None')
                if self.stpxrootinconsistencyportindex is None:
                    raise YPYDataValidationError('Key property stpxrootinconsistencyportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRootInconsistencyTable/CISCO-STP-EXTENSIONS-MIB:stpxRootInconsistencyEntry[CISCO-STP-EXTENSIONS-MIB:stpxRootInconsistencyIndex = ' + str(self.stpxrootinconsistencyindex) + '][CISCO-STP-EXTENSIONS-MIB:stpxRootInconsistencyPortIndex = ' + str(self.stpxrootinconsistencyportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxrootinconsistencyindex is not None:
                    return True

                if self.stpxrootinconsistencyportindex is not None:
                    return True

                if self.stpxrootinconsistencystate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxRootInconsistencyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxrootinconsistencyentry is not None:
                for child_ref in self.stpxrootinconsistencyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable']['meta_info']


    class StpxSMSTInstanceEditTable(object):
        """
        This table contains MST instance information in the 
        Edit Buffer. 
        
        This table is only instantiated when the object value
        of  stpxMSTRegionEditBufferStatus has the value of
        acquiredBySnmp(2).
        
        .. attribute:: stpxsmstinstanceeditentry
        
        	A conceptual row containing MST instance information  in the Edit Buffer.  The total number of entries in this table has to be  less than or equal to the object value of stpxSMSTMaxInstances
        	**type**\: list of :py:class:`StpxSMSTInstanceEditEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxsmstinstanceeditentry = YList()
            self.stpxsmstinstanceeditentry.parent = self
            self.stpxsmstinstanceeditentry.name = 'stpxsmstinstanceeditentry'


        class StpxSMSTInstanceEditEntry(object):
            """
            A conceptual row containing MST instance information 
            in the Edit Buffer.
            
            The total number of entries in this table has to be 
            less than or equal to the object value of stpxSMSTMaxInstances.
            
            .. attribute:: stpxsmstinstanceeditindex
            
            	The MST instance ID, the value of which is in the range from 0 to stpxSMSTMaxInstanceID.   The instances of this table entry with  stpxSMSTInstanceEditIndex of zero is automatically created by the device and can not modified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstanceeditrowstatus
            
            	This object controls the creation and deletion of a row  in stpxSMSTInstanceEditTable.  When creating an entry in this table, 'createAndGo' method is used and the value of this object is set to 'active'. Deactivation of an 'active' entry is not allowed.  When  deleting an entry in this table, 'destroy' method is used.  Once a row becomes active, value in any other column  within such a row may be modified. When a row is active,  setting the instance of stpxSMSTInstanceEditVlansMap1k2k stpxSMSTInstanceEditVlansMap3k4k for the same MST instance both to the value of zero length can not be allowed
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: stpxsmstinstanceeditvlansmap1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance,  then the bit corresponding to that VLAN is set to  '1'. Each VLAN can only be mapped to one unique MST  instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1'  to '0', then that VLAN will be automatically mapped to  SMST instance 0 by the device. If the bit corresponding  to a VLAN is changed from '0' to '1', then that VLAN will  be automatically removed from the MST instance this VLAN was  previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: stpxsmstinstanceeditvlansmap3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. Each VLAN can only be mapped to one unique MST instance with the range from 0 to stpxSMSTMaxInstanceNumber. If the bit corresponding to a VLAN is changed from '1' to '0', then that VLAN will be automatically mapped to SMST instance 0 by the device. If the bit corresponding to a VLAN is changed from '0' to '1', then that VLAN will be automatically removed from the MST instance this VLAN was previously mapped to. If the length of this string is  less than 256 octets, any 'missing' octets are assumed to  contain the value of zero
            	**type**\: str
            
            	**range:** 0..256
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxsmstinstanceeditindex = None
                self.stpxsmstinstanceeditrowstatus = None
                self.stpxsmstinstanceeditvlansmap1k2k = None
                self.stpxsmstinstanceeditvlansmap3k4k = None

            @property
            def _common_path(self):
                if self.stpxsmstinstanceeditindex is None:
                    raise YPYDataValidationError('Key property stpxsmstinstanceeditindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceEditTable/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceEditEntry[CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceEditIndex = ' + str(self.stpxsmstinstanceeditindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxsmstinstanceeditindex is not None:
                    return True

                if self.stpxsmstinstanceeditrowstatus is not None:
                    return True

                if self.stpxsmstinstanceeditvlansmap1k2k is not None:
                    return True

                if self.stpxsmstinstanceeditvlansmap3k4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceEditTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxsmstinstanceeditentry is not None:
                for child_ref in self.stpxsmstinstanceeditentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable']['meta_info']


    class StpxSMSTInstanceTable(object):
        """
        This table contains MST instance information
        for IEEE MST.
        
        .. attribute:: stpxsmstinstanceentry
        
        	A conceptual row containing the MST instance  information for IEEE MST
        	**type**\: list of :py:class:`StpxSMSTInstanceEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxsmstinstanceentry = YList()
            self.stpxsmstinstanceentry.parent = self
            self.stpxsmstinstanceentry.name = 'stpxsmstinstanceentry'


        class StpxSMSTInstanceEntry(object):
            """
            A conceptual row containing the MST instance 
            information for IEEE MST.
            
            .. attribute:: stpxsmstinstanceindex
            
            	The MST instance ID, the value of which is in the range  from 0 to stpxSMSTMaxInstanceID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstancecistintrootcost
            
            	Indicates the CIST Internal Root Path Cost, i.e., the path cost to the CIST Regional Root as specified by the corresponding stpxSMSTInstanceCISTRegionalRoot for the  MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstinstancecistregionalroot
            
            	Indicates the Bridge Identifier (refer to BridgeId  defined in BRIDGE\-MIB) of CIST (Common and Internal  Spanning Tree) Regional Root for the MST region.  This object is only instantiated when the object value of stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex is 0
            	**type**\: str
            
            	**range:** 8
            
            .. attribute:: stpxsmstinstanceremaininghopcount
            
            	The remaining hop count for this MST instance. If this object value is not applicable on an MST instance, then the value retrieved for this object for that MST instance will be \-1.   This object is only instantiated when the object value of stpxSpanningTreeType is mst(4)
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: stpxsmstinstancevlansmapped1k2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 0 through 2047. The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: stpxsmstinstancevlansmapped3k4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 4095. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is mapped to this MST instance, then the bit corresponding to that VLAN is set to '1'. If the length of this string is less than 256 octets, any 'missing' octets are assumed to contain the value  of zero
            	**type**\: str
            
            	**range:** 0..256
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxsmstinstanceindex = None
                self.stpxsmstinstancecistintrootcost = None
                self.stpxsmstinstancecistregionalroot = None
                self.stpxsmstinstanceremaininghopcount = None
                self.stpxsmstinstancevlansmapped1k2k = None
                self.stpxsmstinstancevlansmapped3k4k = None

            @property
            def _common_path(self):
                if self.stpxsmstinstanceindex is None:
                    raise YPYDataValidationError('Key property stpxsmstinstanceindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceTable/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceEntry[CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceIndex = ' + str(self.stpxsmstinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxsmstinstanceindex is not None:
                    return True

                if self.stpxsmstinstancecistintrootcost is not None:
                    return True

                if self.stpxsmstinstancecistregionalroot is not None:
                    return True

                if self.stpxsmstinstanceremaininghopcount is not None:
                    return True

                if self.stpxsmstinstancevlansmapped1k2k is not None:
                    return True

                if self.stpxsmstinstancevlansmapped3k4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTInstanceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxsmstinstanceentry is not None:
                for child_ref in self.stpxsmstinstanceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable']['meta_info']


    class StpxSMSTObjects(object):
        """
        
        
        .. attribute:: stpxsmstconfigdigest
        
        	The IEEE MST region configuration digest
        	**type**\: str
        
        .. attribute:: stpxsmstconfigprestandarddigest
        
        	The pre\-standard MST region configuration digest
        	**type**\: str
        
        .. attribute:: stpxsmstmaxhopcount
        
        	The maximum number of hops for the IEEE MST region
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxinstanceid
        
        	The maximum MST instance ID that can be supported  by the device for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstmaxinstances
        
        	The maximum number of MST instances that can be  supported by the device for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregioneditrevision
        
        	The MST region version in the Edit Buffer for IEEE  MST.  This object is only instantiated when the  stpxMSTRegionEditBufferStatus has the value of  acquiredBySnmp(2)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxsmstregionrevision
        
        	The operational region version for IEEE MST
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxsmstconfigdigest = None
            self.stpxsmstconfigprestandarddigest = None
            self.stpxsmstmaxhopcount = None
            self.stpxsmstmaxinstanceid = None
            self.stpxsmstmaxinstances = None
            self.stpxsmstregioneditrevision = None
            self.stpxsmstregionrevision = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxsmstconfigdigest is not None:
                return True

            if self.stpxsmstconfigprestandarddigest is not None:
                return True

            if self.stpxsmstmaxhopcount is not None:
                return True

            if self.stpxsmstmaxinstanceid is not None:
                return True

            if self.stpxsmstmaxinstances is not None:
                return True

            if self.stpxsmstregioneditrevision is not None:
                return True

            if self.stpxsmstregionrevision is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTObjects']['meta_info']


    class StpxSMSTPortTable(object):
        """
        A table containing port information for the MST 
        Protocol on all the bridge ports existing on the 
        system.
        
        This table is only instantiated when the object 
        value of stpxSpanningTreeType is mst(4)
        
        .. attribute:: stpxsmstportentry
        
        	An entry with port information for the MST protocol on a bridge port
        	**type**\: list of :py:class:`StpxSMSTPortEntry <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxsmstportentry = YList()
            self.stpxsmstportentry.parent = self
            self.stpxsmstportentry.name = 'stpxsmstportentry'


        class StpxSMSTPortEntry(object):
            """
            An entry with port information for the MST protocol
            on a bridge port.
            
            .. attribute:: stpxsmstportindex
            
            	The value of dot1dBasePort (i.e. dot1dBridge.1.4) for the bridge port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: stpxsmstportadminhellotime
            
            	The adminitratively configured hello time in hundredth  of seconds on a port for IEEE MST. The granularity  of this timer is 1 second. An agent may return a badValue  error if a set is attempted to a value which is not a  whole number of seconds. This object value of zero means the hello time is not specifically configured on  this port and object value of stpxSMSTPortConfigedHelloTime retrieved for this port will take on the value of  dot1dStpBridgeHelloTime defined in BRIDGE\-MIB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstportadminmstmode
            
            	The desired MST mode of this port.  preStandard \-\- this port is administratively configured to     transmit pre\-standard, i.e. pre IEEE MST, BPDUs.  auto \-\- the BPDU transmission mode of this port is based      on automatic detection of neighbor ports
            	**type**\: :py:class:`StpxSMSTPortAdminMSTMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortAdminMSTMode_Enum>`
            
            .. attribute:: stpxsmstportconfigedhellotime
            
            	Indicates the effective configuration of the hello time on  a port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stpxsmstportoperhellotime
            
            	The operational hello time in hundredth of seconds on a  port for IEEE MST. If this object value is not applicable on a port, then the value retrieved on that port will be \-1
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: stpxsmstportopermstmode
            
            	Indicates the current operational MST mode of this port.  unknown \-\- the operational mode is currently unknown.  preStandard \-\- this port is currently operating in      pre\-standard MSTP BPDU transmission mode.  standard \-\- this port is currently operating in IEEE MST      BPDU transmission mode
            	**type**\: :py:class:`StpxSMSTPortOperMSTMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortOperMSTMode_Enum>`
            
            .. attribute:: stpxsmstportstatus
            
            	Indicates the operational status of the port for the  MST protocol.   edge \-\- this port is an edge port for the MST region.  boundary \-\- this port is a boundary port for the          MST region.  pvst \-\-  this port is connected to a PVST/PVST+ bridge.     stp \-\- this port is connected to a Single Spanning         Tree bridge.  dispute \-\- this port, as a designated port, received an         inferior BPDU with a designated role and the         learning bit being set.  rstp \-\- this port is connected to a RSTP bridge or an          MST bridge in a different MST region
            	**type**\: :py:class:`StpxSMSTPortStatus_Bits <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortStatus_Bits>`
            
            

            """

            _prefix = 'cisco-stp'
            _revision = '2013-03-07'

            def __init__(self):
                self.parent = None
                self.stpxsmstportindex = None
                self.stpxsmstportadminhellotime = None
                self.stpxsmstportadminmstmode = None
                self.stpxsmstportconfigedhellotime = None
                self.stpxsmstportoperhellotime = None
                self.stpxsmstportopermstmode = None
                self.stpxsmstportstatus = CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortStatus_Bits()

            class StpxSMSTPortAdminMSTMode_Enum(Enum):
                """
                StpxSMSTPortAdminMSTMode_Enum

                The desired MST mode of this port.
                
                preStandard \-\- this port is administratively configured to
                    transmit pre\-standard, i.e. pre IEEE MST, BPDUs.
                
                auto \-\- the BPDU transmission mode of this port is based 
                    on automatic detection of neighbor ports.

                """

                PRESTANDARD = 1

                AUTO = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortAdminMSTMode_Enum']


            class StpxSMSTPortOperMSTMode_Enum(Enum):
                """
                StpxSMSTPortOperMSTMode_Enum

                Indicates the current operational MST mode of this port.
                
                unknown \-\- the operational mode is currently unknown.
                
                preStandard \-\- this port is currently operating in 
                    pre\-standard MSTP BPDU transmission mode.
                
                standard \-\- this port is currently operating in IEEE MST 
                    BPDU transmission mode.

                """

                UNKNOWN = 1

                PRESTANDARD = 2

                STANDARD = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                    return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortOperMSTMode_Enum']


            class StpxSMSTPortStatus_Bits(FixedBitsDict):
                """
                StpxSMSTPortStatus_Bits

                Indicates the operational status of the port for the 
                MST protocol. 
                
                edge \-\- this port is an edge port for the MST region.
                
                boundary \-\- this port is a boundary port for the 
                        MST region.
                
                pvst \-\-  this port is connected to a PVST/PVST+ bridge.   
                
                stp \-\- this port is connected to a Single Spanning
                        Tree bridge.
                
                dispute \-\- this port, as a designated port, received an
                        inferior BPDU with a designated role and the
                        learning bit being set.
                
                rstp \-\- this port is connected to a RSTP bridge or an 
                        MST bridge in a different MST region.
                Keys are:- rstp , edge , stp , boundary , pvst , dispute

                """

                def __init__(self):
                    self._dictionary = { 
                        'rstp':False,
                        'edge':False,
                        'stp':False,
                        'boundary':False,
                        'pvst':False,
                        'dispute':False,
                    }
                    self._pos_map = { 
                        'rstp':5,
                        'edge':0,
                        'stp':3,
                        'boundary':1,
                        'pvst':2,
                        'dispute':4,
                    }

            @property
            def _common_path(self):
                if self.stpxsmstportindex is None:
                    raise YPYDataValidationError('Key property stpxsmstportindex is None')

                return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTPortTable/CISCO-STP-EXTENSIONS-MIB:stpxSMSTPortEntry[CISCO-STP-EXTENSIONS-MIB:stpxSMSTPortIndex = ' + str(self.stpxsmstportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.stpxsmstportindex is not None:
                    return True

                if self.stpxsmstportadminhellotime is not None:
                    return True

                if self.stpxsmstportadminmstmode is not None:
                    return True

                if self.stpxsmstportconfigedhellotime is not None:
                    return True

                if self.stpxsmstportoperhellotime is not None:
                    return True

                if self.stpxsmstportopermstmode is not None:
                    return True

                if self.stpxsmstportstatus is not None:
                    if self.stpxsmstportstatus._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSMSTPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxsmstportentry is not None:
                for child_ref in self.stpxsmstportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable']['meta_info']


    class StpxSpanningTreeObjects(object):
        """
        
        
        .. attribute:: stpxextendedsysidadminenabled
        
        	Indicates whether Extended System ID feature  is administratively enabled on the device or not
        	**type**\: bool
        
        .. attribute:: stpxextendedsysidoperenabled
        
        	Indicates whether Extended System ID feature  is operationaly enabled on the device or not.  If the value of this object is true(1), then the accepted values for dot1dStpPriority in BRIDGE\-MIB should be multiples of 4096 plus bridge instance ID, such as VlanIndex. Changing this object value might cause the values of dot1dBaseBridgeAddress and dot1dStpPriority in BRIDGE\-MIB to be changed also
        	**type**\: bool
        
        .. attribute:: stpxnotificationenable
        
        	Indicates whether a specified notification is enabled or not. If a bit corresponding to a notification is set to 1, then  the specified notification can be generated.  newRoot \-\- the newRoot notification as defined in BRIDGE\-MIB.  topologyChange \-\- the topologyChange notification as                   defined in BRIDGE\-MIB.  inconsistency \-\- the stpxInconsistencyUpdate notification.  rootInconsistency \-\- the stpxRootInconsistencyUpdate                       notification.  loopInconsistency \-\- the stpxLoopInconsistencyUpdate                       notification
        	**type**\: :py:class:`StpxNotificationEnable_Bits <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxNotificationEnable_Bits>`
        
        .. attribute:: stpxspanningtreepathcostmode
        
        	Indicates the administrative  spanning tree path cost mode  configured on device
        	**type**\: :py:class:`StpxSpanningTreePathCostMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostMode_Enum>`
        
        .. attribute:: stpxspanningtreepathcostopermode
        
        	Indicate the operational spanning tree path cost mode on device. This mode applies to all instances of the Spanning Tree protocol running on the device.   When the value of this MIB object gets changed, the path cost of all ports will be reassigned to the default path cost values based on the new spanning tree path cost mode and the ports' speed.  When the value of this MIB object is long(2), the stpxLongStpPortPathCost MIB object must be used in order to retrieve/configure the spanning tree port path cost as a 32 bits value. The set operation on dot1dStpPortPathCost in BRIDGE\-MIB will be rejected. While retrieving the value of dot1dStpPortPathCost, the maximum value of 65535 will be returned if the value of stpxLongStpPortPathCost for the same instance exceeds 65535.  When the value of this MIB object is short(1), the dot1dStpPortPathCost in BRIDGE\-MIB must be used
        	**type**\: :py:class:`StpxSpanningTreePathCostOperMode_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostOperMode_Enum>`
        
        .. attribute:: stpxspanningtreetype
        
        	The actual mode of spanning tree protocol runs on the  device. It can be one of the following\:  pvstPlus \-\- PVST+ (Per VLAN Spanning Tree+ Protocol).  mistp \-\- MISTP (Multi Instance Spanning Tree Protocol).  mistpPvstPlus \-\-  MISTP with the tunneling scheme                      enabled for PVST+.  mst \-\- IEEE 802.1s Multiple Spanning Tree (MST)        with IEEE 802.1w Rapid Spanning Tree Protocol        (RSTP).  rapidPvstPlus \-\- IEEE 802.1w Rapid Spanning Tree          Protocol (RSTP) for all vlans in PVST+.  When the value of this MIB object gets changed, the  network connectivity would be affected and the  connectivity to this device would also be lost  temporarily
        	**type**\: :py:class:`StpxSpanningTreeType_Enum <ydk.models.stp.CISCO_STP_EXTENSIONS_MIB.CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreeType_Enum>`
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxextendedsysidadminenabled = None
            self.stpxextendedsysidoperenabled = None
            self.stpxnotificationenable = CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxNotificationEnable_Bits()
            self.stpxspanningtreepathcostmode = None
            self.stpxspanningtreepathcostopermode = None
            self.stpxspanningtreetype = None

        class StpxSpanningTreePathCostMode_Enum(Enum):
            """
            StpxSpanningTreePathCostMode_Enum

            Indicates the administrative  spanning tree path cost mode 
            configured on device.

            """

            SHORT = 1

            LONG = 2


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostMode_Enum']


        class StpxSpanningTreePathCostOperMode_Enum(Enum):
            """
            StpxSpanningTreePathCostOperMode_Enum

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

            """

            SHORT = 1

            LONG = 2


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostOperMode_Enum']


        class StpxSpanningTreeType_Enum(Enum):
            """
            StpxSpanningTreeType_Enum

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

            """

            PVSTPLUS = 1

            MISTP = 2

            MISTPPVSTPLUS = 3

            MST = 4

            RAPIDPVSTPLUS = 5


            @staticmethod
            def _meta_info():
                from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
                return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreeType_Enum']


        class StpxNotificationEnable_Bits(FixedBitsDict):
            """
            StpxNotificationEnable_Bits

            Indicates whether a specified notification is enabled or not.
            If a bit corresponding to a notification is set to 1, then 
            the specified notification can be generated.
            
            newRoot \-\- the newRoot notification as defined in BRIDGE\-MIB.
            
            topologyChange \-\- the topologyChange notification as
                              defined in BRIDGE\-MIB.
            
            inconsistency \-\- the stpxInconsistencyUpdate notification.
            
            rootInconsistency \-\- the stpxRootInconsistencyUpdate 
                                 notification.
            
            loopInconsistency \-\- the stpxLoopInconsistencyUpdate 
                                 notification.
            Keys are:- loopInconsistency , newRoot , rootInconsistency , inconsistency , topologyChange

            """

            def __init__(self):
                self._dictionary = { 
                    'loopInconsistency':False,
                    'newRoot':False,
                    'rootInconsistency':False,
                    'inconsistency':False,
                    'topologyChange':False,
                }
                self._pos_map = { 
                    'loopInconsistency':4,
                    'newRoot':0,
                    'rootInconsistency':3,
                    'inconsistency':2,
                    'topologyChange':1,
                }

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxSpanningTreeObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxextendedsysidadminenabled is not None:
                return True

            if self.stpxextendedsysidoperenabled is not None:
                return True

            if self.stpxnotificationenable is not None:
                if self.stpxnotificationenable._has_data():
                    return True

            if self.stpxspanningtreepathcostmode is not None:
                return True

            if self.stpxspanningtreepathcostopermode is not None:
                return True

            if self.stpxspanningtreetype is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects']['meta_info']


    class StpxUplinkFastObjects(object):
        """
        
        
        .. attribute:: stpxuplinkfastenabled
        
        	An indication of whether the UplinkFast capability is administratively enabled on the device.  If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is  mst(4), then this object is not instantiated
        	**type**\: bool
        
        .. attribute:: stpxuplinkfastoperenabled
        
        	An indication of whether the UplinkFast capability is  operationally enabled on the device
        	**type**\: bool
        
        .. attribute:: stpxuplinkfasttransitions
        
        	The cumulative number of UplinkFast transitions (from the STP 'Blocking' state directly to the STP 'Forwarding' state).  All transitions are included in this counter, irrespective of the instance of the Spanning Tree  Protocol on which they occur.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxuplinkstationlearningframes
        
        	The cumulative number of station\-learning frames generated due to UplinkFast transitions.  All generated station\-learning frames are included in this counter, irrespective of the instance of the Spanning Tree Protocol on which the UplinkFast transition occurred.  If the platform supports the stpxUplinkFastOperEnabled  object, then this object is not instantiated when the  object value of stpxUplinkFastOperEnabled is false(2). If the platform does not support the  stpxUplinkFastOperEnabled object, then this object is  not instantiated when the object value of  stpxSpanningTreeType is mst(4)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stpxuplinkstationlearninggenrate
        
        	The maximum number of station\-learning frames that this device will generate in each 100 milli\-second period after a UplinkFast transition.  By configuring this object, the network administrator can limit the rate at which station\-learning frames are generated.    If the platform does not support configuration of this object when the object value of stpxSpanningTreeType is mst(4), then this object is not instantiated
        	**type**\: int
        
        	**range:** 0..32000
        
        

        """

        _prefix = 'cisco-stp'
        _revision = '2013-03-07'

        def __init__(self):
            self.parent = None
            self.stpxuplinkfastenabled = None
            self.stpxuplinkfastoperenabled = None
            self.stpxuplinkfasttransitions = None
            self.stpxuplinkstationlearningframes = None
            self.stpxuplinkstationlearninggenrate = None

        @property
        def _common_path(self):

            return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB/CISCO-STP-EXTENSIONS-MIB:stpxUplinkFastObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.stpxuplinkfastenabled is not None:
                return True

            if self.stpxuplinkfastoperenabled is not None:
                return True

            if self.stpxuplinkfasttransitions is not None:
                return True

            if self.stpxuplinkstationlearningframes is not None:
                return True

            if self.stpxuplinkstationlearninggenrate is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
            return meta._meta_table['CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-STP-EXTENSIONS-MIB:CISCO-STP-EXTENSIONS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.stpxbackbonefastobjects is not None and self.stpxbackbonefastobjects._has_data():
            return True

        if self.stpxbackbonefastobjects is not None and self.stpxbackbonefastobjects.is_presence():
            return True

        if self.stpxbpduskewingobjects is not None and self.stpxbpduskewingobjects._has_data():
            return True

        if self.stpxbpduskewingobjects is not None and self.stpxbpduskewingobjects.is_presence():
            return True

        if self.stpxbpduskewingtable is not None and self.stpxbpduskewingtable._has_data():
            return True

        if self.stpxbpduskewingtable is not None and self.stpxbpduskewingtable.is_presence():
            return True

        if self.stpxfaststartobjects is not None and self.stpxfaststartobjects._has_data():
            return True

        if self.stpxfaststartobjects is not None and self.stpxfaststartobjects.is_presence():
            return True

        if self.stpxfaststartopermodetable is not None and self.stpxfaststartopermodetable._has_data():
            return True

        if self.stpxfaststartopermodetable is not None and self.stpxfaststartopermodetable.is_presence():
            return True

        if self.stpxfaststartporttable is not None and self.stpxfaststartporttable._has_data():
            return True

        if self.stpxfaststartporttable is not None and self.stpxfaststartporttable.is_presence():
            return True

        if self.stpxinconsistencytable is not None and self.stpxinconsistencytable._has_data():
            return True

        if self.stpxinconsistencytable is not None and self.stpxinconsistencytable.is_presence():
            return True

        if self.stpxloopguardconfigtable is not None and self.stpxloopguardconfigtable._has_data():
            return True

        if self.stpxloopguardconfigtable is not None and self.stpxloopguardconfigtable.is_presence():
            return True

        if self.stpxloopguardobjects is not None and self.stpxloopguardobjects._has_data():
            return True

        if self.stpxloopguardobjects is not None and self.stpxloopguardobjects.is_presence():
            return True

        if self.stpxloopinconsistencytable is not None and self.stpxloopinconsistencytable._has_data():
            return True

        if self.stpxloopinconsistencytable is not None and self.stpxloopinconsistencytable.is_presence():
            return True

        if self.stpxmistpinstancetable is not None and self.stpxmistpinstancetable._has_data():
            return True

        if self.stpxmistpinstancetable is not None and self.stpxmistpinstancetable.is_presence():
            return True

        if self.stpxmistpobjects is not None and self.stpxmistpobjects._has_data():
            return True

        if self.stpxmistpobjects is not None and self.stpxmistpobjects.is_presence():
            return True

        if self.stpxmstinstanceedittable is not None and self.stpxmstinstanceedittable._has_data():
            return True

        if self.stpxmstinstanceedittable is not None and self.stpxmstinstanceedittable.is_presence():
            return True

        if self.stpxmstinstancetable is not None and self.stpxmstinstancetable._has_data():
            return True

        if self.stpxmstinstancetable is not None and self.stpxmstinstancetable.is_presence():
            return True

        if self.stpxmstobjects is not None and self.stpxmstobjects._has_data():
            return True

        if self.stpxmstobjects is not None and self.stpxmstobjects.is_presence():
            return True

        if self.stpxmstportroletable is not None and self.stpxmstportroletable._has_data():
            return True

        if self.stpxmstportroletable is not None and self.stpxmstportroletable.is_presence():
            return True

        if self.stpxmstporttable is not None and self.stpxmstporttable._has_data():
            return True

        if self.stpxmstporttable is not None and self.stpxmstporttable.is_presence():
            return True

        if self.stpxpvstvlantable is not None and self.stpxpvstvlantable._has_data():
            return True

        if self.stpxpvstvlantable is not None and self.stpxpvstvlantable.is_presence():
            return True

        if self.stpxrootguardconfigtable is not None and self.stpxrootguardconfigtable._has_data():
            return True

        if self.stpxrootguardconfigtable is not None and self.stpxrootguardconfigtable.is_presence():
            return True

        if self.stpxrootinconsistencytable is not None and self.stpxrootinconsistencytable._has_data():
            return True

        if self.stpxrootinconsistencytable is not None and self.stpxrootinconsistencytable.is_presence():
            return True

        if self.stpxrpvstporttable is not None and self.stpxrpvstporttable._has_data():
            return True

        if self.stpxrpvstporttable is not None and self.stpxrpvstporttable.is_presence():
            return True

        if self.stpxrstpobjects is not None and self.stpxrstpobjects._has_data():
            return True

        if self.stpxrstpobjects is not None and self.stpxrstpobjects.is_presence():
            return True

        if self.stpxrstpportroletable is not None and self.stpxrstpportroletable._has_data():
            return True

        if self.stpxrstpportroletable is not None and self.stpxrstpportroletable.is_presence():
            return True

        if self.stpxrstpporttable is not None and self.stpxrstpporttable._has_data():
            return True

        if self.stpxrstpporttable is not None and self.stpxrstpporttable.is_presence():
            return True

        if self.stpxsmstinstanceedittable is not None and self.stpxsmstinstanceedittable._has_data():
            return True

        if self.stpxsmstinstanceedittable is not None and self.stpxsmstinstanceedittable.is_presence():
            return True

        if self.stpxsmstinstancetable is not None and self.stpxsmstinstancetable._has_data():
            return True

        if self.stpxsmstinstancetable is not None and self.stpxsmstinstancetable.is_presence():
            return True

        if self.stpxsmstobjects is not None and self.stpxsmstobjects._has_data():
            return True

        if self.stpxsmstobjects is not None and self.stpxsmstobjects.is_presence():
            return True

        if self.stpxsmstporttable is not None and self.stpxsmstporttable._has_data():
            return True

        if self.stpxsmstporttable is not None and self.stpxsmstporttable.is_presence():
            return True

        if self.stpxspanningtreeobjects is not None and self.stpxspanningtreeobjects._has_data():
            return True

        if self.stpxspanningtreeobjects is not None and self.stpxspanningtreeobjects.is_presence():
            return True

        if self.stpxuplinkfastobjects is not None and self.stpxuplinkfastobjects._has_data():
            return True

        if self.stpxuplinkfastobjects is not None and self.stpxuplinkfastobjects.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.stp._meta import _CISCO_STP_EXTENSIONS_MIB as meta
        return meta._meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']


