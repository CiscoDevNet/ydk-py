""" Q_BRIDGE_MIB 

The VLAN Bridge MIB module for managing Virtual Bridged
Local Area Networks, as defined by IEEE 802.1Q\-2003,
including Restricted Vlan Registration defined by
IEEE 802.1u\-2001 and Vlan Classification defined by
IEEE 802.1v\-2001.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4363; See the RFC itself for
full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class QBRIDGEMIB(Entity):
    """
    
    
    .. attribute:: dot1qbase
    
    	
    	**type**\:  :py:class:`Dot1qBase <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qBase>`
    
    	**config**\: False
    
    .. attribute:: dot1qvlan
    
    	
    	**type**\:  :py:class:`Dot1qVlan <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlan>`
    
    	**config**\: False
    
    .. attribute:: dot1qfdbtable
    
    	A table that contains configuration and control information for each Filtering Database currently operating on this device.  Entries in this table appear automatically when VLANs are assigned FDB IDs in the dot1qVlanCurrentTable
    	**type**\:  :py:class:`Dot1qFdbTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qtpfdbtable
    
    	A table that contains information about unicast entries for which the device has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\:  :py:class:`Dot1qTpFdbTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qtpgrouptable
    
    	A table containing filtering information for VLANs configured into the bridge by (local or network) management, or learned dynamically, specifying the set of ports to which frames received on a VLAN for this FDB and containing a specific Group destination address are allowed to be forwarded
    	**type**\:  :py:class:`Dot1qTpGroupTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpGroupTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qforwardalltable
    
    	A table containing forwarding information for each  VLAN, specifying the set of ports to which forwarding of all multicasts applies, configured statically by management or dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\:  :py:class:`Dot1qForwardAllTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardAllTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qforwardunregisteredtable
    
    	A table containing forwarding information for each VLAN, specifying the set of ports to which forwarding of multicast group\-addressed frames for which no more specific forwarding information applies.  This is configured statically by management and determined dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\:  :py:class:`Dot1qForwardUnregisteredTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardUnregisteredTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qstaticunicasttable
    
    	A table containing filtering information for Unicast MAC addresses for each Filtering Database, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific unicast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from  which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast addresses only
    	**type**\:  :py:class:`Dot1qStaticUnicastTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qstaticmulticasttable
    
    	A table containing filtering information for Multicast and Broadcast MAC addresses for each VLAN, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific Multicast and Broadcast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for Multicast and Broadcast addresses only
    	**type**\:  :py:class:`Dot1qStaticMulticastTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qvlancurrenttable
    
    	A table containing current configuration information for each VLAN currently configured into the device by (local or network) management, or dynamically created as a result of GVRP requests received
    	**type**\:  :py:class:`Dot1qVlanCurrentTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qvlanstatictable
    
    	A table containing static configuration information for each VLAN configured into the device by (local or network) management.  All entries are permanent and will be restored after the device is reset
    	**type**\:  :py:class:`Dot1qVlanStaticTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanStaticTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qportvlanstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic received.  Separate objects are provided for both the most\-significant and least\-significant bits of statistics counters for ports that are associated with this transparent bridge.  The most\-significant bit objects are only required on high\-capacity interfaces, as defined in the conformance clauses for these objects.  This mechanism is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\- significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling. The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or  asynchronous notification
    	**type**\:  :py:class:`Dot1qPortVlanStatisticsTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanStatisticsTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qportvlanhcstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic on high\-capacity interfaces
    	**type**\:  :py:class:`Dot1qPortVlanHCStatisticsTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable>`
    
    	**config**\: False
    
    .. attribute:: dot1qlearningconstraintstable
    
    	A table containing learning constraints for sets of Shared and Independent VLANs
    	**type**\:  :py:class:`Dot1qLearningConstraintsTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable>`
    
    	**config**\: False
    
    .. attribute:: dot1vprotocolgrouptable
    
    	A table that contains mappings from Protocol Templates to Protocol Group Identifiers used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\:  :py:class:`Dot1vProtocolGroupTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable>`
    
    	**config**\: False
    
    .. attribute:: dot1vprotocolporttable
    
    	A table that contains VID sets used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\:  :py:class:`Dot1vProtocolPortTable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolPortTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'Q-BRIDGE-MIB'
    _revision = '2006-01-09'

    def __init__(self):
        super(QBRIDGEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "Q-BRIDGE-MIB"
        self.yang_parent_name = "Q-BRIDGE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dot1qBase", ("dot1qbase", QBRIDGEMIB.Dot1qBase)), ("dot1qVlan", ("dot1qvlan", QBRIDGEMIB.Dot1qVlan)), ("dot1qFdbTable", ("dot1qfdbtable", QBRIDGEMIB.Dot1qFdbTable)), ("dot1qTpFdbTable", ("dot1qtpfdbtable", QBRIDGEMIB.Dot1qTpFdbTable)), ("dot1qTpGroupTable", ("dot1qtpgrouptable", QBRIDGEMIB.Dot1qTpGroupTable)), ("dot1qForwardAllTable", ("dot1qforwardalltable", QBRIDGEMIB.Dot1qForwardAllTable)), ("dot1qForwardUnregisteredTable", ("dot1qforwardunregisteredtable", QBRIDGEMIB.Dot1qForwardUnregisteredTable)), ("dot1qStaticUnicastTable", ("dot1qstaticunicasttable", QBRIDGEMIB.Dot1qStaticUnicastTable)), ("dot1qStaticMulticastTable", ("dot1qstaticmulticasttable", QBRIDGEMIB.Dot1qStaticMulticastTable)), ("dot1qVlanCurrentTable", ("dot1qvlancurrenttable", QBRIDGEMIB.Dot1qVlanCurrentTable)), ("dot1qVlanStaticTable", ("dot1qvlanstatictable", QBRIDGEMIB.Dot1qVlanStaticTable)), ("dot1qPortVlanStatisticsTable", ("dot1qportvlanstatisticstable", QBRIDGEMIB.Dot1qPortVlanStatisticsTable)), ("dot1qPortVlanHCStatisticsTable", ("dot1qportvlanhcstatisticstable", QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable)), ("dot1qLearningConstraintsTable", ("dot1qlearningconstraintstable", QBRIDGEMIB.Dot1qLearningConstraintsTable)), ("dot1vProtocolGroupTable", ("dot1vprotocolgrouptable", QBRIDGEMIB.Dot1vProtocolGroupTable)), ("dot1vProtocolPortTable", ("dot1vprotocolporttable", QBRIDGEMIB.Dot1vProtocolPortTable))])
        self._leafs = OrderedDict()

        self.dot1qbase = QBRIDGEMIB.Dot1qBase()
        self.dot1qbase.parent = self
        self._children_name_map["dot1qbase"] = "dot1qBase"

        self.dot1qvlan = QBRIDGEMIB.Dot1qVlan()
        self.dot1qvlan.parent = self
        self._children_name_map["dot1qvlan"] = "dot1qVlan"

        self.dot1qfdbtable = QBRIDGEMIB.Dot1qFdbTable()
        self.dot1qfdbtable.parent = self
        self._children_name_map["dot1qfdbtable"] = "dot1qFdbTable"

        self.dot1qtpfdbtable = QBRIDGEMIB.Dot1qTpFdbTable()
        self.dot1qtpfdbtable.parent = self
        self._children_name_map["dot1qtpfdbtable"] = "dot1qTpFdbTable"

        self.dot1qtpgrouptable = QBRIDGEMIB.Dot1qTpGroupTable()
        self.dot1qtpgrouptable.parent = self
        self._children_name_map["dot1qtpgrouptable"] = "dot1qTpGroupTable"

        self.dot1qforwardalltable = QBRIDGEMIB.Dot1qForwardAllTable()
        self.dot1qforwardalltable.parent = self
        self._children_name_map["dot1qforwardalltable"] = "dot1qForwardAllTable"

        self.dot1qforwardunregisteredtable = QBRIDGEMIB.Dot1qForwardUnregisteredTable()
        self.dot1qforwardunregisteredtable.parent = self
        self._children_name_map["dot1qforwardunregisteredtable"] = "dot1qForwardUnregisteredTable"

        self.dot1qstaticunicasttable = QBRIDGEMIB.Dot1qStaticUnicastTable()
        self.dot1qstaticunicasttable.parent = self
        self._children_name_map["dot1qstaticunicasttable"] = "dot1qStaticUnicastTable"

        self.dot1qstaticmulticasttable = QBRIDGEMIB.Dot1qStaticMulticastTable()
        self.dot1qstaticmulticasttable.parent = self
        self._children_name_map["dot1qstaticmulticasttable"] = "dot1qStaticMulticastTable"

        self.dot1qvlancurrenttable = QBRIDGEMIB.Dot1qVlanCurrentTable()
        self.dot1qvlancurrenttable.parent = self
        self._children_name_map["dot1qvlancurrenttable"] = "dot1qVlanCurrentTable"

        self.dot1qvlanstatictable = QBRIDGEMIB.Dot1qVlanStaticTable()
        self.dot1qvlanstatictable.parent = self
        self._children_name_map["dot1qvlanstatictable"] = "dot1qVlanStaticTable"

        self.dot1qportvlanstatisticstable = QBRIDGEMIB.Dot1qPortVlanStatisticsTable()
        self.dot1qportvlanstatisticstable.parent = self
        self._children_name_map["dot1qportvlanstatisticstable"] = "dot1qPortVlanStatisticsTable"

        self.dot1qportvlanhcstatisticstable = QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable()
        self.dot1qportvlanhcstatisticstable.parent = self
        self._children_name_map["dot1qportvlanhcstatisticstable"] = "dot1qPortVlanHCStatisticsTable"

        self.dot1qlearningconstraintstable = QBRIDGEMIB.Dot1qLearningConstraintsTable()
        self.dot1qlearningconstraintstable.parent = self
        self._children_name_map["dot1qlearningconstraintstable"] = "dot1qLearningConstraintsTable"

        self.dot1vprotocolgrouptable = QBRIDGEMIB.Dot1vProtocolGroupTable()
        self.dot1vprotocolgrouptable.parent = self
        self._children_name_map["dot1vprotocolgrouptable"] = "dot1vProtocolGroupTable"

        self.dot1vprotocolporttable = QBRIDGEMIB.Dot1vProtocolPortTable()
        self.dot1vprotocolporttable.parent = self
        self._children_name_map["dot1vprotocolporttable"] = "dot1vProtocolPortTable"
        self._segment_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(QBRIDGEMIB, [], name, value)


    class Dot1qBase(Entity):
        """
        
        
        .. attribute:: dot1qvlanversionnumber
        
        	The version number of IEEE 802.1Q that this device supports
        	**type**\:  :py:class:`Dot1qVlanVersionNumber <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qBase.Dot1qVlanVersionNumber>`
        
        	**config**\: False
        
        .. attribute:: dot1qmaxvlanid
        
        	The maximum IEEE 802.1Q VLAN\-ID that this device  supports
        	**type**\: int
        
        	**range:** 1..4094
        
        	**config**\: False
        
        .. attribute:: dot1qmaxsupportedvlans
        
        	The maximum number of IEEE 802.1Q VLANs that this device supports
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: dot1qnumvlans
        
        	The current number of IEEE 802.1Q VLANs that are configured in this device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: dot1qgvrpstatus
        
        	The administrative status requested by management for GVRP.  The value enabled(1) indicates that GVRP should be enabled on this device, on all ports for which it has not been specifically disabled.  When disabled(2), GVRP is disabled on all ports, and all GVRP packets will be forwarded transparently.  This object affects all GVRP Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GVRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:  :py:class:`EnabledStatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledStatus>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qBase, self).__init__()

            self.yang_name = "dot1qBase"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1qvlanversionnumber', (YLeaf(YType.enumeration, 'dot1qVlanVersionNumber'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qBase.Dot1qVlanVersionNumber')])),
                ('dot1qmaxvlanid', (YLeaf(YType.int32, 'dot1qMaxVlanId'), ['int'])),
                ('dot1qmaxsupportedvlans', (YLeaf(YType.uint32, 'dot1qMaxSupportedVlans'), ['int'])),
                ('dot1qnumvlans', (YLeaf(YType.uint32, 'dot1qNumVlans'), ['int'])),
                ('dot1qgvrpstatus', (YLeaf(YType.enumeration, 'dot1qGvrpStatus'), [('ydk.models.cisco_ios_xe.P_BRIDGE_MIB', 'EnabledStatus', '')])),
            ])
            self.dot1qvlanversionnumber = None
            self.dot1qmaxvlanid = None
            self.dot1qmaxsupportedvlans = None
            self.dot1qnumvlans = None
            self.dot1qgvrpstatus = None
            self._segment_path = lambda: "dot1qBase"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qBase, ['dot1qvlanversionnumber', 'dot1qmaxvlanid', 'dot1qmaxsupportedvlans', 'dot1qnumvlans', 'dot1qgvrpstatus'], name, value)

        class Dot1qVlanVersionNumber(Enum):
            """
            Dot1qVlanVersionNumber (Enum Class)

            The version number of IEEE 802.1Q that this device

            supports.

            .. data:: version1 = 1

            """

            version1 = Enum.YLeaf(1, "version1")




    class Dot1qVlan(Entity):
        """
        
        
        .. attribute:: dot1qvlannumdeletes
        
        	The number of times a VLAN entry has been deleted from the dot1qVlanCurrentTable (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: dot1qnextfreelocalvlanindex
        
        	The next available value for dot1qVlanIndex of a local VLAN entry in dot1qVlanStaticTable.  This will report values >=4096 if a new Local VLAN may be created or else the value 0 if this is not possible.  A row creation operation in this table for an entry with a local VlanIndex value may fail if the current value of this object is not used as the index.  Even if the value read is used, there is no guarantee that it will still be the valid index when the create operation is attempted; another manager may have already got in during the intervening time interval. In this case, dot1qNextFreeLocalVlanIndex should be re\-read  and the creation re\-tried with the new value.  This value will automatically change when the current value is used to create a new row
        	**type**\: int
        
        	**range:** 0..None \| 4096..2147483647
        
        	**config**\: False
        
        .. attribute:: dot1qconstraintsetdefault
        
        	The identity of the constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: dot1qconstrainttypedefault
        
        	The type of constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The types are as defined for dot1qConstraintType.  The value of this object MUST be retained across  reinitializations of the management system
        	**type**\:  :py:class:`Dot1qConstraintTypeDefault <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlan.Dot1qConstraintTypeDefault>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qVlan, self).__init__()

            self.yang_name = "dot1qVlan"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1qvlannumdeletes', (YLeaf(YType.uint32, 'dot1qVlanNumDeletes'), ['int'])),
                ('dot1qnextfreelocalvlanindex', (YLeaf(YType.int32, 'dot1qNextFreeLocalVlanIndex'), ['int'])),
                ('dot1qconstraintsetdefault', (YLeaf(YType.int32, 'dot1qConstraintSetDefault'), ['int'])),
                ('dot1qconstrainttypedefault', (YLeaf(YType.enumeration, 'dot1qConstraintTypeDefault'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qVlan.Dot1qConstraintTypeDefault')])),
            ])
            self.dot1qvlannumdeletes = None
            self.dot1qnextfreelocalvlanindex = None
            self.dot1qconstraintsetdefault = None
            self.dot1qconstrainttypedefault = None
            self._segment_path = lambda: "dot1qVlan"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qVlan, ['dot1qvlannumdeletes', 'dot1qnextfreelocalvlanindex', 'dot1qconstraintsetdefault', 'dot1qconstrainttypedefault'], name, value)

        class Dot1qConstraintTypeDefault(Enum):
            """
            Dot1qConstraintTypeDefault (Enum Class)

            The type of constraint set to which a VLAN belongs, if

            there is not an explicit entry for that VLAN in

            dot1qLearningConstraintsTable.  The types are as defined

            for dot1qConstraintType.

            The value of this object MUST be retained across

            reinitializations of the management system.

            .. data:: independent = 1

            .. data:: shared = 2

            """

            independent = Enum.YLeaf(1, "independent")

            shared = Enum.YLeaf(2, "shared")




    class Dot1qFdbTable(Entity):
        """
        A table that contains configuration and control
        information for each Filtering Database currently
        operating on this device.  Entries in this table appear
        automatically when VLANs are assigned FDB IDs in the
        dot1qVlanCurrentTable.
        
        .. attribute:: dot1qfdbentry
        
        	Information about a specific Filtering Database
        	**type**\: list of  		 :py:class:`Dot1qFdbEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qFdbTable, self).__init__()

            self.yang_name = "dot1qFdbTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qFdbEntry", ("dot1qfdbentry", QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry))])
            self._leafs = OrderedDict()

            self.dot1qfdbentry = YList(self)
            self._segment_path = lambda: "dot1qFdbTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qFdbTable, [], name, value)


        class Dot1qFdbEntry(Entity):
            """
            Information about a specific Filtering Database.
            
            .. attribute:: dot1qfdbid  (key)
            
            	The identity of this Filtering Database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qfdbdynamiccount
            
            	The current number of dynamic entries in this Filtering Database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry, self).__init__()

                self.yang_name = "dot1qFdbEntry"
                self.yang_parent_name = "dot1qFdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qfdbid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qfdbid', (YLeaf(YType.uint32, 'dot1qFdbId'), ['int'])),
                    ('dot1qfdbdynamiccount', (YLeaf(YType.uint32, 'dot1qFdbDynamicCount'), ['int'])),
                ])
                self.dot1qfdbid = None
                self.dot1qfdbdynamiccount = None
                self._segment_path = lambda: "dot1qFdbEntry" + "[dot1qFdbId='" + str(self.dot1qfdbid) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qFdbTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry, ['dot1qfdbid', 'dot1qfdbdynamiccount'], name, value)




    class Dot1qTpFdbTable(Entity):
        """
        A table that contains information about unicast entries
        for which the device has forwarding and/or filtering
        information.  This information is used by the
        transparent bridging function in determining how to
        propagate a received frame.
        
        .. attribute:: dot1qtpfdbentry
        
        	Information about a specific unicast MAC address for which the device has some forwarding and/or filtering information
        	**type**\: list of  		 :py:class:`Dot1qTpFdbEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qTpFdbTable, self).__init__()

            self.yang_name = "dot1qTpFdbTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qTpFdbEntry", ("dot1qtpfdbentry", QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry))])
            self._leafs = OrderedDict()

            self.dot1qtpfdbentry = YList(self)
            self._segment_path = lambda: "dot1qTpFdbTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qTpFdbTable, [], name, value)


        class Dot1qTpFdbEntry(Entity):
            """
            Information about a specific unicast MAC address for
            which the device has some forwarding and/or filtering
            information.
            
            .. attribute:: dot1qfdbid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qfdbid <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpfdbaddress  (key)
            
            	A unicast MAC address for which the device has forwarding and/or filtering information
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: dot1qtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1qTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned but that the device does have some forwarding/filtering information about this address (e.g., in the dot1qStaticUnicastTable). Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1qTpFdbStatus is not learned(3)
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dot1qtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This may include         the case where some other MIB object (not the         corresponding instance of dot1qTpFdbPort, nor an         entry in the dot1qStaticUnicastTable) is being         used to determine if and how frames addressed to         the value of the corresponding instance of         dot1qTpFdbAddress are being forwarded.     invalid(2) \- this entry is no longer valid (e.g., it          was learned but has since aged out), but has not         yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1qTpFdbPort was learned and is being used.     self(4) \- the value of the corresponding instance of         dot1qTpFdbAddress represents one of the device's         addresses.  The corresponding instance of         dot1qTpFdbPort indicates which of the device's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1qTpFdbAddress is also the value of an         existing instance of dot1qStaticAddress
            	**type**\:  :py:class:`Dot1qTpFdbStatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry, self).__init__()

                self.yang_name = "dot1qTpFdbEntry"
                self.yang_parent_name = "dot1qTpFdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qfdbid','dot1qtpfdbaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qfdbid', (YLeaf(YType.str, 'dot1qFdbId'), ['int'])),
                    ('dot1qtpfdbaddress', (YLeaf(YType.str, 'dot1qTpFdbAddress'), ['str'])),
                    ('dot1qtpfdbport', (YLeaf(YType.int32, 'dot1qTpFdbPort'), ['int'])),
                    ('dot1qtpfdbstatus', (YLeaf(YType.enumeration, 'dot1qTpFdbStatus'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus')])),
                ])
                self.dot1qfdbid = None
                self.dot1qtpfdbaddress = None
                self.dot1qtpfdbport = None
                self.dot1qtpfdbstatus = None
                self._segment_path = lambda: "dot1qTpFdbEntry" + "[dot1qFdbId='" + str(self.dot1qfdbid) + "']" + "[dot1qTpFdbAddress='" + str(self.dot1qtpfdbaddress) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qTpFdbTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry, ['dot1qfdbid', 'dot1qtpfdbaddress', 'dot1qtpfdbport', 'dot1qtpfdbstatus'], name, value)

            class Dot1qTpFdbStatus(Enum):
                """
                Dot1qTpFdbStatus (Enum Class)

                The status of this entry.  The meanings of the values

                are\:

                    other(1) \- none of the following.  This may include

                        the case where some other MIB object (not the

                        corresponding instance of dot1qTpFdbPort, nor an

                        entry in the dot1qStaticUnicastTable) is being

                        used to determine if and how frames addressed to

                        the value of the corresponding instance of

                        dot1qTpFdbAddress are being forwarded.

                    invalid(2) \- this entry is no longer valid (e.g., it

                        was learned but has since aged out), but has not

                        yet been flushed from the table.

                    learned(3) \- the value of the corresponding instance

                        of dot1qTpFdbPort was learned and is being used.

                    self(4) \- the value of the corresponding instance of

                        dot1qTpFdbAddress represents one of the device's

                        addresses.  The corresponding instance of

                        dot1qTpFdbPort indicates which of the device's

                        ports has this address.

                    mgmt(5) \- the value of the corresponding instance of

                        dot1qTpFdbAddress is also the value of an

                        existing instance of dot1qStaticAddress.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: learned = 3

                .. data:: self = 4

                .. data:: mgmt = 5

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                learned = Enum.YLeaf(3, "learned")

                self = Enum.YLeaf(4, "self")

                mgmt = Enum.YLeaf(5, "mgmt")





    class Dot1qTpGroupTable(Entity):
        """
        A table containing filtering information for VLANs
        configured into the bridge by (local or network)
        management, or learned dynamically, specifying the set of
        ports to which frames received on a VLAN for this FDB
        and containing a specific Group destination address are
        allowed to be forwarded.
        
        .. attribute:: dot1qtpgroupentry
        
        	Filtering information configured into the bridge by management, or learned dynamically, specifying the set of ports to which frames received on a VLAN and containing a specific Group destination address are allowed to be forwarded.  The subset of these ports learned dynamically is also provided
        	**type**\: list of  		 :py:class:`Dot1qTpGroupEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qTpGroupTable, self).__init__()

            self.yang_name = "dot1qTpGroupTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qTpGroupEntry", ("dot1qtpgroupentry", QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry))])
            self._leafs = OrderedDict()

            self.dot1qtpgroupentry = YList(self)
            self._segment_path = lambda: "dot1qTpGroupTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qTpGroupTable, [], name, value)


        class Dot1qTpGroupEntry(Entity):
            """
            Filtering information configured into the bridge by
            management, or learned dynamically, specifying the set of
            ports to which frames received on a VLAN and containing
            a specific Group destination address are allowed to be
            forwarded.  The subset of these ports learned dynamically
            is also provided.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpgroupaddress  (key)
            
            	The destination Group MAC address in a frame to which this entry's filtering information applies
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: dot1qtpgroupegressports
            
            	The complete set of ports, in this VLAN, to which frames destined for this Group MAC address are currently being explicitly forwarded.  This does not include ports for which this address is only implicitly forwarded, in the dot1qForwardAllPorts list
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qtpgrouplearnt
            
            	The subset of ports in dot1qTpGroupEgressPorts that were learned by GMRP or some other dynamic mechanism, in this Filtering database
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry, self).__init__()

                self.yang_name = "dot1qTpGroupEntry"
                self.yang_parent_name = "dot1qTpGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex','dot1qtpgroupaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qtpgroupaddress', (YLeaf(YType.str, 'dot1qTpGroupAddress'), ['str'])),
                    ('dot1qtpgroupegressports', (YLeaf(YType.str, 'dot1qTpGroupEgressPorts'), ['str'])),
                    ('dot1qtpgrouplearnt', (YLeaf(YType.str, 'dot1qTpGroupLearnt'), ['str'])),
                ])
                self.dot1qvlanindex = None
                self.dot1qtpgroupaddress = None
                self.dot1qtpgroupegressports = None
                self.dot1qtpgrouplearnt = None
                self._segment_path = lambda: "dot1qTpGroupEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']" + "[dot1qTpGroupAddress='" + str(self.dot1qtpgroupaddress) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qTpGroupTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry, ['dot1qvlanindex', 'dot1qtpgroupaddress', 'dot1qtpgroupegressports', 'dot1qtpgrouplearnt'], name, value)




    class Dot1qForwardAllTable(Entity):
        """
        A table containing forwarding information for each
        
        VLAN, specifying the set of ports to which forwarding of
        all multicasts applies, configured statically by
        management or dynamically by GMRP.  An entry appears in
        this table for all VLANs that are currently
        instantiated.
        
        .. attribute:: dot1qforwardallentry
        
        	Forwarding information for a VLAN, specifying the set of ports to which all multicasts should be forwarded, configured statically by management or dynamically by GMRP
        	**type**\: list of  		 :py:class:`Dot1qForwardAllEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qForwardAllTable, self).__init__()

            self.yang_name = "dot1qForwardAllTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qForwardAllEntry", ("dot1qforwardallentry", QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry))])
            self._leafs = OrderedDict()

            self.dot1qforwardallentry = YList(self)
            self._segment_path = lambda: "dot1qForwardAllTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qForwardAllTable, [], name, value)


        class Dot1qForwardAllEntry(Entity):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts should be forwarded,
            configured statically by management or dynamically by
            GMRP.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qforwardallports
            
            	The complete set of ports in this VLAN to which all multicast group\-addressed frames are to be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qforwardallstaticports
            
            	The set of ports configured by management in this VLAN to which all multicast group\-addressed frames are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardAllPorts.  This value will be restored after the device is reset.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllForbiddenPorts.  The default value is a string of ones of appropriate length, to indicate the standard behaviour of using basic filtering services, i.e., forward all multicasts to all ports.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qforwardallforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward All Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry, self).__init__()

                self.yang_name = "dot1qForwardAllEntry"
                self.yang_parent_name = "dot1qForwardAllTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qforwardallports', (YLeaf(YType.str, 'dot1qForwardAllPorts'), ['str'])),
                    ('dot1qforwardallstaticports', (YLeaf(YType.str, 'dot1qForwardAllStaticPorts'), ['str'])),
                    ('dot1qforwardallforbiddenports', (YLeaf(YType.str, 'dot1qForwardAllForbiddenPorts'), ['str'])),
                ])
                self.dot1qvlanindex = None
                self.dot1qforwardallports = None
                self.dot1qforwardallstaticports = None
                self.dot1qforwardallforbiddenports = None
                self._segment_path = lambda: "dot1qForwardAllEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qForwardAllTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry, ['dot1qvlanindex', 'dot1qforwardallports', 'dot1qforwardallstaticports', 'dot1qforwardallforbiddenports'], name, value)




    class Dot1qForwardUnregisteredTable(Entity):
        """
        A table containing forwarding information for each
        VLAN, specifying the set of ports to which forwarding of
        multicast group\-addressed frames for which no
        more specific forwarding information applies.  This is
        configured statically by management and determined
        dynamically by GMRP.  An entry appears in this table for
        all VLANs that are currently instantiated.
        
        .. attribute:: dot1qforwardunregisteredentry
        
        	Forwarding information for a VLAN, specifying the set of ports to which all multicasts for which there is no more specific forwarding information shall be forwarded. This is configured statically by management or dynamically by GMRP
        	**type**\: list of  		 :py:class:`Dot1qForwardUnregisteredEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qForwardUnregisteredTable, self).__init__()

            self.yang_name = "dot1qForwardUnregisteredTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qForwardUnregisteredEntry", ("dot1qforwardunregisteredentry", QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry))])
            self._leafs = OrderedDict()

            self.dot1qforwardunregisteredentry = YList(self)
            self._segment_path = lambda: "dot1qForwardUnregisteredTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qForwardUnregisteredTable, [], name, value)


        class Dot1qForwardUnregisteredEntry(Entity):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts for which there is no
            more specific forwarding information shall be forwarded.
            This is configured statically by management or
            dynamically by GMRP.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qforwardunregisteredports
            
            	The complete set of ports in this VLAN to which multicast group\-addressed frames for which there is no more specific forwarding information will be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qforwardunregisteredstaticports
            
            	The set of ports configured by management, in this VLAN, to which multicast group\-addressed frames for which there is no more specific forwarding information  are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardUnregisteredPorts.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredForbiddenPorts.  The default value is a string of zeros of appropriate length, although this has no effect with the default value of dot1qForwardAllStaticPorts.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qforwardunregisteredforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward Unregistered Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry, self).__init__()

                self.yang_name = "dot1qForwardUnregisteredEntry"
                self.yang_parent_name = "dot1qForwardUnregisteredTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qforwardunregisteredports', (YLeaf(YType.str, 'dot1qForwardUnregisteredPorts'), ['str'])),
                    ('dot1qforwardunregisteredstaticports', (YLeaf(YType.str, 'dot1qForwardUnregisteredStaticPorts'), ['str'])),
                    ('dot1qforwardunregisteredforbiddenports', (YLeaf(YType.str, 'dot1qForwardUnregisteredForbiddenPorts'), ['str'])),
                ])
                self.dot1qvlanindex = None
                self.dot1qforwardunregisteredports = None
                self.dot1qforwardunregisteredstaticports = None
                self.dot1qforwardunregisteredforbiddenports = None
                self._segment_path = lambda: "dot1qForwardUnregisteredEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qForwardUnregisteredTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry, ['dot1qvlanindex', 'dot1qforwardunregisteredports', 'dot1qforwardunregisteredstaticports', 'dot1qforwardunregisteredforbiddenports'], name, value)




    class Dot1qStaticUnicastTable(Entity):
        """
        A table containing filtering information for Unicast
        MAC addresses for each Filtering Database, configured
        into the device by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific unicast
        destination addresses are allowed to be forwarded.  A
        value of zero in this table (as the port number from
        
        which frames with a specific destination address are
        received) is used to specify all ports for which there
        is no specific entry in this table for that particular
        destination address.  Entries are valid for unicast
        addresses only.
        
        .. attribute:: dot1qstaticunicastentry
        
        	Filtering information configured into the device by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific unicast destination address are allowed to be forwarded
        	**type**\: list of  		 :py:class:`Dot1qStaticUnicastEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qStaticUnicastTable, self).__init__()

            self.yang_name = "dot1qStaticUnicastTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qStaticUnicastEntry", ("dot1qstaticunicastentry", QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry))])
            self._leafs = OrderedDict()

            self.dot1qstaticunicastentry = YList(self)
            self._segment_path = lambda: "dot1qStaticUnicastTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qStaticUnicastTable, [], name, value)


        class Dot1qStaticUnicastEntry(Entity):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific unicast destination address are
            allowed to be forwarded.
            
            .. attribute:: dot1qfdbid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qfdbid <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qstaticunicastaddress  (key)
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a unicast address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: dot1qstaticunicastreceiveport  (key)
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dot1qstaticunicastallowedtogoto
            
            	The set of ports for which a frame with a specific unicast address will be flooded in the event that it has not been learned.  It also specifies the set of ports on which a specific unicast address may be dynamically learned.  The dot1qTpFdbTable will have an equivalent entry with a dot1qTpFdbPort value of '0' until this address has been learned, at which point it will be updated with the port the address has been seen on.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qstaticunicaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but      the conditions under which it will remain     so differ from the following values. invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  :py:class:`Dot1qStaticUnicastStatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry, self).__init__()

                self.yang_name = "dot1qStaticUnicastEntry"
                self.yang_parent_name = "dot1qStaticUnicastTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qfdbid','dot1qstaticunicastaddress','dot1qstaticunicastreceiveport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qfdbid', (YLeaf(YType.str, 'dot1qFdbId'), ['int'])),
                    ('dot1qstaticunicastaddress', (YLeaf(YType.str, 'dot1qStaticUnicastAddress'), ['str'])),
                    ('dot1qstaticunicastreceiveport', (YLeaf(YType.int32, 'dot1qStaticUnicastReceivePort'), ['int'])),
                    ('dot1qstaticunicastallowedtogoto', (YLeaf(YType.str, 'dot1qStaticUnicastAllowedToGoTo'), ['str'])),
                    ('dot1qstaticunicaststatus', (YLeaf(YType.enumeration, 'dot1qStaticUnicastStatus'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus')])),
                ])
                self.dot1qfdbid = None
                self.dot1qstaticunicastaddress = None
                self.dot1qstaticunicastreceiveport = None
                self.dot1qstaticunicastallowedtogoto = None
                self.dot1qstaticunicaststatus = None
                self._segment_path = lambda: "dot1qStaticUnicastEntry" + "[dot1qFdbId='" + str(self.dot1qfdbid) + "']" + "[dot1qStaticUnicastAddress='" + str(self.dot1qstaticunicastaddress) + "']" + "[dot1qStaticUnicastReceivePort='" + str(self.dot1qstaticunicastreceiveport) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qStaticUnicastTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry, ['dot1qfdbid', 'dot1qstaticunicastaddress', 'dot1qstaticunicastreceiveport', 'dot1qstaticunicastallowedtogoto', 'dot1qstaticunicaststatus'], name, value)

            class Dot1qStaticUnicastStatus(Enum):
                """
                Dot1qStaticUnicastStatus (Enum Class)

                This object indicates the status of this entry.

                other(1) \- this entry is currently in use, but

                    the conditions under which it will remain

                    so differ from the following values.

                invalid(2) \- writing this value to the object

                    removes the corresponding entry.

                permanent(3) \- this entry is currently in use

                    and will remain so after the next reset of

                    the bridge.

                deleteOnReset(4) \- this entry is currently in

                    use and will remain so until the next

                    reset of the bridge.

                deleteOnTimeout(5) \- this entry is currently in

                    use and will remain so until it is aged out.

                The value of this object MUST be retained across

                reinitializations of the management system.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: permanent = 3

                .. data:: deleteOnReset = 4

                .. data:: deleteOnTimeout = 5

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                permanent = Enum.YLeaf(3, "permanent")

                deleteOnReset = Enum.YLeaf(4, "deleteOnReset")

                deleteOnTimeout = Enum.YLeaf(5, "deleteOnTimeout")





    class Dot1qStaticMulticastTable(Entity):
        """
        A table containing filtering information for Multicast
        and Broadcast MAC addresses for each VLAN, configured
        into the device by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific Multicast
        and Broadcast destination addresses are allowed to be
        forwarded.  A value of zero in this table (as the port
        number from which frames with a specific destination
        address are received) is used to specify all ports for
        which there is no specific entry in this table for that
        particular destination address.  Entries are valid for
        Multicast and Broadcast addresses only.
        
        .. attribute:: dot1qstaticmulticastentry
        
        	Filtering information configured into the device by (local or network) management specifying the set of ports to which frames received from this specific port  for this VLAN and containing this Multicast or Broadcast destination address are allowed to be forwarded
        	**type**\: list of  		 :py:class:`Dot1qStaticMulticastEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qStaticMulticastTable, self).__init__()

            self.yang_name = "dot1qStaticMulticastTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qStaticMulticastEntry", ("dot1qstaticmulticastentry", QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry))])
            self._leafs = OrderedDict()

            self.dot1qstaticmulticastentry = YList(self)
            self._segment_path = lambda: "dot1qStaticMulticastTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qStaticMulticastTable, [], name, value)


        class Dot1qStaticMulticastEntry(Entity):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from this specific port
            
            for this VLAN and containing this Multicast or Broadcast
            destination address are allowed to be forwarded.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qstaticmulticastaddress  (key)
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a Multicast or Broadcast address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: dot1qstaticmulticastreceiveport  (key)
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dot1qstaticmulticaststaticegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastForbiddenEgressPorts. The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qstaticmulticastforbiddenegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must not be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastStaticEgressPorts. The default value of this object is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qstaticmulticaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but     the conditions under which it will remain     so differ from the following values.  invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  :py:class:`Dot1qStaticMulticastStatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry, self).__init__()

                self.yang_name = "dot1qStaticMulticastEntry"
                self.yang_parent_name = "dot1qStaticMulticastTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex','dot1qstaticmulticastaddress','dot1qstaticmulticastreceiveport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qstaticmulticastaddress', (YLeaf(YType.str, 'dot1qStaticMulticastAddress'), ['str'])),
                    ('dot1qstaticmulticastreceiveport', (YLeaf(YType.int32, 'dot1qStaticMulticastReceivePort'), ['int'])),
                    ('dot1qstaticmulticaststaticegressports', (YLeaf(YType.str, 'dot1qStaticMulticastStaticEgressPorts'), ['str'])),
                    ('dot1qstaticmulticastforbiddenegressports', (YLeaf(YType.str, 'dot1qStaticMulticastForbiddenEgressPorts'), ['str'])),
                    ('dot1qstaticmulticaststatus', (YLeaf(YType.enumeration, 'dot1qStaticMulticastStatus'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus')])),
                ])
                self.dot1qvlanindex = None
                self.dot1qstaticmulticastaddress = None
                self.dot1qstaticmulticastreceiveport = None
                self.dot1qstaticmulticaststaticegressports = None
                self.dot1qstaticmulticastforbiddenegressports = None
                self.dot1qstaticmulticaststatus = None
                self._segment_path = lambda: "dot1qStaticMulticastEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']" + "[dot1qStaticMulticastAddress='" + str(self.dot1qstaticmulticastaddress) + "']" + "[dot1qStaticMulticastReceivePort='" + str(self.dot1qstaticmulticastreceiveport) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qStaticMulticastTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry, ['dot1qvlanindex', 'dot1qstaticmulticastaddress', 'dot1qstaticmulticastreceiveport', 'dot1qstaticmulticaststaticegressports', 'dot1qstaticmulticastforbiddenegressports', 'dot1qstaticmulticaststatus'], name, value)

            class Dot1qStaticMulticastStatus(Enum):
                """
                Dot1qStaticMulticastStatus (Enum Class)

                This object indicates the status of this entry.

                other(1) \- this entry is currently in use, but

                    the conditions under which it will remain

                    so differ from the following values.

                invalid(2) \- writing this value to the object

                    removes the corresponding entry.

                permanent(3) \- this entry is currently in use

                    and will remain so after the next reset of

                    the bridge.

                deleteOnReset(4) \- this entry is currently in

                    use and will remain so until the next

                    reset of the bridge.

                deleteOnTimeout(5) \- this entry is currently in

                    use and will remain so until it is aged out.

                The value of this object MUST be retained across

                reinitializations of the management system.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: permanent = 3

                .. data:: deleteOnReset = 4

                .. data:: deleteOnTimeout = 5

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                permanent = Enum.YLeaf(3, "permanent")

                deleteOnReset = Enum.YLeaf(4, "deleteOnReset")

                deleteOnTimeout = Enum.YLeaf(5, "deleteOnTimeout")





    class Dot1qVlanCurrentTable(Entity):
        """
        A table containing current configuration information
        for each VLAN currently configured into the device by
        (local or network) management, or dynamically created
        as a result of GVRP requests received.
        
        .. attribute:: dot1qvlancurrententry
        
        	Information for a VLAN configured into the device by  (local or network) management, or dynamically created as a result of GVRP requests received
        	**type**\: list of  		 :py:class:`Dot1qVlanCurrentEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qVlanCurrentTable, self).__init__()

            self.yang_name = "dot1qVlanCurrentTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qVlanCurrentEntry", ("dot1qvlancurrententry", QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry))])
            self._leafs = OrderedDict()

            self.dot1qvlancurrententry = YList(self)
            self._segment_path = lambda: "dot1qVlanCurrentTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qVlanCurrentTable, [], name, value)


        class Dot1qVlanCurrentEntry(Entity):
            """
            Information for a VLAN configured into the device by
            
            (local or network) management, or dynamically created
            as a result of GVRP requests received.
            
            .. attribute:: dot1qvlantimemark  (key)
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qvlanindex  (key)
            
            	The VLAN\-ID or other identifier referring to this VLAN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qvlanfdbid
            
            	The Filtering Database used by this VLAN.  This is one of the dot1qFdbId values in the dot1qFdbTable.  This value is allocated automatically by the device whenever  the VLAN is created\: either dynamically by GVRP, or by management, in dot1qVlanStaticTable.  Allocation of this value follows the learning constraints defined for this VLAN in dot1qLearningConstraintsTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qvlancurrentegressports
            
            	The set of ports that are transmitting traffic for this VLAN as either tagged or untagged frames
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qvlancurrentuntaggedports
            
            	The set of ports that are transmitting traffic for this VLAN as untagged frames
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qvlanstatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but the     conditions under which it will remain so differ     from the following values. permanent(2) \- this entry, corresponding to an entry     in dot1qVlanStaticTable, is currently in use and     will remain so after the next reset of the     device.  The port lists for this entry include     ports from the equivalent dot1qVlanStaticTable     entry and ports learned dynamically. dynamicGvrp(3) \- this entry is currently in use      and will remain so until removed by GVRP.  There     is no static entry for this VLAN, and it will be     removed when the last port leaves the VLAN
            	**type**\:  :py:class:`Dot1qVlanStatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus>`
            
            	**config**\: False
            
            .. attribute:: dot1qvlancreationtime
            
            	The value of sysUpTime when this VLAN was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry, self).__init__()

                self.yang_name = "dot1qVlanCurrentEntry"
                self.yang_parent_name = "dot1qVlanCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlantimemark','dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlantimemark', (YLeaf(YType.uint32, 'dot1qVlanTimeMark'), ['int'])),
                    ('dot1qvlanindex', (YLeaf(YType.uint32, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qvlanfdbid', (YLeaf(YType.uint32, 'dot1qVlanFdbId'), ['int'])),
                    ('dot1qvlancurrentegressports', (YLeaf(YType.str, 'dot1qVlanCurrentEgressPorts'), ['str'])),
                    ('dot1qvlancurrentuntaggedports', (YLeaf(YType.str, 'dot1qVlanCurrentUntaggedPorts'), ['str'])),
                    ('dot1qvlanstatus', (YLeaf(YType.enumeration, 'dot1qVlanStatus'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus')])),
                    ('dot1qvlancreationtime', (YLeaf(YType.uint32, 'dot1qVlanCreationTime'), ['int'])),
                ])
                self.dot1qvlantimemark = None
                self.dot1qvlanindex = None
                self.dot1qvlanfdbid = None
                self.dot1qvlancurrentegressports = None
                self.dot1qvlancurrentuntaggedports = None
                self.dot1qvlanstatus = None
                self.dot1qvlancreationtime = None
                self._segment_path = lambda: "dot1qVlanCurrentEntry" + "[dot1qVlanTimeMark='" + str(self.dot1qvlantimemark) + "']" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qVlanCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry, ['dot1qvlantimemark', 'dot1qvlanindex', 'dot1qvlanfdbid', 'dot1qvlancurrentegressports', 'dot1qvlancurrentuntaggedports', 'dot1qvlanstatus', 'dot1qvlancreationtime'], name, value)

            class Dot1qVlanStatus(Enum):
                """
                Dot1qVlanStatus (Enum Class)

                This object indicates the status of this entry.

                other(1) \- this entry is currently in use, but the

                    conditions under which it will remain so differ

                    from the following values.

                permanent(2) \- this entry, corresponding to an entry

                    in dot1qVlanStaticTable, is currently in use and

                    will remain so after the next reset of the

                    device.  The port lists for this entry include

                    ports from the equivalent dot1qVlanStaticTable

                    entry and ports learned dynamically.

                dynamicGvrp(3) \- this entry is currently in use

                    and will remain so until removed by GVRP.  There

                    is no static entry for this VLAN, and it will be

                    removed when the last port leaves the VLAN.

                .. data:: other = 1

                .. data:: permanent = 2

                .. data:: dynamicGvrp = 3

                """

                other = Enum.YLeaf(1, "other")

                permanent = Enum.YLeaf(2, "permanent")

                dynamicGvrp = Enum.YLeaf(3, "dynamicGvrp")





    class Dot1qVlanStaticTable(Entity):
        """
        A table containing static configuration information for
        each VLAN configured into the device by (local or
        network) management.  All entries are permanent and will
        be restored after the device is reset.
        
        .. attribute:: dot1qvlanstaticentry
        
        	Static information for a VLAN configured into the device by (local or network) management
        	**type**\: list of  		 :py:class:`Dot1qVlanStaticEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qVlanStaticTable, self).__init__()

            self.yang_name = "dot1qVlanStaticTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qVlanStaticEntry", ("dot1qvlanstaticentry", QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry))])
            self._leafs = OrderedDict()

            self.dot1qvlanstaticentry = YList(self)
            self._segment_path = lambda: "dot1qVlanStaticTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qVlanStaticTable, [], name, value)


        class Dot1qVlanStaticEntry(Entity):
            """
            Static information for a VLAN configured into the
            device by (local or network) management.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qvlanstaticname
            
            	An administratively assigned string, which may be used to identify the VLAN
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: dot1qvlanstaticegressports
            
            	The set of ports that are permanently assigned to the egress list for this VLAN by management.  Changes to a bit in this object affect the per\-port, per\-VLAN Registrar control for Registration Fixed for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanForbiddenEgressPorts.  The default value of this object is a string of zeros of appropriate length, indicating not fixed
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qvlanforbiddenegressports
            
            	The set of ports that are prohibited by management from being included in the egress list for this VLAN. Changes to this object that cause a port to be included or excluded affect the per\-port, per\-VLAN Registrar control for Registration Forbidden for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanStaticEgressPorts.  The default value of this object is a string of zeros of appropriate length, excluding all ports from the forbidden set
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qvlanstaticuntaggedports
            
            	The set of ports that should transmit egress packets for this VLAN as untagged.  The default value of this object for the default VLAN (dot1qVlanIndex = 1) is a string of appropriate length including all ports.  There is no specified default for other VLANs.  If a device agent cannot support the set of ports being set, then it will reject the set operation with an error.  For example, a manager might attempt to set more than one VLAN to be untagged on egress where the device does not support this IEEE 802.1Q option
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: dot1qvlanstaticrowstatus
            
            	This object indicates the status of this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry, self).__init__()

                self.yang_name = "dot1qVlanStaticEntry"
                self.yang_parent_name = "dot1qVlanStaticTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qvlanstaticname', (YLeaf(YType.str, 'dot1qVlanStaticName'), ['str'])),
                    ('dot1qvlanstaticegressports', (YLeaf(YType.str, 'dot1qVlanStaticEgressPorts'), ['str'])),
                    ('dot1qvlanforbiddenegressports', (YLeaf(YType.str, 'dot1qVlanForbiddenEgressPorts'), ['str'])),
                    ('dot1qvlanstaticuntaggedports', (YLeaf(YType.str, 'dot1qVlanStaticUntaggedPorts'), ['str'])),
                    ('dot1qvlanstaticrowstatus', (YLeaf(YType.enumeration, 'dot1qVlanStaticRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.dot1qvlanindex = None
                self.dot1qvlanstaticname = None
                self.dot1qvlanstaticegressports = None
                self.dot1qvlanforbiddenegressports = None
                self.dot1qvlanstaticuntaggedports = None
                self.dot1qvlanstaticrowstatus = None
                self._segment_path = lambda: "dot1qVlanStaticEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qVlanStaticTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry, ['dot1qvlanindex', 'dot1qvlanstaticname', 'dot1qvlanstaticegressports', 'dot1qvlanforbiddenegressports', 'dot1qvlanstaticuntaggedports', 'dot1qvlanstaticrowstatus'], name, value)




    class Dot1qPortVlanStatisticsTable(Entity):
        """
        A table containing per\-port, per\-VLAN statistics for
        traffic received.  Separate objects are provided for both the
        most\-significant and least\-significant bits of statistics
        counters for ports that are associated with this transparent
        bridge.  The most\-significant bit objects are only required on
        high\-capacity interfaces, as defined in the conformance clauses
        for these objects.  This mechanism is provided as a way to read
        64\-bit counters for agents that support only SNMPv1.
        
        Note that the reporting of most\-significant and least\-
        significant counter bits separately runs the risk of missing
        an overflow of the lower bits in the interval between sampling.
        The manager must be aware of this possibility, even within the
        same varbindlist, when interpreting the results of a request or
        
        asynchronous notification.
        
        .. attribute:: dot1qportvlanstatisticsentry
        
        	Traffic statistics for a VLAN on an interface
        	**type**\: list of  		 :py:class:`Dot1qPortVlanStatisticsEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qPortVlanStatisticsTable, self).__init__()

            self.yang_name = "dot1qPortVlanStatisticsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qPortVlanStatisticsEntry", ("dot1qportvlanstatisticsentry", QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry))])
            self._leafs = OrderedDict()

            self.dot1qportvlanstatisticsentry = YList(self)
            self._segment_path = lambda: "dot1qPortVlanStatisticsTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qPortVlanStatisticsTable, [], name, value)


        class Dot1qPortVlanStatisticsEntry(Entity):
            """
            Traffic statistics for a VLAN on an interface.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1dBasePortTable.Dot1dBasePortEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportinoverflowframes
            
            	The number of times the associated dot1qTpVlanPortInFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportoutoverflowframes
            
            	The number of times the associated dot1qTpVlanPortOutFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanportinoverflowdiscards
            
            	The number of times the associated dot1qTpVlanPortInDiscards counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry, self).__init__()

                self.yang_name = "dot1qPortVlanStatisticsEntry"
                self.yang_parent_name = "dot1qPortVlanStatisticsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', (YLeaf(YType.str, 'dot1dBasePort'), ['int'])),
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qtpvlanportinframes', (YLeaf(YType.uint32, 'dot1qTpVlanPortInFrames'), ['int'])),
                    ('dot1qtpvlanportoutframes', (YLeaf(YType.uint32, 'dot1qTpVlanPortOutFrames'), ['int'])),
                    ('dot1qtpvlanportindiscards', (YLeaf(YType.uint32, 'dot1qTpVlanPortInDiscards'), ['int'])),
                    ('dot1qtpvlanportinoverflowframes', (YLeaf(YType.uint32, 'dot1qTpVlanPortInOverflowFrames'), ['int'])),
                    ('dot1qtpvlanportoutoverflowframes', (YLeaf(YType.uint32, 'dot1qTpVlanPortOutOverflowFrames'), ['int'])),
                    ('dot1qtpvlanportinoverflowdiscards', (YLeaf(YType.uint32, 'dot1qTpVlanPortInOverflowDiscards'), ['int'])),
                ])
                self.dot1dbaseport = None
                self.dot1qvlanindex = None
                self.dot1qtpvlanportinframes = None
                self.dot1qtpvlanportoutframes = None
                self.dot1qtpvlanportindiscards = None
                self.dot1qtpvlanportinoverflowframes = None
                self.dot1qtpvlanportoutoverflowframes = None
                self.dot1qtpvlanportinoverflowdiscards = None
                self._segment_path = lambda: "dot1qPortVlanStatisticsEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qPortVlanStatisticsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry, ['dot1dbaseport', 'dot1qvlanindex', 'dot1qtpvlanportinframes', 'dot1qtpvlanportoutframes', 'dot1qtpvlanportindiscards', 'dot1qtpvlanportinoverflowframes', 'dot1qtpvlanportoutoverflowframes', 'dot1qtpvlanportinoverflowdiscards'], name, value)




    class Dot1qPortVlanHCStatisticsTable(Entity):
        """
        A table containing per\-port, per\-VLAN statistics for
        traffic on high\-capacity interfaces.
        
        .. attribute:: dot1qportvlanhcstatisticsentry
        
        	Traffic statistics for a VLAN on a high\-capacity interface
        	**type**\: list of  		 :py:class:`Dot1qPortVlanHCStatisticsEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable, self).__init__()

            self.yang_name = "dot1qPortVlanHCStatisticsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qPortVlanHCStatisticsEntry", ("dot1qportvlanhcstatisticsentry", QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry))])
            self._leafs = OrderedDict()

            self.dot1qportvlanhcstatisticsentry = YList(self)
            self._segment_path = lambda: "dot1qPortVlanHCStatisticsTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable, [], name, value)


        class Dot1qPortVlanHCStatisticsEntry(Entity):
            """
            Traffic statistics for a VLAN on a high\-capacity
            interface.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1dBasePortTable.Dot1dBasePortEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanporthcinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a  protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanporthcoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot1qtpvlanporthcindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry, self).__init__()

                self.yang_name = "dot1qPortVlanHCStatisticsEntry"
                self.yang_parent_name = "dot1qPortVlanHCStatisticsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1qvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', (YLeaf(YType.str, 'dot1dBasePort'), ['int'])),
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qtpvlanporthcinframes', (YLeaf(YType.uint64, 'dot1qTpVlanPortHCInFrames'), ['int'])),
                    ('dot1qtpvlanporthcoutframes', (YLeaf(YType.uint64, 'dot1qTpVlanPortHCOutFrames'), ['int'])),
                    ('dot1qtpvlanporthcindiscards', (YLeaf(YType.uint64, 'dot1qTpVlanPortHCInDiscards'), ['int'])),
                ])
                self.dot1dbaseport = None
                self.dot1qvlanindex = None
                self.dot1qtpvlanporthcinframes = None
                self.dot1qtpvlanporthcoutframes = None
                self.dot1qtpvlanporthcindiscards = None
                self._segment_path = lambda: "dot1qPortVlanHCStatisticsEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qPortVlanHCStatisticsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry, ['dot1dbaseport', 'dot1qvlanindex', 'dot1qtpvlanporthcinframes', 'dot1qtpvlanporthcoutframes', 'dot1qtpvlanporthcindiscards'], name, value)




    class Dot1qLearningConstraintsTable(Entity):
        """
        A table containing learning constraints for sets of
        Shared and Independent VLANs.
        
        .. attribute:: dot1qlearningconstraintsentry
        
        	A learning constraint defined for a VLAN
        	**type**\: list of  		 :py:class:`Dot1qLearningConstraintsEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1qLearningConstraintsTable, self).__init__()

            self.yang_name = "dot1qLearningConstraintsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1qLearningConstraintsEntry", ("dot1qlearningconstraintsentry", QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry))])
            self._leafs = OrderedDict()

            self.dot1qlearningconstraintsentry = YList(self)
            self._segment_path = lambda: "dot1qLearningConstraintsTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1qLearningConstraintsTable, [], name, value)


        class Dot1qLearningConstraintsEntry(Entity):
            """
            A learning constraint defined for a VLAN.
            
            .. attribute:: dot1qconstraintvlan  (key)
            
            	The index of the row in dot1qVlanCurrentTable for the VLAN constrained by this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot1qconstraintset  (key)
            
            	The identity of the constraint set to which dot1qConstraintVlan belongs.  These values may be chosen by the management station
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dot1qconstrainttype
            
            	The type of constraint this entry defines. independent(1) \- the VLAN, dot1qConstraintVlan,     uses a filtering database independent from all     other VLANs in the same set, defined by     dot1qConstraintSet. shared(2) \- the VLAN, dot1qConstraintVlan, shares     the same filtering database as all other VLANs     in the same set, defined by dot1qConstraintSet
            	**type**\:  :py:class:`Dot1qConstraintType <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType>`
            
            	**config**\: False
            
            .. attribute:: dot1qconstraintstatus
            
            	The status of this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry, self).__init__()

                self.yang_name = "dot1qLearningConstraintsEntry"
                self.yang_parent_name = "dot1qLearningConstraintsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qconstraintvlan','dot1qconstraintset']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qconstraintvlan', (YLeaf(YType.uint32, 'dot1qConstraintVlan'), ['int'])),
                    ('dot1qconstraintset', (YLeaf(YType.int32, 'dot1qConstraintSet'), ['int'])),
                    ('dot1qconstrainttype', (YLeaf(YType.enumeration, 'dot1qConstraintType'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType')])),
                    ('dot1qconstraintstatus', (YLeaf(YType.enumeration, 'dot1qConstraintStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.dot1qconstraintvlan = None
                self.dot1qconstraintset = None
                self.dot1qconstrainttype = None
                self.dot1qconstraintstatus = None
                self._segment_path = lambda: "dot1qLearningConstraintsEntry" + "[dot1qConstraintVlan='" + str(self.dot1qconstraintvlan) + "']" + "[dot1qConstraintSet='" + str(self.dot1qconstraintset) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qLearningConstraintsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry, ['dot1qconstraintvlan', 'dot1qconstraintset', 'dot1qconstrainttype', 'dot1qconstraintstatus'], name, value)

            class Dot1qConstraintType(Enum):
                """
                Dot1qConstraintType (Enum Class)

                The type of constraint this entry defines.

                independent(1) \- the VLAN, dot1qConstraintVlan,

                    uses a filtering database independent from all

                    other VLANs in the same set, defined by

                    dot1qConstraintSet.

                shared(2) \- the VLAN, dot1qConstraintVlan, shares

                    the same filtering database as all other VLANs

                    in the same set, defined by dot1qConstraintSet.

                .. data:: independent = 1

                .. data:: shared = 2

                """

                independent = Enum.YLeaf(1, "independent")

                shared = Enum.YLeaf(2, "shared")





    class Dot1vProtocolGroupTable(Entity):
        """
        A table that contains mappings from Protocol
        Templates to Protocol Group Identifiers used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolgroupentry
        
        	A mapping from a Protocol Template to a Protocol Group Identifier
        	**type**\: list of  		 :py:class:`Dot1vProtocolGroupEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1vProtocolGroupTable, self).__init__()

            self.yang_name = "dot1vProtocolGroupTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1vProtocolGroupEntry", ("dot1vprotocolgroupentry", QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry))])
            self._leafs = OrderedDict()

            self.dot1vprotocolgroupentry = YList(self)
            self._segment_path = lambda: "dot1vProtocolGroupTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1vProtocolGroupTable, [], name, value)


        class Dot1vProtocolGroupEntry(Entity):
            """
            A mapping from a Protocol Template to a Protocol
            Group Identifier.
            
            .. attribute:: dot1vprotocoltemplateframetype  (key)
            
            	The data\-link encapsulation format or the 'detagged\_frame\_type' in a Protocol Template
            	**type**\:  :py:class:`Dot1vProtocolTemplateFrameType <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType>`
            
            	**config**\: False
            
            .. attribute:: dot1vprotocoltemplateprotocolvalue  (key)
            
            	The identification of the protocol above the data\-link layer in a Protocol Template.  Depending on the frame type, the octet string will have one of the following values\:  For 'ethernet', 'rfc1042' and 'snap8021H',     this is the 16\-bit (2\-octet) IEEE 802.3 Type Field. For 'snapOther',     this is the 40\-bit (5\-octet) PID. For 'llcOther',     this is the 2\-octet IEEE 802.2 Link Service Access     Point (LSAP) pair\: first octet for Destination Service     Access Point (DSAP) and second octet for Source Service     Access Point (SSAP)
            	**type**\: str
            
            	**length:** 2 \| 5
            
            	**config**\: False
            
            .. attribute:: dot1vprotocolgroupid
            
            	Represents a group of protocols that are associated together when assigning a VID to a frame
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: dot1vprotocolgrouprowstatus
            
            	This object indicates the status of this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry, self).__init__()

                self.yang_name = "dot1vProtocolGroupEntry"
                self.yang_parent_name = "dot1vProtocolGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1vprotocoltemplateframetype','dot1vprotocoltemplateprotocolvalue']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1vprotocoltemplateframetype', (YLeaf(YType.enumeration, 'dot1vProtocolTemplateFrameType'), [('ydk.models.cisco_ios_xe.Q_BRIDGE_MIB', 'QBRIDGEMIB', 'Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType')])),
                    ('dot1vprotocoltemplateprotocolvalue', (YLeaf(YType.str, 'dot1vProtocolTemplateProtocolValue'), ['str'])),
                    ('dot1vprotocolgroupid', (YLeaf(YType.int32, 'dot1vProtocolGroupId'), ['int'])),
                    ('dot1vprotocolgrouprowstatus', (YLeaf(YType.enumeration, 'dot1vProtocolGroupRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.dot1vprotocoltemplateframetype = None
                self.dot1vprotocoltemplateprotocolvalue = None
                self.dot1vprotocolgroupid = None
                self.dot1vprotocolgrouprowstatus = None
                self._segment_path = lambda: "dot1vProtocolGroupEntry" + "[dot1vProtocolTemplateFrameType='" + str(self.dot1vprotocoltemplateframetype) + "']" + "[dot1vProtocolTemplateProtocolValue='" + str(self.dot1vprotocoltemplateprotocolvalue) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1vProtocolGroupTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry, ['dot1vprotocoltemplateframetype', 'dot1vprotocoltemplateprotocolvalue', 'dot1vprotocolgroupid', 'dot1vprotocolgrouprowstatus'], name, value)

            class Dot1vProtocolTemplateFrameType(Enum):
                """
                Dot1vProtocolTemplateFrameType (Enum Class)

                The data\-link encapsulation format or the

                'detagged\_frame\_type' in a Protocol Template.

                .. data:: ethernet = 1

                .. data:: rfc1042 = 2

                .. data:: snap8021H = 3

                .. data:: snapOther = 4

                .. data:: llcOther = 5

                """

                ethernet = Enum.YLeaf(1, "ethernet")

                rfc1042 = Enum.YLeaf(2, "rfc1042")

                snap8021H = Enum.YLeaf(3, "snap8021H")

                snapOther = Enum.YLeaf(4, "snapOther")

                llcOther = Enum.YLeaf(5, "llcOther")





    class Dot1vProtocolPortTable(Entity):
        """
        A table that contains VID sets used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolportentry
        
        	A VID set for a port
        	**type**\: list of  		 :py:class:`Dot1vProtocolPortEntry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBRIDGEMIB.Dot1vProtocolPortTable, self).__init__()

            self.yang_name = "dot1vProtocolPortTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot1vProtocolPortEntry", ("dot1vprotocolportentry", QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry))])
            self._leafs = OrderedDict()

            self.dot1vprotocolportentry = YList(self)
            self._segment_path = lambda: "dot1vProtocolPortTable"
            self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(QBRIDGEMIB.Dot1vProtocolPortTable, [], name, value)


        class Dot1vProtocolPortEntry(Entity):
            """
            A VID set for a port.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1dBasePortTable.Dot1dBasePortEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1vprotocolportgroupid  (key)
            
            	Designates a group of protocols in the Protocol Group Database
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dot1vprotocolportgroupvid
            
            	The VID associated with a group of protocols for each port
            	**type**\: int
            
            	**range:** 1..4094
            
            	**config**\: False
            
            .. attribute:: dot1vprotocolportrowstatus
            
            	This object indicates the status of this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry, self).__init__()

                self.yang_name = "dot1vProtocolPortEntry"
                self.yang_parent_name = "dot1vProtocolPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1vprotocolportgroupid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', (YLeaf(YType.str, 'dot1dBasePort'), ['int'])),
                    ('dot1vprotocolportgroupid', (YLeaf(YType.int32, 'dot1vProtocolPortGroupId'), ['int'])),
                    ('dot1vprotocolportgroupvid', (YLeaf(YType.int32, 'dot1vProtocolPortGroupVid'), ['int'])),
                    ('dot1vprotocolportrowstatus', (YLeaf(YType.enumeration, 'dot1vProtocolPortRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.dot1dbaseport = None
                self.dot1vprotocolportgroupid = None
                self.dot1vprotocolportgroupvid = None
                self.dot1vprotocolportrowstatus = None
                self._segment_path = lambda: "dot1vProtocolPortEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1vProtocolPortGroupId='" + str(self.dot1vprotocolportgroupid) + "']"
                self._absolute_path = lambda: "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1vProtocolPortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry, ['dot1dbaseport', 'dot1vprotocolportgroupid', 'dot1vprotocolportgroupvid', 'dot1vprotocolportrowstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = QBRIDGEMIB()
        return self._top_entity



