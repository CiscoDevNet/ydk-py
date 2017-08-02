""" IF_MIB 

The MIB module to describe generic objects for network
interface sub\-layers.  This MIB is an updated version of
MIB\-II's ifTable, and incorporates the extensions defined in
RFC 1229.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IfMib(Entity):
    """
    
    
    .. attribute:: ifmibobjects
    
    	
    	**type**\:   :py:class:`Ifmibobjects <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifmibobjects>`
    
    .. attribute:: ifrcvaddresstable
    
    	This table contains an entry for each address (broadcast, multicast, or uni\-cast) for which the system will receive packets/frames on a particular interface, except as follows\:  \- for an interface operating in promiscuous mode, entries are only required for those addresses for which the system would receive frames were it not operating in promiscuous mode.  \- for 802.5 functional addresses, only one entry is required, for the address which has the functional address bit ANDed with the bit mask of all functional addresses for which the interface will accept frames.  A system is normally able to use any unicast address which corresponds to an entry in this table as a source address
    	**type**\:   :py:class:`Ifrcvaddresstable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable>`
    
    .. attribute:: ifstacktable
    
    	The table containing information on the relationships between the multiple sub\-layers of network interfaces.  In particular, it contains information on which sub\-layers run 'on top of' which other sub\-layers, where each sub\-layer corresponds to a conceptual row in the ifTable.  For example, when the sub\-layer with ifIndex value x runs over the sub\-layer with ifIndex value y, then this table contains\:    ifStackStatus.x.y=active  For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I.  For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer.  (If I is not involved in multiplexing, then these are the only two rows associated with I.)  For example, two rows exist even for an interface which has no others stacked on top or below it\:    ifStackStatus.0.x=active   ifStackStatus.x.0=active 
    	**type**\:   :py:class:`Ifstacktable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifstacktable>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\:   :py:class:`Iftable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable>`
    
    .. attribute:: interfaces
    
    	
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Interfaces>`
    
    

    """

    _prefix = 'IF-MIB'
    _revision = '2000-06-14'

    def __init__(self):
        super(IfMib, self).__init__()
        self._top_entity = None

        self.yang_name = "IF-MIB"
        self.yang_parent_name = "IF-MIB"

        self.ifmibobjects = IfMib.Ifmibobjects()
        self.ifmibobjects.parent = self
        self._children_name_map["ifmibobjects"] = "ifMIBObjects"
        self._children_yang_names.add("ifMIBObjects")

        self.ifrcvaddresstable = IfMib.Ifrcvaddresstable()
        self.ifrcvaddresstable.parent = self
        self._children_name_map["ifrcvaddresstable"] = "ifRcvAddressTable"
        self._children_yang_names.add("ifRcvAddressTable")

        self.ifstacktable = IfMib.Ifstacktable()
        self.ifstacktable.parent = self
        self._children_name_map["ifstacktable"] = "ifStackTable"
        self._children_yang_names.add("ifStackTable")

        self.iftable = IfMib.Iftable()
        self.iftable.parent = self
        self._children_name_map["iftable"] = "ifTable"
        self._children_yang_names.add("ifTable")

        self.interfaces = IfMib.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")


    class Interfaces(Entity):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IfMib.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "IF-MIB"

            self.ifnumber = YLeaf(YType.int32, "ifNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IfMib.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IfMib.Interfaces, self).__setattr__(name, value)

        def has_data(self):
            return self.ifnumber.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IF-MIB:IF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifnumber.is_set or self.ifnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifNumber"):
                self.ifnumber = value
                self.ifnumber.value_namespace = name_space
                self.ifnumber.value_namespace_prefix = name_space_prefix


    class Ifmibobjects(Entity):
        """
        
        
        .. attribute:: ifstacklastchange
        
        	The value of sysUpTime at the time of the last change of the (whole) interface stack.  A change of the interface stack is defined to be any creation, deletion, or change in value of any instance of ifStackStatus.  If the interface stack has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: iftablelastchange
        
        	The value of sysUpTime at the time of the last creation or deletion of an entry in the ifTable.  If the number of entries has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IfMib.Ifmibobjects, self).__init__()

            self.yang_name = "ifMIBObjects"
            self.yang_parent_name = "IF-MIB"

            self.ifstacklastchange = YLeaf(YType.uint32, "ifStackLastChange")

            self.iftablelastchange = YLeaf(YType.uint32, "ifTableLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifstacklastchange",
                            "iftablelastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IfMib.Ifmibobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IfMib.Ifmibobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ifstacklastchange.is_set or
                self.iftablelastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifstacklastchange.yfilter != YFilter.not_set or
                self.iftablelastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ifMIBObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IF-MIB:IF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifstacklastchange.is_set or self.ifstacklastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifstacklastchange.get_name_leafdata())
            if (self.iftablelastchange.is_set or self.iftablelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.iftablelastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifStackLastChange" or name == "ifTableLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifStackLastChange"):
                self.ifstacklastchange = value
                self.ifstacklastchange.value_namespace = name_space
                self.ifstacklastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "ifTableLastChange"):
                self.iftablelastchange = value
                self.iftablelastchange.value_namespace = name_space
                self.iftablelastchange.value_namespace_prefix = name_space_prefix


    class Iftable(Entity):
        """
        A list of interface entries.  The number of entries is
        given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An entry containing management information applicable to a particular interface
        	**type**\: list of    :py:class:`Ifentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IfMib.Iftable, self).__init__()

            self.yang_name = "ifTable"
            self.yang_parent_name = "IF-MIB"

            self.ifentry = YList(self)

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
                        super(IfMib.Iftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IfMib.Iftable, self).__setattr__(name, value)


        class Ifentry(Entity):
            """
            An entry containing management information applicable to a
            particular interface.
            
            .. attribute:: ifindex  <key>
            
            	A unique value, greater than zero, for each interface.  It is recommended that values are assigned contiguously starting from 1.  The value for each interface sub\-layer must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed.  When a managed system initializes, all interfaces start with ifAdminStatus in the down(2) state.  As a result of either explicit management action or per configuration information retained by the managed system, ifAdminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state)
            	**type**\:   :py:class:`Ifadminstatus <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.Ifadminstatus>`
            
            .. attribute:: ifalias
            
            	This object is an 'alias' name for the interface as specified by a network manager, and provides a non\-volatile 'handle' for the interface.  On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero\-length string.  As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re\- initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value.  An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface.  Some agents may support write\-access only for interfaces having particular values of ifType.  An agent which supports write access to this object is required to keep the value in non\-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ifconnectorpresent
            
            	This object has the value 'true(1)' if the interface sublayer has a physical connector and the value 'false(2)' otherwise
            	**type**\:  bool
            
            .. attribute:: ifcounterdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this interface of any Counter32 or Counter64 object contained in the ifTable or ifXTable.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the interface hardware/software
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ifhcinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifInMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinoctets
            
            	The total number of octets received on the interface, including framing characters.  This object is a 64\-bit version of ifInOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifOutMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  This object is a 64\-bit version of ifOutOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhighspeed
            
            	An estimate of the interface's current bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifInMulticastPkts and ifInBroadcastPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	For packet\-oriented interfaces, the number of packets received via the interface which were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing the number of transmission units received via the interface which were discarded because of an unknown or unsupported protocol.  For any interface that does not support protocol multiplexing, this counter will always be 0.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflinkupdowntrapenable
            
            	Indicates whether linkUp/linkDown traps should be generated for this interface.  By default, this object should have the value enabled(1) for interfaces which do not operate on 'top' of any other interface (as defined in the ifStackTable), and disabled(2) otherwise
            	**type**\:   :py:class:`Iflinkupdowntrapenable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.Iflinkupdowntrapenable>`
            
            .. attribute:: ifmtu
            
            	The size of the largest packet which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifname
            
            	The textual name of the interface.  The value of this object should be the name of the interface as assigned by the local device and should be suitable for use in commands entered at the device's `console'.  This might be a text name, such as `le0' or a simple port number, such as `1', depending on the interface naming syntax of the device.  If several entries in the ifTable together represent a single interface as named by the device, then each will have the same value of ifName.  Note that for an agent which responds to SNMP queries concerning an interface on some other (proxied) device, then the value of ifName for such an interface is the proxied device's local name for it.  If there is no local name, or this object is otherwise not applicable, then this object contains a zero\-length string
            	**type**\:  str
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface.  The testing(3) state indicates that no operational packets can be passed.  If ifAdminStatus is down(2) then ifOperStatus should be down(2).  If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should change to dormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection); it should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state; it should remain in the notPresent(6) state if the interface has missing (typically, hardware) components
            	**type**\:   :py:class:`Ifoperstatus <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.Ifoperstatus>`
            
            .. attribute:: ifoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifOutMulticastPkts and ifOutBroadcastPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a MAC address.  The interface's media\-specific MIB must define the bit and byte ordering and the format of the value of this object.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifpromiscuousmode
            
            	This object has a value of false(2) if this interface only accepts packets/frames that are addressed to this station. This object has a value of true(1) when the station accepts all packets/frames transmitted on the media.  The value true(1) is only legal on certain types of media.  If legal, setting this object to a value of true(1) may require the interface to be reset before becoming effective.  The value of ifPromiscuousMode does not affect the reception of broadcast and multicast packets/frames by the interface
            	**type**\:  bool
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  It is recommended that this value point to an instance of a MIB object in the media\-specific MIB, i.e., that this object have the semantics associated with the InstancePointer textual convention defined in RFC 2579.  In fact, it is recommended that the media\-specific MIB specify what value ifSpecific should/can take for values of ifType.  If no MIB definitions specific to the particular media are available, the value should be set to the OBJECT IDENTIFIER { 0 0 }
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iftestcode
            
            	This object contains a code which contains more specific information on the test result, for example an error\-code after a failed test.  Error codes and other values this object may take are specific to the type of interface and/or test.  The value may have the semantics of either the AutonomousType or InstancePointer textual conventions as defined in RFC 2579.  The identifier\:      testCodeUnknown  OBJECT IDENTIFIER \:\:= { 0 0 }  is defined for use if no additional result code is available
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftestid
            
            	This object identifies the current invocation of the interface's test
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: iftestowner
            
            	The entity which currently has the 'ownership' required to invoke a test on this interface
            	**type**\:  str
            
            	**status**\: deprecated
            
            .. attribute:: iftestresult
            
            	This object contains the result of the most recently requested test, or the value none(1) if no tests have been requested since the last reset.  Note that this facility provides no provision for saving the results of one test when starting another, as could be required if used by multiple managers concurrently
            	**type**\:   :py:class:`Iftestresult <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.Iftestresult>`
            
            	**status**\: deprecated
            
            .. attribute:: ifteststatus
            
            	This object indicates whether or not some manager currently has the necessary 'ownership' required to invoke a test on this interface.  A write to this object is only successful when it changes its value from 'notInUse(1)' to 'inUse(2)'. After completion of a test, the agent resets the value back to 'notInUse(1)'
            	**type**\:   :py:class:`Ifteststatus <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.Ifteststatus>`
            
            	**status**\: deprecated
            
            .. attribute:: iftesttype
            
            	A control variable used to start and stop operator\- initiated interface tests.  Most OBJECT IDENTIFIER values assigned to tests are defined elsewhere, in association with specific types of interface.  However, this document assigns a value for a full\-duplex loopback test, and defines the special meanings of the subject identifier\:      noTest  OBJECT IDENTIFIER \:\:= { 0 0 }  When the value noTest is written to this object, no action is taken unless a test is in progress, in which case the test is aborted.  Writing any other value to this object is only valid when no test is currently in progress, in which case the indicated test is initiated.  When read, this object always returns the most recent value that ifTestType was set to.  If it has not been set since the last initialization of the network management subsystem on the agent, a value of noTest is returned
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\:   :py:class:`Ianaiftype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianaiftype>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IfMib.Iftable.Ifentry, self).__init__()

                self.yang_name = "ifEntry"
                self.yang_parent_name = "ifTable"

                self.ifindex = YLeaf(YType.int32, "ifIndex")

                self.ifadminstatus = YLeaf(YType.enumeration, "ifAdminStatus")

                self.ifalias = YLeaf(YType.str, "ifAlias")

                self.ifconnectorpresent = YLeaf(YType.boolean, "ifConnectorPresent")

                self.ifcounterdiscontinuitytime = YLeaf(YType.uint32, "ifCounterDiscontinuityTime")

                self.ifdescr = YLeaf(YType.str, "ifDescr")

                self.ifhcinbroadcastpkts = YLeaf(YType.uint64, "ifHCInBroadcastPkts")

                self.ifhcinmulticastpkts = YLeaf(YType.uint64, "ifHCInMulticastPkts")

                self.ifhcinoctets = YLeaf(YType.uint64, "ifHCInOctets")

                self.ifhcinucastpkts = YLeaf(YType.uint64, "ifHCInUcastPkts")

                self.ifhcoutbroadcastpkts = YLeaf(YType.uint64, "ifHCOutBroadcastPkts")

                self.ifhcoutmulticastpkts = YLeaf(YType.uint64, "ifHCOutMulticastPkts")

                self.ifhcoutoctets = YLeaf(YType.uint64, "ifHCOutOctets")

                self.ifhcoutucastpkts = YLeaf(YType.uint64, "ifHCOutUcastPkts")

                self.ifhighspeed = YLeaf(YType.uint32, "ifHighSpeed")

                self.ifinbroadcastpkts = YLeaf(YType.uint32, "ifInBroadcastPkts")

                self.ifindiscards = YLeaf(YType.uint32, "ifInDiscards")

                self.ifinerrors = YLeaf(YType.uint32, "ifInErrors")

                self.ifinmulticastpkts = YLeaf(YType.uint32, "ifInMulticastPkts")

                self.ifinnucastpkts = YLeaf(YType.uint32, "ifInNUcastPkts")

                self.ifinoctets = YLeaf(YType.uint32, "ifInOctets")

                self.ifinucastpkts = YLeaf(YType.uint32, "ifInUcastPkts")

                self.ifinunknownprotos = YLeaf(YType.uint32, "ifInUnknownProtos")

                self.iflastchange = YLeaf(YType.uint32, "ifLastChange")

                self.iflinkupdowntrapenable = YLeaf(YType.enumeration, "ifLinkUpDownTrapEnable")

                self.ifmtu = YLeaf(YType.int32, "ifMtu")

                self.ifname = YLeaf(YType.str, "ifName")

                self.ifoperstatus = YLeaf(YType.enumeration, "ifOperStatus")

                self.ifoutbroadcastpkts = YLeaf(YType.uint32, "ifOutBroadcastPkts")

                self.ifoutdiscards = YLeaf(YType.uint32, "ifOutDiscards")

                self.ifouterrors = YLeaf(YType.uint32, "ifOutErrors")

                self.ifoutmulticastpkts = YLeaf(YType.uint32, "ifOutMulticastPkts")

                self.ifoutnucastpkts = YLeaf(YType.uint32, "ifOutNUcastPkts")

                self.ifoutoctets = YLeaf(YType.uint32, "ifOutOctets")

                self.ifoutqlen = YLeaf(YType.uint32, "ifOutQLen")

                self.ifoutucastpkts = YLeaf(YType.uint32, "ifOutUcastPkts")

                self.ifphysaddress = YLeaf(YType.str, "ifPhysAddress")

                self.ifpromiscuousmode = YLeaf(YType.boolean, "ifPromiscuousMode")

                self.ifspecific = YLeaf(YType.str, "ifSpecific")

                self.ifspeed = YLeaf(YType.uint32, "ifSpeed")

                self.iftestcode = YLeaf(YType.str, "ifTestCode")

                self.iftestid = YLeaf(YType.int32, "ifTestId")

                self.iftestowner = YLeaf(YType.str, "ifTestOwner")

                self.iftestresult = YLeaf(YType.enumeration, "ifTestResult")

                self.ifteststatus = YLeaf(YType.enumeration, "ifTestStatus")

                self.iftesttype = YLeaf(YType.str, "ifTestType")

                self.iftype = YLeaf(YType.enumeration, "ifType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "ifadminstatus",
                                "ifalias",
                                "ifconnectorpresent",
                                "ifcounterdiscontinuitytime",
                                "ifdescr",
                                "ifhcinbroadcastpkts",
                                "ifhcinmulticastpkts",
                                "ifhcinoctets",
                                "ifhcinucastpkts",
                                "ifhcoutbroadcastpkts",
                                "ifhcoutmulticastpkts",
                                "ifhcoutoctets",
                                "ifhcoutucastpkts",
                                "ifhighspeed",
                                "ifinbroadcastpkts",
                                "ifindiscards",
                                "ifinerrors",
                                "ifinmulticastpkts",
                                "ifinnucastpkts",
                                "ifinoctets",
                                "ifinucastpkts",
                                "ifinunknownprotos",
                                "iflastchange",
                                "iflinkupdowntrapenable",
                                "ifmtu",
                                "ifname",
                                "ifoperstatus",
                                "ifoutbroadcastpkts",
                                "ifoutdiscards",
                                "ifouterrors",
                                "ifoutmulticastpkts",
                                "ifoutnucastpkts",
                                "ifoutoctets",
                                "ifoutqlen",
                                "ifoutucastpkts",
                                "ifphysaddress",
                                "ifpromiscuousmode",
                                "ifspecific",
                                "ifspeed",
                                "iftestcode",
                                "iftestid",
                                "iftestowner",
                                "iftestresult",
                                "ifteststatus",
                                "iftesttype",
                                "iftype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IfMib.Iftable.Ifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IfMib.Iftable.Ifentry, self).__setattr__(name, value)

            class Ifadminstatus(Enum):
                """
                Ifadminstatus

                The desired state of the interface.  The testing(3) state

                indicates that no operational packets can be passed.  When a

                managed system initializes, all interfaces start with

                ifAdminStatus in the down(2) state.  As a result of either

                explicit management action or per configuration information

                retained by the managed system, ifAdminStatus is then

                changed to either the up(1) or testing(3) states (or remains

                in the down(2) state).

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Iflinkupdowntrapenable(Enum):
                """
                Iflinkupdowntrapenable

                Indicates whether linkUp/linkDown traps should be generated

                for this interface.

                By default, this object should have the value enabled(1) for

                interfaces which do not operate on 'top' of any other

                interface (as defined in the ifStackTable), and disabled(2)

                otherwise.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Ifoperstatus(Enum):
                """
                Ifoperstatus

                The current operational state of the interface.  The

                testing(3) state indicates that no operational packets can

                be passed.  If ifAdminStatus is down(2) then ifOperStatus

                should be down(2).  If ifAdminStatus is changed to up(1)

                then ifOperStatus should change to up(1) if the interface is

                ready to transmit and receive network traffic; it should

                change to dormant(5) if the interface is waiting for

                external actions (such as a serial line waiting for an

                incoming connection); it should remain in the down(2) state

                if and only if there is a fault that prevents it from going

                to the up(1) state; it should remain in the notPresent(6)

                state if the interface has missing (typically, hardware)

                components.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")

                unknown = Enum.YLeaf(4, "unknown")

                dormant = Enum.YLeaf(5, "dormant")

                notPresent = Enum.YLeaf(6, "notPresent")

                lowerLayerDown = Enum.YLeaf(7, "lowerLayerDown")


            class Iftestresult(Enum):
                """
                Iftestresult

                This object contains the result of the most recently

                requested test, or the value none(1) if no tests have been

                requested since the last reset.  Note that this facility

                provides no provision for saving the results of one test

                when starting another, as could be required if used by

                multiple managers concurrently.

                .. data:: none = 1

                .. data:: success = 2

                .. data:: inProgress = 3

                .. data:: notSupported = 4

                .. data:: unAbleToRun = 5

                .. data:: aborted = 6

                .. data:: failed = 7

                """

                none = Enum.YLeaf(1, "none")

                success = Enum.YLeaf(2, "success")

                inProgress = Enum.YLeaf(3, "inProgress")

                notSupported = Enum.YLeaf(4, "notSupported")

                unAbleToRun = Enum.YLeaf(5, "unAbleToRun")

                aborted = Enum.YLeaf(6, "aborted")

                failed = Enum.YLeaf(7, "failed")


            class Ifteststatus(Enum):
                """
                Ifteststatus

                This object indicates whether or not some manager currently

                has the necessary 'ownership' required to invoke a test on

                this interface.  A write to this object is only successful

                when it changes its value from 'notInUse(1)' to 'inUse(2)'.

                After completion of a test, the agent resets the value back

                to 'notInUse(1)'.

                .. data:: notInUse = 1

                .. data:: inUse = 2

                """

                notInUse = Enum.YLeaf(1, "notInUse")

                inUse = Enum.YLeaf(2, "inUse")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.ifadminstatus.is_set or
                    self.ifalias.is_set or
                    self.ifconnectorpresent.is_set or
                    self.ifcounterdiscontinuitytime.is_set or
                    self.ifdescr.is_set or
                    self.ifhcinbroadcastpkts.is_set or
                    self.ifhcinmulticastpkts.is_set or
                    self.ifhcinoctets.is_set or
                    self.ifhcinucastpkts.is_set or
                    self.ifhcoutbroadcastpkts.is_set or
                    self.ifhcoutmulticastpkts.is_set or
                    self.ifhcoutoctets.is_set or
                    self.ifhcoutucastpkts.is_set or
                    self.ifhighspeed.is_set or
                    self.ifinbroadcastpkts.is_set or
                    self.ifindiscards.is_set or
                    self.ifinerrors.is_set or
                    self.ifinmulticastpkts.is_set or
                    self.ifinnucastpkts.is_set or
                    self.ifinoctets.is_set or
                    self.ifinucastpkts.is_set or
                    self.ifinunknownprotos.is_set or
                    self.iflastchange.is_set or
                    self.iflinkupdowntrapenable.is_set or
                    self.ifmtu.is_set or
                    self.ifname.is_set or
                    self.ifoperstatus.is_set or
                    self.ifoutbroadcastpkts.is_set or
                    self.ifoutdiscards.is_set or
                    self.ifouterrors.is_set or
                    self.ifoutmulticastpkts.is_set or
                    self.ifoutnucastpkts.is_set or
                    self.ifoutoctets.is_set or
                    self.ifoutqlen.is_set or
                    self.ifoutucastpkts.is_set or
                    self.ifphysaddress.is_set or
                    self.ifpromiscuousmode.is_set or
                    self.ifspecific.is_set or
                    self.ifspeed.is_set or
                    self.iftestcode.is_set or
                    self.iftestid.is_set or
                    self.iftestowner.is_set or
                    self.iftestresult.is_set or
                    self.ifteststatus.is_set or
                    self.iftesttype.is_set or
                    self.iftype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.ifadminstatus.yfilter != YFilter.not_set or
                    self.ifalias.yfilter != YFilter.not_set or
                    self.ifconnectorpresent.yfilter != YFilter.not_set or
                    self.ifcounterdiscontinuitytime.yfilter != YFilter.not_set or
                    self.ifdescr.yfilter != YFilter.not_set or
                    self.ifhcinbroadcastpkts.yfilter != YFilter.not_set or
                    self.ifhcinmulticastpkts.yfilter != YFilter.not_set or
                    self.ifhcinoctets.yfilter != YFilter.not_set or
                    self.ifhcinucastpkts.yfilter != YFilter.not_set or
                    self.ifhcoutbroadcastpkts.yfilter != YFilter.not_set or
                    self.ifhcoutmulticastpkts.yfilter != YFilter.not_set or
                    self.ifhcoutoctets.yfilter != YFilter.not_set or
                    self.ifhcoutucastpkts.yfilter != YFilter.not_set or
                    self.ifhighspeed.yfilter != YFilter.not_set or
                    self.ifinbroadcastpkts.yfilter != YFilter.not_set or
                    self.ifindiscards.yfilter != YFilter.not_set or
                    self.ifinerrors.yfilter != YFilter.not_set or
                    self.ifinmulticastpkts.yfilter != YFilter.not_set or
                    self.ifinnucastpkts.yfilter != YFilter.not_set or
                    self.ifinoctets.yfilter != YFilter.not_set or
                    self.ifinucastpkts.yfilter != YFilter.not_set or
                    self.ifinunknownprotos.yfilter != YFilter.not_set or
                    self.iflastchange.yfilter != YFilter.not_set or
                    self.iflinkupdowntrapenable.yfilter != YFilter.not_set or
                    self.ifmtu.yfilter != YFilter.not_set or
                    self.ifname.yfilter != YFilter.not_set or
                    self.ifoperstatus.yfilter != YFilter.not_set or
                    self.ifoutbroadcastpkts.yfilter != YFilter.not_set or
                    self.ifoutdiscards.yfilter != YFilter.not_set or
                    self.ifouterrors.yfilter != YFilter.not_set or
                    self.ifoutmulticastpkts.yfilter != YFilter.not_set or
                    self.ifoutnucastpkts.yfilter != YFilter.not_set or
                    self.ifoutoctets.yfilter != YFilter.not_set or
                    self.ifoutqlen.yfilter != YFilter.not_set or
                    self.ifoutucastpkts.yfilter != YFilter.not_set or
                    self.ifphysaddress.yfilter != YFilter.not_set or
                    self.ifpromiscuousmode.yfilter != YFilter.not_set or
                    self.ifspecific.yfilter != YFilter.not_set or
                    self.ifspeed.yfilter != YFilter.not_set or
                    self.iftestcode.yfilter != YFilter.not_set or
                    self.iftestid.yfilter != YFilter.not_set or
                    self.iftestowner.yfilter != YFilter.not_set or
                    self.iftestresult.yfilter != YFilter.not_set or
                    self.ifteststatus.yfilter != YFilter.not_set or
                    self.iftesttype.yfilter != YFilter.not_set or
                    self.iftype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ifEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IF-MIB:IF-MIB/ifTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.ifadminstatus.is_set or self.ifadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifadminstatus.get_name_leafdata())
                if (self.ifalias.is_set or self.ifalias.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifalias.get_name_leafdata())
                if (self.ifconnectorpresent.is_set or self.ifconnectorpresent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifconnectorpresent.get_name_leafdata())
                if (self.ifcounterdiscontinuitytime.is_set or self.ifcounterdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifcounterdiscontinuitytime.get_name_leafdata())
                if (self.ifdescr.is_set or self.ifdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifdescr.get_name_leafdata())
                if (self.ifhcinbroadcastpkts.is_set or self.ifhcinbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcinbroadcastpkts.get_name_leafdata())
                if (self.ifhcinmulticastpkts.is_set or self.ifhcinmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcinmulticastpkts.get_name_leafdata())
                if (self.ifhcinoctets.is_set or self.ifhcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcinoctets.get_name_leafdata())
                if (self.ifhcinucastpkts.is_set or self.ifhcinucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcinucastpkts.get_name_leafdata())
                if (self.ifhcoutbroadcastpkts.is_set or self.ifhcoutbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcoutbroadcastpkts.get_name_leafdata())
                if (self.ifhcoutmulticastpkts.is_set or self.ifhcoutmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcoutmulticastpkts.get_name_leafdata())
                if (self.ifhcoutoctets.is_set or self.ifhcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcoutoctets.get_name_leafdata())
                if (self.ifhcoutucastpkts.is_set or self.ifhcoutucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhcoutucastpkts.get_name_leafdata())
                if (self.ifhighspeed.is_set or self.ifhighspeed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifhighspeed.get_name_leafdata())
                if (self.ifinbroadcastpkts.is_set or self.ifinbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinbroadcastpkts.get_name_leafdata())
                if (self.ifindiscards.is_set or self.ifindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindiscards.get_name_leafdata())
                if (self.ifinerrors.is_set or self.ifinerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinerrors.get_name_leafdata())
                if (self.ifinmulticastpkts.is_set or self.ifinmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinmulticastpkts.get_name_leafdata())
                if (self.ifinnucastpkts.is_set or self.ifinnucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinnucastpkts.get_name_leafdata())
                if (self.ifinoctets.is_set or self.ifinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinoctets.get_name_leafdata())
                if (self.ifinucastpkts.is_set or self.ifinucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinucastpkts.get_name_leafdata())
                if (self.ifinunknownprotos.is_set or self.ifinunknownprotos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinunknownprotos.get_name_leafdata())
                if (self.iflastchange.is_set or self.iflastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iflastchange.get_name_leafdata())
                if (self.iflinkupdowntrapenable.is_set or self.iflinkupdowntrapenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iflinkupdowntrapenable.get_name_leafdata())
                if (self.ifmtu.is_set or self.ifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifmtu.get_name_leafdata())
                if (self.ifname.is_set or self.ifname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifname.get_name_leafdata())
                if (self.ifoperstatus.is_set or self.ifoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoperstatus.get_name_leafdata())
                if (self.ifoutbroadcastpkts.is_set or self.ifoutbroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutbroadcastpkts.get_name_leafdata())
                if (self.ifoutdiscards.is_set or self.ifoutdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutdiscards.get_name_leafdata())
                if (self.ifouterrors.is_set or self.ifouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifouterrors.get_name_leafdata())
                if (self.ifoutmulticastpkts.is_set or self.ifoutmulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutmulticastpkts.get_name_leafdata())
                if (self.ifoutnucastpkts.is_set or self.ifoutnucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutnucastpkts.get_name_leafdata())
                if (self.ifoutoctets.is_set or self.ifoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutoctets.get_name_leafdata())
                if (self.ifoutqlen.is_set or self.ifoutqlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutqlen.get_name_leafdata())
                if (self.ifoutucastpkts.is_set or self.ifoutucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutucastpkts.get_name_leafdata())
                if (self.ifphysaddress.is_set or self.ifphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifphysaddress.get_name_leafdata())
                if (self.ifpromiscuousmode.is_set or self.ifpromiscuousmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifpromiscuousmode.get_name_leafdata())
                if (self.ifspecific.is_set or self.ifspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifspecific.get_name_leafdata())
                if (self.ifspeed.is_set or self.ifspeed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifspeed.get_name_leafdata())
                if (self.iftestcode.is_set or self.iftestcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftestcode.get_name_leafdata())
                if (self.iftestid.is_set or self.iftestid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftestid.get_name_leafdata())
                if (self.iftestowner.is_set or self.iftestowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftestowner.get_name_leafdata())
                if (self.iftestresult.is_set or self.iftestresult.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftestresult.get_name_leafdata())
                if (self.ifteststatus.is_set or self.ifteststatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifteststatus.get_name_leafdata())
                if (self.iftesttype.is_set or self.iftesttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftesttype.get_name_leafdata())
                if (self.iftype.is_set or self.iftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "ifAdminStatus" or name == "ifAlias" or name == "ifConnectorPresent" or name == "ifCounterDiscontinuityTime" or name == "ifDescr" or name == "ifHCInBroadcastPkts" or name == "ifHCInMulticastPkts" or name == "ifHCInOctets" or name == "ifHCInUcastPkts" or name == "ifHCOutBroadcastPkts" or name == "ifHCOutMulticastPkts" or name == "ifHCOutOctets" or name == "ifHCOutUcastPkts" or name == "ifHighSpeed" or name == "ifInBroadcastPkts" or name == "ifInDiscards" or name == "ifInErrors" or name == "ifInMulticastPkts" or name == "ifInNUcastPkts" or name == "ifInOctets" or name == "ifInUcastPkts" or name == "ifInUnknownProtos" or name == "ifLastChange" or name == "ifLinkUpDownTrapEnable" or name == "ifMtu" or name == "ifName" or name == "ifOperStatus" or name == "ifOutBroadcastPkts" or name == "ifOutDiscards" or name == "ifOutErrors" or name == "ifOutMulticastPkts" or name == "ifOutNUcastPkts" or name == "ifOutOctets" or name == "ifOutQLen" or name == "ifOutUcastPkts" or name == "ifPhysAddress" or name == "ifPromiscuousMode" or name == "ifSpecific" or name == "ifSpeed" or name == "ifTestCode" or name == "ifTestId" or name == "ifTestOwner" or name == "ifTestResult" or name == "ifTestStatus" or name == "ifTestType" or name == "ifType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ifAdminStatus"):
                    self.ifadminstatus = value
                    self.ifadminstatus.value_namespace = name_space
                    self.ifadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifAlias"):
                    self.ifalias = value
                    self.ifalias.value_namespace = name_space
                    self.ifalias.value_namespace_prefix = name_space_prefix
                if(value_path == "ifConnectorPresent"):
                    self.ifconnectorpresent = value
                    self.ifconnectorpresent.value_namespace = name_space
                    self.ifconnectorpresent.value_namespace_prefix = name_space_prefix
                if(value_path == "ifCounterDiscontinuityTime"):
                    self.ifcounterdiscontinuitytime = value
                    self.ifcounterdiscontinuitytime.value_namespace = name_space
                    self.ifcounterdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ifDescr"):
                    self.ifdescr = value
                    self.ifdescr.value_namespace = name_space
                    self.ifdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCInBroadcastPkts"):
                    self.ifhcinbroadcastpkts = value
                    self.ifhcinbroadcastpkts.value_namespace = name_space
                    self.ifhcinbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCInMulticastPkts"):
                    self.ifhcinmulticastpkts = value
                    self.ifhcinmulticastpkts.value_namespace = name_space
                    self.ifhcinmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCInOctets"):
                    self.ifhcinoctets = value
                    self.ifhcinoctets.value_namespace = name_space
                    self.ifhcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCInUcastPkts"):
                    self.ifhcinucastpkts = value
                    self.ifhcinucastpkts.value_namespace = name_space
                    self.ifhcinucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCOutBroadcastPkts"):
                    self.ifhcoutbroadcastpkts = value
                    self.ifhcoutbroadcastpkts.value_namespace = name_space
                    self.ifhcoutbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCOutMulticastPkts"):
                    self.ifhcoutmulticastpkts = value
                    self.ifhcoutmulticastpkts.value_namespace = name_space
                    self.ifhcoutmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCOutOctets"):
                    self.ifhcoutoctets = value
                    self.ifhcoutoctets.value_namespace = name_space
                    self.ifhcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHCOutUcastPkts"):
                    self.ifhcoutucastpkts = value
                    self.ifhcoutucastpkts.value_namespace = name_space
                    self.ifhcoutucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifHighSpeed"):
                    self.ifhighspeed = value
                    self.ifhighspeed.value_namespace = name_space
                    self.ifhighspeed.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInBroadcastPkts"):
                    self.ifinbroadcastpkts = value
                    self.ifinbroadcastpkts.value_namespace = name_space
                    self.ifinbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInDiscards"):
                    self.ifindiscards = value
                    self.ifindiscards.value_namespace = name_space
                    self.ifindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInErrors"):
                    self.ifinerrors = value
                    self.ifinerrors.value_namespace = name_space
                    self.ifinerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInMulticastPkts"):
                    self.ifinmulticastpkts = value
                    self.ifinmulticastpkts.value_namespace = name_space
                    self.ifinmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInNUcastPkts"):
                    self.ifinnucastpkts = value
                    self.ifinnucastpkts.value_namespace = name_space
                    self.ifinnucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInOctets"):
                    self.ifinoctets = value
                    self.ifinoctets.value_namespace = name_space
                    self.ifinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInUcastPkts"):
                    self.ifinucastpkts = value
                    self.ifinucastpkts.value_namespace = name_space
                    self.ifinucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInUnknownProtos"):
                    self.ifinunknownprotos = value
                    self.ifinunknownprotos.value_namespace = name_space
                    self.ifinunknownprotos.value_namespace_prefix = name_space_prefix
                if(value_path == "ifLastChange"):
                    self.iflastchange = value
                    self.iflastchange.value_namespace = name_space
                    self.iflastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "ifLinkUpDownTrapEnable"):
                    self.iflinkupdowntrapenable = value
                    self.iflinkupdowntrapenable.value_namespace = name_space
                    self.iflinkupdowntrapenable.value_namespace_prefix = name_space_prefix
                if(value_path == "ifMtu"):
                    self.ifmtu = value
                    self.ifmtu.value_namespace = name_space
                    self.ifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "ifName"):
                    self.ifname = value
                    self.ifname.value_namespace = name_space
                    self.ifname.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOperStatus"):
                    self.ifoperstatus = value
                    self.ifoperstatus.value_namespace = name_space
                    self.ifoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutBroadcastPkts"):
                    self.ifoutbroadcastpkts = value
                    self.ifoutbroadcastpkts.value_namespace = name_space
                    self.ifoutbroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutDiscards"):
                    self.ifoutdiscards = value
                    self.ifoutdiscards.value_namespace = name_space
                    self.ifoutdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutErrors"):
                    self.ifouterrors = value
                    self.ifouterrors.value_namespace = name_space
                    self.ifouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutMulticastPkts"):
                    self.ifoutmulticastpkts = value
                    self.ifoutmulticastpkts.value_namespace = name_space
                    self.ifoutmulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutNUcastPkts"):
                    self.ifoutnucastpkts = value
                    self.ifoutnucastpkts.value_namespace = name_space
                    self.ifoutnucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutOctets"):
                    self.ifoutoctets = value
                    self.ifoutoctets.value_namespace = name_space
                    self.ifoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutQLen"):
                    self.ifoutqlen = value
                    self.ifoutqlen.value_namespace = name_space
                    self.ifoutqlen.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutUcastPkts"):
                    self.ifoutucastpkts = value
                    self.ifoutucastpkts.value_namespace = name_space
                    self.ifoutucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifPhysAddress"):
                    self.ifphysaddress = value
                    self.ifphysaddress.value_namespace = name_space
                    self.ifphysaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ifPromiscuousMode"):
                    self.ifpromiscuousmode = value
                    self.ifpromiscuousmode.value_namespace = name_space
                    self.ifpromiscuousmode.value_namespace_prefix = name_space_prefix
                if(value_path == "ifSpecific"):
                    self.ifspecific = value
                    self.ifspecific.value_namespace = name_space
                    self.ifspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "ifSpeed"):
                    self.ifspeed = value
                    self.ifspeed.value_namespace = name_space
                    self.ifspeed.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestCode"):
                    self.iftestcode = value
                    self.iftestcode.value_namespace = name_space
                    self.iftestcode.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestId"):
                    self.iftestid = value
                    self.iftestid.value_namespace = name_space
                    self.iftestid.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestOwner"):
                    self.iftestowner = value
                    self.iftestowner.value_namespace = name_space
                    self.iftestowner.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestResult"):
                    self.iftestresult = value
                    self.iftestresult.value_namespace = name_space
                    self.iftestresult.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestStatus"):
                    self.ifteststatus = value
                    self.ifteststatus.value_namespace = name_space
                    self.ifteststatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifTestType"):
                    self.iftesttype = value
                    self.iftesttype.value_namespace = name_space
                    self.iftesttype.value_namespace_prefix = name_space_prefix
                if(value_path == "ifType"):
                    self.iftype = value
                    self.iftype.value_namespace = name_space
                    self.iftype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ifTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IF-MIB:IF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ifEntry"):
                for c in self.ifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IfMib.Iftable.Ifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ifstacktable(Entity):
        """
        The table containing information on the relationships
        between the multiple sub\-layers of network interfaces.  In
        particular, it contains information on which sub\-layers run
        'on top of' which other sub\-layers, where each sub\-layer
        corresponds to a conceptual row in the ifTable.  For
        example, when the sub\-layer with ifIndex value x runs over
        the sub\-layer with ifIndex value y, then this table
        contains\:
        
          ifStackStatus.x.y=active
        
        For each ifIndex value, I, which identifies an active
        interface, there are always at least two instantiated rows
        in this table associated with I.  For one of these rows, I
        is the value of ifStackHigherLayer; for the other, I is the
        value of ifStackLowerLayer.  (If I is not involved in
        multiplexing, then these are the only two rows associated
        with I.)
        
        For example, two rows exist even for an interface which has
        no others stacked on top or below it\:
        
          ifStackStatus.0.x=active
          ifStackStatus.x.0=active 
        
        .. attribute:: ifstackentry
        
        	Information on a particular relationship between two sub\- layers, specifying that one sub\-layer runs on 'top' of the other sub\-layer.  Each sub\-layer corresponds to a conceptual row in the ifTable
        	**type**\: list of    :py:class:`Ifstackentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifstacktable.Ifstackentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IfMib.Ifstacktable, self).__init__()

            self.yang_name = "ifStackTable"
            self.yang_parent_name = "IF-MIB"

            self.ifstackentry = YList(self)

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
                        super(IfMib.Ifstacktable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IfMib.Ifstacktable, self).__setattr__(name, value)


        class Ifstackentry(Entity):
            """
            Information on a particular relationship between two sub\-
            layers, specifying that one sub\-layer runs on 'top' of the
            other sub\-layer.  Each sub\-layer corresponds to a conceptual
            row in the ifTable.
            
            .. attribute:: ifstackhigherlayer  <key>
            
            	The value of ifIndex corresponding to the higher sub\-layer of the relationship, i.e., the sub\-layer which runs on 'top' of the sub\-layer identified by the corresponding instance of ifStackLowerLayer.  If there is no higher sub\-layer (below the internetwork layer), then this object has the value 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstacklowerlayer  <key>
            
            	The value of ifIndex corresponding to the lower sub\-layer of the relationship, i.e., the sub\-layer which runs 'below' the sub\-layer identified by the corresponding instance of ifStackHigherLayer.  If there is no lower sub\-layer, then this object has the value 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstackstatus
            
            	The status of the relationship between two sub\-layers.  Changing the value of this object from 'active' to 'notInService' or 'destroy' will likely have consequences up and down the interface stack.  Thus, write access to this object is likely to be inappropriate for some types of interfaces, and many implementations will choose not to support write\-access for any type of interface
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IfMib.Ifstacktable.Ifstackentry, self).__init__()

                self.yang_name = "ifStackEntry"
                self.yang_parent_name = "ifStackTable"

                self.ifstackhigherlayer = YLeaf(YType.int32, "ifStackHigherLayer")

                self.ifstacklowerlayer = YLeaf(YType.int32, "ifStackLowerLayer")

                self.ifstackstatus = YLeaf(YType.enumeration, "ifStackStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifstackhigherlayer",
                                "ifstacklowerlayer",
                                "ifstackstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IfMib.Ifstacktable.Ifstackentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IfMib.Ifstacktable.Ifstackentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifstackhigherlayer.is_set or
                    self.ifstacklowerlayer.is_set or
                    self.ifstackstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifstackhigherlayer.yfilter != YFilter.not_set or
                    self.ifstacklowerlayer.yfilter != YFilter.not_set or
                    self.ifstackstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ifStackEntry" + "[ifStackHigherLayer='" + self.ifstackhigherlayer.get() + "']" + "[ifStackLowerLayer='" + self.ifstacklowerlayer.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IF-MIB:IF-MIB/ifStackTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifstackhigherlayer.is_set or self.ifstackhigherlayer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifstackhigherlayer.get_name_leafdata())
                if (self.ifstacklowerlayer.is_set or self.ifstacklowerlayer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifstacklowerlayer.get_name_leafdata())
                if (self.ifstackstatus.is_set or self.ifstackstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifstackstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifStackHigherLayer" or name == "ifStackLowerLayer" or name == "ifStackStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifStackHigherLayer"):
                    self.ifstackhigherlayer = value
                    self.ifstackhigherlayer.value_namespace = name_space
                    self.ifstackhigherlayer.value_namespace_prefix = name_space_prefix
                if(value_path == "ifStackLowerLayer"):
                    self.ifstacklowerlayer = value
                    self.ifstacklowerlayer.value_namespace = name_space
                    self.ifstacklowerlayer.value_namespace_prefix = name_space_prefix
                if(value_path == "ifStackStatus"):
                    self.ifstackstatus = value
                    self.ifstackstatus.value_namespace = name_space
                    self.ifstackstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ifstackentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ifstackentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ifStackTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IF-MIB:IF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ifStackEntry"):
                for c in self.ifstackentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IfMib.Ifstacktable.Ifstackentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ifstackentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifStackEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ifrcvaddresstable(Entity):
        """
        This table contains an entry for each address (broadcast,
        multicast, or uni\-cast) for which the system will receive
        packets/frames on a particular interface, except as follows\:
        
        \- for an interface operating in promiscuous mode, entries
        are only required for those addresses for which the system
        would receive frames were it not operating in promiscuous
        mode.
        
        \- for 802.5 functional addresses, only one entry is
        required, for the address which has the functional address
        bit ANDed with the bit mask of all functional addresses for
        which the interface will accept frames.
        
        A system is normally able to use any unicast address which
        corresponds to an entry in this table as a source address.
        
        .. attribute:: ifrcvaddressentry
        
        	A list of objects identifying an address for which the system will accept packets/frames on the particular interface identified by the index value ifIndex
        	**type**\: list of    :py:class:`Ifrcvaddressentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable.Ifrcvaddressentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IfMib.Ifrcvaddresstable, self).__init__()

            self.yang_name = "ifRcvAddressTable"
            self.yang_parent_name = "IF-MIB"

            self.ifrcvaddressentry = YList(self)

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
                        super(IfMib.Ifrcvaddresstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IfMib.Ifrcvaddresstable, self).__setattr__(name, value)


        class Ifrcvaddressentry(Entity):
            """
            A list of objects identifying an address for which the
            system will accept packets/frames on the particular
            interface identified by the index value ifIndex.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ifrcvaddressaddress  <key>
            
            	An address for which the system will accept packets/frames on this entry's interface
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifrcvaddressstatus
            
            	This object is used to create and delete rows in the ifRcvAddressTable
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ifrcvaddresstype
            
            	This object has the value nonVolatile(3) for those entries in the table which are valid and will not be deleted by the next restart of the managed system.  Entries having the value volatile(2) are valid and exist, but have not been saved, so that will not exist after the next restart of the managed system.  Entries having the value other(1) are valid and exist but are not classified as to whether they will continue to exist after the next restart
            	**type**\:   :py:class:`Ifrcvaddresstype <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable.Ifrcvaddressentry.Ifrcvaddresstype>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IfMib.Ifrcvaddresstable.Ifrcvaddressentry, self).__init__()

                self.yang_name = "ifRcvAddressEntry"
                self.yang_parent_name = "ifRcvAddressTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.ifrcvaddressaddress = YLeaf(YType.str, "ifRcvAddressAddress")

                self.ifrcvaddressstatus = YLeaf(YType.enumeration, "ifRcvAddressStatus")

                self.ifrcvaddresstype = YLeaf(YType.enumeration, "ifRcvAddressType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "ifrcvaddressaddress",
                                "ifrcvaddressstatus",
                                "ifrcvaddresstype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IfMib.Ifrcvaddresstable.Ifrcvaddressentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IfMib.Ifrcvaddresstable.Ifrcvaddressentry, self).__setattr__(name, value)

            class Ifrcvaddresstype(Enum):
                """
                Ifrcvaddresstype

                This object has the value nonVolatile(3) for those entries

                in the table which are valid and will not be deleted by the

                next restart of the managed system.  Entries having the

                value volatile(2) are valid and exist, but have not been

                saved, so that will not exist after the next restart of the

                managed system.  Entries having the value other(1) are valid

                and exist but are not classified as to whether they will

                continue to exist after the next restart.

                .. data:: other = 1

                .. data:: volatile = 2

                .. data:: nonVolatile = 3

                """

                other = Enum.YLeaf(1, "other")

                volatile = Enum.YLeaf(2, "volatile")

                nonVolatile = Enum.YLeaf(3, "nonVolatile")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.ifrcvaddressaddress.is_set or
                    self.ifrcvaddressstatus.is_set or
                    self.ifrcvaddresstype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.ifrcvaddressaddress.yfilter != YFilter.not_set or
                    self.ifrcvaddressstatus.yfilter != YFilter.not_set or
                    self.ifrcvaddresstype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ifRcvAddressEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[ifRcvAddressAddress='" + self.ifrcvaddressaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IF-MIB:IF-MIB/ifRcvAddressTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.ifrcvaddressaddress.is_set or self.ifrcvaddressaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifrcvaddressaddress.get_name_leafdata())
                if (self.ifrcvaddressstatus.is_set or self.ifrcvaddressstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifrcvaddressstatus.get_name_leafdata())
                if (self.ifrcvaddresstype.is_set or self.ifrcvaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifrcvaddresstype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "ifRcvAddressAddress" or name == "ifRcvAddressStatus" or name == "ifRcvAddressType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ifRcvAddressAddress"):
                    self.ifrcvaddressaddress = value
                    self.ifrcvaddressaddress.value_namespace = name_space
                    self.ifrcvaddressaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ifRcvAddressStatus"):
                    self.ifrcvaddressstatus = value
                    self.ifrcvaddressstatus.value_namespace = name_space
                    self.ifrcvaddressstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifRcvAddressType"):
                    self.ifrcvaddresstype = value
                    self.ifrcvaddresstype.value_namespace = name_space
                    self.ifrcvaddresstype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ifrcvaddressentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ifrcvaddressentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ifRcvAddressTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IF-MIB:IF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ifRcvAddressEntry"):
                for c in self.ifrcvaddressentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IfMib.Ifrcvaddresstable.Ifrcvaddressentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ifrcvaddressentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifRcvAddressEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ifmibobjects is not None and self.ifmibobjects.has_data()) or
            (self.ifrcvaddresstable is not None and self.ifrcvaddresstable.has_data()) or
            (self.ifstacktable is not None and self.ifstacktable.has_data()) or
            (self.iftable is not None and self.iftable.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ifmibobjects is not None and self.ifmibobjects.has_operation()) or
            (self.ifrcvaddresstable is not None and self.ifrcvaddresstable.has_operation()) or
            (self.ifstacktable is not None and self.ifstacktable.has_operation()) or
            (self.iftable is not None and self.iftable.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "IF-MIB:IF-MIB" + path_buffer

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

        if (child_yang_name == "ifMIBObjects"):
            if (self.ifmibobjects is None):
                self.ifmibobjects = IfMib.Ifmibobjects()
                self.ifmibobjects.parent = self
                self._children_name_map["ifmibobjects"] = "ifMIBObjects"
            return self.ifmibobjects

        if (child_yang_name == "ifRcvAddressTable"):
            if (self.ifrcvaddresstable is None):
                self.ifrcvaddresstable = IfMib.Ifrcvaddresstable()
                self.ifrcvaddresstable.parent = self
                self._children_name_map["ifrcvaddresstable"] = "ifRcvAddressTable"
            return self.ifrcvaddresstable

        if (child_yang_name == "ifStackTable"):
            if (self.ifstacktable is None):
                self.ifstacktable = IfMib.Ifstacktable()
                self.ifstacktable.parent = self
                self._children_name_map["ifstacktable"] = "ifStackTable"
            return self.ifstacktable

        if (child_yang_name == "ifTable"):
            if (self.iftable is None):
                self.iftable = IfMib.Iftable()
                self.iftable.parent = self
                self._children_name_map["iftable"] = "ifTable"
            return self.iftable

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = IfMib.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ifMIBObjects" or name == "ifRcvAddressTable" or name == "ifStackTable" or name == "ifTable" or name == "interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IfMib()
        return self._top_entity

