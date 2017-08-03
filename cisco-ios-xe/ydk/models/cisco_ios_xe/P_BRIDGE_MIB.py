""" P_BRIDGE_MIB 

The Bridge MIB Extension module for managing Priority
and Multicast Filtering, defined by IEEE 802.1D\-1998,
including Restricted Group Registration defined by
IEEE 802.1t\-2001.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4363; See the RFC itself for
full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Enabledstatus(Enum):
    """
    Enabledstatus

    A simple status value for the object.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



class PBridgeMib(Entity):
    """
    
    
    .. attribute:: dot1dextbase
    
    	
    	**type**\:   :py:class:`Dot1Dextbase <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dextbase>`
    
    .. attribute:: dot1dportoutboundaccessprioritytable
    
    	A table mapping Regenerated User Priority to Outbound Access Priority.  This is a fixed mapping for all port types, with two options for 802.5 Token Ring
    	**type**\:   :py:class:`Dot1Dportoutboundaccessprioritytable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dportoutboundaccessprioritytable>`
    
    .. attribute:: dot1dtphcporttable
    
    	A table that contains information about every high\- capacity port that is associated with this transparent bridge
    	**type**\:   :py:class:`Dot1Dtphcporttable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtphcporttable>`
    
    .. attribute:: dot1dtpportoverflowtable
    
    	A table that contains the most\-significant bits of statistics counters for ports that are associated with this transparent bridge that are on high\-capacity interfaces, as defined in the conformance clauses for this table.  This table is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\-significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling.  The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or asynchronous notification
    	**type**\:   :py:class:`Dot1Dtpportoverflowtable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtpportoverflowtable>`
    
    .. attribute:: dot1dtrafficclasstable
    
    	A table mapping evaluated User Priority to Traffic Class, for forwarding by the bridge.  Traffic class is a number in the range (0..(dot1dPortNumTrafficClasses\-1))
    	**type**\:   :py:class:`Dot1Dtrafficclasstable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtrafficclasstable>`
    
    .. attribute:: dot1duserpriorityregentable
    
    	A list of Regenerated User Priorities for each received User Priority on each port of a bridge.  The Regenerated User Priority value may be used to index the Traffic Class Table for each input port.  This only has effect on media that support native User Priority.  The default values for Regenerated User Priorities are the same as the User Priorities
    	**type**\:   :py:class:`Dot1Duserpriorityregentable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable>`
    
    

    """

    _prefix = 'P-BRIDGE-MIB'
    _revision = '2006-01-09'

    def __init__(self):
        super(PBridgeMib, self).__init__()
        self._top_entity = None

        self.yang_name = "P-BRIDGE-MIB"
        self.yang_parent_name = "P-BRIDGE-MIB"

        self.dot1dextbase = PBridgeMib.Dot1Dextbase()
        self.dot1dextbase.parent = self
        self._children_name_map["dot1dextbase"] = "dot1dExtBase"
        self._children_yang_names.add("dot1dExtBase")

        self.dot1dportoutboundaccessprioritytable = PBridgeMib.Dot1Dportoutboundaccessprioritytable()
        self.dot1dportoutboundaccessprioritytable.parent = self
        self._children_name_map["dot1dportoutboundaccessprioritytable"] = "dot1dPortOutboundAccessPriorityTable"
        self._children_yang_names.add("dot1dPortOutboundAccessPriorityTable")

        self.dot1dtphcporttable = PBridgeMib.Dot1Dtphcporttable()
        self.dot1dtphcporttable.parent = self
        self._children_name_map["dot1dtphcporttable"] = "dot1dTpHCPortTable"
        self._children_yang_names.add("dot1dTpHCPortTable")

        self.dot1dtpportoverflowtable = PBridgeMib.Dot1Dtpportoverflowtable()
        self.dot1dtpportoverflowtable.parent = self
        self._children_name_map["dot1dtpportoverflowtable"] = "dot1dTpPortOverflowTable"
        self._children_yang_names.add("dot1dTpPortOverflowTable")

        self.dot1dtrafficclasstable = PBridgeMib.Dot1Dtrafficclasstable()
        self.dot1dtrafficclasstable.parent = self
        self._children_name_map["dot1dtrafficclasstable"] = "dot1dTrafficClassTable"
        self._children_yang_names.add("dot1dTrafficClassTable")

        self.dot1duserpriorityregentable = PBridgeMib.Dot1Duserpriorityregentable()
        self.dot1duserpriorityregentable.parent = self
        self._children_name_map["dot1duserpriorityregentable"] = "dot1dUserPriorityRegenTable"
        self._children_yang_names.add("dot1dUserPriorityRegenTable")


    class Dot1Dextbase(Entity):
        """
        
        
        .. attribute:: dot1ddevicecapabilities
        
        	Indicates the optional parts of IEEE 802.1D and 802.1Q that are implemented by this device and are manageable through this MIB.  Capabilities that are allowed on a per\-port basis are indicated in dot1dPortCapabilities.  dot1dExtendedFilteringServices(0),                       \-\- can perform filtering of                       \-\- individual multicast addresses                       \-\- controlled by GMRP. dot1dTrafficClasses(1),                       \-\- can map user priority to                       \-\- multiple traffic classes. dot1qStaticEntryIndividualPort(2),                       \-\- dot1qStaticUnicastReceivePort &                       \-\- dot1qStaticMulticastReceivePort                       \-\- can represent non\-zero entries. dot1qIVLCapable(3),   \-\- Independent VLAN Learning (IVL). dot1qSVLCapable(4),   \-\- Shared VLAN Learning (SVL). dot1qHybridCapable(5),                       \-\- both IVL & SVL simultaneously. dot1qConfigurablePvidTagging(6),                       \-\- whether the implementation                       \-\- supports the ability to                       \-\- override the default PVID                       \-\- setting and its egress status                       \-\- (VLAN\-Tagged or Untagged) on                       \-\- each port. dot1dLocalVlanCapable(7)                       \-\- can support multiple local                       \-\- bridges, outside of the scope                       \-\- of 802.1Q defined VLANs
        	**type**\:   :py:class:`Dot1Ddevicecapabilities <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dextbase.Dot1Ddevicecapabilities>`
        
        .. attribute:: dot1dgmrpstatus
        
        	The administrative status requested by management for GMRP.  The value enabled(1) indicates that GMRP should be enabled on this device, in all VLANs, on all ports for which it has not been specifically disabled.  When disabled(2), GMRP is disabled, in all VLANs and on all ports, and all GMRP packets will be forwarded transparently.  This object affects both Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:   :py:class:`Enabledstatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.Enabledstatus>`
        
        .. attribute:: dot1dtrafficclassesenabled
        
        	The value true(1) indicates that Traffic Classes are enabled on this bridge.  When false(2), the bridge operates with a single priority level for all traffic.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:  bool
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Dextbase, self).__init__()

            self.yang_name = "dot1dExtBase"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1ddevicecapabilities = YLeaf(YType.bits, "dot1dDeviceCapabilities")

            self.dot1dgmrpstatus = YLeaf(YType.enumeration, "dot1dGmrpStatus")

            self.dot1dtrafficclassesenabled = YLeaf(YType.boolean, "dot1dTrafficClassesEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1ddevicecapabilities",
                            "dot1dgmrpstatus",
                            "dot1dtrafficclassesenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PBridgeMib.Dot1Dextbase, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Dextbase, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.dot1ddevicecapabilities.is_set or
                self.dot1dgmrpstatus.is_set or
                self.dot1dtrafficclassesenabled.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1ddevicecapabilities.yfilter != YFilter.not_set or
                self.dot1dgmrpstatus.yfilter != YFilter.not_set or
                self.dot1dtrafficclassesenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dExtBase" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1ddevicecapabilities.is_set or self.dot1ddevicecapabilities.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1ddevicecapabilities.get_name_leafdata())
            if (self.dot1dgmrpstatus.is_set or self.dot1dgmrpstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dgmrpstatus.get_name_leafdata())
            if (self.dot1dtrafficclassesenabled.is_set or self.dot1dtrafficclassesenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dtrafficclassesenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dDeviceCapabilities" or name == "dot1dGmrpStatus" or name == "dot1dTrafficClassesEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1dDeviceCapabilities"):
                self.dot1ddevicecapabilities[value] = True
            if(value_path == "dot1dGmrpStatus"):
                self.dot1dgmrpstatus = value
                self.dot1dgmrpstatus.value_namespace = name_space
                self.dot1dgmrpstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dTrafficClassesEnabled"):
                self.dot1dtrafficclassesenabled = value
                self.dot1dtrafficclassesenabled.value_namespace = name_space
                self.dot1dtrafficclassesenabled.value_namespace_prefix = name_space_prefix


    class Dot1Dtphcporttable(Entity):
        """
        A table that contains information about every high\-
        capacity port that is associated with this transparent
        bridge.
        
        .. attribute:: dot1dtphcportentry
        
        	Statistics information for each high\-capacity port of a transparent bridge
        	**type**\: list of    :py:class:`Dot1Dtphcportentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Dtphcporttable, self).__init__()

            self.yang_name = "dot1dTpHCPortTable"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1dtphcportentry = YList(self)

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
                        super(PBridgeMib.Dot1Dtphcporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Dtphcporttable, self).__setattr__(name, value)


        class Dot1Dtphcportentry(Entity):
            """
            Statistics information for each high\-capacity port of a
            transparent bridge.
            
            .. attribute:: dot1dtpport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtphcportindiscards
            
            	Count of valid frames that have been received by this port from its segment that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry, self).__init__()

                self.yang_name = "dot1dTpHCPortEntry"
                self.yang_parent_name = "dot1dTpHCPortTable"

                self.dot1dtpport = YLeaf(YType.str, "dot1dTpPort")

                self.dot1dtphcportindiscards = YLeaf(YType.uint64, "dot1dTpHCPortInDiscards")

                self.dot1dtphcportinframes = YLeaf(YType.uint64, "dot1dTpHCPortInFrames")

                self.dot1dtphcportoutframes = YLeaf(YType.uint64, "dot1dTpHCPortOutFrames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dtpport",
                                "dot1dtphcportindiscards",
                                "dot1dtphcportinframes",
                                "dot1dtphcportoutframes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dtpport.is_set or
                    self.dot1dtphcportindiscards.is_set or
                    self.dot1dtphcportinframes.is_set or
                    self.dot1dtphcportoutframes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dtpport.yfilter != YFilter.not_set or
                    self.dot1dtphcportindiscards.yfilter != YFilter.not_set or
                    self.dot1dtphcportinframes.yfilter != YFilter.not_set or
                    self.dot1dtphcportoutframes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dTpHCPortEntry" + "[dot1dTpPort='" + self.dot1dtpport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTpHCPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dtpport.is_set or self.dot1dtpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpport.get_name_leafdata())
                if (self.dot1dtphcportindiscards.is_set or self.dot1dtphcportindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtphcportindiscards.get_name_leafdata())
                if (self.dot1dtphcportinframes.is_set or self.dot1dtphcportinframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtphcportinframes.get_name_leafdata())
                if (self.dot1dtphcportoutframes.is_set or self.dot1dtphcportoutframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtphcportoutframes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dTpPort" or name == "dot1dTpHCPortInDiscards" or name == "dot1dTpHCPortInFrames" or name == "dot1dTpHCPortOutFrames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dTpPort"):
                    self.dot1dtpport = value
                    self.dot1dtpport.value_namespace = name_space
                    self.dot1dtpport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpHCPortInDiscards"):
                    self.dot1dtphcportindiscards = value
                    self.dot1dtphcportindiscards.value_namespace = name_space
                    self.dot1dtphcportindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpHCPortInFrames"):
                    self.dot1dtphcportinframes = value
                    self.dot1dtphcportinframes.value_namespace = name_space
                    self.dot1dtphcportinframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpHCPortOutFrames"):
                    self.dot1dtphcportoutframes = value
                    self.dot1dtphcportoutframes.value_namespace = name_space
                    self.dot1dtphcportoutframes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dtphcportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dtphcportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTpHCPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dTpHCPortEntry"):
                for c in self.dot1dtphcportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dtphcportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTpHCPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dtpportoverflowtable(Entity):
        """
        A table that contains the most\-significant bits of
        statistics counters for ports that are associated with this
        transparent bridge that are on high\-capacity interfaces, as
        defined in the conformance clauses for this table.  This table
        is provided as a way to read 64\-bit counters for agents that
        support only SNMPv1.
        
        Note that the reporting of most\-significant and
        least\-significant counter bits separately runs the risk of
        missing an overflow of the lower bits in the interval between
        sampling.  The manager must be aware of this possibility, even
        within the same varbindlist, when interpreting the results of
        a request or asynchronous notification.
        
        .. attribute:: dot1dtpportoverflowentry
        
        	The most significant bits of statistics counters for a high\- capacity interface of a transparent bridge.  Each object is associated with a corresponding object in dot1dTpPortTable that indicates the least significant bits of the counter
        	**type**\: list of    :py:class:`Dot1Dtpportoverflowentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Dtpportoverflowtable, self).__init__()

            self.yang_name = "dot1dTpPortOverflowTable"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1dtpportoverflowentry = YList(self)

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
                        super(PBridgeMib.Dot1Dtpportoverflowtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Dtpportoverflowtable, self).__setattr__(name, value)


        class Dot1Dtpportoverflowentry(Entity):
            """
            The most significant bits of statistics counters for a high\-
            capacity interface of a transparent bridge.  Each object is
            associated with a corresponding object in dot1dTpPortTable
            that indicates the least significant bits of the counter.
            
            .. attribute:: dot1dtpport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtpportinoverflowdiscards
            
            	The number of times the associated dot1dTpPortInDiscards counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportinoverflowframes
            
            	The number of times the associated dot1dTpPortInFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportoutoverflowframes
            
            	The number of times the associated dot1dTpPortOutFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry, self).__init__()

                self.yang_name = "dot1dTpPortOverflowEntry"
                self.yang_parent_name = "dot1dTpPortOverflowTable"

                self.dot1dtpport = YLeaf(YType.str, "dot1dTpPort")

                self.dot1dtpportinoverflowdiscards = YLeaf(YType.uint32, "dot1dTpPortInOverflowDiscards")

                self.dot1dtpportinoverflowframes = YLeaf(YType.uint32, "dot1dTpPortInOverflowFrames")

                self.dot1dtpportoutoverflowframes = YLeaf(YType.uint32, "dot1dTpPortOutOverflowFrames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dtpport",
                                "dot1dtpportinoverflowdiscards",
                                "dot1dtpportinoverflowframes",
                                "dot1dtpportoutoverflowframes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dtpport.is_set or
                    self.dot1dtpportinoverflowdiscards.is_set or
                    self.dot1dtpportinoverflowframes.is_set or
                    self.dot1dtpportoutoverflowframes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dtpport.yfilter != YFilter.not_set or
                    self.dot1dtpportinoverflowdiscards.yfilter != YFilter.not_set or
                    self.dot1dtpportinoverflowframes.yfilter != YFilter.not_set or
                    self.dot1dtpportoutoverflowframes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dTpPortOverflowEntry" + "[dot1dTpPort='" + self.dot1dtpport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTpPortOverflowTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dtpport.is_set or self.dot1dtpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpport.get_name_leafdata())
                if (self.dot1dtpportinoverflowdiscards.is_set or self.dot1dtpportinoverflowdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportinoverflowdiscards.get_name_leafdata())
                if (self.dot1dtpportinoverflowframes.is_set or self.dot1dtpportinoverflowframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportinoverflowframes.get_name_leafdata())
                if (self.dot1dtpportoutoverflowframes.is_set or self.dot1dtpportoutoverflowframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportoutoverflowframes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dTpPort" or name == "dot1dTpPortInOverflowDiscards" or name == "dot1dTpPortInOverflowFrames" or name == "dot1dTpPortOutOverflowFrames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dTpPort"):
                    self.dot1dtpport = value
                    self.dot1dtpport.value_namespace = name_space
                    self.dot1dtpport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortInOverflowDiscards"):
                    self.dot1dtpportinoverflowdiscards = value
                    self.dot1dtpportinoverflowdiscards.value_namespace = name_space
                    self.dot1dtpportinoverflowdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortInOverflowFrames"):
                    self.dot1dtpportinoverflowframes = value
                    self.dot1dtpportinoverflowframes.value_namespace = name_space
                    self.dot1dtpportinoverflowframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortOutOverflowFrames"):
                    self.dot1dtpportoutoverflowframes = value
                    self.dot1dtpportoutoverflowframes.value_namespace = name_space
                    self.dot1dtpportoutoverflowframes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dtpportoverflowentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dtpportoverflowentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTpPortOverflowTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dTpPortOverflowEntry"):
                for c in self.dot1dtpportoverflowentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dtpportoverflowentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTpPortOverflowEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Duserpriorityregentable(Entity):
        """
        A list of Regenerated User Priorities for each received
        User Priority on each port of a bridge.  The Regenerated
        User Priority value may be used to index the Traffic
        Class Table for each input port.  This only has effect
        on media that support native User Priority.  The default
        values for Regenerated User Priorities are the same as
        the User Priorities.
        
        .. attribute:: dot1duserpriorityregenentry
        
        	A mapping of incoming User Priority to a Regenerated User Priority
        	**type**\: list of    :py:class:`Dot1Duserpriorityregenentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Duserpriorityregentable, self).__init__()

            self.yang_name = "dot1dUserPriorityRegenTable"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1duserpriorityregenentry = YList(self)

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
                        super(PBridgeMib.Dot1Duserpriorityregentable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Duserpriorityregentable, self).__setattr__(name, value)


        class Dot1Duserpriorityregenentry(Entity):
            """
            A mapping of incoming User Priority to a Regenerated
            User Priority.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1duserpriority  <key>
            
            	The User Priority for a frame received on this port
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dregenuserpriority
            
            	The Regenerated User Priority that the incoming User  Priority is mapped to for this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry, self).__init__()

                self.yang_name = "dot1dUserPriorityRegenEntry"
                self.yang_parent_name = "dot1dUserPriorityRegenTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1duserpriority = YLeaf(YType.int32, "dot1dUserPriority")

                self.dot1dregenuserpriority = YLeaf(YType.int32, "dot1dRegenUserPriority")

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
                                "dot1duserpriority",
                                "dot1dregenuserpriority") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1duserpriority.is_set or
                    self.dot1dregenuserpriority.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1duserpriority.yfilter != YFilter.not_set or
                    self.dot1dregenuserpriority.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dUserPriorityRegenEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1dUserPriority='" + self.dot1duserpriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dUserPriorityRegenTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1duserpriority.is_set or self.dot1duserpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1duserpriority.get_name_leafdata())
                if (self.dot1dregenuserpriority.is_set or self.dot1dregenuserpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dregenuserpriority.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1dUserPriority" or name == "dot1dRegenUserPriority"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dUserPriority"):
                    self.dot1duserpriority = value
                    self.dot1duserpriority.value_namespace = name_space
                    self.dot1duserpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dRegenUserPriority"):
                    self.dot1dregenuserpriority = value
                    self.dot1dregenuserpriority.value_namespace = name_space
                    self.dot1dregenuserpriority.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1duserpriorityregenentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1duserpriorityregenentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dUserPriorityRegenTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dUserPriorityRegenEntry"):
                for c in self.dot1duserpriorityregenentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1duserpriorityregenentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dUserPriorityRegenEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dtrafficclasstable(Entity):
        """
        A table mapping evaluated User Priority to Traffic
        Class, for forwarding by the bridge.  Traffic class is a
        number in the range (0..(dot1dPortNumTrafficClasses\-1)).
        
        .. attribute:: dot1dtrafficclassentry
        
        	User Priority to Traffic Class mapping
        	**type**\: list of    :py:class:`Dot1Dtrafficclassentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Dtrafficclasstable, self).__init__()

            self.yang_name = "dot1dTrafficClassTable"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1dtrafficclassentry = YList(self)

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
                        super(PBridgeMib.Dot1Dtrafficclasstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Dtrafficclasstable, self).__setattr__(name, value)


        class Dot1Dtrafficclassentry(Entity):
            """
            User Priority to Traffic Class mapping.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dtrafficclasspriority  <key>
            
            	The Priority value determined for the received frame. This value is equivalent to the priority indicated in the tagged frame received, or one of the evaluated priorities, determined according to the media\-type.  For untagged frames received from Ethernet media, this value is equal to the dot1dPortDefaultUserPriority value for the ingress port.  For untagged frames received from non\-Ethernet media, this value is equal to the dot1dRegenUserPriority value for the ingress port and media\-specific user priority
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dtrafficclass
            
            	The Traffic Class the received frame is mapped to.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry, self).__init__()

                self.yang_name = "dot1dTrafficClassEntry"
                self.yang_parent_name = "dot1dTrafficClassTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1dtrafficclasspriority = YLeaf(YType.int32, "dot1dTrafficClassPriority")

                self.dot1dtrafficclass = YLeaf(YType.int32, "dot1dTrafficClass")

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
                                "dot1dtrafficclasspriority",
                                "dot1dtrafficclass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1dtrafficclasspriority.is_set or
                    self.dot1dtrafficclass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1dtrafficclasspriority.yfilter != YFilter.not_set or
                    self.dot1dtrafficclass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dTrafficClassEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1dTrafficClassPriority='" + self.dot1dtrafficclasspriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTrafficClassTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1dtrafficclasspriority.is_set or self.dot1dtrafficclasspriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtrafficclasspriority.get_name_leafdata())
                if (self.dot1dtrafficclass.is_set or self.dot1dtrafficclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtrafficclass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1dTrafficClassPriority" or name == "dot1dTrafficClass"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTrafficClassPriority"):
                    self.dot1dtrafficclasspriority = value
                    self.dot1dtrafficclasspriority.value_namespace = name_space
                    self.dot1dtrafficclasspriority.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTrafficClass"):
                    self.dot1dtrafficclass = value
                    self.dot1dtrafficclass.value_namespace = name_space
                    self.dot1dtrafficclass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dtrafficclassentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dtrafficclassentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTrafficClassTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dTrafficClassEntry"):
                for c in self.dot1dtrafficclassentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dtrafficclassentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTrafficClassEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dportoutboundaccessprioritytable(Entity):
        """
        A table mapping Regenerated User Priority to Outbound
        Access Priority.  This is a fixed mapping for all port
        types, with two options for 802.5 Token Ring.
        
        .. attribute:: dot1dportoutboundaccesspriorityentry
        
        	Regenerated User Priority to Outbound Access Priority mapping
        	**type**\: list of    :py:class:`Dot1Dportoutboundaccesspriorityentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBridgeMib.Dot1Dportoutboundaccessprioritytable, self).__init__()

            self.yang_name = "dot1dPortOutboundAccessPriorityTable"
            self.yang_parent_name = "P-BRIDGE-MIB"

            self.dot1dportoutboundaccesspriorityentry = YList(self)

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
                        super(PBridgeMib.Dot1Dportoutboundaccessprioritytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PBridgeMib.Dot1Dportoutboundaccessprioritytable, self).__setattr__(name, value)


        class Dot1Dportoutboundaccesspriorityentry(Entity):
            """
            Regenerated User Priority to Outbound Access Priority
            mapping.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dregenuserpriority  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..7
            
            	**refers to**\:  :py:class:`dot1dregenuserpriority <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
            
            .. attribute:: dot1dportoutboundaccesspriority
            
            	The Outbound Access Priority the received frame is mapped to
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry, self).__init__()

                self.yang_name = "dot1dPortOutboundAccessPriorityEntry"
                self.yang_parent_name = "dot1dPortOutboundAccessPriorityTable"

                self.dot1dbaseport = YLeaf(YType.str, "dot1dBasePort")

                self.dot1dregenuserpriority = YLeaf(YType.str, "dot1dRegenUserPriority")

                self.dot1dportoutboundaccesspriority = YLeaf(YType.int32, "dot1dPortOutboundAccessPriority")

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
                                "dot1dregenuserpriority",
                                "dot1dportoutboundaccesspriority") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1dregenuserpriority.is_set or
                    self.dot1dportoutboundaccesspriority.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1dregenuserpriority.yfilter != YFilter.not_set or
                    self.dot1dportoutboundaccesspriority.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dPortOutboundAccessPriorityEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + "[dot1dRegenUserPriority='" + self.dot1dregenuserpriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dPortOutboundAccessPriorityTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1dregenuserpriority.is_set or self.dot1dregenuserpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dregenuserpriority.get_name_leafdata())
                if (self.dot1dportoutboundaccesspriority.is_set or self.dot1dportoutboundaccesspriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportoutboundaccesspriority.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1dRegenUserPriority" or name == "dot1dPortOutboundAccessPriority"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dRegenUserPriority"):
                    self.dot1dregenuserpriority = value
                    self.dot1dregenuserpriority.value_namespace = name_space
                    self.dot1dregenuserpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortOutboundAccessPriority"):
                    self.dot1dportoutboundaccesspriority = value
                    self.dot1dportoutboundaccesspriority.value_namespace = name_space
                    self.dot1dportoutboundaccesspriority.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dportoutboundaccesspriorityentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dportoutboundaccesspriorityentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dPortOutboundAccessPriorityTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dPortOutboundAccessPriorityEntry"):
                for c in self.dot1dportoutboundaccesspriorityentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dportoutboundaccesspriorityentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dPortOutboundAccessPriorityEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dot1dextbase is not None and self.dot1dextbase.has_data()) or
            (self.dot1dportoutboundaccessprioritytable is not None and self.dot1dportoutboundaccessprioritytable.has_data()) or
            (self.dot1dtphcporttable is not None and self.dot1dtphcporttable.has_data()) or
            (self.dot1dtpportoverflowtable is not None and self.dot1dtpportoverflowtable.has_data()) or
            (self.dot1dtrafficclasstable is not None and self.dot1dtrafficclasstable.has_data()) or
            (self.dot1duserpriorityregentable is not None and self.dot1duserpriorityregentable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dot1dextbase is not None and self.dot1dextbase.has_operation()) or
            (self.dot1dportoutboundaccessprioritytable is not None and self.dot1dportoutboundaccessprioritytable.has_operation()) or
            (self.dot1dtphcporttable is not None and self.dot1dtphcporttable.has_operation()) or
            (self.dot1dtpportoverflowtable is not None and self.dot1dtpportoverflowtable.has_operation()) or
            (self.dot1dtrafficclasstable is not None and self.dot1dtrafficclasstable.has_operation()) or
            (self.dot1duserpriorityregentable is not None and self.dot1duserpriorityregentable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "P-BRIDGE-MIB:P-BRIDGE-MIB" + path_buffer

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

        if (child_yang_name == "dot1dExtBase"):
            if (self.dot1dextbase is None):
                self.dot1dextbase = PBridgeMib.Dot1Dextbase()
                self.dot1dextbase.parent = self
                self._children_name_map["dot1dextbase"] = "dot1dExtBase"
            return self.dot1dextbase

        if (child_yang_name == "dot1dPortOutboundAccessPriorityTable"):
            if (self.dot1dportoutboundaccessprioritytable is None):
                self.dot1dportoutboundaccessprioritytable = PBridgeMib.Dot1Dportoutboundaccessprioritytable()
                self.dot1dportoutboundaccessprioritytable.parent = self
                self._children_name_map["dot1dportoutboundaccessprioritytable"] = "dot1dPortOutboundAccessPriorityTable"
            return self.dot1dportoutboundaccessprioritytable

        if (child_yang_name == "dot1dTpHCPortTable"):
            if (self.dot1dtphcporttable is None):
                self.dot1dtphcporttable = PBridgeMib.Dot1Dtphcporttable()
                self.dot1dtphcporttable.parent = self
                self._children_name_map["dot1dtphcporttable"] = "dot1dTpHCPortTable"
            return self.dot1dtphcporttable

        if (child_yang_name == "dot1dTpPortOverflowTable"):
            if (self.dot1dtpportoverflowtable is None):
                self.dot1dtpportoverflowtable = PBridgeMib.Dot1Dtpportoverflowtable()
                self.dot1dtpportoverflowtable.parent = self
                self._children_name_map["dot1dtpportoverflowtable"] = "dot1dTpPortOverflowTable"
            return self.dot1dtpportoverflowtable

        if (child_yang_name == "dot1dTrafficClassTable"):
            if (self.dot1dtrafficclasstable is None):
                self.dot1dtrafficclasstable = PBridgeMib.Dot1Dtrafficclasstable()
                self.dot1dtrafficclasstable.parent = self
                self._children_name_map["dot1dtrafficclasstable"] = "dot1dTrafficClassTable"
            return self.dot1dtrafficclasstable

        if (child_yang_name == "dot1dUserPriorityRegenTable"):
            if (self.dot1duserpriorityregentable is None):
                self.dot1duserpriorityregentable = PBridgeMib.Dot1Duserpriorityregentable()
                self.dot1duserpriorityregentable.parent = self
                self._children_name_map["dot1duserpriorityregentable"] = "dot1dUserPriorityRegenTable"
            return self.dot1duserpriorityregentable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dot1dExtBase" or name == "dot1dPortOutboundAccessPriorityTable" or name == "dot1dTpHCPortTable" or name == "dot1dTpPortOverflowTable" or name == "dot1dTrafficClassTable" or name == "dot1dUserPriorityRegenTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PBridgeMib()
        return self._top_entity

