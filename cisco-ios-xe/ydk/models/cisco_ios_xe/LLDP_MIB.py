""" LLDP_MIB 

Management Information Base module for LLDP configuration,
statistics, local system data and remote systems data
components.

Copyright (C) IEEE (2005).  This version of this MIB module
is published as subclause 12.1 of IEEE Std 802.1AB\-2005;
see the standard itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Lldpchassisidsubtype(Enum):
    """
    Lldpchassisidsubtype

    This TC describes the source of a chassis identifier.

    The enumeration 'chassisComponent(1)' represents a chassis

    identifier based on the value of entPhysicalAlias object

    (defined in IETF RFC 2737) for a chassis component (i.e.,

    an entPhysicalClass value of 'chassis(3)').

    The enumeration 'interfaceAlias(2)' represents a chassis

    identifier based on the value of ifAlias object (defined in

    IETF RFC 2863) for an interface on the containing chassis.

    The enumeration 'portComponent(3)' represents a chassis

    identifier based on the value of entPhysicalAlias object

    (defined in IETF RFC 2737) for a port or backplane

    component (i.e., entPhysicalClass value of 'port(10)' or

    'backplane(4)'), within the containing chassis.

    The enumeration 'macAddress(4)' represents a chassis

    identifier based on the value of a unicast source address

    (encoded in network byte order and IEEE 802.3 canonical bit

    order), of a port on the containing chassis as defined in

    IEEE Std 802\-2001.

    The enumeration 'networkAddress(5)' represents a chassis

    identifier based on a network address, associated with

    a particular chassis.  The encoded address is actually

    composed of two fields.  The first field is a single octet,

    representing the IANA AddressFamilyNumbers value for the

    specific address type, and the second field is the network

    address value.

    The enumeration 'interfaceName(6)' represents a chassis

    identifier based on the value of ifName object (defined in

    IETF RFC 2863) for an interface on the containing chassis.

    The enumeration 'local(7)' represents a chassis identifier

    based on a locally defined value.

    .. data:: chassisComponent = 1

    .. data:: interfaceAlias = 2

    .. data:: portComponent = 3

    .. data:: macAddress = 4

    .. data:: networkAddress = 5

    .. data:: interfaceName = 6

    .. data:: local = 7

    """

    chassisComponent = Enum.YLeaf(1, "chassisComponent")

    interfaceAlias = Enum.YLeaf(2, "interfaceAlias")

    portComponent = Enum.YLeaf(3, "portComponent")

    macAddress = Enum.YLeaf(4, "macAddress")

    networkAddress = Enum.YLeaf(5, "networkAddress")

    interfaceName = Enum.YLeaf(6, "interfaceName")

    local = Enum.YLeaf(7, "local")


class Lldpmanaddrifsubtype(Enum):
    """
    Lldpmanaddrifsubtype

    This TC describes the basis of a particular type of

    interface associated with the management address.

    The enumeration 'unknown(1)' represents the case where the

    interface is not known.

    The enumeration 'ifIndex(2)' represents interface identifier

    based on the ifIndex MIB object.

    The enumeration 'systemPortNumber(3)' represents interface

    identifier based on the system port numbering convention.

    .. data:: unknown = 1

    .. data:: ifIndex = 2

    .. data:: systemPortNumber = 3

    """

    unknown = Enum.YLeaf(1, "unknown")

    ifIndex = Enum.YLeaf(2, "ifIndex")

    systemPortNumber = Enum.YLeaf(3, "systemPortNumber")


class Lldpportidsubtype(Enum):
    """
    Lldpportidsubtype

    This TC describes the source of a particular type of port

    identifier used in the LLDP MIB.

    The enumeration 'interfaceAlias(1)' represents a port

    identifier based on the ifAlias MIB object, defined in IETF

    RFC 2863.

    The enumeration 'portComponent(2)' represents a port

    identifier based on the value of entPhysicalAlias (defined in

    IETF RFC 2737) for a port component (i.e., entPhysicalClass

    value of 'port(10)'), within the containing chassis.

    The enumeration 'macAddress(3)' represents a port identifier

    based on a unicast source address (encoded in network

    byte order and IEEE 802.3 canonical bit order), which has

    been detected by the agent and associated with a particular

    port (IEEE Std 802\-2001).

    The enumeration 'networkAddress(4)' represents a port

    identifier based on a network address, detected by the agent

    and associated with a particular port.

    The enumeration 'interfaceName(5)' represents a port

    identifier based on the ifName MIB object, defined in IETF

    RFC 2863.

    The enumeration 'agentCircuitId(6)' represents a port

    identifier based on the agent\-local identifier of the circuit

    (defined in RFC 3046), detected by the agent and associated

    with a particular port.

    The enumeration 'local(7)' represents a port identifier

    based on a value locally assigned.

    .. data:: interfaceAlias = 1

    .. data:: portComponent = 2

    .. data:: macAddress = 3

    .. data:: networkAddress = 4

    .. data:: interfaceName = 5

    .. data:: agentCircuitId = 6

    .. data:: local = 7

    """

    interfaceAlias = Enum.YLeaf(1, "interfaceAlias")

    portComponent = Enum.YLeaf(2, "portComponent")

    macAddress = Enum.YLeaf(3, "macAddress")

    networkAddress = Enum.YLeaf(4, "networkAddress")

    interfaceName = Enum.YLeaf(5, "interfaceName")

    agentCircuitId = Enum.YLeaf(6, "agentCircuitId")

    local = Enum.YLeaf(7, "local")


class Lldpsystemcapabilitiesmap(Bits):
    """
    Lldpsystemcapabilitiesmap

    This TC describes the system capabilities.
    
    The bit 'other(0)' indicates that the system has capabilities
    other than those listed below.
    
    The bit 'repeater(1)' indicates that the system has repeater
    capability.
    
    The bit 'bridge(2)' indicates that the system has bridge
    capability.
    
    The bit 'wlanAccessPoint(3)' indicates that the system has 
    WLAN access point capability.
    
    The bit 'router(4)' indicates that the system has router
    capability.
    
    The bit 'telephone(5)' indicates that the system has telephone
    capability.
    
    The bit 'docsisCableDevice(6)' indicates that the system has
    DOCSIS Cable Device capability (IETF RFC 2669 & 2670).
    
    The bit 'stationOnly(7)' indicates that the system has only
    station capability and nothing else.
    Keys are:- stationOnly , docsisCableDevice , bridge , wlanAccessPoint , telephone , repeater , router , other

    """

    def __init__(self):
        super(Lldpsystemcapabilitiesmap, self).__init__()


class LldpMib(Entity):
    """
    
    
    .. attribute:: lldpconfiguration
    
    	
    	**type**\:   :py:class:`Lldpconfiguration <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpconfiguration>`
    
    .. attribute:: lldplocalsystemdata
    
    	
    	**type**\:   :py:class:`Lldplocalsystemdata <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldplocalsystemdata>`
    
    .. attribute:: lldplocmanaddrtable
    
    	This table contains management address information on the local system known to this agent
    	**type**\:   :py:class:`Lldplocmanaddrtable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldplocmanaddrtable>`
    
    .. attribute:: lldplocporttable
    
    	This table contains one or more rows per port information associated with the local system known to this agent
    	**type**\:   :py:class:`Lldplocporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldplocporttable>`
    
    .. attribute:: lldpportconfigtable
    
    	The table that controls LLDP frame transmission on individual ports
    	**type**\:   :py:class:`Lldpportconfigtable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpportconfigtable>`
    
    .. attribute:: lldpremmanaddrtable
    
    	This table contains one or more rows per management address information on the remote system learned on a particular port contained in the local chassis known to this agent
    	**type**\:   :py:class:`Lldpremmanaddrtable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremmanaddrtable>`
    
    .. attribute:: lldpremorgdefinfotable
    
    	This table contains one or more rows per physical network connection which advertises the organizationally defined information.  Note that this table contains one or more rows of organizationally defined information that is not recognized by the local agent.  If the local system is capable of recognizing any organizationally defined information, appropriate extension MIBs from the organization should be used for information retrieval
    	**type**\:   :py:class:`Lldpremorgdefinfotable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremorgdefinfotable>`
    
    .. attribute:: lldpremtable
    
    	This table contains one or more rows per physical network connection known to this agent.  The agent may wish to ensure that only one lldpRemEntry is present for each local port, or it may choose to maintain multiple lldpRemEntries for the same local port.  The following procedure may be used to retrieve remote systems information updates from an LLDP agent\:     1. NMS polls all tables associated with remote systems       and keeps a local copy of the information retrieved.       NMS polls periodically the values of the following       objects\:          a. lldpStatsRemTablesInserts          b. lldpStatsRemTablesDeletes          c. lldpStatsRemTablesDrops          d. lldpStatsRemTablesAgeouts          e. lldpStatsRxPortAgeoutsTotal for all ports.     2. LLDP agent updates remote systems MIB objects, and       sends out notifications to a list of notification       destinations.     3. NMS receives the notifications and compares the new       values of objects listed in step 1.          Periodically, NMS should poll the object       lldpStatsRemTablesLastChangeTime to find out if anything       has changed since the last poll.  if something has       changed, NMS will poll the objects listed in step 1 to       figure out what kind of changes occurred in the tables.        if value of lldpStatsRemTablesInserts has changed,       then NMS will walk all tables by employing TimeFilter       with the last\-polled time value.  This request will       return new objects or objects whose values are updated       since the last poll.        if value of lldpStatsRemTablesAgeouts has changed,       then NMS will walk the lldpStatsRxPortAgeoutsTotal and       compare the new values with previously recorded ones.       For ports whose lldpStatsRxPortAgeoutsTotal value is       greater than the recorded value, NMS will have to       retrieve objects associated with those ports from       table(s) without employing a TimeFilter (which is       performed by specifying 0 for the TimeFilter.)        lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops       objects are provided for informational purposes
    	**type**\:   :py:class:`Lldpremtable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable>`
    
    .. attribute:: lldpremunknowntlvtable
    
    	This table contains information about an incoming TLV which is not recognized by the receiving LLDP agent.  The TLV may be from a later version of the basic management set.  This table should only contain TLVs that are found in a single LLDP frame.  Entries in this table, associated with an MAC service access point (MSAP, the access point for MAC services provided to the LCC sublayer, defined in IEEE 100, which is also identified with a particular lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with most recently received unrecognized TLV from the same MSAP, or they will naturally age out when the rxInfoTTL timer (associated with the MSAP) expires
    	**type**\:   :py:class:`Lldpremunknowntlvtable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremunknowntlvtable>`
    
    .. attribute:: lldpstatistics
    
    	
    	**type**\:   :py:class:`Lldpstatistics <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpstatistics>`
    
    .. attribute:: lldpstatsrxporttable
    
    	A table containing LLDP reception statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:   :py:class:`Lldpstatsrxporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpstatsrxporttable>`
    
    .. attribute:: lldpstatstxporttable
    
    	A table containing LLDP transmission statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:   :py:class:`Lldpstatstxporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpstatstxporttable>`
    
    

    """

    _prefix = 'LLDP-MIB'
    _revision = '2005-05-06'

    def __init__(self):
        super(LldpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "LLDP-MIB"
        self.yang_parent_name = "LLDP-MIB"

        self.lldpconfiguration = LldpMib.Lldpconfiguration()
        self.lldpconfiguration.parent = self
        self._children_name_map["lldpconfiguration"] = "lldpConfiguration"
        self._children_yang_names.add("lldpConfiguration")

        self.lldplocalsystemdata = LldpMib.Lldplocalsystemdata()
        self.lldplocalsystemdata.parent = self
        self._children_name_map["lldplocalsystemdata"] = "lldpLocalSystemData"
        self._children_yang_names.add("lldpLocalSystemData")

        self.lldplocmanaddrtable = LldpMib.Lldplocmanaddrtable()
        self.lldplocmanaddrtable.parent = self
        self._children_name_map["lldplocmanaddrtable"] = "lldpLocManAddrTable"
        self._children_yang_names.add("lldpLocManAddrTable")

        self.lldplocporttable = LldpMib.Lldplocporttable()
        self.lldplocporttable.parent = self
        self._children_name_map["lldplocporttable"] = "lldpLocPortTable"
        self._children_yang_names.add("lldpLocPortTable")

        self.lldpportconfigtable = LldpMib.Lldpportconfigtable()
        self.lldpportconfigtable.parent = self
        self._children_name_map["lldpportconfigtable"] = "lldpPortConfigTable"
        self._children_yang_names.add("lldpPortConfigTable")

        self.lldpremmanaddrtable = LldpMib.Lldpremmanaddrtable()
        self.lldpremmanaddrtable.parent = self
        self._children_name_map["lldpremmanaddrtable"] = "lldpRemManAddrTable"
        self._children_yang_names.add("lldpRemManAddrTable")

        self.lldpremorgdefinfotable = LldpMib.Lldpremorgdefinfotable()
        self.lldpremorgdefinfotable.parent = self
        self._children_name_map["lldpremorgdefinfotable"] = "lldpRemOrgDefInfoTable"
        self._children_yang_names.add("lldpRemOrgDefInfoTable")

        self.lldpremtable = LldpMib.Lldpremtable()
        self.lldpremtable.parent = self
        self._children_name_map["lldpremtable"] = "lldpRemTable"
        self._children_yang_names.add("lldpRemTable")

        self.lldpremunknowntlvtable = LldpMib.Lldpremunknowntlvtable()
        self.lldpremunknowntlvtable.parent = self
        self._children_name_map["lldpremunknowntlvtable"] = "lldpRemUnknownTLVTable"
        self._children_yang_names.add("lldpRemUnknownTLVTable")

        self.lldpstatistics = LldpMib.Lldpstatistics()
        self.lldpstatistics.parent = self
        self._children_name_map["lldpstatistics"] = "lldpStatistics"
        self._children_yang_names.add("lldpStatistics")

        self.lldpstatsrxporttable = LldpMib.Lldpstatsrxporttable()
        self.lldpstatsrxporttable.parent = self
        self._children_name_map["lldpstatsrxporttable"] = "lldpStatsRxPortTable"
        self._children_yang_names.add("lldpStatsRxPortTable")

        self.lldpstatstxporttable = LldpMib.Lldpstatstxporttable()
        self.lldpstatstxporttable.parent = self
        self._children_name_map["lldpstatstxporttable"] = "lldpStatsTxPortTable"
        self._children_yang_names.add("lldpStatsTxPortTable")


    class Lldpconfiguration(Entity):
        """
        
        
        .. attribute:: lldpmessagetxholdmultiplier
        
        	The time\-to\-live value expressed as a multiple of the lldpMessageTxInterval object.  The actual time\-to\-live value used in LLDP frames, transmitted on behalf of this LLDP agent, can be expressed by the following formula\: TTL = min(65535, (lldpMessageTxInterval \* lldpMessageTxHoldMultiplier)) For example, if the value of lldpMessageTxInterval is '30', and the value of lldpMessageTxHoldMultiplier is '4', then the value '120' is encoded in the TTL field in the LLDP header.  The default value for lldpMessageTxHoldMultiplier object is 4.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\:  int
        
        	**range:** 2..10
        
        .. attribute:: lldpmessagetxinterval
        
        	The interval at which LLDP frames are transmitted on behalf of this LLDP agent.  The default value for lldpMessageTxInterval object is 30 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\:  int
        
        	**range:** 5..32768
        
        	**units**\: seconds
        
        .. attribute:: lldpnotificationinterval
        
        	This object controls the transmission of LLDP notifications.  the agent must not generate more than one lldpRemTablesChange notification\-event in the indicated period, where a 'notification\-event' is the transmission of a single notification PDU type to a list of notification destinations. If additional changes in lldpRemoteSystemsData object groups occur within the indicated throttling period, then these trap\- events must be suppressed by the agent. An NMS should periodically check the value of lldpStatsRemTableLastChangeTime to detect any missed lldpRemTablesChange notification\-events, e.g. due to throttling or transmission loss.  If notification transmission is enabled for particular ports, the suggested default throttling period is 5 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\:  int
        
        	**range:** 5..3600
        
        	**units**\: seconds
        
        .. attribute:: lldpreinitdelay
        
        	The lldpReinitDelay indicates the delay (in units of seconds) from when lldpPortConfigAdminStatus object of a particular port becomes 'disabled' until re\-initialization will be attempted.  The default value for lldpReintDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: seconds
        
        .. attribute:: lldptxdelay
        
        	The lldpTxDelay indicates the delay (in units of seconds) between successive LLDP frame transmissions  initiated by value/status changes in the LLDP local systems MIB.  The recommended value for the lldpTxDelay is set by the following  formula\:     1 <= lldpTxDelay <= (0.25 \* lldpMessageTxInterval)  The default value for lldpTxDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\:  int
        
        	**range:** 1..8192
        
        	**units**\: seconds
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpconfiguration, self).__init__()

            self.yang_name = "lldpConfiguration"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpmessagetxholdmultiplier = YLeaf(YType.int32, "lldpMessageTxHoldMultiplier")

            self.lldpmessagetxinterval = YLeaf(YType.int32, "lldpMessageTxInterval")

            self.lldpnotificationinterval = YLeaf(YType.int32, "lldpNotificationInterval")

            self.lldpreinitdelay = YLeaf(YType.int32, "lldpReinitDelay")

            self.lldptxdelay = YLeaf(YType.int32, "lldpTxDelay")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("lldpmessagetxholdmultiplier",
                            "lldpmessagetxinterval",
                            "lldpnotificationinterval",
                            "lldpreinitdelay",
                            "lldptxdelay") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LldpMib.Lldpconfiguration, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpconfiguration, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.lldpmessagetxholdmultiplier.is_set or
                self.lldpmessagetxinterval.is_set or
                self.lldpnotificationinterval.is_set or
                self.lldpreinitdelay.is_set or
                self.lldptxdelay.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.lldpmessagetxholdmultiplier.yfilter != YFilter.not_set or
                self.lldpmessagetxinterval.yfilter != YFilter.not_set or
                self.lldpnotificationinterval.yfilter != YFilter.not_set or
                self.lldpreinitdelay.yfilter != YFilter.not_set or
                self.lldptxdelay.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpConfiguration" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.lldpmessagetxholdmultiplier.is_set or self.lldpmessagetxholdmultiplier.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpmessagetxholdmultiplier.get_name_leafdata())
            if (self.lldpmessagetxinterval.is_set or self.lldpmessagetxinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpmessagetxinterval.get_name_leafdata())
            if (self.lldpnotificationinterval.is_set or self.lldpnotificationinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpnotificationinterval.get_name_leafdata())
            if (self.lldpreinitdelay.is_set or self.lldpreinitdelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpreinitdelay.get_name_leafdata())
            if (self.lldptxdelay.is_set or self.lldptxdelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldptxdelay.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpMessageTxHoldMultiplier" or name == "lldpMessageTxInterval" or name == "lldpNotificationInterval" or name == "lldpReinitDelay" or name == "lldpTxDelay"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "lldpMessageTxHoldMultiplier"):
                self.lldpmessagetxholdmultiplier = value
                self.lldpmessagetxholdmultiplier.value_namespace = name_space
                self.lldpmessagetxholdmultiplier.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpMessageTxInterval"):
                self.lldpmessagetxinterval = value
                self.lldpmessagetxinterval.value_namespace = name_space
                self.lldpmessagetxinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpNotificationInterval"):
                self.lldpnotificationinterval = value
                self.lldpnotificationinterval.value_namespace = name_space
                self.lldpnotificationinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpReinitDelay"):
                self.lldpreinitdelay = value
                self.lldpreinitdelay.value_namespace = name_space
                self.lldpreinitdelay.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpTxDelay"):
                self.lldptxdelay = value
                self.lldptxdelay.value_namespace = name_space
                self.lldptxdelay.value_namespace_prefix = name_space_prefix


    class Lldpstatistics(Entity):
        """
        
        
        .. attribute:: lldpstatsremtablesageouts
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter should be incremented only once when the complete set of information is completely invalidated (aged out) from all related tables.  Partial aging, similar to deletion case, is not allowed, and thus, should not change the value of this counter
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtablesdeletes
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects.  This counter should be incremented only once when the complete set of information is completely deleted from all related tables.  Partial deletions, such as deletion of rows associated with a particular MSAP from some tables, but not from all tables are not allowed, thus should not change the value of this counter
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesdrops
        
        	The number of times the complete set of information advertised by a particular MSAP could not be entered into tables contained in lldpRemoteSystemsData and lldpExtensions objects because of insufficient resources
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesinserts
        
        	The number of times the complete set of information advertised by a particular MSAP has been inserted into tables contained in lldpRemoteSystemsData and lldpExtensions objects.  The complete set of information received from a particular MSAP should be inserted into related tables.  If partial information cannot be inserted for a reason such as lack of resources, all of the complete set of information should be removed.  This counter should be incremented only once after the complete set of information is successfully recorded in all related tables.  Any failures during inserting information set which result in deletion of previously inserted information should not trigger any changes in lldpStatsRemTablesInserts since the insert is not completed yet or or in lldpStatsRemTablesDeletes, since the deletion would only be a partial deletion. If the failure was the result of lack of resources, the lldpStatsRemTablesDrops counter should be incremented once
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtableslastchangetime
        
        	The value of sysUpTime object (defined in IETF RFC 3418) at the time an entry is created, modified, or deleted in the in tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems.  An NMS can use this object to reduce polling of the lldpRemoteSystemsData objects
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpstatistics, self).__init__()

            self.yang_name = "lldpStatistics"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpstatsremtablesageouts = YLeaf(YType.uint32, "lldpStatsRemTablesAgeouts")

            self.lldpstatsremtablesdeletes = YLeaf(YType.uint32, "lldpStatsRemTablesDeletes")

            self.lldpstatsremtablesdrops = YLeaf(YType.uint32, "lldpStatsRemTablesDrops")

            self.lldpstatsremtablesinserts = YLeaf(YType.uint32, "lldpStatsRemTablesInserts")

            self.lldpstatsremtableslastchangetime = YLeaf(YType.uint32, "lldpStatsRemTablesLastChangeTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("lldpstatsremtablesageouts",
                            "lldpstatsremtablesdeletes",
                            "lldpstatsremtablesdrops",
                            "lldpstatsremtablesinserts",
                            "lldpstatsremtableslastchangetime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LldpMib.Lldpstatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpstatistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.lldpstatsremtablesageouts.is_set or
                self.lldpstatsremtablesdeletes.is_set or
                self.lldpstatsremtablesdrops.is_set or
                self.lldpstatsremtablesinserts.is_set or
                self.lldpstatsremtableslastchangetime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.lldpstatsremtablesageouts.yfilter != YFilter.not_set or
                self.lldpstatsremtablesdeletes.yfilter != YFilter.not_set or
                self.lldpstatsremtablesdrops.yfilter != YFilter.not_set or
                self.lldpstatsremtablesinserts.yfilter != YFilter.not_set or
                self.lldpstatsremtableslastchangetime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpStatistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.lldpstatsremtablesageouts.is_set or self.lldpstatsremtablesageouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpstatsremtablesageouts.get_name_leafdata())
            if (self.lldpstatsremtablesdeletes.is_set or self.lldpstatsremtablesdeletes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpstatsremtablesdeletes.get_name_leafdata())
            if (self.lldpstatsremtablesdrops.is_set or self.lldpstatsremtablesdrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpstatsremtablesdrops.get_name_leafdata())
            if (self.lldpstatsremtablesinserts.is_set or self.lldpstatsremtablesinserts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpstatsremtablesinserts.get_name_leafdata())
            if (self.lldpstatsremtableslastchangetime.is_set or self.lldpstatsremtableslastchangetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldpstatsremtableslastchangetime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpStatsRemTablesAgeouts" or name == "lldpStatsRemTablesDeletes" or name == "lldpStatsRemTablesDrops" or name == "lldpStatsRemTablesInserts" or name == "lldpStatsRemTablesLastChangeTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "lldpStatsRemTablesAgeouts"):
                self.lldpstatsremtablesageouts = value
                self.lldpstatsremtablesageouts.value_namespace = name_space
                self.lldpstatsremtablesageouts.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpStatsRemTablesDeletes"):
                self.lldpstatsremtablesdeletes = value
                self.lldpstatsremtablesdeletes.value_namespace = name_space
                self.lldpstatsremtablesdeletes.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpStatsRemTablesDrops"):
                self.lldpstatsremtablesdrops = value
                self.lldpstatsremtablesdrops.value_namespace = name_space
                self.lldpstatsremtablesdrops.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpStatsRemTablesInserts"):
                self.lldpstatsremtablesinserts = value
                self.lldpstatsremtablesinserts.value_namespace = name_space
                self.lldpstatsremtablesinserts.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpStatsRemTablesLastChangeTime"):
                self.lldpstatsremtableslastchangetime = value
                self.lldpstatsremtableslastchangetime.value_namespace = name_space
                self.lldpstatsremtableslastchangetime.value_namespace_prefix = name_space_prefix


    class Lldplocalsystemdata(Entity):
        """
        
        
        .. attribute:: lldplocchassisid
        
        	The string value used to identify the chassis component associated with the local system
        	**type**\:  str
        
        	**length:** 1..255
        
        .. attribute:: lldplocchassisidsubtype
        
        	The type of encoding used to identify the chassis associated with the local system
        	**type**\:   :py:class:`Lldpchassisidsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpchassisidsubtype>`
        
        .. attribute:: lldplocsyscapenabled
        
        	The bitmap value used to identify which system capabilities are enabled on the local system
        	**type**\:   :py:class:`Lldpsystemcapabilitiesmap <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpsystemcapabilitiesmap>`
        
        .. attribute:: lldplocsyscapsupported
        
        	The bitmap value used to identify which system capabilities are supported on the local system
        	**type**\:   :py:class:`Lldpsystemcapabilitiesmap <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpsystemcapabilitiesmap>`
        
        .. attribute:: lldplocsysdesc
        
        	The string value used to identify the system description of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysDesc object should have the same value of sysDesc object
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: lldplocsysname
        
        	The string value used to identify the system name of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysName object should have the same value of sysName object
        	**type**\:  str
        
        	**length:** 0..255
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldplocalsystemdata, self).__init__()

            self.yang_name = "lldpLocalSystemData"
            self.yang_parent_name = "LLDP-MIB"

            self.lldplocchassisid = YLeaf(YType.str, "lldpLocChassisId")

            self.lldplocchassisidsubtype = YLeaf(YType.enumeration, "lldpLocChassisIdSubtype")

            self.lldplocsyscapenabled = YLeaf(YType.bits, "lldpLocSysCapEnabled")

            self.lldplocsyscapsupported = YLeaf(YType.bits, "lldpLocSysCapSupported")

            self.lldplocsysdesc = YLeaf(YType.str, "lldpLocSysDesc")

            self.lldplocsysname = YLeaf(YType.str, "lldpLocSysName")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("lldplocchassisid",
                            "lldplocchassisidsubtype",
                            "lldplocsyscapenabled",
                            "lldplocsyscapsupported",
                            "lldplocsysdesc",
                            "lldplocsysname") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LldpMib.Lldplocalsystemdata, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldplocalsystemdata, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.lldplocchassisid.is_set or
                self.lldplocchassisidsubtype.is_set or
                self.lldplocsyscapenabled.is_set or
                self.lldplocsyscapsupported.is_set or
                self.lldplocsysdesc.is_set or
                self.lldplocsysname.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.lldplocchassisid.yfilter != YFilter.not_set or
                self.lldplocchassisidsubtype.yfilter != YFilter.not_set or
                self.lldplocsyscapenabled.yfilter != YFilter.not_set or
                self.lldplocsyscapsupported.yfilter != YFilter.not_set or
                self.lldplocsysdesc.yfilter != YFilter.not_set or
                self.lldplocsysname.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpLocalSystemData" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.lldplocchassisid.is_set or self.lldplocchassisid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocchassisid.get_name_leafdata())
            if (self.lldplocchassisidsubtype.is_set or self.lldplocchassisidsubtype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocchassisidsubtype.get_name_leafdata())
            if (self.lldplocsyscapenabled.is_set or self.lldplocsyscapenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocsyscapenabled.get_name_leafdata())
            if (self.lldplocsyscapsupported.is_set or self.lldplocsyscapsupported.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocsyscapsupported.get_name_leafdata())
            if (self.lldplocsysdesc.is_set or self.lldplocsysdesc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocsysdesc.get_name_leafdata())
            if (self.lldplocsysname.is_set or self.lldplocsysname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lldplocsysname.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpLocChassisId" or name == "lldpLocChassisIdSubtype" or name == "lldpLocSysCapEnabled" or name == "lldpLocSysCapSupported" or name == "lldpLocSysDesc" or name == "lldpLocSysName"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "lldpLocChassisId"):
                self.lldplocchassisid = value
                self.lldplocchassisid.value_namespace = name_space
                self.lldplocchassisid.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpLocChassisIdSubtype"):
                self.lldplocchassisidsubtype = value
                self.lldplocchassisidsubtype.value_namespace = name_space
                self.lldplocchassisidsubtype.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpLocSysCapEnabled"):
                self.lldplocsyscapenabled[value] = True
            if(value_path == "lldpLocSysCapSupported"):
                self.lldplocsyscapsupported[value] = True
            if(value_path == "lldpLocSysDesc"):
                self.lldplocsysdesc = value
                self.lldplocsysdesc.value_namespace = name_space
                self.lldplocsysdesc.value_namespace_prefix = name_space_prefix
            if(value_path == "lldpLocSysName"):
                self.lldplocsysname = value
                self.lldplocsysname.value_namespace = name_space
                self.lldplocsysname.value_namespace_prefix = name_space_prefix


    class Lldpportconfigtable(Entity):
        """
        The table that controls LLDP frame transmission on individual
        ports.
        
        .. attribute:: lldpportconfigentry
        
        	LLDP configuration information for a particular port. This configuration parameter controls the transmission and the reception of LLDP frames on those ports whose rows are created in this table
        	**type**\: list of    :py:class:`Lldpportconfigentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpportconfigtable.Lldpportconfigentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpportconfigtable, self).__init__()

            self.yang_name = "lldpPortConfigTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpportconfigentry = YList(self)

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
                        super(LldpMib.Lldpportconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpportconfigtable, self).__setattr__(name, value)


        class Lldpportconfigentry(Entity):
            """
            LLDP configuration information for a particular port.
            This configuration parameter controls the transmission and
            the reception of LLDP frames on those ports whose rows are
            created in this table.
            
            .. attribute:: lldpportconfigportnum  <key>
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpPortConfigTable
            	**type**\:  int
            
            	**range:** 1..4096
            
            .. attribute:: lldpportconfigadminstatus
            
            	The administratively desired status of the local LLDP agent.  If the associated lldpPortConfigAdminStatus object has a value of 'txOnly(1)', then LLDP agent will transmit LLDP frames on this port and it will not store any information about the remote systems connected.  If the associated lldpPortConfigAdminStatus object has a value of 'rxOnly(2)', then the LLDP agent will receive, but it will not transmit LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'txAndRx(3)', then the LLDP agent will transmit and receive LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'disabled(4)', then LLDP agent will not transmit or receive LLDP frames on this port.  If there is remote systems information which is received on this port and stored in other tables, before the port's lldpPortConfigAdminStatus becomes disabled, then the information will naturally age out
            	**type**\:   :py:class:`Lldpportconfigadminstatus <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpportconfigtable.Lldpportconfigentry.Lldpportconfigadminstatus>`
            
            .. attribute:: lldpportconfignotificationenable
            
            	The lldpPortConfigNotificationEnable controls, on a per port basis,  whether or not notifications from the agent are enabled. The value true(1) means that notifications are enabled; the value false(2) means that they are not
            	**type**\:  bool
            
            .. attribute:: lldpportconfigtlvstxenable
            
            	The lldpPortConfigTLVsTxEnable, defined as a bitmap, includes the basic set of LLDP TLVs whose transmission is allowed on the local LLDP agent by the network management. Each bit in the bitmap corresponds to a TLV type associated with a specific optional TLV.  It should be noted that the organizationally\-specific TLVs are excluded from the lldpTLVsTxEnable bitmap.  LLDP Organization Specific Information Extension MIBs should have similar configuration object to control transmission of their organizationally defined TLVs.  The bit 'portDesc(0)' indicates that LLDP agent should transmit 'Port Description TLV'.  The bit 'sysName(1)' indicates that LLDP agent should transmit 'System Name TLV'.  The bit 'sysDesc(2)' indicates that LLDP agent should transmit 'System Description TLV'.  The bit 'sysCap(3)' indicates that LLDP agent should transmit 'System Capabilities TLV'.  There is no bit reserved for the management address TLV type since transmission of management address TLVs are controlled by another object, lldpConfigManAddrTable.  The default value for lldpPortConfigTLVsTxEnable object is empty set, which means no enumerated values are set.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
            	**type**\:   :py:class:`Lldpportconfigtlvstxenable <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpportconfigtable.Lldpportconfigentry.Lldpportconfigtlvstxenable>`
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpportconfigtable.Lldpportconfigentry, self).__init__()

                self.yang_name = "lldpPortConfigEntry"
                self.yang_parent_name = "lldpPortConfigTable"

                self.lldpportconfigportnum = YLeaf(YType.int32, "lldpPortConfigPortNum")

                self.lldpportconfigadminstatus = YLeaf(YType.enumeration, "lldpPortConfigAdminStatus")

                self.lldpportconfignotificationenable = YLeaf(YType.boolean, "lldpPortConfigNotificationEnable")

                self.lldpportconfigtlvstxenable = YLeaf(YType.bits, "lldpPortConfigTLVsTxEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpportconfigportnum",
                                "lldpportconfigadminstatus",
                                "lldpportconfignotificationenable",
                                "lldpportconfigtlvstxenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpportconfigtable.Lldpportconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpportconfigtable.Lldpportconfigentry, self).__setattr__(name, value)

            class Lldpportconfigadminstatus(Enum):
                """
                Lldpportconfigadminstatus

                The administratively desired status of the local LLDP agent.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'txOnly(1)', then LLDP agent will transmit LLDP

                frames on this port and it will not store any information

                about the remote systems connected.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'rxOnly(2)', then the LLDP agent will receive,

                but it will not transmit LLDP frames on this port.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'txAndRx(3)', then the LLDP agent will transmit

                and receive LLDP frames on this port.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'disabled(4)', then LLDP agent will not transmit or

                receive LLDP frames on this port.  If there is remote systems

                information which is received on this port and stored in

                other tables, before the port's lldpPortConfigAdminStatus

                becomes disabled, then the information will naturally age out.

                .. data:: txOnly = 1

                .. data:: rxOnly = 2

                .. data:: txAndRx = 3

                .. data:: disabled = 4

                """

                txOnly = Enum.YLeaf(1, "txOnly")

                rxOnly = Enum.YLeaf(2, "rxOnly")

                txAndRx = Enum.YLeaf(3, "txAndRx")

                disabled = Enum.YLeaf(4, "disabled")


            def has_data(self):
                return (
                    self.lldpportconfigportnum.is_set or
                    self.lldpportconfigadminstatus.is_set or
                    self.lldpportconfignotificationenable.is_set or
                    self.lldpportconfigtlvstxenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpportconfigportnum.yfilter != YFilter.not_set or
                    self.lldpportconfigadminstatus.yfilter != YFilter.not_set or
                    self.lldpportconfignotificationenable.yfilter != YFilter.not_set or
                    self.lldpportconfigtlvstxenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpPortConfigEntry" + "[lldpPortConfigPortNum='" + self.lldpportconfigportnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpPortConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpportconfigportnum.is_set or self.lldpportconfigportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpportconfigportnum.get_name_leafdata())
                if (self.lldpportconfigadminstatus.is_set or self.lldpportconfigadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpportconfigadminstatus.get_name_leafdata())
                if (self.lldpportconfignotificationenable.is_set or self.lldpportconfignotificationenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpportconfignotificationenable.get_name_leafdata())
                if (self.lldpportconfigtlvstxenable.is_set or self.lldpportconfigtlvstxenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpportconfigtlvstxenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpPortConfigPortNum" or name == "lldpPortConfigAdminStatus" or name == "lldpPortConfigNotificationEnable" or name == "lldpPortConfigTLVsTxEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpPortConfigPortNum"):
                    self.lldpportconfigportnum = value
                    self.lldpportconfigportnum.value_namespace = name_space
                    self.lldpportconfigportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpPortConfigAdminStatus"):
                    self.lldpportconfigadminstatus = value
                    self.lldpportconfigadminstatus.value_namespace = name_space
                    self.lldpportconfigadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpPortConfigNotificationEnable"):
                    self.lldpportconfignotificationenable = value
                    self.lldpportconfignotificationenable.value_namespace = name_space
                    self.lldpportconfignotificationenable.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpPortConfigTLVsTxEnable"):
                    self.lldpportconfigtlvstxenable[value] = True

        def has_data(self):
            for c in self.lldpportconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpportconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpPortConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpPortConfigEntry"):
                for c in self.lldpportconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpportconfigtable.Lldpportconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpportconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpPortConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpstatstxporttable(Entity):
        """
        A table containing LLDP transmission statistics for
        individual ports.  Entries are not required to exist in
        this table while the lldpPortConfigEntry object is equal to
        'disabled(4)'.
        
        .. attribute:: lldpstatstxportentry
        
        	LLDP frame transmission statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of    :py:class:`Lldpstatstxportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpstatstxporttable.Lldpstatstxportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpstatstxporttable, self).__init__()

            self.yang_name = "lldpStatsTxPortTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpstatstxportentry = YList(self)

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
                        super(LldpMib.Lldpstatstxporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpstatstxporttable, self).__setattr__(name, value)


        class Lldpstatstxportentry(Entity):
            """
            LLDP frame transmission statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatstxportnum  <key>
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\:  int
            
            	**range:** 1..4096
            
            .. attribute:: lldpstatstxportframestotal
            
            	The number of LLDP frames transmitted by this LLDP agent on the indicated port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpstatstxporttable.Lldpstatstxportentry, self).__init__()

                self.yang_name = "lldpStatsTxPortEntry"
                self.yang_parent_name = "lldpStatsTxPortTable"

                self.lldpstatstxportnum = YLeaf(YType.int32, "lldpStatsTxPortNum")

                self.lldpstatstxportframestotal = YLeaf(YType.uint32, "lldpStatsTxPortFramesTotal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpstatstxportnum",
                                "lldpstatstxportframestotal") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpstatstxporttable.Lldpstatstxportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpstatstxporttable.Lldpstatstxportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpstatstxportnum.is_set or
                    self.lldpstatstxportframestotal.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpstatstxportnum.yfilter != YFilter.not_set or
                    self.lldpstatstxportframestotal.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpStatsTxPortEntry" + "[lldpStatsTxPortNum='" + self.lldpstatstxportnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpStatsTxPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpstatstxportnum.is_set or self.lldpstatstxportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatstxportnum.get_name_leafdata())
                if (self.lldpstatstxportframestotal.is_set or self.lldpstatstxportframestotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatstxportframestotal.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpStatsTxPortNum" or name == "lldpStatsTxPortFramesTotal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpStatsTxPortNum"):
                    self.lldpstatstxportnum = value
                    self.lldpstatstxportnum.value_namespace = name_space
                    self.lldpstatstxportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsTxPortFramesTotal"):
                    self.lldpstatstxportframestotal = value
                    self.lldpstatstxportframestotal.value_namespace = name_space
                    self.lldpstatstxportframestotal.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldpstatstxportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpstatstxportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpStatsTxPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpStatsTxPortEntry"):
                for c in self.lldpstatstxportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpstatstxporttable.Lldpstatstxportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpstatstxportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpStatsTxPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpstatsrxporttable(Entity):
        """
        A table containing LLDP reception statistics for individual
        ports.  Entries are not required to exist in this table while
        the lldpPortConfigEntry object is equal to 'disabled(4)'.
        
        .. attribute:: lldpstatsrxportentry
        
        	LLDP frame reception statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of    :py:class:`Lldpstatsrxportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpstatsrxporttable.Lldpstatsrxportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpstatsrxporttable, self).__init__()

            self.yang_name = "lldpStatsRxPortTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpstatsrxportentry = YList(self)

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
                        super(LldpMib.Lldpstatsrxporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpstatsrxporttable, self).__setattr__(name, value)


        class Lldpstatsrxportentry(Entity):
            """
            LLDP frame reception statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatsrxportnum  <key>
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\:  int
            
            	**range:** 1..4096
            
            .. attribute:: lldpstatsrxportageoutstotal
            
            	The counter that represents the number of age\-outs that occurred on a given port.  An age\-out is the number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter is similar to lldpStatsRemTablesAgeouts, except that the counter is on a per port basis.  This enables NMS to poll tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems on the indicated port only.  This counter should be set to zero during agent initialization and its value should not be saved in non\-volatile storage. When a port's admin status changes from 'disabled' to 'rxOnly', 'txOnly' or 'txAndRx', the counter associated with the same port should reset to 0.  The agent should also flush all remote system information associated with the same port.  This counter should be incremented only once when the complete set of information is invalidated (aged out) from all related tables on a particular port.  Partial aging is not allowed, and thus, should not change the value of this counter
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframesdiscardedtotal
            
            	The number of LLDP frames received by this LLDP agent on the indicated port, and then discarded for any reason. This counter can provide an indication that LLDP header formating problems may exist with the local LLDP agent in the sending system or that LLDPDU validation problems may exist with the local LLDP agent in the receiving system
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframeserrors
            
            	The number of invalid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframestotal
            
            	The number of valid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsdiscardedtotal
            
            	The number of LLDP TLVs discarded for any reason by this LLDP agent on the indicated port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsunrecognizedtotal
            
            	The number of LLDP TLVs received on the given port that are not recognized by this LLDP agent on the indicated port.  An unrecognized TLV is referred to as the TLV whose type value is in the range of reserved TLV types (000 1001 \- 111 1110) in Table 9.1 of IEEE Std 802.1AB\-2005.  An unrecognized TLV may be a basic management TLV from a later LLDP version
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpstatsrxporttable.Lldpstatsrxportentry, self).__init__()

                self.yang_name = "lldpStatsRxPortEntry"
                self.yang_parent_name = "lldpStatsRxPortTable"

                self.lldpstatsrxportnum = YLeaf(YType.int32, "lldpStatsRxPortNum")

                self.lldpstatsrxportageoutstotal = YLeaf(YType.uint32, "lldpStatsRxPortAgeoutsTotal")

                self.lldpstatsrxportframesdiscardedtotal = YLeaf(YType.uint32, "lldpStatsRxPortFramesDiscardedTotal")

                self.lldpstatsrxportframeserrors = YLeaf(YType.uint32, "lldpStatsRxPortFramesErrors")

                self.lldpstatsrxportframestotal = YLeaf(YType.uint32, "lldpStatsRxPortFramesTotal")

                self.lldpstatsrxporttlvsdiscardedtotal = YLeaf(YType.uint32, "lldpStatsRxPortTLVsDiscardedTotal")

                self.lldpstatsrxporttlvsunrecognizedtotal = YLeaf(YType.uint32, "lldpStatsRxPortTLVsUnrecognizedTotal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpstatsrxportnum",
                                "lldpstatsrxportageoutstotal",
                                "lldpstatsrxportframesdiscardedtotal",
                                "lldpstatsrxportframeserrors",
                                "lldpstatsrxportframestotal",
                                "lldpstatsrxporttlvsdiscardedtotal",
                                "lldpstatsrxporttlvsunrecognizedtotal") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpstatsrxporttable.Lldpstatsrxportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpstatsrxporttable.Lldpstatsrxportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpstatsrxportnum.is_set or
                    self.lldpstatsrxportageoutstotal.is_set or
                    self.lldpstatsrxportframesdiscardedtotal.is_set or
                    self.lldpstatsrxportframeserrors.is_set or
                    self.lldpstatsrxportframestotal.is_set or
                    self.lldpstatsrxporttlvsdiscardedtotal.is_set or
                    self.lldpstatsrxporttlvsunrecognizedtotal.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpstatsrxportnum.yfilter != YFilter.not_set or
                    self.lldpstatsrxportageoutstotal.yfilter != YFilter.not_set or
                    self.lldpstatsrxportframesdiscardedtotal.yfilter != YFilter.not_set or
                    self.lldpstatsrxportframeserrors.yfilter != YFilter.not_set or
                    self.lldpstatsrxportframestotal.yfilter != YFilter.not_set or
                    self.lldpstatsrxporttlvsdiscardedtotal.yfilter != YFilter.not_set or
                    self.lldpstatsrxporttlvsunrecognizedtotal.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpStatsRxPortEntry" + "[lldpStatsRxPortNum='" + self.lldpstatsrxportnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpStatsRxPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpstatsrxportnum.is_set or self.lldpstatsrxportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxportnum.get_name_leafdata())
                if (self.lldpstatsrxportageoutstotal.is_set or self.lldpstatsrxportageoutstotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxportageoutstotal.get_name_leafdata())
                if (self.lldpstatsrxportframesdiscardedtotal.is_set or self.lldpstatsrxportframesdiscardedtotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxportframesdiscardedtotal.get_name_leafdata())
                if (self.lldpstatsrxportframeserrors.is_set or self.lldpstatsrxportframeserrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxportframeserrors.get_name_leafdata())
                if (self.lldpstatsrxportframestotal.is_set or self.lldpstatsrxportframestotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxportframestotal.get_name_leafdata())
                if (self.lldpstatsrxporttlvsdiscardedtotal.is_set or self.lldpstatsrxporttlvsdiscardedtotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxporttlvsdiscardedtotal.get_name_leafdata())
                if (self.lldpstatsrxporttlvsunrecognizedtotal.is_set or self.lldpstatsrxporttlvsunrecognizedtotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpstatsrxporttlvsunrecognizedtotal.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpStatsRxPortNum" or name == "lldpStatsRxPortAgeoutsTotal" or name == "lldpStatsRxPortFramesDiscardedTotal" or name == "lldpStatsRxPortFramesErrors" or name == "lldpStatsRxPortFramesTotal" or name == "lldpStatsRxPortTLVsDiscardedTotal" or name == "lldpStatsRxPortTLVsUnrecognizedTotal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpStatsRxPortNum"):
                    self.lldpstatsrxportnum = value
                    self.lldpstatsrxportnum.value_namespace = name_space
                    self.lldpstatsrxportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortAgeoutsTotal"):
                    self.lldpstatsrxportageoutstotal = value
                    self.lldpstatsrxportageoutstotal.value_namespace = name_space
                    self.lldpstatsrxportageoutstotal.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortFramesDiscardedTotal"):
                    self.lldpstatsrxportframesdiscardedtotal = value
                    self.lldpstatsrxportframesdiscardedtotal.value_namespace = name_space
                    self.lldpstatsrxportframesdiscardedtotal.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortFramesErrors"):
                    self.lldpstatsrxportframeserrors = value
                    self.lldpstatsrxportframeserrors.value_namespace = name_space
                    self.lldpstatsrxportframeserrors.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortFramesTotal"):
                    self.lldpstatsrxportframestotal = value
                    self.lldpstatsrxportframestotal.value_namespace = name_space
                    self.lldpstatsrxportframestotal.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortTLVsDiscardedTotal"):
                    self.lldpstatsrxporttlvsdiscardedtotal = value
                    self.lldpstatsrxporttlvsdiscardedtotal.value_namespace = name_space
                    self.lldpstatsrxporttlvsdiscardedtotal.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpStatsRxPortTLVsUnrecognizedTotal"):
                    self.lldpstatsrxporttlvsunrecognizedtotal = value
                    self.lldpstatsrxporttlvsunrecognizedtotal.value_namespace = name_space
                    self.lldpstatsrxporttlvsunrecognizedtotal.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldpstatsrxportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpstatsrxportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpStatsRxPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpStatsRxPortEntry"):
                for c in self.lldpstatsrxportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpstatsrxporttable.Lldpstatsrxportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpstatsrxportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpStatsRxPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldplocporttable(Entity):
        """
        This table contains one or more rows per port information
        associated with the local system known to this agent.
        
        .. attribute:: lldplocportentry
        
        	Information about a particular port component.  Entries may be created and deleted in this table by the agent
        	**type**\: list of    :py:class:`Lldplocportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldplocporttable.Lldplocportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldplocporttable, self).__init__()

            self.yang_name = "lldpLocPortTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldplocportentry = YList(self)

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
                        super(LldpMib.Lldplocporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldplocporttable, self).__setattr__(name, value)


        class Lldplocportentry(Entity):
            """
            Information about a particular port component.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocportnum  <key>
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpLocPortTable
            	**type**\:  int
            
            	**range:** 1..4096
            
            .. attribute:: lldplocportdesc
            
            	The string value used to identify the 802 LAN station's port description associated with the local system.  If the local agent supports IETF RFC 2863, lldpLocPortDesc object should have the same value of ifDescr object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: lldplocportid
            
            	The string value used to identify the port component associated with a given port in the local system
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: lldplocportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpLocPortId' object
            	**type**\:   :py:class:`Lldpportidsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpportidsubtype>`
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldplocporttable.Lldplocportentry, self).__init__()

                self.yang_name = "lldpLocPortEntry"
                self.yang_parent_name = "lldpLocPortTable"

                self.lldplocportnum = YLeaf(YType.int32, "lldpLocPortNum")

                self.lldplocportdesc = YLeaf(YType.str, "lldpLocPortDesc")

                self.lldplocportid = YLeaf(YType.str, "lldpLocPortId")

                self.lldplocportidsubtype = YLeaf(YType.enumeration, "lldpLocPortIdSubtype")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldplocportnum",
                                "lldplocportdesc",
                                "lldplocportid",
                                "lldplocportidsubtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldplocporttable.Lldplocportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldplocporttable.Lldplocportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldplocportnum.is_set or
                    self.lldplocportdesc.is_set or
                    self.lldplocportid.is_set or
                    self.lldplocportidsubtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldplocportnum.yfilter != YFilter.not_set or
                    self.lldplocportdesc.yfilter != YFilter.not_set or
                    self.lldplocportid.yfilter != YFilter.not_set or
                    self.lldplocportidsubtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpLocPortEntry" + "[lldpLocPortNum='" + self.lldplocportnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpLocPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldplocportnum.is_set or self.lldplocportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocportnum.get_name_leafdata())
                if (self.lldplocportdesc.is_set or self.lldplocportdesc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocportdesc.get_name_leafdata())
                if (self.lldplocportid.is_set or self.lldplocportid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocportid.get_name_leafdata())
                if (self.lldplocportidsubtype.is_set or self.lldplocportidsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocportidsubtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpLocPortNum" or name == "lldpLocPortDesc" or name == "lldpLocPortId" or name == "lldpLocPortIdSubtype"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpLocPortNum"):
                    self.lldplocportnum = value
                    self.lldplocportnum.value_namespace = name_space
                    self.lldplocportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocPortDesc"):
                    self.lldplocportdesc = value
                    self.lldplocportdesc.value_namespace = name_space
                    self.lldplocportdesc.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocPortId"):
                    self.lldplocportid = value
                    self.lldplocportid.value_namespace = name_space
                    self.lldplocportid.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocPortIdSubtype"):
                    self.lldplocportidsubtype = value
                    self.lldplocportidsubtype.value_namespace = name_space
                    self.lldplocportidsubtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldplocportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldplocportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpLocPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpLocPortEntry"):
                for c in self.lldplocportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldplocporttable.Lldplocportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldplocportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpLocPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldplocmanaddrtable(Entity):
        """
        This table contains management address information on the
        local system known to this agent.
        
        .. attribute:: lldplocmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the system identified by a particular lldpLocChassisId.  Each management address should have distinct 'management address type' (lldpLocManAddrSubtype) and 'management address' (lldpLocManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of    :py:class:`Lldplocmanaddrentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldplocmanaddrtable.Lldplocmanaddrentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldplocmanaddrtable, self).__init__()

            self.yang_name = "lldpLocManAddrTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldplocmanaddrentry = YList(self)

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
                        super(LldpMib.Lldplocmanaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldplocmanaddrtable, self).__setattr__(name, value)


        class Lldplocmanaddrentry(Entity):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the system identified by a particular
            lldpLocChassisId.  Each management address should have
            distinct 'management address type' (lldpLocManAddrSubtype) and
            'management address' (lldpLocManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocmanaddrsubtype  <key>
            
            	The type of management address identifier encoding used in the associated 'lldpLocManagmentAddr' object
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: lldplocmanaddr  <key>
            
            	The string value used to identify the management address component associated with the local system.  The purpose of this address is to contact the management entity
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: lldpconfigmanaddrportstxenable
            
            	A set of ports that are identified by a PortList, in which each port is represented as a bit.  The corresponding local system management address instance will be transmitted on the member ports of the lldpManAddrPortsTxEnable.    The default value for lldpConfigManAddrPortsTxEnable object is empty binary string, which means no ports are specified for advertising indicated management address instance
            	**type**\:  str
            
            	**length:** 0..512
            
            .. attribute:: lldplocmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the local system
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the local system
            	**type**\:   :py:class:`Lldpmanaddrifsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpmanaddrifsubtype>`
            
            .. attribute:: lldplocmanaddrlen
            
            	The total length of the management address subtype and the management address fields in LLDPDUs transmitted by the local LLDP agent.  The management address length field is needed so that the receiving systems that do not implement SNMP will not be required to implement an iana family numbers/address length equivalency table in order to decode the management adress
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the local system agent
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldplocmanaddrtable.Lldplocmanaddrentry, self).__init__()

                self.yang_name = "lldpLocManAddrEntry"
                self.yang_parent_name = "lldpLocManAddrTable"

                self.lldplocmanaddrsubtype = YLeaf(YType.enumeration, "lldpLocManAddrSubtype")

                self.lldplocmanaddr = YLeaf(YType.str, "lldpLocManAddr")

                self.lldpconfigmanaddrportstxenable = YLeaf(YType.str, "lldpConfigManAddrPortsTxEnable")

                self.lldplocmanaddrifid = YLeaf(YType.int32, "lldpLocManAddrIfId")

                self.lldplocmanaddrifsubtype = YLeaf(YType.enumeration, "lldpLocManAddrIfSubtype")

                self.lldplocmanaddrlen = YLeaf(YType.int32, "lldpLocManAddrLen")

                self.lldplocmanaddroid = YLeaf(YType.str, "lldpLocManAddrOID")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldplocmanaddrsubtype",
                                "lldplocmanaddr",
                                "lldpconfigmanaddrportstxenable",
                                "lldplocmanaddrifid",
                                "lldplocmanaddrifsubtype",
                                "lldplocmanaddrlen",
                                "lldplocmanaddroid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldplocmanaddrtable.Lldplocmanaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldplocmanaddrtable.Lldplocmanaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldplocmanaddrsubtype.is_set or
                    self.lldplocmanaddr.is_set or
                    self.lldpconfigmanaddrportstxenable.is_set or
                    self.lldplocmanaddrifid.is_set or
                    self.lldplocmanaddrifsubtype.is_set or
                    self.lldplocmanaddrlen.is_set or
                    self.lldplocmanaddroid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldplocmanaddrsubtype.yfilter != YFilter.not_set or
                    self.lldplocmanaddr.yfilter != YFilter.not_set or
                    self.lldpconfigmanaddrportstxenable.yfilter != YFilter.not_set or
                    self.lldplocmanaddrifid.yfilter != YFilter.not_set or
                    self.lldplocmanaddrifsubtype.yfilter != YFilter.not_set or
                    self.lldplocmanaddrlen.yfilter != YFilter.not_set or
                    self.lldplocmanaddroid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpLocManAddrEntry" + "[lldpLocManAddrSubtype='" + self.lldplocmanaddrsubtype.get() + "']" + "[lldpLocManAddr='" + self.lldplocmanaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpLocManAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldplocmanaddrsubtype.is_set or self.lldplocmanaddrsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddrsubtype.get_name_leafdata())
                if (self.lldplocmanaddr.is_set or self.lldplocmanaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddr.get_name_leafdata())
                if (self.lldpconfigmanaddrportstxenable.is_set or self.lldpconfigmanaddrportstxenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpconfigmanaddrportstxenable.get_name_leafdata())
                if (self.lldplocmanaddrifid.is_set or self.lldplocmanaddrifid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddrifid.get_name_leafdata())
                if (self.lldplocmanaddrifsubtype.is_set or self.lldplocmanaddrifsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddrifsubtype.get_name_leafdata())
                if (self.lldplocmanaddrlen.is_set or self.lldplocmanaddrlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddrlen.get_name_leafdata())
                if (self.lldplocmanaddroid.is_set or self.lldplocmanaddroid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldplocmanaddroid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpLocManAddrSubtype" or name == "lldpLocManAddr" or name == "lldpConfigManAddrPortsTxEnable" or name == "lldpLocManAddrIfId" or name == "lldpLocManAddrIfSubtype" or name == "lldpLocManAddrLen" or name == "lldpLocManAddrOID"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpLocManAddrSubtype"):
                    self.lldplocmanaddrsubtype = value
                    self.lldplocmanaddrsubtype.value_namespace = name_space
                    self.lldplocmanaddrsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocManAddr"):
                    self.lldplocmanaddr = value
                    self.lldplocmanaddr.value_namespace = name_space
                    self.lldplocmanaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpConfigManAddrPortsTxEnable"):
                    self.lldpconfigmanaddrportstxenable = value
                    self.lldpconfigmanaddrportstxenable.value_namespace = name_space
                    self.lldpconfigmanaddrportstxenable.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocManAddrIfId"):
                    self.lldplocmanaddrifid = value
                    self.lldplocmanaddrifid.value_namespace = name_space
                    self.lldplocmanaddrifid.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocManAddrIfSubtype"):
                    self.lldplocmanaddrifsubtype = value
                    self.lldplocmanaddrifsubtype.value_namespace = name_space
                    self.lldplocmanaddrifsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocManAddrLen"):
                    self.lldplocmanaddrlen = value
                    self.lldplocmanaddrlen.value_namespace = name_space
                    self.lldplocmanaddrlen.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpLocManAddrOID"):
                    self.lldplocmanaddroid = value
                    self.lldplocmanaddroid.value_namespace = name_space
                    self.lldplocmanaddroid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldplocmanaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldplocmanaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpLocManAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpLocManAddrEntry"):
                for c in self.lldplocmanaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldplocmanaddrtable.Lldplocmanaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldplocmanaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpLocManAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpremtable(Entity):
        """
        This table contains one or more rows per physical network
        connection known to this agent.  The agent may wish to ensure
        that only one lldpRemEntry is present for each local port,
        or it may choose to maintain multiple lldpRemEntries for
        the same local port.
        
        The following procedure may be used to retrieve remote
        systems information updates from an LLDP agent\:
        
           1. NMS polls all tables associated with remote systems
              and keeps a local copy of the information retrieved.
              NMS polls periodically the values of the following
              objects\:
                 a. lldpStatsRemTablesInserts
                 b. lldpStatsRemTablesDeletes
                 c. lldpStatsRemTablesDrops
                 d. lldpStatsRemTablesAgeouts
                 e. lldpStatsRxPortAgeoutsTotal for all ports.
        
           2. LLDP agent updates remote systems MIB objects, and
              sends out notifications to a list of notification
              destinations.
        
           3. NMS receives the notifications and compares the new
              values of objects listed in step 1.  
        
              Periodically, NMS should poll the object
              lldpStatsRemTablesLastChangeTime to find out if anything
              has changed since the last poll.  if something has
              changed, NMS will poll the objects listed in step 1 to
              figure out what kind of changes occurred in the tables.
        
              if value of lldpStatsRemTablesInserts has changed,
              then NMS will walk all tables by employing TimeFilter
              with the last\-polled time value.  This request will
              return new objects or objects whose values are updated
              since the last poll.
        
              if value of lldpStatsRemTablesAgeouts has changed,
              then NMS will walk the lldpStatsRxPortAgeoutsTotal and
              compare the new values with previously recorded ones.
              For ports whose lldpStatsRxPortAgeoutsTotal value is
              greater than the recorded value, NMS will have to
              retrieve objects associated with those ports from
              table(s) without employing a TimeFilter (which is
              performed by specifying 0 for the TimeFilter.)
        
              lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops
              objects are provided for informational purposes.
        
        .. attribute:: lldprementry
        
        	Information about a particular physical network connection. Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of    :py:class:`Lldprementry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpremtable, self).__init__()

            self.yang_name = "lldpRemTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldprementry = YList(self)

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
                        super(LldpMib.Lldpremtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpremtable, self).__setattr__(name, value)


        class Lldprementry(Entity):
            """
            Information about a particular physical network connection.
            Entries may be created and deleted in this table by the agent,
            if a physical topology discovery process is active.
            
            .. attribute:: lldpremtimemark  <key>
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention in IETF RFC 2021 and  http\://www.ietf.org/IESG/Implementations/RFC2021\-Implementation.txt to see how TimeFilter works
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremlocalportnum  <key>
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The lldpRemLocalPortNum identifies the port on which the remote system information is received.  The value of this object is used as a port index to the lldpRemTable
            	**type**\:  int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremindex  <key>
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular connection instance, unique only for the indicated remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemIndex will wrap between reboots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremchassisid
            
            	The string value used to identify the chassis component associated with the remote system
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: lldpremchassisidsubtype
            
            	The type of encoding used to identify the chassis associated with the remote system
            	**type**\:   :py:class:`Lldpchassisidsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpchassisidsubtype>`
            
            .. attribute:: lldpremportdesc
            
            	The string value used to identify the description of the given port associated with the remote system
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: lldpremportid
            
            	The string value used to identify the port component associated with the remote system
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: lldpremportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpRemPortId' object
            	**type**\:   :py:class:`Lldpportidsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpportidsubtype>`
            
            .. attribute:: lldpremsyscapenabled
            
            	The bitmap value used to identify which system capabilities are enabled on the remote system
            	**type**\:   :py:class:`Lldpsystemcapabilitiesmap <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpsystemcapabilitiesmap>`
            
            .. attribute:: lldpremsyscapsupported
            
            	The bitmap value used to identify which system capabilities are supported on the remote system
            	**type**\:   :py:class:`Lldpsystemcapabilitiesmap <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpsystemcapabilitiesmap>`
            
            .. attribute:: lldpremsysdesc
            
            	The string value used to identify the system description of the remote system
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: lldpremsysname
            
            	The string value used to identify the system name of the remote system
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpremtable.Lldprementry, self).__init__()

                self.yang_name = "lldpRemEntry"
                self.yang_parent_name = "lldpRemTable"

                self.lldpremtimemark = YLeaf(YType.uint32, "lldpRemTimeMark")

                self.lldpremlocalportnum = YLeaf(YType.int32, "lldpRemLocalPortNum")

                self.lldpremindex = YLeaf(YType.int32, "lldpRemIndex")

                self.lldpremchassisid = YLeaf(YType.str, "lldpRemChassisId")

                self.lldpremchassisidsubtype = YLeaf(YType.enumeration, "lldpRemChassisIdSubtype")

                self.lldpremportdesc = YLeaf(YType.str, "lldpRemPortDesc")

                self.lldpremportid = YLeaf(YType.str, "lldpRemPortId")

                self.lldpremportidsubtype = YLeaf(YType.enumeration, "lldpRemPortIdSubtype")

                self.lldpremsyscapenabled = YLeaf(YType.bits, "lldpRemSysCapEnabled")

                self.lldpremsyscapsupported = YLeaf(YType.bits, "lldpRemSysCapSupported")

                self.lldpremsysdesc = YLeaf(YType.str, "lldpRemSysDesc")

                self.lldpremsysname = YLeaf(YType.str, "lldpRemSysName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpremtimemark",
                                "lldpremlocalportnum",
                                "lldpremindex",
                                "lldpremchassisid",
                                "lldpremchassisidsubtype",
                                "lldpremportdesc",
                                "lldpremportid",
                                "lldpremportidsubtype",
                                "lldpremsyscapenabled",
                                "lldpremsyscapsupported",
                                "lldpremsysdesc",
                                "lldpremsysname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpremtable.Lldprementry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpremtable.Lldprementry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpremtimemark.is_set or
                    self.lldpremlocalportnum.is_set or
                    self.lldpremindex.is_set or
                    self.lldpremchassisid.is_set or
                    self.lldpremchassisidsubtype.is_set or
                    self.lldpremportdesc.is_set or
                    self.lldpremportid.is_set or
                    self.lldpremportidsubtype.is_set or
                    self.lldpremsyscapenabled.is_set or
                    self.lldpremsyscapsupported.is_set or
                    self.lldpremsysdesc.is_set or
                    self.lldpremsysname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpremtimemark.yfilter != YFilter.not_set or
                    self.lldpremlocalportnum.yfilter != YFilter.not_set or
                    self.lldpremindex.yfilter != YFilter.not_set or
                    self.lldpremchassisid.yfilter != YFilter.not_set or
                    self.lldpremchassisidsubtype.yfilter != YFilter.not_set or
                    self.lldpremportdesc.yfilter != YFilter.not_set or
                    self.lldpremportid.yfilter != YFilter.not_set or
                    self.lldpremportidsubtype.yfilter != YFilter.not_set or
                    self.lldpremsyscapenabled.yfilter != YFilter.not_set or
                    self.lldpremsyscapsupported.yfilter != YFilter.not_set or
                    self.lldpremsysdesc.yfilter != YFilter.not_set or
                    self.lldpremsysname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpRemEntry" + "[lldpRemTimeMark='" + self.lldpremtimemark.get() + "']" + "[lldpRemLocalPortNum='" + self.lldpremlocalportnum.get() + "']" + "[lldpRemIndex='" + self.lldpremindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpRemTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpremtimemark.is_set or self.lldpremtimemark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremtimemark.get_name_leafdata())
                if (self.lldpremlocalportnum.is_set or self.lldpremlocalportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremlocalportnum.get_name_leafdata())
                if (self.lldpremindex.is_set or self.lldpremindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremindex.get_name_leafdata())
                if (self.lldpremchassisid.is_set or self.lldpremchassisid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremchassisid.get_name_leafdata())
                if (self.lldpremchassisidsubtype.is_set or self.lldpremchassisidsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremchassisidsubtype.get_name_leafdata())
                if (self.lldpremportdesc.is_set or self.lldpremportdesc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremportdesc.get_name_leafdata())
                if (self.lldpremportid.is_set or self.lldpremportid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremportid.get_name_leafdata())
                if (self.lldpremportidsubtype.is_set or self.lldpremportidsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremportidsubtype.get_name_leafdata())
                if (self.lldpremsyscapenabled.is_set or self.lldpremsyscapenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremsyscapenabled.get_name_leafdata())
                if (self.lldpremsyscapsupported.is_set or self.lldpremsyscapsupported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremsyscapsupported.get_name_leafdata())
                if (self.lldpremsysdesc.is_set or self.lldpremsysdesc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremsysdesc.get_name_leafdata())
                if (self.lldpremsysname.is_set or self.lldpremsysname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremsysname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpRemTimeMark" or name == "lldpRemLocalPortNum" or name == "lldpRemIndex" or name == "lldpRemChassisId" or name == "lldpRemChassisIdSubtype" or name == "lldpRemPortDesc" or name == "lldpRemPortId" or name == "lldpRemPortIdSubtype" or name == "lldpRemSysCapEnabled" or name == "lldpRemSysCapSupported" or name == "lldpRemSysDesc" or name == "lldpRemSysName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpRemTimeMark"):
                    self.lldpremtimemark = value
                    self.lldpremtimemark.value_namespace = name_space
                    self.lldpremtimemark.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemLocalPortNum"):
                    self.lldpremlocalportnum = value
                    self.lldpremlocalportnum.value_namespace = name_space
                    self.lldpremlocalportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemIndex"):
                    self.lldpremindex = value
                    self.lldpremindex.value_namespace = name_space
                    self.lldpremindex.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemChassisId"):
                    self.lldpremchassisid = value
                    self.lldpremchassisid.value_namespace = name_space
                    self.lldpremchassisid.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemChassisIdSubtype"):
                    self.lldpremchassisidsubtype = value
                    self.lldpremchassisidsubtype.value_namespace = name_space
                    self.lldpremchassisidsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemPortDesc"):
                    self.lldpremportdesc = value
                    self.lldpremportdesc.value_namespace = name_space
                    self.lldpremportdesc.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemPortId"):
                    self.lldpremportid = value
                    self.lldpremportid.value_namespace = name_space
                    self.lldpremportid.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemPortIdSubtype"):
                    self.lldpremportidsubtype = value
                    self.lldpremportidsubtype.value_namespace = name_space
                    self.lldpremportidsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemSysCapEnabled"):
                    self.lldpremsyscapenabled[value] = True
                if(value_path == "lldpRemSysCapSupported"):
                    self.lldpremsyscapsupported[value] = True
                if(value_path == "lldpRemSysDesc"):
                    self.lldpremsysdesc = value
                    self.lldpremsysdesc.value_namespace = name_space
                    self.lldpremsysdesc.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemSysName"):
                    self.lldpremsysname = value
                    self.lldpremsysname.value_namespace = name_space
                    self.lldpremsysname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldprementry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldprementry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpRemTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpRemEntry"):
                for c in self.lldprementry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpremtable.Lldprementry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldprementry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpRemEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpremmanaddrtable(Entity):
        """
        This table contains one or more rows per management address
        information on the remote system learned on a particular port
        contained in the local chassis known to this agent.
        
        .. attribute:: lldpremmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the remote system identified by a particular lldpRemIndex whose information is received on lldpRemLocalPortNum of the local system.  Each management address should have distinct 'management address type' (lldpRemManAddrSubtype) and 'management address' (lldpRemManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of    :py:class:`Lldpremmanaddrentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremmanaddrtable.Lldpremmanaddrentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpremmanaddrtable, self).__init__()

            self.yang_name = "lldpRemManAddrTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpremmanaddrentry = YList(self)

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
                        super(LldpMib.Lldpremmanaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpremmanaddrtable, self).__setattr__(name, value)


        class Lldpremmanaddrentry(Entity):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the remote system identified by a particular
            lldpRemIndex whose information is received on
            lldpRemLocalPortNum of the local system.  Each management
            address should have distinct 'management address
            type' (lldpRemManAddrSubtype) and 'management address'
            (lldpRemManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremtimemark  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremmanaddrsubtype  <key>
            
            	The type of management address identifier encoding used in the associated 'lldpRemManagmentAddr' object
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: lldpremmanaddr  <key>
            
            	The string value used to identify the management address component associated with the remote system.  The purpose of this address is to contact the management entity
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: lldpremmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the remote system
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldpremmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the remote system
            	**type**\:   :py:class:`Lldpmanaddrifsubtype <ydk.models.cisco_ios_xe.LLDP_MIB.Lldpmanaddrifsubtype>`
            
            .. attribute:: lldpremmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the remote system agent
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpremmanaddrtable.Lldpremmanaddrentry, self).__init__()

                self.yang_name = "lldpRemManAddrEntry"
                self.yang_parent_name = "lldpRemManAddrTable"

                self.lldpremtimemark = YLeaf(YType.str, "lldpRemTimeMark")

                self.lldpremlocalportnum = YLeaf(YType.str, "lldpRemLocalPortNum")

                self.lldpremindex = YLeaf(YType.str, "lldpRemIndex")

                self.lldpremmanaddrsubtype = YLeaf(YType.enumeration, "lldpRemManAddrSubtype")

                self.lldpremmanaddr = YLeaf(YType.str, "lldpRemManAddr")

                self.lldpremmanaddrifid = YLeaf(YType.int32, "lldpRemManAddrIfId")

                self.lldpremmanaddrifsubtype = YLeaf(YType.enumeration, "lldpRemManAddrIfSubtype")

                self.lldpremmanaddroid = YLeaf(YType.str, "lldpRemManAddrOID")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpremtimemark",
                                "lldpremlocalportnum",
                                "lldpremindex",
                                "lldpremmanaddrsubtype",
                                "lldpremmanaddr",
                                "lldpremmanaddrifid",
                                "lldpremmanaddrifsubtype",
                                "lldpremmanaddroid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpremmanaddrtable.Lldpremmanaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpremmanaddrtable.Lldpremmanaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpremtimemark.is_set or
                    self.lldpremlocalportnum.is_set or
                    self.lldpremindex.is_set or
                    self.lldpremmanaddrsubtype.is_set or
                    self.lldpremmanaddr.is_set or
                    self.lldpremmanaddrifid.is_set or
                    self.lldpremmanaddrifsubtype.is_set or
                    self.lldpremmanaddroid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpremtimemark.yfilter != YFilter.not_set or
                    self.lldpremlocalportnum.yfilter != YFilter.not_set or
                    self.lldpremindex.yfilter != YFilter.not_set or
                    self.lldpremmanaddrsubtype.yfilter != YFilter.not_set or
                    self.lldpremmanaddr.yfilter != YFilter.not_set or
                    self.lldpremmanaddrifid.yfilter != YFilter.not_set or
                    self.lldpremmanaddrifsubtype.yfilter != YFilter.not_set or
                    self.lldpremmanaddroid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpRemManAddrEntry" + "[lldpRemTimeMark='" + self.lldpremtimemark.get() + "']" + "[lldpRemLocalPortNum='" + self.lldpremlocalportnum.get() + "']" + "[lldpRemIndex='" + self.lldpremindex.get() + "']" + "[lldpRemManAddrSubtype='" + self.lldpremmanaddrsubtype.get() + "']" + "[lldpRemManAddr='" + self.lldpremmanaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpRemManAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpremtimemark.is_set or self.lldpremtimemark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremtimemark.get_name_leafdata())
                if (self.lldpremlocalportnum.is_set or self.lldpremlocalportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremlocalportnum.get_name_leafdata())
                if (self.lldpremindex.is_set or self.lldpremindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremindex.get_name_leafdata())
                if (self.lldpremmanaddrsubtype.is_set or self.lldpremmanaddrsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremmanaddrsubtype.get_name_leafdata())
                if (self.lldpremmanaddr.is_set or self.lldpremmanaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremmanaddr.get_name_leafdata())
                if (self.lldpremmanaddrifid.is_set or self.lldpremmanaddrifid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremmanaddrifid.get_name_leafdata())
                if (self.lldpremmanaddrifsubtype.is_set or self.lldpremmanaddrifsubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremmanaddrifsubtype.get_name_leafdata())
                if (self.lldpremmanaddroid.is_set or self.lldpremmanaddroid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremmanaddroid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpRemTimeMark" or name == "lldpRemLocalPortNum" or name == "lldpRemIndex" or name == "lldpRemManAddrSubtype" or name == "lldpRemManAddr" or name == "lldpRemManAddrIfId" or name == "lldpRemManAddrIfSubtype" or name == "lldpRemManAddrOID"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpRemTimeMark"):
                    self.lldpremtimemark = value
                    self.lldpremtimemark.value_namespace = name_space
                    self.lldpremtimemark.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemLocalPortNum"):
                    self.lldpremlocalportnum = value
                    self.lldpremlocalportnum.value_namespace = name_space
                    self.lldpremlocalportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemIndex"):
                    self.lldpremindex = value
                    self.lldpremindex.value_namespace = name_space
                    self.lldpremindex.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemManAddrSubtype"):
                    self.lldpremmanaddrsubtype = value
                    self.lldpremmanaddrsubtype.value_namespace = name_space
                    self.lldpremmanaddrsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemManAddr"):
                    self.lldpremmanaddr = value
                    self.lldpremmanaddr.value_namespace = name_space
                    self.lldpremmanaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemManAddrIfId"):
                    self.lldpremmanaddrifid = value
                    self.lldpremmanaddrifid.value_namespace = name_space
                    self.lldpremmanaddrifid.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemManAddrIfSubtype"):
                    self.lldpremmanaddrifsubtype = value
                    self.lldpremmanaddrifsubtype.value_namespace = name_space
                    self.lldpremmanaddrifsubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemManAddrOID"):
                    self.lldpremmanaddroid = value
                    self.lldpremmanaddroid.value_namespace = name_space
                    self.lldpremmanaddroid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldpremmanaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpremmanaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpRemManAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpRemManAddrEntry"):
                for c in self.lldpremmanaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpremmanaddrtable.Lldpremmanaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpremmanaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpRemManAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpremunknowntlvtable(Entity):
        """
        This table contains information about an incoming TLV which
        is not recognized by the receiving LLDP agent.  The TLV may
        be from a later version of the basic management set.
        
        This table should only contain TLVs that are found in
        a single LLDP frame.  Entries in this table, associated
        with an MAC service access point (MSAP, the access point
        for MAC services provided to the LCC sublayer, defined
        in IEEE 100, which is also identified with a particular
        lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with
        most recently received unrecognized TLV from the same MSAP,
        or they will naturally age out when the rxInfoTTL timer
        (associated with the MSAP) expires.
        
        .. attribute:: lldpremunknowntlventry
        
        	Information about an unrecognized TLV received from a physical network connection.  Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of    :py:class:`Lldpremunknowntlventry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremunknowntlvtable.Lldpremunknowntlventry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpremunknowntlvtable, self).__init__()

            self.yang_name = "lldpRemUnknownTLVTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpremunknowntlventry = YList(self)

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
                        super(LldpMib.Lldpremunknowntlvtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpremunknowntlvtable, self).__setattr__(name, value)


        class Lldpremunknowntlventry(Entity):
            """
            Information about an unrecognized TLV received from a
            physical network connection.  Entries may be created and
            deleted in this table by the agent, if a physical topology
            discovery process is active.
            
            .. attribute:: lldpremtimemark  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremunknowntlvtype  <key>
            
            	This object represents the value extracted from the type field of the TLV
            	**type**\:  int
            
            	**range:** 9..126
            
            .. attribute:: lldpremunknowntlvinfo
            
            	This object represents the value extracted from the value field of the TLV
            	**type**\:  str
            
            	**length:** 0..511
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpremunknowntlvtable.Lldpremunknowntlventry, self).__init__()

                self.yang_name = "lldpRemUnknownTLVEntry"
                self.yang_parent_name = "lldpRemUnknownTLVTable"

                self.lldpremtimemark = YLeaf(YType.str, "lldpRemTimeMark")

                self.lldpremlocalportnum = YLeaf(YType.str, "lldpRemLocalPortNum")

                self.lldpremindex = YLeaf(YType.str, "lldpRemIndex")

                self.lldpremunknowntlvtype = YLeaf(YType.int32, "lldpRemUnknownTLVType")

                self.lldpremunknowntlvinfo = YLeaf(YType.str, "lldpRemUnknownTLVInfo")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpremtimemark",
                                "lldpremlocalportnum",
                                "lldpremindex",
                                "lldpremunknowntlvtype",
                                "lldpremunknowntlvinfo") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpremunknowntlvtable.Lldpremunknowntlventry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpremunknowntlvtable.Lldpremunknowntlventry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpremtimemark.is_set or
                    self.lldpremlocalportnum.is_set or
                    self.lldpremindex.is_set or
                    self.lldpremunknowntlvtype.is_set or
                    self.lldpremunknowntlvinfo.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpremtimemark.yfilter != YFilter.not_set or
                    self.lldpremlocalportnum.yfilter != YFilter.not_set or
                    self.lldpremindex.yfilter != YFilter.not_set or
                    self.lldpremunknowntlvtype.yfilter != YFilter.not_set or
                    self.lldpremunknowntlvinfo.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpRemUnknownTLVEntry" + "[lldpRemTimeMark='" + self.lldpremtimemark.get() + "']" + "[lldpRemLocalPortNum='" + self.lldpremlocalportnum.get() + "']" + "[lldpRemIndex='" + self.lldpremindex.get() + "']" + "[lldpRemUnknownTLVType='" + self.lldpremunknowntlvtype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpRemUnknownTLVTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpremtimemark.is_set or self.lldpremtimemark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremtimemark.get_name_leafdata())
                if (self.lldpremlocalportnum.is_set or self.lldpremlocalportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremlocalportnum.get_name_leafdata())
                if (self.lldpremindex.is_set or self.lldpremindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremindex.get_name_leafdata())
                if (self.lldpremunknowntlvtype.is_set or self.lldpremunknowntlvtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremunknowntlvtype.get_name_leafdata())
                if (self.lldpremunknowntlvinfo.is_set or self.lldpremunknowntlvinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremunknowntlvinfo.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpRemTimeMark" or name == "lldpRemLocalPortNum" or name == "lldpRemIndex" or name == "lldpRemUnknownTLVType" or name == "lldpRemUnknownTLVInfo"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpRemTimeMark"):
                    self.lldpremtimemark = value
                    self.lldpremtimemark.value_namespace = name_space
                    self.lldpremtimemark.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemLocalPortNum"):
                    self.lldpremlocalportnum = value
                    self.lldpremlocalportnum.value_namespace = name_space
                    self.lldpremlocalportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemIndex"):
                    self.lldpremindex = value
                    self.lldpremindex.value_namespace = name_space
                    self.lldpremindex.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemUnknownTLVType"):
                    self.lldpremunknowntlvtype = value
                    self.lldpremunknowntlvtype.value_namespace = name_space
                    self.lldpremunknowntlvtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemUnknownTLVInfo"):
                    self.lldpremunknowntlvinfo = value
                    self.lldpremunknowntlvinfo.value_namespace = name_space
                    self.lldpremunknowntlvinfo.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldpremunknowntlventry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpremunknowntlventry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpRemUnknownTLVTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpRemUnknownTLVEntry"):
                for c in self.lldpremunknowntlventry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpremunknowntlvtable.Lldpremunknowntlventry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpremunknowntlventry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpRemUnknownTLVEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lldpremorgdefinfotable(Entity):
        """
        This table contains one or more rows per physical network
        connection which advertises the organizationally defined
        information.
        
        Note that this table contains one or more rows of
        organizationally defined information that is not recognized
        by the local agent.
        
        If the local system is capable of recognizing any
        organizationally defined information, appropriate extension
        MIBs from the organization should be used for information
        retrieval.
        
        .. attribute:: lldpremorgdefinfoentry
        
        	Information about the unrecognized organizationally defined information advertised by the remote system. The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and lldpRemOrgDefInfoIndex are indexes to this table.  If there is an lldpRemOrgDefInfoEntry associated with a particular remote system identified by the lldpRemLocalPortNum and lldpRemIndex, there must be an lldpRemEntry associated with the same instance (i.e, using same indexes.)  When the lldpRemEntry for the same index is removed from the lldpRemTable, the associated lldpRemOrgDefInfoEntry should be removed from the lldpRemOrgDefInfoTable.  Entries may be created and deleted in this table by the agent
        	**type**\: list of    :py:class:`Lldpremorgdefinfoentry <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremorgdefinfotable.Lldpremorgdefinfoentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LldpMib.Lldpremorgdefinfotable, self).__init__()

            self.yang_name = "lldpRemOrgDefInfoTable"
            self.yang_parent_name = "LLDP-MIB"

            self.lldpremorgdefinfoentry = YList(self)

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
                        super(LldpMib.Lldpremorgdefinfotable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpMib.Lldpremorgdefinfotable, self).__setattr__(name, value)


        class Lldpremorgdefinfoentry(Entity):
            """
            Information about the unrecognized organizationally
            defined information advertised by the remote system.
            The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex,
            lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and
            lldpRemOrgDefInfoIndex are indexes to this table.  If there is
            an lldpRemOrgDefInfoEntry associated with a particular remote
            system identified by the lldpRemLocalPortNum and lldpRemIndex,
            there must be an lldpRemEntry associated with the same
            instance (i.e, using same indexes.)  When the lldpRemEntry
            for the same index is removed from the lldpRemTable, the
            associated lldpRemOrgDefInfoEntry should be removed from
            the lldpRemOrgDefInfoTable.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremtimemark  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LldpMib.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremorgdefinfooui  <key>
            
            	The Organizationally Unique Identifier (OUI), as defined in IEEE std 802\-2001, is a 24 bit (three octets) globally unique assigned number referenced by various standards, of the information received from the remote system
            	**type**\:  str
            
            	**length:** 3
            
            .. attribute:: lldpremorgdefinfosubtype  <key>
            
            	The integer value used to identify the subtype of the organizationally defined information received from the remote system.  The subtype value is required to identify different instances of organizationally defined information that could not be retrieved without a unique identifier that indicates the particular type of information contained in the information string
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: lldpremorgdefinfoindex  <key>
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular unrecognized organizationally defined information instance, unique only for the lldpRemOrgDefInfoOUI and lldpRemOrgDefInfoSubtype from the same remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemOrgDefInfoIndex will wrap between reboots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremorgdefinfo
            
            	The string value used to identify the organizationally defined information of the remote system.  The encoding for this object should be as defined for SnmpAdminString TC
            	**type**\:  str
            
            	**length:** 0..507
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LldpMib.Lldpremorgdefinfotable.Lldpremorgdefinfoentry, self).__init__()

                self.yang_name = "lldpRemOrgDefInfoEntry"
                self.yang_parent_name = "lldpRemOrgDefInfoTable"

                self.lldpremtimemark = YLeaf(YType.str, "lldpRemTimeMark")

                self.lldpremlocalportnum = YLeaf(YType.str, "lldpRemLocalPortNum")

                self.lldpremindex = YLeaf(YType.str, "lldpRemIndex")

                self.lldpremorgdefinfooui = YLeaf(YType.str, "lldpRemOrgDefInfoOUI")

                self.lldpremorgdefinfosubtype = YLeaf(YType.int32, "lldpRemOrgDefInfoSubtype")

                self.lldpremorgdefinfoindex = YLeaf(YType.int32, "lldpRemOrgDefInfoIndex")

                self.lldpremorgdefinfo = YLeaf(YType.str, "lldpRemOrgDefInfo")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lldpremtimemark",
                                "lldpremlocalportnum",
                                "lldpremindex",
                                "lldpremorgdefinfooui",
                                "lldpremorgdefinfosubtype",
                                "lldpremorgdefinfoindex",
                                "lldpremorgdefinfo") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpMib.Lldpremorgdefinfotable.Lldpremorgdefinfoentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpMib.Lldpremorgdefinfotable.Lldpremorgdefinfoentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.lldpremtimemark.is_set or
                    self.lldpremlocalportnum.is_set or
                    self.lldpremindex.is_set or
                    self.lldpremorgdefinfooui.is_set or
                    self.lldpremorgdefinfosubtype.is_set or
                    self.lldpremorgdefinfoindex.is_set or
                    self.lldpremorgdefinfo.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lldpremtimemark.yfilter != YFilter.not_set or
                    self.lldpremlocalportnum.yfilter != YFilter.not_set or
                    self.lldpremindex.yfilter != YFilter.not_set or
                    self.lldpremorgdefinfooui.yfilter != YFilter.not_set or
                    self.lldpremorgdefinfosubtype.yfilter != YFilter.not_set or
                    self.lldpremorgdefinfoindex.yfilter != YFilter.not_set or
                    self.lldpremorgdefinfo.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lldpRemOrgDefInfoEntry" + "[lldpRemTimeMark='" + self.lldpremtimemark.get() + "']" + "[lldpRemLocalPortNum='" + self.lldpremlocalportnum.get() + "']" + "[lldpRemIndex='" + self.lldpremindex.get() + "']" + "[lldpRemOrgDefInfoOUI='" + self.lldpremorgdefinfooui.get() + "']" + "[lldpRemOrgDefInfoSubtype='" + self.lldpremorgdefinfosubtype.get() + "']" + "[lldpRemOrgDefInfoIndex='" + self.lldpremorgdefinfoindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "LLDP-MIB:LLDP-MIB/lldpRemOrgDefInfoTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lldpremtimemark.is_set or self.lldpremtimemark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremtimemark.get_name_leafdata())
                if (self.lldpremlocalportnum.is_set or self.lldpremlocalportnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremlocalportnum.get_name_leafdata())
                if (self.lldpremindex.is_set or self.lldpremindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremindex.get_name_leafdata())
                if (self.lldpremorgdefinfooui.is_set or self.lldpremorgdefinfooui.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremorgdefinfooui.get_name_leafdata())
                if (self.lldpremorgdefinfosubtype.is_set or self.lldpremorgdefinfosubtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremorgdefinfosubtype.get_name_leafdata())
                if (self.lldpremorgdefinfoindex.is_set or self.lldpremorgdefinfoindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremorgdefinfoindex.get_name_leafdata())
                if (self.lldpremorgdefinfo.is_set or self.lldpremorgdefinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldpremorgdefinfo.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lldpRemTimeMark" or name == "lldpRemLocalPortNum" or name == "lldpRemIndex" or name == "lldpRemOrgDefInfoOUI" or name == "lldpRemOrgDefInfoSubtype" or name == "lldpRemOrgDefInfoIndex" or name == "lldpRemOrgDefInfo"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lldpRemTimeMark"):
                    self.lldpremtimemark = value
                    self.lldpremtimemark.value_namespace = name_space
                    self.lldpremtimemark.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemLocalPortNum"):
                    self.lldpremlocalportnum = value
                    self.lldpremlocalportnum.value_namespace = name_space
                    self.lldpremlocalportnum.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemIndex"):
                    self.lldpremindex = value
                    self.lldpremindex.value_namespace = name_space
                    self.lldpremindex.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemOrgDefInfoOUI"):
                    self.lldpremorgdefinfooui = value
                    self.lldpremorgdefinfooui.value_namespace = name_space
                    self.lldpremorgdefinfooui.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemOrgDefInfoSubtype"):
                    self.lldpremorgdefinfosubtype = value
                    self.lldpremorgdefinfosubtype.value_namespace = name_space
                    self.lldpremorgdefinfosubtype.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemOrgDefInfoIndex"):
                    self.lldpremorgdefinfoindex = value
                    self.lldpremorgdefinfoindex.value_namespace = name_space
                    self.lldpremorgdefinfoindex.value_namespace_prefix = name_space_prefix
                if(value_path == "lldpRemOrgDefInfo"):
                    self.lldpremorgdefinfo = value
                    self.lldpremorgdefinfo.value_namespace = name_space
                    self.lldpremorgdefinfo.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lldpremorgdefinfoentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lldpremorgdefinfoentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldpRemOrgDefInfoTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "LLDP-MIB:LLDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lldpRemOrgDefInfoEntry"):
                for c in self.lldpremorgdefinfoentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LldpMib.Lldpremorgdefinfotable.Lldpremorgdefinfoentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lldpremorgdefinfoentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lldpRemOrgDefInfoEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.lldpconfiguration is not None and self.lldpconfiguration.has_data()) or
            (self.lldplocalsystemdata is not None and self.lldplocalsystemdata.has_data()) or
            (self.lldplocmanaddrtable is not None and self.lldplocmanaddrtable.has_data()) or
            (self.lldplocporttable is not None and self.lldplocporttable.has_data()) or
            (self.lldpportconfigtable is not None and self.lldpportconfigtable.has_data()) or
            (self.lldpremmanaddrtable is not None and self.lldpremmanaddrtable.has_data()) or
            (self.lldpremorgdefinfotable is not None and self.lldpremorgdefinfotable.has_data()) or
            (self.lldpremtable is not None and self.lldpremtable.has_data()) or
            (self.lldpremunknowntlvtable is not None and self.lldpremunknowntlvtable.has_data()) or
            (self.lldpstatistics is not None and self.lldpstatistics.has_data()) or
            (self.lldpstatsrxporttable is not None and self.lldpstatsrxporttable.has_data()) or
            (self.lldpstatstxporttable is not None and self.lldpstatstxporttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.lldpconfiguration is not None and self.lldpconfiguration.has_operation()) or
            (self.lldplocalsystemdata is not None and self.lldplocalsystemdata.has_operation()) or
            (self.lldplocmanaddrtable is not None and self.lldplocmanaddrtable.has_operation()) or
            (self.lldplocporttable is not None and self.lldplocporttable.has_operation()) or
            (self.lldpportconfigtable is not None and self.lldpportconfigtable.has_operation()) or
            (self.lldpremmanaddrtable is not None and self.lldpremmanaddrtable.has_operation()) or
            (self.lldpremorgdefinfotable is not None and self.lldpremorgdefinfotable.has_operation()) or
            (self.lldpremtable is not None and self.lldpremtable.has_operation()) or
            (self.lldpremunknowntlvtable is not None and self.lldpremunknowntlvtable.has_operation()) or
            (self.lldpstatistics is not None and self.lldpstatistics.has_operation()) or
            (self.lldpstatsrxporttable is not None and self.lldpstatsrxporttable.has_operation()) or
            (self.lldpstatstxporttable is not None and self.lldpstatstxporttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "LLDP-MIB:LLDP-MIB" + path_buffer

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

        if (child_yang_name == "lldpConfiguration"):
            if (self.lldpconfiguration is None):
                self.lldpconfiguration = LldpMib.Lldpconfiguration()
                self.lldpconfiguration.parent = self
                self._children_name_map["lldpconfiguration"] = "lldpConfiguration"
            return self.lldpconfiguration

        if (child_yang_name == "lldpLocalSystemData"):
            if (self.lldplocalsystemdata is None):
                self.lldplocalsystemdata = LldpMib.Lldplocalsystemdata()
                self.lldplocalsystemdata.parent = self
                self._children_name_map["lldplocalsystemdata"] = "lldpLocalSystemData"
            return self.lldplocalsystemdata

        if (child_yang_name == "lldpLocManAddrTable"):
            if (self.lldplocmanaddrtable is None):
                self.lldplocmanaddrtable = LldpMib.Lldplocmanaddrtable()
                self.lldplocmanaddrtable.parent = self
                self._children_name_map["lldplocmanaddrtable"] = "lldpLocManAddrTable"
            return self.lldplocmanaddrtable

        if (child_yang_name == "lldpLocPortTable"):
            if (self.lldplocporttable is None):
                self.lldplocporttable = LldpMib.Lldplocporttable()
                self.lldplocporttable.parent = self
                self._children_name_map["lldplocporttable"] = "lldpLocPortTable"
            return self.lldplocporttable

        if (child_yang_name == "lldpPortConfigTable"):
            if (self.lldpportconfigtable is None):
                self.lldpportconfigtable = LldpMib.Lldpportconfigtable()
                self.lldpportconfigtable.parent = self
                self._children_name_map["lldpportconfigtable"] = "lldpPortConfigTable"
            return self.lldpportconfigtable

        if (child_yang_name == "lldpRemManAddrTable"):
            if (self.lldpremmanaddrtable is None):
                self.lldpremmanaddrtable = LldpMib.Lldpremmanaddrtable()
                self.lldpremmanaddrtable.parent = self
                self._children_name_map["lldpremmanaddrtable"] = "lldpRemManAddrTable"
            return self.lldpremmanaddrtable

        if (child_yang_name == "lldpRemOrgDefInfoTable"):
            if (self.lldpremorgdefinfotable is None):
                self.lldpremorgdefinfotable = LldpMib.Lldpremorgdefinfotable()
                self.lldpremorgdefinfotable.parent = self
                self._children_name_map["lldpremorgdefinfotable"] = "lldpRemOrgDefInfoTable"
            return self.lldpremorgdefinfotable

        if (child_yang_name == "lldpRemTable"):
            if (self.lldpremtable is None):
                self.lldpremtable = LldpMib.Lldpremtable()
                self.lldpremtable.parent = self
                self._children_name_map["lldpremtable"] = "lldpRemTable"
            return self.lldpremtable

        if (child_yang_name == "lldpRemUnknownTLVTable"):
            if (self.lldpremunknowntlvtable is None):
                self.lldpremunknowntlvtable = LldpMib.Lldpremunknowntlvtable()
                self.lldpremunknowntlvtable.parent = self
                self._children_name_map["lldpremunknowntlvtable"] = "lldpRemUnknownTLVTable"
            return self.lldpremunknowntlvtable

        if (child_yang_name == "lldpStatistics"):
            if (self.lldpstatistics is None):
                self.lldpstatistics = LldpMib.Lldpstatistics()
                self.lldpstatistics.parent = self
                self._children_name_map["lldpstatistics"] = "lldpStatistics"
            return self.lldpstatistics

        if (child_yang_name == "lldpStatsRxPortTable"):
            if (self.lldpstatsrxporttable is None):
                self.lldpstatsrxporttable = LldpMib.Lldpstatsrxporttable()
                self.lldpstatsrxporttable.parent = self
                self._children_name_map["lldpstatsrxporttable"] = "lldpStatsRxPortTable"
            return self.lldpstatsrxporttable

        if (child_yang_name == "lldpStatsTxPortTable"):
            if (self.lldpstatstxporttable is None):
                self.lldpstatstxporttable = LldpMib.Lldpstatstxporttable()
                self.lldpstatstxporttable.parent = self
                self._children_name_map["lldpstatstxporttable"] = "lldpStatsTxPortTable"
            return self.lldpstatstxporttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "lldpConfiguration" or name == "lldpLocalSystemData" or name == "lldpLocManAddrTable" or name == "lldpLocPortTable" or name == "lldpPortConfigTable" or name == "lldpRemManAddrTable" or name == "lldpRemOrgDefInfoTable" or name == "lldpRemTable" or name == "lldpRemUnknownTLVTable" or name == "lldpStatistics" or name == "lldpStatsRxPortTable" or name == "lldpStatsTxPortTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = LldpMib()
        return self._top_entity

