""" BRIDGE_MIB 

The Bridge MIB module for managing devices that support
IEEE 802.1D.

Copyright (C) The Internet Society (2005).  This version of
this MIB module is part of RFC 4188; see the RFC itself for
full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BRIDGEMIB(Entity):
    """
    
    
    .. attribute:: dot1dbase
    
    	
    	**type**\:  :py:class:`Dot1Dbase <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbase>`
    
    .. attribute:: dot1dstp
    
    	
    	**type**\:  :py:class:`Dot1Dstp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstp>`
    
    .. attribute:: dot1dtp
    
    	
    	**type**\:  :py:class:`Dot1Dtp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtp>`
    
    .. attribute:: dot1dbaseporttable
    
    	A table that contains generic information about every port that is associated with this bridge.  Transparent, source\-route, and srt ports are included
    	**type**\:  :py:class:`Dot1Dbaseporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable>`
    
    .. attribute:: dot1dstpporttable
    
    	A table that contains port\-specific information for the Spanning Tree Protocol
    	**type**\:  :py:class:`Dot1Dstpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstpporttable>`
    
    .. attribute:: dot1dtpfdbtable
    
    	A table that contains information about unicast entries for which the bridge has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\:  :py:class:`Dot1Dtpfdbtable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpfdbtable>`
    
    .. attribute:: dot1dtpporttable
    
    	A table that contains information about every port that is associated with this transparent bridge
    	**type**\:  :py:class:`Dot1Dtpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpporttable>`
    
    .. attribute:: dot1dstatictable
    
    	A table containing filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific destination addresses are allowed to be forwarded.  The value of zero in this table, as the port number from which frames with a specific destination address are received, is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast and for group/broadcast addresses
    	**type**\:  :py:class:`Dot1Dstatictable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstatictable>`
    
    

    """

    _prefix = 'BRIDGE-MIB'
    _revision = '2005-09-19'

    def __init__(self):
        super(BRIDGEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "BRIDGE-MIB"
        self.yang_parent_name = "BRIDGE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("dot1dBase", ("dot1dbase", BRIDGEMIB.Dot1Dbase)), ("dot1dStp", ("dot1dstp", BRIDGEMIB.Dot1Dstp)), ("dot1dTp", ("dot1dtp", BRIDGEMIB.Dot1Dtp)), ("dot1dBasePortTable", ("dot1dbaseporttable", BRIDGEMIB.Dot1Dbaseporttable)), ("dot1dStpPortTable", ("dot1dstpporttable", BRIDGEMIB.Dot1Dstpporttable)), ("dot1dTpFdbTable", ("dot1dtpfdbtable", BRIDGEMIB.Dot1Dtpfdbtable)), ("dot1dTpPortTable", ("dot1dtpporttable", BRIDGEMIB.Dot1Dtpporttable)), ("dot1dStaticTable", ("dot1dstatictable", BRIDGEMIB.Dot1Dstatictable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.dot1dbase = BRIDGEMIB.Dot1Dbase()
        self.dot1dbase.parent = self
        self._children_name_map["dot1dbase"] = "dot1dBase"
        self._children_yang_names.add("dot1dBase")

        self.dot1dstp = BRIDGEMIB.Dot1Dstp()
        self.dot1dstp.parent = self
        self._children_name_map["dot1dstp"] = "dot1dStp"
        self._children_yang_names.add("dot1dStp")

        self.dot1dtp = BRIDGEMIB.Dot1Dtp()
        self.dot1dtp.parent = self
        self._children_name_map["dot1dtp"] = "dot1dTp"
        self._children_yang_names.add("dot1dTp")

        self.dot1dbaseporttable = BRIDGEMIB.Dot1Dbaseporttable()
        self.dot1dbaseporttable.parent = self
        self._children_name_map["dot1dbaseporttable"] = "dot1dBasePortTable"
        self._children_yang_names.add("dot1dBasePortTable")

        self.dot1dstpporttable = BRIDGEMIB.Dot1Dstpporttable()
        self.dot1dstpporttable.parent = self
        self._children_name_map["dot1dstpporttable"] = "dot1dStpPortTable"
        self._children_yang_names.add("dot1dStpPortTable")

        self.dot1dtpfdbtable = BRIDGEMIB.Dot1Dtpfdbtable()
        self.dot1dtpfdbtable.parent = self
        self._children_name_map["dot1dtpfdbtable"] = "dot1dTpFdbTable"
        self._children_yang_names.add("dot1dTpFdbTable")

        self.dot1dtpporttable = BRIDGEMIB.Dot1Dtpporttable()
        self.dot1dtpporttable.parent = self
        self._children_name_map["dot1dtpporttable"] = "dot1dTpPortTable"
        self._children_yang_names.add("dot1dTpPortTable")

        self.dot1dstatictable = BRIDGEMIB.Dot1Dstatictable()
        self.dot1dstatictable.parent = self
        self._children_name_map["dot1dstatictable"] = "dot1dStaticTable"
        self._children_yang_names.add("dot1dStaticTable")
        self._segment_path = lambda: "BRIDGE-MIB:BRIDGE-MIB"


    class Dot1Dbase(Entity):
        """
        
        
        .. attribute:: dot1dbasebridgeaddress
        
        	The MAC address used by this bridge when it must be referred to in a unique fashion.  It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge.  However, it is only  required to be unique.  When concatenated with dot1dStpPriority, a unique BridgeIdentifier is formed, which is used in the Spanning Tree Protocol
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: dot1dbasenumports
        
        	The number of ports controlled by this bridging entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: ports
        
        .. attribute:: dot1dbasetype
        
        	Indicates what type of bridging this bridge can perform.  If a bridge is actually performing a certain type of bridging, this will be indicated by entries in the port table for the given type
        	**type**\:  :py:class:`Dot1Dbasetype <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbase.Dot1Dbasetype>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dbase, self).__init__()

            self.yang_name = "dot1dBase"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1dbasebridgeaddress', YLeaf(YType.str, 'dot1dBaseBridgeAddress')),
                ('dot1dbasenumports', YLeaf(YType.int32, 'dot1dBaseNumPorts')),
                ('dot1dbasetype', YLeaf(YType.enumeration, 'dot1dBaseType')),
            ])
            self.dot1dbasebridgeaddress = None
            self.dot1dbasenumports = None
            self.dot1dbasetype = None
            self._segment_path = lambda: "dot1dBase"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dbase, ['dot1dbasebridgeaddress', 'dot1dbasenumports', 'dot1dbasetype'], name, value)

        class Dot1Dbasetype(Enum):
            """
            Dot1Dbasetype (Enum Class)

            Indicates what type of bridging this bridge can

            perform.  If a bridge is actually performing a

            certain type of bridging, this will be indicated by

            entries in the port table for the given type.

            .. data:: unknown = 1

            .. data:: transparent_only = 2

            .. data:: sourceroute_only = 3

            .. data:: srt = 4

            """

            unknown = Enum.YLeaf(1, "unknown")

            transparent_only = Enum.YLeaf(2, "transparent-only")

            sourceroute_only = Enum.YLeaf(3, "sourceroute-only")

            srt = Enum.YLeaf(4, "srt")



    class Dot1Dstp(Entity):
        """
        
        
        .. attribute:: dot1dstpprotocolspecification
        
        	An indication of what version of the Spanning Tree Protocol is being run.  The value 'decLb100(2)' indicates the DEC LANbridge 100 Spanning Tree protocol. IEEE 802.1D implementations will return 'ieee8021d(3)'. If future versions of the IEEE Spanning Tree Protocol that are incompatible with the current version are released a new value will be defined
        	**type**\:  :py:class:`Dot1Dstpprotocolspecification <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstp.Dot1Dstpprotocolspecification>`
        
        .. attribute:: dot1dstppriority
        
        	The value of the write\-able portion of the Bridge ID (i.e., the first two octets of the (8 octet long) Bridge ID).  The other (last) 6 octets of the Bridge ID are given by the value of dot1dBaseBridgeAddress. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-61440, in steps of 4096
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: dot1dstptimesincetopologychange
        
        	The time (in hundredths of a second) since the last time a topology change was detected by the bridge entity. For RSTP, this reports the time since the tcWhile timer for any port on this Bridge was nonzero
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstptopchanges
        
        	The total number of topology changes detected by this bridge since the management entity was last reset or initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1dstpdesignatedroot
        
        	The bridge identifier of the root of the spanning tree, as determined by the Spanning Tree Protocol, as executed by this node.  This value is used as the Root Identifier parameter in all Configuration Bridge PDUs originated by this node
        	**type**\: str
        
        	**length:** 8
        
        .. attribute:: dot1dstprootcost
        
        	The cost of the path to the root as seen from this bridge
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstprootport
        
        	The port number of the port that offers the lowest cost path from this bridge to the root bridge
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstpmaxage
        
        	The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstphellotime
        
        	The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpholdtime
        
        	This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpforwarddelay
        
        	This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state.  The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state.  This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. [Note that this value is the one that this bridge is currently using, in contrast to dot1dStpBridgeForwardDelay, which is the value that this bridge and all others would start using if/when this bridge were to become the root.]
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgemaxage
        
        	The value that all bridges use for MaxAge when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeHelloTime.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\: int
        
        	**range:** 600..4000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgehellotime
        
        	The value that all bridges use for HelloTime when this bridge is acting as the root.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted  to a value that is not a whole number of seconds
        	**type**\: int
        
        	**range:** 100..1000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgeforwarddelay
        
        	The value that all bridges use for ForwardDelay when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeMaxAge.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\: int
        
        	**range:** 400..3000
        
        	**units**\: centi-seconds
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dstp, self).__init__()

            self.yang_name = "dot1dStp"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1dstpprotocolspecification', YLeaf(YType.enumeration, 'dot1dStpProtocolSpecification')),
                ('dot1dstppriority', YLeaf(YType.int32, 'dot1dStpPriority')),
                ('dot1dstptimesincetopologychange', YLeaf(YType.uint32, 'dot1dStpTimeSinceTopologyChange')),
                ('dot1dstptopchanges', YLeaf(YType.uint32, 'dot1dStpTopChanges')),
                ('dot1dstpdesignatedroot', YLeaf(YType.str, 'dot1dStpDesignatedRoot')),
                ('dot1dstprootcost', YLeaf(YType.int32, 'dot1dStpRootCost')),
                ('dot1dstprootport', YLeaf(YType.int32, 'dot1dStpRootPort')),
                ('dot1dstpmaxage', YLeaf(YType.int32, 'dot1dStpMaxAge')),
                ('dot1dstphellotime', YLeaf(YType.int32, 'dot1dStpHelloTime')),
                ('dot1dstpholdtime', YLeaf(YType.int32, 'dot1dStpHoldTime')),
                ('dot1dstpforwarddelay', YLeaf(YType.int32, 'dot1dStpForwardDelay')),
                ('dot1dstpbridgemaxage', YLeaf(YType.int32, 'dot1dStpBridgeMaxAge')),
                ('dot1dstpbridgehellotime', YLeaf(YType.int32, 'dot1dStpBridgeHelloTime')),
                ('dot1dstpbridgeforwarddelay', YLeaf(YType.int32, 'dot1dStpBridgeForwardDelay')),
            ])
            self.dot1dstpprotocolspecification = None
            self.dot1dstppriority = None
            self.dot1dstptimesincetopologychange = None
            self.dot1dstptopchanges = None
            self.dot1dstpdesignatedroot = None
            self.dot1dstprootcost = None
            self.dot1dstprootport = None
            self.dot1dstpmaxage = None
            self.dot1dstphellotime = None
            self.dot1dstpholdtime = None
            self.dot1dstpforwarddelay = None
            self.dot1dstpbridgemaxage = None
            self.dot1dstpbridgehellotime = None
            self.dot1dstpbridgeforwarddelay = None
            self._segment_path = lambda: "dot1dStp"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dstp, ['dot1dstpprotocolspecification', 'dot1dstppriority', 'dot1dstptimesincetopologychange', 'dot1dstptopchanges', 'dot1dstpdesignatedroot', 'dot1dstprootcost', 'dot1dstprootport', 'dot1dstpmaxage', 'dot1dstphellotime', 'dot1dstpholdtime', 'dot1dstpforwarddelay', 'dot1dstpbridgemaxage', 'dot1dstpbridgehellotime', 'dot1dstpbridgeforwarddelay'], name, value)

        class Dot1Dstpprotocolspecification(Enum):
            """
            Dot1Dstpprotocolspecification (Enum Class)

            An indication of what version of the Spanning Tree

            Protocol is being run.  The value 'decLb100(2)'

            indicates the DEC LANbridge 100 Spanning Tree protocol.

            IEEE 802.1D implementations will return 'ieee8021d(3)'.

            If future versions of the IEEE Spanning Tree Protocol

            that are incompatible with the current version

            are released a new value will be defined.

            .. data:: unknown = 1

            .. data:: decLb100 = 2

            .. data:: ieee8021d = 3

            """

            unknown = Enum.YLeaf(1, "unknown")

            decLb100 = Enum.YLeaf(2, "decLb100")

            ieee8021d = Enum.YLeaf(3, "ieee8021d")



    class Dot1Dtp(Entity):
        """
        
        
        .. attribute:: dot1dtplearnedentrydiscards
        
        	The total number of Forwarding Database entries that have been or would have been learned, but have been discarded due to a lack of storage space in the Forwarding Database.  If this counter is increasing, it indicates that the Forwarding Database is regularly becoming full (a condition that has unpleasant performance effects on the subnetwork).  If this counter has a significant value but is not presently increasing, it indicates that the problem has been occurring but is not persistent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dot1dtpagingtime
        
        	The timeout period in seconds for aging out dynamically\-learned forwarding information. 802.1D\-1998 recommends a default of 300 seconds
        	**type**\: int
        
        	**range:** 10..1000000
        
        	**units**\: seconds
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dtp, self).__init__()

            self.yang_name = "dot1dTp"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dot1dtplearnedentrydiscards', YLeaf(YType.uint32, 'dot1dTpLearnedEntryDiscards')),
                ('dot1dtpagingtime', YLeaf(YType.int32, 'dot1dTpAgingTime')),
            ])
            self.dot1dtplearnedentrydiscards = None
            self.dot1dtpagingtime = None
            self._segment_path = lambda: "dot1dTp"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dtp, ['dot1dtplearnedentrydiscards', 'dot1dtpagingtime'], name, value)


    class Dot1Dbaseporttable(Entity):
        """
        A table that contains generic information about every
        port that is associated with this bridge.  Transparent,
        source\-route, and srt ports are included.
        
        .. attribute:: dot1dbaseportentry
        
        	A list of information for each port of the bridge
        	**type**\: list of  		 :py:class:`Dot1Dbaseportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dbaseporttable, self).__init__()

            self.yang_name = "dot1dBasePortTable"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dBasePortEntry", ("dot1dbaseportentry", BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry))])
            self._leafs = OrderedDict()

            self.dot1dbaseportentry = YList(self)
            self._segment_path = lambda: "dot1dBasePortTable"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dbaseporttable, [], name, value)


        class Dot1Dbaseportentry(Entity):
            """
            A list of information for each port of the bridge.
            
            .. attribute:: dot1dbaseport  (key)
            
            	The port number of the port for which this entry contains bridge management information
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dbaseportifindex
            
            	The value of the instance of the ifIndex object, defined in IF\-MIB, for the interface corresponding to this port
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1dbaseportcircuit
            
            	For a port that (potentially) has the same value of dot1dBasePortIfIndex as another port on the same bridge. This object contains the name of an object instance unique to this port.  For example, in the case where multiple ports correspond one\-to\-one with multiple X.25 virtual circuits, this value might identify an (e.g., the first) object instance associated with the X.25 virtual circuit corresponding to this port.  For a port which has a unique value of dot1dBasePortIfIndex, this object can have the value { 0 0 }
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: dot1dbaseportdelayexceededdiscards
            
            	The number of frames discarded by this port due to excessive transit delay through the bridge.  It is incremented by both transparent and source route bridges
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dbaseportmtuexceededdiscards
            
            	The number of frames discarded by this port due to an excessive size.  It is incremented by both transparent and source route bridges
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportcapabilities
            
            	Indicates the parts of IEEE 802.1D and 802.1Q that are optional on a per\-port basis, that are implemented by this device, and that are manageable through this MIB.  dot1qDot1qTagging(0), \-\- supports 802.1Q VLAN tagging of                       \-\- frames and GVRP. dot1qConfigurableAcceptableFrameTypes(1),                       \-\- allows modified values of                       \-\- dot1qPortAcceptableFrameTypes. dot1qIngressFiltering(2)                       \-\- supports the discarding of any                       \-\- frame received on a Port whose                       \-\- VLAN classification does not                       \-\- include that Port in its Member                       \-\- set
            	**type**\:  :py:class:`Dot1Dportcapabilities <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Dportcapabilities>`
            
            .. attribute:: dot1dportdefaultuserpriority
            
            	The default ingress User Priority for this port.  This only has effect on media, such as Ethernet, that do not support native User Priority.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1dportnumtrafficclasses
            
            	The number of egress traffic classes supported on this port.  This object may optionally be read\-only.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 1..8
            
            .. attribute:: dot1dportgarpjointime
            
            	The GARP Join time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavetime
            
            	The GARP Leave time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavealltime
            
            	The GARP LeaveAll time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgmrpstatus
            
            	The administrative state of GMRP operation on this port.  The value enabled(1) indicates that GMRP is enabled on this port in all VLANs as long as dot1dGmrpStatus is also enabled(1). A value of disabled(2) indicates that GMRP is disabled on this port in all VLANs\: any GMRP packets received will be silently discarded, and no GMRP registrations will be propagated from other ports.  Setting this to a value of enabled(1) will be stored by the agent but will only take effect on the GMRP protocol operation if dot1dGmrpStatus also indicates the value enabled(1).  This object affects all GMRP Applicant and Registrar state machines on this port.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  :py:class:`EnabledStatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledStatus>`
            
            .. attribute:: dot1dportgmrpfailedregistrations
            
            	The total number of failed GMRP registrations, for any reason, in all VLANs, on this port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportgmrplastpduorigin
            
            	The Source MAC Address of the last GMRP message received on this port
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dportrestrictedgroupregistration
            
            	The state of Restricted Group Registration on this port. If the value of this control is true(1), then creation of a new dynamic entry is permitted only if there is a Static Filtering Entry for the VLAN concerned, in which the Registrar Administrative Control value is Normal Registration.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: bool
            
            .. attribute:: dot1qpvid
            
            	The PVID, the VLAN\-ID assigned to untagged frames or Priority\-Tagged frames received on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qportacceptableframetypes
            
            	When this is admitOnlyVlanTagged(2), the device will discard untagged frames or Priority\-Tagged frames received on this port.  When admitAll(1), untagged frames or Priority\-Tagged frames received on this port will be accepted and assigned to a VID based on the PVID and VID Set for this port.  This control does not affect VLAN\-independent Bridge Protocol Data Unit (BPDU) frames, such as GVRP and Spanning Tree Protocol (STP).  It does affect VLAN\- dependent BPDU frames, such as GMRP.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  :py:class:`Dot1Qportacceptableframetypes <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Qportacceptableframetypes>`
            
            .. attribute:: dot1qportingressfiltering
            
            	When this is true(1), the device will discard incoming frames for VLANs that do not include this Port in its  Member set.  When false(2), the port will accept all incoming frames.  This control does not affect VLAN\-independent BPDU frames, such as GVRP and STP.  It does affect VLAN\- dependent BPDU frames, such as GMRP.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: bool
            
            .. attribute:: dot1qportgvrpstatus
            
            	The state of GVRP operation on this port.  The value enabled(1) indicates that GVRP is enabled on this port, as long as dot1qGvrpStatus is also enabled for this device.  When disabled(2) but dot1qGvrpStatus is still enabled for the device, GVRP is disabled on this port\: any GVRP packets received will be silently discarded, and no GVRP registrations will be propagated from other ports.  This object affects all GVRP Applicant and Registrar state machines on this port.  A transition from disabled(2) to enabled(1) will cause a reset of all GVRP state machines on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  :py:class:`EnabledStatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledStatus>`
            
            .. attribute:: dot1qportgvrpfailedregistrations
            
            	The total number of failed GVRP registrations, for any reason, on this port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qportgvrplastpduorigin
            
            	The Source MAC Address of the last GVRP message received on this port
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qportrestrictedvlanregistration
            
            	The state of Restricted VLAN Registration on this port. If the value of this control is true(1), then creation of a new dynamic VLAN entry is permitted only if there is a Static VLAN Registration Entry for the VLAN concerned, in which the Registrar Administrative Control value for this port is Normal Registration.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\: bool
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry, self).__init__()

                self.yang_name = "dot1dBasePortEntry"
                self.yang_parent_name = "dot1dBasePortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', YLeaf(YType.int32, 'dot1dBasePort')),
                    ('dot1dbaseportifindex', YLeaf(YType.int32, 'dot1dBasePortIfIndex')),
                    ('dot1dbaseportcircuit', YLeaf(YType.str, 'dot1dBasePortCircuit')),
                    ('dot1dbaseportdelayexceededdiscards', YLeaf(YType.uint32, 'dot1dBasePortDelayExceededDiscards')),
                    ('dot1dbaseportmtuexceededdiscards', YLeaf(YType.uint32, 'dot1dBasePortMtuExceededDiscards')),
                    ('dot1dportcapabilities', YLeaf(YType.bits, 'P-BRIDGE-MIB:dot1dPortCapabilities')),
                    ('dot1dportdefaultuserpriority', YLeaf(YType.int32, 'P-BRIDGE-MIB:dot1dPortDefaultUserPriority')),
                    ('dot1dportnumtrafficclasses', YLeaf(YType.int32, 'P-BRIDGE-MIB:dot1dPortNumTrafficClasses')),
                    ('dot1dportgarpjointime', YLeaf(YType.int32, 'P-BRIDGE-MIB:dot1dPortGarpJoinTime')),
                    ('dot1dportgarpleavetime', YLeaf(YType.int32, 'P-BRIDGE-MIB:dot1dPortGarpLeaveTime')),
                    ('dot1dportgarpleavealltime', YLeaf(YType.int32, 'P-BRIDGE-MIB:dot1dPortGarpLeaveAllTime')),
                    ('dot1dportgmrpstatus', YLeaf(YType.enumeration, 'P-BRIDGE-MIB:dot1dPortGmrpStatus')),
                    ('dot1dportgmrpfailedregistrations', YLeaf(YType.uint32, 'P-BRIDGE-MIB:dot1dPortGmrpFailedRegistrations')),
                    ('dot1dportgmrplastpduorigin', YLeaf(YType.str, 'P-BRIDGE-MIB:dot1dPortGmrpLastPduOrigin')),
                    ('dot1dportrestrictedgroupregistration', YLeaf(YType.boolean, 'P-BRIDGE-MIB:dot1dPortRestrictedGroupRegistration')),
                    ('dot1qpvid', YLeaf(YType.uint32, 'Q-BRIDGE-MIB:dot1qPvid')),
                    ('dot1qportacceptableframetypes', YLeaf(YType.enumeration, 'Q-BRIDGE-MIB:dot1qPortAcceptableFrameTypes')),
                    ('dot1qportingressfiltering', YLeaf(YType.boolean, 'Q-BRIDGE-MIB:dot1qPortIngressFiltering')),
                    ('dot1qportgvrpstatus', YLeaf(YType.enumeration, 'Q-BRIDGE-MIB:dot1qPortGvrpStatus')),
                    ('dot1qportgvrpfailedregistrations', YLeaf(YType.uint32, 'Q-BRIDGE-MIB:dot1qPortGvrpFailedRegistrations')),
                    ('dot1qportgvrplastpduorigin', YLeaf(YType.str, 'Q-BRIDGE-MIB:dot1qPortGvrpLastPduOrigin')),
                    ('dot1qportrestrictedvlanregistration', YLeaf(YType.boolean, 'Q-BRIDGE-MIB:dot1qPortRestrictedVlanRegistration')),
                ])
                self.dot1dbaseport = None
                self.dot1dbaseportifindex = None
                self.dot1dbaseportcircuit = None
                self.dot1dbaseportdelayexceededdiscards = None
                self.dot1dbaseportmtuexceededdiscards = None
                self.dot1dportcapabilities = Bits()
                self.dot1dportdefaultuserpriority = None
                self.dot1dportnumtrafficclasses = None
                self.dot1dportgarpjointime = None
                self.dot1dportgarpleavetime = None
                self.dot1dportgarpleavealltime = None
                self.dot1dportgmrpstatus = None
                self.dot1dportgmrpfailedregistrations = None
                self.dot1dportgmrplastpduorigin = None
                self.dot1dportrestrictedgroupregistration = None
                self.dot1qpvid = None
                self.dot1qportacceptableframetypes = None
                self.dot1qportingressfiltering = None
                self.dot1qportgvrpstatus = None
                self.dot1qportgvrpfailedregistrations = None
                self.dot1qportgvrplastpduorigin = None
                self.dot1qportrestrictedvlanregistration = None
                self._segment_path = lambda: "dot1dBasePortEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']"
                self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/dot1dBasePortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BRIDGEMIB.Dot1Dbaseporttable.Dot1Dbaseportentry, ['dot1dbaseport', 'dot1dbaseportifindex', 'dot1dbaseportcircuit', 'dot1dbaseportdelayexceededdiscards', 'dot1dbaseportmtuexceededdiscards', 'dot1dportcapabilities', 'dot1dportdefaultuserpriority', 'dot1dportnumtrafficclasses', 'dot1dportgarpjointime', 'dot1dportgarpleavetime', 'dot1dportgarpleavealltime', 'dot1dportgmrpstatus', 'dot1dportgmrpfailedregistrations', 'dot1dportgmrplastpduorigin', 'dot1dportrestrictedgroupregistration', 'dot1qpvid', 'dot1qportacceptableframetypes', 'dot1qportingressfiltering', 'dot1qportgvrpstatus', 'dot1qportgvrpfailedregistrations', 'dot1qportgvrplastpduorigin', 'dot1qportrestrictedvlanregistration'], name, value)

            class Dot1Qportacceptableframetypes(Enum):
                """
                Dot1Qportacceptableframetypes (Enum Class)

                When this is admitOnlyVlanTagged(2), the device will

                discard untagged frames or Priority\-Tagged frames

                received on this port.  When admitAll(1), untagged

                frames or Priority\-Tagged frames received on this port

                will be accepted and assigned to a VID based on the

                PVID and VID Set for this port.

                This control does not affect VLAN\-independent Bridge

                Protocol Data Unit (BPDU) frames, such as GVRP and

                Spanning Tree Protocol (STP).  It does affect VLAN\-

                dependent BPDU frames, such as GMRP.

                The value of this object MUST be retained across

                reinitializations of the management system.

                .. data:: admitAll = 1

                .. data:: admitOnlyVlanTagged = 2

                """

                admitAll = Enum.YLeaf(1, "admitAll")

                admitOnlyVlanTagged = Enum.YLeaf(2, "admitOnlyVlanTagged")



    class Dot1Dstpporttable(Entity):
        """
        A table that contains port\-specific information
        for the Spanning Tree Protocol.
        
        .. attribute:: dot1dstpportentry
        
        	A list of information maintained by every port about the Spanning Tree Protocol state for that port
        	**type**\: list of  		 :py:class:`Dot1Dstpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dstpporttable, self).__init__()

            self.yang_name = "dot1dStpPortTable"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dStpPortEntry", ("dot1dstpportentry", BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry))])
            self._leafs = OrderedDict()

            self.dot1dstpportentry = YList(self)
            self._segment_path = lambda: "dot1dStpPortTable"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dstpporttable, [], name, value)


        class Dot1Dstpportentry(Entity):
            """
            A list of information maintained by every port about
            the Spanning Tree Protocol state for that port.
            
            .. attribute:: dot1dstpport  (key)
            
            	The port number of the port for which this entry contains Spanning Tree Protocol management information
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportpriority
            
            	The value of the priority field that is contained in the first (in network byte order) octet of the (2 octet long) Port ID.  The other octet of the Port ID is given by the value of dot1dStpPort. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-240, in steps of 16
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: dot1dstpportstate
            
            	The port's current state, as defined by application of the Spanning Tree Protocol.  This state controls what action a port takes on reception of a frame.  If the bridge has detected a port that is malfunctioning, it will place that port into the broken(6) state.  For ports that are disabled (see dot1dStpPortEnable), this object will have a value of disabled(1)
            	**type**\:  :py:class:`Dot1Dstpportstate <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry.Dot1Dstpportstate>`
            
            .. attribute:: dot1dstpportenable
            
            	The enabled/disabled status of the port
            	**type**\:  :py:class:`Dot1Dstpportenable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry.Dot1Dstpportenable>`
            
            .. attribute:: dot1dstpportpathcost
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to  the speed of the attached LAN.  New implementations should support dot1dStpPortPathCost32. If the port path costs exceeds the maximum value of this object then this object should report the maximum value, namely 65535.  Applications should try to read the dot1dStpPortPathCost32 object if this object reports the maximum value
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportdesignatedroot
            
            	The unique Bridge Identifier of the Bridge recorded as the Root in the Configuration BPDUs transmitted by the Designated Bridge for the segment to which the port is attached
            	**type**\: str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportdesignatedcost
            
            	The path cost of the Designated Port of the segment connected to this port.  This value is compared to the Root Path Cost field in received bridge PDUs
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dstpportdesignatedbridge
            
            	The Bridge Identifier of the bridge that this port considers to be the Designated Bridge for this port's segment
            	**type**\: str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportdesignatedport
            
            	The Port Identifier of the port on the Designated Bridge for this port's segment
            	**type**\: str
            
            	**length:** 2
            
            .. attribute:: dot1dstpportforwardtransitions
            
            	The number of times this port has transitioned from the Learning state to the Forwarding state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dstpportpathcost32
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  This object replaces dot1dStpPortPathCost to support IEEE 802.1t
            	**type**\: int
            
            	**range:** 1..200000000
            
            .. attribute:: stpxlongstpportpathcost
            
            	The contribution of this port to the path cost (in 32 bits value) of paths towards the spanning tree root which include this port.  This object is used to configure the spanning tree port path cost in 32 bits value range when the stpxSpanningTreePathCostOperMode is long(2).  If the stpxSpanningTreePathCostOperMode is short(1), this  MIB object is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry, self).__init__()

                self.yang_name = "dot1dStpPortEntry"
                self.yang_parent_name = "dot1dStpPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dstpport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dstpport', YLeaf(YType.int32, 'dot1dStpPort')),
                    ('dot1dstpportpriority', YLeaf(YType.int32, 'dot1dStpPortPriority')),
                    ('dot1dstpportstate', YLeaf(YType.enumeration, 'dot1dStpPortState')),
                    ('dot1dstpportenable', YLeaf(YType.enumeration, 'dot1dStpPortEnable')),
                    ('dot1dstpportpathcost', YLeaf(YType.int32, 'dot1dStpPortPathCost')),
                    ('dot1dstpportdesignatedroot', YLeaf(YType.str, 'dot1dStpPortDesignatedRoot')),
                    ('dot1dstpportdesignatedcost', YLeaf(YType.int32, 'dot1dStpPortDesignatedCost')),
                    ('dot1dstpportdesignatedbridge', YLeaf(YType.str, 'dot1dStpPortDesignatedBridge')),
                    ('dot1dstpportdesignatedport', YLeaf(YType.str, 'dot1dStpPortDesignatedPort')),
                    ('dot1dstpportforwardtransitions', YLeaf(YType.uint32, 'dot1dStpPortForwardTransitions')),
                    ('dot1dstpportpathcost32', YLeaf(YType.int32, 'dot1dStpPortPathCost32')),
                    ('stpxlongstpportpathcost', YLeaf(YType.uint32, 'CISCO-STP-EXTENSIONS-MIB:stpxLongStpPortPathCost')),
                ])
                self.dot1dstpport = None
                self.dot1dstpportpriority = None
                self.dot1dstpportstate = None
                self.dot1dstpportenable = None
                self.dot1dstpportpathcost = None
                self.dot1dstpportdesignatedroot = None
                self.dot1dstpportdesignatedcost = None
                self.dot1dstpportdesignatedbridge = None
                self.dot1dstpportdesignatedport = None
                self.dot1dstpportforwardtransitions = None
                self.dot1dstpportpathcost32 = None
                self.stpxlongstpportpathcost = None
                self._segment_path = lambda: "dot1dStpPortEntry" + "[dot1dStpPort='" + str(self.dot1dstpport) + "']"
                self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/dot1dStpPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BRIDGEMIB.Dot1Dstpporttable.Dot1Dstpportentry, ['dot1dstpport', 'dot1dstpportpriority', 'dot1dstpportstate', 'dot1dstpportenable', 'dot1dstpportpathcost', 'dot1dstpportdesignatedroot', 'dot1dstpportdesignatedcost', 'dot1dstpportdesignatedbridge', 'dot1dstpportdesignatedport', 'dot1dstpportforwardtransitions', 'dot1dstpportpathcost32', 'stpxlongstpportpathcost'], name, value)

            class Dot1Dstpportenable(Enum):
                """
                Dot1Dstpportenable (Enum Class)

                The enabled/disabled status of the port.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Dot1Dstpportstate(Enum):
                """
                Dot1Dstpportstate (Enum Class)

                The port's current state, as defined by application of

                the Spanning Tree Protocol.  This state controls what

                action a port takes on reception of a frame.  If the

                bridge has detected a port that is malfunctioning, it

                will place that port into the broken(6) state.  For

                ports that are disabled (see dot1dStpPortEnable), this

                object will have a value of disabled(1).

                .. data:: disabled = 1

                .. data:: blocking = 2

                .. data:: listening = 3

                .. data:: learning = 4

                .. data:: forwarding = 5

                .. data:: broken = 6

                """

                disabled = Enum.YLeaf(1, "disabled")

                blocking = Enum.YLeaf(2, "blocking")

                listening = Enum.YLeaf(3, "listening")

                learning = Enum.YLeaf(4, "learning")

                forwarding = Enum.YLeaf(5, "forwarding")

                broken = Enum.YLeaf(6, "broken")



    class Dot1Dtpfdbtable(Entity):
        """
        A table that contains information about unicast
        entries for which the bridge has forwarding and/or
        filtering information.  This information is used
        by the transparent bridging function in
        determining how to propagate a received frame.
        
        .. attribute:: dot1dtpfdbentry
        
        	Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information
        	**type**\: list of  		 :py:class:`Dot1Dtpfdbentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpfdbtable.Dot1Dtpfdbentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dtpfdbtable, self).__init__()

            self.yang_name = "dot1dTpFdbTable"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dTpFdbEntry", ("dot1dtpfdbentry", BRIDGEMIB.Dot1Dtpfdbtable.Dot1Dtpfdbentry))])
            self._leafs = OrderedDict()

            self.dot1dtpfdbentry = YList(self)
            self._segment_path = lambda: "dot1dTpFdbTable"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dtpfdbtable, [], name, value)


        class Dot1Dtpfdbentry(Entity):
            """
            Information about a specific unicast MAC address
            for which the bridge has some forwarding and/or
            filtering information.
            
            .. attribute:: dot1dtpfdbaddress  (key)
            
            	A unicast MAC address for which the bridge has forwarding and/or filtering information
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1dTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned, but that the bridge does have some forwarding/filtering information about this address (e.g., in the dot1dStaticTable).  Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1dTpFdbStatus is not learned(3)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This would         include the case where some other MIB object         (not the corresponding instance of         dot1dTpFdbPort, nor an entry in the         dot1dStaticTable) is being used to determine if         and how frames addressed to the value of the         corresponding instance of dot1dTpFdbAddress are         being forwarded.     invalid(2) \- this entry is no longer valid (e.g.,         it was learned but has since aged out), but has         not yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1dTpFdbPort was learned, and is being         used.     self(4) \- the value of the corresponding instance of         dot1dTpFdbAddress represents one of the bridge's         addresses.  The corresponding instance of         dot1dTpFdbPort indicates which of the bridge's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1dTpFdbAddress is also the value of an         existing instance of dot1dStaticAddress
            	**type**\:  :py:class:`Dot1Dtpfdbstatus <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1Dtpfdbstatus>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BRIDGEMIB.Dot1Dtpfdbtable.Dot1Dtpfdbentry, self).__init__()

                self.yang_name = "dot1dTpFdbEntry"
                self.yang_parent_name = "dot1dTpFdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dtpfdbaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dtpfdbaddress', YLeaf(YType.str, 'dot1dTpFdbAddress')),
                    ('dot1dtpfdbport', YLeaf(YType.int32, 'dot1dTpFdbPort')),
                    ('dot1dtpfdbstatus', YLeaf(YType.enumeration, 'dot1dTpFdbStatus')),
                ])
                self.dot1dtpfdbaddress = None
                self.dot1dtpfdbport = None
                self.dot1dtpfdbstatus = None
                self._segment_path = lambda: "dot1dTpFdbEntry" + "[dot1dTpFdbAddress='" + str(self.dot1dtpfdbaddress) + "']"
                self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/dot1dTpFdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BRIDGEMIB.Dot1Dtpfdbtable.Dot1Dtpfdbentry, ['dot1dtpfdbaddress', 'dot1dtpfdbport', 'dot1dtpfdbstatus'], name, value)

            class Dot1Dtpfdbstatus(Enum):
                """
                Dot1Dtpfdbstatus (Enum Class)

                The status of this entry.  The meanings of the

                values are\:

                    other(1) \- none of the following.  This would

                        include the case where some other MIB object

                        (not the corresponding instance of

                        dot1dTpFdbPort, nor an entry in the

                        dot1dStaticTable) is being used to determine if

                        and how frames addressed to the value of the

                        corresponding instance of dot1dTpFdbAddress are

                        being forwarded.

                    invalid(2) \- this entry is no longer valid (e.g.,

                        it was learned but has since aged out), but has

                        not yet been flushed from the table.

                    learned(3) \- the value of the corresponding instance

                        of dot1dTpFdbPort was learned, and is being

                        used.

                    self(4) \- the value of the corresponding instance of

                        dot1dTpFdbAddress represents one of the bridge's

                        addresses.  The corresponding instance of

                        dot1dTpFdbPort indicates which of the bridge's

                        ports has this address.

                    mgmt(5) \- the value of the corresponding instance of

                        dot1dTpFdbAddress is also the value of an

                        existing instance of dot1dStaticAddress.

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



    class Dot1Dtpporttable(Entity):
        """
        A table that contains information about every port that
        is associated with this transparent bridge.
        
        .. attribute:: dot1dtpportentry
        
        	A list of information for each port of a transparent bridge
        	**type**\: list of  		 :py:class:`Dot1Dtpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dtpporttable, self).__init__()

            self.yang_name = "dot1dTpPortTable"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dTpPortEntry", ("dot1dtpportentry", BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry))])
            self._leafs = OrderedDict()

            self.dot1dtpportentry = YList(self)
            self._segment_path = lambda: "dot1dTpPortTable"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dtpporttable, [], name, value)


        class Dot1Dtpportentry(Entity):
            """
            A list of information for each port of a transparent
            bridge.
            
            .. attribute:: dot1dtpport  (key)
            
            	The port number of the port for which this entry contains Transparent bridging management information
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dtpportmaxinfo
            
            	The maximum size of the INFO (non\-MAC) field that  this port will receive or transmit
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: dot1dtpportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportindiscards
            
            	Count of received valid frames that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry, self).__init__()

                self.yang_name = "dot1dTpPortEntry"
                self.yang_parent_name = "dot1dTpPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dtpport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dtpport', YLeaf(YType.int32, 'dot1dTpPort')),
                    ('dot1dtpportmaxinfo', YLeaf(YType.int32, 'dot1dTpPortMaxInfo')),
                    ('dot1dtpportinframes', YLeaf(YType.uint32, 'dot1dTpPortInFrames')),
                    ('dot1dtpportoutframes', YLeaf(YType.uint32, 'dot1dTpPortOutFrames')),
                    ('dot1dtpportindiscards', YLeaf(YType.uint32, 'dot1dTpPortInDiscards')),
                ])
                self.dot1dtpport = None
                self.dot1dtpportmaxinfo = None
                self.dot1dtpportinframes = None
                self.dot1dtpportoutframes = None
                self.dot1dtpportindiscards = None
                self._segment_path = lambda: "dot1dTpPortEntry" + "[dot1dTpPort='" + str(self.dot1dtpport) + "']"
                self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/dot1dTpPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BRIDGEMIB.Dot1Dtpporttable.Dot1Dtpportentry, ['dot1dtpport', 'dot1dtpportmaxinfo', 'dot1dtpportinframes', 'dot1dtpportoutframes', 'dot1dtpportindiscards'], name, value)


    class Dot1Dstatictable(Entity):
        """
        A table containing filtering information configured
        into the bridge by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific destination
        addresses are allowed to be forwarded.  The value of
        zero in this table, as the port number from which frames
        with a specific destination address are received, is
        used to specify all ports for which there is no specific
        entry in this table for that particular destination
        address.  Entries are valid for unicast and for
        group/broadcast addresses.
        
        .. attribute:: dot1dstaticentry
        
        	Filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific destination address are allowed to be forwarded
        	**type**\: list of  		 :py:class:`Dot1Dstaticentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstatictable.Dot1Dstaticentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BRIDGEMIB.Dot1Dstatictable, self).__init__()

            self.yang_name = "dot1dStaticTable"
            self.yang_parent_name = "BRIDGE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot1dStaticEntry", ("dot1dstaticentry", BRIDGEMIB.Dot1Dstatictable.Dot1Dstaticentry))])
            self._leafs = OrderedDict()

            self.dot1dstaticentry = YList(self)
            self._segment_path = lambda: "dot1dStaticTable"
            self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BRIDGEMIB.Dot1Dstatictable, [], name, value)


        class Dot1Dstaticentry(Entity):
            """
            Filtering information configured into the bridge by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific destination address are allowed to
            be forwarded.
            
            .. attribute:: dot1dstaticaddress  (key)
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object can take the value of a unicast address, a group address, or the broadcast address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dstaticreceiveport  (key)
            
            	Either the value '0', or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the bridge for which there is no other applicable entry
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot1dstaticallowedtogoto
            
            	The set of ports to which frames received from a specific port and destined for a specific MAC address, are allowed to be forwarded.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc.  Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the bridge is represented by a single bit within the value of this object.  If that bit has a value of '1', then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  (Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.)  The default value of this object is a string of ones of appropriate length.  The value of this object may exceed the required minimum maximum message size of some SNMP transport (484 bytes, in the case of SNMP over UDP, see RFC 3417, section 3.2). SNMP engines on bridges supporting a large number of ports must support appropriate maximum message sizes
            	**type**\: str
            
            	**length:** 0..512
            
            .. attribute:: dot1dstaticstatus
            
            	This object indicates the status of this entry. The default value is permanent(3).     other(1) \- this entry is currently in use but the         conditions under which it will remain so are         different from each of the following values.     invalid(2) \- writing this value to the object         removes the corresponding entry.     permanent(3) \- this entry is currently in use and         will remain so after the next reset of the         bridge.     deleteOnReset(4) \- this entry is currently in use         and will remain so until the next reset of the         bridge.     deleteOnTimeout(5) \- this entry is currently in use         and will remain so until it is aged out
            	**type**\:  :py:class:`Dot1Dstaticstatus <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1Dstatictable.Dot1Dstaticentry.Dot1Dstaticstatus>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BRIDGEMIB.Dot1Dstatictable.Dot1Dstaticentry, self).__init__()

                self.yang_name = "dot1dStaticEntry"
                self.yang_parent_name = "dot1dStaticTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dstaticaddress','dot1dstaticreceiveport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dstaticaddress', YLeaf(YType.str, 'dot1dStaticAddress')),
                    ('dot1dstaticreceiveport', YLeaf(YType.int32, 'dot1dStaticReceivePort')),
                    ('dot1dstaticallowedtogoto', YLeaf(YType.str, 'dot1dStaticAllowedToGoTo')),
                    ('dot1dstaticstatus', YLeaf(YType.enumeration, 'dot1dStaticStatus')),
                ])
                self.dot1dstaticaddress = None
                self.dot1dstaticreceiveport = None
                self.dot1dstaticallowedtogoto = None
                self.dot1dstaticstatus = None
                self._segment_path = lambda: "dot1dStaticEntry" + "[dot1dStaticAddress='" + str(self.dot1dstaticaddress) + "']" + "[dot1dStaticReceivePort='" + str(self.dot1dstaticreceiveport) + "']"
                self._absolute_path = lambda: "BRIDGE-MIB:BRIDGE-MIB/dot1dStaticTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BRIDGEMIB.Dot1Dstatictable.Dot1Dstaticentry, ['dot1dstaticaddress', 'dot1dstaticreceiveport', 'dot1dstaticallowedtogoto', 'dot1dstaticstatus'], name, value)

            class Dot1Dstaticstatus(Enum):
                """
                Dot1Dstaticstatus (Enum Class)

                This object indicates the status of this entry.

                The default value is permanent(3).

                    other(1) \- this entry is currently in use but the

                        conditions under which it will remain so are

                        different from each of the following values.

                    invalid(2) \- writing this value to the object

                        removes the corresponding entry.

                    permanent(3) \- this entry is currently in use and

                        will remain so after the next reset of the

                        bridge.

                    deleteOnReset(4) \- this entry is currently in use

                        and will remain so until the next reset of the

                        bridge.

                    deleteOnTimeout(5) \- this entry is currently in use

                        and will remain so until it is aged out.

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


    def clone_ptr(self):
        self._top_entity = BRIDGEMIB()
        return self._top_entity

