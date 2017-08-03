""" BRIDGE_MIB 

The Bridge MIB module for managing devices that support
IEEE 802.1D.

Copyright (C) The Internet Society (2005).  This version of
this MIB module is part of RFC 4188; see the RFC itself for
full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BridgeMib(Entity):
    """
    
    
    .. attribute:: dot1dbase
    
    	
    	**type**\:   :py:class:`Dot1Dbase <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbase>`
    
    .. attribute:: dot1dbaseporttable
    
    	A table that contains generic information about every port that is associated with this bridge.  Transparent, source\-route, and srt ports are included
    	**type**\:   :py:class:`Dot1Dbaseporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable>`
    
    .. attribute:: dot1dstatictable
    
    	A table containing filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific destination addresses are allowed to be forwarded.  The value of zero in this table, as the port number from which frames with a specific destination address are received, is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast and for group/broadcast addresses
    	**type**\:   :py:class:`Dot1Dstatictable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable>`
    
    .. attribute:: dot1dstp
    
    	
    	**type**\:   :py:class:`Dot1Dstp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstp>`
    
    .. attribute:: dot1dstpporttable
    
    	A table that contains port\-specific information for the Spanning Tree Protocol
    	**type**\:   :py:class:`Dot1Dstpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable>`
    
    .. attribute:: dot1dtp
    
    	
    	**type**\:   :py:class:`Dot1Dtp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtp>`
    
    .. attribute:: dot1dtpfdbtable
    
    	A table that contains information about unicast entries for which the bridge has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\:   :py:class:`Dot1Dtpfdbtable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable>`
    
    .. attribute:: dot1dtpporttable
    
    	A table that contains information about every port that is associated with this transparent bridge
    	**type**\:   :py:class:`Dot1Dtpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable>`
    
    

    """

    _prefix = 'BRIDGE-MIB'
    _revision = '2005-09-19'

    def __init__(self):
        super(BridgeMib, self).__init__()
        self._top_entity = None

        self.yang_name = "BRIDGE-MIB"
        self.yang_parent_name = "BRIDGE-MIB"

        self.dot1dbase = BridgeMib.Dot1Dbase()
        self.dot1dbase.parent = self
        self._children_name_map["dot1dbase"] = "dot1dBase"
        self._children_yang_names.add("dot1dBase")

        self.dot1dbaseporttable = BridgeMib.Dot1Dbaseporttable()
        self.dot1dbaseporttable.parent = self
        self._children_name_map["dot1dbaseporttable"] = "dot1dBasePortTable"
        self._children_yang_names.add("dot1dBasePortTable")

        self.dot1dstatictable = BridgeMib.Dot1Dstatictable()
        self.dot1dstatictable.parent = self
        self._children_name_map["dot1dstatictable"] = "dot1dStaticTable"
        self._children_yang_names.add("dot1dStaticTable")

        self.dot1dstp = BridgeMib.Dot1Dstp()
        self.dot1dstp.parent = self
        self._children_name_map["dot1dstp"] = "dot1dStp"
        self._children_yang_names.add("dot1dStp")

        self.dot1dstpporttable = BridgeMib.Dot1Dstpporttable()
        self.dot1dstpporttable.parent = self
        self._children_name_map["dot1dstpporttable"] = "dot1dStpPortTable"
        self._children_yang_names.add("dot1dStpPortTable")

        self.dot1dtp = BridgeMib.Dot1Dtp()
        self.dot1dtp.parent = self
        self._children_name_map["dot1dtp"] = "dot1dTp"
        self._children_yang_names.add("dot1dTp")

        self.dot1dtpfdbtable = BridgeMib.Dot1Dtpfdbtable()
        self.dot1dtpfdbtable.parent = self
        self._children_name_map["dot1dtpfdbtable"] = "dot1dTpFdbTable"
        self._children_yang_names.add("dot1dTpFdbTable")

        self.dot1dtpporttable = BridgeMib.Dot1Dtpporttable()
        self.dot1dtpporttable.parent = self
        self._children_name_map["dot1dtpporttable"] = "dot1dTpPortTable"
        self._children_yang_names.add("dot1dTpPortTable")


    class Dot1Dbase(Entity):
        """
        
        
        .. attribute:: dot1dbasebridgeaddress
        
        	The MAC address used by this bridge when it must be referred to in a unique fashion.  It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge.  However, it is only  required to be unique.  When concatenated with dot1dStpPriority, a unique BridgeIdentifier is formed, which is used in the Spanning Tree Protocol
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: dot1dbasenumports
        
        	The number of ports controlled by this bridging entity
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: ports
        
        .. attribute:: dot1dbasetype
        
        	Indicates what type of bridging this bridge can perform.  If a bridge is actually performing a certain type of bridging, this will be indicated by entries in the port table for the given type
        	**type**\:   :py:class:`Dot1Dbasetype <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbase.Dot1Dbasetype>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dbase, self).__init__()

            self.yang_name = "dot1dBase"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dbasebridgeaddress = YLeaf(YType.str, "dot1dBaseBridgeAddress")

            self.dot1dbasenumports = YLeaf(YType.int32, "dot1dBaseNumPorts")

            self.dot1dbasetype = YLeaf(YType.enumeration, "dot1dBaseType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1dbasebridgeaddress",
                            "dot1dbasenumports",
                            "dot1dbasetype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeMib.Dot1Dbase, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dbase, self).__setattr__(name, value)

        class Dot1Dbasetype(Enum):
            """
            Dot1Dbasetype

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


        def has_data(self):
            return (
                self.dot1dbasebridgeaddress.is_set or
                self.dot1dbasenumports.is_set or
                self.dot1dbasetype.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1dbasebridgeaddress.yfilter != YFilter.not_set or
                self.dot1dbasenumports.yfilter != YFilter.not_set or
                self.dot1dbasetype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dBase" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1dbasebridgeaddress.is_set or self.dot1dbasebridgeaddress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dbasebridgeaddress.get_name_leafdata())
            if (self.dot1dbasenumports.is_set or self.dot1dbasenumports.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dbasenumports.get_name_leafdata())
            if (self.dot1dbasetype.is_set or self.dot1dbasetype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dbasetype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dBaseBridgeAddress" or name == "dot1dBaseNumPorts" or name == "dot1dBaseType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1dBaseBridgeAddress"):
                self.dot1dbasebridgeaddress = value
                self.dot1dbasebridgeaddress.value_namespace = name_space
                self.dot1dbasebridgeaddress.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dBaseNumPorts"):
                self.dot1dbasenumports = value
                self.dot1dbasenumports.value_namespace = name_space
                self.dot1dbasenumports.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dBaseType"):
                self.dot1dbasetype = value
                self.dot1dbasetype.value_namespace = name_space
                self.dot1dbasetype.value_namespace_prefix = name_space_prefix


    class Dot1Dstp(Entity):
        """
        
        
        .. attribute:: dot1dstpbridgeforwarddelay
        
        	The value that all bridges use for ForwardDelay when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeMaxAge.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 400..3000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgehellotime
        
        	The value that all bridges use for HelloTime when this bridge is acting as the root.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted  to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgemaxage
        
        	The value that all bridges use for MaxAge when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeHelloTime.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 600..4000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpdesignatedroot
        
        	The bridge identifier of the root of the spanning tree, as determined by the Spanning Tree Protocol, as executed by this node.  This value is used as the Root Identifier parameter in all Configuration Bridge PDUs originated by this node
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: dot1dstpforwarddelay
        
        	This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state.  The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state.  This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. [Note that this value is the one that this bridge is currently using, in contrast to dot1dStpBridgeForwardDelay, which is the value that this bridge and all others would start using if/when this bridge were to become the root.]
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstphellotime
        
        	The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpholdtime
        
        	This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpmaxage
        
        	The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstppriority
        
        	The value of the write\-able portion of the Bridge ID (i.e., the first two octets of the (8 octet long) Bridge ID).  The other (last) 6 octets of the Bridge ID are given by the value of dot1dBaseBridgeAddress. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-61440, in steps of 4096
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: dot1dstpprotocolspecification
        
        	An indication of what version of the Spanning Tree Protocol is being run.  The value 'decLb100(2)' indicates the DEC LANbridge 100 Spanning Tree protocol. IEEE 802.1D implementations will return 'ieee8021d(3)'. If future versions of the IEEE Spanning Tree Protocol that are incompatible with the current version are released a new value will be defined
        	**type**\:   :py:class:`Dot1Dstpprotocolspecification <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstp.Dot1Dstpprotocolspecification>`
        
        .. attribute:: dot1dstprootcost
        
        	The cost of the path to the root as seen from this bridge
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstprootport
        
        	The port number of the port that offers the lowest cost path from this bridge to the root bridge
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstptimesincetopologychange
        
        	The time (in hundredths of a second) since the last time a topology change was detected by the bridge entity. For RSTP, this reports the time since the tcWhile timer for any port on this Bridge was nonzero
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstptopchanges
        
        	The total number of topology changes detected by this bridge since the management entity was last reset or initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dstp, self).__init__()

            self.yang_name = "dot1dStp"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dstpbridgeforwarddelay = YLeaf(YType.int32, "dot1dStpBridgeForwardDelay")

            self.dot1dstpbridgehellotime = YLeaf(YType.int32, "dot1dStpBridgeHelloTime")

            self.dot1dstpbridgemaxage = YLeaf(YType.int32, "dot1dStpBridgeMaxAge")

            self.dot1dstpdesignatedroot = YLeaf(YType.str, "dot1dStpDesignatedRoot")

            self.dot1dstpforwarddelay = YLeaf(YType.int32, "dot1dStpForwardDelay")

            self.dot1dstphellotime = YLeaf(YType.int32, "dot1dStpHelloTime")

            self.dot1dstpholdtime = YLeaf(YType.int32, "dot1dStpHoldTime")

            self.dot1dstpmaxage = YLeaf(YType.int32, "dot1dStpMaxAge")

            self.dot1dstppriority = YLeaf(YType.int32, "dot1dStpPriority")

            self.dot1dstpprotocolspecification = YLeaf(YType.enumeration, "dot1dStpProtocolSpecification")

            self.dot1dstprootcost = YLeaf(YType.int32, "dot1dStpRootCost")

            self.dot1dstprootport = YLeaf(YType.int32, "dot1dStpRootPort")

            self.dot1dstptimesincetopologychange = YLeaf(YType.uint32, "dot1dStpTimeSinceTopologyChange")

            self.dot1dstptopchanges = YLeaf(YType.uint32, "dot1dStpTopChanges")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1dstpbridgeforwarddelay",
                            "dot1dstpbridgehellotime",
                            "dot1dstpbridgemaxage",
                            "dot1dstpdesignatedroot",
                            "dot1dstpforwarddelay",
                            "dot1dstphellotime",
                            "dot1dstpholdtime",
                            "dot1dstpmaxage",
                            "dot1dstppriority",
                            "dot1dstpprotocolspecification",
                            "dot1dstprootcost",
                            "dot1dstprootport",
                            "dot1dstptimesincetopologychange",
                            "dot1dstptopchanges") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeMib.Dot1Dstp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dstp, self).__setattr__(name, value)

        class Dot1Dstpprotocolspecification(Enum):
            """
            Dot1Dstpprotocolspecification

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


        def has_data(self):
            return (
                self.dot1dstpbridgeforwarddelay.is_set or
                self.dot1dstpbridgehellotime.is_set or
                self.dot1dstpbridgemaxage.is_set or
                self.dot1dstpdesignatedroot.is_set or
                self.dot1dstpforwarddelay.is_set or
                self.dot1dstphellotime.is_set or
                self.dot1dstpholdtime.is_set or
                self.dot1dstpmaxage.is_set or
                self.dot1dstppriority.is_set or
                self.dot1dstpprotocolspecification.is_set or
                self.dot1dstprootcost.is_set or
                self.dot1dstprootport.is_set or
                self.dot1dstptimesincetopologychange.is_set or
                self.dot1dstptopchanges.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1dstpbridgeforwarddelay.yfilter != YFilter.not_set or
                self.dot1dstpbridgehellotime.yfilter != YFilter.not_set or
                self.dot1dstpbridgemaxage.yfilter != YFilter.not_set or
                self.dot1dstpdesignatedroot.yfilter != YFilter.not_set or
                self.dot1dstpforwarddelay.yfilter != YFilter.not_set or
                self.dot1dstphellotime.yfilter != YFilter.not_set or
                self.dot1dstpholdtime.yfilter != YFilter.not_set or
                self.dot1dstpmaxage.yfilter != YFilter.not_set or
                self.dot1dstppriority.yfilter != YFilter.not_set or
                self.dot1dstpprotocolspecification.yfilter != YFilter.not_set or
                self.dot1dstprootcost.yfilter != YFilter.not_set or
                self.dot1dstprootport.yfilter != YFilter.not_set or
                self.dot1dstptimesincetopologychange.yfilter != YFilter.not_set or
                self.dot1dstptopchanges.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dStp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1dstpbridgeforwarddelay.is_set or self.dot1dstpbridgeforwarddelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpbridgeforwarddelay.get_name_leafdata())
            if (self.dot1dstpbridgehellotime.is_set or self.dot1dstpbridgehellotime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpbridgehellotime.get_name_leafdata())
            if (self.dot1dstpbridgemaxage.is_set or self.dot1dstpbridgemaxage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpbridgemaxage.get_name_leafdata())
            if (self.dot1dstpdesignatedroot.is_set or self.dot1dstpdesignatedroot.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpdesignatedroot.get_name_leafdata())
            if (self.dot1dstpforwarddelay.is_set or self.dot1dstpforwarddelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpforwarddelay.get_name_leafdata())
            if (self.dot1dstphellotime.is_set or self.dot1dstphellotime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstphellotime.get_name_leafdata())
            if (self.dot1dstpholdtime.is_set or self.dot1dstpholdtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpholdtime.get_name_leafdata())
            if (self.dot1dstpmaxage.is_set or self.dot1dstpmaxage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpmaxage.get_name_leafdata())
            if (self.dot1dstppriority.is_set or self.dot1dstppriority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstppriority.get_name_leafdata())
            if (self.dot1dstpprotocolspecification.is_set or self.dot1dstpprotocolspecification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstpprotocolspecification.get_name_leafdata())
            if (self.dot1dstprootcost.is_set or self.dot1dstprootcost.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstprootcost.get_name_leafdata())
            if (self.dot1dstprootport.is_set or self.dot1dstprootport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstprootport.get_name_leafdata())
            if (self.dot1dstptimesincetopologychange.is_set or self.dot1dstptimesincetopologychange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstptimesincetopologychange.get_name_leafdata())
            if (self.dot1dstptopchanges.is_set or self.dot1dstptopchanges.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dstptopchanges.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dStpBridgeForwardDelay" or name == "dot1dStpBridgeHelloTime" or name == "dot1dStpBridgeMaxAge" or name == "dot1dStpDesignatedRoot" or name == "dot1dStpForwardDelay" or name == "dot1dStpHelloTime" or name == "dot1dStpHoldTime" or name == "dot1dStpMaxAge" or name == "dot1dStpPriority" or name == "dot1dStpProtocolSpecification" or name == "dot1dStpRootCost" or name == "dot1dStpRootPort" or name == "dot1dStpTimeSinceTopologyChange" or name == "dot1dStpTopChanges"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1dStpBridgeForwardDelay"):
                self.dot1dstpbridgeforwarddelay = value
                self.dot1dstpbridgeforwarddelay.value_namespace = name_space
                self.dot1dstpbridgeforwarddelay.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpBridgeHelloTime"):
                self.dot1dstpbridgehellotime = value
                self.dot1dstpbridgehellotime.value_namespace = name_space
                self.dot1dstpbridgehellotime.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpBridgeMaxAge"):
                self.dot1dstpbridgemaxage = value
                self.dot1dstpbridgemaxage.value_namespace = name_space
                self.dot1dstpbridgemaxage.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpDesignatedRoot"):
                self.dot1dstpdesignatedroot = value
                self.dot1dstpdesignatedroot.value_namespace = name_space
                self.dot1dstpdesignatedroot.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpForwardDelay"):
                self.dot1dstpforwarddelay = value
                self.dot1dstpforwarddelay.value_namespace = name_space
                self.dot1dstpforwarddelay.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpHelloTime"):
                self.dot1dstphellotime = value
                self.dot1dstphellotime.value_namespace = name_space
                self.dot1dstphellotime.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpHoldTime"):
                self.dot1dstpholdtime = value
                self.dot1dstpholdtime.value_namespace = name_space
                self.dot1dstpholdtime.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpMaxAge"):
                self.dot1dstpmaxage = value
                self.dot1dstpmaxage.value_namespace = name_space
                self.dot1dstpmaxage.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpPriority"):
                self.dot1dstppriority = value
                self.dot1dstppriority.value_namespace = name_space
                self.dot1dstppriority.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpProtocolSpecification"):
                self.dot1dstpprotocolspecification = value
                self.dot1dstpprotocolspecification.value_namespace = name_space
                self.dot1dstpprotocolspecification.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpRootCost"):
                self.dot1dstprootcost = value
                self.dot1dstprootcost.value_namespace = name_space
                self.dot1dstprootcost.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpRootPort"):
                self.dot1dstprootport = value
                self.dot1dstprootport.value_namespace = name_space
                self.dot1dstprootport.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpTimeSinceTopologyChange"):
                self.dot1dstptimesincetopologychange = value
                self.dot1dstptimesincetopologychange.value_namespace = name_space
                self.dot1dstptimesincetopologychange.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dStpTopChanges"):
                self.dot1dstptopchanges = value
                self.dot1dstptopchanges.value_namespace = name_space
                self.dot1dstptopchanges.value_namespace_prefix = name_space_prefix


    class Dot1Dtp(Entity):
        """
        
        
        .. attribute:: dot1dtpagingtime
        
        	The timeout period in seconds for aging out dynamically\-learned forwarding information. 802.1D\-1998 recommends a default of 300 seconds
        	**type**\:  int
        
        	**range:** 10..1000000
        
        	**units**\: seconds
        
        .. attribute:: dot1dtplearnedentrydiscards
        
        	The total number of Forwarding Database entries that have been or would have been learned, but have been discarded due to a lack of storage space in the Forwarding Database.  If this counter is increasing, it indicates that the Forwarding Database is regularly becoming full (a condition that has unpleasant performance effects on the subnetwork).  If this counter has a significant value but is not presently increasing, it indicates that the problem has been occurring but is not persistent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dtp, self).__init__()

            self.yang_name = "dot1dTp"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dtpagingtime = YLeaf(YType.int32, "dot1dTpAgingTime")

            self.dot1dtplearnedentrydiscards = YLeaf(YType.uint32, "dot1dTpLearnedEntryDiscards")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dot1dtpagingtime",
                            "dot1dtplearnedentrydiscards") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeMib.Dot1Dtp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dtp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.dot1dtpagingtime.is_set or
                self.dot1dtplearnedentrydiscards.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dot1dtpagingtime.yfilter != YFilter.not_set or
                self.dot1dtplearnedentrydiscards.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dot1dtpagingtime.is_set or self.dot1dtpagingtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dtpagingtime.get_name_leafdata())
            if (self.dot1dtplearnedentrydiscards.is_set or self.dot1dtplearnedentrydiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dot1dtplearnedentrydiscards.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTpAgingTime" or name == "dot1dTpLearnedEntryDiscards"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dot1dTpAgingTime"):
                self.dot1dtpagingtime = value
                self.dot1dtpagingtime.value_namespace = name_space
                self.dot1dtpagingtime.value_namespace_prefix = name_space_prefix
            if(value_path == "dot1dTpLearnedEntryDiscards"):
                self.dot1dtplearnedentrydiscards = value
                self.dot1dtplearnedentrydiscards.value_namespace = name_space
                self.dot1dtplearnedentrydiscards.value_namespace_prefix = name_space_prefix


    class Dot1Dbaseporttable(Entity):
        """
        A table that contains generic information about every
        port that is associated with this bridge.  Transparent,
        source\-route, and srt ports are included.
        
        .. attribute:: dot1dbaseportentry
        
        	A list of information for each port of the bridge
        	**type**\: list of    :py:class:`Dot1Dbaseportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dbaseporttable, self).__init__()

            self.yang_name = "dot1dBasePortTable"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dbaseportentry = YList(self)

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
                        super(BridgeMib.Dot1Dbaseporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dbaseporttable, self).__setattr__(name, value)


        class Dot1Dbaseportentry(Entity):
            """
            A list of information for each port of the bridge.
            
            .. attribute:: dot1dbaseport  <key>
            
            	The port number of the port for which this entry contains bridge management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dbaseportcircuit
            
            	For a port that (potentially) has the same value of dot1dBasePortIfIndex as another port on the same bridge. This object contains the name of an object instance unique to this port.  For example, in the case where multiple ports correspond one\-to\-one with multiple X.25 virtual circuits, this value might identify an (e.g., the first) object instance associated with the X.25 virtual circuit corresponding to this port.  For a port which has a unique value of dot1dBasePortIfIndex, this object can have the value { 0 0 }
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: dot1dbaseportdelayexceededdiscards
            
            	The number of frames discarded by this port due to excessive transit delay through the bridge.  It is incremented by both transparent and source route bridges
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dbaseportifindex
            
            	The value of the instance of the ifIndex object, defined in IF\-MIB, for the interface corresponding to this port
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1dbaseportmtuexceededdiscards
            
            	The number of frames discarded by this port due to an excessive size.  It is incremented by both transparent and source route bridges
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportcapabilities
            
            	Indicates the parts of IEEE 802.1D and 802.1Q that are optional on a per\-port basis, that are implemented by this device, and that are manageable through this MIB.  dot1qDot1qTagging(0), \-\- supports 802.1Q VLAN tagging of                       \-\- frames and GVRP. dot1qConfigurableAcceptableFrameTypes(1),                       \-\- allows modified values of                       \-\- dot1qPortAcceptableFrameTypes. dot1qIngressFiltering(2)                       \-\- supports the discarding of any                       \-\- frame received on a Port whose                       \-\- VLAN classification does not                       \-\- include that Port in its Member                       \-\- set
            	**type**\:   :py:class:`Dot1Dportcapabilities <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Dportcapabilities>`
            
            .. attribute:: dot1dportdefaultuserpriority
            
            	The default ingress User Priority for this port.  This only has effect on media, such as Ethernet, that do not support native User Priority.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dportgarpjointime
            
            	The GARP Join time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavealltime
            
            	The GARP LeaveAll time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavetime
            
            	The GARP Leave time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgmrpfailedregistrations
            
            	The total number of failed GMRP registrations, for any reason, in all VLANs, on this port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportgmrplastpduorigin
            
            	The Source MAC Address of the last GMRP message received on this port
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dportgmrpstatus
            
            	The administrative state of GMRP operation on this port.  The value enabled(1) indicates that GMRP is enabled on this port in all VLANs as long as dot1dGmrpStatus is also enabled(1). A value of disabled(2) indicates that GMRP is disabled on this port in all VLANs\: any GMRP packets received will be silently discarded, and no GMRP registrations will be propagated from other ports.  Setting this to a value of enabled(1) will be stored by the agent but will only take effect on the GMRP protocol operation if dot1dGmrpStatus also indicates the value enabled(1).  This object affects all GMRP Applicant and Registrar state machines on this port.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`Enabledstatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.Enabledstatus>`
            
            .. attribute:: dot1dportnumtrafficclasses
            
            	The number of egress traffic classes supported on this port.  This object may optionally be read\-only.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: dot1dportrestrictedgroupregistration
            
            	The state of Restricted Group Registration on this port. If the value of this control is true(1), then creation of a new dynamic entry is permitted only if there is a Static Filtering Entry for the VLAN concerned, in which the Registrar Administrative Control value is Normal Registration.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  bool
            
            .. attribute:: dot1qportacceptableframetypes
            
            	When this is admitOnlyVlanTagged(2), the device will discard untagged frames or Priority\-Tagged frames received on this port.  When admitAll(1), untagged frames or Priority\-Tagged frames received on this port will be accepted and assigned to a VID based on the PVID and VID Set for this port.  This control does not affect VLAN\-independent Bridge Protocol Data Unit (BPDU) frames, such as GVRP and Spanning Tree Protocol (STP).  It does affect VLAN\- dependent BPDU frames, such as GMRP.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`Dot1Qportacceptableframetypes <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Qportacceptableframetypes>`
            
            .. attribute:: dot1qportgvrpfailedregistrations
            
            	The total number of failed GVRP registrations, for any reason, on this port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1qportgvrplastpduorigin
            
            	The Source MAC Address of the last GVRP message received on this port
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1qportgvrpstatus
            
            	The state of GVRP operation on this port.  The value enabled(1) indicates that GVRP is enabled on this port, as long as dot1qGvrpStatus is also enabled for this device.  When disabled(2) but dot1qGvrpStatus is still enabled for the device, GVRP is disabled on this port\: any GVRP packets received will be silently discarded, and no GVRP registrations will be propagated from other ports.  This object affects all GVRP Applicant and Registrar state machines on this port.  A transition from disabled(2) to enabled(1) will cause a reset of all GVRP state machines on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`Enabledstatus <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.Enabledstatus>`
            
            .. attribute:: dot1qportingressfiltering
            
            	When this is true(1), the device will discard incoming frames for VLANs that do not include this Port in its  Member set.  When false(2), the port will accept all incoming frames.  This control does not affect VLAN\-independent BPDU frames, such as GVRP and STP.  It does affect VLAN\- dependent BPDU frames, such as GMRP.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  bool
            
            .. attribute:: dot1qportrestrictedvlanregistration
            
            	The state of Restricted VLAN Registration on this port. If the value of this control is true(1), then creation of a new dynamic VLAN entry is permitted only if there is a Static VLAN Registration Entry for the VLAN concerned, in which the Registrar Administrative Control value for this port is Normal Registration.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  bool
            
            .. attribute:: dot1qpvid
            
            	The PVID, the VLAN\-ID assigned to untagged frames or Priority\-Tagged frames received on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry, self).__init__()

                self.yang_name = "dot1dBasePortEntry"
                self.yang_parent_name = "dot1dBasePortTable"

                self.dot1dbaseport = YLeaf(YType.int32, "dot1dBasePort")

                self.dot1dbaseportcircuit = YLeaf(YType.str, "dot1dBasePortCircuit")

                self.dot1dbaseportdelayexceededdiscards = YLeaf(YType.uint32, "dot1dBasePortDelayExceededDiscards")

                self.dot1dbaseportifindex = YLeaf(YType.int32, "dot1dBasePortIfIndex")

                self.dot1dbaseportmtuexceededdiscards = YLeaf(YType.uint32, "dot1dBasePortMtuExceededDiscards")

                self.dot1dportcapabilities = YLeaf(YType.bits, "P-BRIDGE-MIB:dot1dPortCapabilities")

                self.dot1dportdefaultuserpriority = YLeaf(YType.int32, "P-BRIDGE-MIB:dot1dPortDefaultUserPriority")

                self.dot1dportgarpjointime = YLeaf(YType.int32, "P-BRIDGE-MIB:dot1dPortGarpJoinTime")

                self.dot1dportgarpleavealltime = YLeaf(YType.int32, "P-BRIDGE-MIB:dot1dPortGarpLeaveAllTime")

                self.dot1dportgarpleavetime = YLeaf(YType.int32, "P-BRIDGE-MIB:dot1dPortGarpLeaveTime")

                self.dot1dportgmrpfailedregistrations = YLeaf(YType.uint32, "P-BRIDGE-MIB:dot1dPortGmrpFailedRegistrations")

                self.dot1dportgmrplastpduorigin = YLeaf(YType.str, "P-BRIDGE-MIB:dot1dPortGmrpLastPduOrigin")

                self.dot1dportgmrpstatus = YLeaf(YType.enumeration, "P-BRIDGE-MIB:dot1dPortGmrpStatus")

                self.dot1dportnumtrafficclasses = YLeaf(YType.int32, "P-BRIDGE-MIB:dot1dPortNumTrafficClasses")

                self.dot1dportrestrictedgroupregistration = YLeaf(YType.boolean, "P-BRIDGE-MIB:dot1dPortRestrictedGroupRegistration")

                self.dot1qportacceptableframetypes = YLeaf(YType.enumeration, "Q-BRIDGE-MIB:dot1qPortAcceptableFrameTypes")

                self.dot1qportgvrpfailedregistrations = YLeaf(YType.uint32, "Q-BRIDGE-MIB:dot1qPortGvrpFailedRegistrations")

                self.dot1qportgvrplastpduorigin = YLeaf(YType.str, "Q-BRIDGE-MIB:dot1qPortGvrpLastPduOrigin")

                self.dot1qportgvrpstatus = YLeaf(YType.enumeration, "Q-BRIDGE-MIB:dot1qPortGvrpStatus")

                self.dot1qportingressfiltering = YLeaf(YType.boolean, "Q-BRIDGE-MIB:dot1qPortIngressFiltering")

                self.dot1qportrestrictedvlanregistration = YLeaf(YType.boolean, "Q-BRIDGE-MIB:dot1qPortRestrictedVlanRegistration")

                self.dot1qpvid = YLeaf(YType.uint32, "Q-BRIDGE-MIB:dot1qPvid")

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
                                "dot1dbaseportcircuit",
                                "dot1dbaseportdelayexceededdiscards",
                                "dot1dbaseportifindex",
                                "dot1dbaseportmtuexceededdiscards",
                                "dot1dportcapabilities",
                                "dot1dportdefaultuserpriority",
                                "dot1dportgarpjointime",
                                "dot1dportgarpleavealltime",
                                "dot1dportgarpleavetime",
                                "dot1dportgmrpfailedregistrations",
                                "dot1dportgmrplastpduorigin",
                                "dot1dportgmrpstatus",
                                "dot1dportnumtrafficclasses",
                                "dot1dportrestrictedgroupregistration",
                                "dot1qportacceptableframetypes",
                                "dot1qportgvrpfailedregistrations",
                                "dot1qportgvrplastpduorigin",
                                "dot1qportgvrpstatus",
                                "dot1qportingressfiltering",
                                "dot1qportrestrictedvlanregistration",
                                "dot1qpvid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry, self).__setattr__(name, value)

            class Dot1Qportacceptableframetypes(Enum):
                """
                Dot1Qportacceptableframetypes

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


            def has_data(self):
                return (
                    self.dot1dbaseport.is_set or
                    self.dot1dbaseportcircuit.is_set or
                    self.dot1dbaseportdelayexceededdiscards.is_set or
                    self.dot1dbaseportifindex.is_set or
                    self.dot1dbaseportmtuexceededdiscards.is_set or
                    self.dot1dportcapabilities.is_set or
                    self.dot1dportdefaultuserpriority.is_set or
                    self.dot1dportgarpjointime.is_set or
                    self.dot1dportgarpleavealltime.is_set or
                    self.dot1dportgarpleavetime.is_set or
                    self.dot1dportgmrpfailedregistrations.is_set or
                    self.dot1dportgmrplastpduorigin.is_set or
                    self.dot1dportgmrpstatus.is_set or
                    self.dot1dportnumtrafficclasses.is_set or
                    self.dot1dportrestrictedgroupregistration.is_set or
                    self.dot1qportacceptableframetypes.is_set or
                    self.dot1qportgvrpfailedregistrations.is_set or
                    self.dot1qportgvrplastpduorigin.is_set or
                    self.dot1qportgvrpstatus.is_set or
                    self.dot1qportingressfiltering.is_set or
                    self.dot1qportrestrictedvlanregistration.is_set or
                    self.dot1qpvid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dbaseport.yfilter != YFilter.not_set or
                    self.dot1dbaseportcircuit.yfilter != YFilter.not_set or
                    self.dot1dbaseportdelayexceededdiscards.yfilter != YFilter.not_set or
                    self.dot1dbaseportifindex.yfilter != YFilter.not_set or
                    self.dot1dbaseportmtuexceededdiscards.yfilter != YFilter.not_set or
                    self.dot1dportcapabilities.yfilter != YFilter.not_set or
                    self.dot1dportdefaultuserpriority.yfilter != YFilter.not_set or
                    self.dot1dportgarpjointime.yfilter != YFilter.not_set or
                    self.dot1dportgarpleavealltime.yfilter != YFilter.not_set or
                    self.dot1dportgarpleavetime.yfilter != YFilter.not_set or
                    self.dot1dportgmrpfailedregistrations.yfilter != YFilter.not_set or
                    self.dot1dportgmrplastpduorigin.yfilter != YFilter.not_set or
                    self.dot1dportgmrpstatus.yfilter != YFilter.not_set or
                    self.dot1dportnumtrafficclasses.yfilter != YFilter.not_set or
                    self.dot1dportrestrictedgroupregistration.yfilter != YFilter.not_set or
                    self.dot1qportacceptableframetypes.yfilter != YFilter.not_set or
                    self.dot1qportgvrpfailedregistrations.yfilter != YFilter.not_set or
                    self.dot1qportgvrplastpduorigin.yfilter != YFilter.not_set or
                    self.dot1qportgvrpstatus.yfilter != YFilter.not_set or
                    self.dot1qportingressfiltering.yfilter != YFilter.not_set or
                    self.dot1qportrestrictedvlanregistration.yfilter != YFilter.not_set or
                    self.dot1qpvid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dBasePortEntry" + "[dot1dBasePort='" + self.dot1dbaseport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BRIDGE-MIB:BRIDGE-MIB/dot1dBasePortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dbaseport.is_set or self.dot1dbaseport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseport.get_name_leafdata())
                if (self.dot1dbaseportcircuit.is_set or self.dot1dbaseportcircuit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseportcircuit.get_name_leafdata())
                if (self.dot1dbaseportdelayexceededdiscards.is_set or self.dot1dbaseportdelayexceededdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseportdelayexceededdiscards.get_name_leafdata())
                if (self.dot1dbaseportifindex.is_set or self.dot1dbaseportifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseportifindex.get_name_leafdata())
                if (self.dot1dbaseportmtuexceededdiscards.is_set or self.dot1dbaseportmtuexceededdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dbaseportmtuexceededdiscards.get_name_leafdata())
                if (self.dot1dportcapabilities.is_set or self.dot1dportcapabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportcapabilities.get_name_leafdata())
                if (self.dot1dportdefaultuserpriority.is_set or self.dot1dportdefaultuserpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportdefaultuserpriority.get_name_leafdata())
                if (self.dot1dportgarpjointime.is_set or self.dot1dportgarpjointime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgarpjointime.get_name_leafdata())
                if (self.dot1dportgarpleavealltime.is_set or self.dot1dportgarpleavealltime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgarpleavealltime.get_name_leafdata())
                if (self.dot1dportgarpleavetime.is_set or self.dot1dportgarpleavetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgarpleavetime.get_name_leafdata())
                if (self.dot1dportgmrpfailedregistrations.is_set or self.dot1dportgmrpfailedregistrations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgmrpfailedregistrations.get_name_leafdata())
                if (self.dot1dportgmrplastpduorigin.is_set or self.dot1dportgmrplastpduorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgmrplastpduorigin.get_name_leafdata())
                if (self.dot1dportgmrpstatus.is_set or self.dot1dportgmrpstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportgmrpstatus.get_name_leafdata())
                if (self.dot1dportnumtrafficclasses.is_set or self.dot1dportnumtrafficclasses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportnumtrafficclasses.get_name_leafdata())
                if (self.dot1dportrestrictedgroupregistration.is_set or self.dot1dportrestrictedgroupregistration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dportrestrictedgroupregistration.get_name_leafdata())
                if (self.dot1qportacceptableframetypes.is_set or self.dot1qportacceptableframetypes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportacceptableframetypes.get_name_leafdata())
                if (self.dot1qportgvrpfailedregistrations.is_set or self.dot1qportgvrpfailedregistrations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportgvrpfailedregistrations.get_name_leafdata())
                if (self.dot1qportgvrplastpduorigin.is_set or self.dot1qportgvrplastpduorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportgvrplastpduorigin.get_name_leafdata())
                if (self.dot1qportgvrpstatus.is_set or self.dot1qportgvrpstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportgvrpstatus.get_name_leafdata())
                if (self.dot1qportingressfiltering.is_set or self.dot1qportingressfiltering.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportingressfiltering.get_name_leafdata())
                if (self.dot1qportrestrictedvlanregistration.is_set or self.dot1qportrestrictedvlanregistration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qportrestrictedvlanregistration.get_name_leafdata())
                if (self.dot1qpvid.is_set or self.dot1qpvid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1qpvid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dBasePort" or name == "dot1dBasePortCircuit" or name == "dot1dBasePortDelayExceededDiscards" or name == "dot1dBasePortIfIndex" or name == "dot1dBasePortMtuExceededDiscards" or name == "dot1dPortCapabilities" or name == "dot1dPortDefaultUserPriority" or name == "dot1dPortGarpJoinTime" or name == "dot1dPortGarpLeaveAllTime" or name == "dot1dPortGarpLeaveTime" or name == "dot1dPortGmrpFailedRegistrations" or name == "dot1dPortGmrpLastPduOrigin" or name == "dot1dPortGmrpStatus" or name == "dot1dPortNumTrafficClasses" or name == "dot1dPortRestrictedGroupRegistration" or name == "dot1qPortAcceptableFrameTypes" or name == "dot1qPortGvrpFailedRegistrations" or name == "dot1qPortGvrpLastPduOrigin" or name == "dot1qPortGvrpStatus" or name == "dot1qPortIngressFiltering" or name == "dot1qPortRestrictedVlanRegistration" or name == "dot1qPvid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dBasePort"):
                    self.dot1dbaseport = value
                    self.dot1dbaseport.value_namespace = name_space
                    self.dot1dbaseport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dBasePortCircuit"):
                    self.dot1dbaseportcircuit = value
                    self.dot1dbaseportcircuit.value_namespace = name_space
                    self.dot1dbaseportcircuit.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dBasePortDelayExceededDiscards"):
                    self.dot1dbaseportdelayexceededdiscards = value
                    self.dot1dbaseportdelayexceededdiscards.value_namespace = name_space
                    self.dot1dbaseportdelayexceededdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dBasePortIfIndex"):
                    self.dot1dbaseportifindex = value
                    self.dot1dbaseportifindex.value_namespace = name_space
                    self.dot1dbaseportifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dBasePortMtuExceededDiscards"):
                    self.dot1dbaseportmtuexceededdiscards = value
                    self.dot1dbaseportmtuexceededdiscards.value_namespace = name_space
                    self.dot1dbaseportmtuexceededdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortCapabilities"):
                    self.dot1dportcapabilities[value] = True
                if(value_path == "dot1dPortDefaultUserPriority"):
                    self.dot1dportdefaultuserpriority = value
                    self.dot1dportdefaultuserpriority.value_namespace = name_space
                    self.dot1dportdefaultuserpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGarpJoinTime"):
                    self.dot1dportgarpjointime = value
                    self.dot1dportgarpjointime.value_namespace = name_space
                    self.dot1dportgarpjointime.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGarpLeaveAllTime"):
                    self.dot1dportgarpleavealltime = value
                    self.dot1dportgarpleavealltime.value_namespace = name_space
                    self.dot1dportgarpleavealltime.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGarpLeaveTime"):
                    self.dot1dportgarpleavetime = value
                    self.dot1dportgarpleavetime.value_namespace = name_space
                    self.dot1dportgarpleavetime.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGmrpFailedRegistrations"):
                    self.dot1dportgmrpfailedregistrations = value
                    self.dot1dportgmrpfailedregistrations.value_namespace = name_space
                    self.dot1dportgmrpfailedregistrations.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGmrpLastPduOrigin"):
                    self.dot1dportgmrplastpduorigin = value
                    self.dot1dportgmrplastpduorigin.value_namespace = name_space
                    self.dot1dportgmrplastpduorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortGmrpStatus"):
                    self.dot1dportgmrpstatus = value
                    self.dot1dportgmrpstatus.value_namespace = name_space
                    self.dot1dportgmrpstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortNumTrafficClasses"):
                    self.dot1dportnumtrafficclasses = value
                    self.dot1dportnumtrafficclasses.value_namespace = name_space
                    self.dot1dportnumtrafficclasses.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dPortRestrictedGroupRegistration"):
                    self.dot1dportrestrictedgroupregistration = value
                    self.dot1dportrestrictedgroupregistration.value_namespace = name_space
                    self.dot1dportrestrictedgroupregistration.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortAcceptableFrameTypes"):
                    self.dot1qportacceptableframetypes = value
                    self.dot1qportacceptableframetypes.value_namespace = name_space
                    self.dot1qportacceptableframetypes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortGvrpFailedRegistrations"):
                    self.dot1qportgvrpfailedregistrations = value
                    self.dot1qportgvrpfailedregistrations.value_namespace = name_space
                    self.dot1qportgvrpfailedregistrations.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortGvrpLastPduOrigin"):
                    self.dot1qportgvrplastpduorigin = value
                    self.dot1qportgvrplastpduorigin.value_namespace = name_space
                    self.dot1qportgvrplastpduorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortGvrpStatus"):
                    self.dot1qportgvrpstatus = value
                    self.dot1qportgvrpstatus.value_namespace = name_space
                    self.dot1qportgvrpstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortIngressFiltering"):
                    self.dot1qportingressfiltering = value
                    self.dot1qportingressfiltering.value_namespace = name_space
                    self.dot1qportingressfiltering.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPortRestrictedVlanRegistration"):
                    self.dot1qportrestrictedvlanregistration = value
                    self.dot1qportrestrictedvlanregistration.value_namespace = name_space
                    self.dot1qportrestrictedvlanregistration.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1qPvid"):
                    self.dot1qpvid = value
                    self.dot1qpvid.value_namespace = name_space
                    self.dot1qpvid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dbaseportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dbaseportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dBasePortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dBasePortEntry"):
                for c in self.dot1dbaseportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dbaseportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dBasePortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dstpporttable(Entity):
        """
        A table that contains port\-specific information
        for the Spanning Tree Protocol.
        
        .. attribute:: dot1dstpportentry
        
        	A list of information maintained by every port about the Spanning Tree Protocol state for that port
        	**type**\: list of    :py:class:`Dot1Dstpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dstpporttable, self).__init__()

            self.yang_name = "dot1dStpPortTable"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dstpportentry = YList(self)

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
                        super(BridgeMib.Dot1Dstpporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dstpporttable, self).__setattr__(name, value)


        class Dot1Dstpportentry(Entity):
            """
            A list of information maintained by every port about
            the Spanning Tree Protocol state for that port.
            
            .. attribute:: dot1dstpport  <key>
            
            	The port number of the port for which this entry contains Spanning Tree Protocol management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportdesignatedbridge
            
            	The Bridge Identifier of the bridge that this port considers to be the Designated Bridge for this port's segment
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportdesignatedcost
            
            	The path cost of the Designated Port of the segment connected to this port.  This value is compared to the Root Path Cost field in received bridge PDUs
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dstpportdesignatedport
            
            	The Port Identifier of the port on the Designated Bridge for this port's segment
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: dot1dstpportdesignatedroot
            
            	The unique Bridge Identifier of the Bridge recorded as the Root in the Configuration BPDUs transmitted by the Designated Bridge for the segment to which the port is attached
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportenable
            
            	The enabled/disabled status of the port
            	**type**\:   :py:class:`Dot1Dstpportenable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1Dstpportenable>`
            
            .. attribute:: dot1dstpportforwardtransitions
            
            	The number of times this port has transitioned from the Learning state to the Forwarding state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dstpportpathcost
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to  the speed of the attached LAN.  New implementations should support dot1dStpPortPathCost32. If the port path costs exceeds the maximum value of this object then this object should report the maximum value, namely 65535.  Applications should try to read the dot1dStpPortPathCost32 object if this object reports the maximum value
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportpathcost32
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  This object replaces dot1dStpPortPathCost to support IEEE 802.1t
            	**type**\:  int
            
            	**range:** 1..200000000
            
            .. attribute:: dot1dstpportpriority
            
            	The value of the priority field that is contained in the first (in network byte order) octet of the (2 octet long) Port ID.  The other octet of the Port ID is given by the value of dot1dStpPort. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-240, in steps of 16
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: dot1dstpportstate
            
            	The port's current state, as defined by application of the Spanning Tree Protocol.  This state controls what action a port takes on reception of a frame.  If the bridge has detected a port that is malfunctioning, it will place that port into the broken(6) state.  For ports that are disabled (see dot1dStpPortEnable), this object will have a value of disabled(1)
            	**type**\:   :py:class:`Dot1Dstpportstate <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1Dstpportstate>`
            
            .. attribute:: stpxlongstpportpathcost
            
            	The contribution of this port to the path cost (in 32 bits value) of paths towards the spanning tree root which include this port.  This object is used to configure the spanning tree port path cost in 32 bits value range when the stpxSpanningTreePathCostOperMode is long(2).  If the stpxSpanningTreePathCostOperMode is short(1), this  MIB object is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry, self).__init__()

                self.yang_name = "dot1dStpPortEntry"
                self.yang_parent_name = "dot1dStpPortTable"

                self.dot1dstpport = YLeaf(YType.int32, "dot1dStpPort")

                self.dot1dstpportdesignatedbridge = YLeaf(YType.str, "dot1dStpPortDesignatedBridge")

                self.dot1dstpportdesignatedcost = YLeaf(YType.int32, "dot1dStpPortDesignatedCost")

                self.dot1dstpportdesignatedport = YLeaf(YType.str, "dot1dStpPortDesignatedPort")

                self.dot1dstpportdesignatedroot = YLeaf(YType.str, "dot1dStpPortDesignatedRoot")

                self.dot1dstpportenable = YLeaf(YType.enumeration, "dot1dStpPortEnable")

                self.dot1dstpportforwardtransitions = YLeaf(YType.uint32, "dot1dStpPortForwardTransitions")

                self.dot1dstpportpathcost = YLeaf(YType.int32, "dot1dStpPortPathCost")

                self.dot1dstpportpathcost32 = YLeaf(YType.int32, "dot1dStpPortPathCost32")

                self.dot1dstpportpriority = YLeaf(YType.int32, "dot1dStpPortPriority")

                self.dot1dstpportstate = YLeaf(YType.enumeration, "dot1dStpPortState")

                self.stpxlongstpportpathcost = YLeaf(YType.uint32, "CISCO-STP-EXTENSIONS-MIB:stpxLongStpPortPathCost")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dstpport",
                                "dot1dstpportdesignatedbridge",
                                "dot1dstpportdesignatedcost",
                                "dot1dstpportdesignatedport",
                                "dot1dstpportdesignatedroot",
                                "dot1dstpportenable",
                                "dot1dstpportforwardtransitions",
                                "dot1dstpportpathcost",
                                "dot1dstpportpathcost32",
                                "dot1dstpportpriority",
                                "dot1dstpportstate",
                                "stpxlongstpportpathcost") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry, self).__setattr__(name, value)

            class Dot1Dstpportenable(Enum):
                """
                Dot1Dstpportenable

                The enabled/disabled status of the port.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Dot1Dstpportstate(Enum):
                """
                Dot1Dstpportstate

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


            def has_data(self):
                return (
                    self.dot1dstpport.is_set or
                    self.dot1dstpportdesignatedbridge.is_set or
                    self.dot1dstpportdesignatedcost.is_set or
                    self.dot1dstpportdesignatedport.is_set or
                    self.dot1dstpportdesignatedroot.is_set or
                    self.dot1dstpportenable.is_set or
                    self.dot1dstpportforwardtransitions.is_set or
                    self.dot1dstpportpathcost.is_set or
                    self.dot1dstpportpathcost32.is_set or
                    self.dot1dstpportpriority.is_set or
                    self.dot1dstpportstate.is_set or
                    self.stpxlongstpportpathcost.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dstpport.yfilter != YFilter.not_set or
                    self.dot1dstpportdesignatedbridge.yfilter != YFilter.not_set or
                    self.dot1dstpportdesignatedcost.yfilter != YFilter.not_set or
                    self.dot1dstpportdesignatedport.yfilter != YFilter.not_set or
                    self.dot1dstpportdesignatedroot.yfilter != YFilter.not_set or
                    self.dot1dstpportenable.yfilter != YFilter.not_set or
                    self.dot1dstpportforwardtransitions.yfilter != YFilter.not_set or
                    self.dot1dstpportpathcost.yfilter != YFilter.not_set or
                    self.dot1dstpportpathcost32.yfilter != YFilter.not_set or
                    self.dot1dstpportpriority.yfilter != YFilter.not_set or
                    self.dot1dstpportstate.yfilter != YFilter.not_set or
                    self.stpxlongstpportpathcost.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dStpPortEntry" + "[dot1dStpPort='" + self.dot1dstpport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BRIDGE-MIB:BRIDGE-MIB/dot1dStpPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dstpport.is_set or self.dot1dstpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpport.get_name_leafdata())
                if (self.dot1dstpportdesignatedbridge.is_set or self.dot1dstpportdesignatedbridge.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportdesignatedbridge.get_name_leafdata())
                if (self.dot1dstpportdesignatedcost.is_set or self.dot1dstpportdesignatedcost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportdesignatedcost.get_name_leafdata())
                if (self.dot1dstpportdesignatedport.is_set or self.dot1dstpportdesignatedport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportdesignatedport.get_name_leafdata())
                if (self.dot1dstpportdesignatedroot.is_set or self.dot1dstpportdesignatedroot.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportdesignatedroot.get_name_leafdata())
                if (self.dot1dstpportenable.is_set or self.dot1dstpportenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportenable.get_name_leafdata())
                if (self.dot1dstpportforwardtransitions.is_set or self.dot1dstpportforwardtransitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportforwardtransitions.get_name_leafdata())
                if (self.dot1dstpportpathcost.is_set or self.dot1dstpportpathcost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportpathcost.get_name_leafdata())
                if (self.dot1dstpportpathcost32.is_set or self.dot1dstpportpathcost32.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportpathcost32.get_name_leafdata())
                if (self.dot1dstpportpriority.is_set or self.dot1dstpportpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportpriority.get_name_leafdata())
                if (self.dot1dstpportstate.is_set or self.dot1dstpportstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstpportstate.get_name_leafdata())
                if (self.stpxlongstpportpathcost.is_set or self.stpxlongstpportpathcost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxlongstpportpathcost.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dStpPort" or name == "dot1dStpPortDesignatedBridge" or name == "dot1dStpPortDesignatedCost" or name == "dot1dStpPortDesignatedPort" or name == "dot1dStpPortDesignatedRoot" or name == "dot1dStpPortEnable" or name == "dot1dStpPortForwardTransitions" or name == "dot1dStpPortPathCost" or name == "dot1dStpPortPathCost32" or name == "dot1dStpPortPriority" or name == "dot1dStpPortState" or name == "stpxLongStpPortPathCost"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dStpPort"):
                    self.dot1dstpport = value
                    self.dot1dstpport.value_namespace = name_space
                    self.dot1dstpport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortDesignatedBridge"):
                    self.dot1dstpportdesignatedbridge = value
                    self.dot1dstpportdesignatedbridge.value_namespace = name_space
                    self.dot1dstpportdesignatedbridge.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortDesignatedCost"):
                    self.dot1dstpportdesignatedcost = value
                    self.dot1dstpportdesignatedcost.value_namespace = name_space
                    self.dot1dstpportdesignatedcost.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortDesignatedPort"):
                    self.dot1dstpportdesignatedport = value
                    self.dot1dstpportdesignatedport.value_namespace = name_space
                    self.dot1dstpportdesignatedport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortDesignatedRoot"):
                    self.dot1dstpportdesignatedroot = value
                    self.dot1dstpportdesignatedroot.value_namespace = name_space
                    self.dot1dstpportdesignatedroot.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortEnable"):
                    self.dot1dstpportenable = value
                    self.dot1dstpportenable.value_namespace = name_space
                    self.dot1dstpportenable.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortForwardTransitions"):
                    self.dot1dstpportforwardtransitions = value
                    self.dot1dstpportforwardtransitions.value_namespace = name_space
                    self.dot1dstpportforwardtransitions.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortPathCost"):
                    self.dot1dstpportpathcost = value
                    self.dot1dstpportpathcost.value_namespace = name_space
                    self.dot1dstpportpathcost.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortPathCost32"):
                    self.dot1dstpportpathcost32 = value
                    self.dot1dstpportpathcost32.value_namespace = name_space
                    self.dot1dstpportpathcost32.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortPriority"):
                    self.dot1dstpportpriority = value
                    self.dot1dstpportpriority.value_namespace = name_space
                    self.dot1dstpportpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStpPortState"):
                    self.dot1dstpportstate = value
                    self.dot1dstpportstate.value_namespace = name_space
                    self.dot1dstpportstate.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxLongStpPortPathCost"):
                    self.stpxlongstpportpathcost = value
                    self.stpxlongstpportpathcost.value_namespace = name_space
                    self.stpxlongstpportpathcost.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dstpportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dstpportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dStpPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dStpPortEntry"):
                for c in self.dot1dstpportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dstpportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dStpPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dtpfdbtable(Entity):
        """
        A table that contains information about unicast
        entries for which the bridge has forwarding and/or
        filtering information.  This information is used
        by the transparent bridging function in
        determining how to propagate a received frame.
        
        .. attribute:: dot1dtpfdbentry
        
        	Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information
        	**type**\: list of    :py:class:`Dot1Dtpfdbentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dtpfdbtable, self).__init__()

            self.yang_name = "dot1dTpFdbTable"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dtpfdbentry = YList(self)

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
                        super(BridgeMib.Dot1Dtpfdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dtpfdbtable, self).__setattr__(name, value)


        class Dot1Dtpfdbentry(Entity):
            """
            Information about a specific unicast MAC address
            for which the bridge has some forwarding and/or
            filtering information.
            
            .. attribute:: dot1dtpfdbaddress  <key>
            
            	A unicast MAC address for which the bridge has forwarding and/or filtering information
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1dTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned, but that the bridge does have some forwarding/filtering information about this address (e.g., in the dot1dStaticTable).  Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1dTpFdbStatus is not learned(3)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This would         include the case where some other MIB object         (not the corresponding instance of         dot1dTpFdbPort, nor an entry in the         dot1dStaticTable) is being used to determine if         and how frames addressed to the value of the         corresponding instance of dot1dTpFdbAddress are         being forwarded.     invalid(2) \- this entry is no longer valid (e.g.,         it was learned but has since aged out), but has         not yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1dTpFdbPort was learned, and is being         used.     self(4) \- the value of the corresponding instance of         dot1dTpFdbAddress represents one of the bridge's         addresses.  The corresponding instance of         dot1dTpFdbPort indicates which of the bridge's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1dTpFdbAddress is also the value of an         existing instance of dot1dStaticAddress
            	**type**\:   :py:class:`Dot1Dtpfdbstatus <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1Dtpfdbstatus>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry, self).__init__()

                self.yang_name = "dot1dTpFdbEntry"
                self.yang_parent_name = "dot1dTpFdbTable"

                self.dot1dtpfdbaddress = YLeaf(YType.str, "dot1dTpFdbAddress")

                self.dot1dtpfdbport = YLeaf(YType.int32, "dot1dTpFdbPort")

                self.dot1dtpfdbstatus = YLeaf(YType.enumeration, "dot1dTpFdbStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dtpfdbaddress",
                                "dot1dtpfdbport",
                                "dot1dtpfdbstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry, self).__setattr__(name, value)

            class Dot1Dtpfdbstatus(Enum):
                """
                Dot1Dtpfdbstatus

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


            def has_data(self):
                return (
                    self.dot1dtpfdbaddress.is_set or
                    self.dot1dtpfdbport.is_set or
                    self.dot1dtpfdbstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dtpfdbaddress.yfilter != YFilter.not_set or
                    self.dot1dtpfdbport.yfilter != YFilter.not_set or
                    self.dot1dtpfdbstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dTpFdbEntry" + "[dot1dTpFdbAddress='" + self.dot1dtpfdbaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BRIDGE-MIB:BRIDGE-MIB/dot1dTpFdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dtpfdbaddress.is_set or self.dot1dtpfdbaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpfdbaddress.get_name_leafdata())
                if (self.dot1dtpfdbport.is_set or self.dot1dtpfdbport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpfdbport.get_name_leafdata())
                if (self.dot1dtpfdbstatus.is_set or self.dot1dtpfdbstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpfdbstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dTpFdbAddress" or name == "dot1dTpFdbPort" or name == "dot1dTpFdbStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dTpFdbAddress"):
                    self.dot1dtpfdbaddress = value
                    self.dot1dtpfdbaddress.value_namespace = name_space
                    self.dot1dtpfdbaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpFdbPort"):
                    self.dot1dtpfdbport = value
                    self.dot1dtpfdbport.value_namespace = name_space
                    self.dot1dtpfdbport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpFdbStatus"):
                    self.dot1dtpfdbstatus = value
                    self.dot1dtpfdbstatus.value_namespace = name_space
                    self.dot1dtpfdbstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dtpfdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dtpfdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTpFdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dTpFdbEntry"):
                for c in self.dot1dtpfdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dtpfdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTpFdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot1Dtpporttable(Entity):
        """
        A table that contains information about every port that
        is associated with this transparent bridge.
        
        .. attribute:: dot1dtpportentry
        
        	A list of information for each port of a transparent bridge
        	**type**\: list of    :py:class:`Dot1Dtpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dtpporttable, self).__init__()

            self.yang_name = "dot1dTpPortTable"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dtpportentry = YList(self)

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
                        super(BridgeMib.Dot1Dtpporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dtpporttable, self).__setattr__(name, value)


        class Dot1Dtpportentry(Entity):
            """
            A list of information for each port of a transparent
            bridge.
            
            .. attribute:: dot1dtpport  <key>
            
            	The port number of the port for which this entry contains Transparent bridging management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dtpportindiscards
            
            	Count of received valid frames that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportmaxinfo
            
            	The maximum size of the INFO (non\-MAC) field that  this port will receive or transmit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: dot1dtpportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry, self).__init__()

                self.yang_name = "dot1dTpPortEntry"
                self.yang_parent_name = "dot1dTpPortTable"

                self.dot1dtpport = YLeaf(YType.int32, "dot1dTpPort")

                self.dot1dtpportindiscards = YLeaf(YType.uint32, "dot1dTpPortInDiscards")

                self.dot1dtpportinframes = YLeaf(YType.uint32, "dot1dTpPortInFrames")

                self.dot1dtpportmaxinfo = YLeaf(YType.int32, "dot1dTpPortMaxInfo")

                self.dot1dtpportoutframes = YLeaf(YType.uint32, "dot1dTpPortOutFrames")

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
                                "dot1dtpportindiscards",
                                "dot1dtpportinframes",
                                "dot1dtpportmaxinfo",
                                "dot1dtpportoutframes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot1dtpport.is_set or
                    self.dot1dtpportindiscards.is_set or
                    self.dot1dtpportinframes.is_set or
                    self.dot1dtpportmaxinfo.is_set or
                    self.dot1dtpportoutframes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dtpport.yfilter != YFilter.not_set or
                    self.dot1dtpportindiscards.yfilter != YFilter.not_set or
                    self.dot1dtpportinframes.yfilter != YFilter.not_set or
                    self.dot1dtpportmaxinfo.yfilter != YFilter.not_set or
                    self.dot1dtpportoutframes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dTpPortEntry" + "[dot1dTpPort='" + self.dot1dtpport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BRIDGE-MIB:BRIDGE-MIB/dot1dTpPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dtpport.is_set or self.dot1dtpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpport.get_name_leafdata())
                if (self.dot1dtpportindiscards.is_set or self.dot1dtpportindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportindiscards.get_name_leafdata())
                if (self.dot1dtpportinframes.is_set or self.dot1dtpportinframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportinframes.get_name_leafdata())
                if (self.dot1dtpportmaxinfo.is_set or self.dot1dtpportmaxinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportmaxinfo.get_name_leafdata())
                if (self.dot1dtpportoutframes.is_set or self.dot1dtpportoutframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dtpportoutframes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dTpPort" or name == "dot1dTpPortInDiscards" or name == "dot1dTpPortInFrames" or name == "dot1dTpPortMaxInfo" or name == "dot1dTpPortOutFrames"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dTpPort"):
                    self.dot1dtpport = value
                    self.dot1dtpport.value_namespace = name_space
                    self.dot1dtpport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortInDiscards"):
                    self.dot1dtpportindiscards = value
                    self.dot1dtpportindiscards.value_namespace = name_space
                    self.dot1dtpportindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortInFrames"):
                    self.dot1dtpportinframes = value
                    self.dot1dtpportinframes.value_namespace = name_space
                    self.dot1dtpportinframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortMaxInfo"):
                    self.dot1dtpportmaxinfo = value
                    self.dot1dtpportmaxinfo.value_namespace = name_space
                    self.dot1dtpportmaxinfo.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dTpPortOutFrames"):
                    self.dot1dtpportoutframes = value
                    self.dot1dtpportoutframes.value_namespace = name_space
                    self.dot1dtpportoutframes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dtpportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dtpportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dTpPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dTpPortEntry"):
                for c in self.dot1dtpportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dtpportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dTpPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Dot1Dstaticentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable.Dot1Dstaticentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            super(BridgeMib.Dot1Dstatictable, self).__init__()

            self.yang_name = "dot1dStaticTable"
            self.yang_parent_name = "BRIDGE-MIB"

            self.dot1dstaticentry = YList(self)

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
                        super(BridgeMib.Dot1Dstatictable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeMib.Dot1Dstatictable, self).__setattr__(name, value)


        class Dot1Dstaticentry(Entity):
            """
            Filtering information configured into the bridge by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific destination address are allowed to
            be forwarded.
            
            .. attribute:: dot1dstaticaddress  <key>
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object can take the value of a unicast address, a group address, or the broadcast address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dstaticreceiveport  <key>
            
            	Either the value '0', or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the bridge for which there is no other applicable entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1dstaticallowedtogoto
            
            	The set of ports to which frames received from a specific port and destined for a specific MAC address, are allowed to be forwarded.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc.  Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the bridge is represented by a single bit within the value of this object.  If that bit has a value of '1', then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  (Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.)  The default value of this object is a string of ones of appropriate length.  The value of this object may exceed the required minimum maximum message size of some SNMP transport (484 bytes, in the case of SNMP over UDP, see RFC 3417, section 3.2). SNMP engines on bridges supporting a large number of ports must support appropriate maximum message sizes
            	**type**\:  str
            
            	**length:** 0..512
            
            .. attribute:: dot1dstaticstatus
            
            	This object indicates the status of this entry. The default value is permanent(3).     other(1) \- this entry is currently in use but the         conditions under which it will remain so are         different from each of the following values.     invalid(2) \- writing this value to the object         removes the corresponding entry.     permanent(3) \- this entry is currently in use and         will remain so after the next reset of the         bridge.     deleteOnReset(4) \- this entry is currently in use         and will remain so until the next reset of the         bridge.     deleteOnTimeout(5) \- this entry is currently in use         and will remain so until it is aged out
            	**type**\:   :py:class:`Dot1Dstaticstatus <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable.Dot1Dstaticentry.Dot1Dstaticstatus>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                super(BridgeMib.Dot1Dstatictable.Dot1Dstaticentry, self).__init__()

                self.yang_name = "dot1dStaticEntry"
                self.yang_parent_name = "dot1dStaticTable"

                self.dot1dstaticaddress = YLeaf(YType.str, "dot1dStaticAddress")

                self.dot1dstaticreceiveport = YLeaf(YType.int32, "dot1dStaticReceivePort")

                self.dot1dstaticallowedtogoto = YLeaf(YType.str, "dot1dStaticAllowedToGoTo")

                self.dot1dstaticstatus = YLeaf(YType.enumeration, "dot1dStaticStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot1dstaticaddress",
                                "dot1dstaticreceiveport",
                                "dot1dstaticallowedtogoto",
                                "dot1dstaticstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeMib.Dot1Dstatictable.Dot1Dstaticentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeMib.Dot1Dstatictable.Dot1Dstaticentry, self).__setattr__(name, value)

            class Dot1Dstaticstatus(Enum):
                """
                Dot1Dstaticstatus

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


            def has_data(self):
                return (
                    self.dot1dstaticaddress.is_set or
                    self.dot1dstaticreceiveport.is_set or
                    self.dot1dstaticallowedtogoto.is_set or
                    self.dot1dstaticstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot1dstaticaddress.yfilter != YFilter.not_set or
                    self.dot1dstaticreceiveport.yfilter != YFilter.not_set or
                    self.dot1dstaticallowedtogoto.yfilter != YFilter.not_set or
                    self.dot1dstaticstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot1dStaticEntry" + "[dot1dStaticAddress='" + self.dot1dstaticaddress.get() + "']" + "[dot1dStaticReceivePort='" + self.dot1dstaticreceiveport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "BRIDGE-MIB:BRIDGE-MIB/dot1dStaticTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot1dstaticaddress.is_set or self.dot1dstaticaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstaticaddress.get_name_leafdata())
                if (self.dot1dstaticreceiveport.is_set or self.dot1dstaticreceiveport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstaticreceiveport.get_name_leafdata())
                if (self.dot1dstaticallowedtogoto.is_set or self.dot1dstaticallowedtogoto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstaticallowedtogoto.get_name_leafdata())
                if (self.dot1dstaticstatus.is_set or self.dot1dstaticstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot1dstaticstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot1dStaticAddress" or name == "dot1dStaticReceivePort" or name == "dot1dStaticAllowedToGoTo" or name == "dot1dStaticStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot1dStaticAddress"):
                    self.dot1dstaticaddress = value
                    self.dot1dstaticaddress.value_namespace = name_space
                    self.dot1dstaticaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStaticReceivePort"):
                    self.dot1dstaticreceiveport = value
                    self.dot1dstaticreceiveport.value_namespace = name_space
                    self.dot1dstaticreceiveport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStaticAllowedToGoTo"):
                    self.dot1dstaticallowedtogoto = value
                    self.dot1dstaticallowedtogoto.value_namespace = name_space
                    self.dot1dstaticallowedtogoto.value_namespace_prefix = name_space_prefix
                if(value_path == "dot1dStaticStatus"):
                    self.dot1dstaticstatus = value
                    self.dot1dstaticstatus.value_namespace = name_space
                    self.dot1dstaticstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot1dstaticentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot1dstaticentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot1dStaticTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "BRIDGE-MIB:BRIDGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot1dStaticEntry"):
                for c in self.dot1dstaticentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeMib.Dot1Dstatictable.Dot1Dstaticentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot1dstaticentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot1dStaticEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dot1dbase is not None and self.dot1dbase.has_data()) or
            (self.dot1dbaseporttable is not None and self.dot1dbaseporttable.has_data()) or
            (self.dot1dstatictable is not None and self.dot1dstatictable.has_data()) or
            (self.dot1dstp is not None and self.dot1dstp.has_data()) or
            (self.dot1dstpporttable is not None and self.dot1dstpporttable.has_data()) or
            (self.dot1dtp is not None and self.dot1dtp.has_data()) or
            (self.dot1dtpfdbtable is not None and self.dot1dtpfdbtable.has_data()) or
            (self.dot1dtpporttable is not None and self.dot1dtpporttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dot1dbase is not None and self.dot1dbase.has_operation()) or
            (self.dot1dbaseporttable is not None and self.dot1dbaseporttable.has_operation()) or
            (self.dot1dstatictable is not None and self.dot1dstatictable.has_operation()) or
            (self.dot1dstp is not None and self.dot1dstp.has_operation()) or
            (self.dot1dstpporttable is not None and self.dot1dstpporttable.has_operation()) or
            (self.dot1dtp is not None and self.dot1dtp.has_operation()) or
            (self.dot1dtpfdbtable is not None and self.dot1dtpfdbtable.has_operation()) or
            (self.dot1dtpporttable is not None and self.dot1dtpporttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "BRIDGE-MIB:BRIDGE-MIB" + path_buffer

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

        if (child_yang_name == "dot1dBase"):
            if (self.dot1dbase is None):
                self.dot1dbase = BridgeMib.Dot1Dbase()
                self.dot1dbase.parent = self
                self._children_name_map["dot1dbase"] = "dot1dBase"
            return self.dot1dbase

        if (child_yang_name == "dot1dBasePortTable"):
            if (self.dot1dbaseporttable is None):
                self.dot1dbaseporttable = BridgeMib.Dot1Dbaseporttable()
                self.dot1dbaseporttable.parent = self
                self._children_name_map["dot1dbaseporttable"] = "dot1dBasePortTable"
            return self.dot1dbaseporttable

        if (child_yang_name == "dot1dStaticTable"):
            if (self.dot1dstatictable is None):
                self.dot1dstatictable = BridgeMib.Dot1Dstatictable()
                self.dot1dstatictable.parent = self
                self._children_name_map["dot1dstatictable"] = "dot1dStaticTable"
            return self.dot1dstatictable

        if (child_yang_name == "dot1dStp"):
            if (self.dot1dstp is None):
                self.dot1dstp = BridgeMib.Dot1Dstp()
                self.dot1dstp.parent = self
                self._children_name_map["dot1dstp"] = "dot1dStp"
            return self.dot1dstp

        if (child_yang_name == "dot1dStpPortTable"):
            if (self.dot1dstpporttable is None):
                self.dot1dstpporttable = BridgeMib.Dot1Dstpporttable()
                self.dot1dstpporttable.parent = self
                self._children_name_map["dot1dstpporttable"] = "dot1dStpPortTable"
            return self.dot1dstpporttable

        if (child_yang_name == "dot1dTp"):
            if (self.dot1dtp is None):
                self.dot1dtp = BridgeMib.Dot1Dtp()
                self.dot1dtp.parent = self
                self._children_name_map["dot1dtp"] = "dot1dTp"
            return self.dot1dtp

        if (child_yang_name == "dot1dTpFdbTable"):
            if (self.dot1dtpfdbtable is None):
                self.dot1dtpfdbtable = BridgeMib.Dot1Dtpfdbtable()
                self.dot1dtpfdbtable.parent = self
                self._children_name_map["dot1dtpfdbtable"] = "dot1dTpFdbTable"
            return self.dot1dtpfdbtable

        if (child_yang_name == "dot1dTpPortTable"):
            if (self.dot1dtpporttable is None):
                self.dot1dtpporttable = BridgeMib.Dot1Dtpporttable()
                self.dot1dtpporttable.parent = self
                self._children_name_map["dot1dtpporttable"] = "dot1dTpPortTable"
            return self.dot1dtpporttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dot1dBase" or name == "dot1dBasePortTable" or name == "dot1dStaticTable" or name == "dot1dStp" or name == "dot1dStpPortTable" or name == "dot1dTp" or name == "dot1dTpFdbTable" or name == "dot1dTpPortTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BridgeMib()
        return self._top_entity

