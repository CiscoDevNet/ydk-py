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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class QBridgeMib(Entity):
    """
    
    
    .. attribute:: dot1qbase
    
    	
    	**type**\:   :py:class:`Dot1Qbase <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qbase>`
    
    .. attribute:: dot1qfdbtable
    
    	A table that contains configuration and control information for each Filtering Database currently operating on this device.  Entries in this table appear automatically when VLANs are assigned FDB IDs in the dot1qVlanCurrentTable
    	**type**\:   :py:class:`Dot1Qfdbtable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qfdbtable>`
    
    .. attribute:: dot1qforwardalltable
    
    	A table containing forwarding information for each  VLAN, specifying the set of ports to which forwarding of all multicasts applies, configured statically by management or dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\:   :py:class:`Dot1Qforwardalltable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qforwardalltable>`
    
    .. attribute:: dot1qforwardunregisteredtable
    
    	A table containing forwarding information for each VLAN, specifying the set of ports to which forwarding of multicast group\-addressed frames for which no more specific forwarding information applies.  This is configured statically by management and determined dynamically by GMRP.  An entry appears in this table for all VLANs that are currently instantiated
    	**type**\:   :py:class:`Dot1Qforwardunregisteredtable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qforwardunregisteredtable>`
    
    .. attribute:: dot1qlearningconstraintstable
    
    	A table containing learning constraints for sets of Shared and Independent VLANs
    	**type**\:   :py:class:`Dot1Qlearningconstraintstable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qlearningconstraintstable>`
    
    .. attribute:: dot1qportvlanhcstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic on high\-capacity interfaces
    	**type**\:   :py:class:`Dot1Qportvlanhcstatisticstable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qportvlanhcstatisticstable>`
    
    .. attribute:: dot1qportvlanstatisticstable
    
    	A table containing per\-port, per\-VLAN statistics for traffic received.  Separate objects are provided for both the most\-significant and least\-significant bits of statistics counters for ports that are associated with this transparent bridge.  The most\-significant bit objects are only required on high\-capacity interfaces, as defined in the conformance clauses for these objects.  This mechanism is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\- significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling. The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or  asynchronous notification
    	**type**\:   :py:class:`Dot1Qportvlanstatisticstable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qportvlanstatisticstable>`
    
    .. attribute:: dot1qstaticmulticasttable
    
    	A table containing filtering information for Multicast and Broadcast MAC addresses for each VLAN, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific Multicast and Broadcast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for Multicast and Broadcast addresses only
    	**type**\:   :py:class:`Dot1Qstaticmulticasttable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticmulticasttable>`
    
    .. attribute:: dot1qstaticunicasttable
    
    	A table containing filtering information for Unicast MAC addresses for each Filtering Database, configured into the device by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific unicast destination addresses are allowed to be forwarded.  A value of zero in this table (as the port number from  which frames with a specific destination address are received) is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast addresses only
    	**type**\:   :py:class:`Dot1Qstaticunicasttable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticunicasttable>`
    
    .. attribute:: dot1qtpfdbtable
    
    	A table that contains information about unicast entries for which the device has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\:   :py:class:`Dot1Qtpfdbtable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qtpfdbtable>`
    
    .. attribute:: dot1qtpgrouptable
    
    	A table containing filtering information for VLANs configured into the bridge by (local or network) management, or learned dynamically, specifying the set of ports to which frames received on a VLAN for this FDB and containing a specific Group destination address are allowed to be forwarded
    	**type**\:   :py:class:`Dot1Qtpgrouptable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qtpgrouptable>`
    
    .. attribute:: dot1qvlan
    
    	
    	**type**\:   :py:class:`Dot1Qvlan <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlan>`
    
    .. attribute:: dot1qvlancurrenttable
    
    	A table containing current configuration information for each VLAN currently configured into the device by (local or network) management, or dynamically created as a result of GVRP requests received
    	**type**\:   :py:class:`Dot1Qvlancurrenttable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable>`
    
    .. attribute:: dot1qvlanstatictable
    
    	A table containing static configuration information for each VLAN configured into the device by (local or network) management.  All entries are permanent and will be restored after the device is reset
    	**type**\:   :py:class:`Dot1Qvlanstatictable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlanstatictable>`
    
    .. attribute:: dot1vprotocolgrouptable
    
    	A table that contains mappings from Protocol Templates to Protocol Group Identifiers used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\:   :py:class:`Dot1Vprotocolgrouptable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Vprotocolgrouptable>`
    
    .. attribute:: dot1vprotocolporttable
    
    	A table that contains VID sets used for Port\-and\-Protocol\-based VLAN Classification
    	**type**\:   :py:class:`Dot1Vprotocolporttable <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Vprotocolporttable>`
    
    

    """

    _prefix = 'Q-BRIDGE-MIB'
    _revision = '2006-01-09'

    def __init__(self):
        super(QBridgeMib, self).__init__()
        self._top_entity = None

        self.yang_name = "Q-BRIDGE-MIB"
        self.yang_parent_name = "Q-BRIDGE-MIB"

        self.dot1qbase = QBridgeMib.Dot1Qbase()
        self.dot1qbase.parent = self
        self._children_name_map["dot1qbase"] = "dot1qBase"
        self._children_yang_names.add("dot1qBase")

        self.dot1qfdbtable = QBridgeMib.Dot1Qfdbtable()
        self.dot1qfdbtable.parent = self
        self._children_name_map["dot1qfdbtable"] = "dot1qFdbTable"
        self._children_yang_names.add("dot1qFdbTable")

        self.dot1qforwardalltable = QBridgeMib.Dot1Qforwardalltable()
        self.dot1qforwardalltable.parent = self
        self._children_name_map["dot1qforwardalltable"] = "dot1qForwardAllTable"
        self._children_yang_names.add("dot1qForwardAllTable")

        self.dot1qforwardunregisteredtable = QBridgeMib.Dot1Qforwardunregisteredtable()
        self.dot1qforwardunregisteredtable.parent = self
        self._children_name_map["dot1qforwardunregisteredtable"] = "dot1qForwardUnregisteredTable"
        self._children_yang_names.add("dot1qForwardUnregisteredTable")

        self.dot1qlearningconstraintstable = QBridgeMib.Dot1Qlearningconstraintstable()
        self.dot1qlearningconstraintstable.parent = self
        self._children_name_map["dot1qlearningconstraintstable"] = "dot1qLearningConstraintsTable"
        self._children_yang_names.add("dot1qLearningConstraintsTable")

        self.dot1qportvlanhcstatisticstable = QBridgeMib.Dot1Qportvlanhcstatisticstable()
        self.dot1qportvlanhcstatisticstable.parent = self
        self._children_name_map["dot1qportvlanhcstatisticstable"] = "dot1qPortVlanHCStatisticsTable"
        self._children_yang_names.add("dot1qPortVlanHCStatisticsTable")

        self.dot1qportvlanstatisticstable = QBridgeMib.Dot1Qportvlanstatisticstable()
        self.dot1qportvlanstatisticstable.parent = self
        self._children_name_map["dot1qportvlanstatisticstable"] = "dot1qPortVlanStatisticsTable"
        self._children_yang_names.add("dot1qPortVlanStatisticsTable")

        self.dot1qstaticmulticasttable = QBridgeMib.Dot1Qstaticmulticasttable()
        self.dot1qstaticmulticasttable.parent = self
        self._children_name_map["dot1qstaticmulticasttable"] = "dot1qStaticMulticastTable"
        self._children_yang_names.add("dot1qStaticMulticastTable")

        self.dot1qstaticunicasttable = QBridgeMib.Dot1Qstaticunicasttable()
        self.dot1qstaticunicasttable.parent = self
        self._children_name_map["dot1qstaticunicasttable"] = "dot1qStaticUnicastTable"
        self._children_yang_names.add("dot1qStaticUnicastTable")

        self.dot1qtpfdbtable = QBridgeMib.Dot1Qtpfdbtable()
        self.dot1qtpfdbtable.parent = self
        self._children_name_map["dot1qtpfdbtable"] = "dot1qTpFdbTable"
        self._children_yang_names.add("dot1qTpFdbTable")

        self.dot1qtpgrouptable = QBridgeMib.Dot1Qtpgrouptable()
        self.dot1qtpgrouptable.parent = self
        self._children_name_map["dot1qtpgrouptable"] = "dot1qTpGroupTable"
        self._children_yang_names.add("dot1qTpGroupTable")

        self.dot1qvlan = QBridgeMib.Dot1Qvlan()
        self.dot1qvlan.parent = self
        self._children_name_map["dot1qvlan"] = "dot1qVlan"
        self._children_yang_names.add("dot1qVlan")

        self.dot1qvlancurrenttable = QBridgeMib.Dot1Qvlancurrenttable()
        self.dot1qvlancurrenttable.parent = self
        self._children_name_map["dot1qvlancurrenttable"] = "dot1qVlanCurrentTable"
        self._children_yang_names.add("dot1qVlanCurrentTable")

        self.dot1qvlanstatictable = QBridgeMib.Dot1Qvlanstatictable()
        self.dot1qvlanstatictable.parent = self
        self._children_name_map["dot1qvlanstatictable"] = "dot1qVlanStaticTable"
        self._children_yang_names.add("dot1qVlanStaticTable")

        self.dot1vprotocolgrouptable = QBridgeMib.Dot1Vprotocolgrouptable()
        self.dot1vprotocolgrouptable.parent = self
        self._children_name_map["dot1vprotocolgrouptable"] = "dot1vProtocolGroupTable"
        self._children_yang_names.add("dot1vProtocolGroupTable")

        self.dot1vprotocolporttable = QBridgeMib.Dot1Vprotocolporttable()
        self.dot1vprotocolporttable.parent = self
        self._children_name_map["dot1vprotocolporttable"] = "dot1vProtocolPortTable"
        self._children_yang_names.add("dot1vProtocolPortTable")


    class Dot1Qbase(Entity):
        """
        
        
        .. attribute:: dot1qgvrpstatus
        
        	The administrative status requested by management for GVRP.  The value enabled(1) indicates that GVRP should be enabled on this device, on all ports for which it has not been specifically disabled.  When disabled(2), GVRP is disabled on all ports, and all GVRP packets will be forwarded transparently.  This object affects all GVRP Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GVRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:   :py:class:`Enabledstatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.Enabledstatus>`
        
        .. attribute:: dot1qmaxsupportedvlans
        
        	The maximum number of IEEE 802.1Q VLANs that this device supports
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1qmaxvlanid
        
        	The maximum IEEE 802.1Q VLAN\-ID that this device  supports
        	**type**\:  int
        
        	**range:** 1..4094
        
        .. attribute:: dot1qnumvlans
        
        	The current number of IEEE 802.1Q VLANs that are configured in this device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1qvlanversionnumber
        
        	The version number of IEEE 802.1Q that this device supports
        	**type**\:   :py:class:`Dot1Qvlanversionnumber <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qbase.Dot1Qvlanversionnumber>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qbase, self).__init__()

            self.yang_name = "dot1qBase"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qgvrpstatus = YLeaf(YType.enumeration, "dot1qGvrpStatus")

            self.dot1qmaxsupportedvlans = YLeaf(YType.uint32, "dot1qMaxSupportedVlans")

            self.dot1qmaxvlanid = YLeaf(YType.int32, "dot1qMaxVlanId")

            self.dot1qnumvlans = YLeaf(YType.uint32, "dot1qNumVlans")

            self.dot1qvlanversionnumber = YLeaf(YType.enumeration, "dot1qVlanVersionNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1qgvrpstatus",
                            "dot1qmaxsupportedvlans",
                            "dot1qmaxvlanid",
                            "dot1qnumvlans",
                            "dot1qvlanversionnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(QBridgeMib.Dot1Qbase, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qbase, self).__setattr__(name, value)

        class Dot1Qvlanversionnumber(Enum):
            """
            Dot1Qvlanversionnumber

            The version number of IEEE 802.1Q that this device

            supports.

            .. data:: version1 = 1

            """

            version1 = Enum.YLeaf(1, "version1")


        def has_data(self):
            return (
                self.dot1qgvrpstatus.is_set or
                self.dot1qmaxsupportedvlans.is_set or
                self.dot1qmaxvlanid.is_set or
                self.dot1qnumvlans.is_set or
                self.dot1qvlanversionnumber.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1qgvrpstatus.yfilter != YFilter.not_set or
                self.dot1qmaxsupportedvlans.yfilter != YFilter.not_set or
                self.dot1qmaxvlanid.yfilter != YFilter.not_set or
                self.dot1qnumvlans.yfilter != YFilter.not_set or
                self.dot1qvlanversionnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qBase" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1qgvrpstatus.is_set or self.dot1qgvrpstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qgvrpstatus.get_name_leafdata())
            if (self.dot1qmaxsupportedvlans.is_set or self.dot1qmaxsupportedvlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qmaxsupportedvlans.get_name_leafdata())
            if (self.dot1qmaxvlanid.is_set or self.dot1qmaxvlanid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qmaxvlanid.get_name_leafdata())
            if (self.dot1qnumvlans.is_set or self.dot1qnumvlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qnumvlans.get_name_leafdata())
            if (self.dot1qvlanversionnumber.is_set or self.dot1qvlanversionnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qvlanversionnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qGvrpStatus" or name == "dot1qMaxSupportedVlans" or name == "dot1qMaxVlanId" or name == "dot1qNumVlans" or name == "dot1qVlanVersionNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1qGvrpStatus"):
                self.dot1qgvrpstatus = value
                self.dot1qgvrpstatus.value_namespace = name_space
                self.dot1qgvrpstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qMaxSupportedVlans"):
                self.dot1qmaxsupportedvlans = value
                self.dot1qmaxsupportedvlans.value_namespace = name_space
                self.dot1qmaxsupportedvlans.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qMaxVlanId"):
                self.dot1qmaxvlanid = value
                self.dot1qmaxvlanid.value_namespace = name_space
                self.dot1qmaxvlanid.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qNumVlans"):
                self.dot1qnumvlans = value
                self.dot1qnumvlans.value_namespace = name_space
                self.dot1qnumvlans.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qVlanVersionNumber"):
                self.dot1qvlanversionnumber = value
                self.dot1qvlanversionnumber.value_namespace = name_space
                self.dot1qvlanversionnumber.value_namespace_prefix = name_space_prefix


    class Dot1Qvlan(Entity):
        """
        
        
        .. attribute:: dot1qconstraintsetdefault
        
        	The identity of the constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: dot1qconstrainttypedefault
        
        	The type of constraint set to which a VLAN belongs, if there is not an explicit entry for that VLAN in dot1qLearningConstraintsTable.  The types are as defined for dot1qConstraintType.  The value of this object MUST be retained across  reinitializations of the management system
        	**type**\:   :py:class:`Dot1Qconstrainttypedefault <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlan.Dot1Qconstrainttypedefault>`
        
        .. attribute:: dot1qnextfreelocalvlanindex
        
        	The next available value for dot1qVlanIndex of a local VLAN entry in dot1qVlanStaticTable.  This will report values >=4096 if a new Local VLAN may be created or else the value 0 if this is not possible.  A row creation operation in this table for an entry with a local VlanIndex value may fail if the current value of this object is not used as the index.  Even if the value read is used, there is no guarantee that it will still be the valid index when the create operation is attempted; another manager may have already got in during the intervening time interval. In this case, dot1qNextFreeLocalVlanIndex should be re\-read  and the creation re\-tried with the new value.  This value will automatically change when the current value is used to create a new row
        	**type**\:  int
        
        	**range:** 0..None \| 4096..2147483647
        
        .. attribute:: dot1qvlannumdeletes
        
        	The number of times a VLAN entry has been deleted from the dot1qVlanCurrentTable (for any reason).  If an entry is deleted, then inserted, and then deleted, this counter will be incremented by 2
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qvlan, self).__init__()

            self.yang_name = "dot1qVlan"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qconstraintsetdefault = YLeaf(YType.int32, "dot1qConstraintSetDefault")

            self.dot1qconstrainttypedefault = YLeaf(YType.enumeration, "dot1qConstraintTypeDefault")

            self.dot1qnextfreelocalvlanindex = YLeaf(YType.int32, "dot1qNextFreeLocalVlanIndex")

            self.dot1qvlannumdeletes = YLeaf(YType.uint32, "dot1qVlanNumDeletes")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1qconstraintsetdefault",
                            "dot1qconstrainttypedefault",
                            "dot1qnextfreelocalvlanindex",
                            "dot1qvlannumdeletes") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(QBridgeMib.Dot1Qvlan, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qvlan, self).__setattr__(name, value)

        class Dot1Qconstrainttypedefault(Enum):
            """
            Dot1Qconstrainttypedefault

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


        def has_data(self):
            return (
                self.dot1qconstraintsetdefault.is_set or
                self.dot1qconstrainttypedefault.is_set or
                self.dot1qnextfreelocalvlanindex.is_set or
                self.dot1qvlannumdeletes.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1qconstraintsetdefault.yfilter != YFilter.not_set or
                self.dot1qconstrainttypedefault.yfilter != YFilter.not_set or
                self.dot1qnextfreelocalvlanindex.yfilter != YFilter.not_set or
                self.dot1qvlannumdeletes.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qVlan" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1qconstraintsetdefault.is_set or self.dot1qconstraintsetdefault.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qconstraintsetdefault.get_name_leafdata())
            if (self.dot1qconstrainttypedefault.is_set or self.dot1qconstrainttypedefault.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qconstrainttypedefault.get_name_leafdata())
            if (self.dot1qnextfreelocalvlanindex.is_set or self.dot1qnextfreelocalvlanindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qnextfreelocalvlanindex.get_name_leafdata())
            if (self.dot1qvlannumdeletes.is_set or self.dot1qvlannumdeletes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1qvlannumdeletes.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qConstraintSetDefault" or name == "dot1qConstraintTypeDefault" or name == "dot1qNextFreeLocalVlanIndex" or name == "dot1qVlanNumDeletes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1qConstraintSetDefault"):
                self.dot1qconstraintsetdefault = value
                self.dot1qconstraintsetdefault.value_namespace = name_space
                self.dot1qconstraintsetdefault.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qConstraintTypeDefault"):
                self.dot1qconstrainttypedefault = value
                self.dot1qconstrainttypedefault.value_namespace = name_space
                self.dot1qconstrainttypedefault.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qNextFreeLocalVlanIndex"):
                self.dot1qnextfreelocalvlanindex = value
                self.dot1qnextfreelocalvlanindex.value_namespace = name_space
                self.dot1qnextfreelocalvlanindex.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1qVlanNumDeletes"):
                self.dot1qvlannumdeletes = value
                self.dot1qvlannumdeletes.value_namespace = name_space
                self.dot1qvlannumdeletes.value_namespace_prefix = name_space_prefix


    class Dot1Qfdbtable(Entity):
        """
        A table that contains configuration and control
        information for each Filtering Database currently
        operating on this device.  Entries in this table appear
        automatically when VLANs are assigned FDB IDs in the
        dot1qVlanCurrentTable.
        
        .. attribute:: dot1qfdbentry
        
        	Information about a specific Filtering Database
        	**type**\: list of    :py:class:`Dot1Qfdbentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qfdbtable, self).__init__()

            self.yang_name = "dot1qFdbTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qfdbentry = YList(self)

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
                        super(QBridgeMib.Dot1Qfdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qfdbtable, self).__setattr__(name, value)


        class Dot1Qfdbentry(Entity):
            """
            Information about a specific Filtering Database.
            
            .. attribute:: dot1qfdbid  <key>
            
            	The identity of this Filtering Database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qfdbdynamiccount
            
            	The current number of dynamic entries in this Filtering Database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry, self).__init__()

                self.yang_name = "dot1qFdbEntry"
                self.yang_parent_name = "dot1qFdbTable"

                self.dot1qfdbid = YLeaf(YType.uint32, "dot1qFdbId")

                self.dot1qfdbdynamiccount = YLeaf(YType.uint32, "dot1qFdbDynamicCount")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qfdbid",
                                "dot1qfdbdynamiccount") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1qfdbid.is_set or
                    self.dot1qfdbdynamiccount.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qfdbid.yfilter != YFilter.not_set or
                    self.dot1qfdbdynamiccount.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qFdbEntry" + "[dot1qFdbId='" + self.dot1qfdbid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qFdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qfdbid.is_set or self.dot1qfdbid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qfdbid.get_name_leafdata())
                if (self.dot1qfdbdynamiccount.is_set or self.dot1qfdbdynamiccount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qfdbdynamiccount.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qFdbId" or name == "dot1qFdbDynamicCount"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qFdbId"):
                    self.dot1qfdbid = value
                    self.dot1qfdbid.value_namespace = name_space
                    self.dot1qfdbid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qFdbDynamicCount"):
                    self.dot1qfdbdynamiccount = value
                    self.dot1qfdbdynamiccount.value_namespace = name_space
                    self.dot1qfdbdynamiccount.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qfdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qfdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qFdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qFdbEntry"):
                for c in self.dot1qfdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qfdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qFdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qtpfdbtable(Entity):
        """
        A table that contains information about unicast entries
        for which the device has forwarding and/or filtering
        information.  This information is used by the
        transparent bridging function in determining how to
        propagate a received frame.
        
        .. attribute:: dot1qtpfdbentry
        
        	Information about a specific unicast MAC address for which the device has some forwarding and/or filtering information
        	**type**\: list of    :py:class:`Dot1Qtpfdbentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qtpfdbtable, self).__init__()

            self.yang_name = "dot1qTpFdbTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qtpfdbentry = YList(self)

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
                        super(QBridgeMib.Dot1Qtpfdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qtpfdbtable, self).__setattr__(name, value)


        class Dot1Qtpfdbentry(Entity):
            """
            Information about a specific unicast MAC address for
            which the device has some forwarding and/or filtering
            information.
            
            .. attribute:: dot1qfdbid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qfdbid <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry>`
            
            .. attribute:: dot1qtpfdbaddress  <key>
            
            	A unicast MAC address for which the device has forwarding and/or filtering information
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1qTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned but that the device does have some forwarding/filtering information about this address (e.g., in the dot1qStaticUnicastTable). Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1qTpFdbStatus is not learned(3)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This may include         the case where some other MIB object (not the         corresponding instance of dot1qTpFdbPort, nor an         entry in the dot1qStaticUnicastTable) is being         used to determine if and how frames addressed to         the value of the corresponding instance of         dot1qTpFdbAddress are being forwarded.     invalid(2) \- this entry is no longer valid (e.g., it          was learned but has since aged out), but has not         yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1qTpFdbPort was learned and is being used.     self(4) \- the value of the corresponding instance of         dot1qTpFdbAddress represents one of the device's         addresses.  The corresponding instance of         dot1qTpFdbPort indicates which of the device's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1qTpFdbAddress is also the value of an         existing instance of dot1qStaticAddress
            	**type**\:   :py:class:`Dot1Qtpfdbstatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry.Dot1Qtpfdbstatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry, self).__init__()

                self.yang_name = "dot1qTpFdbEntry"
                self.yang_parent_name = "dot1qTpFdbTable"

                self.dot1qfdbid = YLeaf(YType.str, "dot1qFdbId")

                self.dot1qtpfdbaddress = YLeaf(YType.str, "dot1qTpFdbAddress")

                self.dot1qtpfdbport = YLeaf(YType.int32, "dot1qTpFdbPort")

                self.dot1qtpfdbstatus = YLeaf(YType.enumeration, "dot1qTpFdbStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qfdbid",
                                "dot1qtpfdbaddress",
                                "dot1qtpfdbport",
                                "dot1qtpfdbstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry, self).__setattr__(name, value)

            class Dot1Qtpfdbstatus(Enum):
                """
                Dot1Qtpfdbstatus

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


            def has_data(self):
                return (
                    self.dot1qfdbid.is_set or
                    self.dot1qtpfdbaddress.is_set or
                    self.dot1qtpfdbport.is_set or
                    self.dot1qtpfdbstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qfdbid.yfilter != YFilter.not_set or
                    self.dot1qtpfdbaddress.yfilter != YFilter.not_set or
                    self.dot1qtpfdbport.yfilter != YFilter.not_set or
                    self.dot1qtpfdbstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qTpFdbEntry" + "[dot1qFdbId='" + self.dot1qfdbid.get() + "']" + "[dot1qTpFdbAddress='" + self.dot1qtpfdbaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qTpFdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qfdbid.is_set or self.dot1qfdbid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qfdbid.get_name_leafdata())
                if (self.dot1qtpfdbaddress.is_set or self.dot1qtpfdbaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpfdbaddress.get_name_leafdata())
                if (self.dot1qtpfdbport.is_set or self.dot1qtpfdbport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpfdbport.get_name_leafdata())
                if (self.dot1qtpfdbstatus.is_set or self.dot1qtpfdbstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpfdbstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qFdbId" or name == "dot1qTpFdbAddress" or name == "dot1qTpFdbPort" or name == "dot1qTpFdbStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qFdbId"):
                    self.dot1qfdbid = value
                    self.dot1qfdbid.value_namespace = name_space
                    self.dot1qfdbid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpFdbAddress"):
                    self.dot1qtpfdbaddress = value
                    self.dot1qtpfdbaddress.value_namespace = name_space
                    self.dot1qtpfdbaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpFdbPort"):
                    self.dot1qtpfdbport = value
                    self.dot1qtpfdbport.value_namespace = name_space
                    self.dot1qtpfdbport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpFdbStatus"):
                    self.dot1qtpfdbstatus = value
                    self.dot1qtpfdbstatus.value_namespace = name_space
                    self.dot1qtpfdbstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qtpfdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qtpfdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qTpFdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qTpFdbEntry"):
                for c in self.dot1qtpfdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qtpfdbtable.Dot1Qtpfdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qtpfdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qTpFdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qtpgrouptable(Entity):
        """
        A table containing filtering information for VLANs
        configured into the bridge by (local or network)
        management, or learned dynamically, specifying the set of
        ports to which frames received on a VLAN for this FDB
        and containing a specific Group destination address are
        allowed to be forwarded.
        
        .. attribute:: dot1qtpgroupentry
        
        	Filtering information configured into the bridge by management, or learned dynamically, specifying the set of ports to which frames received on a VLAN and containing a specific Group destination address are allowed to be forwarded.  The subset of these ports learned dynamically is also provided
        	**type**\: list of    :py:class:`Dot1Qtpgroupentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qtpgrouptable.Dot1Qtpgroupentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qtpgrouptable, self).__init__()

            self.yang_name = "dot1qTpGroupTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qtpgroupentry = YList(self)

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
                        super(QBridgeMib.Dot1Qtpgrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qtpgrouptable, self).__setattr__(name, value)


        class Dot1Qtpgroupentry(Entity):
            """
            Filtering information configured into the bridge by
            management, or learned dynamically, specifying the set of
            ports to which frames received on a VLAN and containing
            a specific Group destination address are allowed to be
            forwarded.  The subset of these ports learned dynamically
            is also provided.
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qtpgroupaddress  <key>
            
            	The destination Group MAC address in a frame to which this entry's filtering information applies
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qtpgroupegressports
            
            	The complete set of ports, in this VLAN, to which frames destined for this Group MAC address are currently being explicitly forwarded.  This does not include ports for which this address is only implicitly forwarded, in the dot1qForwardAllPorts list
            	**type**\:  str
            
            .. attribute:: dot1qtpgrouplearnt
            
            	The subset of ports in dot1qTpGroupEgressPorts that were learned by GMRP or some other dynamic mechanism, in this Filtering database
            	**type**\:  str
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qtpgrouptable.Dot1Qtpgroupentry, self).__init__()

                self.yang_name = "dot1qTpGroupEntry"
                self.yang_parent_name = "dot1qTpGroupTable"

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qtpgroupaddress = YLeaf(YType.str, "dot1qTpGroupAddress")

                self.dot1qtpgroupegressports = YLeaf(YType.str, "dot1qTpGroupEgressPorts")

                self.dot1qtpgrouplearnt = YLeaf(YType.str, "dot1qTpGroupLearnt")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlanindex",
                                "dot1qtpgroupaddress",
                                "dot1qtpgroupegressports",
                                "dot1qtpgrouplearnt") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qtpgrouptable.Dot1Qtpgroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qtpgrouptable.Dot1Qtpgroupentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1qvlanindex.is_set or
                    self.dot1qtpgroupaddress.is_set or
                    self.dot1qtpgroupegressports.is_set or
                    self.dot1qtpgrouplearnt.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qtpgroupaddress.yfilter != YFilter.not_set or
                    self.dot1qtpgroupegressports.yfilter != YFilter.not_set or
                    self.dot1qtpgrouplearnt.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qTpGroupEntry" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + "[dot1qTpGroupAddress='" + self.dot1qtpgroupaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qTpGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qtpgroupaddress.is_set or self.dot1qtpgroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpgroupaddress.get_name_leafdata())
                if (self.dot1qtpgroupegressports.is_set or self.dot1qtpgroupegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpgroupegressports.get_name_leafdata())
                if (self.dot1qtpgrouplearnt.is_set or self.dot1qtpgrouplearnt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpgrouplearnt.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanIndex" or name == "dot1qTpGroupAddress" or name == "dot1qTpGroupEgressPorts" or name == "dot1qTpGroupLearnt"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpGroupAddress"):
                    self.dot1qtpgroupaddress = value
                    self.dot1qtpgroupaddress.value_namespace = name_space
                    self.dot1qtpgroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpGroupEgressPorts"):
                    self.dot1qtpgroupegressports = value
                    self.dot1qtpgroupegressports.value_namespace = name_space
                    self.dot1qtpgroupegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpGroupLearnt"):
                    self.dot1qtpgrouplearnt = value
                    self.dot1qtpgrouplearnt.value_namespace = name_space
                    self.dot1qtpgrouplearnt.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qtpgroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qtpgroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qTpGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qTpGroupEntry"):
                for c in self.dot1qtpgroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qtpgrouptable.Dot1Qtpgroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qtpgroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qTpGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qforwardalltable(Entity):
        """
        A table containing forwarding information for each
        
        VLAN, specifying the set of ports to which forwarding of
        all multicasts applies, configured statically by
        management or dynamically by GMRP.  An entry appears in
        this table for all VLANs that are currently
        instantiated.
        
        .. attribute:: dot1qforwardallentry
        
        	Forwarding information for a VLAN, specifying the set of ports to which all multicasts should be forwarded, configured statically by management or dynamically by GMRP
        	**type**\: list of    :py:class:`Dot1Qforwardallentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qforwardalltable.Dot1Qforwardallentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qforwardalltable, self).__init__()

            self.yang_name = "dot1qForwardAllTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qforwardallentry = YList(self)

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
                        super(QBridgeMib.Dot1Qforwardalltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qforwardalltable, self).__setattr__(name, value)


        class Dot1Qforwardallentry(Entity):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts should be forwarded,
            configured statically by management or dynamically by
            GMRP.
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qforwardallforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward All Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            .. attribute:: dot1qforwardallports
            
            	The complete set of ports in this VLAN to which all multicast group\-addressed frames are to be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\:  str
            
            .. attribute:: dot1qforwardallstaticports
            
            	The set of ports configured by management in this VLAN to which all multicast group\-addressed frames are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardAllPorts.  This value will be restored after the device is reset.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardAllForbiddenPorts.  The default value is a string of ones of appropriate length, to indicate the standard behaviour of using basic filtering services, i.e., forward all multicasts to all ports.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qforwardalltable.Dot1Qforwardallentry, self).__init__()

                self.yang_name = "dot1qForwardAllEntry"
                self.yang_parent_name = "dot1qForwardAllTable"

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qforwardallforbiddenports = YLeaf(YType.str, "dot1qForwardAllForbiddenPorts")

                self.dot1qforwardallports = YLeaf(YType.str, "dot1qForwardAllPorts")

                self.dot1qforwardallstaticports = YLeaf(YType.str, "dot1qForwardAllStaticPorts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlanindex",
                                "dot1qforwardallforbiddenports",
                                "dot1qforwardallports",
                                "dot1qforwardallstaticports") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qforwardalltable.Dot1Qforwardallentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qforwardalltable.Dot1Qforwardallentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1qvlanindex.is_set or
                    self.dot1qforwardallforbiddenports.is_set or
                    self.dot1qforwardallports.is_set or
                    self.dot1qforwardallstaticports.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qforwardallforbiddenports.yfilter != YFilter.not_set or
                    self.dot1qforwardallports.yfilter != YFilter.not_set or
                    self.dot1qforwardallstaticports.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qForwardAllEntry" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qForwardAllTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qforwardallforbiddenports.is_set or self.dot1qforwardallforbiddenports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardallforbiddenports.get_name_leafdata())
                if (self.dot1qforwardallports.is_set or self.dot1qforwardallports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardallports.get_name_leafdata())
                if (self.dot1qforwardallstaticports.is_set or self.dot1qforwardallstaticports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardallstaticports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanIndex" or name == "dot1qForwardAllForbiddenPorts" or name == "dot1qForwardAllPorts" or name == "dot1qForwardAllStaticPorts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardAllForbiddenPorts"):
                    self.dot1qforwardallforbiddenports = value
                    self.dot1qforwardallforbiddenports.value_namespace = name_space
                    self.dot1qforwardallforbiddenports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardAllPorts"):
                    self.dot1qforwardallports = value
                    self.dot1qforwardallports.value_namespace = name_space
                    self.dot1qforwardallports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardAllStaticPorts"):
                    self.dot1qforwardallstaticports = value
                    self.dot1qforwardallstaticports.value_namespace = name_space
                    self.dot1qforwardallstaticports.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qforwardallentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qforwardallentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qForwardAllTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qForwardAllEntry"):
                for c in self.dot1qforwardallentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qforwardalltable.Dot1Qforwardallentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qforwardallentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qForwardAllEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qforwardunregisteredtable(Entity):
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
        	**type**\: list of    :py:class:`Dot1Qforwardunregisteredentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qforwardunregisteredtable.Dot1Qforwardunregisteredentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qforwardunregisteredtable, self).__init__()

            self.yang_name = "dot1qForwardUnregisteredTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qforwardunregisteredentry = YList(self)

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
                        super(QBridgeMib.Dot1Qforwardunregisteredtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qforwardunregisteredtable, self).__setattr__(name, value)


        class Dot1Qforwardunregisteredentry(Entity):
            """
            Forwarding information for a VLAN, specifying the set
            of ports to which all multicasts for which there is no
            more specific forwarding information shall be forwarded.
            This is configured statically by management or
            dynamically by GMRP.
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qforwardunregisteredforbiddenports
            
            	The set of ports configured by management in this VLAN for which the Service Requirement attribute Forward Unregistered Multicast Groups may not be dynamically registered by GMRP.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredStaticPorts.  The default value is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            .. attribute:: dot1qforwardunregisteredports
            
            	The complete set of ports in this VLAN to which multicast group\-addressed frames for which there is no more specific forwarding information will be forwarded. This includes ports for which this need has been determined dynamically by GMRP, or configured statically by management
            	**type**\:  str
            
            .. attribute:: dot1qforwardunregisteredstaticports
            
            	The set of ports configured by management, in this VLAN, to which multicast group\-addressed frames for which there is no more specific forwarding information  are to be forwarded.  Ports entered in this list will also appear in the complete set shown by dot1qForwardUnregisteredPorts.  This value will be restored after the device is reset.  A port may not be added in this set if it is already a member of the set of ports in dot1qForwardUnregisteredForbiddenPorts.  The default value is a string of zeros of appropriate length, although this has no effect with the default value of dot1qForwardAllStaticPorts.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qforwardunregisteredtable.Dot1Qforwardunregisteredentry, self).__init__()

                self.yang_name = "dot1qForwardUnregisteredEntry"
                self.yang_parent_name = "dot1qForwardUnregisteredTable"

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qforwardunregisteredforbiddenports = YLeaf(YType.str, "dot1qForwardUnregisteredForbiddenPorts")

                self.dot1qforwardunregisteredports = YLeaf(YType.str, "dot1qForwardUnregisteredPorts")

                self.dot1qforwardunregisteredstaticports = YLeaf(YType.str, "dot1qForwardUnregisteredStaticPorts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlanindex",
                                "dot1qforwardunregisteredforbiddenports",
                                "dot1qforwardunregisteredports",
                                "dot1qforwardunregisteredstaticports") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qforwardunregisteredtable.Dot1Qforwardunregisteredentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qforwardunregisteredtable.Dot1Qforwardunregisteredentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1qvlanindex.is_set or
                    self.dot1qforwardunregisteredforbiddenports.is_set or
                    self.dot1qforwardunregisteredports.is_set or
                    self.dot1qforwardunregisteredstaticports.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qforwardunregisteredforbiddenports.yfilter != YFilter.not_set or
                    self.dot1qforwardunregisteredports.yfilter != YFilter.not_set or
                    self.dot1qforwardunregisteredstaticports.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qForwardUnregisteredEntry" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qForwardUnregisteredTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qforwardunregisteredforbiddenports.is_set or self.dot1qforwardunregisteredforbiddenports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardunregisteredforbiddenports.get_name_leafdata())
                if (self.dot1qforwardunregisteredports.is_set or self.dot1qforwardunregisteredports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardunregisteredports.get_name_leafdata())
                if (self.dot1qforwardunregisteredstaticports.is_set or self.dot1qforwardunregisteredstaticports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qforwardunregisteredstaticports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanIndex" or name == "dot1qForwardUnregisteredForbiddenPorts" or name == "dot1qForwardUnregisteredPorts" or name == "dot1qForwardUnregisteredStaticPorts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardUnregisteredForbiddenPorts"):
                    self.dot1qforwardunregisteredforbiddenports = value
                    self.dot1qforwardunregisteredforbiddenports.value_namespace = name_space
                    self.dot1qforwardunregisteredforbiddenports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardUnregisteredPorts"):
                    self.dot1qforwardunregisteredports = value
                    self.dot1qforwardunregisteredports.value_namespace = name_space
                    self.dot1qforwardunregisteredports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qForwardUnregisteredStaticPorts"):
                    self.dot1qforwardunregisteredstaticports = value
                    self.dot1qforwardunregisteredstaticports.value_namespace = name_space
                    self.dot1qforwardunregisteredstaticports.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qforwardunregisteredentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qforwardunregisteredentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qForwardUnregisteredTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qForwardUnregisteredEntry"):
                for c in self.dot1qforwardunregisteredentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qforwardunregisteredtable.Dot1Qforwardunregisteredentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qforwardunregisteredentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qForwardUnregisteredEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qstaticunicasttable(Entity):
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
        	**type**\: list of    :py:class:`Dot1Qstaticunicastentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qstaticunicasttable, self).__init__()

            self.yang_name = "dot1qStaticUnicastTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qstaticunicastentry = YList(self)

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
                        super(QBridgeMib.Dot1Qstaticunicasttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qstaticunicasttable, self).__setattr__(name, value)


        class Dot1Qstaticunicastentry(Entity):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific unicast destination address are
            allowed to be forwarded.
            
            .. attribute:: dot1qfdbid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qfdbid <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qfdbtable.Dot1Qfdbentry>`
            
            .. attribute:: dot1qstaticunicastaddress  <key>
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a unicast address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qstaticunicastreceiveport  <key>
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qstaticunicastallowedtogoto
            
            	The set of ports for which a frame with a specific unicast address will be flooded in the event that it has not been learned.  It also specifies the set of ports on which a specific unicast address may be dynamically learned.  The dot1qTpFdbTable will have an equivalent entry with a dot1qTpFdbPort value of '0' until this address has been learned, at which point it will be updated with the port the address has been seen on.  This only applies to ports that are members of the VLAN, defined by dot1qVlanCurrentEgressPorts.  The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            .. attribute:: dot1qstaticunicaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but      the conditions under which it will remain     so differ from the following values. invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`Dot1Qstaticunicaststatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry.Dot1Qstaticunicaststatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry, self).__init__()

                self.yang_name = "dot1qStaticUnicastEntry"
                self.yang_parent_name = "dot1qStaticUnicastTable"

                self.dot1qfdbid = YLeaf(YType.str, "dot1qFdbId")

                self.dot1qstaticunicastaddress = YLeaf(YType.str, "dot1qStaticUnicastAddress")

                self.dot1qstaticunicastreceiveport = YLeaf(YType.int32, "dot1qStaticUnicastReceivePort")

                self.dot1qstaticunicastallowedtogoto = YLeaf(YType.str, "dot1qStaticUnicastAllowedToGoTo")

                self.dot1qstaticunicaststatus = YLeaf(YType.enumeration, "dot1qStaticUnicastStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qfdbid",
                                "dot1qstaticunicastaddress",
                                "dot1qstaticunicastreceiveport",
                                "dot1qstaticunicastallowedtogoto",
                                "dot1qstaticunicaststatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry, self).__setattr__(name, value)

            class Dot1Qstaticunicaststatus(Enum):
                """
                Dot1Qstaticunicaststatus

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


            def has_data(self):
                return (
                    self.dot1qfdbid.is_set or
                    self.dot1qstaticunicastaddress.is_set or
                    self.dot1qstaticunicastreceiveport.is_set or
                    self.dot1qstaticunicastallowedtogoto.is_set or
                    self.dot1qstaticunicaststatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qfdbid.yfilter != YFilter.not_set or
                    self.dot1qstaticunicastaddress.yfilter != YFilter.not_set or
                    self.dot1qstaticunicastreceiveport.yfilter != YFilter.not_set or
                    self.dot1qstaticunicastallowedtogoto.yfilter != YFilter.not_set or
                    self.dot1qstaticunicaststatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qStaticUnicastEntry" + "[dot1qFdbId='" + self.dot1qfdbid.get() + "']" + "[dot1qStaticUnicastAddress='" + self.dot1qstaticunicastaddress.get() + "']" + "[dot1qStaticUnicastReceivePort='" + self.dot1qstaticunicastreceiveport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qStaticUnicastTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qfdbid.is_set or self.dot1qfdbid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qfdbid.get_name_leafdata())
                if (self.dot1qstaticunicastaddress.is_set or self.dot1qstaticunicastaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticunicastaddress.get_name_leafdata())
                if (self.dot1qstaticunicastreceiveport.is_set or self.dot1qstaticunicastreceiveport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticunicastreceiveport.get_name_leafdata())
                if (self.dot1qstaticunicastallowedtogoto.is_set or self.dot1qstaticunicastallowedtogoto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticunicastallowedtogoto.get_name_leafdata())
                if (self.dot1qstaticunicaststatus.is_set or self.dot1qstaticunicaststatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticunicaststatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qFdbId" or name == "dot1qStaticUnicastAddress" or name == "dot1qStaticUnicastReceivePort" or name == "dot1qStaticUnicastAllowedToGoTo" or name == "dot1qStaticUnicastStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qFdbId"):
                    self.dot1qfdbid = value
                    self.dot1qfdbid.value_namespace = name_space
                    self.dot1qfdbid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticUnicastAddress"):
                    self.dot1qstaticunicastaddress = value
                    self.dot1qstaticunicastaddress.value_namespace = name_space
                    self.dot1qstaticunicastaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticUnicastReceivePort"):
                    self.dot1qstaticunicastreceiveport = value
                    self.dot1qstaticunicastreceiveport.value_namespace = name_space
                    self.dot1qstaticunicastreceiveport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticUnicastAllowedToGoTo"):
                    self.dot1qstaticunicastallowedtogoto = value
                    self.dot1qstaticunicastallowedtogoto.value_namespace = name_space
                    self.dot1qstaticunicastallowedtogoto.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticUnicastStatus"):
                    self.dot1qstaticunicaststatus = value
                    self.dot1qstaticunicaststatus.value_namespace = name_space
                    self.dot1qstaticunicaststatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qstaticunicastentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qstaticunicastentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qStaticUnicastTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qStaticUnicastEntry"):
                for c in self.dot1qstaticunicastentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qstaticunicasttable.Dot1Qstaticunicastentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qstaticunicastentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qStaticUnicastEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qstaticmulticasttable(Entity):
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
        	**type**\: list of    :py:class:`Dot1Qstaticmulticastentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qstaticmulticasttable, self).__init__()

            self.yang_name = "dot1qStaticMulticastTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qstaticmulticastentry = YList(self)

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
                        super(QBridgeMib.Dot1Qstaticmulticasttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qstaticmulticasttable, self).__setattr__(name, value)


        class Dot1Qstaticmulticastentry(Entity):
            """
            Filtering information configured into the device by
            (local or network) management specifying the set of
            ports to which frames received from this specific port
            
            for this VLAN and containing this Multicast or Broadcast
            destination address are allowed to be forwarded.
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qstaticmulticastaddress  <key>
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object must take the value of a Multicast or Broadcast address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qstaticmulticastreceiveport  <key>
            
            	Either the value '0' or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the device for which there is no other applicable entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qstaticmulticastforbiddenegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must not be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastStaticEgressPorts. The default value of this object is a string of zeros of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            .. attribute:: dot1qstaticmulticaststaticegressports
            
            	The set of ports to which frames received from a specific port and destined for a specific Multicast or Broadcast MAC address must be forwarded, regardless of any dynamic information, e.g., from GMRP.  A port may not be added in this set if it is already a member of the set of ports in dot1qStaticMulticastForbiddenEgressPorts. The default value of this object is a string of ones of appropriate length.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  str
            
            .. attribute:: dot1qstaticmulticaststatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but     the conditions under which it will remain     so differ from the following values.  invalid(2) \- writing this value to the object     removes the corresponding entry. permanent(3) \- this entry is currently in use     and will remain so after the next reset of     the bridge. deleteOnReset(4) \- this entry is currently in     use and will remain so until the next     reset of the bridge. deleteOnTimeout(5) \- this entry is currently in     use and will remain so until it is aged out.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`Dot1Qstaticmulticaststatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry.Dot1Qstaticmulticaststatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry, self).__init__()

                self.yang_name = "dot1qStaticMulticastEntry"
                self.yang_parent_name = "dot1qStaticMulticastTable"

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qstaticmulticastaddress = YLeaf(YType.str, "dot1qStaticMulticastAddress")

                self.dot1qstaticmulticastreceiveport = YLeaf(YType.int32, "dot1qStaticMulticastReceivePort")

                self.dot1qstaticmulticastforbiddenegressports = YLeaf(YType.str, "dot1qStaticMulticastForbiddenEgressPorts")

                self.dot1qstaticmulticaststaticegressports = YLeaf(YType.str, "dot1qStaticMulticastStaticEgressPorts")

                self.dot1qstaticmulticaststatus = YLeaf(YType.enumeration, "dot1qStaticMulticastStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlanindex",
                                "dot1qstaticmulticastaddress",
                                "dot1qstaticmulticastreceiveport",
                                "dot1qstaticmulticastforbiddenegressports",
                                "dot1qstaticmulticaststaticegressports",
                                "dot1qstaticmulticaststatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry, self).__setattr__(name, value)

            class Dot1Qstaticmulticaststatus(Enum):
                """
                Dot1Qstaticmulticaststatus

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


            def has_data(self):
                return (
                    self.dot1qvlanindex.is_set or
                    self.dot1qstaticmulticastaddress.is_set or
                    self.dot1qstaticmulticastreceiveport.is_set or
                    self.dot1qstaticmulticastforbiddenegressports.is_set or
                    self.dot1qstaticmulticaststaticegressports.is_set or
                    self.dot1qstaticmulticaststatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qstaticmulticastaddress.yfilter != YFilter.not_set or
                    self.dot1qstaticmulticastreceiveport.yfilter != YFilter.not_set or
                    self.dot1qstaticmulticastforbiddenegressports.yfilter != YFilter.not_set or
                    self.dot1qstaticmulticaststaticegressports.yfilter != YFilter.not_set or
                    self.dot1qstaticmulticaststatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qStaticMulticastEntry" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + "[dot1qStaticMulticastAddress='" + self.dot1qstaticmulticastaddress.get() + "']" + "[dot1qStaticMulticastReceivePort='" + self.dot1qstaticmulticastreceiveport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qStaticMulticastTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qstaticmulticastaddress.is_set or self.dot1qstaticmulticastaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticmulticastaddress.get_name_leafdata())
                if (self.dot1qstaticmulticastreceiveport.is_set or self.dot1qstaticmulticastreceiveport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticmulticastreceiveport.get_name_leafdata())
                if (self.dot1qstaticmulticastforbiddenegressports.is_set or self.dot1qstaticmulticastforbiddenegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticmulticastforbiddenegressports.get_name_leafdata())
                if (self.dot1qstaticmulticaststaticegressports.is_set or self.dot1qstaticmulticaststaticegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticmulticaststaticegressports.get_name_leafdata())
                if (self.dot1qstaticmulticaststatus.is_set or self.dot1qstaticmulticaststatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qstaticmulticaststatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanIndex" or name == "dot1qStaticMulticastAddress" or name == "dot1qStaticMulticastReceivePort" or name == "dot1qStaticMulticastForbiddenEgressPorts" or name == "dot1qStaticMulticastStaticEgressPorts" or name == "dot1qStaticMulticastStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticMulticastAddress"):
                    self.dot1qstaticmulticastaddress = value
                    self.dot1qstaticmulticastaddress.value_namespace = name_space
                    self.dot1qstaticmulticastaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticMulticastReceivePort"):
                    self.dot1qstaticmulticastreceiveport = value
                    self.dot1qstaticmulticastreceiveport.value_namespace = name_space
                    self.dot1qstaticmulticastreceiveport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticMulticastForbiddenEgressPorts"):
                    self.dot1qstaticmulticastforbiddenegressports = value
                    self.dot1qstaticmulticastforbiddenegressports.value_namespace = name_space
                    self.dot1qstaticmulticastforbiddenegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticMulticastStaticEgressPorts"):
                    self.dot1qstaticmulticaststaticegressports = value
                    self.dot1qstaticmulticaststaticegressports.value_namespace = name_space
                    self.dot1qstaticmulticaststaticegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qStaticMulticastStatus"):
                    self.dot1qstaticmulticaststatus = value
                    self.dot1qstaticmulticaststatus.value_namespace = name_space
                    self.dot1qstaticmulticaststatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qstaticmulticastentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qstaticmulticastentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qStaticMulticastTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qStaticMulticastEntry"):
                for c in self.dot1qstaticmulticastentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qstaticmulticasttable.Dot1Qstaticmulticastentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qstaticmulticastentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qStaticMulticastEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qvlancurrenttable(Entity):
        """
        A table containing current configuration information
        for each VLAN currently configured into the device by
        (local or network) management, or dynamically created
        as a result of GVRP requests received.
        
        .. attribute:: dot1qvlancurrententry
        
        	Information for a VLAN configured into the device by  (local or network) management, or dynamically created as a result of GVRP requests received
        	**type**\: list of    :py:class:`Dot1Qvlancurrententry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qvlancurrenttable, self).__init__()

            self.yang_name = "dot1qVlanCurrentTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qvlancurrententry = YList(self)

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
                        super(QBridgeMib.Dot1Qvlancurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qvlancurrenttable, self).__setattr__(name, value)


        class Dot1Qvlancurrententry(Entity):
            """
            Information for a VLAN configured into the device by
            
            (local or network) management, or dynamically created
            as a result of GVRP requests received.
            
            .. attribute:: dot1qvlantimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention to see how this works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlanindex  <key>
            
            	The VLAN\-ID or other identifier referring to this VLAN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlancreationtime
            
            	The value of sysUpTime when this VLAN was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlancurrentegressports
            
            	The set of ports that are transmitting traffic for this VLAN as either tagged or untagged frames
            	**type**\:  str
            
            .. attribute:: dot1qvlancurrentuntaggedports
            
            	The set of ports that are transmitting traffic for this VLAN as untagged frames
            	**type**\:  str
            
            .. attribute:: dot1qvlanfdbid
            
            	The Filtering Database used by this VLAN.  This is one of the dot1qFdbId values in the dot1qFdbTable.  This value is allocated automatically by the device whenever  the VLAN is created\: either dynamically by GVRP, or by management, in dot1qVlanStaticTable.  Allocation of this value follows the learning constraints defined for this VLAN in dot1qLearningConstraintsTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qvlanstatus
            
            	This object indicates the status of this entry. other(1) \- this entry is currently in use, but the     conditions under which it will remain so differ     from the following values. permanent(2) \- this entry, corresponding to an entry     in dot1qVlanStaticTable, is currently in use and     will remain so after the next reset of the     device.  The port lists for this entry include     ports from the equivalent dot1qVlanStaticTable     entry and ports learned dynamically. dynamicGvrp(3) \- this entry is currently in use      and will remain so until removed by GVRP.  There     is no static entry for this VLAN, and it will be     removed when the last port leaves the VLAN
            	**type**\:   :py:class:`Dot1Qvlanstatus <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry.Dot1Qvlanstatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry, self).__init__()

                self.yang_name = "dot1qVlanCurrentEntry"
                self.yang_parent_name = "dot1qVlanCurrentTable"

                self.dot1qvlantimemark = YLeaf(YType.uint32, "dot1qVlanTimeMark")

                self.dot1qvlanindex = YLeaf(YType.uint32, "dot1qVlanIndex")

                self.dot1qvlancreationtime = YLeaf(YType.uint32, "dot1qVlanCreationTime")

                self.dot1qvlancurrentegressports = YLeaf(YType.str, "dot1qVlanCurrentEgressPorts")

                self.dot1qvlancurrentuntaggedports = YLeaf(YType.str, "dot1qVlanCurrentUntaggedPorts")

                self.dot1qvlanfdbid = YLeaf(YType.uint32, "dot1qVlanFdbId")

                self.dot1qvlanstatus = YLeaf(YType.enumeration, "dot1qVlanStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlantimemark",
                                "dot1qvlanindex",
                                "dot1qvlancreationtime",
                                "dot1qvlancurrentegressports",
                                "dot1qvlancurrentuntaggedports",
                                "dot1qvlanfdbid",
                                "dot1qvlanstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry, self).__setattr__(name, value)

            class Dot1Qvlanstatus(Enum):
                """
                Dot1Qvlanstatus

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


            def has_data(self):
                return (
                    self.dot1qvlantimemark.is_set or
                    self.dot1qvlanindex.is_set or
                    self.dot1qvlancreationtime.is_set or
                    self.dot1qvlancurrentegressports.is_set or
                    self.dot1qvlancurrentuntaggedports.is_set or
                    self.dot1qvlanfdbid.is_set or
                    self.dot1qvlanstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlantimemark.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qvlancreationtime.yfilter != YFilter.not_set or
                    self.dot1qvlancurrentegressports.yfilter != YFilter.not_set or
                    self.dot1qvlancurrentuntaggedports.yfilter != YFilter.not_set or
                    self.dot1qvlanfdbid.yfilter != YFilter.not_set or
                    self.dot1qvlanstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qVlanCurrentEntry" + "[dot1qVlanTimeMark='" + self.dot1qvlantimemark.get() + "']" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qVlanCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlantimemark.is_set or self.dot1qvlantimemark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlantimemark.get_name_leafdata())
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qvlancreationtime.is_set or self.dot1qvlancreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlancreationtime.get_name_leafdata())
                if (self.dot1qvlancurrentegressports.is_set or self.dot1qvlancurrentegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlancurrentegressports.get_name_leafdata())
                if (self.dot1qvlancurrentuntaggedports.is_set or self.dot1qvlancurrentuntaggedports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlancurrentuntaggedports.get_name_leafdata())
                if (self.dot1qvlanfdbid.is_set or self.dot1qvlanfdbid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanfdbid.get_name_leafdata())
                if (self.dot1qvlanstatus.is_set or self.dot1qvlanstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanTimeMark" or name == "dot1qVlanIndex" or name == "dot1qVlanCreationTime" or name == "dot1qVlanCurrentEgressPorts" or name == "dot1qVlanCurrentUntaggedPorts" or name == "dot1qVlanFdbId" or name == "dot1qVlanStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanTimeMark"):
                    self.dot1qvlantimemark = value
                    self.dot1qvlantimemark.value_namespace = name_space
                    self.dot1qvlantimemark.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanCreationTime"):
                    self.dot1qvlancreationtime = value
                    self.dot1qvlancreationtime.value_namespace = name_space
                    self.dot1qvlancreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanCurrentEgressPorts"):
                    self.dot1qvlancurrentegressports = value
                    self.dot1qvlancurrentegressports.value_namespace = name_space
                    self.dot1qvlancurrentegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanCurrentUntaggedPorts"):
                    self.dot1qvlancurrentuntaggedports = value
                    self.dot1qvlancurrentuntaggedports.value_namespace = name_space
                    self.dot1qvlancurrentuntaggedports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanFdbId"):
                    self.dot1qvlanfdbid = value
                    self.dot1qvlanfdbid.value_namespace = name_space
                    self.dot1qvlanfdbid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanStatus"):
                    self.dot1qvlanstatus = value
                    self.dot1qvlanstatus.value_namespace = name_space
                    self.dot1qvlanstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qvlancurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qvlancurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qVlanCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qVlanCurrentEntry"):
                for c in self.dot1qvlancurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qvlancurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qVlanCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qvlanstatictable(Entity):
        """
        A table containing static configuration information for
        each VLAN configured into the device by (local or
        network) management.  All entries are permanent and will
        be restored after the device is reset.
        
        .. attribute:: dot1qvlanstaticentry
        
        	Static information for a VLAN configured into the device by (local or network) management
        	**type**\: list of    :py:class:`Dot1Qvlanstaticentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlanstatictable.Dot1Qvlanstaticentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qvlanstatictable, self).__init__()

            self.yang_name = "dot1qVlanStaticTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qvlanstaticentry = YList(self)

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
                        super(QBridgeMib.Dot1Qvlanstatictable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qvlanstatictable, self).__setattr__(name, value)


        class Dot1Qvlanstaticentry(Entity):
            """
            Static information for a VLAN configured into the
            device by (local or network) management.
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qvlanforbiddenegressports
            
            	The set of ports that are prohibited by management from being included in the egress list for this VLAN. Changes to this object that cause a port to be included or excluded affect the per\-port, per\-VLAN Registrar control for Registration Forbidden for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanStaticEgressPorts.  The default value of this object is a string of zeros of appropriate length, excluding all ports from the forbidden set
            	**type**\:  str
            
            .. attribute:: dot1qvlanstaticegressports
            
            	The set of ports that are permanently assigned to the egress list for this VLAN by management.  Changes to a bit in this object affect the per\-port, per\-VLAN Registrar control for Registration Fixed for the relevant GVRP state machine on each port.  A port may not be added in this set if it is already a member of the set of ports in dot1qVlanForbiddenEgressPorts.  The default value of this object is a string of zeros of appropriate length, indicating not fixed
            	**type**\:  str
            
            .. attribute:: dot1qvlanstaticname
            
            	An administratively assigned string, which may be used to identify the VLAN
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: dot1qvlanstaticrowstatus
            
            	This object indicates the status of this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: dot1qvlanstaticuntaggedports
            
            	The set of ports that should transmit egress packets for this VLAN as untagged.  The default value of this object for the default VLAN (dot1qVlanIndex = 1) is a string of appropriate length including all ports.  There is no specified default for other VLANs.  If a device agent cannot support the set of ports being set, then it will reject the set operation with an error.  For example, a manager might attempt to set more than one VLAN to be untagged on egress where the device does not support this IEEE 802.1Q option
            	**type**\:  str
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qvlanstatictable.Dot1Qvlanstaticentry, self).__init__()

                self.yang_name = "dot1qVlanStaticEntry"
                self.yang_parent_name = "dot1qVlanStaticTable"

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qvlanforbiddenegressports = YLeaf(YType.str, "dot1qVlanForbiddenEgressPorts")

                self.dot1qvlanstaticegressports = YLeaf(YType.str, "dot1qVlanStaticEgressPorts")

                self.dot1qvlanstaticname = YLeaf(YType.str, "dot1qVlanStaticName")

                self.dot1qvlanstaticrowstatus = YLeaf(YType.enumeration, "dot1qVlanStaticRowStatus")

                self.dot1qvlanstaticuntaggedports = YLeaf(YType.str, "dot1qVlanStaticUntaggedPorts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qvlanindex",
                                "dot1qvlanforbiddenegressports",
                                "dot1qvlanstaticegressports",
                                "dot1qvlanstaticname",
                                "dot1qvlanstaticrowstatus",
                                "dot1qvlanstaticuntaggedports") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qvlanstatictable.Dot1Qvlanstaticentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qvlanstatictable.Dot1Qvlanstaticentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1qvlanindex.is_set or
                    self.dot1qvlanforbiddenegressports.is_set or
                    self.dot1qvlanstaticegressports.is_set or
                    self.dot1qvlanstaticname.is_set or
                    self.dot1qvlanstaticrowstatus.is_set or
                    self.dot1qvlanstaticuntaggedports.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qvlanforbiddenegressports.yfilter != YFilter.not_set or
                    self.dot1qvlanstaticegressports.yfilter != YFilter.not_set or
                    self.dot1qvlanstaticname.yfilter != YFilter.not_set or
                    self.dot1qvlanstaticrowstatus.yfilter != YFilter.not_set or
                    self.dot1qvlanstaticuntaggedports.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qVlanStaticEntry" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qVlanStaticTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qvlanforbiddenegressports.is_set or self.dot1qvlanforbiddenegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanforbiddenegressports.get_name_leafdata())
                if (self.dot1qvlanstaticegressports.is_set or self.dot1qvlanstaticegressports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanstaticegressports.get_name_leafdata())
                if (self.dot1qvlanstaticname.is_set or self.dot1qvlanstaticname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanstaticname.get_name_leafdata())
                if (self.dot1qvlanstaticrowstatus.is_set or self.dot1qvlanstaticrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanstaticrowstatus.get_name_leafdata())
                if (self.dot1qvlanstaticuntaggedports.is_set or self.dot1qvlanstaticuntaggedports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanstaticuntaggedports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qVlanIndex" or name == "dot1qVlanForbiddenEgressPorts" or name == "dot1qVlanStaticEgressPorts" or name == "dot1qVlanStaticName" or name == "dot1qVlanStaticRowStatus" or name == "dot1qVlanStaticUntaggedPorts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanForbiddenEgressPorts"):
                    self.dot1qvlanforbiddenegressports = value
                    self.dot1qvlanforbiddenegressports.value_namespace = name_space
                    self.dot1qvlanforbiddenegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanStaticEgressPorts"):
                    self.dot1qvlanstaticegressports = value
                    self.dot1qvlanstaticegressports.value_namespace = name_space
                    self.dot1qvlanstaticegressports.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanStaticName"):
                    self.dot1qvlanstaticname = value
                    self.dot1qvlanstaticname.value_namespace = name_space
                    self.dot1qvlanstaticname.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanStaticRowStatus"):
                    self.dot1qvlanstaticrowstatus = value
                    self.dot1qvlanstaticrowstatus.value_namespace = name_space
                    self.dot1qvlanstaticrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanStaticUntaggedPorts"):
                    self.dot1qvlanstaticuntaggedports = value
                    self.dot1qvlanstaticuntaggedports.value_namespace = name_space
                    self.dot1qvlanstaticuntaggedports.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qvlanstaticentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qvlanstaticentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qVlanStaticTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qVlanStaticEntry"):
                for c in self.dot1qvlanstaticentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qvlanstatictable.Dot1Qvlanstaticentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qvlanstaticentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qVlanStaticEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qportvlanstatisticstable(Entity):
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
        	**type**\: list of    :py:class:`Dot1Qportvlanstatisticsentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qportvlanstatisticstable.Dot1Qportvlanstatisticsentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qportvlanstatisticstable, self).__init__()

            self.yang_name = "dot1qPortVlanStatisticsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qportvlanstatisticsentry = YList(self)

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
                        super(QBridgeMib.Dot1Qportvlanstatisticstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qportvlanstatisticstable, self).__setattr__(name, value)


        class Dot1Qportvlanstatisticsentry(Entity):
            """
            Traffic statistics for a VLAN on an interface.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qtpvlanportindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinoverflowdiscards
            
            	The number of times the associated dot1qTpVlanPortInDiscards counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportinoverflowframes
            
            	The number of times the associated dot1qTpVlanPortInFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qtpvlanportoutoverflowframes
            
            	The number of times the associated dot1qTpVlanPortOutFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qportvlanstatisticstable.Dot1Qportvlanstatisticsentry, self).__init__()

                self.yang_name = "dot1qPortVlanStatisticsEntry"
                self.yang_parent_name = "dot1qPortVlanStatisticsTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qtpvlanportindiscards = YLeaf(YType.uint32, "dot1qTpVlanPortInDiscards")

                self.dot1qtpvlanportinframes = YLeaf(YType.uint32, "dot1qTpVlanPortInFrames")

                self.dot1qtpvlanportinoverflowdiscards = YLeaf(YType.uint32, "dot1qTpVlanPortInOverflowDiscards")

                self.dot1qtpvlanportinoverflowframes = YLeaf(YType.uint32, "dot1qTpVlanPortInOverflowFrames")

                self.dot1qtpvlanportoutframes = YLeaf(YType.uint32, "dot1qTpVlanPortOutFrames")

                self.dot1qtpvlanportoutoverflowframes = YLeaf(YType.uint32, "dot1qTpVlanPortOutOverflowFrames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dbaseport",
                                "dot1qvlanindex",
                                "dot1qtpvlanportindiscards",
                                "dot1qtpvlanportinframes",
                                "dot1qtpvlanportinoverflowdiscards",
                                "dot1qtpvlanportinoverflowframes",
                                "dot1qtpvlanportoutframes",
                                "dot1qtpvlanportoutoverflowframes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qportvlanstatisticstable.Dot1Qportvlanstatisticsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qportvlanstatisticstable.Dot1Qportvlanstatisticsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1qvlanindex.is_set or
                    self.dot1qtpvlanportindiscards.is_set or
                    self.dot1qtpvlanportinframes.is_set or
                    self.dot1qtpvlanportinoverflowdiscards.is_set or
                    self.dot1qtpvlanportinoverflowframes.is_set or
                    self.dot1qtpvlanportoutframes.is_set or
                    self.dot1qtpvlanportoutoverflowframes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportindiscards.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportinframes.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportinoverflowdiscards.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportinoverflowframes.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportoutframes.yfilter != YFilter.not_set or
                    self.dot1qtpvlanportoutoverflowframes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qPortVlanStatisticsEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qPortVlanStatisticsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qtpvlanportindiscards.is_set or self.dot1qtpvlanportindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportindiscards.get_name_leafdata())
                if (self.dot1qtpvlanportinframes.is_set or self.dot1qtpvlanportinframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportinframes.get_name_leafdata())
                if (self.dot1qtpvlanportinoverflowdiscards.is_set or self.dot1qtpvlanportinoverflowdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportinoverflowdiscards.get_name_leafdata())
                if (self.dot1qtpvlanportinoverflowframes.is_set or self.dot1qtpvlanportinoverflowframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportinoverflowframes.get_name_leafdata())
                if (self.dot1qtpvlanportoutframes.is_set or self.dot1qtpvlanportoutframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportoutframes.get_name_leafdata())
                if (self.dot1qtpvlanportoutoverflowframes.is_set or self.dot1qtpvlanportoutoverflowframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanportoutoverflowframes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1qVlanIndex" or name == "dot1qTpVlanPortInDiscards" or name == "dot1qTpVlanPortInFrames" or name == "dot1qTpVlanPortInOverflowDiscards" or name == "dot1qTpVlanPortInOverflowFrames" or name == "dot1qTpVlanPortOutFrames" or name == "dot1qTpVlanPortOutOverflowFrames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortInDiscards"):
                    self.dot1qtpvlanportindiscards = value
                    self.dot1qtpvlanportindiscards.value_namespace = name_space
                    self.dot1qtpvlanportindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortInFrames"):
                    self.dot1qtpvlanportinframes = value
                    self.dot1qtpvlanportinframes.value_namespace = name_space
                    self.dot1qtpvlanportinframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortInOverflowDiscards"):
                    self.dot1qtpvlanportinoverflowdiscards = value
                    self.dot1qtpvlanportinoverflowdiscards.value_namespace = name_space
                    self.dot1qtpvlanportinoverflowdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortInOverflowFrames"):
                    self.dot1qtpvlanportinoverflowframes = value
                    self.dot1qtpvlanportinoverflowframes.value_namespace = name_space
                    self.dot1qtpvlanportinoverflowframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortOutFrames"):
                    self.dot1qtpvlanportoutframes = value
                    self.dot1qtpvlanportoutframes.value_namespace = name_space
                    self.dot1qtpvlanportoutframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortOutOverflowFrames"):
                    self.dot1qtpvlanportoutoverflowframes = value
                    self.dot1qtpvlanportoutoverflowframes.value_namespace = name_space
                    self.dot1qtpvlanportoutoverflowframes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qportvlanstatisticsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qportvlanstatisticsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qPortVlanStatisticsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qPortVlanStatisticsEntry"):
                for c in self.dot1qportvlanstatisticsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qportvlanstatisticstable.Dot1Qportvlanstatisticsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qportvlanstatisticsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qPortVlanStatisticsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qportvlanhcstatisticstable(Entity):
        """
        A table containing per\-port, per\-VLAN statistics for
        traffic on high\-capacity interfaces.
        
        .. attribute:: dot1qportvlanhcstatisticsentry
        
        	Traffic statistics for a VLAN on a high\-capacity interface
        	**type**\: list of    :py:class:`Dot1Qportvlanhcstatisticsentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qportvlanhcstatisticstable.Dot1Qportvlanhcstatisticsentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qportvlanhcstatisticstable, self).__init__()

            self.yang_name = "dot1qPortVlanHCStatisticsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qportvlanhcstatisticsentry = YList(self)

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
                        super(QBridgeMib.Dot1Qportvlanhcstatisticstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qportvlanhcstatisticstable, self).__setattr__(name, value)


        class Dot1Qportvlanhcstatisticsentry(Entity):
            """
            Traffic statistics for a VLAN on a high\-capacity
            interface.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1qvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qvlancurrenttable.Dot1Qvlancurrententry>`
            
            .. attribute:: dot1qtpvlanporthcindiscards
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN and that were discarded due to VLAN\-related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1qtpvlanporthcinframes
            
            	The number of valid frames received by this port from its segment that were classified as belonging to this VLAN.  Note that a frame received on this port is counted by this object if and only if it is for a  protocol being processed by the local forwarding process for this VLAN.  This object includes received bridge management frames classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1qtpvlanporthcoutframes
            
            	The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN.  This includes bridge management frames originated by this device that are classified as belonging to this VLAN (e.g., GMRP, but not GVRP or STP)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qportvlanhcstatisticstable.Dot1Qportvlanhcstatisticsentry, self).__init__()

                self.yang_name = "dot1qPortVlanHCStatisticsEntry"
                self.yang_parent_name = "dot1qPortVlanHCStatisticsTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1qvlanindex = YLeaf(YType.str, "dot1qVlanIndex")

                self.dot1qtpvlanporthcindiscards = YLeaf(YType.uint64, "dot1qTpVlanPortHCInDiscards")

                self.dot1qtpvlanporthcinframes = YLeaf(YType.uint64, "dot1qTpVlanPortHCInFrames")

                self.dot1qtpvlanporthcoutframes = YLeaf(YType.uint64, "dot1qTpVlanPortHCOutFrames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dbaseport",
                                "dot1qvlanindex",
                                "dot1qtpvlanporthcindiscards",
                                "dot1qtpvlanporthcinframes",
                                "dot1qtpvlanporthcoutframes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qportvlanhcstatisticstable.Dot1Qportvlanhcstatisticsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qportvlanhcstatisticstable.Dot1Qportvlanhcstatisticsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1qvlanindex.is_set or
                    self.dot1qtpvlanporthcindiscards.is_set or
                    self.dot1qtpvlanporthcinframes.is_set or
                    self.dot1qtpvlanporthcoutframes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1qvlanindex.yfilter != YFilter.not_set or
                    self.dot1qtpvlanporthcindiscards.yfilter != YFilter.not_set or
                    self.dot1qtpvlanporthcinframes.yfilter != YFilter.not_set or
                    self.dot1qtpvlanporthcoutframes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qPortVlanHCStatisticsEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1qVlanIndex='" + self.dot1qvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qPortVlanHCStatisticsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1qvlanindex.is_set or self.dot1qvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qvlanindex.get_name_leafdata())
                if (self.dot1qtpvlanporthcindiscards.is_set or self.dot1qtpvlanporthcindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanporthcindiscards.get_name_leafdata())
                if (self.dot1qtpvlanporthcinframes.is_set or self.dot1qtpvlanporthcinframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanporthcinframes.get_name_leafdata())
                if (self.dot1qtpvlanporthcoutframes.is_set or self.dot1qtpvlanporthcoutframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qtpvlanporthcoutframes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1qVlanIndex" or name == "dot1qTpVlanPortHCInDiscards" or name == "dot1qTpVlanPortHCInFrames" or name == "dot1qTpVlanPortHCOutFrames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qVlanIndex"):
                    self.dot1qvlanindex = value
                    self.dot1qvlanindex.value_namespace = name_space
                    self.dot1qvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortHCInDiscards"):
                    self.dot1qtpvlanporthcindiscards = value
                    self.dot1qtpvlanporthcindiscards.value_namespace = name_space
                    self.dot1qtpvlanporthcindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortHCInFrames"):
                    self.dot1qtpvlanporthcinframes = value
                    self.dot1qtpvlanporthcinframes.value_namespace = name_space
                    self.dot1qtpvlanporthcinframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qTpVlanPortHCOutFrames"):
                    self.dot1qtpvlanporthcoutframes = value
                    self.dot1qtpvlanporthcoutframes.value_namespace = name_space
                    self.dot1qtpvlanporthcoutframes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qportvlanhcstatisticsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qportvlanhcstatisticsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qPortVlanHCStatisticsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qPortVlanHCStatisticsEntry"):
                for c in self.dot1qportvlanhcstatisticsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qportvlanhcstatisticstable.Dot1Qportvlanhcstatisticsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qportvlanhcstatisticsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qPortVlanHCStatisticsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Qlearningconstraintstable(Entity):
        """
        A table containing learning constraints for sets of
        Shared and Independent VLANs.
        
        .. attribute:: dot1qlearningconstraintsentry
        
        	A learning constraint defined for a VLAN
        	**type**\: list of    :py:class:`Dot1Qlearningconstraintsentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Qlearningconstraintstable, self).__init__()

            self.yang_name = "dot1qLearningConstraintsTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1qlearningconstraintsentry = YList(self)

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
                        super(QBridgeMib.Dot1Qlearningconstraintstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Qlearningconstraintstable, self).__setattr__(name, value)


        class Dot1Qlearningconstraintsentry(Entity):
            """
            A learning constraint defined for a VLAN.
            
            .. attribute:: dot1qconstraintvlan  <key>
            
            	The index of the row in dot1qVlanCurrentTable for the VLAN constrained by this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qconstraintset  <key>
            
            	The identity of the constraint set to which dot1qConstraintVlan belongs.  These values may be chosen by the management station
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1qconstraintstatus
            
            	The status of this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: dot1qconstrainttype
            
            	The type of constraint this entry defines. independent(1) \- the VLAN, dot1qConstraintVlan,     uses a filtering database independent from all     other VLANs in the same set, defined by     dot1qConstraintSet. shared(2) \- the VLAN, dot1qConstraintVlan, shares     the same filtering database as all other VLANs     in the same set, defined by dot1qConstraintSet
            	**type**\:   :py:class:`Dot1Qconstrainttype <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry.Dot1Qconstrainttype>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry, self).__init__()

                self.yang_name = "dot1qLearningConstraintsEntry"
                self.yang_parent_name = "dot1qLearningConstraintsTable"

                self.dot1qconstraintvlan = YLeaf(YType.uint32, "dot1qConstraintVlan")

                self.dot1qconstraintset = YLeaf(YType.int32, "dot1qConstraintSet")

                self.dot1qconstraintstatus = YLeaf(YType.enumeration, "dot1qConstraintStatus")

                self.dot1qconstrainttype = YLeaf(YType.enumeration, "dot1qConstraintType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1qconstraintvlan",
                                "dot1qconstraintset",
                                "dot1qconstraintstatus",
                                "dot1qconstrainttype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry, self).__setattr__(name, value)

            class Dot1Qconstrainttype(Enum):
                """
                Dot1Qconstrainttype

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


            def has_data(self):
                return (
                    self.dot1qconstraintvlan.is_set or
                    self.dot1qconstraintset.is_set or
                    self.dot1qconstraintstatus.is_set or
                    self.dot1qconstrainttype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1qconstraintvlan.yfilter != YFilter.not_set or
                    self.dot1qconstraintset.yfilter != YFilter.not_set or
                    self.dot1qconstraintstatus.yfilter != YFilter.not_set or
                    self.dot1qconstrainttype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1qLearningConstraintsEntry" + "[dot1qConstraintVlan='" + self.dot1qconstraintvlan.get() + "']" + "[dot1qConstraintSet='" + self.dot1qconstraintset.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1qLearningConstraintsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1qconstraintvlan.is_set or self.dot1qconstraintvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qconstraintvlan.get_name_leafdata())
                if (self.dot1qconstraintset.is_set or self.dot1qconstraintset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qconstraintset.get_name_leafdata())
                if (self.dot1qconstraintstatus.is_set or self.dot1qconstraintstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qconstraintstatus.get_name_leafdata())
                if (self.dot1qconstrainttype.is_set or self.dot1qconstrainttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qconstrainttype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1qConstraintVlan" or name == "dot1qConstraintSet" or name == "dot1qConstraintStatus" or name == "dot1qConstraintType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1qConstraintVlan"):
                    self.dot1qconstraintvlan = value
                    self.dot1qconstraintvlan.value_namespace = name_space
                    self.dot1qconstraintvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qConstraintSet"):
                    self.dot1qconstraintset = value
                    self.dot1qconstraintset.value_namespace = name_space
                    self.dot1qconstraintset.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qConstraintStatus"):
                    self.dot1qconstraintstatus = value
                    self.dot1qconstraintstatus.value_namespace = name_space
                    self.dot1qconstraintstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qConstraintType"):
                    self.dot1qconstrainttype = value
                    self.dot1qconstrainttype.value_namespace = name_space
                    self.dot1qconstrainttype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1qlearningconstraintsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1qlearningconstraintsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1qLearningConstraintsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1qLearningConstraintsEntry"):
                for c in self.dot1qlearningconstraintsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Qlearningconstraintstable.Dot1Qlearningconstraintsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1qlearningconstraintsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1qLearningConstraintsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Vprotocolgrouptable(Entity):
        """
        A table that contains mappings from Protocol
        Templates to Protocol Group Identifiers used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolgroupentry
        
        	A mapping from a Protocol Template to a Protocol Group Identifier
        	**type**\: list of    :py:class:`Dot1Vprotocolgroupentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Vprotocolgrouptable, self).__init__()

            self.yang_name = "dot1vProtocolGroupTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1vprotocolgroupentry = YList(self)

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
                        super(QBridgeMib.Dot1Vprotocolgrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Vprotocolgrouptable, self).__setattr__(name, value)


        class Dot1Vprotocolgroupentry(Entity):
            """
            A mapping from a Protocol Template to a Protocol
            Group Identifier.
            
            .. attribute:: dot1vprotocoltemplateframetype  <key>
            
            	The data\-link encapsulation format or the 'detagged\_frame\_type' in a Protocol Template
            	**type**\:   :py:class:`Dot1Vprotocoltemplateframetype <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry.Dot1Vprotocoltemplateframetype>`
            
            .. attribute:: dot1vprotocoltemplateprotocolvalue  <key>
            
            	The identification of the protocol above the data\-link layer in a Protocol Template.  Depending on the frame type, the octet string will have one of the following values\:  For 'ethernet', 'rfc1042' and 'snap8021H',     this is the 16\-bit (2\-octet) IEEE 802.3 Type Field. For 'snapOther',     this is the 40\-bit (5\-octet) PID. For 'llcOther',     this is the 2\-octet IEEE 802.2 Link Service Access     Point (LSAP) pair\: first octet for Destination Service     Access Point (DSAP) and second octet for Source Service     Access Point (SSAP)
            	**type**\:  str
            
            	**length:** 2 \| 5
            
            .. attribute:: dot1vprotocolgroupid
            
            	Represents a group of protocols that are associated together when assigning a VID to a frame
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1vprotocolgrouprowstatus
            
            	This object indicates the status of this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry, self).__init__()

                self.yang_name = "dot1vProtocolGroupEntry"
                self.yang_parent_name = "dot1vProtocolGroupTable"

                self.dot1vprotocoltemplateframetype = YLeaf(YType.enumeration, "dot1vProtocolTemplateFrameType")

                self.dot1vprotocoltemplateprotocolvalue = YLeaf(YType.str, "dot1vProtocolTemplateProtocolValue")

                self.dot1vprotocolgroupid = YLeaf(YType.int32, "dot1vProtocolGroupId")

                self.dot1vprotocolgrouprowstatus = YLeaf(YType.enumeration, "dot1vProtocolGroupRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1vprotocoltemplateframetype",
                                "dot1vprotocoltemplateprotocolvalue",
                                "dot1vprotocolgroupid",
                                "dot1vprotocolgrouprowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry, self).__setattr__(name, value)

            class Dot1Vprotocoltemplateframetype(Enum):
                """
                Dot1Vprotocoltemplateframetype

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


            def has_data(self):
                return (
                    self.dot1vprotocoltemplateframetype.is_set or
                    self.dot1vprotocoltemplateprotocolvalue.is_set or
                    self.dot1vprotocolgroupid.is_set or
                    self.dot1vprotocolgrouprowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1vprotocoltemplateframetype.yfilter != YFilter.not_set or
                    self.dot1vprotocoltemplateprotocolvalue.yfilter != YFilter.not_set or
                    self.dot1vprotocolgroupid.yfilter != YFilter.not_set or
                    self.dot1vprotocolgrouprowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1vProtocolGroupEntry" + "[dot1vProtocolTemplateFrameType='" + self.dot1vprotocoltemplateframetype.get() + "']" + "[dot1vProtocolTemplateProtocolValue='" + self.dot1vprotocoltemplateprotocolvalue.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1vProtocolGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1vprotocoltemplateframetype.is_set or self.dot1vprotocoltemplateframetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocoltemplateframetype.get_name_leafdata())
                if (self.dot1vprotocoltemplateprotocolvalue.is_set or self.dot1vprotocoltemplateprotocolvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocoltemplateprotocolvalue.get_name_leafdata())
                if (self.dot1vprotocolgroupid.is_set or self.dot1vprotocolgroupid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocolgroupid.get_name_leafdata())
                if (self.dot1vprotocolgrouprowstatus.is_set or self.dot1vprotocolgrouprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocolgrouprowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1vProtocolTemplateFrameType" or name == "dot1vProtocolTemplateProtocolValue" or name == "dot1vProtocolGroupId" or name == "dot1vProtocolGroupRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1vProtocolTemplateFrameType"):
                    self.dot1vprotocoltemplateframetype = value
                    self.dot1vprotocoltemplateframetype.value_namespace = name_space
                    self.dot1vprotocoltemplateframetype.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolTemplateProtocolValue"):
                    self.dot1vprotocoltemplateprotocolvalue = value
                    self.dot1vprotocoltemplateprotocolvalue.value_namespace = name_space
                    self.dot1vprotocoltemplateprotocolvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolGroupId"):
                    self.dot1vprotocolgroupid = value
                    self.dot1vprotocolgroupid.value_namespace = name_space
                    self.dot1vprotocolgroupid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolGroupRowStatus"):
                    self.dot1vprotocolgrouprowstatus = value
                    self.dot1vprotocolgrouprowstatus.value_namespace = name_space
                    self.dot1vprotocolgrouprowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1vprotocolgroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1vprotocolgroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1vProtocolGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1vProtocolGroupEntry"):
                for c in self.dot1vprotocolgroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Vprotocolgrouptable.Dot1Vprotocolgroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1vprotocolgroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1vProtocolGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Vprotocolporttable(Entity):
        """
        A table that contains VID sets used for
        Port\-and\-Protocol\-based VLAN Classification.
        
        .. attribute:: dot1vprotocolportentry
        
        	A VID set for a port
        	**type**\: list of    :py:class:`Dot1Vprotocolportentry <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBridgeMib.Dot1Vprotocolporttable.Dot1Vprotocolportentry>`
        
        

        """

        _prefix = 'Q-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(QBridgeMib.Dot1Vprotocolporttable, self).__init__()

            self.yang_name = "dot1vProtocolPortTable"
            self.yang_parent_name = "Q-BRIDGE-MIB"

            self.dot1vprotocolportentry = YList(self)

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
                        super(QBridgeMib.Dot1Vprotocolporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(QBridgeMib.Dot1Vprotocolporttable, self).__setattr__(name, value)


        class Dot1Vprotocolportentry(Entity):
            """
            A VID set for a port.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1vprotocolportgroupid  <key>
            
            	Designates a group of protocols in the Protocol Group Database
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1vprotocolportgroupvid
            
            	The VID associated with a group of protocols for each port
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: dot1vprotocolportrowstatus
            
            	This object indicates the status of this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'Q-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(QBridgeMib.Dot1Vprotocolporttable.Dot1Vprotocolportentry, self).__init__()

                self.yang_name = "dot1vProtocolPortEntry"
                self.yang_parent_name = "dot1vProtocolPortTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1vprotocolportgroupid = YLeaf(YType.int32, "dot1vProtocolPortGroupId")

                self.dot1vprotocolportgroupvid = YLeaf(YType.int32, "dot1vProtocolPortGroupVid")

                self.dot1vprotocolportrowstatus = YLeaf(YType.enumeration, "dot1vProtocolPortRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dbaseport",
                                "dot1vprotocolportgroupid",
                                "dot1vprotocolportgroupvid",
                                "dot1vprotocolportrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(QBridgeMib.Dot1Vprotocolporttable.Dot1Vprotocolportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(QBridgeMib.Dot1Vprotocolporttable.Dot1Vprotocolportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1vprotocolportgroupid.is_set or
                    self.dot1vprotocolportgroupvid.is_set or
                    self.dot1vprotocolportrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1vprotocolportgroupid.yfilter != YFilter.not_set or
                    self.dot1vprotocolportgroupvid.yfilter != YFilter.not_set or
                    self.dot1vprotocolportrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1vProtocolPortEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1vProtocolPortGroupId='" + self.dot1vprotocolportgroupid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/dot1vProtocolPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1vprotocolportgroupid.is_set or self.dot1vprotocolportgroupid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocolportgroupid.get_name_leafdata())
                if (self.dot1vprotocolportgroupvid.is_set or self.dot1vprotocolportgroupvid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocolportgroupvid.get_name_leafdata())
                if (self.dot1vprotocolportrowstatus.is_set or self.dot1vprotocolportrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1vprotocolportrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1vProtocolPortGroupId" or name == "dot1vProtocolPortGroupVid" or name == "dot1vProtocolPortRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolPortGroupId"):
                    self.dot1vprotocolportgroupid = value
                    self.dot1vprotocolportgroupid.value_namespace = name_space
                    self.dot1vprotocolportgroupid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolPortGroupVid"):
                    self.dot1vprotocolportgroupvid = value
                    self.dot1vprotocolportgroupvid.value_namespace = name_space
                    self.dot1vprotocolportgroupvid.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1vProtocolPortRowStatus"):
                    self.dot1vprotocolportrowstatus = value
                    self.dot1vprotocolportrowstatus.value_namespace = name_space
                    self.dot1vprotocolportrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1vprotocolportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1vprotocolportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1vProtocolPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1vProtocolPortEntry"):
                for c in self.dot1vprotocolportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = QBridgeMib.Dot1Vprotocolporttable.Dot1Vprotocolportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1vprotocolportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1vProtocolPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dot1qbase is not None and self.dot1qbase.has_data()) or
            (self.dot1qfdbtable is not None and self.dot1qfdbtable.has_data()) or
            (self.dot1qforwardalltable is not None and self.dot1qforwardalltable.has_data()) or
            (self.dot1qforwardunregisteredtable is not None and self.dot1qforwardunregisteredtable.has_data()) or
            (self.dot1qlearningconstraintstable is not None and self.dot1qlearningconstraintstable.has_data()) or
            (self.dot1qportvlanhcstatisticstable is not None and self.dot1qportvlanhcstatisticstable.has_data()) or
            (self.dot1qportvlanstatisticstable is not None and self.dot1qportvlanstatisticstable.has_data()) or
            (self.dot1qstaticmulticasttable is not None and self.dot1qstaticmulticasttable.has_data()) or
            (self.dot1qstaticunicasttable is not None and self.dot1qstaticunicasttable.has_data()) or
            (self.dot1qtpfdbtable is not None and self.dot1qtpfdbtable.has_data()) or
            (self.dot1qtpgrouptable is not None and self.dot1qtpgrouptable.has_data()) or
            (self.dot1qvlan is not None and self.dot1qvlan.has_data()) or
            (self.dot1qvlancurrenttable is not None and self.dot1qvlancurrenttable.has_data()) or
            (self.dot1qvlanstatictable is not None and self.dot1qvlanstatictable.has_data()) or
            (self.dot1vprotocolgrouptable is not None and self.dot1vprotocolgrouptable.has_data()) or
            (self.dot1vprotocolporttable is not None and self.dot1vprotocolporttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dot1qbase is not None and self.dot1qbase.has_operation()) or
            (self.dot1qfdbtable is not None and self.dot1qfdbtable.has_operation()) or
            (self.dot1qforwardalltable is not None and self.dot1qforwardalltable.has_operation()) or
            (self.dot1qforwardunregisteredtable is not None and self.dot1qforwardunregisteredtable.has_operation()) or
            (self.dot1qlearningconstraintstable is not None and self.dot1qlearningconstraintstable.has_operation()) or
            (self.dot1qportvlanhcstatisticstable is not None and self.dot1qportvlanhcstatisticstable.has_operation()) or
            (self.dot1qportvlanstatisticstable is not None and self.dot1qportvlanstatisticstable.has_operation()) or
            (self.dot1qstaticmulticasttable is not None and self.dot1qstaticmulticasttable.has_operation()) or
            (self.dot1qstaticunicasttable is not None and self.dot1qstaticunicasttable.has_operation()) or
            (self.dot1qtpfdbtable is not None and self.dot1qtpfdbtable.has_operation()) or
            (self.dot1qtpgrouptable is not None and self.dot1qtpgrouptable.has_operation()) or
            (self.dot1qvlan is not None and self.dot1qvlan.has_operation()) or
            (self.dot1qvlancurrenttable is not None and self.dot1qvlancurrenttable.has_operation()) or
            (self.dot1qvlanstatictable is not None and self.dot1qvlanstatictable.has_operation()) or
            (self.dot1vprotocolgrouptable is not None and self.dot1vprotocolgrouptable.has_operation()) or
            (self.dot1vprotocolporttable is not None and self.dot1vprotocolporttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Q-BRIDGE-MIB:Q-BRIDGE-MIB" + path_buffer

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

        if (child_yang_name == "dot1qBase"):
            if (self.dot1qbase is None):
                self.dot1qbase = QBridgeMib.Dot1Qbase()
                self.dot1qbase.parent = self
                self._children_name_map["dot1qbase"] = "dot1qBase"
            return self.dot1qbase

        if (child_yang_name == "dot1qFdbTable"):
            if (self.dot1qfdbtable is None):
                self.dot1qfdbtable = QBridgeMib.Dot1Qfdbtable()
                self.dot1qfdbtable.parent = self
                self._children_name_map["dot1qfdbtable"] = "dot1qFdbTable"
            return self.dot1qfdbtable

        if (child_yang_name == "dot1qForwardAllTable"):
            if (self.dot1qforwardalltable is None):
                self.dot1qforwardalltable = QBridgeMib.Dot1Qforwardalltable()
                self.dot1qforwardalltable.parent = self
                self._children_name_map["dot1qforwardalltable"] = "dot1qForwardAllTable"
            return self.dot1qforwardalltable

        if (child_yang_name == "dot1qForwardUnregisteredTable"):
            if (self.dot1qforwardunregisteredtable is None):
                self.dot1qforwardunregisteredtable = QBridgeMib.Dot1Qforwardunregisteredtable()
                self.dot1qforwardunregisteredtable.parent = self
                self._children_name_map["dot1qforwardunregisteredtable"] = "dot1qForwardUnregisteredTable"
            return self.dot1qforwardunregisteredtable

        if (child_yang_name == "dot1qLearningConstraintsTable"):
            if (self.dot1qlearningconstraintstable is None):
                self.dot1qlearningconstraintstable = QBridgeMib.Dot1Qlearningconstraintstable()
                self.dot1qlearningconstraintstable.parent = self
                self._children_name_map["dot1qlearningconstraintstable"] = "dot1qLearningConstraintsTable"
            return self.dot1qlearningconstraintstable

        if (child_yang_name == "dot1qPortVlanHCStatisticsTable"):
            if (self.dot1qportvlanhcstatisticstable is None):
                self.dot1qportvlanhcstatisticstable = QBridgeMib.Dot1Qportvlanhcstatisticstable()
                self.dot1qportvlanhcstatisticstable.parent = self
                self._children_name_map["dot1qportvlanhcstatisticstable"] = "dot1qPortVlanHCStatisticsTable"
            return self.dot1qportvlanhcstatisticstable

        if (child_yang_name == "dot1qPortVlanStatisticsTable"):
            if (self.dot1qportvlanstatisticstable is None):
                self.dot1qportvlanstatisticstable = QBridgeMib.Dot1Qportvlanstatisticstable()
                self.dot1qportvlanstatisticstable.parent = self
                self._children_name_map["dot1qportvlanstatisticstable"] = "dot1qPortVlanStatisticsTable"
            return self.dot1qportvlanstatisticstable

        if (child_yang_name == "dot1qStaticMulticastTable"):
            if (self.dot1qstaticmulticasttable is None):
                self.dot1qstaticmulticasttable = QBridgeMib.Dot1Qstaticmulticasttable()
                self.dot1qstaticmulticasttable.parent = self
                self._children_name_map["dot1qstaticmulticasttable"] = "dot1qStaticMulticastTable"
            return self.dot1qstaticmulticasttable

        if (child_yang_name == "dot1qStaticUnicastTable"):
            if (self.dot1qstaticunicasttable is None):
                self.dot1qstaticunicasttable = QBridgeMib.Dot1Qstaticunicasttable()
                self.dot1qstaticunicasttable.parent = self
                self._children_name_map["dot1qstaticunicasttable"] = "dot1qStaticUnicastTable"
            return self.dot1qstaticunicasttable

        if (child_yang_name == "dot1qTpFdbTable"):
            if (self.dot1qtpfdbtable is None):
                self.dot1qtpfdbtable = QBridgeMib.Dot1Qtpfdbtable()
                self.dot1qtpfdbtable.parent = self
                self._children_name_map["dot1qtpfdbtable"] = "dot1qTpFdbTable"
            return self.dot1qtpfdbtable

        if (child_yang_name == "dot1qTpGroupTable"):
            if (self.dot1qtpgrouptable is None):
                self.dot1qtpgrouptable = QBridgeMib.Dot1Qtpgrouptable()
                self.dot1qtpgrouptable.parent = self
                self._children_name_map["dot1qtpgrouptable"] = "dot1qTpGroupTable"
            return self.dot1qtpgrouptable

        if (child_yang_name == "dot1qVlan"):
            if (self.dot1qvlan is None):
                self.dot1qvlan = QBridgeMib.Dot1Qvlan()
                self.dot1qvlan.parent = self
                self._children_name_map["dot1qvlan"] = "dot1qVlan"
            return self.dot1qvlan

        if (child_yang_name == "dot1qVlanCurrentTable"):
            if (self.dot1qvlancurrenttable is None):
                self.dot1qvlancurrenttable = QBridgeMib.Dot1Qvlancurrenttable()
                self.dot1qvlancurrenttable.parent = self
                self._children_name_map["dot1qvlancurrenttable"] = "dot1qVlanCurrentTable"
            return self.dot1qvlancurrenttable

        if (child_yang_name == "dot1qVlanStaticTable"):
            if (self.dot1qvlanstatictable is None):
                self.dot1qvlanstatictable = QBridgeMib.Dot1Qvlanstatictable()
                self.dot1qvlanstatictable.parent = self
                self._children_name_map["dot1qvlanstatictable"] = "dot1qVlanStaticTable"
            return self.dot1qvlanstatictable

        if (child_yang_name == "dot1vProtocolGroupTable"):
            if (self.dot1vprotocolgrouptable is None):
                self.dot1vprotocolgrouptable = QBridgeMib.Dot1Vprotocolgrouptable()
                self.dot1vprotocolgrouptable.parent = self
                self._children_name_map["dot1vprotocolgrouptable"] = "dot1vProtocolGroupTable"
            return self.dot1vprotocolgrouptable

        if (child_yang_name == "dot1vProtocolPortTable"):
            if (self.dot1vprotocolporttable is None):
                self.dot1vprotocolporttable = QBridgeMib.Dot1Vprotocolporttable()
                self.dot1vprotocolporttable.parent = self
                self._children_name_map["dot1vprotocolporttable"] = "dot1vProtocolPortTable"
            return self.dot1vprotocolporttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dot1qBase" or name == "dot1qFdbTable" or name == "dot1qForwardAllTable" or name == "dot1qForwardUnregisteredTable" or name == "dot1qLearningConstraintsTable" or name == "dot1qPortVlanHCStatisticsTable" or name == "dot1qPortVlanStatisticsTable" or name == "dot1qStaticMulticastTable" or name == "dot1qStaticUnicastTable" or name == "dot1qTpFdbTable" or name == "dot1qTpGroupTable" or name == "dot1qVlan" or name == "dot1qVlanCurrentTable" or name == "dot1qVlanStaticTable" or name == "dot1vProtocolGroupTable" or name == "dot1vProtocolPortTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = QBridgeMib()
        return self._top_entity

