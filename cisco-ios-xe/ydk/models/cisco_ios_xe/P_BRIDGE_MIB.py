""" P_BRIDGE_MIB 

The Bridge MIB Extension module for managing Priority
and Multicast Filtering, defined by IEEE 802.1D\-1998,
including Restricted Group Registration defined by
IEEE 802.1t\-2001.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4363; See the RFC itself for
full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EnabledStatus(Enum):
    """
    EnabledStatus (Enum Class)

    A simple status value for the object.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



class PBRIDGEMIB(Entity):
    """
    
    
    .. attribute:: dot1dextbase
    
    	
    	**type**\:  :py:class:`Dot1Dextbase <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dextbase>`
    
    .. attribute:: dot1dtphcporttable
    
    	A table that contains information about every high\- capacity port that is associated with this transparent bridge
    	**type**\:  :py:class:`Dot1Dtphcporttable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtphcporttable>`
    
    .. attribute:: dot1dtpportoverflowtable
    
    	A table that contains the most\-significant bits of statistics counters for ports that are associated with this transparent bridge that are on high\-capacity interfaces, as defined in the conformance clauses for this table.  This table is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\-significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling.  The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or asynchronous notification
    	**type**\:  :py:class:`Dot1Dtpportoverflowtable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtpportoverflowtable>`
    
    .. attribute:: dot1duserpriorityregentable
    
    	A list of Regenerated User Priorities for each received User Priority on each port of a bridge.  The Regenerated User Priority value may be used to index the Traffic Class Table for each input port.  This only has effect on media that support native User Priority.  The default values for Regenerated User Priorities are the same as the User Priorities
    	**type**\:  :py:class:`Dot1Duserpriorityregentable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Duserpriorityregentable>`
    
    .. attribute:: dot1dtrafficclasstable
    
    	A table mapping evaluated User Priority to Traffic Class, for forwarding by the bridge.  Traffic class is a number in the range (0..(dot1dPortNumTrafficClasses\-1))
    	**type**\:  :py:class:`Dot1Dtrafficclasstable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtrafficclasstable>`
    
    .. attribute:: dot1dportoutboundaccessprioritytable
    
    	A table mapping Regenerated User Priority to Outbound Access Priority.  This is a fixed mapping for all port types, with two options for 802.5 Token Ring
    	**type**\:  :py:class:`Dot1Dportoutboundaccessprioritytable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable>`
    
    

    """

    _prefix = 'P-BRIDGE-MIB'
    _revision = '2006-01-09'

    def __init__(self):
        super(PBRIDGEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "P-BRIDGE-MIB"
        self.yang_parent_name = "P-BRIDGE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("dot1dExtBase", ("dot1dextbase", PBRIDGEMIB.Dot1Dextbase)), ("dot1dTpHCPortTable", ("dot1dtphcporttable", PBRIDGEMIB.Dot1Dtphcporttable)), ("dot1dTpPortOverflowTable", ("dot1dtpportoverflowtable", PBRIDGEMIB.Dot1Dtpportoverflowtable)), ("dot1dUserPriorityRegenTable", ("dot1duserpriorityregentable", PBRIDGEMIB.Dot1Duserpriorityregentable)), ("dot1dTrafficClassTable", ("dot1dtrafficclasstable", PBRIDGEMIB.Dot1Dtrafficclasstable)), ("dot1dPortOutboundAccessPriorityTable", ("dot1dportoutboundaccessprioritytable", PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.dot1dextbase = PBRIDGEMIB.Dot1Dextbase()
        self.dot1dextbase.parent = self
        self._children_name_map["dot1dextbase"] = "dot1dExtBase"
        self._children_yang_names.add("dot1dExtBase")

        self.dot1dtphcporttable = PBRIDGEMIB.Dot1Dtphcporttable()
        self.dot1dtphcporttable.parent = self
        self._children_name_map["dot1dtphcporttable"] = "dot1dTpHCPortTable"
        self._children_yang_names.add("dot1dTpHCPortTable")

        self.dot1dtpportoverflowtable = PBRIDGEMIB.Dot1Dtpportoverflowtable()
        self.dot1dtpportoverflowtable.parent = self
        self._children_name_map["dot1dtpportoverflowtable"] = "dot1dTpPortOverflowTable"
        self._children_yang_names.add("dot1dTpPortOverflowTable")

        self.dot1duserpriorityregentable = PBRIDGEMIB.Dot1Duserpriorityregentable()
        self.dot1duserpriorityregentable.parent = self
        self._children_name_map["dot1duserpriorityregentable"] = "dot1dUserPriorityRegenTable"
        self._children_yang_names.add("dot1dUserPriorityRegenTable")

        self.dot1dtrafficclasstable = PBRIDGEMIB.Dot1Dtrafficclasstable()
        self.dot1dtrafficclasstable.parent = self
        self._children_name_map["dot1dtrafficclasstable"] = "dot1dTrafficClassTable"
        self._children_yang_names.add("dot1dTrafficClassTable")

        self.dot1dportoutboundaccessprioritytable = PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable()
        self.dot1dportoutboundaccessprioritytable.parent = self
        self._children_name_map["dot1dportoutboundaccessprioritytable"] = "dot1dPortOutboundAccessPriorityTable"
        self._children_yang_names.add("dot1dPortOutboundAccessPriorityTable")
        self._segment_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB"


    class Dot1Dextbase(Entity):
        """
        
        
        .. attribute:: dot1ddevicecapabilities
        
        	Indicates the optional parts of IEEE 802.1D and 802.1Q that are implemented by this device and are manageable through this MIB.  Capabilities that are allowed on a per\-port basis are indicated in dot1dPortCapabilities.  dot1dExtendedFilteringServices(0),                       \-\- can perform filtering of                       \-\- individual multicast addresses                       \-\- controlled by GMRP. dot1dTrafficClasses(1),                       \-\- can map user priority to                       \-\- multiple traffic classes. dot1qStaticEntryIndividualPort(2),                       \-\- dot1qStaticUnicastReceivePort &                       \-\- dot1qStaticMulticastReceivePort                       \-\- can represent non\-zero entries. dot1qIVLCapable(3),   \-\- Independent VLAN Learning (IVL). dot1qSVLCapable(4),   \-\- Shared VLAN Learning (SVL). dot1qHybridCapable(5),                       \-\- both IVL & SVL simultaneously. dot1qConfigurablePvidTagging(6),                       \-\- whether the implementation                       \-\- supports the ability to                       \-\- override the default PVID                       \-\- setting and its egress status                       \-\- (VLAN\-Tagged or Untagged) on                       \-\- each port. dot1dLocalVlanCapable(7)                       \-\- can support multiple local                       \-\- bridges, outside of the scope                       \-\- of 802.1Q defined VLANs
        	**type**\:  :py:class:`Dot1Ddevicecapabilities <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dextbase.Dot1Ddevicecapabilities>`
        
        .. attribute:: dot1dtrafficclassesenabled
        
        	The value true(1) indicates that Traffic Classes are enabled on this bridge.  When false(2), the bridge operates with a single priority level for all traffic.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\: bool
        
        .. attribute:: dot1dgmrpstatus
        
        	The administrative status requested by management for GMRP.  The value enabled(1) indicates that GMRP should be enabled on this device, in all VLANs, on all ports for which it has not been specifically disabled.  When disabled(2), GMRP is disabled, in all VLANs and on all ports, and all GMRP packets will be forwarded transparently.  This object affects both Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:  :py:class:`EnabledStatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledStatus>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Dextbase, self).__init__()

            self.yang_name = "dot1dExtBase"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1ddevicecapabilities', YLeaf(YType.bits, 'dot1dDeviceCapabilities')),
                ('dot1dtrafficclassesenabled', YLeaf(YType.boolean, 'dot1dTrafficClassesEnabled')),
                ('dot1dgmrpstatus', YLeaf(YType.enumeration, 'dot1dGmrpStatus')),
            ])
            self.dot1ddevicecapabilities = Bits()
            self.dot1dtrafficclassesenabled = None
            self.dot1dgmrpstatus = None
            self._segment_path = lambda: "dot1dExtBase"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Dextbase, ['dot1ddevicecapabilities', 'dot1dtrafficclassesenabled', 'dot1dgmrpstatus'], name, value)


    class Dot1Dtphcporttable(Entity):
        """
        A table that contains information about every high\-
        capacity port that is associated with this transparent
        bridge.
        
        .. attribute:: dot1dtphcportentry
        
        	Statistics information for each high\-capacity port of a transparent bridge
        	**type**\: list of  		 :py:class:`Dot1Dtphcportentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtphcporttable.Dot1Dtphcportentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Dtphcporttable, self).__init__()

            self.yang_name = "dot1dTpHCPortTable"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dTpHCPortEntry", ("dot1dtphcportentry", PBRIDGEMIB.Dot1Dtphcporttable.Dot1Dtphcportentry))])
            self._leafs = OrderedDict()

            self.dot1dtphcportentry = YList(self)
            self._segment_path = lambda: "dot1dTpHCPortTable"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Dtphcporttable, [], name, value)


        class Dot1Dtphcportentry(Entity):
            """
            Statistics information for each high\-capacity port of a
            transparent bridge.
            
            .. attribute:: dot1dtpport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtphcportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportindiscards
            
            	Count of valid frames that have been received by this port from its segment that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBRIDGEMIB.Dot1Dtphcporttable.Dot1Dtphcportentry, self).__init__()

                self.yang_name = "dot1dTpHCPortEntry"
                self.yang_parent_name = "dot1dTpHCPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dtpport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dtpport', YLeaf(YType.str, 'dot1dTpPort')),
                    ('dot1dtphcportinframes', YLeaf(YType.uint64, 'dot1dTpHCPortInFrames')),
                    ('dot1dtphcportoutframes', YLeaf(YType.uint64, 'dot1dTpHCPortOutFrames')),
                    ('dot1dtphcportindiscards', YLeaf(YType.uint64, 'dot1dTpHCPortInDiscards')),
                ])
                self.dot1dtpport = None
                self.dot1dtphcportinframes = None
                self.dot1dtphcportoutframes = None
                self.dot1dtphcportindiscards = None
                self._segment_path = lambda: "dot1dTpHCPortEntry" + "[dot1dTpPort='" + str(self.dot1dtpport) + "']"
                self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTpHCPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PBRIDGEMIB.Dot1Dtphcporttable.Dot1Dtphcportentry, ['dot1dtpport', 'dot1dtphcportinframes', 'dot1dtphcportoutframes', 'dot1dtphcportindiscards'], name, value)


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
        	**type**\: list of  		 :py:class:`Dot1Dtpportoverflowentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Dtpportoverflowtable, self).__init__()

            self.yang_name = "dot1dTpPortOverflowTable"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dTpPortOverflowEntry", ("dot1dtpportoverflowentry", PBRIDGEMIB.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry))])
            self._leafs = OrderedDict()

            self.dot1dtpportoverflowentry = YList(self)
            self._segment_path = lambda: "dot1dTpPortOverflowTable"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Dtpportoverflowtable, [], name, value)


        class Dot1Dtpportoverflowentry(Entity):
            """
            The most significant bits of statistics counters for a high\-
            capacity interface of a transparent bridge.  Each object is
            associated with a corresponding object in dot1dTpPortTable
            that indicates the least significant bits of the counter.
            
            .. attribute:: dot1dtpport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtpportinoverflowframes
            
            	The number of times the associated dot1dTpPortInFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportoutoverflowframes
            
            	The number of times the associated dot1dTpPortOutFrames counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportinoverflowdiscards
            
            	The number of times the associated dot1dTpPortInDiscards counter has overflowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBRIDGEMIB.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry, self).__init__()

                self.yang_name = "dot1dTpPortOverflowEntry"
                self.yang_parent_name = "dot1dTpPortOverflowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dtpport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dtpport', YLeaf(YType.str, 'dot1dTpPort')),
                    ('dot1dtpportinoverflowframes', YLeaf(YType.uint32, 'dot1dTpPortInOverflowFrames')),
                    ('dot1dtpportoutoverflowframes', YLeaf(YType.uint32, 'dot1dTpPortOutOverflowFrames')),
                    ('dot1dtpportinoverflowdiscards', YLeaf(YType.uint32, 'dot1dTpPortInOverflowDiscards')),
                ])
                self.dot1dtpport = None
                self.dot1dtpportinoverflowframes = None
                self.dot1dtpportoutoverflowframes = None
                self.dot1dtpportinoverflowdiscards = None
                self._segment_path = lambda: "dot1dTpPortOverflowEntry" + "[dot1dTpPort='" + str(self.dot1dtpport) + "']"
                self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTpPortOverflowTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PBRIDGEMIB.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry, ['dot1dtpport', 'dot1dtpportinoverflowframes', 'dot1dtpportoutoverflowframes', 'dot1dtpportinoverflowdiscards'], name, value)


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
        	**type**\: list of  		 :py:class:`Dot1Duserpriorityregenentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Duserpriorityregentable, self).__init__()

            self.yang_name = "dot1dUserPriorityRegenTable"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dUserPriorityRegenEntry", ("dot1duserpriorityregenentry", PBRIDGEMIB.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry))])
            self._leafs = OrderedDict()

            self.dot1duserpriorityregenentry = YList(self)
            self._segment_path = lambda: "dot1dUserPriorityRegenTable"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Duserpriorityregentable, [], name, value)


        class Dot1Duserpriorityregenentry(Entity):
            """
            A mapping of incoming User Priority to a Regenerated
            User Priority.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1duserpriority  (key)
            
            	The User Priority for a frame received on this port
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1dregenuserpriority
            
            	The Regenerated User Priority that the incoming User  Priority is mapped to for this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBRIDGEMIB.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry, self).__init__()

                self.yang_name = "dot1dUserPriorityRegenEntry"
                self.yang_parent_name = "dot1dUserPriorityRegenTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1duserpriority']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', YLeaf(YType.str, 'dot1dBasePort')),
                    ('dot1duserpriority', YLeaf(YType.int32, 'dot1dUserPriority')),
                    ('dot1dregenuserpriority', YLeaf(YType.int32, 'dot1dRegenUserPriority')),
                ])
                self.dot1dbaseport = None
                self.dot1duserpriority = None
                self.dot1dregenuserpriority = None
                self._segment_path = lambda: "dot1dUserPriorityRegenEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1dUserPriority='" + str(self.dot1duserpriority) + "']"
                self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dUserPriorityRegenTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PBRIDGEMIB.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry, ['dot1dbaseport', 'dot1duserpriority', 'dot1dregenuserpriority'], name, value)


    class Dot1Dtrafficclasstable(Entity):
        """
        A table mapping evaluated User Priority to Traffic
        Class, for forwarding by the bridge.  Traffic class is a
        number in the range (0..(dot1dPortNumTrafficClasses\-1)).
        
        .. attribute:: dot1dtrafficclassentry
        
        	User Priority to Traffic Class mapping
        	**type**\: list of  		 :py:class:`Dot1Dtrafficclassentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Dtrafficclasstable, self).__init__()

            self.yang_name = "dot1dTrafficClassTable"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dTrafficClassEntry", ("dot1dtrafficclassentry", PBRIDGEMIB.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry))])
            self._leafs = OrderedDict()

            self.dot1dtrafficclassentry = YList(self)
            self._segment_path = lambda: "dot1dTrafficClassTable"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Dtrafficclasstable, [], name, value)


        class Dot1Dtrafficclassentry(Entity):
            """
            User Priority to Traffic Class mapping.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dtrafficclasspriority  (key)
            
            	The Priority value determined for the received frame. This value is equivalent to the priority indicated in the tagged frame received, or one of the evaluated priorities, determined according to the media\-type.  For untagged frames received from Ethernet media, this value is equal to the dot1dPortDefaultUserPriority value for the ingress port.  For untagged frames received from non\-Ethernet media, this value is equal to the dot1dRegenUserPriority value for the ingress port and media\-specific user priority
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1dtrafficclass
            
            	The Traffic Class the received frame is mapped to.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBRIDGEMIB.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry, self).__init__()

                self.yang_name = "dot1dTrafficClassEntry"
                self.yang_parent_name = "dot1dTrafficClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1dtrafficclasspriority']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', YLeaf(YType.str, 'dot1dBasePort')),
                    ('dot1dtrafficclasspriority', YLeaf(YType.int32, 'dot1dTrafficClassPriority')),
                    ('dot1dtrafficclass', YLeaf(YType.int32, 'dot1dTrafficClass')),
                ])
                self.dot1dbaseport = None
                self.dot1dtrafficclasspriority = None
                self.dot1dtrafficclass = None
                self._segment_path = lambda: "dot1dTrafficClassEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1dTrafficClassPriority='" + str(self.dot1dtrafficclasspriority) + "']"
                self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dTrafficClassTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PBRIDGEMIB.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry, ['dot1dbaseport', 'dot1dtrafficclasspriority', 'dot1dtrafficclass'], name, value)


    class Dot1Dportoutboundaccessprioritytable(Entity):
        """
        A table mapping Regenerated User Priority to Outbound
        Access Priority.  This is a fixed mapping for all port
        types, with two options for 802.5 Token Ring.
        
        .. attribute:: dot1dportoutboundaccesspriorityentry
        
        	Regenerated User Priority to Outbound Access Priority mapping
        	**type**\: list of  		 :py:class:`Dot1Dportoutboundaccesspriorityentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            super(PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable, self).__init__()

            self.yang_name = "dot1dPortOutboundAccessPriorityTable"
            self.yang_parent_name = "P-BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dPortOutboundAccessPriorityEntry", ("dot1dportoutboundaccesspriorityentry", PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry))])
            self._leafs = OrderedDict()

            self.dot1dportoutboundaccesspriorityentry = YList(self)
            self._segment_path = lambda: "dot1dPortOutboundAccessPriorityTable"
            self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable, [], name, value)


        class Dot1Dportoutboundaccesspriorityentry(Entity):
            """
            Regenerated User Priority to Outbound Access Priority
            mapping.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dregenuserpriority  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..7
            
            	**refers to**\:  :py:class:`dot1dregenuserpriority <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBRIDGEMIB.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
            
            .. attribute:: dot1dportoutboundaccesspriority
            
            	The Outbound Access Priority the received frame is mapped to
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                super(PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry, self).__init__()

                self.yang_name = "dot1dPortOutboundAccessPriorityEntry"
                self.yang_parent_name = "dot1dPortOutboundAccessPriorityTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','dot1dregenuserpriority']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', YLeaf(YType.str, 'dot1dBasePort')),
                    ('dot1dregenuserpriority', YLeaf(YType.str, 'dot1dRegenUserPriority')),
                    ('dot1dportoutboundaccesspriority', YLeaf(YType.int32, 'dot1dPortOutboundAccessPriority')),
                ])
                self.dot1dbaseport = None
                self.dot1dregenuserpriority = None
                self.dot1dportoutboundaccesspriority = None
                self._segment_path = lambda: "dot1dPortOutboundAccessPriorityEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[dot1dRegenUserPriority='" + str(self.dot1dregenuserpriority) + "']"
                self._absolute_path = lambda: "P-BRIDGE-MIB:P-BRIDGE-MIB/dot1dPortOutboundAccessPriorityTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PBRIDGEMIB.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry, ['dot1dbaseport', 'dot1dregenuserpriority', 'dot1dportoutboundaccesspriority'], name, value)

    def clone_ptr(self):
        self._top_entity = PBRIDGEMIB()
        return self._top_entity

